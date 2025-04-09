import numpy as np




# Generated from reverse engineering
def l520_g(x: np.ndarray) -> np.ndarray:
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




def l520_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l520_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l520_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l520_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l520_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l520_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l520_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l520_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l520_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l520_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l520_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l520_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l520_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l520_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l520_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l520_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l520_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l520_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l520_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l520_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l520_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l520_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l520_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l520_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l520_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l520_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l520_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l520_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l520_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l520_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l520_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l520_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l520_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l520_33(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[33] + 1.0)
def l520_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[32] + x[66] + -1.0)
def l520_35(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[33] + x[67])
def l520_36(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[34] + x[68])
def l520_37(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[35] + x[69])
def l520_38(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + x[70])
def l520_39(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + x[71])
def l520_40(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + x[72])
def l520_41(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + x[73])
def l520_42(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + x[74])
def l520_43(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + x[75])
def l520_44(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + x[76])
def l520_45(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + x[77])
def l520_46(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + x[78])
def l520_47(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + x[79])
def l520_48(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + x[80])
def l520_49(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + x[81])
def l520_50(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + x[82])
def l520_51(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + x[83])
def l520_52(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + x[84])
def l520_53(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + x[85])
def l520_54(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + x[86])
def l520_55(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + x[87])
def l520_56(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + x[88])
def l520_57(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + x[89])
def l520_58(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + x[90])
def l520_59(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + x[91])
def l520_60(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + x[92])
def l520_61(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + x[93])
def l520_62(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + x[94])
def l520_63(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + x[95])
def l520_64(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[34] + 1.0)
def l520_65(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[35] + 1.0)
def l520_66(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + 1.0)
def l520_67(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + 1.0)
def l520_68(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + 1.0)
def l520_69(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + 1.0)
def l520_70(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + 1.0)
def l520_71(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + 1.0)
def l520_72(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + 1.0)
def l520_73(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + 1.0)
def l520_74(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + 1.0)
def l520_75(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + 1.0)
def l520_76(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + 1.0)
def l520_77(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + 1.0)
def l520_78(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + 1.0)
def l520_79(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + 1.0)
def l520_80(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + 1.0)
def l520_81(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + 1.0)
def l520_82(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + 1.0)
def l520_83(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + 1.0)
def l520_84(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + 1.0)
def l520_85(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + 1.0)
def l520_86(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + 1.0)
def l520_87(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + 1.0)
def l520_88(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + 1.0)
def l520_89(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + 1.0)
def l520_90(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + 1.0)
def l520_91(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + 1.0)
def l520_92(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[62] + 1.0)
def l520_93(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[63] + 1.0)
def l520_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[64] + x[66] + -1.0)
def l520_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[65] + x[67] + -1.0)
def l520_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[66] + x[68] + -1.0)
def l520_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[67] + x[69] + -1.0)
def l520_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[68] + x[70] + -1.0)
def l520_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[69] + x[71] + -1.0)
def l520_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[70] + x[72] + -1.0)
def l520_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[71] + x[73] + -1.0)
def l520_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[72] + x[74] + -1.0)
def l520_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[73] + x[75] + -1.0)
def l520_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[74] + x[76] + -1.0)
def l520_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[75] + x[77] + -1.0)
def l520_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[76] + x[78] + -1.0)
def l520_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[77] + x[79] + -1.0)
def l520_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[78] + x[80] + -1.0)
def l520_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[79] + x[81] + -1.0)
def l520_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[80] + x[82] + -1.0)
def l520_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[81] + x[83] + -1.0)
def l520_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[82] + x[84] + -1.0)
def l520_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[83] + x[85] + -1.0)
def l520_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[84] + x[86] + -1.0)
def l520_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[85] + x[87] + -1.0)
def l520_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[86] + x[88] + -1.0)
def l520_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[87] + x[89] + -1.0)
def l520_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[88] + x[90] + -1.0)
def l520_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[89] + x[91] + -1.0)
def l520_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[90] + x[92] + -1.0)
def l520_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[91] + x[93] + -1.0)
def l520_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[92] + x[94] + -1.0)
def l520_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[93] + x[95] + -1.0)
def l520_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l520_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l520_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l520_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l520_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l520_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l520_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[100])
def l520_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[101])
def l520_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[102])
def l520_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[103])
def l520_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[104])
def l520_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[105])
def l520_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[106])
def l520_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[107])
def l520_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[108])
def l520_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[109])
def l520_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[110])
def l520_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[111])
def l520_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[112])
def l520_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[113])
def l520_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[114])
def l520_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[115])
def l520_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[116])
def l520_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[117])
def l520_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[118])
def l520_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[119])
def l520_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[120])
def l520_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[121])
def l520_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[122])
def l520_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[123])
def l520_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[124])
def l520_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[125])
def l520_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[126])
def l520_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[127])
def l520_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l520_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l520_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l520_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l520_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l520_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l520_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l520_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l520_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l520_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l520_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l520_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l520_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l520_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l520_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l520_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l520_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[144])
def l520_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[145])
def l520_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[146])
def l520_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[147])
def l520_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[148])
def l520_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[149])
def l520_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[150])
def l520_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[151])
def l520_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[152])
def l520_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[153])
def l520_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[154])
def l520_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[155])
def l520_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[156])
def l520_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[157])
def l520_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[158])
def l520_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[159])
def l520_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l520_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l520_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l520_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l520_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l520_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l520_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l520_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l520_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l520_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l520_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l520_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l520_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l520_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l520_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l520_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l520_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l520_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l520_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l520_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l520_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l520_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l520_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l520_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l520_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l520_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l520_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l520_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l520_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l520_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l520_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l520_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l520_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l520_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l520_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l520_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l520_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l520_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l520_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l520_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l520_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l520_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l520_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l520_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l520_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l520_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l520_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l520_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l520_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l520_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l520_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l520_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l520_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l520_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l520_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l520_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l520_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l520_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l520_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l520_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l520_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l520_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l520_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l520_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l520_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l520_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l520_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l520_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l520_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l520_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l520_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l520_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l520_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l520_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l520_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l520_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l520_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l520_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l520_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l520_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l520_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l520_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l520_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l520_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l520_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l520_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l520_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l520_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l520_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l520_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l520_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l520_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l520_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l520_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l520_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l520_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l520_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l520_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l520_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l520_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l520_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l520_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l520_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l520_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l520_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l520_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l520_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l520_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l520_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l520_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l520_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l520_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l520_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l520_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l520_304(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l520_305(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l520_306(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l520_307(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l520_308(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l520_309(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l520_310(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l520_311(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l520_312(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l520_313(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l520_314(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l520_315(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l520_316(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l520_317(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l520_(x):
    # x is a list (or vector) of length 288
    return [
        l520_0(x),
        l520_1(x),
        l520_2(x),
        l520_3(x),
        l520_4(x),
        l520_5(x),
        l520_6(x),
        l520_7(x),
        l520_8(x),
        l520_9(x),
        l520_10(x),
        l520_11(x),
        l520_12(x),
        l520_13(x),
        l520_14(x),
        l520_15(x),
        l520_16(x),
        l520_17(x),
        l520_18(x),
        l520_19(x),
        l520_20(x),
        l520_21(x),
        l520_22(x),
        l520_23(x),
        l520_24(x),
        l520_25(x),
        l520_26(x),
        l520_27(x),
        l520_28(x),
        l520_29(x),
        l520_30(x),
        l520_31(x),
        l520_32(x),
        l520_33(x),
        l520_34(x),
        l520_35(x),
        l520_36(x),
        l520_37(x),
        l520_38(x),
        l520_39(x),
        l520_40(x),
        l520_41(x),
        l520_42(x),
        l520_43(x),
        l520_44(x),
        l520_45(x),
        l520_46(x),
        l520_47(x),
        l520_48(x),
        l520_49(x),
        l520_50(x),
        l520_51(x),
        l520_52(x),
        l520_53(x),
        l520_54(x),
        l520_55(x),
        l520_56(x),
        l520_57(x),
        l520_58(x),
        l520_59(x),
        l520_60(x),
        l520_61(x),
        l520_62(x),
        l520_63(x),
        l520_64(x),
        l520_65(x),
        l520_66(x),
        l520_67(x),
        l520_68(x),
        l520_69(x),
        l520_70(x),
        l520_71(x),
        l520_72(x),
        l520_73(x),
        l520_74(x),
        l520_75(x),
        l520_76(x),
        l520_77(x),
        l520_78(x),
        l520_79(x),
        l520_80(x),
        l520_81(x),
        l520_82(x),
        l520_83(x),
        l520_84(x),
        l520_85(x),
        l520_86(x),
        l520_87(x),
        l520_88(x),
        l520_89(x),
        l520_90(x),
        l520_91(x),
        l520_92(x),
        l520_93(x),
        l520_94(x),
        l520_95(x),
        l520_96(x),
        l520_97(x),
        l520_98(x),
        l520_99(x),
        l520_100(x),
        l520_101(x),
        l520_102(x),
        l520_103(x),
        l520_104(x),
        l520_105(x),
        l520_106(x),
        l520_107(x),
        l520_108(x),
        l520_109(x),
        l520_110(x),
        l520_111(x),
        l520_112(x),
        l520_113(x),
        l520_114(x),
        l520_115(x),
        l520_116(x),
        l520_117(x),
        l520_118(x),
        l520_119(x),
        l520_120(x),
        l520_121(x),
        l520_122(x),
        l520_123(x),
        l520_124(x),
        l520_125(x),
        l520_126(x),
        l520_127(x),
        l520_128(x),
        l520_129(x),
        l520_130(x),
        l520_131(x),
        l520_132(x),
        l520_133(x),
        l520_134(x),
        l520_135(x),
        l520_136(x),
        l520_137(x),
        l520_138(x),
        l520_139(x),
        l520_140(x),
        l520_141(x),
        l520_142(x),
        l520_143(x),
        l520_144(x),
        l520_145(x),
        l520_146(x),
        l520_147(x),
        l520_148(x),
        l520_149(x),
        l520_150(x),
        l520_151(x),
        l520_152(x),
        l520_153(x),
        l520_154(x),
        l520_155(x),
        l520_156(x),
        l520_157(x),
        l520_158(x),
        l520_159(x),
        l520_160(x),
        l520_161(x),
        l520_162(x),
        l520_163(x),
        l520_164(x),
        l520_165(x),
        l520_166(x),
        l520_167(x),
        l520_168(x),
        l520_169(x),
        l520_170(x),
        l520_171(x),
        l520_172(x),
        l520_173(x),
        l520_174(x),
        l520_175(x),
        l520_176(x),
        l520_177(x),
        l520_178(x),
        l520_179(x),
        l520_180(x),
        l520_181(x),
        l520_182(x),
        l520_183(x),
        l520_184(x),
        l520_185(x),
        l520_186(x),
        l520_187(x),
        l520_188(x),
        l520_189(x),
        l520_190(x),
        l520_191(x),
        l520_192(x),
        l520_193(x),
        l520_194(x),
        l520_195(x),
        l520_196(x),
        l520_197(x),
        l520_198(x),
        l520_199(x),
        l520_200(x),
        l520_201(x),
        l520_202(x),
        l520_203(x),
        l520_204(x),
        l520_205(x),
        l520_206(x),
        l520_207(x),
        l520_208(x),
        l520_209(x),
        l520_210(x),
        l520_211(x),
        l520_212(x),
        l520_213(x),
        l520_214(x),
        l520_215(x),
        l520_216(x),
        l520_217(x),
        l520_218(x),
        l520_219(x),
        l520_220(x),
        l520_221(x),
        l520_222(x),
        l520_223(x),
        l520_224(x),
        l520_225(x),
        l520_226(x),
        l520_227(x),
        l520_228(x),
        l520_229(x),
        l520_230(x),
        l520_231(x),
        l520_232(x),
        l520_233(x),
        l520_234(x),
        l520_235(x),
        l520_236(x),
        l520_237(x),
        l520_238(x),
        l520_239(x),
        l520_240(x),
        l520_241(x),
        l520_242(x),
        l520_243(x),
        l520_244(x),
        l520_245(x),
        l520_246(x),
        l520_247(x),
        l520_248(x),
        l520_249(x),
        l520_250(x),
        l520_251(x),
        l520_252(x),
        l520_253(x),
        l520_254(x),
        l520_255(x),
        l520_256(x),
        l520_257(x),
        l520_258(x),
        l520_259(x),
        l520_260(x),
        l520_261(x),
        l520_262(x),
        l520_263(x),
        l520_264(x),
        l520_265(x),
        l520_266(x),
        l520_267(x),
        l520_268(x),
        l520_269(x),
        l520_270(x),
        l520_271(x),
        l520_272(x),
        l520_273(x),
        l520_274(x),
        l520_275(x),
        l520_276(x),
        l520_277(x),
        l520_278(x),
        l520_279(x),
        l520_280(x),
        l520_281(x),
        l520_282(x),
        l520_283(x),
        l520_284(x),
        l520_285(x),
        l520_286(x),
        l520_287(x),
        l520_288(x),
        l520_289(x),
        l520_290(x),
        l520_291(x),
        l520_292(x),
        l520_293(x),
        l520_294(x),
        l520_295(x),
        l520_296(x),
        l520_297(x),
        l520_298(x),
        l520_299(x),
        l520_300(x),
        l520_301(x),
        l520_302(x),
        l520_303(x),
        l520_304(x),
        l520_305(x),
        l520_306(x),
        l520_307(x),
        l520_308(x),
        l520_309(x),
        l520_310(x),
        l520_311(x),
        l520_312(x),
        l520_313(x),
        l520_314(x),
        l520_315(x),
        l520_316(x),
        l520_317(x),
    ]