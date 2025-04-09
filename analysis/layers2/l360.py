import numpy as np




# Generated from reverse engineering
def l360_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 312
    out = np.empty(312, dtype=np.float32)
    
    # for i in range(0, 36):
    for i in range(0, 36):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xf (len=4)
    biases = [1.0, 1.0, 1.0, 1.0]
    # for i in range(36, 40):
    for i in range(0, 4):
        s = -1 * x[36 + i]
        s += biases[i]
        out[36 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0]
    # for i in range(40, 44):
    for i in range(0, 4):
        s = x[32 + i] + x[72 + i]
        s += biases[i]
        out[40 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(44, 64):
    for i in range(0, 20):
        s = x[76 + i] + -1 * x[36 + i]
        out[44 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffffff (len=24)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(64, 88):
    for i in range(0, 24):
        s = -1 * x[40 + i]
        s += biases[i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(88, 112):
    for i in range(0, 24):
        s = x[64 + i] + x[72 + i]
        s += biases[i]
        out[88 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(112, 120):
    for i in range(0, 8):
        s = x[64 + i]
        out[112 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(120, 312):
    for i in range(0, 192):
        s = x[96 + i]
        out[120 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l360_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l360_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l360_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l360_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l360_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l360_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l360_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l360_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l360_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l360_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l360_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l360_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l360_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l360_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l360_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l360_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l360_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l360_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l360_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l360_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l360_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l360_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l360_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l360_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l360_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l360_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l360_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l360_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l360_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l360_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l360_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l360_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l360_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l360_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l360_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l360_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l360_36(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + 1.0)
def l360_37(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + 1.0)
def l360_38(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + 1.0)
def l360_39(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + 1.0)
def l360_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[32] + x[72] + -1.0)
def l360_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[33] + x[73] + -1.0)
def l360_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[34] + x[74] + -1.0)
def l360_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[35] + x[75] + -1.0)
def l360_44(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + x[76])
def l360_45(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + x[77])
def l360_46(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + x[78])
def l360_47(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + x[79])
def l360_48(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + x[80])
def l360_49(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + x[81])
def l360_50(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + x[82])
def l360_51(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + x[83])
def l360_52(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + x[84])
def l360_53(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + x[85])
def l360_54(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + x[86])
def l360_55(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + x[87])
def l360_56(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + x[88])
def l360_57(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + x[89])
def l360_58(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + x[90])
def l360_59(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + x[91])
def l360_60(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + x[92])
def l360_61(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + x[93])
def l360_62(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + x[94])
def l360_63(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + x[95])
def l360_64(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + 1.0)
def l360_65(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + 1.0)
def l360_66(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + 1.0)
def l360_67(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + 1.0)
def l360_68(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + 1.0)
def l360_69(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + 1.0)
def l360_70(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + 1.0)
def l360_71(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + 1.0)
def l360_72(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + 1.0)
def l360_73(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + 1.0)
def l360_74(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + 1.0)
def l360_75(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + 1.0)
def l360_76(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + 1.0)
def l360_77(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + 1.0)
def l360_78(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + 1.0)
def l360_79(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + 1.0)
def l360_80(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + 1.0)
def l360_81(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + 1.0)
def l360_82(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + 1.0)
def l360_83(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + 1.0)
def l360_84(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + 1.0)
def l360_85(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + 1.0)
def l360_86(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[62] + 1.0)
def l360_87(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[63] + 1.0)
def l360_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[64] + x[72] + -1.0)
def l360_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[65] + x[73] + -1.0)
def l360_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[66] + x[74] + -1.0)
def l360_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[67] + x[75] + -1.0)
def l360_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[68] + x[76] + -1.0)
def l360_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[69] + x[77] + -1.0)
def l360_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[70] + x[78] + -1.0)
def l360_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[71] + x[79] + -1.0)
def l360_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[72] + x[80] + -1.0)
def l360_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[73] + x[81] + -1.0)
def l360_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[74] + x[82] + -1.0)
def l360_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[75] + x[83] + -1.0)
def l360_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[76] + x[84] + -1.0)
def l360_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[77] + x[85] + -1.0)
def l360_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[78] + x[86] + -1.0)
def l360_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[79] + x[87] + -1.0)
def l360_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[80] + x[88] + -1.0)
def l360_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[81] + x[89] + -1.0)
def l360_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[82] + x[90] + -1.0)
def l360_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[83] + x[91] + -1.0)
def l360_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[84] + x[92] + -1.0)
def l360_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[85] + x[93] + -1.0)
def l360_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[86] + x[94] + -1.0)
def l360_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[87] + x[95] + -1.0)
def l360_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l360_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l360_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l360_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l360_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l360_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l360_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l360_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l360_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l360_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l360_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l360_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l360_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[100])
def l360_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[101])
def l360_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[102])
def l360_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[103])
def l360_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[104])
def l360_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[105])
def l360_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[106])
def l360_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[107])
def l360_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[108])
def l360_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[109])
def l360_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[110])
def l360_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[111])
def l360_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[112])
def l360_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[113])
def l360_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[114])
def l360_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[115])
def l360_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[116])
def l360_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[117])
def l360_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[118])
def l360_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[119])
def l360_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[120])
def l360_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[121])
def l360_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[122])
def l360_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[123])
def l360_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[124])
def l360_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[125])
def l360_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[126])
def l360_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[127])
def l360_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l360_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l360_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l360_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l360_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l360_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l360_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l360_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l360_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l360_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l360_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l360_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l360_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l360_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l360_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l360_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l360_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[144])
def l360_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[145])
def l360_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[146])
def l360_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[147])
def l360_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[148])
def l360_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[149])
def l360_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[150])
def l360_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[151])
def l360_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[152])
def l360_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[153])
def l360_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[154])
def l360_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[155])
def l360_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[156])
def l360_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[157])
def l360_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[158])
def l360_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[159])
def l360_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l360_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l360_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l360_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l360_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l360_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l360_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l360_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l360_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l360_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l360_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l360_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l360_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l360_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l360_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l360_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l360_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l360_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l360_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l360_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l360_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l360_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l360_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l360_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l360_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l360_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l360_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l360_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l360_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l360_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l360_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l360_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l360_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l360_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l360_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l360_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l360_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l360_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l360_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l360_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l360_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l360_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l360_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l360_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l360_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l360_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l360_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l360_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l360_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l360_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l360_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l360_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l360_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l360_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l360_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l360_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l360_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l360_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l360_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l360_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l360_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l360_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l360_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l360_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l360_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l360_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l360_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l360_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l360_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l360_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l360_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l360_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l360_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l360_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l360_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l360_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l360_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l360_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l360_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l360_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l360_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l360_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l360_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l360_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l360_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l360_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l360_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l360_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l360_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l360_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l360_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l360_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l360_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l360_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l360_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l360_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l360_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l360_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l360_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l360_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l360_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l360_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l360_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l360_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l360_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l360_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l360_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l360_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l360_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l360_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l360_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l360_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l360_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l360_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l360_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l360_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l360_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l360_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l360_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l360_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l360_304(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l360_305(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l360_306(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l360_307(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l360_308(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l360_309(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l360_310(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l360_311(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l360_(x):
    # x is a list (or vector) of length 288
    return [
        l360_0(x),
        l360_1(x),
        l360_2(x),
        l360_3(x),
        l360_4(x),
        l360_5(x),
        l360_6(x),
        l360_7(x),
        l360_8(x),
        l360_9(x),
        l360_10(x),
        l360_11(x),
        l360_12(x),
        l360_13(x),
        l360_14(x),
        l360_15(x),
        l360_16(x),
        l360_17(x),
        l360_18(x),
        l360_19(x),
        l360_20(x),
        l360_21(x),
        l360_22(x),
        l360_23(x),
        l360_24(x),
        l360_25(x),
        l360_26(x),
        l360_27(x),
        l360_28(x),
        l360_29(x),
        l360_30(x),
        l360_31(x),
        l360_32(x),
        l360_33(x),
        l360_34(x),
        l360_35(x),
        l360_36(x),
        l360_37(x),
        l360_38(x),
        l360_39(x),
        l360_40(x),
        l360_41(x),
        l360_42(x),
        l360_43(x),
        l360_44(x),
        l360_45(x),
        l360_46(x),
        l360_47(x),
        l360_48(x),
        l360_49(x),
        l360_50(x),
        l360_51(x),
        l360_52(x),
        l360_53(x),
        l360_54(x),
        l360_55(x),
        l360_56(x),
        l360_57(x),
        l360_58(x),
        l360_59(x),
        l360_60(x),
        l360_61(x),
        l360_62(x),
        l360_63(x),
        l360_64(x),
        l360_65(x),
        l360_66(x),
        l360_67(x),
        l360_68(x),
        l360_69(x),
        l360_70(x),
        l360_71(x),
        l360_72(x),
        l360_73(x),
        l360_74(x),
        l360_75(x),
        l360_76(x),
        l360_77(x),
        l360_78(x),
        l360_79(x),
        l360_80(x),
        l360_81(x),
        l360_82(x),
        l360_83(x),
        l360_84(x),
        l360_85(x),
        l360_86(x),
        l360_87(x),
        l360_88(x),
        l360_89(x),
        l360_90(x),
        l360_91(x),
        l360_92(x),
        l360_93(x),
        l360_94(x),
        l360_95(x),
        l360_96(x),
        l360_97(x),
        l360_98(x),
        l360_99(x),
        l360_100(x),
        l360_101(x),
        l360_102(x),
        l360_103(x),
        l360_104(x),
        l360_105(x),
        l360_106(x),
        l360_107(x),
        l360_108(x),
        l360_109(x),
        l360_110(x),
        l360_111(x),
        l360_112(x),
        l360_113(x),
        l360_114(x),
        l360_115(x),
        l360_116(x),
        l360_117(x),
        l360_118(x),
        l360_119(x),
        l360_120(x),
        l360_121(x),
        l360_122(x),
        l360_123(x),
        l360_124(x),
        l360_125(x),
        l360_126(x),
        l360_127(x),
        l360_128(x),
        l360_129(x),
        l360_130(x),
        l360_131(x),
        l360_132(x),
        l360_133(x),
        l360_134(x),
        l360_135(x),
        l360_136(x),
        l360_137(x),
        l360_138(x),
        l360_139(x),
        l360_140(x),
        l360_141(x),
        l360_142(x),
        l360_143(x),
        l360_144(x),
        l360_145(x),
        l360_146(x),
        l360_147(x),
        l360_148(x),
        l360_149(x),
        l360_150(x),
        l360_151(x),
        l360_152(x),
        l360_153(x),
        l360_154(x),
        l360_155(x),
        l360_156(x),
        l360_157(x),
        l360_158(x),
        l360_159(x),
        l360_160(x),
        l360_161(x),
        l360_162(x),
        l360_163(x),
        l360_164(x),
        l360_165(x),
        l360_166(x),
        l360_167(x),
        l360_168(x),
        l360_169(x),
        l360_170(x),
        l360_171(x),
        l360_172(x),
        l360_173(x),
        l360_174(x),
        l360_175(x),
        l360_176(x),
        l360_177(x),
        l360_178(x),
        l360_179(x),
        l360_180(x),
        l360_181(x),
        l360_182(x),
        l360_183(x),
        l360_184(x),
        l360_185(x),
        l360_186(x),
        l360_187(x),
        l360_188(x),
        l360_189(x),
        l360_190(x),
        l360_191(x),
        l360_192(x),
        l360_193(x),
        l360_194(x),
        l360_195(x),
        l360_196(x),
        l360_197(x),
        l360_198(x),
        l360_199(x),
        l360_200(x),
        l360_201(x),
        l360_202(x),
        l360_203(x),
        l360_204(x),
        l360_205(x),
        l360_206(x),
        l360_207(x),
        l360_208(x),
        l360_209(x),
        l360_210(x),
        l360_211(x),
        l360_212(x),
        l360_213(x),
        l360_214(x),
        l360_215(x),
        l360_216(x),
        l360_217(x),
        l360_218(x),
        l360_219(x),
        l360_220(x),
        l360_221(x),
        l360_222(x),
        l360_223(x),
        l360_224(x),
        l360_225(x),
        l360_226(x),
        l360_227(x),
        l360_228(x),
        l360_229(x),
        l360_230(x),
        l360_231(x),
        l360_232(x),
        l360_233(x),
        l360_234(x),
        l360_235(x),
        l360_236(x),
        l360_237(x),
        l360_238(x),
        l360_239(x),
        l360_240(x),
        l360_241(x),
        l360_242(x),
        l360_243(x),
        l360_244(x),
        l360_245(x),
        l360_246(x),
        l360_247(x),
        l360_248(x),
        l360_249(x),
        l360_250(x),
        l360_251(x),
        l360_252(x),
        l360_253(x),
        l360_254(x),
        l360_255(x),
        l360_256(x),
        l360_257(x),
        l360_258(x),
        l360_259(x),
        l360_260(x),
        l360_261(x),
        l360_262(x),
        l360_263(x),
        l360_264(x),
        l360_265(x),
        l360_266(x),
        l360_267(x),
        l360_268(x),
        l360_269(x),
        l360_270(x),
        l360_271(x),
        l360_272(x),
        l360_273(x),
        l360_274(x),
        l360_275(x),
        l360_276(x),
        l360_277(x),
        l360_278(x),
        l360_279(x),
        l360_280(x),
        l360_281(x),
        l360_282(x),
        l360_283(x),
        l360_284(x),
        l360_285(x),
        l360_286(x),
        l360_287(x),
        l360_288(x),
        l360_289(x),
        l360_290(x),
        l360_291(x),
        l360_292(x),
        l360_293(x),
        l360_294(x),
        l360_295(x),
        l360_296(x),
        l360_297(x),
        l360_298(x),
        l360_299(x),
        l360_300(x),
        l360_301(x),
        l360_302(x),
        l360_303(x),
        l360_304(x),
        l360_305(x),
        l360_306(x),
        l360_307(x),
        l360_308(x),
        l360_309(x),
        l360_310(x),
        l360_311(x),
    ]