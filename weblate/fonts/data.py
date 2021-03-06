# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2019 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#


# List of chars in the Ubuntu font, otherwise we use DroidSansFallback
BASE_CHARS = {
    0x0000,
    0x0008,
    0x0009,
    0x000D,
    0x001D,
    0x0020,
    0x0021,
    0x0022,
    0x0023,
    0x0024,
    0x0025,
    0x0026,
    0x0027,
    0x0028,
    0x0029,
    0x002A,
    0x002B,
    0x002C,
    0x002D,
    0x002E,
    0x002F,
    0x0030,
    0x0031,
    0x0032,
    0x0033,
    0x0034,
    0x0035,
    0x0036,
    0x0037,
    0x0038,
    0x0039,
    0x003A,
    0x003B,
    0x003C,
    0x003D,
    0x003E,
    0x003F,
    0x0040,
    0x0041,
    0x0042,
    0x0043,
    0x0044,
    0x0045,
    0x0046,
    0x0047,
    0x0048,
    0x0049,
    0x004A,
    0x004B,
    0x004C,
    0x004D,
    0x004E,
    0x004F,
    0x0050,
    0x0051,
    0x0052,
    0x0053,
    0x0054,
    0x0055,
    0x0056,
    0x0057,
    0x0058,
    0x0059,
    0x005A,
    0x005B,
    0x005C,
    0x005D,
    0x005E,
    0x005F,
    0x0060,
    0x0061,
    0x0062,
    0x0063,
    0x0064,
    0x0065,
    0x0066,
    0x0067,
    0x0068,
    0x0069,
    0x006A,
    0x006B,
    0x006C,
    0x006D,
    0x006E,
    0x006F,
    0x0070,
    0x0071,
    0x0072,
    0x0073,
    0x0074,
    0x0075,
    0x0076,
    0x0077,
    0x0078,
    0x0079,
    0x007A,
    0x007B,
    0x007C,
    0x007D,
    0x007E,
    0x00A0,
    0x00A1,
    0x00A2,
    0x00A3,
    0x00A4,
    0x00A5,
    0x00A6,
    0x00A7,
    0x00A8,
    0x00A9,
    0x00AA,
    0x00AB,
    0x00AC,
    0x00AD,
    0x00AE,
    0x00AF,
    0x00B0,
    0x00B1,
    0x00B2,
    0x00B3,
    0x00B4,
    0x00B5,
    0x00B6,
    0x00B7,
    0x00B8,
    0x00B9,
    0x00BA,
    0x00BB,
    0x00BC,
    0x00BD,
    0x00BE,
    0x00BF,
    0x00C0,
    0x00C1,
    0x00C2,
    0x00C3,
    0x00C4,
    0x00C5,
    0x00C6,
    0x00C7,
    0x00C8,
    0x00C9,
    0x00CA,
    0x00CB,
    0x00CC,
    0x00CD,
    0x00CE,
    0x00CF,
    0x00D0,
    0x00D1,
    0x00D2,
    0x00D3,
    0x00D4,
    0x00D5,
    0x00D6,
    0x00D7,
    0x00D8,
    0x00D9,
    0x00DA,
    0x00DB,
    0x00DC,
    0x00DD,
    0x00DE,
    0x00DF,
    0x00E0,
    0x00E1,
    0x00E2,
    0x00E3,
    0x00E4,
    0x00E5,
    0x00E6,
    0x00E7,
    0x00E8,
    0x00E9,
    0x00EA,
    0x00EB,
    0x00EC,
    0x00ED,
    0x00EE,
    0x00EF,
    0x00F0,
    0x00F1,
    0x00F2,
    0x00F3,
    0x00F4,
    0x00F5,
    0x00F6,
    0x00F7,
    0x00F8,
    0x00F9,
    0x00FA,
    0x00FB,
    0x00FC,
    0x00FD,
    0x00FE,
    0x00FF,
    0x0100,
    0x0101,
    0x0102,
    0x0103,
    0x0104,
    0x0105,
    0x0106,
    0x0107,
    0x0108,
    0x0109,
    0x010A,
    0x010B,
    0x010C,
    0x010D,
    0x010E,
    0x010F,
    0x0110,
    0x0111,
    0x0112,
    0x0113,
    0x0114,
    0x0115,
    0x0116,
    0x0117,
    0x0118,
    0x0119,
    0x011A,
    0x011B,
    0x011C,
    0x011D,
    0x011E,
    0x011F,
    0x0120,
    0x0121,
    0x0122,
    0x0123,
    0x0124,
    0x0125,
    0x0126,
    0x0127,
    0x0128,
    0x0129,
    0x012A,
    0x012B,
    0x012C,
    0x012D,
    0x012E,
    0x012F,
    0x0130,
    0x0131,
    0x0132,
    0x0133,
    0x0134,
    0x0135,
    0x0136,
    0x0137,
    0x0138,
    0x0139,
    0x013A,
    0x013B,
    0x013C,
    0x013D,
    0x013E,
    0x013F,
    0x0140,
    0x0141,
    0x0142,
    0x0143,
    0x0144,
    0x0145,
    0x0146,
    0x0147,
    0x0148,
    0x0149,
    0x014A,
    0x014B,
    0x014C,
    0x014D,
    0x014E,
    0x014F,
    0x0150,
    0x0151,
    0x0152,
    0x0153,
    0x0154,
    0x0155,
    0x0156,
    0x0157,
    0x0158,
    0x0159,
    0x015A,
    0x015B,
    0x015C,
    0x015D,
    0x015E,
    0x015F,
    0x0160,
    0x0161,
    0x0162,
    0x0163,
    0x0164,
    0x0165,
    0x0166,
    0x0167,
    0x0168,
    0x0169,
    0x016A,
    0x016B,
    0x016C,
    0x016D,
    0x016E,
    0x016F,
    0x0170,
    0x0171,
    0x0172,
    0x0173,
    0x0174,
    0x0175,
    0x0176,
    0x0177,
    0x0178,
    0x0179,
    0x017A,
    0x017B,
    0x017C,
    0x017D,
    0x017E,
    0x017F,
    0x0180,
    0x0181,
    0x0182,
    0x0183,
    0x0184,
    0x0185,
    0x0186,
    0x0187,
    0x0188,
    0x0189,
    0x018A,
    0x018B,
    0x018C,
    0x018D,
    0x018E,
    0x018F,
    0x0190,
    0x0191,
    0x0192,
    0x0193,
    0x0194,
    0x0195,
    0x0196,
    0x0197,
    0x0198,
    0x0199,
    0x019A,
    0x019B,
    0x019C,
    0x019D,
    0x019E,
    0x019F,
    0x01A0,
    0x01A1,
    0x01A2,
    0x01A3,
    0x01A4,
    0x01A5,
    0x01A6,
    0x01A7,
    0x01A8,
    0x01A9,
    0x01AA,
    0x01AB,
    0x01AC,
    0x01AD,
    0x01AE,
    0x01AF,
    0x01B0,
    0x01B1,
    0x01B2,
    0x01B3,
    0x01B4,
    0x01B5,
    0x01B6,
    0x01B7,
    0x01B8,
    0x01B9,
    0x01BA,
    0x01BB,
    0x01BC,
    0x01BD,
    0x01BE,
    0x01BF,
    0x01C0,
    0x01C1,
    0x01C2,
    0x01C3,
    0x01C4,
    0x01C5,
    0x01C6,
    0x01C7,
    0x01C8,
    0x01C9,
    0x01CA,
    0x01CB,
    0x01CC,
    0x01CD,
    0x01CE,
    0x01CF,
    0x01D0,
    0x01D1,
    0x01D2,
    0x01D3,
    0x01D4,
    0x01D5,
    0x01D6,
    0x01D7,
    0x01D8,
    0x01D9,
    0x01DA,
    0x01DB,
    0x01DC,
    0x01DD,
    0x01DE,
    0x01DF,
    0x01E0,
    0x01E1,
    0x01E2,
    0x01E3,
    0x01E4,
    0x01E5,
    0x01E6,
    0x01E7,
    0x01E8,
    0x01E9,
    0x01EA,
    0x01EB,
    0x01EC,
    0x01ED,
    0x01EE,
    0x01EF,
    0x01F0,
    0x01F1,
    0x01F2,
    0x01F3,
    0x01F4,
    0x01F5,
    0x01F6,
    0x01F7,
    0x01F8,
    0x01F9,
    0x01FA,
    0x01FB,
    0x01FC,
    0x01FD,
    0x01FE,
    0x01FF,
    0x0200,
    0x0201,
    0x0202,
    0x0203,
    0x0204,
    0x0205,
    0x0206,
    0x0207,
    0x0208,
    0x0209,
    0x020A,
    0x020B,
    0x020C,
    0x020D,
    0x020E,
    0x020F,
    0x0210,
    0x0211,
    0x0212,
    0x0213,
    0x0214,
    0x0215,
    0x0216,
    0x0217,
    0x0218,
    0x0219,
    0x021A,
    0x021B,
    0x021C,
    0x021D,
    0x021E,
    0x021F,
    0x0220,
    0x0221,
    0x0222,
    0x0223,
    0x0224,
    0x0225,
    0x0226,
    0x0227,
    0x0228,
    0x0229,
    0x022A,
    0x022B,
    0x022C,
    0x022D,
    0x022E,
    0x022F,
    0x0230,
    0x0231,
    0x0232,
    0x0233,
    0x0234,
    0x0235,
    0x0236,
    0x0237,
    0x0238,
    0x0239,
    0x023A,
    0x023B,
    0x023C,
    0x023D,
    0x023E,
    0x023F,
    0x0240,
    0x0241,
    0x0242,
    0x0243,
    0x0244,
    0x0245,
    0x0246,
    0x0247,
    0x0248,
    0x0249,
    0x024A,
    0x024B,
    0x024C,
    0x024D,
    0x024E,
    0x024F,
    0x0292,
    0x02BC,
    0x02C6,
    0x02C7,
    0x02C9,
    0x02D8,
    0x02D9,
    0x02DA,
    0x02DB,
    0x02DC,
    0x02DD,
    0x0311,
    0x0384,
    0x0385,
    0x0386,
    0x0388,
    0x0389,
    0x038A,
    0x038C,
    0x038E,
    0x038F,
    0x0390,
    0x0391,
    0x0392,
    0x0393,
    0x0394,
    0x0395,
    0x0396,
    0x0397,
    0x0398,
    0x0399,
    0x039A,
    0x039B,
    0x039C,
    0x039D,
    0x039E,
    0x039F,
    0x03A0,
    0x03A1,
    0x03A3,
    0x03A4,
    0x03A5,
    0x03A6,
    0x03A7,
    0x03A8,
    0x03A9,
    0x03AA,
    0x03AB,
    0x03AC,
    0x03AD,
    0x03AE,
    0x03AF,
    0x03B0,
    0x03B1,
    0x03B2,
    0x03B3,
    0x03B4,
    0x03B5,
    0x03B6,
    0x03B7,
    0x03B8,
    0x03B9,
    0x03BA,
    0x03BB,
    0x03BC,
    0x03BD,
    0x03BE,
    0x03BF,
    0x03C0,
    0x03C1,
    0x03C2,
    0x03C3,
    0x03C4,
    0x03C5,
    0x03C6,
    0x03C7,
    0x03C8,
    0x03C9,
    0x03CA,
    0x03CB,
    0x03CC,
    0x03CD,
    0x03CE,
    0x0400,
    0x0401,
    0x0402,
    0x0403,
    0x0404,
    0x0405,
    0x0406,
    0x0407,
    0x0408,
    0x0409,
    0x040A,
    0x040B,
    0x040C,
    0x040D,
    0x040E,
    0x040F,
    0x0410,
    0x0411,
    0x0412,
    0x0413,
    0x0414,
    0x0415,
    0x0416,
    0x0417,
    0x0418,
    0x0419,
    0x041A,
    0x041B,
    0x041C,
    0x041D,
    0x041E,
    0x041F,
    0x0420,
    0x0421,
    0x0422,
    0x0423,
    0x0424,
    0x0425,
    0x0426,
    0x0427,
    0x0428,
    0x0429,
    0x042A,
    0x042B,
    0x042C,
    0x042D,
    0x042E,
    0x042F,
    0x0430,
    0x0431,
    0x0432,
    0x0433,
    0x0434,
    0x0435,
    0x0436,
    0x0437,
    0x0438,
    0x0439,
    0x043A,
    0x043B,
    0x043C,
    0x043D,
    0x043E,
    0x043F,
    0x0440,
    0x0441,
    0x0442,
    0x0443,
    0x0444,
    0x0445,
    0x0446,
    0x0447,
    0x0448,
    0x0449,
    0x044A,
    0x044B,
    0x044C,
    0x044D,
    0x044E,
    0x044F,
    0x0450,
    0x0451,
    0x0452,
    0x0453,
    0x0454,
    0x0455,
    0x0456,
    0x0457,
    0x0458,
    0x0459,
    0x045A,
    0x045B,
    0x045C,
    0x045D,
    0x045E,
    0x045F,
    0x0462,
    0x0463,
    0x0472,
    0x0473,
    0x0474,
    0x0475,
    0x048A,
    0x048B,
    0x048C,
    0x048D,
    0x048E,
    0x048F,
    0x0490,
    0x0491,
    0x0492,
    0x0493,
    0x0494,
    0x0495,
    0x0496,
    0x0497,
    0x0498,
    0x0499,
    0x049A,
    0x049B,
    0x049C,
    0x049D,
    0x049E,
    0x049F,
    0x04A0,
    0x04A1,
    0x04A2,
    0x04A3,
    0x04A4,
    0x04A5,
    0x04A6,
    0x04A7,
    0x04A8,
    0x04A9,
    0x04AA,
    0x04AB,
    0x04AC,
    0x04AD,
    0x04AE,
    0x04AF,
    0x04B0,
    0x04B1,
    0x04B2,
    0x04B3,
    0x04B4,
    0x04B5,
    0x04B6,
    0x04B7,
    0x04B8,
    0x04B9,
    0x04BA,
    0x04BB,
    0x04BC,
    0x04BD,
    0x04BE,
    0x04BF,
    0x04C0,
    0x04C1,
    0x04C2,
    0x04C3,
    0x04C4,
    0x04C5,
    0x04C6,
    0x04C7,
    0x04C8,
    0x04C9,
    0x04CA,
    0x04CB,
    0x04CC,
    0x04CD,
    0x04CE,
    0x04CF,
    0x04D0,
    0x04D1,
    0x04D2,
    0x04D3,
    0x04D4,
    0x04D5,
    0x04D6,
    0x04D7,
    0x04D8,
    0x04D9,
    0x04DA,
    0x04DB,
    0x04DC,
    0x04DD,
    0x04DE,
    0x04DF,
    0x04E0,
    0x04E1,
    0x04E2,
    0x04E3,
    0x04E4,
    0x04E5,
    0x04E6,
    0x04E7,
    0x04E8,
    0x04E9,
    0x04EA,
    0x04EB,
    0x04EC,
    0x04ED,
    0x04EE,
    0x04EF,
    0x04F0,
    0x04F1,
    0x04F2,
    0x04F3,
    0x04F4,
    0x04F5,
    0x04F6,
    0x04F7,
    0x04F8,
    0x04F9,
    0x1E80,
    0x1E81,
    0x1E82,
    0x1E83,
    0x1E84,
    0x1E85,
    0x1EF2,
    0x1EF3,
    0x1F00,
    0x1F01,
    0x1F02,
    0x1F03,
    0x1F04,
    0x1F05,
    0x1F06,
    0x1F07,
    0x1F08,
    0x1F09,
    0x1F0A,
    0x1F0B,
    0x1F0C,
    0x1F0D,
    0x1F0E,
    0x1F0F,
    0x1F10,
    0x1F11,
    0x1F12,
    0x1F13,
    0x1F14,
    0x1F15,
    0x1F18,
    0x1F19,
    0x1F1A,
    0x1F1B,
    0x1F1C,
    0x1F1D,
    0x1F20,
    0x1F21,
    0x1F22,
    0x1F23,
    0x1F24,
    0x1F25,
    0x1F26,
    0x1F27,
    0x1F28,
    0x1F29,
    0x1F2A,
    0x1F2B,
    0x1F2C,
    0x1F2D,
    0x1F2E,
    0x1F2F,
    0x1F30,
    0x1F31,
    0x1F32,
    0x1F33,
    0x1F34,
    0x1F35,
    0x1F36,
    0x1F37,
    0x1F38,
    0x1F39,
    0x1F3A,
    0x1F3B,
    0x1F3C,
    0x1F3D,
    0x1F3E,
    0x1F3F,
    0x1F40,
    0x1F41,
    0x1F42,
    0x1F43,
    0x1F44,
    0x1F45,
    0x1F48,
    0x1F49,
    0x1F4A,
    0x1F4B,
    0x1F4C,
    0x1F4D,
    0x1F50,
    0x1F51,
    0x1F52,
    0x1F53,
    0x1F54,
    0x1F55,
    0x1F56,
    0x1F57,
    0x1F59,
    0x1F5B,
    0x1F5D,
    0x1F5F,
    0x1F60,
    0x1F61,
    0x1F62,
    0x1F63,
    0x1F64,
    0x1F65,
    0x1F66,
    0x1F67,
    0x1F68,
    0x1F69,
    0x1F6A,
    0x1F6B,
    0x1F6C,
    0x1F6D,
    0x1F6E,
    0x1F6F,
    0x1F70,
    0x1F71,
    0x1F72,
    0x1F73,
    0x1F74,
    0x1F75,
    0x1F76,
    0x1F77,
    0x1F78,
    0x1F79,
    0x1F7A,
    0x1F7B,
    0x1F7C,
    0x1F7D,
    0x1F80,
    0x1F81,
    0x1F82,
    0x1F83,
    0x1F84,
    0x1F85,
    0x1F86,
    0x1F87,
    0x1F88,
    0x1F89,
    0x1F8A,
    0x1F8B,
    0x1F8C,
    0x1F8D,
    0x1F8E,
    0x1F8F,
    0x1F90,
    0x1F91,
    0x1F92,
    0x1F93,
    0x1F94,
    0x1F95,
    0x1F96,
    0x1F97,
    0x1F98,
    0x1F99,
    0x1F9A,
    0x1F9B,
    0x1F9C,
    0x1F9D,
    0x1F9E,
    0x1F9F,
    0x1FA0,
    0x1FA1,
    0x1FA2,
    0x1FA3,
    0x1FA4,
    0x1FA5,
    0x1FA6,
    0x1FA7,
    0x1FA8,
    0x1FA9,
    0x1FAA,
    0x1FAB,
    0x1FAC,
    0x1FAD,
    0x1FAE,
    0x1FAF,
    0x1FB0,
    0x1FB1,
    0x1FB2,
    0x1FB3,
    0x1FB4,
    0x1FB6,
    0x1FB7,
    0x1FB8,
    0x1FB9,
    0x1FBA,
    0x1FBB,
    0x1FBC,
    0x1FBD,
    0x1FBE,
    0x1FBF,
    0x1FC0,
    0x1FC1,
    0x1FC2,
    0x1FC3,
    0x1FC4,
    0x1FC6,
    0x1FC7,
    0x1FC8,
    0x1FC9,
    0x1FCA,
    0x1FCB,
    0x1FCC,
    0x1FCD,
    0x1FCE,
    0x1FCF,
    0x1FD0,
    0x1FD1,
    0x1FD2,
    0x1FD3,
    0x1FD6,
    0x1FD7,
    0x1FD8,
    0x1FD9,
    0x1FDA,
    0x1FDB,
    0x1FDD,
    0x1FDE,
    0x1FDF,
    0x1FE0,
    0x1FE1,
    0x1FE2,
    0x1FE3,
    0x1FE4,
    0x1FE5,
    0x1FE6,
    0x1FE7,
    0x1FE8,
    0x1FE9,
    0x1FEA,
    0x1FEB,
    0x1FEC,
    0x1FED,
    0x1FEE,
    0x1FEF,
    0x1FF2,
    0x1FF3,
    0x1FF4,
    0x1FF6,
    0x1FF7,
    0x1FF8,
    0x1FF9,
    0x1FFA,
    0x1FFB,
    0x1FFC,
    0x1FFD,
    0x1FFE,
    0x2013,
    0x2014,
    0x2015,
    0x2018,
    0x2019,
    0x201A,
    0x201C,
    0x201D,
    0x201E,
    0x2020,
    0x2021,
    0x2022,
    0x2026,
    0x2030,
    0x2039,
    0x203A,
    0x2044,
    0x2070,
    0x2074,
    0x2075,
    0x2076,
    0x2077,
    0x2078,
    0x2079,
    0x2080,
    0x2081,
    0x2082,
    0x2083,
    0x2084,
    0x2085,
    0x2086,
    0x2087,
    0x2088,
    0x2089,
    0x20AC,
    0x20AE,
    0x20B4,
    0x20B9,
    0x2113,
    0x2116,
    0x2122,
    0x2126,
    0x212E,
    0x2153,
    0x2154,
    0x2155,
    0x2156,
    0x2157,
    0x2158,
    0x2159,
    0x215A,
    0x215B,
    0x215C,
    0x215D,
    0x215E,
    0x2202,
    0x2206,
    0x220F,
    0x2211,
    0x2212,
    0x2215,
    0x2219,
    0x221A,
    0x221E,
    0x222B,
    0x2248,
    0x2260,
    0x2264,
    0x2265,
    0x25CA,
    0xE0FF,
    0xEFFD,
    0xF000,
    0xF001,
    0xF002,
    0xF0FF,
    0xF200,
    0xF506,
    0xF507,
    0xF508,
    0xF509,
    0xF50A,
    0xF50B,
    0xF50C,
    0xF50D,
    0xF50E,
    0xF50F,
    0xF510,
    0xF511,
    0xF800,
    0xF801,
    0xF802,
    0xF803,
    0xF804,
    0xF805,
    0xF806,
    0xF807,
    0xF808,
    0xF809,
    0xF80A,
    0xF80B,
    0xF80C,
    0xF80D,
    0xF80E,
    0xF80F,
    0xF810,
    0xF811,
    0xF812,
    0xF813,
    0xF814,
    0xF815,
    0xF816,
    0xF817,
    0xF818,
    0xF819,
    0xF81A,
    0xF81B,
    0xF81C,
    0xF81D,
    0xFB00,
    0xFB01,
    0xFB02,
    0xFB03,
    0xFB04,
    0xFFFF,
}
