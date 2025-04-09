import numpy as np




# Generated from reverse engineering
def l356_g(x: np.ndarray) -> np.ndarray:
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




def l356_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l356_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l356_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l356_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l356_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l356_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l356_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l356_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l356_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l356_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l356_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l356_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l356_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l356_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l356_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l356_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l356_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l356_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l356_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l356_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l356_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l356_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l356_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l356_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l356_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l356_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l356_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l356_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l356_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l356_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l356_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l356_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l356_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l356_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l356_34(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[34] + 1.0)
def l356_35(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[35] + 1.0)
def l356_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[32] + x[68] + -1.0)
def l356_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[33] + x[69] + -1.0)
def l356_38(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[34] + x[70])
def l356_39(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[35] + x[71])
def l356_40(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + x[72])
def l356_41(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + x[73])
def l356_42(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + x[74])
def l356_43(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + x[75])
def l356_44(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + x[76])
def l356_45(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + x[77])
def l356_46(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + x[78])
def l356_47(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + x[79])
def l356_48(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + x[80])
def l356_49(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + x[81])
def l356_50(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + x[82])
def l356_51(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + x[83])
def l356_52(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + x[84])
def l356_53(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + x[85])
def l356_54(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + x[86])
def l356_55(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + x[87])
def l356_56(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + x[88])
def l356_57(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + x[89])
def l356_58(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + x[90])
def l356_59(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + x[91])
def l356_60(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + x[92])
def l356_61(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + x[93])
def l356_62(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + x[94])
def l356_63(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + x[95])
def l356_64(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + 1.0)
def l356_65(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + 1.0)
def l356_66(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + 1.0)
def l356_67(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + 1.0)
def l356_68(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + 1.0)
def l356_69(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + 1.0)
def l356_70(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + 1.0)
def l356_71(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + 1.0)
def l356_72(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + 1.0)
def l356_73(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + 1.0)
def l356_74(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + 1.0)
def l356_75(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + 1.0)
def l356_76(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + 1.0)
def l356_77(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + 1.0)
def l356_78(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + 1.0)
def l356_79(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + 1.0)
def l356_80(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + 1.0)
def l356_81(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + 1.0)
def l356_82(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + 1.0)
def l356_83(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + 1.0)
def l356_84(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + 1.0)
def l356_85(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + 1.0)
def l356_86(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + 1.0)
def l356_87(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + 1.0)
def l356_88(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + 1.0)
def l356_89(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + 1.0)
def l356_90(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[62] + 1.0)
def l356_91(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[63] + 1.0)
def l356_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[64] + x[68] + -1.0)
def l356_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[65] + x[69] + -1.0)
def l356_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[66] + x[70] + -1.0)
def l356_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[67] + x[71] + -1.0)
def l356_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[68] + x[72] + -1.0)
def l356_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[69] + x[73] + -1.0)
def l356_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[70] + x[74] + -1.0)
def l356_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[71] + x[75] + -1.0)
def l356_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[72] + x[76] + -1.0)
def l356_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[73] + x[77] + -1.0)
def l356_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[74] + x[78] + -1.0)
def l356_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[75] + x[79] + -1.0)
def l356_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[76] + x[80] + -1.0)
def l356_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[77] + x[81] + -1.0)
def l356_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[78] + x[82] + -1.0)
def l356_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[79] + x[83] + -1.0)
def l356_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[80] + x[84] + -1.0)
def l356_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[81] + x[85] + -1.0)
def l356_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[82] + x[86] + -1.0)
def l356_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[83] + x[87] + -1.0)
def l356_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[84] + x[88] + -1.0)
def l356_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[85] + x[89] + -1.0)
def l356_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[86] + x[90] + -1.0)
def l356_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[87] + x[91] + -1.0)
def l356_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[88] + x[92] + -1.0)
def l356_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[89] + x[93] + -1.0)
def l356_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[90] + x[94] + -1.0)
def l356_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[91] + x[95] + -1.0)
def l356_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l356_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l356_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l356_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l356_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l356_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l356_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l356_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l356_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[100])
def l356_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[101])
def l356_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[102])
def l356_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[103])
def l356_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[104])
def l356_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[105])
def l356_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[106])
def l356_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[107])
def l356_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[108])
def l356_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[109])
def l356_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[110])
def l356_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[111])
def l356_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[112])
def l356_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[113])
def l356_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[114])
def l356_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[115])
def l356_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[116])
def l356_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[117])
def l356_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[118])
def l356_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[119])
def l356_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[120])
def l356_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[121])
def l356_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[122])
def l356_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[123])
def l356_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[124])
def l356_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[125])
def l356_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[126])
def l356_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[127])
def l356_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l356_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l356_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l356_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l356_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l356_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l356_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l356_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l356_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l356_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l356_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l356_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l356_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l356_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l356_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l356_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l356_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[144])
def l356_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[145])
def l356_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[146])
def l356_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[147])
def l356_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[148])
def l356_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[149])
def l356_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[150])
def l356_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[151])
def l356_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[152])
def l356_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[153])
def l356_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[154])
def l356_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[155])
def l356_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[156])
def l356_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[157])
def l356_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[158])
def l356_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[159])
def l356_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l356_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l356_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l356_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l356_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l356_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l356_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l356_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l356_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l356_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l356_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l356_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l356_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l356_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l356_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l356_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l356_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l356_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l356_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l356_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l356_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l356_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l356_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l356_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l356_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l356_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l356_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l356_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l356_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l356_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l356_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l356_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l356_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l356_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l356_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l356_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l356_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l356_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l356_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l356_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l356_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l356_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l356_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l356_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l356_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l356_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l356_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l356_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l356_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l356_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l356_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l356_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l356_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l356_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l356_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l356_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l356_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l356_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l356_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l356_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l356_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l356_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l356_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l356_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l356_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l356_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l356_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l356_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l356_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l356_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l356_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l356_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l356_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l356_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l356_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l356_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l356_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l356_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l356_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l356_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l356_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l356_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l356_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l356_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l356_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l356_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l356_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l356_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l356_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l356_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l356_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l356_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l356_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l356_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l356_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l356_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l356_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l356_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l356_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l356_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l356_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l356_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l356_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l356_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l356_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l356_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l356_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l356_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l356_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l356_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l356_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l356_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l356_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l356_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l356_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l356_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l356_304(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l356_305(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l356_306(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l356_307(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l356_308(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l356_309(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l356_310(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l356_311(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l356_312(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l356_313(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l356_314(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l356_315(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l356_(x):
    # x is a list (or vector) of length 288
    return [
        l356_0(x),
        l356_1(x),
        l356_2(x),
        l356_3(x),
        l356_4(x),
        l356_5(x),
        l356_6(x),
        l356_7(x),
        l356_8(x),
        l356_9(x),
        l356_10(x),
        l356_11(x),
        l356_12(x),
        l356_13(x),
        l356_14(x),
        l356_15(x),
        l356_16(x),
        l356_17(x),
        l356_18(x),
        l356_19(x),
        l356_20(x),
        l356_21(x),
        l356_22(x),
        l356_23(x),
        l356_24(x),
        l356_25(x),
        l356_26(x),
        l356_27(x),
        l356_28(x),
        l356_29(x),
        l356_30(x),
        l356_31(x),
        l356_32(x),
        l356_33(x),
        l356_34(x),
        l356_35(x),
        l356_36(x),
        l356_37(x),
        l356_38(x),
        l356_39(x),
        l356_40(x),
        l356_41(x),
        l356_42(x),
        l356_43(x),
        l356_44(x),
        l356_45(x),
        l356_46(x),
        l356_47(x),
        l356_48(x),
        l356_49(x),
        l356_50(x),
        l356_51(x),
        l356_52(x),
        l356_53(x),
        l356_54(x),
        l356_55(x),
        l356_56(x),
        l356_57(x),
        l356_58(x),
        l356_59(x),
        l356_60(x),
        l356_61(x),
        l356_62(x),
        l356_63(x),
        l356_64(x),
        l356_65(x),
        l356_66(x),
        l356_67(x),
        l356_68(x),
        l356_69(x),
        l356_70(x),
        l356_71(x),
        l356_72(x),
        l356_73(x),
        l356_74(x),
        l356_75(x),
        l356_76(x),
        l356_77(x),
        l356_78(x),
        l356_79(x),
        l356_80(x),
        l356_81(x),
        l356_82(x),
        l356_83(x),
        l356_84(x),
        l356_85(x),
        l356_86(x),
        l356_87(x),
        l356_88(x),
        l356_89(x),
        l356_90(x),
        l356_91(x),
        l356_92(x),
        l356_93(x),
        l356_94(x),
        l356_95(x),
        l356_96(x),
        l356_97(x),
        l356_98(x),
        l356_99(x),
        l356_100(x),
        l356_101(x),
        l356_102(x),
        l356_103(x),
        l356_104(x),
        l356_105(x),
        l356_106(x),
        l356_107(x),
        l356_108(x),
        l356_109(x),
        l356_110(x),
        l356_111(x),
        l356_112(x),
        l356_113(x),
        l356_114(x),
        l356_115(x),
        l356_116(x),
        l356_117(x),
        l356_118(x),
        l356_119(x),
        l356_120(x),
        l356_121(x),
        l356_122(x),
        l356_123(x),
        l356_124(x),
        l356_125(x),
        l356_126(x),
        l356_127(x),
        l356_128(x),
        l356_129(x),
        l356_130(x),
        l356_131(x),
        l356_132(x),
        l356_133(x),
        l356_134(x),
        l356_135(x),
        l356_136(x),
        l356_137(x),
        l356_138(x),
        l356_139(x),
        l356_140(x),
        l356_141(x),
        l356_142(x),
        l356_143(x),
        l356_144(x),
        l356_145(x),
        l356_146(x),
        l356_147(x),
        l356_148(x),
        l356_149(x),
        l356_150(x),
        l356_151(x),
        l356_152(x),
        l356_153(x),
        l356_154(x),
        l356_155(x),
        l356_156(x),
        l356_157(x),
        l356_158(x),
        l356_159(x),
        l356_160(x),
        l356_161(x),
        l356_162(x),
        l356_163(x),
        l356_164(x),
        l356_165(x),
        l356_166(x),
        l356_167(x),
        l356_168(x),
        l356_169(x),
        l356_170(x),
        l356_171(x),
        l356_172(x),
        l356_173(x),
        l356_174(x),
        l356_175(x),
        l356_176(x),
        l356_177(x),
        l356_178(x),
        l356_179(x),
        l356_180(x),
        l356_181(x),
        l356_182(x),
        l356_183(x),
        l356_184(x),
        l356_185(x),
        l356_186(x),
        l356_187(x),
        l356_188(x),
        l356_189(x),
        l356_190(x),
        l356_191(x),
        l356_192(x),
        l356_193(x),
        l356_194(x),
        l356_195(x),
        l356_196(x),
        l356_197(x),
        l356_198(x),
        l356_199(x),
        l356_200(x),
        l356_201(x),
        l356_202(x),
        l356_203(x),
        l356_204(x),
        l356_205(x),
        l356_206(x),
        l356_207(x),
        l356_208(x),
        l356_209(x),
        l356_210(x),
        l356_211(x),
        l356_212(x),
        l356_213(x),
        l356_214(x),
        l356_215(x),
        l356_216(x),
        l356_217(x),
        l356_218(x),
        l356_219(x),
        l356_220(x),
        l356_221(x),
        l356_222(x),
        l356_223(x),
        l356_224(x),
        l356_225(x),
        l356_226(x),
        l356_227(x),
        l356_228(x),
        l356_229(x),
        l356_230(x),
        l356_231(x),
        l356_232(x),
        l356_233(x),
        l356_234(x),
        l356_235(x),
        l356_236(x),
        l356_237(x),
        l356_238(x),
        l356_239(x),
        l356_240(x),
        l356_241(x),
        l356_242(x),
        l356_243(x),
        l356_244(x),
        l356_245(x),
        l356_246(x),
        l356_247(x),
        l356_248(x),
        l356_249(x),
        l356_250(x),
        l356_251(x),
        l356_252(x),
        l356_253(x),
        l356_254(x),
        l356_255(x),
        l356_256(x),
        l356_257(x),
        l356_258(x),
        l356_259(x),
        l356_260(x),
        l356_261(x),
        l356_262(x),
        l356_263(x),
        l356_264(x),
        l356_265(x),
        l356_266(x),
        l356_267(x),
        l356_268(x),
        l356_269(x),
        l356_270(x),
        l356_271(x),
        l356_272(x),
        l356_273(x),
        l356_274(x),
        l356_275(x),
        l356_276(x),
        l356_277(x),
        l356_278(x),
        l356_279(x),
        l356_280(x),
        l356_281(x),
        l356_282(x),
        l356_283(x),
        l356_284(x),
        l356_285(x),
        l356_286(x),
        l356_287(x),
        l356_288(x),
        l356_289(x),
        l356_290(x),
        l356_291(x),
        l356_292(x),
        l356_293(x),
        l356_294(x),
        l356_295(x),
        l356_296(x),
        l356_297(x),
        l356_298(x),
        l356_299(x),
        l356_300(x),
        l356_301(x),
        l356_302(x),
        l356_303(x),
        l356_304(x),
        l356_305(x),
        l356_306(x),
        l356_307(x),
        l356_308(x),
        l356_309(x),
        l356_310(x),
        l356_311(x),
        l356_312(x),
        l356_313(x),
        l356_314(x),
        l356_315(x),
    ]