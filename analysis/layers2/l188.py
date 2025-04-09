import numpy as np




# Generated from reverse engineering
def l188_g(x: np.ndarray) -> np.ndarray:
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




def l188_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l188_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l188_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l188_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l188_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l188_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l188_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l188_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l188_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l188_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l188_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l188_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l188_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l188_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l188_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l188_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l188_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l188_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l188_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l188_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l188_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l188_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l188_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l188_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l188_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l188_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l188_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l188_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l188_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l188_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l188_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l188_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l188_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l188_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l188_34(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[34] + 1.0)
def l188_35(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[35] + 1.0)
def l188_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[32] + x[68] + -1.0)
def l188_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[33] + x[69] + -1.0)
def l188_38(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[34] + x[70])
def l188_39(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[35] + x[71])
def l188_40(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + x[72])
def l188_41(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + x[73])
def l188_42(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + x[74])
def l188_43(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + x[75])
def l188_44(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + x[76])
def l188_45(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + x[77])
def l188_46(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + x[78])
def l188_47(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + x[79])
def l188_48(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + x[80])
def l188_49(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + x[81])
def l188_50(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + x[82])
def l188_51(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + x[83])
def l188_52(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + x[84])
def l188_53(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + x[85])
def l188_54(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + x[86])
def l188_55(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + x[87])
def l188_56(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + x[88])
def l188_57(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + x[89])
def l188_58(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + x[90])
def l188_59(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + x[91])
def l188_60(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + x[92])
def l188_61(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + x[93])
def l188_62(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + x[94])
def l188_63(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + x[95])
def l188_64(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + 1.0)
def l188_65(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + 1.0)
def l188_66(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + 1.0)
def l188_67(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + 1.0)
def l188_68(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + 1.0)
def l188_69(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + 1.0)
def l188_70(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + 1.0)
def l188_71(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + 1.0)
def l188_72(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + 1.0)
def l188_73(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + 1.0)
def l188_74(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + 1.0)
def l188_75(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + 1.0)
def l188_76(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + 1.0)
def l188_77(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + 1.0)
def l188_78(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + 1.0)
def l188_79(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + 1.0)
def l188_80(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + 1.0)
def l188_81(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + 1.0)
def l188_82(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + 1.0)
def l188_83(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + 1.0)
def l188_84(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + 1.0)
def l188_85(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + 1.0)
def l188_86(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + 1.0)
def l188_87(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + 1.0)
def l188_88(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + 1.0)
def l188_89(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + 1.0)
def l188_90(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[62] + 1.0)
def l188_91(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[63] + 1.0)
def l188_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[64] + x[68] + -1.0)
def l188_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[65] + x[69] + -1.0)
def l188_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[66] + x[70] + -1.0)
def l188_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[67] + x[71] + -1.0)
def l188_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[68] + x[72] + -1.0)
def l188_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[69] + x[73] + -1.0)
def l188_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[70] + x[74] + -1.0)
def l188_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[71] + x[75] + -1.0)
def l188_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[72] + x[76] + -1.0)
def l188_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[73] + x[77] + -1.0)
def l188_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[74] + x[78] + -1.0)
def l188_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[75] + x[79] + -1.0)
def l188_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[76] + x[80] + -1.0)
def l188_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[77] + x[81] + -1.0)
def l188_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[78] + x[82] + -1.0)
def l188_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[79] + x[83] + -1.0)
def l188_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[80] + x[84] + -1.0)
def l188_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[81] + x[85] + -1.0)
def l188_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[82] + x[86] + -1.0)
def l188_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[83] + x[87] + -1.0)
def l188_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[84] + x[88] + -1.0)
def l188_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[85] + x[89] + -1.0)
def l188_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[86] + x[90] + -1.0)
def l188_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[87] + x[91] + -1.0)
def l188_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[88] + x[92] + -1.0)
def l188_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[89] + x[93] + -1.0)
def l188_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[90] + x[94] + -1.0)
def l188_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[91] + x[95] + -1.0)
def l188_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l188_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l188_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l188_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l188_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l188_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l188_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l188_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l188_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[100])
def l188_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[101])
def l188_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[102])
def l188_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[103])
def l188_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[104])
def l188_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[105])
def l188_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[106])
def l188_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[107])
def l188_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[108])
def l188_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[109])
def l188_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[110])
def l188_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[111])
def l188_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[112])
def l188_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[113])
def l188_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[114])
def l188_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[115])
def l188_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[116])
def l188_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[117])
def l188_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[118])
def l188_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[119])
def l188_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[120])
def l188_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[121])
def l188_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[122])
def l188_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[123])
def l188_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[124])
def l188_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[125])
def l188_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[126])
def l188_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[127])
def l188_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l188_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l188_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l188_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l188_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l188_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l188_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l188_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l188_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l188_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l188_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l188_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l188_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l188_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l188_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l188_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l188_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[144])
def l188_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[145])
def l188_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[146])
def l188_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[147])
def l188_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[148])
def l188_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[149])
def l188_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[150])
def l188_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[151])
def l188_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[152])
def l188_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[153])
def l188_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[154])
def l188_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[155])
def l188_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[156])
def l188_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[157])
def l188_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[158])
def l188_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[159])
def l188_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l188_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l188_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l188_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l188_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l188_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l188_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l188_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l188_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l188_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l188_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l188_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l188_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l188_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l188_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l188_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l188_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l188_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l188_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l188_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l188_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l188_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l188_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l188_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l188_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l188_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l188_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l188_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l188_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l188_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l188_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l188_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l188_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l188_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l188_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l188_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l188_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l188_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l188_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l188_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l188_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l188_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l188_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l188_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l188_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l188_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l188_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l188_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l188_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l188_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l188_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l188_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l188_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l188_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l188_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l188_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l188_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l188_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l188_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l188_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l188_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l188_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l188_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l188_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l188_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l188_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l188_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l188_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l188_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l188_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l188_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l188_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l188_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l188_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l188_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l188_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l188_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l188_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l188_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l188_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l188_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l188_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l188_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l188_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l188_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l188_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l188_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l188_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l188_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l188_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l188_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l188_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l188_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l188_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l188_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l188_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l188_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l188_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l188_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l188_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l188_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l188_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l188_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l188_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l188_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l188_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l188_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l188_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l188_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l188_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l188_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l188_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l188_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l188_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l188_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l188_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l188_304(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l188_305(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l188_306(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l188_307(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l188_308(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l188_309(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l188_310(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l188_311(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l188_312(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l188_313(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l188_314(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l188_315(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l188_(x):
    # x is a list (or vector) of length 288
    return [
        l188_0(x),
        l188_1(x),
        l188_2(x),
        l188_3(x),
        l188_4(x),
        l188_5(x),
        l188_6(x),
        l188_7(x),
        l188_8(x),
        l188_9(x),
        l188_10(x),
        l188_11(x),
        l188_12(x),
        l188_13(x),
        l188_14(x),
        l188_15(x),
        l188_16(x),
        l188_17(x),
        l188_18(x),
        l188_19(x),
        l188_20(x),
        l188_21(x),
        l188_22(x),
        l188_23(x),
        l188_24(x),
        l188_25(x),
        l188_26(x),
        l188_27(x),
        l188_28(x),
        l188_29(x),
        l188_30(x),
        l188_31(x),
        l188_32(x),
        l188_33(x),
        l188_34(x),
        l188_35(x),
        l188_36(x),
        l188_37(x),
        l188_38(x),
        l188_39(x),
        l188_40(x),
        l188_41(x),
        l188_42(x),
        l188_43(x),
        l188_44(x),
        l188_45(x),
        l188_46(x),
        l188_47(x),
        l188_48(x),
        l188_49(x),
        l188_50(x),
        l188_51(x),
        l188_52(x),
        l188_53(x),
        l188_54(x),
        l188_55(x),
        l188_56(x),
        l188_57(x),
        l188_58(x),
        l188_59(x),
        l188_60(x),
        l188_61(x),
        l188_62(x),
        l188_63(x),
        l188_64(x),
        l188_65(x),
        l188_66(x),
        l188_67(x),
        l188_68(x),
        l188_69(x),
        l188_70(x),
        l188_71(x),
        l188_72(x),
        l188_73(x),
        l188_74(x),
        l188_75(x),
        l188_76(x),
        l188_77(x),
        l188_78(x),
        l188_79(x),
        l188_80(x),
        l188_81(x),
        l188_82(x),
        l188_83(x),
        l188_84(x),
        l188_85(x),
        l188_86(x),
        l188_87(x),
        l188_88(x),
        l188_89(x),
        l188_90(x),
        l188_91(x),
        l188_92(x),
        l188_93(x),
        l188_94(x),
        l188_95(x),
        l188_96(x),
        l188_97(x),
        l188_98(x),
        l188_99(x),
        l188_100(x),
        l188_101(x),
        l188_102(x),
        l188_103(x),
        l188_104(x),
        l188_105(x),
        l188_106(x),
        l188_107(x),
        l188_108(x),
        l188_109(x),
        l188_110(x),
        l188_111(x),
        l188_112(x),
        l188_113(x),
        l188_114(x),
        l188_115(x),
        l188_116(x),
        l188_117(x),
        l188_118(x),
        l188_119(x),
        l188_120(x),
        l188_121(x),
        l188_122(x),
        l188_123(x),
        l188_124(x),
        l188_125(x),
        l188_126(x),
        l188_127(x),
        l188_128(x),
        l188_129(x),
        l188_130(x),
        l188_131(x),
        l188_132(x),
        l188_133(x),
        l188_134(x),
        l188_135(x),
        l188_136(x),
        l188_137(x),
        l188_138(x),
        l188_139(x),
        l188_140(x),
        l188_141(x),
        l188_142(x),
        l188_143(x),
        l188_144(x),
        l188_145(x),
        l188_146(x),
        l188_147(x),
        l188_148(x),
        l188_149(x),
        l188_150(x),
        l188_151(x),
        l188_152(x),
        l188_153(x),
        l188_154(x),
        l188_155(x),
        l188_156(x),
        l188_157(x),
        l188_158(x),
        l188_159(x),
        l188_160(x),
        l188_161(x),
        l188_162(x),
        l188_163(x),
        l188_164(x),
        l188_165(x),
        l188_166(x),
        l188_167(x),
        l188_168(x),
        l188_169(x),
        l188_170(x),
        l188_171(x),
        l188_172(x),
        l188_173(x),
        l188_174(x),
        l188_175(x),
        l188_176(x),
        l188_177(x),
        l188_178(x),
        l188_179(x),
        l188_180(x),
        l188_181(x),
        l188_182(x),
        l188_183(x),
        l188_184(x),
        l188_185(x),
        l188_186(x),
        l188_187(x),
        l188_188(x),
        l188_189(x),
        l188_190(x),
        l188_191(x),
        l188_192(x),
        l188_193(x),
        l188_194(x),
        l188_195(x),
        l188_196(x),
        l188_197(x),
        l188_198(x),
        l188_199(x),
        l188_200(x),
        l188_201(x),
        l188_202(x),
        l188_203(x),
        l188_204(x),
        l188_205(x),
        l188_206(x),
        l188_207(x),
        l188_208(x),
        l188_209(x),
        l188_210(x),
        l188_211(x),
        l188_212(x),
        l188_213(x),
        l188_214(x),
        l188_215(x),
        l188_216(x),
        l188_217(x),
        l188_218(x),
        l188_219(x),
        l188_220(x),
        l188_221(x),
        l188_222(x),
        l188_223(x),
        l188_224(x),
        l188_225(x),
        l188_226(x),
        l188_227(x),
        l188_228(x),
        l188_229(x),
        l188_230(x),
        l188_231(x),
        l188_232(x),
        l188_233(x),
        l188_234(x),
        l188_235(x),
        l188_236(x),
        l188_237(x),
        l188_238(x),
        l188_239(x),
        l188_240(x),
        l188_241(x),
        l188_242(x),
        l188_243(x),
        l188_244(x),
        l188_245(x),
        l188_246(x),
        l188_247(x),
        l188_248(x),
        l188_249(x),
        l188_250(x),
        l188_251(x),
        l188_252(x),
        l188_253(x),
        l188_254(x),
        l188_255(x),
        l188_256(x),
        l188_257(x),
        l188_258(x),
        l188_259(x),
        l188_260(x),
        l188_261(x),
        l188_262(x),
        l188_263(x),
        l188_264(x),
        l188_265(x),
        l188_266(x),
        l188_267(x),
        l188_268(x),
        l188_269(x),
        l188_270(x),
        l188_271(x),
        l188_272(x),
        l188_273(x),
        l188_274(x),
        l188_275(x),
        l188_276(x),
        l188_277(x),
        l188_278(x),
        l188_279(x),
        l188_280(x),
        l188_281(x),
        l188_282(x),
        l188_283(x),
        l188_284(x),
        l188_285(x),
        l188_286(x),
        l188_287(x),
        l188_288(x),
        l188_289(x),
        l188_290(x),
        l188_291(x),
        l188_292(x),
        l188_293(x),
        l188_294(x),
        l188_295(x),
        l188_296(x),
        l188_297(x),
        l188_298(x),
        l188_299(x),
        l188_300(x),
        l188_301(x),
        l188_302(x),
        l188_303(x),
        l188_304(x),
        l188_305(x),
        l188_306(x),
        l188_307(x),
        l188_308(x),
        l188_309(x),
        l188_310(x),
        l188_311(x),
        l188_312(x),
        l188_313(x),
        l188_314(x),
        l188_315(x),
    ]