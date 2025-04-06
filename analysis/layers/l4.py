def l4_0(x):
    # x is a list (or vector) of length 232
    # masks 10000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000000000000000000000000000000000000000000000000000000
    # bitshifts    x[56] << 7    x[112] >> 8    x[168] << 7
    # weight sections
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[0] + 128.0*x[56] + -256.0*x[112] + 128.0*x[168])
def l4_1(x):
    # x is a list (or vector) of length 232
    # masks 010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000000000000000000000000000000000000000000000000000000
    # bitshifts    x[57] << 7    x[113] >> 8    x[169] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[1] + 128.0*x[57] + -256.0*x[113] + 128.0*x[169])
def l4_2(x):
    # x is a list (or vector) of length 232
    # masks 0010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000000000
    # bitshifts    x[58] << 7    x[114] >> 8    x[170] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[2] + 128.0*x[58] + -256.0*x[114] + 128.0*x[170])
def l4_3(x):
    # x is a list (or vector) of length 232
    # masks 00010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000000000000000000000000000000000000000000000000000
    # bitshifts    x[59] << 7    x[115] >> 8    x[171] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[3] + 128.0*x[59] + -256.0*x[115] + 128.0*x[171])
def l4_4(x):
    # x is a list (or vector) of length 232
    # masks 000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000000000000000000000000000000000000000000000000000
    # bitshifts    x[60] << 7    x[116] >> 8    x[172] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[4] + 128.0*x[60] + -256.0*x[116] + 128.0*x[172])
def l4_5(x):
    # x is a list (or vector) of length 232
    # masks 0000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000000
    # bitshifts    x[61] << 7    x[117] >> 8    x[173] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[5] + 128.0*x[61] + -256.0*x[117] + 128.0*x[173])
def l4_6(x):
    # x is a list (or vector) of length 232
    # masks 00000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000000000000000000000000000000000000000000000000
    # bitshifts    x[62] << 7    x[118] >> 8    x[174] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[6] + 128.0*x[62] + -256.0*x[118] + 128.0*x[174])
def l4_7(x):
    # x is a list (or vector) of length 232
    # masks 000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000000000000000000000000000000000000000000000000
    # bitshifts    x[63] << 7    x[119] >> 8    x[175] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[7] + 128.0*x[63] + -256.0*x[119] + 128.0*x[175])
def l4_8(x):
    # x is a list (or vector) of length 232
    # masks 0000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000
    # bitshifts    x[64] << 7    x[120] >> 8    x[176] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[8] + 128.0*x[64] + -256.0*x[120] + 128.0*x[176])
def l4_9(x):
    # x is a list (or vector) of length 232
    # masks 00000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000000000000000000000000000000000000000000000
    # bitshifts    x[65] << 7    x[121] >> 8    x[177] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[9] + 128.0*x[65] + -256.0*x[121] + 128.0*x[177])
def l4_10(x):
    # x is a list (or vector) of length 232
    # masks 000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000000000000000000000000000000000000000000000
    # bitshifts    x[66] << 7    x[122] >> 8    x[178] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[10] + 128.0*x[66] + -256.0*x[122] + 128.0*x[178])
def l4_11(x):
    # x is a list (or vector) of length 232
    # masks 0000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000
    # bitshifts    x[67] << 7    x[123] >> 8    x[179] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[11] + 128.0*x[67] + -256.0*x[123] + 128.0*x[179])
def l4_12(x):
    # x is a list (or vector) of length 232
    # masks 00000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000000000000000000000000000000000000000000
    # bitshifts    x[68] << 7    x[124] >> 8    x[180] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[12] + 128.0*x[68] + -256.0*x[124] + 128.0*x[180])
def l4_13(x):
    # x is a list (or vector) of length 232
    # masks 000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000000000000000000000000000000000000000000
    # bitshifts    x[69] << 7    x[125] >> 8    x[181] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[13] + 128.0*x[69] + -256.0*x[125] + 128.0*x[181])
def l4_14(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000
    # bitshifts    x[70] << 7    x[126] >> 8    x[182] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[14] + 128.0*x[70] + -256.0*x[126] + 128.0*x[182])
def l4_15(x):
    # x is a list (or vector) of length 232
    # masks 00000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000000000000000000000000000000000000000
    # bitshifts    x[71] << 7    x[127] >> 8    x[183] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[15] + 128.0*x[71] + -256.0*x[127] + 128.0*x[183])
def l4_16(x):
    # x is a list (or vector) of length 232
    # masks 000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000000000000000000000000000000000000000
    # bitshifts    x[72] << 7    x[128] >> 8    x[184] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[16] + 128.0*x[72] + -256.0*x[128] + 128.0*x[184])
def l4_17(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000
    # bitshifts    x[73] << 7    x[129] >> 8    x[185] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[17] + 128.0*x[73] + -256.0*x[129] + 128.0*x[185])
def l4_18(x):
    # x is a list (or vector) of length 232
    # masks 00000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000000000000000000000000000000000000
    # bitshifts    x[74] << 7    x[130] >> 8    x[186] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[18] + 128.0*x[74] + -256.0*x[130] + 128.0*x[186])
def l4_19(x):
    # x is a list (or vector) of length 232
    # masks 000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000000000000000000000000000000000000
    # bitshifts    x[75] << 7    x[131] >> 8    x[187] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[19] + 128.0*x[75] + -256.0*x[131] + 128.0*x[187])
def l4_20(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000
    # bitshifts    x[76] << 7    x[132] >> 8    x[188] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[20] + 128.0*x[76] + -256.0*x[132] + 128.0*x[188])
def l4_21(x):
    # x is a list (or vector) of length 232
    # masks 00000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000000000000000000000000000000000
    # bitshifts    x[77] << 7    x[133] >> 8    x[189] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[21] + 128.0*x[77] + -256.0*x[133] + 128.0*x[189])
def l4_22(x):
    # x is a list (or vector) of length 232
    # masks 000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000000000000000000000000000000000
    # bitshifts    x[78] << 7    x[134] >> 8    x[190] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[22] + 128.0*x[78] + -256.0*x[134] + 128.0*x[190])
def l4_23(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000
    # bitshifts    x[79] << 7    x[135] >> 8    x[191] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[23] + 128.0*x[79] + -256.0*x[135] + 128.0*x[191])
def l4_24(x):
    # x is a list (or vector) of length 232
    # masks 00000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000000000000000000000000000000
    # bitshifts    x[80] << 7    x[136] >> 8    x[192] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[24] + 128.0*x[80] + -256.0*x[136] + 128.0*x[192])
def l4_25(x):
    # x is a list (or vector) of length 232
    # masks 000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000000000000000000000000000000
    # bitshifts    x[81] << 7    x[137] >> 8    x[193] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[25] + 128.0*x[81] + -256.0*x[137] + 128.0*x[193])
def l4_26(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000
    # bitshifts    x[82] << 7    x[138] >> 8    x[194] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[26] + 128.0*x[82] + -256.0*x[138] + 128.0*x[194])
def l4_27(x):
    # x is a list (or vector) of length 232
    # masks 00000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000000000000000000000000000
    # bitshifts    x[83] << 7    x[139] >> 8    x[195] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[27] + 128.0*x[83] + -256.0*x[139] + 128.0*x[195])
def l4_28(x):
    # x is a list (or vector) of length 232
    # masks 000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000000000000000000000000000
    # bitshifts    x[84] << 7    x[140] >> 8    x[196] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[28] + 128.0*x[84] + -256.0*x[140] + 128.0*x[196])
def l4_29(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000
    # bitshifts    x[85] << 7    x[141] >> 8    x[197] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[29] + 128.0*x[85] + -256.0*x[141] + 128.0*x[197])
def l4_30(x):
    # x is a list (or vector) of length 232
    # masks 00000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000000000000000000000000
    # bitshifts    x[86] << 7    x[142] >> 8    x[198] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[30] + 128.0*x[86] + -256.0*x[142] + 128.0*x[198])
def l4_31(x):
    # x is a list (or vector) of length 232
    # masks 000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000000000000000000000000
    # bitshifts    x[87] << 7    x[143] >> 8    x[199] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[31] + 128.0*x[87] + -256.0*x[143] + 128.0*x[199])
def l4_32(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000
    # bitshifts    x[88] << 7    x[144] >> 8    x[200] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[32] + 128.0*x[88] + -256.0*x[144] + 128.0*x[200])
def l4_33(x):
    # x is a list (or vector) of length 232
    # masks 00000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000000000000000000000
    # bitshifts    x[89] << 7    x[145] >> 8    x[201] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[33] + 128.0*x[89] + -256.0*x[145] + 128.0*x[201])
def l4_34(x):
    # x is a list (or vector) of length 232
    # masks 000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000000000000000000000
    # bitshifts    x[90] << 7    x[146] >> 8    x[202] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[34] + 128.0*x[90] + -256.0*x[146] + 128.0*x[202])
def l4_35(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000
    # bitshifts    x[91] << 7    x[147] >> 8    x[203] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[35] + 128.0*x[91] + -256.0*x[147] + 128.0*x[203])
def l4_36(x):
    # x is a list (or vector) of length 232
    # masks 00000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000000000000000000
    # bitshifts    x[92] << 7    x[148] >> 8    x[204] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[36] + 128.0*x[92] + -256.0*x[148] + 128.0*x[204])
def l4_37(x):
    # x is a list (or vector) of length 232
    # masks 000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000000000000000000
    # bitshifts    x[93] << 7    x[149] >> 8    x[205] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[37] + 128.0*x[93] + -256.0*x[149] + 128.0*x[205])
def l4_38(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000
    # bitshifts    x[94] << 7    x[150] >> 8    x[206] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[38] + 128.0*x[94] + -256.0*x[150] + 128.0*x[206])
def l4_39(x):
    # x is a list (or vector) of length 232
    # masks 00000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000000000000000
    # bitshifts    x[95] << 7    x[151] >> 8    x[207] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[39] + 128.0*x[95] + -256.0*x[151] + 128.0*x[207])
def l4_40(x):
    # x is a list (or vector) of length 232
    # masks 000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000000000000000
    # bitshifts    x[96] << 7    x[152] >> 8    x[208] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[40] + 128.0*x[96] + -256.0*x[152] + 128.0*x[208])
def l4_41(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000
    # bitshifts    x[97] << 7    x[153] >> 8    x[209] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[41] + 128.0*x[97] + -256.0*x[153] + 128.0*x[209])
def l4_42(x):
    # x is a list (or vector) of length 232
    # masks 00000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000000000000
    # bitshifts    x[98] << 7    x[154] >> 8    x[210] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[42] + 128.0*x[98] + -256.0*x[154] + 128.0*x[210])
def l4_43(x):
    # x is a list (or vector) of length 232
    # masks 000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000000000000
    # bitshifts    x[99] << 7    x[155] >> 8    x[211] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[43] + 128.0*x[99] + -256.0*x[155] + 128.0*x[211])
def l4_44(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000
    # bitshifts    x[100] << 7    x[156] >> 8    x[212] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[44] + 128.0*x[100] + -256.0*x[156] + 128.0*x[212])
def l4_45(x):
    # x is a list (or vector) of length 232
    # masks 00000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000000000
    # bitshifts    x[101] << 7    x[157] >> 8    x[213] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[45] + 128.0*x[101] + -256.0*x[157] + 128.0*x[213])
def l4_46(x):
    # x is a list (or vector) of length 232
    # masks 000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000000000
    # bitshifts    x[102] << 7    x[158] >> 8    x[214] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[46] + 128.0*x[102] + -256.0*x[158] + 128.0*x[214])
def l4_47(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000
    # bitshifts    x[103] << 7    x[159] >> 8    x[215] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[47] + 128.0*x[103] + -256.0*x[159] + 128.0*x[215])
def l4_48(x):
    # x is a list (or vector) of length 232
    # masks 00000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000000
    # bitshifts    x[104] << 7    x[160] >> 8    x[216] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[48] + 128.0*x[104] + -256.0*x[160] + 128.0*x[216])
def l4_49(x):
    # x is a list (or vector) of length 232
    # masks 000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000000
    # bitshifts    x[105] << 7    x[161] >> 8    x[217] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[49] + 128.0*x[105] + -256.0*x[161] + 128.0*x[217])
def l4_50(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000
    # bitshifts    x[106] << 7    x[162] >> 8    x[218] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[50] + 128.0*x[106] + -256.0*x[162] + 128.0*x[218])
def l4_51(x):
    # x is a list (or vector) of length 232
    # masks 00000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000
    # bitshifts    x[107] << 7    x[163] >> 8    x[219] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[51] + 128.0*x[107] + -256.0*x[163] + 128.0*x[219])
def l4_52(x):
    # x is a list (or vector) of length 232
    # masks 000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000
    # bitshifts    x[108] << 7    x[164] >> 8    x[220] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[52] + 128.0*x[108] + -256.0*x[164] + 128.0*x[220])
def l4_53(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000
    # bitshifts    x[109] << 7    x[165] >> 8    x[221] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[53] + 128.0*x[109] + -256.0*x[165] + 128.0*x[221])
def l4_54(x):
    # x is a list (or vector) of length 232
    # masks 00000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000
    # bitshifts    x[110] << 7    x[166] >> 8    x[222] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[54] + 128.0*x[110] + -256.0*x[166] + 128.0*x[222])
def l4_55(x):
    # x is a list (or vector) of length 232
    # masks 000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000
    # bitshifts    x[111] << 7    x[167] >> 8    x[223] << 7
    # weight sections
#     0.0
#     1.0
#     0.0
#     128.0
#     0.0
#     -256.0
#     0.0
#     128.0
#     0.0

    return max(0, x[55] + 128.0*x[111] + -256.0*x[167] + 128.0*x[223])
def l4_56(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000
    # bitshifts
    # weight sections
#     0.0
#     1.0
#     0.0

    return max(0, x[224])
def l4_57(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000
    # bitshifts
    # weight sections
#     0.0
#     1.0
#     0.0

    return max(0, x[225])
def l4_58(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000
    # bitshifts
    # weight sections
#     0.0
#     1.0
#     0.0

    return max(0, x[226])
def l4_59(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000
    # bitshifts
    # weight sections
#     0.0
#     1.0
#     0.0

    return max(0, x[227])
def l4_60(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000
    # bitshifts
    # weight sections
#     0.0
#     1.0
#     0.0

    return max(0, x[228])
def l4_61(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100
    # bitshifts
    # weight sections
#     0.0
#     1.0
#     0.0

    return max(0, x[229])
def l4_62(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010
    # bitshifts
    # weight sections
#     0.0
#     1.0
#     0.0

    return max(0, x[230])
def l4_63(x):
    # x is a list (or vector) of length 232
    # masks 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
    # bitshifts
    # weight sections
#     0.0
#     1.0

    return max(0, x[231])
def l4_(x):
    # x is a list (or vector) of length 232

    return [
        l4_0(x),
        l4_1(x),
        l4_2(x),
        l4_3(x),
        l4_4(x),
        l4_5(x),
        l4_6(x),
        l4_7(x),
        l4_8(x),
        l4_9(x),
        l4_10(x),
        l4_11(x),
        l4_12(x),
        l4_13(x),
        l4_14(x),
        l4_15(x),
        l4_16(x),
        l4_17(x),
        l4_18(x),
        l4_19(x),
        l4_20(x),
        l4_21(x),
        l4_22(x),
        l4_23(x),
        l4_24(x),
        l4_25(x),
        l4_26(x),
        l4_27(x),
        l4_28(x),
        l4_29(x),
        l4_30(x),
        l4_31(x),
        l4_32(x),
        l4_33(x),
        l4_34(x),
        l4_35(x),
        l4_36(x),
        l4_37(x),
        l4_38(x),
        l4_39(x),
        l4_40(x),
        l4_41(x),
        l4_42(x),
        l4_43(x),
        l4_44(x),
        l4_45(x),
        l4_46(x),
        l4_47(x),
        l4_48(x),
        l4_49(x),
        l4_50(x),
        l4_51(x),
        l4_52(x),
        l4_53(x),
        l4_54(x),
        l4_55(x),
        l4_56(x),
        l4_57(x),
        l4_58(x),
        l4_59(x),
        l4_60(x),
        l4_61(x),
        l4_62(x),
        l4_63(x),
    ]



# Test the function
# Generate a random 232-bit input
import random
x = [random.randint(0, 1) for _ in range(232)]


def convert_vec_to_bin(y):
    # Sanity check: y should be a list of integers
    for i in range(len(y)):
        if not isinstance(y[i], int):
            if y[i] % 1 != 0:
                print(f"Element {i} is not an integer: {y[i]}")
    y_int = int("".join(str(int(y[i])) for i in range(len(y))))
    y_str = "".join(chr(int(y[i])) for i in range(len(y)))
    print(y_str)
    y_hex = hex(y_int)
    return y_hex

import numpy as np

def human_l4(x: np.ndarray) -> np.ndarray:
    """
    Implements the bitwise logic equivalent of layer 4.
    Input:
      x - a numpy array of shape (232,) with dtype=np.float32.
    Output:
      A numpy array of shape (64,) representing the layer output.
    
    For i = 0 to 55:
      output[i] = max(0, 1*x[i] + 128*x[i+56] - 256*x[i+112] + 128*x[i+168])
    For i = 56 to 63:
      output[i] = max(0, 1*x[i+168])
    """
    out = np.empty(64, dtype=np.float32)
    
    # First 56 outputs
    for i in range(56):
        s = (1.0 * x[i] +
             128.0 * x[i + 56] +
            -256.0 * x[i + 112] +
             128.0 * x[i + 168])
        out[i] = s if s > 0 else 0.0  # ReLU
    
    # Last 8 outputs
    for i in range(56, 64):
        s = 1.0 * x[i + 168]  # For i=56, x[224] ... for i=63, x[231]
        out[i] = s if s > 0 else 0.0  # ReLU
    
    return out



# def human_l4_2(x: np.ndarray) -> np.ndarray:
#     """
#     Implements the bitwise logic equivalent of layer 4.
#     Input:
#       x - a numpy array of shape (232,) with dtype=np.float32.
#     Output:
#       A numpy array of shape (64,) representing the layer output.
    
#     For i = 0 to 55:
#       output[i] = max(0, 1*x[i] + 128*x[i+56] - 256*x[i+112] + 128*x[i+168])
#     For i = 56 to 63:
#       output[i] = max(0, 1*x[i+168])
#     """
#     out = np.empty(64, dtype=np.float32)
    
#     # First 56 outputs
#     for i in range(56):
#         s = x[i] + x[i + 56] << 7 + x[i + 112] >> 8 + x[i + 168] << 7
#         out[i] = s if s > 0 else 0.0  # ReLU
    
#     # Last 8 outputs
#     for i in range(56, 64):
#         s = x[i + 168]  # For i=56, x[224] ... for i=63, x[231]
#         out[i] = s if s > 0 else 0.0  # ReLU
    
#     return out

# Generated from reverse engineering
def l4_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 64
    out = np.empty(64, dtype=np.float32)

    for i in range(0, 56):
        s = x[i + 0] + +1*(x[i + 56] << 7) + -1*(x[i + 112] << 8) + +1*(x[i + 168] << 7)
        out[i] = s if s > 0 else 0.0 # ReLu

    for i in range(56, 64):
        s = x[i + 168]
        out[i] = s if s > 0 else 0.0 # ReLu

    return out

# Generated from reverse engineering
def l4_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 64
    out = np.empty(64, dtype=np.float32)

    biases = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for i in range(0, 56):
        s = x[0 + i] + 1*(x[i + 56] << 7) + -1*(x[i + 112] << 8) + 1*(x[i + 168] << 7)
        s += biases[i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu

    biases = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for i in range(0, 8):
        s = x[224 + i]
        s += biases[i]
        out[56 + i] = s if s > 0 else 0.0 # ReLu

    return out



print(convert_vec_to_bin(l4_(x)))
print(convert_vec_to_bin(human_l4(x)))
print(convert_vec_to_bin(l4_g(x)))