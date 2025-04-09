import numpy as np




# Generated from reverse engineering
def l352_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 318
    out = np.empty(318, dtype=np.float32)
    
    # for i in range(0, 33):
    for i in range(0, 33):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x1 (len=1)
    biases = [1.0]
    # for i in range(33, 34):
    for i in range(0, 1):
        s = -1 * x[33 + i]
        s += biases[i]
        out[33 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0]
    # for i in range(34, 35):
    for i in range(0, 1):
        s = x[32 + i] + x[66 + i]
        s += biases[i]
        out[34 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(35, 64):
    for i in range(0, 29):
        s = x[67 + i] + -1 * x[33 + i]
        out[35 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3fffffff (len=30)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(64, 94):
    for i in range(0, 30):
        s = -1 * x[34 + i]
        s += biases[i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(94, 124):
    for i in range(0, 30):
        s = x[64 + i] + x[66 + i]
        s += biases[i]
        out[94 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(124, 126):
    for i in range(0, 2):
        s = x[64 + i]
        out[124 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(126, 318):
    for i in range(0, 192):
        s = x[96 + i]
        out[126 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l352_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l352_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l352_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l352_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l352_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l352_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l352_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l352_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l352_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l352_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l352_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l352_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l352_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l352_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l352_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l352_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l352_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l352_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l352_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l352_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l352_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l352_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l352_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l352_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l352_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l352_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l352_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l352_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l352_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l352_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l352_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l352_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l352_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l352_33(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[33] + 1.0)
def l352_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[32] + x[66] + -1.0)
def l352_35(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[33] + x[67])
def l352_36(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[34] + x[68])
def l352_37(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[35] + x[69])
def l352_38(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + x[70])
def l352_39(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + x[71])
def l352_40(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + x[72])
def l352_41(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + x[73])
def l352_42(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + x[74])
def l352_43(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + x[75])
def l352_44(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + x[76])
def l352_45(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + x[77])
def l352_46(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + x[78])
def l352_47(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + x[79])
def l352_48(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + x[80])
def l352_49(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + x[81])
def l352_50(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + x[82])
def l352_51(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + x[83])
def l352_52(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + x[84])
def l352_53(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + x[85])
def l352_54(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + x[86])
def l352_55(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + x[87])
def l352_56(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + x[88])
def l352_57(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + x[89])
def l352_58(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + x[90])
def l352_59(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + x[91])
def l352_60(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + x[92])
def l352_61(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + x[93])
def l352_62(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + x[94])
def l352_63(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + x[95])
def l352_64(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[34] + 1.0)
def l352_65(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[35] + 1.0)
def l352_66(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + 1.0)
def l352_67(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + 1.0)
def l352_68(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + 1.0)
def l352_69(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + 1.0)
def l352_70(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + 1.0)
def l352_71(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + 1.0)
def l352_72(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + 1.0)
def l352_73(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + 1.0)
def l352_74(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + 1.0)
def l352_75(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + 1.0)
def l352_76(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + 1.0)
def l352_77(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + 1.0)
def l352_78(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + 1.0)
def l352_79(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + 1.0)
def l352_80(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + 1.0)
def l352_81(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + 1.0)
def l352_82(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + 1.0)
def l352_83(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + 1.0)
def l352_84(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + 1.0)
def l352_85(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + 1.0)
def l352_86(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + 1.0)
def l352_87(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + 1.0)
def l352_88(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + 1.0)
def l352_89(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + 1.0)
def l352_90(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + 1.0)
def l352_91(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + 1.0)
def l352_92(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[62] + 1.0)
def l352_93(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[63] + 1.0)
def l352_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[64] + x[66] + -1.0)
def l352_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[65] + x[67] + -1.0)
def l352_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[66] + x[68] + -1.0)
def l352_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[67] + x[69] + -1.0)
def l352_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[68] + x[70] + -1.0)
def l352_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[69] + x[71] + -1.0)
def l352_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[70] + x[72] + -1.0)
def l352_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[71] + x[73] + -1.0)
def l352_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[72] + x[74] + -1.0)
def l352_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[73] + x[75] + -1.0)
def l352_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[74] + x[76] + -1.0)
def l352_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[75] + x[77] + -1.0)
def l352_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[76] + x[78] + -1.0)
def l352_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[77] + x[79] + -1.0)
def l352_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[78] + x[80] + -1.0)
def l352_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[79] + x[81] + -1.0)
def l352_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[80] + x[82] + -1.0)
def l352_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[81] + x[83] + -1.0)
def l352_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[82] + x[84] + -1.0)
def l352_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[83] + x[85] + -1.0)
def l352_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[84] + x[86] + -1.0)
def l352_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[85] + x[87] + -1.0)
def l352_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[86] + x[88] + -1.0)
def l352_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[87] + x[89] + -1.0)
def l352_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[88] + x[90] + -1.0)
def l352_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[89] + x[91] + -1.0)
def l352_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[90] + x[92] + -1.0)
def l352_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[91] + x[93] + -1.0)
def l352_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[92] + x[94] + -1.0)
def l352_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[93] + x[95] + -1.0)
def l352_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l352_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l352_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l352_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l352_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l352_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l352_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[100])
def l352_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[101])
def l352_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[102])
def l352_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[103])
def l352_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[104])
def l352_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[105])
def l352_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[106])
def l352_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[107])
def l352_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[108])
def l352_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[109])
def l352_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[110])
def l352_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[111])
def l352_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[112])
def l352_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[113])
def l352_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[114])
def l352_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[115])
def l352_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[116])
def l352_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[117])
def l352_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[118])
def l352_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[119])
def l352_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[120])
def l352_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[121])
def l352_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[122])
def l352_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[123])
def l352_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[124])
def l352_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[125])
def l352_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[126])
def l352_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[127])
def l352_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l352_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l352_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l352_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l352_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l352_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l352_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l352_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l352_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l352_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l352_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l352_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l352_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l352_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l352_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l352_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l352_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[144])
def l352_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[145])
def l352_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[146])
def l352_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[147])
def l352_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[148])
def l352_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[149])
def l352_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[150])
def l352_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[151])
def l352_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[152])
def l352_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[153])
def l352_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[154])
def l352_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[155])
def l352_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[156])
def l352_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[157])
def l352_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[158])
def l352_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[159])
def l352_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l352_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l352_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l352_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l352_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l352_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l352_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l352_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l352_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l352_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l352_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l352_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l352_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l352_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l352_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l352_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l352_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l352_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l352_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l352_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l352_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l352_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l352_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l352_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l352_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l352_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l352_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l352_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l352_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l352_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l352_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l352_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l352_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l352_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l352_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l352_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l352_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l352_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l352_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l352_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l352_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l352_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l352_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l352_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l352_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l352_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l352_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l352_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l352_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l352_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l352_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l352_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l352_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l352_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l352_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l352_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l352_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l352_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l352_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l352_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l352_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l352_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l352_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l352_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l352_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l352_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l352_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l352_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l352_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l352_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l352_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l352_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l352_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l352_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l352_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l352_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l352_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l352_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l352_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l352_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l352_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l352_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l352_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l352_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l352_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l352_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l352_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l352_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l352_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l352_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l352_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l352_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l352_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l352_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l352_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l352_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l352_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l352_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l352_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l352_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l352_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l352_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l352_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l352_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l352_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l352_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l352_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l352_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l352_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l352_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l352_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l352_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l352_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l352_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l352_304(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l352_305(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l352_306(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l352_307(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l352_308(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l352_309(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l352_310(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l352_311(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l352_312(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l352_313(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l352_314(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l352_315(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l352_316(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l352_317(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l352_(x):
    # x is a list (or vector) of length 288
    return [
        l352_0(x),
        l352_1(x),
        l352_2(x),
        l352_3(x),
        l352_4(x),
        l352_5(x),
        l352_6(x),
        l352_7(x),
        l352_8(x),
        l352_9(x),
        l352_10(x),
        l352_11(x),
        l352_12(x),
        l352_13(x),
        l352_14(x),
        l352_15(x),
        l352_16(x),
        l352_17(x),
        l352_18(x),
        l352_19(x),
        l352_20(x),
        l352_21(x),
        l352_22(x),
        l352_23(x),
        l352_24(x),
        l352_25(x),
        l352_26(x),
        l352_27(x),
        l352_28(x),
        l352_29(x),
        l352_30(x),
        l352_31(x),
        l352_32(x),
        l352_33(x),
        l352_34(x),
        l352_35(x),
        l352_36(x),
        l352_37(x),
        l352_38(x),
        l352_39(x),
        l352_40(x),
        l352_41(x),
        l352_42(x),
        l352_43(x),
        l352_44(x),
        l352_45(x),
        l352_46(x),
        l352_47(x),
        l352_48(x),
        l352_49(x),
        l352_50(x),
        l352_51(x),
        l352_52(x),
        l352_53(x),
        l352_54(x),
        l352_55(x),
        l352_56(x),
        l352_57(x),
        l352_58(x),
        l352_59(x),
        l352_60(x),
        l352_61(x),
        l352_62(x),
        l352_63(x),
        l352_64(x),
        l352_65(x),
        l352_66(x),
        l352_67(x),
        l352_68(x),
        l352_69(x),
        l352_70(x),
        l352_71(x),
        l352_72(x),
        l352_73(x),
        l352_74(x),
        l352_75(x),
        l352_76(x),
        l352_77(x),
        l352_78(x),
        l352_79(x),
        l352_80(x),
        l352_81(x),
        l352_82(x),
        l352_83(x),
        l352_84(x),
        l352_85(x),
        l352_86(x),
        l352_87(x),
        l352_88(x),
        l352_89(x),
        l352_90(x),
        l352_91(x),
        l352_92(x),
        l352_93(x),
        l352_94(x),
        l352_95(x),
        l352_96(x),
        l352_97(x),
        l352_98(x),
        l352_99(x),
        l352_100(x),
        l352_101(x),
        l352_102(x),
        l352_103(x),
        l352_104(x),
        l352_105(x),
        l352_106(x),
        l352_107(x),
        l352_108(x),
        l352_109(x),
        l352_110(x),
        l352_111(x),
        l352_112(x),
        l352_113(x),
        l352_114(x),
        l352_115(x),
        l352_116(x),
        l352_117(x),
        l352_118(x),
        l352_119(x),
        l352_120(x),
        l352_121(x),
        l352_122(x),
        l352_123(x),
        l352_124(x),
        l352_125(x),
        l352_126(x),
        l352_127(x),
        l352_128(x),
        l352_129(x),
        l352_130(x),
        l352_131(x),
        l352_132(x),
        l352_133(x),
        l352_134(x),
        l352_135(x),
        l352_136(x),
        l352_137(x),
        l352_138(x),
        l352_139(x),
        l352_140(x),
        l352_141(x),
        l352_142(x),
        l352_143(x),
        l352_144(x),
        l352_145(x),
        l352_146(x),
        l352_147(x),
        l352_148(x),
        l352_149(x),
        l352_150(x),
        l352_151(x),
        l352_152(x),
        l352_153(x),
        l352_154(x),
        l352_155(x),
        l352_156(x),
        l352_157(x),
        l352_158(x),
        l352_159(x),
        l352_160(x),
        l352_161(x),
        l352_162(x),
        l352_163(x),
        l352_164(x),
        l352_165(x),
        l352_166(x),
        l352_167(x),
        l352_168(x),
        l352_169(x),
        l352_170(x),
        l352_171(x),
        l352_172(x),
        l352_173(x),
        l352_174(x),
        l352_175(x),
        l352_176(x),
        l352_177(x),
        l352_178(x),
        l352_179(x),
        l352_180(x),
        l352_181(x),
        l352_182(x),
        l352_183(x),
        l352_184(x),
        l352_185(x),
        l352_186(x),
        l352_187(x),
        l352_188(x),
        l352_189(x),
        l352_190(x),
        l352_191(x),
        l352_192(x),
        l352_193(x),
        l352_194(x),
        l352_195(x),
        l352_196(x),
        l352_197(x),
        l352_198(x),
        l352_199(x),
        l352_200(x),
        l352_201(x),
        l352_202(x),
        l352_203(x),
        l352_204(x),
        l352_205(x),
        l352_206(x),
        l352_207(x),
        l352_208(x),
        l352_209(x),
        l352_210(x),
        l352_211(x),
        l352_212(x),
        l352_213(x),
        l352_214(x),
        l352_215(x),
        l352_216(x),
        l352_217(x),
        l352_218(x),
        l352_219(x),
        l352_220(x),
        l352_221(x),
        l352_222(x),
        l352_223(x),
        l352_224(x),
        l352_225(x),
        l352_226(x),
        l352_227(x),
        l352_228(x),
        l352_229(x),
        l352_230(x),
        l352_231(x),
        l352_232(x),
        l352_233(x),
        l352_234(x),
        l352_235(x),
        l352_236(x),
        l352_237(x),
        l352_238(x),
        l352_239(x),
        l352_240(x),
        l352_241(x),
        l352_242(x),
        l352_243(x),
        l352_244(x),
        l352_245(x),
        l352_246(x),
        l352_247(x),
        l352_248(x),
        l352_249(x),
        l352_250(x),
        l352_251(x),
        l352_252(x),
        l352_253(x),
        l352_254(x),
        l352_255(x),
        l352_256(x),
        l352_257(x),
        l352_258(x),
        l352_259(x),
        l352_260(x),
        l352_261(x),
        l352_262(x),
        l352_263(x),
        l352_264(x),
        l352_265(x),
        l352_266(x),
        l352_267(x),
        l352_268(x),
        l352_269(x),
        l352_270(x),
        l352_271(x),
        l352_272(x),
        l352_273(x),
        l352_274(x),
        l352_275(x),
        l352_276(x),
        l352_277(x),
        l352_278(x),
        l352_279(x),
        l352_280(x),
        l352_281(x),
        l352_282(x),
        l352_283(x),
        l352_284(x),
        l352_285(x),
        l352_286(x),
        l352_287(x),
        l352_288(x),
        l352_289(x),
        l352_290(x),
        l352_291(x),
        l352_292(x),
        l352_293(x),
        l352_294(x),
        l352_295(x),
        l352_296(x),
        l352_297(x),
        l352_298(x),
        l352_299(x),
        l352_300(x),
        l352_301(x),
        l352_302(x),
        l352_303(x),
        l352_304(x),
        l352_305(x),
        l352_306(x),
        l352_307(x),
        l352_308(x),
        l352_309(x),
        l352_310(x),
        l352_311(x),
        l352_312(x),
        l352_313(x),
        l352_314(x),
        l352_315(x),
        l352_316(x),
        l352_317(x),
    ]