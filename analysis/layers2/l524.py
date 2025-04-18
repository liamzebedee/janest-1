import numpy as np




# Generated from reverse engineering
def l524_g(x: np.ndarray) -> np.ndarray:
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




def l524_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l524_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l524_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l524_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l524_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l524_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l524_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l524_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l524_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l524_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l524_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l524_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l524_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l524_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l524_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l524_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l524_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l524_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l524_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l524_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l524_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l524_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l524_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l524_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l524_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l524_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l524_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l524_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l524_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l524_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l524_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l524_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l524_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l524_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l524_34(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[34] + 1.0)
def l524_35(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[35] + 1.0)
def l524_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[32] + x[68] + -1.0)
def l524_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[33] + x[69] + -1.0)
def l524_38(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[34] + x[70])
def l524_39(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[35] + x[71])
def l524_40(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + x[72])
def l524_41(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + x[73])
def l524_42(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + x[74])
def l524_43(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + x[75])
def l524_44(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + x[76])
def l524_45(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + x[77])
def l524_46(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + x[78])
def l524_47(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + x[79])
def l524_48(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + x[80])
def l524_49(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + x[81])
def l524_50(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + x[82])
def l524_51(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + x[83])
def l524_52(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + x[84])
def l524_53(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + x[85])
def l524_54(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + x[86])
def l524_55(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + x[87])
def l524_56(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + x[88])
def l524_57(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + x[89])
def l524_58(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + x[90])
def l524_59(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + x[91])
def l524_60(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + x[92])
def l524_61(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + x[93])
def l524_62(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + x[94])
def l524_63(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + x[95])
def l524_64(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + 1.0)
def l524_65(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + 1.0)
def l524_66(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + 1.0)
def l524_67(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + 1.0)
def l524_68(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + 1.0)
def l524_69(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + 1.0)
def l524_70(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + 1.0)
def l524_71(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + 1.0)
def l524_72(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + 1.0)
def l524_73(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + 1.0)
def l524_74(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + 1.0)
def l524_75(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + 1.0)
def l524_76(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + 1.0)
def l524_77(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + 1.0)
def l524_78(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + 1.0)
def l524_79(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + 1.0)
def l524_80(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + 1.0)
def l524_81(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + 1.0)
def l524_82(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + 1.0)
def l524_83(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + 1.0)
def l524_84(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + 1.0)
def l524_85(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + 1.0)
def l524_86(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + 1.0)
def l524_87(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + 1.0)
def l524_88(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + 1.0)
def l524_89(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + 1.0)
def l524_90(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[62] + 1.0)
def l524_91(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[63] + 1.0)
def l524_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[64] + x[68] + -1.0)
def l524_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[65] + x[69] + -1.0)
def l524_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[66] + x[70] + -1.0)
def l524_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[67] + x[71] + -1.0)
def l524_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[68] + x[72] + -1.0)
def l524_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[69] + x[73] + -1.0)
def l524_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[70] + x[74] + -1.0)
def l524_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[71] + x[75] + -1.0)
def l524_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[72] + x[76] + -1.0)
def l524_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[73] + x[77] + -1.0)
def l524_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[74] + x[78] + -1.0)
def l524_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[75] + x[79] + -1.0)
def l524_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[76] + x[80] + -1.0)
def l524_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[77] + x[81] + -1.0)
def l524_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[78] + x[82] + -1.0)
def l524_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[79] + x[83] + -1.0)
def l524_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[80] + x[84] + -1.0)
def l524_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[81] + x[85] + -1.0)
def l524_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[82] + x[86] + -1.0)
def l524_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[83] + x[87] + -1.0)
def l524_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[84] + x[88] + -1.0)
def l524_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[85] + x[89] + -1.0)
def l524_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[86] + x[90] + -1.0)
def l524_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[87] + x[91] + -1.0)
def l524_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[88] + x[92] + -1.0)
def l524_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[89] + x[93] + -1.0)
def l524_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[90] + x[94] + -1.0)
def l524_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[91] + x[95] + -1.0)
def l524_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l524_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l524_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l524_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l524_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l524_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l524_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l524_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l524_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[100])
def l524_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[101])
def l524_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[102])
def l524_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[103])
def l524_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[104])
def l524_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[105])
def l524_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[106])
def l524_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[107])
def l524_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[108])
def l524_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[109])
def l524_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[110])
def l524_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[111])
def l524_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[112])
def l524_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[113])
def l524_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[114])
def l524_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[115])
def l524_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[116])
def l524_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[117])
def l524_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[118])
def l524_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[119])
def l524_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[120])
def l524_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[121])
def l524_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[122])
def l524_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[123])
def l524_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[124])
def l524_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[125])
def l524_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[126])
def l524_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[127])
def l524_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l524_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l524_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l524_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l524_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l524_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l524_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l524_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l524_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l524_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l524_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l524_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l524_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l524_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l524_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l524_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l524_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[144])
def l524_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[145])
def l524_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[146])
def l524_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[147])
def l524_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[148])
def l524_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[149])
def l524_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[150])
def l524_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[151])
def l524_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[152])
def l524_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[153])
def l524_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[154])
def l524_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[155])
def l524_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[156])
def l524_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[157])
def l524_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[158])
def l524_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[159])
def l524_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l524_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l524_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l524_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l524_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l524_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l524_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l524_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l524_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l524_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l524_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l524_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l524_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l524_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l524_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l524_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l524_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l524_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l524_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l524_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l524_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l524_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l524_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l524_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l524_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l524_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l524_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l524_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l524_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l524_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l524_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l524_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l524_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l524_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l524_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l524_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l524_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l524_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l524_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l524_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l524_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l524_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l524_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l524_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l524_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l524_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l524_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l524_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l524_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l524_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l524_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l524_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l524_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l524_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l524_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l524_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l524_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l524_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l524_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l524_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l524_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l524_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l524_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l524_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l524_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l524_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l524_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l524_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l524_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l524_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l524_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l524_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l524_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l524_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l524_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l524_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l524_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l524_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l524_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l524_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l524_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l524_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l524_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l524_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l524_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l524_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l524_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l524_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l524_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l524_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l524_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l524_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l524_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l524_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l524_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l524_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l524_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l524_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l524_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l524_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l524_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l524_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l524_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l524_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l524_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l524_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l524_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l524_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l524_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l524_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l524_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l524_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l524_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l524_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l524_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l524_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l524_304(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l524_305(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l524_306(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l524_307(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l524_308(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l524_309(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l524_310(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l524_311(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l524_312(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l524_313(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l524_314(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l524_315(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l524_(x):
    # x is a list (or vector) of length 288
    return [
        l524_0(x),
        l524_1(x),
        l524_2(x),
        l524_3(x),
        l524_4(x),
        l524_5(x),
        l524_6(x),
        l524_7(x),
        l524_8(x),
        l524_9(x),
        l524_10(x),
        l524_11(x),
        l524_12(x),
        l524_13(x),
        l524_14(x),
        l524_15(x),
        l524_16(x),
        l524_17(x),
        l524_18(x),
        l524_19(x),
        l524_20(x),
        l524_21(x),
        l524_22(x),
        l524_23(x),
        l524_24(x),
        l524_25(x),
        l524_26(x),
        l524_27(x),
        l524_28(x),
        l524_29(x),
        l524_30(x),
        l524_31(x),
        l524_32(x),
        l524_33(x),
        l524_34(x),
        l524_35(x),
        l524_36(x),
        l524_37(x),
        l524_38(x),
        l524_39(x),
        l524_40(x),
        l524_41(x),
        l524_42(x),
        l524_43(x),
        l524_44(x),
        l524_45(x),
        l524_46(x),
        l524_47(x),
        l524_48(x),
        l524_49(x),
        l524_50(x),
        l524_51(x),
        l524_52(x),
        l524_53(x),
        l524_54(x),
        l524_55(x),
        l524_56(x),
        l524_57(x),
        l524_58(x),
        l524_59(x),
        l524_60(x),
        l524_61(x),
        l524_62(x),
        l524_63(x),
        l524_64(x),
        l524_65(x),
        l524_66(x),
        l524_67(x),
        l524_68(x),
        l524_69(x),
        l524_70(x),
        l524_71(x),
        l524_72(x),
        l524_73(x),
        l524_74(x),
        l524_75(x),
        l524_76(x),
        l524_77(x),
        l524_78(x),
        l524_79(x),
        l524_80(x),
        l524_81(x),
        l524_82(x),
        l524_83(x),
        l524_84(x),
        l524_85(x),
        l524_86(x),
        l524_87(x),
        l524_88(x),
        l524_89(x),
        l524_90(x),
        l524_91(x),
        l524_92(x),
        l524_93(x),
        l524_94(x),
        l524_95(x),
        l524_96(x),
        l524_97(x),
        l524_98(x),
        l524_99(x),
        l524_100(x),
        l524_101(x),
        l524_102(x),
        l524_103(x),
        l524_104(x),
        l524_105(x),
        l524_106(x),
        l524_107(x),
        l524_108(x),
        l524_109(x),
        l524_110(x),
        l524_111(x),
        l524_112(x),
        l524_113(x),
        l524_114(x),
        l524_115(x),
        l524_116(x),
        l524_117(x),
        l524_118(x),
        l524_119(x),
        l524_120(x),
        l524_121(x),
        l524_122(x),
        l524_123(x),
        l524_124(x),
        l524_125(x),
        l524_126(x),
        l524_127(x),
        l524_128(x),
        l524_129(x),
        l524_130(x),
        l524_131(x),
        l524_132(x),
        l524_133(x),
        l524_134(x),
        l524_135(x),
        l524_136(x),
        l524_137(x),
        l524_138(x),
        l524_139(x),
        l524_140(x),
        l524_141(x),
        l524_142(x),
        l524_143(x),
        l524_144(x),
        l524_145(x),
        l524_146(x),
        l524_147(x),
        l524_148(x),
        l524_149(x),
        l524_150(x),
        l524_151(x),
        l524_152(x),
        l524_153(x),
        l524_154(x),
        l524_155(x),
        l524_156(x),
        l524_157(x),
        l524_158(x),
        l524_159(x),
        l524_160(x),
        l524_161(x),
        l524_162(x),
        l524_163(x),
        l524_164(x),
        l524_165(x),
        l524_166(x),
        l524_167(x),
        l524_168(x),
        l524_169(x),
        l524_170(x),
        l524_171(x),
        l524_172(x),
        l524_173(x),
        l524_174(x),
        l524_175(x),
        l524_176(x),
        l524_177(x),
        l524_178(x),
        l524_179(x),
        l524_180(x),
        l524_181(x),
        l524_182(x),
        l524_183(x),
        l524_184(x),
        l524_185(x),
        l524_186(x),
        l524_187(x),
        l524_188(x),
        l524_189(x),
        l524_190(x),
        l524_191(x),
        l524_192(x),
        l524_193(x),
        l524_194(x),
        l524_195(x),
        l524_196(x),
        l524_197(x),
        l524_198(x),
        l524_199(x),
        l524_200(x),
        l524_201(x),
        l524_202(x),
        l524_203(x),
        l524_204(x),
        l524_205(x),
        l524_206(x),
        l524_207(x),
        l524_208(x),
        l524_209(x),
        l524_210(x),
        l524_211(x),
        l524_212(x),
        l524_213(x),
        l524_214(x),
        l524_215(x),
        l524_216(x),
        l524_217(x),
        l524_218(x),
        l524_219(x),
        l524_220(x),
        l524_221(x),
        l524_222(x),
        l524_223(x),
        l524_224(x),
        l524_225(x),
        l524_226(x),
        l524_227(x),
        l524_228(x),
        l524_229(x),
        l524_230(x),
        l524_231(x),
        l524_232(x),
        l524_233(x),
        l524_234(x),
        l524_235(x),
        l524_236(x),
        l524_237(x),
        l524_238(x),
        l524_239(x),
        l524_240(x),
        l524_241(x),
        l524_242(x),
        l524_243(x),
        l524_244(x),
        l524_245(x),
        l524_246(x),
        l524_247(x),
        l524_248(x),
        l524_249(x),
        l524_250(x),
        l524_251(x),
        l524_252(x),
        l524_253(x),
        l524_254(x),
        l524_255(x),
        l524_256(x),
        l524_257(x),
        l524_258(x),
        l524_259(x),
        l524_260(x),
        l524_261(x),
        l524_262(x),
        l524_263(x),
        l524_264(x),
        l524_265(x),
        l524_266(x),
        l524_267(x),
        l524_268(x),
        l524_269(x),
        l524_270(x),
        l524_271(x),
        l524_272(x),
        l524_273(x),
        l524_274(x),
        l524_275(x),
        l524_276(x),
        l524_277(x),
        l524_278(x),
        l524_279(x),
        l524_280(x),
        l524_281(x),
        l524_282(x),
        l524_283(x),
        l524_284(x),
        l524_285(x),
        l524_286(x),
        l524_287(x),
        l524_288(x),
        l524_289(x),
        l524_290(x),
        l524_291(x),
        l524_292(x),
        l524_293(x),
        l524_294(x),
        l524_295(x),
        l524_296(x),
        l524_297(x),
        l524_298(x),
        l524_299(x),
        l524_300(x),
        l524_301(x),
        l524_302(x),
        l524_303(x),
        l524_304(x),
        l524_305(x),
        l524_306(x),
        l524_307(x),
        l524_308(x),
        l524_309(x),
        l524_310(x),
        l524_311(x),
        l524_312(x),
        l524_313(x),
        l524_314(x),
        l524_315(x),
    ]