import numpy as np




# Generated from reverse engineering
def l184_g(x: np.ndarray) -> np.ndarray:
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




def l184_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l184_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l184_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l184_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l184_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l184_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l184_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l184_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l184_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l184_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l184_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l184_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l184_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l184_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l184_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l184_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l184_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l184_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l184_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l184_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l184_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l184_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l184_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l184_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l184_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l184_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l184_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l184_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l184_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l184_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l184_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l184_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l184_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l184_33(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[33] + 1.0)
def l184_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[32] + x[66] + -1.0)
def l184_35(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[33] + x[67])
def l184_36(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[34] + x[68])
def l184_37(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[35] + x[69])
def l184_38(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + x[70])
def l184_39(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + x[71])
def l184_40(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + x[72])
def l184_41(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + x[73])
def l184_42(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + x[74])
def l184_43(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + x[75])
def l184_44(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + x[76])
def l184_45(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + x[77])
def l184_46(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + x[78])
def l184_47(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + x[79])
def l184_48(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + x[80])
def l184_49(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + x[81])
def l184_50(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + x[82])
def l184_51(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + x[83])
def l184_52(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + x[84])
def l184_53(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + x[85])
def l184_54(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + x[86])
def l184_55(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + x[87])
def l184_56(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + x[88])
def l184_57(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + x[89])
def l184_58(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + x[90])
def l184_59(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + x[91])
def l184_60(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + x[92])
def l184_61(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + x[93])
def l184_62(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + x[94])
def l184_63(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + x[95])
def l184_64(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[34] + 1.0)
def l184_65(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[35] + 1.0)
def l184_66(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[36] + 1.0)
def l184_67(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[37] + 1.0)
def l184_68(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[38] + 1.0)
def l184_69(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[39] + 1.0)
def l184_70(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + 1.0)
def l184_71(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + 1.0)
def l184_72(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + 1.0)
def l184_73(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + 1.0)
def l184_74(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + 1.0)
def l184_75(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + 1.0)
def l184_76(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + 1.0)
def l184_77(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + 1.0)
def l184_78(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + 1.0)
def l184_79(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + 1.0)
def l184_80(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + 1.0)
def l184_81(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + 1.0)
def l184_82(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + 1.0)
def l184_83(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + 1.0)
def l184_84(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + 1.0)
def l184_85(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + 1.0)
def l184_86(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + 1.0)
def l184_87(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + 1.0)
def l184_88(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + 1.0)
def l184_89(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + 1.0)
def l184_90(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + 1.0)
def l184_91(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + 1.0)
def l184_92(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[62] + 1.0)
def l184_93(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[63] + 1.0)
def l184_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[64] + x[66] + -1.0)
def l184_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[65] + x[67] + -1.0)
def l184_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[66] + x[68] + -1.0)
def l184_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[67] + x[69] + -1.0)
def l184_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[68] + x[70] + -1.0)
def l184_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[69] + x[71] + -1.0)
def l184_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[70] + x[72] + -1.0)
def l184_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[71] + x[73] + -1.0)
def l184_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[72] + x[74] + -1.0)
def l184_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[73] + x[75] + -1.0)
def l184_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[74] + x[76] + -1.0)
def l184_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[75] + x[77] + -1.0)
def l184_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[76] + x[78] + -1.0)
def l184_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[77] + x[79] + -1.0)
def l184_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[78] + x[80] + -1.0)
def l184_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[79] + x[81] + -1.0)
def l184_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[80] + x[82] + -1.0)
def l184_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[81] + x[83] + -1.0)
def l184_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[82] + x[84] + -1.0)
def l184_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[83] + x[85] + -1.0)
def l184_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[84] + x[86] + -1.0)
def l184_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[85] + x[87] + -1.0)
def l184_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[86] + x[88] + -1.0)
def l184_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[87] + x[89] + -1.0)
def l184_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[88] + x[90] + -1.0)
def l184_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[89] + x[91] + -1.0)
def l184_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[90] + x[92] + -1.0)
def l184_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[91] + x[93] + -1.0)
def l184_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[92] + x[94] + -1.0)
def l184_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[93] + x[95] + -1.0)
def l184_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l184_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l184_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l184_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l184_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l184_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l184_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[100])
def l184_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[101])
def l184_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[102])
def l184_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[103])
def l184_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[104])
def l184_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[105])
def l184_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[106])
def l184_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[107])
def l184_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[108])
def l184_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[109])
def l184_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[110])
def l184_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[111])
def l184_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[112])
def l184_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[113])
def l184_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[114])
def l184_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[115])
def l184_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[116])
def l184_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[117])
def l184_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[118])
def l184_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[119])
def l184_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[120])
def l184_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[121])
def l184_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[122])
def l184_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[123])
def l184_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[124])
def l184_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[125])
def l184_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[126])
def l184_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[127])
def l184_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l184_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l184_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l184_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l184_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l184_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l184_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l184_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l184_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l184_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l184_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l184_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l184_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l184_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l184_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l184_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l184_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[144])
def l184_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[145])
def l184_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[146])
def l184_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[147])
def l184_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[148])
def l184_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[149])
def l184_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[150])
def l184_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[151])
def l184_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[152])
def l184_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[153])
def l184_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[154])
def l184_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[155])
def l184_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[156])
def l184_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[157])
def l184_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[158])
def l184_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[159])
def l184_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l184_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l184_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l184_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l184_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l184_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l184_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l184_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l184_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l184_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l184_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l184_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l184_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l184_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l184_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l184_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l184_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l184_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l184_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l184_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l184_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l184_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l184_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l184_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l184_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l184_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l184_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l184_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l184_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l184_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l184_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l184_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l184_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l184_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l184_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l184_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l184_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l184_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l184_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l184_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l184_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l184_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l184_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l184_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l184_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l184_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l184_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l184_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l184_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l184_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l184_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l184_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l184_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l184_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l184_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l184_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l184_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l184_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l184_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l184_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l184_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l184_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l184_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l184_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l184_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l184_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l184_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l184_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l184_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l184_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l184_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l184_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l184_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l184_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l184_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l184_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l184_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l184_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l184_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l184_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l184_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l184_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l184_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l184_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l184_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l184_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l184_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l184_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l184_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l184_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l184_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l184_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l184_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l184_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l184_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l184_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l184_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l184_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l184_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l184_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l184_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l184_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l184_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l184_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l184_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l184_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l184_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l184_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l184_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l184_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l184_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l184_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l184_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l184_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l184_304(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l184_305(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l184_306(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l184_307(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l184_308(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l184_309(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l184_310(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l184_311(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l184_312(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l184_313(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l184_314(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l184_315(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l184_316(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l184_317(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l184_(x):
    # x is a list (or vector) of length 288
    return [
        l184_0(x),
        l184_1(x),
        l184_2(x),
        l184_3(x),
        l184_4(x),
        l184_5(x),
        l184_6(x),
        l184_7(x),
        l184_8(x),
        l184_9(x),
        l184_10(x),
        l184_11(x),
        l184_12(x),
        l184_13(x),
        l184_14(x),
        l184_15(x),
        l184_16(x),
        l184_17(x),
        l184_18(x),
        l184_19(x),
        l184_20(x),
        l184_21(x),
        l184_22(x),
        l184_23(x),
        l184_24(x),
        l184_25(x),
        l184_26(x),
        l184_27(x),
        l184_28(x),
        l184_29(x),
        l184_30(x),
        l184_31(x),
        l184_32(x),
        l184_33(x),
        l184_34(x),
        l184_35(x),
        l184_36(x),
        l184_37(x),
        l184_38(x),
        l184_39(x),
        l184_40(x),
        l184_41(x),
        l184_42(x),
        l184_43(x),
        l184_44(x),
        l184_45(x),
        l184_46(x),
        l184_47(x),
        l184_48(x),
        l184_49(x),
        l184_50(x),
        l184_51(x),
        l184_52(x),
        l184_53(x),
        l184_54(x),
        l184_55(x),
        l184_56(x),
        l184_57(x),
        l184_58(x),
        l184_59(x),
        l184_60(x),
        l184_61(x),
        l184_62(x),
        l184_63(x),
        l184_64(x),
        l184_65(x),
        l184_66(x),
        l184_67(x),
        l184_68(x),
        l184_69(x),
        l184_70(x),
        l184_71(x),
        l184_72(x),
        l184_73(x),
        l184_74(x),
        l184_75(x),
        l184_76(x),
        l184_77(x),
        l184_78(x),
        l184_79(x),
        l184_80(x),
        l184_81(x),
        l184_82(x),
        l184_83(x),
        l184_84(x),
        l184_85(x),
        l184_86(x),
        l184_87(x),
        l184_88(x),
        l184_89(x),
        l184_90(x),
        l184_91(x),
        l184_92(x),
        l184_93(x),
        l184_94(x),
        l184_95(x),
        l184_96(x),
        l184_97(x),
        l184_98(x),
        l184_99(x),
        l184_100(x),
        l184_101(x),
        l184_102(x),
        l184_103(x),
        l184_104(x),
        l184_105(x),
        l184_106(x),
        l184_107(x),
        l184_108(x),
        l184_109(x),
        l184_110(x),
        l184_111(x),
        l184_112(x),
        l184_113(x),
        l184_114(x),
        l184_115(x),
        l184_116(x),
        l184_117(x),
        l184_118(x),
        l184_119(x),
        l184_120(x),
        l184_121(x),
        l184_122(x),
        l184_123(x),
        l184_124(x),
        l184_125(x),
        l184_126(x),
        l184_127(x),
        l184_128(x),
        l184_129(x),
        l184_130(x),
        l184_131(x),
        l184_132(x),
        l184_133(x),
        l184_134(x),
        l184_135(x),
        l184_136(x),
        l184_137(x),
        l184_138(x),
        l184_139(x),
        l184_140(x),
        l184_141(x),
        l184_142(x),
        l184_143(x),
        l184_144(x),
        l184_145(x),
        l184_146(x),
        l184_147(x),
        l184_148(x),
        l184_149(x),
        l184_150(x),
        l184_151(x),
        l184_152(x),
        l184_153(x),
        l184_154(x),
        l184_155(x),
        l184_156(x),
        l184_157(x),
        l184_158(x),
        l184_159(x),
        l184_160(x),
        l184_161(x),
        l184_162(x),
        l184_163(x),
        l184_164(x),
        l184_165(x),
        l184_166(x),
        l184_167(x),
        l184_168(x),
        l184_169(x),
        l184_170(x),
        l184_171(x),
        l184_172(x),
        l184_173(x),
        l184_174(x),
        l184_175(x),
        l184_176(x),
        l184_177(x),
        l184_178(x),
        l184_179(x),
        l184_180(x),
        l184_181(x),
        l184_182(x),
        l184_183(x),
        l184_184(x),
        l184_185(x),
        l184_186(x),
        l184_187(x),
        l184_188(x),
        l184_189(x),
        l184_190(x),
        l184_191(x),
        l184_192(x),
        l184_193(x),
        l184_194(x),
        l184_195(x),
        l184_196(x),
        l184_197(x),
        l184_198(x),
        l184_199(x),
        l184_200(x),
        l184_201(x),
        l184_202(x),
        l184_203(x),
        l184_204(x),
        l184_205(x),
        l184_206(x),
        l184_207(x),
        l184_208(x),
        l184_209(x),
        l184_210(x),
        l184_211(x),
        l184_212(x),
        l184_213(x),
        l184_214(x),
        l184_215(x),
        l184_216(x),
        l184_217(x),
        l184_218(x),
        l184_219(x),
        l184_220(x),
        l184_221(x),
        l184_222(x),
        l184_223(x),
        l184_224(x),
        l184_225(x),
        l184_226(x),
        l184_227(x),
        l184_228(x),
        l184_229(x),
        l184_230(x),
        l184_231(x),
        l184_232(x),
        l184_233(x),
        l184_234(x),
        l184_235(x),
        l184_236(x),
        l184_237(x),
        l184_238(x),
        l184_239(x),
        l184_240(x),
        l184_241(x),
        l184_242(x),
        l184_243(x),
        l184_244(x),
        l184_245(x),
        l184_246(x),
        l184_247(x),
        l184_248(x),
        l184_249(x),
        l184_250(x),
        l184_251(x),
        l184_252(x),
        l184_253(x),
        l184_254(x),
        l184_255(x),
        l184_256(x),
        l184_257(x),
        l184_258(x),
        l184_259(x),
        l184_260(x),
        l184_261(x),
        l184_262(x),
        l184_263(x),
        l184_264(x),
        l184_265(x),
        l184_266(x),
        l184_267(x),
        l184_268(x),
        l184_269(x),
        l184_270(x),
        l184_271(x),
        l184_272(x),
        l184_273(x),
        l184_274(x),
        l184_275(x),
        l184_276(x),
        l184_277(x),
        l184_278(x),
        l184_279(x),
        l184_280(x),
        l184_281(x),
        l184_282(x),
        l184_283(x),
        l184_284(x),
        l184_285(x),
        l184_286(x),
        l184_287(x),
        l184_288(x),
        l184_289(x),
        l184_290(x),
        l184_291(x),
        l184_292(x),
        l184_293(x),
        l184_294(x),
        l184_295(x),
        l184_296(x),
        l184_297(x),
        l184_298(x),
        l184_299(x),
        l184_300(x),
        l184_301(x),
        l184_302(x),
        l184_303(x),
        l184_304(x),
        l184_305(x),
        l184_306(x),
        l184_307(x),
        l184_308(x),
        l184_309(x),
        l184_310(x),
        l184_311(x),
        l184_312(x),
        l184_313(x),
        l184_314(x),
        l184_315(x),
        l184_316(x),
        l184_317(x),
    ]