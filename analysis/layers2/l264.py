import numpy as np




# Generated from reverse engineering
def l264_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 319
    out = np.empty(319, dtype=np.float32)
    
    # for i in range(0, 33):
    for i in range(0, 33):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(33, 64):
    for i in range(0, 31):
        s = x[32 + i] + x[65 + i]
        s += biases[i]
        out[33 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 95):
    for i in range(0, 31):
        s = x[33 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(95, 126):
    for i in range(0, 31):
        s = x[64 + i] + x[65 + i]
        s += biases[i]
        out[95 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(126, 127):
    for i in range(0, 1):
        s = x[64 + i]
        out[126 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(127, 319):
    for i in range(0, 192):
        s = x[64 + i]
        out[127 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l264_0(x):
    # x is a list (or vector) of length 256
    return max(0, x[0])
def l264_1(x):
    # x is a list (or vector) of length 256
    return max(0, x[1])
def l264_2(x):
    # x is a list (or vector) of length 256
    return max(0, x[2])
def l264_3(x):
    # x is a list (or vector) of length 256
    return max(0, x[3])
def l264_4(x):
    # x is a list (or vector) of length 256
    return max(0, x[4])
def l264_5(x):
    # x is a list (or vector) of length 256
    return max(0, x[5])
def l264_6(x):
    # x is a list (or vector) of length 256
    return max(0, x[6])
def l264_7(x):
    # x is a list (or vector) of length 256
    return max(0, x[7])
def l264_8(x):
    # x is a list (or vector) of length 256
    return max(0, x[8])
def l264_9(x):
    # x is a list (or vector) of length 256
    return max(0, x[9])
def l264_10(x):
    # x is a list (or vector) of length 256
    return max(0, x[10])
def l264_11(x):
    # x is a list (or vector) of length 256
    return max(0, x[11])
def l264_12(x):
    # x is a list (or vector) of length 256
    return max(0, x[12])
def l264_13(x):
    # x is a list (or vector) of length 256
    return max(0, x[13])
def l264_14(x):
    # x is a list (or vector) of length 256
    return max(0, x[14])
def l264_15(x):
    # x is a list (or vector) of length 256
    return max(0, x[15])
def l264_16(x):
    # x is a list (or vector) of length 256
    return max(0, x[16])
def l264_17(x):
    # x is a list (or vector) of length 256
    return max(0, x[17])
def l264_18(x):
    # x is a list (or vector) of length 256
    return max(0, x[18])
def l264_19(x):
    # x is a list (or vector) of length 256
    return max(0, x[19])
def l264_20(x):
    # x is a list (or vector) of length 256
    return max(0, x[20])
def l264_21(x):
    # x is a list (or vector) of length 256
    return max(0, x[21])
def l264_22(x):
    # x is a list (or vector) of length 256
    return max(0, x[22])
def l264_23(x):
    # x is a list (or vector) of length 256
    return max(0, x[23])
def l264_24(x):
    # x is a list (or vector) of length 256
    return max(0, x[24])
def l264_25(x):
    # x is a list (or vector) of length 256
    return max(0, x[25])
def l264_26(x):
    # x is a list (or vector) of length 256
    return max(0, x[26])
def l264_27(x):
    # x is a list (or vector) of length 256
    return max(0, x[27])
def l264_28(x):
    # x is a list (or vector) of length 256
    return max(0, x[28])
def l264_29(x):
    # x is a list (or vector) of length 256
    return max(0, x[29])
def l264_30(x):
    # x is a list (or vector) of length 256
    return max(0, x[30])
def l264_31(x):
    # x is a list (or vector) of length 256
    return max(0, x[31])
def l264_32(x):
    # x is a list (or vector) of length 256
    return max(0, x[32])
def l264_33(x):
    # x is a list (or vector) of length 256
    return max(0, x[32] + x[65] + -1.0)
def l264_34(x):
    # x is a list (or vector) of length 256
    return max(0, x[33] + x[66] + -1.0)
def l264_35(x):
    # x is a list (or vector) of length 256
    return max(0, x[34] + x[67] + -1.0)
def l264_36(x):
    # x is a list (or vector) of length 256
    return max(0, x[35] + x[68] + -1.0)
def l264_37(x):
    # x is a list (or vector) of length 256
    return max(0, x[36] + x[69] + -1.0)
def l264_38(x):
    # x is a list (or vector) of length 256
    return max(0, x[37] + x[70] + -1.0)
def l264_39(x):
    # x is a list (or vector) of length 256
    return max(0, x[38] + x[71] + -1.0)
def l264_40(x):
    # x is a list (or vector) of length 256
    return max(0, x[39] + x[72] + -1.0)
def l264_41(x):
    # x is a list (or vector) of length 256
    return max(0, x[40] + x[73] + -1.0)
def l264_42(x):
    # x is a list (or vector) of length 256
    return max(0, x[41] + x[74] + -1.0)
def l264_43(x):
    # x is a list (or vector) of length 256
    return max(0, x[42] + x[75] + -1.0)
def l264_44(x):
    # x is a list (or vector) of length 256
    return max(0, x[43] + x[76] + -1.0)
def l264_45(x):
    # x is a list (or vector) of length 256
    return max(0, x[44] + x[77] + -1.0)
def l264_46(x):
    # x is a list (or vector) of length 256
    return max(0, x[45] + x[78] + -1.0)
def l264_47(x):
    # x is a list (or vector) of length 256
    return max(0, x[46] + x[79] + -1.0)
def l264_48(x):
    # x is a list (or vector) of length 256
    return max(0, x[47] + x[80] + -1.0)
def l264_49(x):
    # x is a list (or vector) of length 256
    return max(0, x[48] + x[81] + -1.0)
def l264_50(x):
    # x is a list (or vector) of length 256
    return max(0, x[49] + x[82] + -1.0)
def l264_51(x):
    # x is a list (or vector) of length 256
    return max(0, x[50] + x[83] + -1.0)
def l264_52(x):
    # x is a list (or vector) of length 256
    return max(0, x[51] + x[84] + -1.0)
def l264_53(x):
    # x is a list (or vector) of length 256
    return max(0, x[52] + x[85] + -1.0)
def l264_54(x):
    # x is a list (or vector) of length 256
    return max(0, x[53] + x[86] + -1.0)
def l264_55(x):
    # x is a list (or vector) of length 256
    return max(0, x[54] + x[87] + -1.0)
def l264_56(x):
    # x is a list (or vector) of length 256
    return max(0, x[55] + x[88] + -1.0)
def l264_57(x):
    # x is a list (or vector) of length 256
    return max(0, x[56] + x[89] + -1.0)
def l264_58(x):
    # x is a list (or vector) of length 256
    return max(0, x[57] + x[90] + -1.0)
def l264_59(x):
    # x is a list (or vector) of length 256
    return max(0, x[58] + x[91] + -1.0)
def l264_60(x):
    # x is a list (or vector) of length 256
    return max(0, x[59] + x[92] + -1.0)
def l264_61(x):
    # x is a list (or vector) of length 256
    return max(0, x[60] + x[93] + -1.0)
def l264_62(x):
    # x is a list (or vector) of length 256
    return max(0, x[61] + x[94] + -1.0)
def l264_63(x):
    # x is a list (or vector) of length 256
    return max(0, x[62] + x[95] + -1.0)
def l264_64(x):
    # x is a list (or vector) of length 256
    return max(0, x[33])
def l264_65(x):
    # x is a list (or vector) of length 256
    return max(0, x[34])
def l264_66(x):
    # x is a list (or vector) of length 256
    return max(0, x[35])
def l264_67(x):
    # x is a list (or vector) of length 256
    return max(0, x[36])
def l264_68(x):
    # x is a list (or vector) of length 256
    return max(0, x[37])
def l264_69(x):
    # x is a list (or vector) of length 256
    return max(0, x[38])
def l264_70(x):
    # x is a list (or vector) of length 256
    return max(0, x[39])
def l264_71(x):
    # x is a list (or vector) of length 256
    return max(0, x[40])
def l264_72(x):
    # x is a list (or vector) of length 256
    return max(0, x[41])
def l264_73(x):
    # x is a list (or vector) of length 256
    return max(0, x[42])
def l264_74(x):
    # x is a list (or vector) of length 256
    return max(0, x[43])
def l264_75(x):
    # x is a list (or vector) of length 256
    return max(0, x[44])
def l264_76(x):
    # x is a list (or vector) of length 256
    return max(0, x[45])
def l264_77(x):
    # x is a list (or vector) of length 256
    return max(0, x[46])
def l264_78(x):
    # x is a list (or vector) of length 256
    return max(0, x[47])
def l264_79(x):
    # x is a list (or vector) of length 256
    return max(0, x[48])
def l264_80(x):
    # x is a list (or vector) of length 256
    return max(0, x[49])
def l264_81(x):
    # x is a list (or vector) of length 256
    return max(0, x[50])
def l264_82(x):
    # x is a list (or vector) of length 256
    return max(0, x[51])
def l264_83(x):
    # x is a list (or vector) of length 256
    return max(0, x[52])
def l264_84(x):
    # x is a list (or vector) of length 256
    return max(0, x[53])
def l264_85(x):
    # x is a list (or vector) of length 256
    return max(0, x[54])
def l264_86(x):
    # x is a list (or vector) of length 256
    return max(0, x[55])
def l264_87(x):
    # x is a list (or vector) of length 256
    return max(0, x[56])
def l264_88(x):
    # x is a list (or vector) of length 256
    return max(0, x[57])
def l264_89(x):
    # x is a list (or vector) of length 256
    return max(0, x[58])
def l264_90(x):
    # x is a list (or vector) of length 256
    return max(0, x[59])
def l264_91(x):
    # x is a list (or vector) of length 256
    return max(0, x[60])
def l264_92(x):
    # x is a list (or vector) of length 256
    return max(0, x[61])
def l264_93(x):
    # x is a list (or vector) of length 256
    return max(0, x[62])
def l264_94(x):
    # x is a list (or vector) of length 256
    return max(0, x[63])
def l264_95(x):
    # x is a list (or vector) of length 256
    return max(0, x[64] + x[65] + -1.0)
def l264_96(x):
    # x is a list (or vector) of length 256
    return max(0, x[65] + x[66] + -1.0)
def l264_97(x):
    # x is a list (or vector) of length 256
    return max(0, x[66] + x[67] + -1.0)
def l264_98(x):
    # x is a list (or vector) of length 256
    return max(0, x[67] + x[68] + -1.0)
def l264_99(x):
    # x is a list (or vector) of length 256
    return max(0, x[68] + x[69] + -1.0)
def l264_100(x):
    # x is a list (or vector) of length 256
    return max(0, x[69] + x[70] + -1.0)
def l264_101(x):
    # x is a list (or vector) of length 256
    return max(0, x[70] + x[71] + -1.0)
def l264_102(x):
    # x is a list (or vector) of length 256
    return max(0, x[71] + x[72] + -1.0)
def l264_103(x):
    # x is a list (or vector) of length 256
    return max(0, x[72] + x[73] + -1.0)
def l264_104(x):
    # x is a list (or vector) of length 256
    return max(0, x[73] + x[74] + -1.0)
def l264_105(x):
    # x is a list (or vector) of length 256
    return max(0, x[74] + x[75] + -1.0)
def l264_106(x):
    # x is a list (or vector) of length 256
    return max(0, x[75] + x[76] + -1.0)
def l264_107(x):
    # x is a list (or vector) of length 256
    return max(0, x[76] + x[77] + -1.0)
def l264_108(x):
    # x is a list (or vector) of length 256
    return max(0, x[77] + x[78] + -1.0)
def l264_109(x):
    # x is a list (or vector) of length 256
    return max(0, x[78] + x[79] + -1.0)
def l264_110(x):
    # x is a list (or vector) of length 256
    return max(0, x[79] + x[80] + -1.0)
def l264_111(x):
    # x is a list (or vector) of length 256
    return max(0, x[80] + x[81] + -1.0)
def l264_112(x):
    # x is a list (or vector) of length 256
    return max(0, x[81] + x[82] + -1.0)
def l264_113(x):
    # x is a list (or vector) of length 256
    return max(0, x[82] + x[83] + -1.0)
def l264_114(x):
    # x is a list (or vector) of length 256
    return max(0, x[83] + x[84] + -1.0)
def l264_115(x):
    # x is a list (or vector) of length 256
    return max(0, x[84] + x[85] + -1.0)
def l264_116(x):
    # x is a list (or vector) of length 256
    return max(0, x[85] + x[86] + -1.0)
def l264_117(x):
    # x is a list (or vector) of length 256
    return max(0, x[86] + x[87] + -1.0)
def l264_118(x):
    # x is a list (or vector) of length 256
    return max(0, x[87] + x[88] + -1.0)
def l264_119(x):
    # x is a list (or vector) of length 256
    return max(0, x[88] + x[89] + -1.0)
def l264_120(x):
    # x is a list (or vector) of length 256
    return max(0, x[89] + x[90] + -1.0)
def l264_121(x):
    # x is a list (or vector) of length 256
    return max(0, x[90] + x[91] + -1.0)
def l264_122(x):
    # x is a list (or vector) of length 256
    return max(0, x[91] + x[92] + -1.0)
def l264_123(x):
    # x is a list (or vector) of length 256
    return max(0, x[92] + x[93] + -1.0)
def l264_124(x):
    # x is a list (or vector) of length 256
    return max(0, x[93] + x[94] + -1.0)
def l264_125(x):
    # x is a list (or vector) of length 256
    return max(0, x[94] + x[95] + -1.0)
def l264_126(x):
    # x is a list (or vector) of length 256
    return max(0, x[64])
def l264_127(x):
    # x is a list (or vector) of length 256
    return max(0, x[64])
def l264_128(x):
    # x is a list (or vector) of length 256
    return max(0, x[65])
def l264_129(x):
    # x is a list (or vector) of length 256
    return max(0, x[66])
def l264_130(x):
    # x is a list (or vector) of length 256
    return max(0, x[67])
def l264_131(x):
    # x is a list (or vector) of length 256
    return max(0, x[68])
def l264_132(x):
    # x is a list (or vector) of length 256
    return max(0, x[69])
def l264_133(x):
    # x is a list (or vector) of length 256
    return max(0, x[70])
def l264_134(x):
    # x is a list (or vector) of length 256
    return max(0, x[71])
def l264_135(x):
    # x is a list (or vector) of length 256
    return max(0, x[72])
def l264_136(x):
    # x is a list (or vector) of length 256
    return max(0, x[73])
def l264_137(x):
    # x is a list (or vector) of length 256
    return max(0, x[74])
def l264_138(x):
    # x is a list (or vector) of length 256
    return max(0, x[75])
def l264_139(x):
    # x is a list (or vector) of length 256
    return max(0, x[76])
def l264_140(x):
    # x is a list (or vector) of length 256
    return max(0, x[77])
def l264_141(x):
    # x is a list (or vector) of length 256
    return max(0, x[78])
def l264_142(x):
    # x is a list (or vector) of length 256
    return max(0, x[79])
def l264_143(x):
    # x is a list (or vector) of length 256
    return max(0, x[80])
def l264_144(x):
    # x is a list (or vector) of length 256
    return max(0, x[81])
def l264_145(x):
    # x is a list (or vector) of length 256
    return max(0, x[82])
def l264_146(x):
    # x is a list (or vector) of length 256
    return max(0, x[83])
def l264_147(x):
    # x is a list (or vector) of length 256
    return max(0, x[84])
def l264_148(x):
    # x is a list (or vector) of length 256
    return max(0, x[85])
def l264_149(x):
    # x is a list (or vector) of length 256
    return max(0, x[86])
def l264_150(x):
    # x is a list (or vector) of length 256
    return max(0, x[87])
def l264_151(x):
    # x is a list (or vector) of length 256
    return max(0, x[88])
def l264_152(x):
    # x is a list (or vector) of length 256
    return max(0, x[89])
def l264_153(x):
    # x is a list (or vector) of length 256
    return max(0, x[90])
def l264_154(x):
    # x is a list (or vector) of length 256
    return max(0, x[91])
def l264_155(x):
    # x is a list (or vector) of length 256
    return max(0, x[92])
def l264_156(x):
    # x is a list (or vector) of length 256
    return max(0, x[93])
def l264_157(x):
    # x is a list (or vector) of length 256
    return max(0, x[94])
def l264_158(x):
    # x is a list (or vector) of length 256
    return max(0, x[95])
def l264_159(x):
    # x is a list (or vector) of length 256
    return max(0, x[96])
def l264_160(x):
    # x is a list (or vector) of length 256
    return max(0, x[97])
def l264_161(x):
    # x is a list (or vector) of length 256
    return max(0, x[98])
def l264_162(x):
    # x is a list (or vector) of length 256
    return max(0, x[99])
def l264_163(x):
    # x is a list (or vector) of length 256
    return max(0, x[100])
def l264_164(x):
    # x is a list (or vector) of length 256
    return max(0, x[101])
def l264_165(x):
    # x is a list (or vector) of length 256
    return max(0, x[102])
def l264_166(x):
    # x is a list (or vector) of length 256
    return max(0, x[103])
def l264_167(x):
    # x is a list (or vector) of length 256
    return max(0, x[104])
def l264_168(x):
    # x is a list (or vector) of length 256
    return max(0, x[105])
def l264_169(x):
    # x is a list (or vector) of length 256
    return max(0, x[106])
def l264_170(x):
    # x is a list (or vector) of length 256
    return max(0, x[107])
def l264_171(x):
    # x is a list (or vector) of length 256
    return max(0, x[108])
def l264_172(x):
    # x is a list (or vector) of length 256
    return max(0, x[109])
def l264_173(x):
    # x is a list (or vector) of length 256
    return max(0, x[110])
def l264_174(x):
    # x is a list (or vector) of length 256
    return max(0, x[111])
def l264_175(x):
    # x is a list (or vector) of length 256
    return max(0, x[112])
def l264_176(x):
    # x is a list (or vector) of length 256
    return max(0, x[113])
def l264_177(x):
    # x is a list (or vector) of length 256
    return max(0, x[114])
def l264_178(x):
    # x is a list (or vector) of length 256
    return max(0, x[115])
def l264_179(x):
    # x is a list (or vector) of length 256
    return max(0, x[116])
def l264_180(x):
    # x is a list (or vector) of length 256
    return max(0, x[117])
def l264_181(x):
    # x is a list (or vector) of length 256
    return max(0, x[118])
def l264_182(x):
    # x is a list (or vector) of length 256
    return max(0, x[119])
def l264_183(x):
    # x is a list (or vector) of length 256
    return max(0, x[120])
def l264_184(x):
    # x is a list (or vector) of length 256
    return max(0, x[121])
def l264_185(x):
    # x is a list (or vector) of length 256
    return max(0, x[122])
def l264_186(x):
    # x is a list (or vector) of length 256
    return max(0, x[123])
def l264_187(x):
    # x is a list (or vector) of length 256
    return max(0, x[124])
def l264_188(x):
    # x is a list (or vector) of length 256
    return max(0, x[125])
def l264_189(x):
    # x is a list (or vector) of length 256
    return max(0, x[126])
def l264_190(x):
    # x is a list (or vector) of length 256
    return max(0, x[127])
def l264_191(x):
    # x is a list (or vector) of length 256
    return max(0, x[128])
def l264_192(x):
    # x is a list (or vector) of length 256
    return max(0, x[129])
def l264_193(x):
    # x is a list (or vector) of length 256
    return max(0, x[130])
def l264_194(x):
    # x is a list (or vector) of length 256
    return max(0, x[131])
def l264_195(x):
    # x is a list (or vector) of length 256
    return max(0, x[132])
def l264_196(x):
    # x is a list (or vector) of length 256
    return max(0, x[133])
def l264_197(x):
    # x is a list (or vector) of length 256
    return max(0, x[134])
def l264_198(x):
    # x is a list (or vector) of length 256
    return max(0, x[135])
def l264_199(x):
    # x is a list (or vector) of length 256
    return max(0, x[136])
def l264_200(x):
    # x is a list (or vector) of length 256
    return max(0, x[137])
def l264_201(x):
    # x is a list (or vector) of length 256
    return max(0, x[138])
def l264_202(x):
    # x is a list (or vector) of length 256
    return max(0, x[139])
def l264_203(x):
    # x is a list (or vector) of length 256
    return max(0, x[140])
def l264_204(x):
    # x is a list (or vector) of length 256
    return max(0, x[141])
def l264_205(x):
    # x is a list (or vector) of length 256
    return max(0, x[142])
def l264_206(x):
    # x is a list (or vector) of length 256
    return max(0, x[143])
def l264_207(x):
    # x is a list (or vector) of length 256
    return max(0, x[144])
def l264_208(x):
    # x is a list (or vector) of length 256
    return max(0, x[145])
def l264_209(x):
    # x is a list (or vector) of length 256
    return max(0, x[146])
def l264_210(x):
    # x is a list (or vector) of length 256
    return max(0, x[147])
def l264_211(x):
    # x is a list (or vector) of length 256
    return max(0, x[148])
def l264_212(x):
    # x is a list (or vector) of length 256
    return max(0, x[149])
def l264_213(x):
    # x is a list (or vector) of length 256
    return max(0, x[150])
def l264_214(x):
    # x is a list (or vector) of length 256
    return max(0, x[151])
def l264_215(x):
    # x is a list (or vector) of length 256
    return max(0, x[152])
def l264_216(x):
    # x is a list (or vector) of length 256
    return max(0, x[153])
def l264_217(x):
    # x is a list (or vector) of length 256
    return max(0, x[154])
def l264_218(x):
    # x is a list (or vector) of length 256
    return max(0, x[155])
def l264_219(x):
    # x is a list (or vector) of length 256
    return max(0, x[156])
def l264_220(x):
    # x is a list (or vector) of length 256
    return max(0, x[157])
def l264_221(x):
    # x is a list (or vector) of length 256
    return max(0, x[158])
def l264_222(x):
    # x is a list (or vector) of length 256
    return max(0, x[159])
def l264_223(x):
    # x is a list (or vector) of length 256
    return max(0, x[160])
def l264_224(x):
    # x is a list (or vector) of length 256
    return max(0, x[161])
def l264_225(x):
    # x is a list (or vector) of length 256
    return max(0, x[162])
def l264_226(x):
    # x is a list (or vector) of length 256
    return max(0, x[163])
def l264_227(x):
    # x is a list (or vector) of length 256
    return max(0, x[164])
def l264_228(x):
    # x is a list (or vector) of length 256
    return max(0, x[165])
def l264_229(x):
    # x is a list (or vector) of length 256
    return max(0, x[166])
def l264_230(x):
    # x is a list (or vector) of length 256
    return max(0, x[167])
def l264_231(x):
    # x is a list (or vector) of length 256
    return max(0, x[168])
def l264_232(x):
    # x is a list (or vector) of length 256
    return max(0, x[169])
def l264_233(x):
    # x is a list (or vector) of length 256
    return max(0, x[170])
def l264_234(x):
    # x is a list (or vector) of length 256
    return max(0, x[171])
def l264_235(x):
    # x is a list (or vector) of length 256
    return max(0, x[172])
def l264_236(x):
    # x is a list (or vector) of length 256
    return max(0, x[173])
def l264_237(x):
    # x is a list (or vector) of length 256
    return max(0, x[174])
def l264_238(x):
    # x is a list (or vector) of length 256
    return max(0, x[175])
def l264_239(x):
    # x is a list (or vector) of length 256
    return max(0, x[176])
def l264_240(x):
    # x is a list (or vector) of length 256
    return max(0, x[177])
def l264_241(x):
    # x is a list (or vector) of length 256
    return max(0, x[178])
def l264_242(x):
    # x is a list (or vector) of length 256
    return max(0, x[179])
def l264_243(x):
    # x is a list (or vector) of length 256
    return max(0, x[180])
def l264_244(x):
    # x is a list (or vector) of length 256
    return max(0, x[181])
def l264_245(x):
    # x is a list (or vector) of length 256
    return max(0, x[182])
def l264_246(x):
    # x is a list (or vector) of length 256
    return max(0, x[183])
def l264_247(x):
    # x is a list (or vector) of length 256
    return max(0, x[184])
def l264_248(x):
    # x is a list (or vector) of length 256
    return max(0, x[185])
def l264_249(x):
    # x is a list (or vector) of length 256
    return max(0, x[186])
def l264_250(x):
    # x is a list (or vector) of length 256
    return max(0, x[187])
def l264_251(x):
    # x is a list (or vector) of length 256
    return max(0, x[188])
def l264_252(x):
    # x is a list (or vector) of length 256
    return max(0, x[189])
def l264_253(x):
    # x is a list (or vector) of length 256
    return max(0, x[190])
def l264_254(x):
    # x is a list (or vector) of length 256
    return max(0, x[191])
def l264_255(x):
    # x is a list (or vector) of length 256
    return max(0, x[192])
def l264_256(x):
    # x is a list (or vector) of length 256
    return max(0, x[193])
def l264_257(x):
    # x is a list (or vector) of length 256
    return max(0, x[194])
def l264_258(x):
    # x is a list (or vector) of length 256
    return max(0, x[195])
def l264_259(x):
    # x is a list (or vector) of length 256
    return max(0, x[196])
def l264_260(x):
    # x is a list (or vector) of length 256
    return max(0, x[197])
def l264_261(x):
    # x is a list (or vector) of length 256
    return max(0, x[198])
def l264_262(x):
    # x is a list (or vector) of length 256
    return max(0, x[199])
def l264_263(x):
    # x is a list (or vector) of length 256
    return max(0, x[200])
def l264_264(x):
    # x is a list (or vector) of length 256
    return max(0, x[201])
def l264_265(x):
    # x is a list (or vector) of length 256
    return max(0, x[202])
def l264_266(x):
    # x is a list (or vector) of length 256
    return max(0, x[203])
def l264_267(x):
    # x is a list (or vector) of length 256
    return max(0, x[204])
def l264_268(x):
    # x is a list (or vector) of length 256
    return max(0, x[205])
def l264_269(x):
    # x is a list (or vector) of length 256
    return max(0, x[206])
def l264_270(x):
    # x is a list (or vector) of length 256
    return max(0, x[207])
def l264_271(x):
    # x is a list (or vector) of length 256
    return max(0, x[208])
def l264_272(x):
    # x is a list (or vector) of length 256
    return max(0, x[209])
def l264_273(x):
    # x is a list (or vector) of length 256
    return max(0, x[210])
def l264_274(x):
    # x is a list (or vector) of length 256
    return max(0, x[211])
def l264_275(x):
    # x is a list (or vector) of length 256
    return max(0, x[212])
def l264_276(x):
    # x is a list (or vector) of length 256
    return max(0, x[213])
def l264_277(x):
    # x is a list (or vector) of length 256
    return max(0, x[214])
def l264_278(x):
    # x is a list (or vector) of length 256
    return max(0, x[215])
def l264_279(x):
    # x is a list (or vector) of length 256
    return max(0, x[216])
def l264_280(x):
    # x is a list (or vector) of length 256
    return max(0, x[217])
def l264_281(x):
    # x is a list (or vector) of length 256
    return max(0, x[218])
def l264_282(x):
    # x is a list (or vector) of length 256
    return max(0, x[219])
def l264_283(x):
    # x is a list (or vector) of length 256
    return max(0, x[220])
def l264_284(x):
    # x is a list (or vector) of length 256
    return max(0, x[221])
def l264_285(x):
    # x is a list (or vector) of length 256
    return max(0, x[222])
def l264_286(x):
    # x is a list (or vector) of length 256
    return max(0, x[223])
def l264_287(x):
    # x is a list (or vector) of length 256
    return max(0, x[224])
def l264_288(x):
    # x is a list (or vector) of length 256
    return max(0, x[225])
def l264_289(x):
    # x is a list (or vector) of length 256
    return max(0, x[226])
def l264_290(x):
    # x is a list (or vector) of length 256
    return max(0, x[227])
def l264_291(x):
    # x is a list (or vector) of length 256
    return max(0, x[228])
def l264_292(x):
    # x is a list (or vector) of length 256
    return max(0, x[229])
def l264_293(x):
    # x is a list (or vector) of length 256
    return max(0, x[230])
def l264_294(x):
    # x is a list (or vector) of length 256
    return max(0, x[231])
def l264_295(x):
    # x is a list (or vector) of length 256
    return max(0, x[232])
def l264_296(x):
    # x is a list (or vector) of length 256
    return max(0, x[233])
def l264_297(x):
    # x is a list (or vector) of length 256
    return max(0, x[234])
def l264_298(x):
    # x is a list (or vector) of length 256
    return max(0, x[235])
def l264_299(x):
    # x is a list (or vector) of length 256
    return max(0, x[236])
def l264_300(x):
    # x is a list (or vector) of length 256
    return max(0, x[237])
def l264_301(x):
    # x is a list (or vector) of length 256
    return max(0, x[238])
def l264_302(x):
    # x is a list (or vector) of length 256
    return max(0, x[239])
def l264_303(x):
    # x is a list (or vector) of length 256
    return max(0, x[240])
def l264_304(x):
    # x is a list (or vector) of length 256
    return max(0, x[241])
def l264_305(x):
    # x is a list (or vector) of length 256
    return max(0, x[242])
def l264_306(x):
    # x is a list (or vector) of length 256
    return max(0, x[243])
def l264_307(x):
    # x is a list (or vector) of length 256
    return max(0, x[244])
def l264_308(x):
    # x is a list (or vector) of length 256
    return max(0, x[245])
def l264_309(x):
    # x is a list (or vector) of length 256
    return max(0, x[246])
def l264_310(x):
    # x is a list (or vector) of length 256
    return max(0, x[247])
def l264_311(x):
    # x is a list (or vector) of length 256
    return max(0, x[248])
def l264_312(x):
    # x is a list (or vector) of length 256
    return max(0, x[249])
def l264_313(x):
    # x is a list (or vector) of length 256
    return max(0, x[250])
def l264_314(x):
    # x is a list (or vector) of length 256
    return max(0, x[251])
def l264_315(x):
    # x is a list (or vector) of length 256
    return max(0, x[252])
def l264_316(x):
    # x is a list (or vector) of length 256
    return max(0, x[253])
def l264_317(x):
    # x is a list (or vector) of length 256
    return max(0, x[254])
def l264_318(x):
    # x is a list (or vector) of length 256
    return max(0, x[255])
def l264_(x):
    # x is a list (or vector) of length 256
    return [
        l264_0(x),
        l264_1(x),
        l264_2(x),
        l264_3(x),
        l264_4(x),
        l264_5(x),
        l264_6(x),
        l264_7(x),
        l264_8(x),
        l264_9(x),
        l264_10(x),
        l264_11(x),
        l264_12(x),
        l264_13(x),
        l264_14(x),
        l264_15(x),
        l264_16(x),
        l264_17(x),
        l264_18(x),
        l264_19(x),
        l264_20(x),
        l264_21(x),
        l264_22(x),
        l264_23(x),
        l264_24(x),
        l264_25(x),
        l264_26(x),
        l264_27(x),
        l264_28(x),
        l264_29(x),
        l264_30(x),
        l264_31(x),
        l264_32(x),
        l264_33(x),
        l264_34(x),
        l264_35(x),
        l264_36(x),
        l264_37(x),
        l264_38(x),
        l264_39(x),
        l264_40(x),
        l264_41(x),
        l264_42(x),
        l264_43(x),
        l264_44(x),
        l264_45(x),
        l264_46(x),
        l264_47(x),
        l264_48(x),
        l264_49(x),
        l264_50(x),
        l264_51(x),
        l264_52(x),
        l264_53(x),
        l264_54(x),
        l264_55(x),
        l264_56(x),
        l264_57(x),
        l264_58(x),
        l264_59(x),
        l264_60(x),
        l264_61(x),
        l264_62(x),
        l264_63(x),
        l264_64(x),
        l264_65(x),
        l264_66(x),
        l264_67(x),
        l264_68(x),
        l264_69(x),
        l264_70(x),
        l264_71(x),
        l264_72(x),
        l264_73(x),
        l264_74(x),
        l264_75(x),
        l264_76(x),
        l264_77(x),
        l264_78(x),
        l264_79(x),
        l264_80(x),
        l264_81(x),
        l264_82(x),
        l264_83(x),
        l264_84(x),
        l264_85(x),
        l264_86(x),
        l264_87(x),
        l264_88(x),
        l264_89(x),
        l264_90(x),
        l264_91(x),
        l264_92(x),
        l264_93(x),
        l264_94(x),
        l264_95(x),
        l264_96(x),
        l264_97(x),
        l264_98(x),
        l264_99(x),
        l264_100(x),
        l264_101(x),
        l264_102(x),
        l264_103(x),
        l264_104(x),
        l264_105(x),
        l264_106(x),
        l264_107(x),
        l264_108(x),
        l264_109(x),
        l264_110(x),
        l264_111(x),
        l264_112(x),
        l264_113(x),
        l264_114(x),
        l264_115(x),
        l264_116(x),
        l264_117(x),
        l264_118(x),
        l264_119(x),
        l264_120(x),
        l264_121(x),
        l264_122(x),
        l264_123(x),
        l264_124(x),
        l264_125(x),
        l264_126(x),
        l264_127(x),
        l264_128(x),
        l264_129(x),
        l264_130(x),
        l264_131(x),
        l264_132(x),
        l264_133(x),
        l264_134(x),
        l264_135(x),
        l264_136(x),
        l264_137(x),
        l264_138(x),
        l264_139(x),
        l264_140(x),
        l264_141(x),
        l264_142(x),
        l264_143(x),
        l264_144(x),
        l264_145(x),
        l264_146(x),
        l264_147(x),
        l264_148(x),
        l264_149(x),
        l264_150(x),
        l264_151(x),
        l264_152(x),
        l264_153(x),
        l264_154(x),
        l264_155(x),
        l264_156(x),
        l264_157(x),
        l264_158(x),
        l264_159(x),
        l264_160(x),
        l264_161(x),
        l264_162(x),
        l264_163(x),
        l264_164(x),
        l264_165(x),
        l264_166(x),
        l264_167(x),
        l264_168(x),
        l264_169(x),
        l264_170(x),
        l264_171(x),
        l264_172(x),
        l264_173(x),
        l264_174(x),
        l264_175(x),
        l264_176(x),
        l264_177(x),
        l264_178(x),
        l264_179(x),
        l264_180(x),
        l264_181(x),
        l264_182(x),
        l264_183(x),
        l264_184(x),
        l264_185(x),
        l264_186(x),
        l264_187(x),
        l264_188(x),
        l264_189(x),
        l264_190(x),
        l264_191(x),
        l264_192(x),
        l264_193(x),
        l264_194(x),
        l264_195(x),
        l264_196(x),
        l264_197(x),
        l264_198(x),
        l264_199(x),
        l264_200(x),
        l264_201(x),
        l264_202(x),
        l264_203(x),
        l264_204(x),
        l264_205(x),
        l264_206(x),
        l264_207(x),
        l264_208(x),
        l264_209(x),
        l264_210(x),
        l264_211(x),
        l264_212(x),
        l264_213(x),
        l264_214(x),
        l264_215(x),
        l264_216(x),
        l264_217(x),
        l264_218(x),
        l264_219(x),
        l264_220(x),
        l264_221(x),
        l264_222(x),
        l264_223(x),
        l264_224(x),
        l264_225(x),
        l264_226(x),
        l264_227(x),
        l264_228(x),
        l264_229(x),
        l264_230(x),
        l264_231(x),
        l264_232(x),
        l264_233(x),
        l264_234(x),
        l264_235(x),
        l264_236(x),
        l264_237(x),
        l264_238(x),
        l264_239(x),
        l264_240(x),
        l264_241(x),
        l264_242(x),
        l264_243(x),
        l264_244(x),
        l264_245(x),
        l264_246(x),
        l264_247(x),
        l264_248(x),
        l264_249(x),
        l264_250(x),
        l264_251(x),
        l264_252(x),
        l264_253(x),
        l264_254(x),
        l264_255(x),
        l264_256(x),
        l264_257(x),
        l264_258(x),
        l264_259(x),
        l264_260(x),
        l264_261(x),
        l264_262(x),
        l264_263(x),
        l264_264(x),
        l264_265(x),
        l264_266(x),
        l264_267(x),
        l264_268(x),
        l264_269(x),
        l264_270(x),
        l264_271(x),
        l264_272(x),
        l264_273(x),
        l264_274(x),
        l264_275(x),
        l264_276(x),
        l264_277(x),
        l264_278(x),
        l264_279(x),
        l264_280(x),
        l264_281(x),
        l264_282(x),
        l264_283(x),
        l264_284(x),
        l264_285(x),
        l264_286(x),
        l264_287(x),
        l264_288(x),
        l264_289(x),
        l264_290(x),
        l264_291(x),
        l264_292(x),
        l264_293(x),
        l264_294(x),
        l264_295(x),
        l264_296(x),
        l264_297(x),
        l264_298(x),
        l264_299(x),
        l264_300(x),
        l264_301(x),
        l264_302(x),
        l264_303(x),
        l264_304(x),
        l264_305(x),
        l264_306(x),
        l264_307(x),
        l264_308(x),
        l264_309(x),
        l264_310(x),
        l264_311(x),
        l264_312(x),
        l264_313(x),
        l264_314(x),
        l264_315(x),
        l264_316(x),
        l264_317(x),
        l264_318(x),
    ]