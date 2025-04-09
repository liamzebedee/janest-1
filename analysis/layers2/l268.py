import numpy as np




# Generated from reverse engineering
def l268_g(x: np.ndarray) -> np.ndarray:
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




def l268_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l268_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l268_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l268_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l268_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l268_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l268_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l268_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l268_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l268_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l268_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l268_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l268_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l268_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l268_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l268_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l268_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l268_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l268_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l268_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l268_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l268_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l268_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l268_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l268_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l268_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l268_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l268_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l268_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l268_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l268_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l268_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l268_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l268_33(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[33] + 1.0)
def l268_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[32] + x[66] + -1.0)
def l268_35(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[33] + x[67])
def l268_36(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[34] + x[68])
def l268_37(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[35] + x[69])
def l268_38(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + x[70])
def l268_39(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + x[71])
def l268_40(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + x[72])
def l268_41(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + x[73])
def l268_42(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + x[74])
def l268_43(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + x[75])
def l268_44(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + x[76])
def l268_45(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + x[77])
def l268_46(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + x[78])
def l268_47(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + x[79])
def l268_48(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + x[80])
def l268_49(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + x[81])
def l268_50(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + x[82])
def l268_51(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + x[83])
def l268_52(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + x[84])
def l268_53(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + x[85])
def l268_54(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + x[86])
def l268_55(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + x[87])
def l268_56(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + x[88])
def l268_57(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + x[89])
def l268_58(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + x[90])
def l268_59(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + x[91])
def l268_60(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + x[92])
def l268_61(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + x[93])
def l268_62(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + x[94])
def l268_63(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + x[95])
def l268_64(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[34] + 1.0)
def l268_65(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[35] + 1.0)
def l268_66(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + 1.0)
def l268_67(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + 1.0)
def l268_68(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + 1.0)
def l268_69(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + 1.0)
def l268_70(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + 1.0)
def l268_71(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + 1.0)
def l268_72(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + 1.0)
def l268_73(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + 1.0)
def l268_74(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + 1.0)
def l268_75(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + 1.0)
def l268_76(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + 1.0)
def l268_77(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + 1.0)
def l268_78(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + 1.0)
def l268_79(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + 1.0)
def l268_80(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + 1.0)
def l268_81(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + 1.0)
def l268_82(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + 1.0)
def l268_83(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + 1.0)
def l268_84(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + 1.0)
def l268_85(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + 1.0)
def l268_86(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + 1.0)
def l268_87(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + 1.0)
def l268_88(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + 1.0)
def l268_89(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + 1.0)
def l268_90(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + 1.0)
def l268_91(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + 1.0)
def l268_92(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[62] + 1.0)
def l268_93(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[63] + 1.0)
def l268_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[64] + x[66] + -1.0)
def l268_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[65] + x[67] + -1.0)
def l268_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[66] + x[68] + -1.0)
def l268_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[67] + x[69] + -1.0)
def l268_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[68] + x[70] + -1.0)
def l268_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[69] + x[71] + -1.0)
def l268_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[70] + x[72] + -1.0)
def l268_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[71] + x[73] + -1.0)
def l268_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[72] + x[74] + -1.0)
def l268_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[73] + x[75] + -1.0)
def l268_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[74] + x[76] + -1.0)
def l268_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[75] + x[77] + -1.0)
def l268_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[76] + x[78] + -1.0)
def l268_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[77] + x[79] + -1.0)
def l268_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[78] + x[80] + -1.0)
def l268_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[79] + x[81] + -1.0)
def l268_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[80] + x[82] + -1.0)
def l268_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[81] + x[83] + -1.0)
def l268_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[82] + x[84] + -1.0)
def l268_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[83] + x[85] + -1.0)
def l268_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[84] + x[86] + -1.0)
def l268_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[85] + x[87] + -1.0)
def l268_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[86] + x[88] + -1.0)
def l268_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[87] + x[89] + -1.0)
def l268_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[88] + x[90] + -1.0)
def l268_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[89] + x[91] + -1.0)
def l268_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[90] + x[92] + -1.0)
def l268_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[91] + x[93] + -1.0)
def l268_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[92] + x[94] + -1.0)
def l268_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[93] + x[95] + -1.0)
def l268_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l268_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l268_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l268_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l268_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l268_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l268_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[100])
def l268_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[101])
def l268_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[102])
def l268_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[103])
def l268_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[104])
def l268_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[105])
def l268_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[106])
def l268_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[107])
def l268_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[108])
def l268_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[109])
def l268_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[110])
def l268_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[111])
def l268_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[112])
def l268_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[113])
def l268_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[114])
def l268_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[115])
def l268_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[116])
def l268_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[117])
def l268_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[118])
def l268_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[119])
def l268_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[120])
def l268_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[121])
def l268_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[122])
def l268_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[123])
def l268_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[124])
def l268_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[125])
def l268_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[126])
def l268_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[127])
def l268_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l268_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l268_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l268_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l268_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l268_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l268_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l268_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l268_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l268_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l268_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l268_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l268_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l268_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l268_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l268_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l268_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[144])
def l268_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[145])
def l268_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[146])
def l268_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[147])
def l268_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[148])
def l268_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[149])
def l268_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[150])
def l268_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[151])
def l268_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[152])
def l268_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[153])
def l268_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[154])
def l268_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[155])
def l268_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[156])
def l268_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[157])
def l268_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[158])
def l268_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[159])
def l268_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l268_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l268_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l268_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l268_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l268_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l268_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l268_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l268_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l268_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l268_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l268_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l268_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l268_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l268_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l268_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l268_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l268_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l268_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l268_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l268_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l268_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l268_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l268_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l268_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l268_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l268_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l268_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l268_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l268_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l268_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l268_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l268_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l268_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l268_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l268_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l268_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l268_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l268_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l268_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l268_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l268_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l268_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l268_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l268_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l268_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l268_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l268_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l268_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l268_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l268_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l268_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l268_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l268_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l268_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l268_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l268_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l268_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l268_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l268_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l268_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l268_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l268_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l268_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l268_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l268_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l268_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l268_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l268_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l268_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l268_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l268_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l268_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l268_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l268_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l268_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l268_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l268_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l268_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l268_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l268_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l268_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l268_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l268_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l268_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l268_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l268_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l268_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l268_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l268_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l268_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l268_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l268_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l268_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l268_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l268_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l268_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l268_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l268_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l268_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l268_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l268_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l268_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l268_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l268_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l268_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l268_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l268_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l268_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l268_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l268_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l268_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l268_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l268_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l268_304(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l268_305(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l268_306(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l268_307(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l268_308(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l268_309(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l268_310(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l268_311(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l268_312(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l268_313(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l268_314(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l268_315(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l268_316(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l268_317(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l268_(x):
    # x is a list (or vector) of length 288
    return [
        l268_0(x),
        l268_1(x),
        l268_2(x),
        l268_3(x),
        l268_4(x),
        l268_5(x),
        l268_6(x),
        l268_7(x),
        l268_8(x),
        l268_9(x),
        l268_10(x),
        l268_11(x),
        l268_12(x),
        l268_13(x),
        l268_14(x),
        l268_15(x),
        l268_16(x),
        l268_17(x),
        l268_18(x),
        l268_19(x),
        l268_20(x),
        l268_21(x),
        l268_22(x),
        l268_23(x),
        l268_24(x),
        l268_25(x),
        l268_26(x),
        l268_27(x),
        l268_28(x),
        l268_29(x),
        l268_30(x),
        l268_31(x),
        l268_32(x),
        l268_33(x),
        l268_34(x),
        l268_35(x),
        l268_36(x),
        l268_37(x),
        l268_38(x),
        l268_39(x),
        l268_40(x),
        l268_41(x),
        l268_42(x),
        l268_43(x),
        l268_44(x),
        l268_45(x),
        l268_46(x),
        l268_47(x),
        l268_48(x),
        l268_49(x),
        l268_50(x),
        l268_51(x),
        l268_52(x),
        l268_53(x),
        l268_54(x),
        l268_55(x),
        l268_56(x),
        l268_57(x),
        l268_58(x),
        l268_59(x),
        l268_60(x),
        l268_61(x),
        l268_62(x),
        l268_63(x),
        l268_64(x),
        l268_65(x),
        l268_66(x),
        l268_67(x),
        l268_68(x),
        l268_69(x),
        l268_70(x),
        l268_71(x),
        l268_72(x),
        l268_73(x),
        l268_74(x),
        l268_75(x),
        l268_76(x),
        l268_77(x),
        l268_78(x),
        l268_79(x),
        l268_80(x),
        l268_81(x),
        l268_82(x),
        l268_83(x),
        l268_84(x),
        l268_85(x),
        l268_86(x),
        l268_87(x),
        l268_88(x),
        l268_89(x),
        l268_90(x),
        l268_91(x),
        l268_92(x),
        l268_93(x),
        l268_94(x),
        l268_95(x),
        l268_96(x),
        l268_97(x),
        l268_98(x),
        l268_99(x),
        l268_100(x),
        l268_101(x),
        l268_102(x),
        l268_103(x),
        l268_104(x),
        l268_105(x),
        l268_106(x),
        l268_107(x),
        l268_108(x),
        l268_109(x),
        l268_110(x),
        l268_111(x),
        l268_112(x),
        l268_113(x),
        l268_114(x),
        l268_115(x),
        l268_116(x),
        l268_117(x),
        l268_118(x),
        l268_119(x),
        l268_120(x),
        l268_121(x),
        l268_122(x),
        l268_123(x),
        l268_124(x),
        l268_125(x),
        l268_126(x),
        l268_127(x),
        l268_128(x),
        l268_129(x),
        l268_130(x),
        l268_131(x),
        l268_132(x),
        l268_133(x),
        l268_134(x),
        l268_135(x),
        l268_136(x),
        l268_137(x),
        l268_138(x),
        l268_139(x),
        l268_140(x),
        l268_141(x),
        l268_142(x),
        l268_143(x),
        l268_144(x),
        l268_145(x),
        l268_146(x),
        l268_147(x),
        l268_148(x),
        l268_149(x),
        l268_150(x),
        l268_151(x),
        l268_152(x),
        l268_153(x),
        l268_154(x),
        l268_155(x),
        l268_156(x),
        l268_157(x),
        l268_158(x),
        l268_159(x),
        l268_160(x),
        l268_161(x),
        l268_162(x),
        l268_163(x),
        l268_164(x),
        l268_165(x),
        l268_166(x),
        l268_167(x),
        l268_168(x),
        l268_169(x),
        l268_170(x),
        l268_171(x),
        l268_172(x),
        l268_173(x),
        l268_174(x),
        l268_175(x),
        l268_176(x),
        l268_177(x),
        l268_178(x),
        l268_179(x),
        l268_180(x),
        l268_181(x),
        l268_182(x),
        l268_183(x),
        l268_184(x),
        l268_185(x),
        l268_186(x),
        l268_187(x),
        l268_188(x),
        l268_189(x),
        l268_190(x),
        l268_191(x),
        l268_192(x),
        l268_193(x),
        l268_194(x),
        l268_195(x),
        l268_196(x),
        l268_197(x),
        l268_198(x),
        l268_199(x),
        l268_200(x),
        l268_201(x),
        l268_202(x),
        l268_203(x),
        l268_204(x),
        l268_205(x),
        l268_206(x),
        l268_207(x),
        l268_208(x),
        l268_209(x),
        l268_210(x),
        l268_211(x),
        l268_212(x),
        l268_213(x),
        l268_214(x),
        l268_215(x),
        l268_216(x),
        l268_217(x),
        l268_218(x),
        l268_219(x),
        l268_220(x),
        l268_221(x),
        l268_222(x),
        l268_223(x),
        l268_224(x),
        l268_225(x),
        l268_226(x),
        l268_227(x),
        l268_228(x),
        l268_229(x),
        l268_230(x),
        l268_231(x),
        l268_232(x),
        l268_233(x),
        l268_234(x),
        l268_235(x),
        l268_236(x),
        l268_237(x),
        l268_238(x),
        l268_239(x),
        l268_240(x),
        l268_241(x),
        l268_242(x),
        l268_243(x),
        l268_244(x),
        l268_245(x),
        l268_246(x),
        l268_247(x),
        l268_248(x),
        l268_249(x),
        l268_250(x),
        l268_251(x),
        l268_252(x),
        l268_253(x),
        l268_254(x),
        l268_255(x),
        l268_256(x),
        l268_257(x),
        l268_258(x),
        l268_259(x),
        l268_260(x),
        l268_261(x),
        l268_262(x),
        l268_263(x),
        l268_264(x),
        l268_265(x),
        l268_266(x),
        l268_267(x),
        l268_268(x),
        l268_269(x),
        l268_270(x),
        l268_271(x),
        l268_272(x),
        l268_273(x),
        l268_274(x),
        l268_275(x),
        l268_276(x),
        l268_277(x),
        l268_278(x),
        l268_279(x),
        l268_280(x),
        l268_281(x),
        l268_282(x),
        l268_283(x),
        l268_284(x),
        l268_285(x),
        l268_286(x),
        l268_287(x),
        l268_288(x),
        l268_289(x),
        l268_290(x),
        l268_291(x),
        l268_292(x),
        l268_293(x),
        l268_294(x),
        l268_295(x),
        l268_296(x),
        l268_297(x),
        l268_298(x),
        l268_299(x),
        l268_300(x),
        l268_301(x),
        l268_302(x),
        l268_303(x),
        l268_304(x),
        l268_305(x),
        l268_306(x),
        l268_307(x),
        l268_308(x),
        l268_309(x),
        l268_310(x),
        l268_311(x),
        l268_312(x),
        l268_313(x),
        l268_314(x),
        l268_315(x),
        l268_316(x),
        l268_317(x),
    ]