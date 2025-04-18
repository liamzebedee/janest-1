import numpy as np




# Generated from reverse engineering
def l440_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 316
    out = np.empty(316, dtype=np.float32)
    
    # for i in range(0, 34):
    for i in range(0, 34):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3 (len=2)
    biases = [1.0, 1.0]
    # for i in range(34, 36):
    for i in range(0, 2):
        s = -1 * x[34 + i]
        s += biases[i]
        out[34 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0]
    # for i in range(36, 38):
    for i in range(0, 2):
        s = x[32 + i] + x[68 + i]
        s += biases[i]
        out[36 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(38, 64):
    for i in range(0, 26):
        s = x[70 + i] + -1 * x[34 + i]
        out[38 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xfffffff (len=28)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(64, 92):
    for i in range(0, 28):
        s = -1 * x[36 + i]
        s += biases[i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(92, 120):
    for i in range(0, 28):
        s = x[64 + i] + x[68 + i]
        s += biases[i]
        out[92 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(120, 124):
    for i in range(0, 4):
        s = x[64 + i]
        out[120 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(124, 316):
    for i in range(0, 192):
        s = x[96 + i]
        out[124 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l440_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l440_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l440_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l440_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l440_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l440_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l440_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l440_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l440_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l440_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l440_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l440_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l440_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l440_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l440_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l440_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l440_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l440_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l440_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l440_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l440_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l440_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l440_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l440_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l440_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l440_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l440_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l440_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l440_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l440_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l440_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l440_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l440_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l440_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l440_34(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[34] + 1.0)
def l440_35(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[35] + 1.0)
def l440_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[32] + x[68] + -1.0)
def l440_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[33] + x[69] + -1.0)
def l440_38(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[34] + x[70])
def l440_39(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[35] + x[71])
def l440_40(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + x[72])
def l440_41(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + x[73])
def l440_42(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + x[74])
def l440_43(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + x[75])
def l440_44(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + x[76])
def l440_45(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + x[77])
def l440_46(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + x[78])
def l440_47(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + x[79])
def l440_48(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + x[80])
def l440_49(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + x[81])
def l440_50(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + x[82])
def l440_51(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + x[83])
def l440_52(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + x[84])
def l440_53(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + x[85])
def l440_54(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + x[86])
def l440_55(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + x[87])
def l440_56(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + x[88])
def l440_57(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + x[89])
def l440_58(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + x[90])
def l440_59(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + x[91])
def l440_60(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + x[92])
def l440_61(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + x[93])
def l440_62(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + x[94])
def l440_63(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + x[95])
def l440_64(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + 1.0)
def l440_65(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + 1.0)
def l440_66(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + 1.0)
def l440_67(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + 1.0)
def l440_68(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + 1.0)
def l440_69(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + 1.0)
def l440_70(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + 1.0)
def l440_71(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + 1.0)
def l440_72(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + 1.0)
def l440_73(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + 1.0)
def l440_74(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + 1.0)
def l440_75(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + 1.0)
def l440_76(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + 1.0)
def l440_77(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + 1.0)
def l440_78(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + 1.0)
def l440_79(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + 1.0)
def l440_80(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + 1.0)
def l440_81(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + 1.0)
def l440_82(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + 1.0)
def l440_83(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + 1.0)
def l440_84(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + 1.0)
def l440_85(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + 1.0)
def l440_86(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + 1.0)
def l440_87(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + 1.0)
def l440_88(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + 1.0)
def l440_89(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + 1.0)
def l440_90(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[62] + 1.0)
def l440_91(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[63] + 1.0)
def l440_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[64] + x[68] + -1.0)
def l440_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[65] + x[69] + -1.0)
def l440_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[66] + x[70] + -1.0)
def l440_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[67] + x[71] + -1.0)
def l440_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[68] + x[72] + -1.0)
def l440_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[69] + x[73] + -1.0)
def l440_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[70] + x[74] + -1.0)
def l440_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[71] + x[75] + -1.0)
def l440_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[72] + x[76] + -1.0)
def l440_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[73] + x[77] + -1.0)
def l440_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[74] + x[78] + -1.0)
def l440_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[75] + x[79] + -1.0)
def l440_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[76] + x[80] + -1.0)
def l440_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[77] + x[81] + -1.0)
def l440_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[78] + x[82] + -1.0)
def l440_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[79] + x[83] + -1.0)
def l440_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[80] + x[84] + -1.0)
def l440_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[81] + x[85] + -1.0)
def l440_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[82] + x[86] + -1.0)
def l440_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[83] + x[87] + -1.0)
def l440_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[84] + x[88] + -1.0)
def l440_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[85] + x[89] + -1.0)
def l440_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[86] + x[90] + -1.0)
def l440_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[87] + x[91] + -1.0)
def l440_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[88] + x[92] + -1.0)
def l440_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[89] + x[93] + -1.0)
def l440_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[90] + x[94] + -1.0)
def l440_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[91] + x[95] + -1.0)
def l440_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l440_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l440_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l440_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l440_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l440_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l440_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l440_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l440_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[100])
def l440_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[101])
def l440_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[102])
def l440_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[103])
def l440_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[104])
def l440_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[105])
def l440_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[106])
def l440_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[107])
def l440_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[108])
def l440_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[109])
def l440_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[110])
def l440_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[111])
def l440_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[112])
def l440_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[113])
def l440_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[114])
def l440_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[115])
def l440_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[116])
def l440_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[117])
def l440_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[118])
def l440_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[119])
def l440_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[120])
def l440_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[121])
def l440_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[122])
def l440_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[123])
def l440_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[124])
def l440_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[125])
def l440_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[126])
def l440_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[127])
def l440_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l440_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l440_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l440_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l440_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l440_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l440_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l440_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l440_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l440_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l440_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l440_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l440_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l440_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l440_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l440_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l440_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[144])
def l440_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[145])
def l440_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[146])
def l440_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[147])
def l440_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[148])
def l440_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[149])
def l440_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[150])
def l440_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[151])
def l440_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[152])
def l440_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[153])
def l440_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[154])
def l440_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[155])
def l440_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[156])
def l440_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[157])
def l440_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[158])
def l440_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[159])
def l440_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l440_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l440_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l440_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l440_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l440_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l440_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l440_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l440_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l440_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l440_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l440_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l440_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l440_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l440_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l440_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l440_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l440_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l440_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l440_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l440_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l440_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l440_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l440_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l440_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l440_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l440_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l440_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l440_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l440_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l440_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l440_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l440_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l440_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l440_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l440_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l440_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l440_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l440_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l440_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l440_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l440_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l440_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l440_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l440_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l440_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l440_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l440_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l440_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l440_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l440_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l440_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l440_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l440_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l440_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l440_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l440_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l440_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l440_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l440_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l440_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l440_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l440_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l440_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l440_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l440_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l440_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l440_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l440_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l440_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l440_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l440_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l440_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l440_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l440_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l440_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l440_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l440_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l440_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l440_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l440_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l440_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l440_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l440_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l440_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l440_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l440_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l440_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l440_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l440_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l440_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l440_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l440_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l440_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l440_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l440_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l440_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l440_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l440_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l440_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l440_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l440_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l440_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l440_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l440_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l440_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l440_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l440_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l440_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l440_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l440_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l440_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l440_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l440_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l440_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l440_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l440_304(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l440_305(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l440_306(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l440_307(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l440_308(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l440_309(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l440_310(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l440_311(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l440_312(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l440_313(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l440_314(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l440_315(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l440_(x):
    # x is a list (or vector) of length 288
    return [
        l440_0(x),
        l440_1(x),
        l440_2(x),
        l440_3(x),
        l440_4(x),
        l440_5(x),
        l440_6(x),
        l440_7(x),
        l440_8(x),
        l440_9(x),
        l440_10(x),
        l440_11(x),
        l440_12(x),
        l440_13(x),
        l440_14(x),
        l440_15(x),
        l440_16(x),
        l440_17(x),
        l440_18(x),
        l440_19(x),
        l440_20(x),
        l440_21(x),
        l440_22(x),
        l440_23(x),
        l440_24(x),
        l440_25(x),
        l440_26(x),
        l440_27(x),
        l440_28(x),
        l440_29(x),
        l440_30(x),
        l440_31(x),
        l440_32(x),
        l440_33(x),
        l440_34(x),
        l440_35(x),
        l440_36(x),
        l440_37(x),
        l440_38(x),
        l440_39(x),
        l440_40(x),
        l440_41(x),
        l440_42(x),
        l440_43(x),
        l440_44(x),
        l440_45(x),
        l440_46(x),
        l440_47(x),
        l440_48(x),
        l440_49(x),
        l440_50(x),
        l440_51(x),
        l440_52(x),
        l440_53(x),
        l440_54(x),
        l440_55(x),
        l440_56(x),
        l440_57(x),
        l440_58(x),
        l440_59(x),
        l440_60(x),
        l440_61(x),
        l440_62(x),
        l440_63(x),
        l440_64(x),
        l440_65(x),
        l440_66(x),
        l440_67(x),
        l440_68(x),
        l440_69(x),
        l440_70(x),
        l440_71(x),
        l440_72(x),
        l440_73(x),
        l440_74(x),
        l440_75(x),
        l440_76(x),
        l440_77(x),
        l440_78(x),
        l440_79(x),
        l440_80(x),
        l440_81(x),
        l440_82(x),
        l440_83(x),
        l440_84(x),
        l440_85(x),
        l440_86(x),
        l440_87(x),
        l440_88(x),
        l440_89(x),
        l440_90(x),
        l440_91(x),
        l440_92(x),
        l440_93(x),
        l440_94(x),
        l440_95(x),
        l440_96(x),
        l440_97(x),
        l440_98(x),
        l440_99(x),
        l440_100(x),
        l440_101(x),
        l440_102(x),
        l440_103(x),
        l440_104(x),
        l440_105(x),
        l440_106(x),
        l440_107(x),
        l440_108(x),
        l440_109(x),
        l440_110(x),
        l440_111(x),
        l440_112(x),
        l440_113(x),
        l440_114(x),
        l440_115(x),
        l440_116(x),
        l440_117(x),
        l440_118(x),
        l440_119(x),
        l440_120(x),
        l440_121(x),
        l440_122(x),
        l440_123(x),
        l440_124(x),
        l440_125(x),
        l440_126(x),
        l440_127(x),
        l440_128(x),
        l440_129(x),
        l440_130(x),
        l440_131(x),
        l440_132(x),
        l440_133(x),
        l440_134(x),
        l440_135(x),
        l440_136(x),
        l440_137(x),
        l440_138(x),
        l440_139(x),
        l440_140(x),
        l440_141(x),
        l440_142(x),
        l440_143(x),
        l440_144(x),
        l440_145(x),
        l440_146(x),
        l440_147(x),
        l440_148(x),
        l440_149(x),
        l440_150(x),
        l440_151(x),
        l440_152(x),
        l440_153(x),
        l440_154(x),
        l440_155(x),
        l440_156(x),
        l440_157(x),
        l440_158(x),
        l440_159(x),
        l440_160(x),
        l440_161(x),
        l440_162(x),
        l440_163(x),
        l440_164(x),
        l440_165(x),
        l440_166(x),
        l440_167(x),
        l440_168(x),
        l440_169(x),
        l440_170(x),
        l440_171(x),
        l440_172(x),
        l440_173(x),
        l440_174(x),
        l440_175(x),
        l440_176(x),
        l440_177(x),
        l440_178(x),
        l440_179(x),
        l440_180(x),
        l440_181(x),
        l440_182(x),
        l440_183(x),
        l440_184(x),
        l440_185(x),
        l440_186(x),
        l440_187(x),
        l440_188(x),
        l440_189(x),
        l440_190(x),
        l440_191(x),
        l440_192(x),
        l440_193(x),
        l440_194(x),
        l440_195(x),
        l440_196(x),
        l440_197(x),
        l440_198(x),
        l440_199(x),
        l440_200(x),
        l440_201(x),
        l440_202(x),
        l440_203(x),
        l440_204(x),
        l440_205(x),
        l440_206(x),
        l440_207(x),
        l440_208(x),
        l440_209(x),
        l440_210(x),
        l440_211(x),
        l440_212(x),
        l440_213(x),
        l440_214(x),
        l440_215(x),
        l440_216(x),
        l440_217(x),
        l440_218(x),
        l440_219(x),
        l440_220(x),
        l440_221(x),
        l440_222(x),
        l440_223(x),
        l440_224(x),
        l440_225(x),
        l440_226(x),
        l440_227(x),
        l440_228(x),
        l440_229(x),
        l440_230(x),
        l440_231(x),
        l440_232(x),
        l440_233(x),
        l440_234(x),
        l440_235(x),
        l440_236(x),
        l440_237(x),
        l440_238(x),
        l440_239(x),
        l440_240(x),
        l440_241(x),
        l440_242(x),
        l440_243(x),
        l440_244(x),
        l440_245(x),
        l440_246(x),
        l440_247(x),
        l440_248(x),
        l440_249(x),
        l440_250(x),
        l440_251(x),
        l440_252(x),
        l440_253(x),
        l440_254(x),
        l440_255(x),
        l440_256(x),
        l440_257(x),
        l440_258(x),
        l440_259(x),
        l440_260(x),
        l440_261(x),
        l440_262(x),
        l440_263(x),
        l440_264(x),
        l440_265(x),
        l440_266(x),
        l440_267(x),
        l440_268(x),
        l440_269(x),
        l440_270(x),
        l440_271(x),
        l440_272(x),
        l440_273(x),
        l440_274(x),
        l440_275(x),
        l440_276(x),
        l440_277(x),
        l440_278(x),
        l440_279(x),
        l440_280(x),
        l440_281(x),
        l440_282(x),
        l440_283(x),
        l440_284(x),
        l440_285(x),
        l440_286(x),
        l440_287(x),
        l440_288(x),
        l440_289(x),
        l440_290(x),
        l440_291(x),
        l440_292(x),
        l440_293(x),
        l440_294(x),
        l440_295(x),
        l440_296(x),
        l440_297(x),
        l440_298(x),
        l440_299(x),
        l440_300(x),
        l440_301(x),
        l440_302(x),
        l440_303(x),
        l440_304(x),
        l440_305(x),
        l440_306(x),
        l440_307(x),
        l440_308(x),
        l440_309(x),
        l440_310(x),
        l440_311(x),
        l440_312(x),
        l440_313(x),
        l440_314(x),
        l440_315(x),
    ]