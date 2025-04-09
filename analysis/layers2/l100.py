import numpy as np




# Generated from reverse engineering
def l100_g(x: np.ndarray) -> np.ndarray:
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




def l100_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l100_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l100_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l100_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l100_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l100_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l100_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l100_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l100_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l100_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l100_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l100_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l100_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l100_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l100_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l100_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l100_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l100_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l100_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l100_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l100_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l100_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l100_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l100_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l100_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l100_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l100_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l100_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l100_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l100_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l100_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l100_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l100_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l100_33(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[33] + 1.0)
def l100_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[32] + x[66] + -1.0)
def l100_35(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[33] + x[67])
def l100_36(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[34] + x[68])
def l100_37(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[35] + x[69])
def l100_38(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + x[70])
def l100_39(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + x[71])
def l100_40(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + x[72])
def l100_41(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + x[73])
def l100_42(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + x[74])
def l100_43(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + x[75])
def l100_44(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + x[76])
def l100_45(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + x[77])
def l100_46(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + x[78])
def l100_47(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + x[79])
def l100_48(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + x[80])
def l100_49(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + x[81])
def l100_50(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + x[82])
def l100_51(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + x[83])
def l100_52(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + x[84])
def l100_53(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + x[85])
def l100_54(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + x[86])
def l100_55(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + x[87])
def l100_56(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + x[88])
def l100_57(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + x[89])
def l100_58(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + x[90])
def l100_59(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + x[91])
def l100_60(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + x[92])
def l100_61(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + x[93])
def l100_62(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + x[94])
def l100_63(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + x[95])
def l100_64(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[34] + 1.0)
def l100_65(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[35] + 1.0)
def l100_66(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + 1.0)
def l100_67(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + 1.0)
def l100_68(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + 1.0)
def l100_69(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + 1.0)
def l100_70(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + 1.0)
def l100_71(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + 1.0)
def l100_72(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + 1.0)
def l100_73(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + 1.0)
def l100_74(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + 1.0)
def l100_75(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + 1.0)
def l100_76(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + 1.0)
def l100_77(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + 1.0)
def l100_78(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + 1.0)
def l100_79(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + 1.0)
def l100_80(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + 1.0)
def l100_81(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + 1.0)
def l100_82(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + 1.0)
def l100_83(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + 1.0)
def l100_84(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + 1.0)
def l100_85(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + 1.0)
def l100_86(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + 1.0)
def l100_87(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + 1.0)
def l100_88(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + 1.0)
def l100_89(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + 1.0)
def l100_90(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + 1.0)
def l100_91(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + 1.0)
def l100_92(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[62] + 1.0)
def l100_93(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[63] + 1.0)
def l100_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[64] + x[66] + -1.0)
def l100_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[65] + x[67] + -1.0)
def l100_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[66] + x[68] + -1.0)
def l100_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[67] + x[69] + -1.0)
def l100_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[68] + x[70] + -1.0)
def l100_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[69] + x[71] + -1.0)
def l100_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[70] + x[72] + -1.0)
def l100_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[71] + x[73] + -1.0)
def l100_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[72] + x[74] + -1.0)
def l100_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[73] + x[75] + -1.0)
def l100_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[74] + x[76] + -1.0)
def l100_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[75] + x[77] + -1.0)
def l100_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[76] + x[78] + -1.0)
def l100_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[77] + x[79] + -1.0)
def l100_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[78] + x[80] + -1.0)
def l100_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[79] + x[81] + -1.0)
def l100_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[80] + x[82] + -1.0)
def l100_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[81] + x[83] + -1.0)
def l100_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[82] + x[84] + -1.0)
def l100_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[83] + x[85] + -1.0)
def l100_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[84] + x[86] + -1.0)
def l100_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[85] + x[87] + -1.0)
def l100_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[86] + x[88] + -1.0)
def l100_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[87] + x[89] + -1.0)
def l100_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[88] + x[90] + -1.0)
def l100_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[89] + x[91] + -1.0)
def l100_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[90] + x[92] + -1.0)
def l100_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[91] + x[93] + -1.0)
def l100_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[92] + x[94] + -1.0)
def l100_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[93] + x[95] + -1.0)
def l100_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l100_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l100_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l100_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l100_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l100_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l100_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[100])
def l100_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[101])
def l100_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[102])
def l100_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[103])
def l100_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[104])
def l100_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[105])
def l100_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[106])
def l100_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[107])
def l100_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[108])
def l100_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[109])
def l100_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[110])
def l100_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[111])
def l100_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[112])
def l100_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[113])
def l100_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[114])
def l100_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[115])
def l100_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[116])
def l100_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[117])
def l100_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[118])
def l100_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[119])
def l100_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[120])
def l100_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[121])
def l100_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[122])
def l100_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[123])
def l100_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[124])
def l100_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[125])
def l100_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[126])
def l100_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[127])
def l100_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l100_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l100_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l100_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l100_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l100_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l100_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l100_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l100_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l100_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l100_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l100_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l100_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l100_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l100_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l100_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l100_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[144])
def l100_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[145])
def l100_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[146])
def l100_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[147])
def l100_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[148])
def l100_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[149])
def l100_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[150])
def l100_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[151])
def l100_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[152])
def l100_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[153])
def l100_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[154])
def l100_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[155])
def l100_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[156])
def l100_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[157])
def l100_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[158])
def l100_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[159])
def l100_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l100_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l100_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l100_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l100_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l100_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l100_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l100_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l100_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l100_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l100_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l100_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l100_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l100_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l100_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l100_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l100_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l100_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l100_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l100_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l100_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l100_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l100_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l100_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l100_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l100_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l100_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l100_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l100_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l100_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l100_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l100_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l100_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l100_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l100_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l100_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l100_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l100_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l100_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l100_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l100_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l100_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l100_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l100_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l100_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l100_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l100_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l100_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l100_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l100_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l100_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l100_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l100_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l100_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l100_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l100_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l100_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l100_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l100_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l100_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l100_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l100_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l100_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l100_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l100_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l100_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l100_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l100_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l100_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l100_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l100_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l100_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l100_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l100_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l100_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l100_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l100_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l100_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l100_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l100_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l100_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l100_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l100_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l100_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l100_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l100_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l100_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l100_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l100_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l100_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l100_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l100_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l100_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l100_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l100_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l100_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l100_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l100_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l100_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l100_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l100_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l100_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l100_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l100_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l100_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l100_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l100_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l100_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l100_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l100_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l100_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l100_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l100_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l100_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l100_304(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l100_305(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l100_306(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l100_307(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l100_308(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l100_309(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l100_310(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l100_311(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l100_312(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l100_313(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l100_314(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l100_315(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l100_316(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l100_317(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l100_(x):
    # x is a list (or vector) of length 288
    return [
        l100_0(x),
        l100_1(x),
        l100_2(x),
        l100_3(x),
        l100_4(x),
        l100_5(x),
        l100_6(x),
        l100_7(x),
        l100_8(x),
        l100_9(x),
        l100_10(x),
        l100_11(x),
        l100_12(x),
        l100_13(x),
        l100_14(x),
        l100_15(x),
        l100_16(x),
        l100_17(x),
        l100_18(x),
        l100_19(x),
        l100_20(x),
        l100_21(x),
        l100_22(x),
        l100_23(x),
        l100_24(x),
        l100_25(x),
        l100_26(x),
        l100_27(x),
        l100_28(x),
        l100_29(x),
        l100_30(x),
        l100_31(x),
        l100_32(x),
        l100_33(x),
        l100_34(x),
        l100_35(x),
        l100_36(x),
        l100_37(x),
        l100_38(x),
        l100_39(x),
        l100_40(x),
        l100_41(x),
        l100_42(x),
        l100_43(x),
        l100_44(x),
        l100_45(x),
        l100_46(x),
        l100_47(x),
        l100_48(x),
        l100_49(x),
        l100_50(x),
        l100_51(x),
        l100_52(x),
        l100_53(x),
        l100_54(x),
        l100_55(x),
        l100_56(x),
        l100_57(x),
        l100_58(x),
        l100_59(x),
        l100_60(x),
        l100_61(x),
        l100_62(x),
        l100_63(x),
        l100_64(x),
        l100_65(x),
        l100_66(x),
        l100_67(x),
        l100_68(x),
        l100_69(x),
        l100_70(x),
        l100_71(x),
        l100_72(x),
        l100_73(x),
        l100_74(x),
        l100_75(x),
        l100_76(x),
        l100_77(x),
        l100_78(x),
        l100_79(x),
        l100_80(x),
        l100_81(x),
        l100_82(x),
        l100_83(x),
        l100_84(x),
        l100_85(x),
        l100_86(x),
        l100_87(x),
        l100_88(x),
        l100_89(x),
        l100_90(x),
        l100_91(x),
        l100_92(x),
        l100_93(x),
        l100_94(x),
        l100_95(x),
        l100_96(x),
        l100_97(x),
        l100_98(x),
        l100_99(x),
        l100_100(x),
        l100_101(x),
        l100_102(x),
        l100_103(x),
        l100_104(x),
        l100_105(x),
        l100_106(x),
        l100_107(x),
        l100_108(x),
        l100_109(x),
        l100_110(x),
        l100_111(x),
        l100_112(x),
        l100_113(x),
        l100_114(x),
        l100_115(x),
        l100_116(x),
        l100_117(x),
        l100_118(x),
        l100_119(x),
        l100_120(x),
        l100_121(x),
        l100_122(x),
        l100_123(x),
        l100_124(x),
        l100_125(x),
        l100_126(x),
        l100_127(x),
        l100_128(x),
        l100_129(x),
        l100_130(x),
        l100_131(x),
        l100_132(x),
        l100_133(x),
        l100_134(x),
        l100_135(x),
        l100_136(x),
        l100_137(x),
        l100_138(x),
        l100_139(x),
        l100_140(x),
        l100_141(x),
        l100_142(x),
        l100_143(x),
        l100_144(x),
        l100_145(x),
        l100_146(x),
        l100_147(x),
        l100_148(x),
        l100_149(x),
        l100_150(x),
        l100_151(x),
        l100_152(x),
        l100_153(x),
        l100_154(x),
        l100_155(x),
        l100_156(x),
        l100_157(x),
        l100_158(x),
        l100_159(x),
        l100_160(x),
        l100_161(x),
        l100_162(x),
        l100_163(x),
        l100_164(x),
        l100_165(x),
        l100_166(x),
        l100_167(x),
        l100_168(x),
        l100_169(x),
        l100_170(x),
        l100_171(x),
        l100_172(x),
        l100_173(x),
        l100_174(x),
        l100_175(x),
        l100_176(x),
        l100_177(x),
        l100_178(x),
        l100_179(x),
        l100_180(x),
        l100_181(x),
        l100_182(x),
        l100_183(x),
        l100_184(x),
        l100_185(x),
        l100_186(x),
        l100_187(x),
        l100_188(x),
        l100_189(x),
        l100_190(x),
        l100_191(x),
        l100_192(x),
        l100_193(x),
        l100_194(x),
        l100_195(x),
        l100_196(x),
        l100_197(x),
        l100_198(x),
        l100_199(x),
        l100_200(x),
        l100_201(x),
        l100_202(x),
        l100_203(x),
        l100_204(x),
        l100_205(x),
        l100_206(x),
        l100_207(x),
        l100_208(x),
        l100_209(x),
        l100_210(x),
        l100_211(x),
        l100_212(x),
        l100_213(x),
        l100_214(x),
        l100_215(x),
        l100_216(x),
        l100_217(x),
        l100_218(x),
        l100_219(x),
        l100_220(x),
        l100_221(x),
        l100_222(x),
        l100_223(x),
        l100_224(x),
        l100_225(x),
        l100_226(x),
        l100_227(x),
        l100_228(x),
        l100_229(x),
        l100_230(x),
        l100_231(x),
        l100_232(x),
        l100_233(x),
        l100_234(x),
        l100_235(x),
        l100_236(x),
        l100_237(x),
        l100_238(x),
        l100_239(x),
        l100_240(x),
        l100_241(x),
        l100_242(x),
        l100_243(x),
        l100_244(x),
        l100_245(x),
        l100_246(x),
        l100_247(x),
        l100_248(x),
        l100_249(x),
        l100_250(x),
        l100_251(x),
        l100_252(x),
        l100_253(x),
        l100_254(x),
        l100_255(x),
        l100_256(x),
        l100_257(x),
        l100_258(x),
        l100_259(x),
        l100_260(x),
        l100_261(x),
        l100_262(x),
        l100_263(x),
        l100_264(x),
        l100_265(x),
        l100_266(x),
        l100_267(x),
        l100_268(x),
        l100_269(x),
        l100_270(x),
        l100_271(x),
        l100_272(x),
        l100_273(x),
        l100_274(x),
        l100_275(x),
        l100_276(x),
        l100_277(x),
        l100_278(x),
        l100_279(x),
        l100_280(x),
        l100_281(x),
        l100_282(x),
        l100_283(x),
        l100_284(x),
        l100_285(x),
        l100_286(x),
        l100_287(x),
        l100_288(x),
        l100_289(x),
        l100_290(x),
        l100_291(x),
        l100_292(x),
        l100_293(x),
        l100_294(x),
        l100_295(x),
        l100_296(x),
        l100_297(x),
        l100_298(x),
        l100_299(x),
        l100_300(x),
        l100_301(x),
        l100_302(x),
        l100_303(x),
        l100_304(x),
        l100_305(x),
        l100_306(x),
        l100_307(x),
        l100_308(x),
        l100_309(x),
        l100_310(x),
        l100_311(x),
        l100_312(x),
        l100_313(x),
        l100_314(x),
        l100_315(x),
        l100_316(x),
        l100_317(x),
    ]