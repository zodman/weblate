# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2013 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <http://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.shortcuts import render_to_response, get_object_or_404
from django.utils.translation import ugettext as _
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import formats
import uuid
import time

from trans.models import SubProject, Unit, Suggestion, Change, Comment
from trans.forms import (
    TranslationForm, SearchForm,
    MergeForm, AutoForm, ReviewForm,
    AntispamForm, CommentForm
)
from trans.views.helper import get_translation
from trans.checks import CHECKS
from trans.util import join_plural
from accounts.models import Profile, send_notification_email
import weblate


def get_filter_name(rqtype):
    '''
    Returns name of current filter.
    '''
    if rqtype == 'fuzzy':
        return _('Fuzzy strings')
    elif rqtype == 'untranslated':
        return _('Untranslated strings')
    elif rqtype == 'suggestions':
        return _('Strings with suggestions')
    elif rqtype == 'allchecks':
        return _('Strings with any failing checks')
    elif rqtype in CHECKS:
        return CHECKS[rqtype].name
    else:
        return None


def cleanup_session(session):
    '''
    Deletes old search results from session storage.
    '''
    now = int(time.time())
    for key in session.keys():
        if key.startswith('search_') and session[key]['ttl'] < now:
            del session[key]


def search(translation, request):
    '''
    Performs search or retuns cached search results.
    '''

    # Already performed search
    if 'sid' in request.GET:
        # Grab from session storage
        search_id = 'search_%s' % request.GET['sid']

        # Check if we know the search
        if search_id not in request.session:
            messages.error(request, _('Invalid search string!'))
            return HttpResponseRedirect(translation.get_absolute_url())

        return request.session[search_id]

    # Possible new search
    rqtype = request.GET.get('type', 'all')
    search_query = ''

    search_form = SearchForm(request.GET)
    review_form = ReviewForm(request.GET)

    if review_form.is_valid():
        # Review
        allunits = translation.unit_set.review(
            review_form.cleaned_data['date'],
            request.user
        )

        formatted_date = formats.date_format(
            review_form.cleaned_data['date'],
            'SHORT_DATE_FORMAT'
        )
        name = _('Review of translations since %s') % formatted_date
    elif search_form.is_valid():
        # Apply search conditions
        allunits = translation.unit_set.search(
            search_form.cleaned_data['search'],
            search_form.cleaned_data['q'],
            search_form.cleaned_data['src'],
            search_form.cleaned_data['ctx'],
            search_form.cleaned_data['tgt'],
        )

        name = _('Search for "%s"') % search_query
    else:
        # Filtering by type
        allunits = translation.unit_set.filter_type(rqtype, translation)

        name = get_filter_name(rqtype)

    # Grab unit IDs
    unit_ids = list(allunits.values_list('id', flat=True))

    # Check empty search results
    if len(unit_ids) == 0:
        messages.warning(request, _('No string matched your search!'))
        return HttpResponseRedirect(translation.get_absolute_url())

    # Remove old search results
    cleanup_session(request.session)

    # Store in cache and return
    search_id = str(uuid.uuid1())
    search_result = {
        'name': name,
        'ids': unit_ids,
        'search_id': search_id,
        'ttl': int(time.time()) + 86400,
    }

    request.session['search_%s' % search_id] = search_result

    return search_result


def handle_translate(obj, request, profile, user_locked,
                     this_unit_url, next_unit_url):
    '''
    Saves translation or suggestion to database and backend.
    '''
    # Antispam protection
    if not request.user.is_authenticated():
        antispam = AntispamForm(request.POST)
        if not antispam.is_valid():
            # Silently redirect to next entry
            return HttpResponseRedirect(next_unit_url)

    form = TranslationForm(request.POST)
    if not form.is_valid():
        return
    # Check whether translation is not outdated
    obj.check_sync()
    try:
        try:
            unit = Unit.objects.get(
                checksum=form.cleaned_data['checksum'],
                translation=obj
            )
        except Unit.MultipleObjectsReturned:
            # Possible temporary inconsistency caused by ongoing update
            # of repo, let's pretend everyting is okay
            unit = Unit.objects.filter(
                checksum=form.cleaned_data['checksum'],
                translation=obj
            )[0]
        if 'suggest' in request.POST:
            # Handle suggesion saving
            user = request.user
            if form.cleaned_data['target'][0] == '':
                messages.error(request, _('Your suggestion is empty!'))
                # Stay on same entry
                return HttpResponseRedirect(this_unit_url)
            # Invite user to become translator if there is nobody else
            recent_changes = Change.objects.content().filter(
                translation=unit.translation,
            ).exclude(
                user=None
            )
            if not recent_changes.exists():
                messages.info(request, _(
                    'There is currently no active translator for this '
                    'translation, please consider becoming a translator '
                    'as your suggestion might otherwise remain unreviewed.'
                ))
            # Create the suggestion
            unit.add_suggestion(
                join_plural(form.cleaned_data['target']),
                user,
                profile
            )
        elif not request.user.is_authenticated():
            # We accept translations only from authenticated
            messages.error(
                request,
                _('You need to log in to be able to save translations!')
            )
        elif not request.user.has_perm('trans.save_translation'):
            # Need privilege to save
            messages.error(
                request,
                _('You don\'t have privileges to save translations!')
            )
        elif not user_locked:
            # Remember old checks
            oldchecks = set(
                unit.active_checks().values_list('check', flat=True)
            )
            # Update unit and save it
            unit.target = join_plural(form.cleaned_data['target'])
            unit.fuzzy = form.cleaned_data['fuzzy']
            saved = unit.save_backend(request)

            if saved:
                # Get new set of checks
                newchecks = set(
                    unit.active_checks().values_list('check', flat=True)
                )
                # Did we introduce any new failures?
                if newchecks > oldchecks:
                    # Show message to user
                    messages.error(
                        request,
                        _('Some checks have failed on your translation!')
                    )
                    # Stay on same entry
                    return HttpResponseRedirect(this_unit_url)

        # Redirect to next entry
        return HttpResponseRedirect(next_unit_url)
    except Unit.DoesNotExist:
        weblate.logger.error(
            'message %s disappeared!',
            form.cleaned_data['checksum']
        )
        messages.error(
            request,
            _('Message you wanted to translate is no longer available!')
        )


def handle_merge(obj, request, profile, next_unit_url):
    '''
    Handles unit merging.
    '''
    if not request.user.has_perm('trans.save_translation'):
        # Need privilege to save
        messages.error(
            request,
            _('You don\'t have privileges to save translations!')
        )
    else:
        try:
            mergeform = MergeForm(request.GET)
            if mergeform.is_valid():
                try:
                    unit = Unit.objects.get(
                        checksum=mergeform.cleaned_data['checksum'],
                        translation=obj
                    )
                except Unit.MultipleObjectsReturned:
                    # Possible temporary inconsistency caused by ongoing
                    # update of repo, let's pretend everyting is okay
                    unit = Unit.objects.filter(
                        checksum=mergeform.cleaned_data['checksum'],
                        translation=obj
                    )[0]

                merged = Unit.objects.get(
                    pk=mergeform.cleaned_data['merge']
                )

                if unit.checksum != merged.checksum:
                    messages.error(
                        request,
                        _('Can not merge different messages!')
                    )
                else:
                    # Store unit
                    unit.target = merged.target
                    unit.fuzzy = merged.fuzzy
                    saved = unit.save_backend(request)
                    # Update stats if there was change
                    if saved:
                        profile.translated += 1
                        profile.save()
                    # Redirect to next entry
                    return HttpResponseRedirect(next_unit_url)
        except Unit.DoesNotExist:
            weblate.logger.error(
                'message %s disappeared!',
                mergeform.cleaned_data['checksum']
            )
            messages.error(
                request,
                _('Message you wanted to translate is no longer available!')
            )


def handle_suggestions(request, this_unit_url):
    '''
    Handles suggestion deleting/accepting.
    '''
    # Check for authenticated users
    if not request.user.is_authenticated():
        messages.error(
            request,
            _('You need to log in to be able to manage suggestions!')
        )
        return HttpResponseRedirect(this_unit_url)

    # Parse suggestion ID
    if 'accept' in request.GET:
        if not request.user.has_perm('trans.accept_suggestion'):
            messages.error(
                request,
                _('You do not have privilege to accept suggestions!')
            )
            return HttpResponseRedirect(this_unit_url)
        sugid = request.GET['accept']
    else:
        if not request.user.has_perm('trans.delete_suggestion'):
            messages.error(
                request,
                _('You do not have privilege to delete suggestions!')
            )
            return HttpResponseRedirect(this_unit_url)
        sugid = request.GET['delete']
    try:
        sugid = int(sugid)
        suggestion = Suggestion.objects.get(pk=sugid)
    except Suggestion.DoesNotExist:
        suggestion = None

    if suggestion is not None:
        if 'accept' in request.GET:
            # Accept suggesiont
            suggestion.accept(request)
        # Invalidate caches
        for unit in Unit.objects.filter(checksum=suggestion.checksum):
            unit.translation.invalidate_cache('suggestions')
        # Delete suggestion in both cases (accepted ones are no longer
        # needed)
        suggestion.delete()
    else:
        messages.error(request, _('Invalid suggestion!'))

    # Redirect to same entry for possible editing
    return HttpResponseRedirect(this_unit_url)


def translate(request, project, subproject, lang):
    '''
    Generic entry point for translating, suggesting and searching.
    '''
    obj = get_translation(request, project, subproject, lang)

    # Check locks
    project_locked, user_locked, own_lock = obj.is_locked(request, True)
    locked = project_locked or user_locked

    if request.user.is_authenticated():
        profile = request.user.get_profile()
        antispam = None
    else:
        profile = None
        antispam = AntispamForm()

    # Search results
    search_result = search(obj, request)
    num_results = len(search_result['ids'])

    # Handle redirects
    if isinstance(search_result, HttpResponse):
        return search_result

    # Search offset
    try:
        offset = int(request.GET.get('offset', '0'))
    except ValueError:
        offset = 0

    # Check boundaries
    if offset < 0 or offset >= num_results:
        messages.info(request, _('You have reached end of translating.'))
        # Delete search
        del request.session['search_%s' % search_result['search_id']]
        # Redirect to translation
        return HttpResponseRedirect(obj.get_absolute_url())

    # Some URLs we will most likely use
    base_unit_url = '%s?sid=%s&offset=' % (
        obj.get_translate_url(),
        search_result['search_id'],
    )
    this_unit_url = base_unit_url + str(offset)
    next_unit_url = base_unit_url + str(offset + 1)

    response = None

    # Any form submitted?
    if request.method == 'POST' and not project_locked:
        response = handle_translate(
            obj, request, profile, user_locked, this_unit_url, next_unit_url
        )

    # Handle translation merging
    elif 'merge' in request.GET and not locked:
        response = handle_merge(obj, request, profile, next_unit_url)

    # Handle accepting/deleting suggestions
    elif not locked and ('accept' in request.GET or 'delete' in request.GET):
        response = handle_suggestions(request, this_unit_url)

    # Pass possible redirect further
    if response is not None:
        return response

    # Grab actual unit
    unit = obj.unit_set.get(pk=search_result['ids'][offset])

    # Show secondary languages for logged in users
    if profile:
        secondary_langs = profile.secondary_languages.exclude(
            id=unit.translation.language.id
        )
        project = unit.translation.subproject.project
        secondary = Unit.objects.filter(
            checksum=unit.checksum,
            translated=True,
            translation__subproject__project=project,
            translation__language__in=secondary_langs,
        )
        # distinct('target') works with Django 1.4 so let's emulate that
        # based on presumption we won't get too many results
        targets = {}
        res = []
        for lang in secondary:
            if lang.target in targets:
                continue
            targets[lang.target] = 1
            res.append(lang)
        secondary = res
    else:
        secondary = None

    # Prepare form
    form = TranslationForm(initial={
        'checksum': unit.checksum,
        'target': (unit.translation.language, unit.get_target_plurals()),
        'fuzzy': unit.fuzzy,
    })

    total = obj.unit_set.all().count()

    return render_to_response(
        'translate.html',
        RequestContext(
            request,
            {
                'this_unit_url': this_unit_url,
                'first_unit_url': base_unit_url + '0',
                'last_unit_url': base_unit_url + str(num_results - 1),
                'next_unit_url': next_unit_url,
                'prev_unit_url': base_unit_url + str(offset - 1),
                'object': obj,
                'unit': unit,
                'last_changes': unit.change_set.all()[:10],
                'total': total,
                'search_id': search_result['search_id'],
                'offset': offset,
                'filter_name': search_result['name'],
                'filter_count': num_results,
                'filter_pos': offset + 1,
                'form': form,
                'antispam': antispam,
                'comment_form': CommentForm(),
                'target_language': obj.language.code.replace('_', '-').lower(),
                'update_lock': own_lock,
                'secondary': secondary,
                'locked': locked,
                'user_locked': user_locked,
                'project_locked': project_locked,
            },
        )
    )


@login_required
@permission_required('trans.automatic_translation')
def auto_translation(request, project, subproject, lang):
    obj = get_translation(request, project, subproject, lang)
    obj.commit_pending(request)
    autoform = AutoForm(obj, request.POST)
    change = None
    if not obj.subproject.locked and autoform.is_valid():
        if autoform.cleaned_data['inconsistent']:
            units = obj.unit_set.filter_type('inconsistent', obj)
        elif autoform.cleaned_data['overwrite']:
            units = obj.unit_set.all()
        else:
            units = obj.unit_set.filter(translated=False)

        sources = Unit.objects.filter(
            translation__language=obj.language,
            translated=True
        )
        if autoform.cleaned_data['subproject'] == '':
            sources = sources.filter(
                translation__subproject__project=obj.subproject.project
            ).exclude(
                translation=obj
            )
        else:
            subprj = SubProject.objects.get(
                project=obj.subproject.project,
                slug=autoform.cleaned_data['subproject']
            )
            sources = sources.filter(translation__subproject=subprj)

        for unit in units.iterator():
            update = sources.filter(checksum=unit.checksum)
            if update.exists():
                # Get first entry
                update = update[0]
                # No save if translation is same
                if unit.fuzzy == update.fuzzy and unit.target == update.target:
                    continue
                # Copy translation
                unit.fuzzy = update.fuzzy
                unit.target = update.target
                # Create signle change object for whole merge
                if change is None:
                    change = Change.objects.create(
                        action=Change.ACTION_AUTO,
                        translation=unit.translation,
                        user=request.user
                    )
                # Save unit to backend
                unit.save_backend(request, False, False)

        messages.info(request, _('Automatic translation completed.'))
    else:
        messages.error(request, _('Failed to process form!'))

    return HttpResponseRedirect(obj.get_absolute_url())


@login_required
def comment(request, pk):
    '''
    Adds new comment.
    '''
    obj = get_object_or_404(Unit, pk=pk)
    obj.check_acl(request)
    if request.POST.get('type', '') == 'source':
        lang = None
    else:
        lang = obj.translation.language

    form = CommentForm(request.POST)

    if form.is_valid():
        new_comment = Comment.objects.create(
            user=request.user,
            checksum=obj.checksum,
            project=obj.translation.subproject.project,
            comment=form.cleaned_data['comment'],
            language=lang
        )
        Change.objects.create(
            unit=obj,
            action=Change.ACTION_COMMENT,
            translation=obj.translation,
            user=request.user
        )

        # Invalidate counts cache
        if lang is None:
            obj.translation.invalidate_cache('sourcecomments')
        else:
            obj.translation.invalidate_cache('targetcomments')
        messages.info(request, _('Posted new comment'))
        # Notify subscribed users
        subscriptions = Profile.objects.subscribed_new_comment(
            obj.translation.subproject.project,
            lang,
            request.user
        )
        for subscription in subscriptions:
            subscription.notify_new_comment(obj, new_comment)
        # Notify upstream
        report_source_bugs = obj.translation.subproject.report_source_bugs
        if lang is None and report_source_bugs != '':
            send_notification_email(
                'en',
                report_source_bugs,
                'new_comment',
                obj.translation,
                {
                    'unit': obj,
                    'comment': new_comment,
                    'subproject': obj.translation.subproject,
                },
                from_email=request.user.email,
            )
    else:
        messages.error(request, _('Failed to add comment!'))

    return HttpResponseRedirect(obj.get_absolute_url())
