import numpy as np




# Generated from reverse engineering
def l348_g(x: np.ndarray) -> np.ndarray:
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




def l348_0(x):
    # x is a list (or vector) of length 256
    return max(0, x[0])
def l348_1(x):
    # x is a list (or vector) of length 256
    return max(0, x[1])
def l348_2(x):
    # x is a list (or vector) of length 256
    return max(0, x[2])
def l348_3(x):
    # x is a list (or vector) of length 256
    return max(0, x[3])
def l348_4(x):
    # x is a list (or vector) of length 256
    return max(0, x[4])
def l348_5(x):
    # x is a list (or vector) of length 256
    return max(0, x[5])
def l348_6(x):
    # x is a list (or vector) of length 256
    return max(0, x[6])
def l348_7(x):
    # x is a list (or vector) of length 256
    return max(0, x[7])
def l348_8(x):
    # x is a list (or vector) of length 256
    return max(0, x[8])
def l348_9(x):
    # x is a list (or vector) of length 256
    return max(0, x[9])
def l348_10(x):
    # x is a list (or vector) of length 256
    return max(0, x[10])
def l348_11(x):
    # x is a list (or vector) of length 256
    return max(0, x[11])
def l348_12(x):
    # x is a list (or vector) of length 256
    return max(0, x[12])
def l348_13(x):
    # x is a list (or vector) of length 256
    return max(0, x[13])
def l348_14(x):
    # x is a list (or vector) of length 256
    return max(0, x[14])
def l348_15(x):
    # x is a list (or vector) of length 256
    return max(0, x[15])
def l348_16(x):
    # x is a list (or vector) of length 256
    return max(0, x[16])
def l348_17(x):
    # x is a list (or vector) of length 256
    return max(0, x[17])
def l348_18(x):
    # x is a list (or vector) of length 256
    return max(0, x[18])
def l348_19(x):
    # x is a list (or vector) of length 256
    return max(0, x[19])
def l348_20(x):
    # x is a list (or vector) of length 256
    return max(0, x[20])
def l348_21(x):
    # x is a list (or vector) of length 256
    return max(0, x[21])
def l348_22(x):
    # x is a list (or vector) of length 256
    return max(0, x[22])
def l348_23(x):
    # x is a list (or vector) of length 256
    return max(0, x[23])
def l348_24(x):
    # x is a list (or vector) of length 256
    return max(0, x[24])
def l348_25(x):
    # x is a list (or vector) of length 256
    return max(0, x[25])
def l348_26(x):
    # x is a list (or vector) of length 256
    return max(0, x[26])
def l348_27(x):
    # x is a list (or vector) of length 256
    return max(0, x[27])
def l348_28(x):
    # x is a list (or vector) of length 256
    return max(0, x[28])
def l348_29(x):
    # x is a list (or vector) of length 256
    return max(0, x[29])
def l348_30(x):
    # x is a list (or vector) of length 256
    return max(0, x[30])
def l348_31(x):
    # x is a list (or vector) of length 256
    return max(0, x[31])
def l348_32(x):
    # x is a list (or vector) of length 256
    return max(0, x[32])
def l348_33(x):
    # x is a list (or vector) of length 256
    return max(0, x[32] + x[65] + -1.0)
def l348_34(x):
    # x is a list (or vector) of length 256
    return max(0, x[33] + x[66] + -1.0)
def l348_35(x):
    # x is a list (or vector) of length 256
    return max(0, x[34] + x[67] + -1.0)
def l348_36(x):
    # x is a list (or vector) of length 256
    return max(0, x[35] + x[68] + -1.0)
def l348_37(x):
    # x is a list (or vector) of length 256
    return max(0, x[36] + x[69] + -1.0)
def l348_38(x):
    # x is a list (or vector) of length 256
    return max(0, x[37] + x[70] + -1.0)
def l348_39(x):
    # x is a list (or vector) of length 256
    return max(0, x[38] + x[71] + -1.0)
def l348_40(x):
    # x is a list (or vector) of length 256
    return max(0, x[39] + x[72] + -1.0)
def l348_41(x):
    # x is a list (or vector) of length 256
    return max(0, x[40] + x[73] + -1.0)
def l348_42(x):
    # x is a list (or vector) of length 256
    return max(0, x[41] + x[74] + -1.0)
def l348_43(x):
    # x is a list (or vector) of length 256
    return max(0, x[42] + x[75] + -1.0)
def l348_44(x):
    # x is a list (or vector) of length 256
    return max(0, x[43] + x[76] + -1.0)
def l348_45(x):
    # x is a list (or vector) of length 256
    return max(0, x[44] + x[77] + -1.0)
def l348_46(x):
    # x is a list (or vector) of length 256
    return max(0, x[45] + x[78] + -1.0)
def l348_47(x):
    # x is a list (or vector) of length 256
    return max(0, x[46] + x[79] + -1.0)
def l348_48(x):
    # x is a list (or vector) of length 256
    return max(0, x[47] + x[80] + -1.0)
def l348_49(x):
    # x is a list (or vector) of length 256
    return max(0, x[48] + x[81] + -1.0)
def l348_50(x):
    # x is a list (or vector) of length 256
    return max(0, x[49] + x[82] + -1.0)
def l348_51(x):
    # x is a list (or vector) of length 256
    return max(0, x[50] + x[83] + -1.0)
def l348_52(x):
    # x is a list (or vector) of length 256
    return max(0, x[51] + x[84] + -1.0)
def l348_53(x):
    # x is a list (or vector) of length 256
    return max(0, x[52] + x[85] + -1.0)
def l348_54(x):
    # x is a list (or vector) of length 256
    return max(0, x[53] + x[86] + -1.0)
def l348_55(x):
    # x is a list (or vector) of length 256
    return max(0, x[54] + x[87] + -1.0)
def l348_56(x):
    # x is a list (or vector) of length 256
    return max(0, x[55] + x[88] + -1.0)
def l348_57(x):
    # x is a list (or vector) of length 256
    return max(0, x[56] + x[89] + -1.0)
def l348_58(x):
    # x is a list (or vector) of length 256
    return max(0, x[57] + x[90] + -1.0)
def l348_59(x):
    # x is a list (or vector) of length 256
    return max(0, x[58] + x[91] + -1.0)
def l348_60(x):
    # x is a list (or vector) of length 256
    return max(0, x[59] + x[92] + -1.0)
def l348_61(x):
    # x is a list (or vector) of length 256
    return max(0, x[60] + x[93] + -1.0)
def l348_62(x):
    # x is a list (or vector) of length 256
    return max(0, x[61] + x[94] + -1.0)
def l348_63(x):
    # x is a list (or vector) of length 256
    return max(0, x[62] + x[95] + -1.0)
def l348_64(x):
    # x is a list (or vector) of length 256
    return max(0, x[33])
def l348_65(x):
    # x is a list (or vector) of length 256
    return max(0, x[34])
def l348_66(x):
    # x is a list (or vector) of length 256
    return max(0, x[35])
def l348_67(x):
    # x is a list (or vector) of length 256
    return max(0, x[36])
def l348_68(x):
    # x is a list (or vector) of length 256
    return max(0, x[37])
def l348_69(x):
    # x is a list (or vector) of length 256
    return max(0, x[38])
def l348_70(x):
    # x is a list (or vector) of length 256
    return max(0, x[39])
def l348_71(x):
    # x is a list (or vector) of length 256
    return max(0, x[40])
def l348_72(x):
    # x is a list (or vector) of length 256
    return max(0, x[41])
def l348_73(x):
    # x is a list (or vector) of length 256
    return max(0, x[42])
def l348_74(x):
    # x is a list (or vector) of length 256
    return max(0, x[43])
def l348_75(x):
    # x is a list (or vector) of length 256
    return max(0, x[44])
def l348_76(x):
    # x is a list (or vector) of length 256
    return max(0, x[45])
def l348_77(x):
    # x is a list (or vector) of length 256
    return max(0, x[46])
def l348_78(x):
    # x is a list (or vector) of length 256
    return max(0, x[47])
def l348_79(x):
    # x is a list (or vector) of length 256
    return max(0, x[48])
def l348_80(x):
    # x is a list (or vector) of length 256
    return max(0, x[49])
def l348_81(x):
    # x is a list (or vector) of length 256
    return max(0, x[50])
def l348_82(x):
    # x is a list (or vector) of length 256
    return max(0, x[51])
def l348_83(x):
    # x is a list (or vector) of length 256
    return max(0, x[52])
def l348_84(x):
    # x is a list (or vector) of length 256
    return max(0, x[53])
def l348_85(x):
    # x is a list (or vector) of length 256
    return max(0, x[54])
def l348_86(x):
    # x is a list (or vector) of length 256
    return max(0, x[55])
def l348_87(x):
    # x is a list (or vector) of length 256
    return max(0, x[56])
def l348_88(x):
    # x is a list (or vector) of length 256
    return max(0, x[57])
def l348_89(x):
    # x is a list (or vector) of length 256
    return max(0, x[58])
def l348_90(x):
    # x is a list (or vector) of length 256
    return max(0, x[59])
def l348_91(x):
    # x is a list (or vector) of length 256
    return max(0, x[60])
def l348_92(x):
    # x is a list (or vector) of length 256
    return max(0, x[61])
def l348_93(x):
    # x is a list (or vector) of length 256
    return max(0, x[62])
def l348_94(x):
    # x is a list (or vector) of length 256
    return max(0, x[63])
def l348_95(x):
    # x is a list (or vector) of length 256
    return max(0, x[64] + x[65] + -1.0)
def l348_96(x):
    # x is a list (or vector) of length 256
    return max(0, x[65] + x[66] + -1.0)
def l348_97(x):
    # x is a list (or vector) of length 256
    return max(0, x[66] + x[67] + -1.0)
def l348_98(x):
    # x is a list (or vector) of length 256
    return max(0, x[67] + x[68] + -1.0)
def l348_99(x):
    # x is a list (or vector) of length 256
    return max(0, x[68] + x[69] + -1.0)
def l348_100(x):
    # x is a list (or vector) of length 256
    return max(0, x[69] + x[70] + -1.0)
def l348_101(x):
    # x is a list (or vector) of length 256
    return max(0, x[70] + x[71] + -1.0)
def l348_102(x):
    # x is a list (or vector) of length 256
    return max(0, x[71] + x[72] + -1.0)
def l348_103(x):
    # x is a list (or vector) of length 256
    return max(0, x[72] + x[73] + -1.0)
def l348_104(x):
    # x is a list (or vector) of length 256
    return max(0, x[73] + x[74] + -1.0)
def l348_105(x):
    # x is a list (or vector) of length 256
    return max(0, x[74] + x[75] + -1.0)
def l348_106(x):
    # x is a list (or vector) of length 256
    return max(0, x[75] + x[76] + -1.0)
def l348_107(x):
    # x is a list (or vector) of length 256
    return max(0, x[76] + x[77] + -1.0)
def l348_108(x):
    # x is a list (or vector) of length 256
    return max(0, x[77] + x[78] + -1.0)
def l348_109(x):
    # x is a list (or vector) of length 256
    return max(0, x[78] + x[79] + -1.0)
def l348_110(x):
    # x is a list (or vector) of length 256
    return max(0, x[79] + x[80] + -1.0)
def l348_111(x):
    # x is a list (or vector) of length 256
    return max(0, x[80] + x[81] + -1.0)
def l348_112(x):
    # x is a list (or vector) of length 256
    return max(0, x[81] + x[82] + -1.0)
def l348_113(x):
    # x is a list (or vector) of length 256
    return max(0, x[82] + x[83] + -1.0)
def l348_114(x):
    # x is a list (or vector) of length 256
    return max(0, x[83] + x[84] + -1.0)
def l348_115(x):
    # x is a list (or vector) of length 256
    return max(0, x[84] + x[85] + -1.0)
def l348_116(x):
    # x is a list (or vector) of length 256
    return max(0, x[85] + x[86] + -1.0)
def l348_117(x):
    # x is a list (or vector) of length 256
    return max(0, x[86] + x[87] + -1.0)
def l348_118(x):
    # x is a list (or vector) of length 256
    return max(0, x[87] + x[88] + -1.0)
def l348_119(x):
    # x is a list (or vector) of length 256
    return max(0, x[88] + x[89] + -1.0)
def l348_120(x):
    # x is a list (or vector) of length 256
    return max(0, x[89] + x[90] + -1.0)
def l348_121(x):
    # x is a list (or vector) of length 256
    return max(0, x[90] + x[91] + -1.0)
def l348_122(x):
    # x is a list (or vector) of length 256
    return max(0, x[91] + x[92] + -1.0)
def l348_123(x):
    # x is a list (or vector) of length 256
    return max(0, x[92] + x[93] + -1.0)
def l348_124(x):
    # x is a list (or vector) of length 256
    return max(0, x[93] + x[94] + -1.0)
def l348_125(x):
    # x is a list (or vector) of length 256
    return max(0, x[94] + x[95] + -1.0)
def l348_126(x):
    # x is a list (or vector) of length 256
    return max(0, x[64])
def l348_127(x):
    # x is a list (or vector) of length 256
    return max(0, x[64])
def l348_128(x):
    # x is a list (or vector) of length 256
    return max(0, x[65])
def l348_129(x):
    # x is a list (or vector) of length 256
    return max(0, x[66])
def l348_130(x):
    # x is a list (or vector) of length 256
    return max(0, x[67])
def l348_131(x):
    # x is a list (or vector) of length 256
    return max(0, x[68])
def l348_132(x):
    # x is a list (or vector) of length 256
    return max(0, x[69])
def l348_133(x):
    # x is a list (or vector) of length 256
    return max(0, x[70])
def l348_134(x):
    # x is a list (or vector) of length 256
    return max(0, x[71])
def l348_135(x):
    # x is a list (or vector) of length 256
    return max(0, x[72])
def l348_136(x):
    # x is a list (or vector) of length 256
    return max(0, x[73])
def l348_137(x):
    # x is a list (or vector) of length 256
    return max(0, x[74])
def l348_138(x):
    # x is a list (or vector) of length 256
    return max(0, x[75])
def l348_139(x):
    # x is a list (or vector) of length 256
    return max(0, x[76])
def l348_140(x):
    # x is a list (or vector) of length 256
    return max(0, x[77])
def l348_141(x):
    # x is a list (or vector) of length 256
    return max(0, x[78])
def l348_142(x):
    # x is a list (or vector) of length 256
    return max(0, x[79])
def l348_143(x):
    # x is a list (or vector) of length 256
    return max(0, x[80])
def l348_144(x):
    # x is a list (or vector) of length 256
    return max(0, x[81])
def l348_145(x):
    # x is a list (or vector) of length 256
    return max(0, x[82])
def l348_146(x):
    # x is a list (or vector) of length 256
    return max(0, x[83])
def l348_147(x):
    # x is a list (or vector) of length 256
    return max(0, x[84])
def l348_148(x):
    # x is a list (or vector) of length 256
    return max(0, x[85])
def l348_149(x):
    # x is a list (or vector) of length 256
    return max(0, x[86])
def l348_150(x):
    # x is a list (or vector) of length 256
    return max(0, x[87])
def l348_151(x):
    # x is a list (or vector) of length 256
    return max(0, x[88])
def l348_152(x):
    # x is a list (or vector) of length 256
    return max(0, x[89])
def l348_153(x):
    # x is a list (or vector) of length 256
    return max(0, x[90])
def l348_154(x):
    # x is a list (or vector) of length 256
    return max(0, x[91])
def l348_155(x):
    # x is a list (or vector) of length 256
    return max(0, x[92])
def l348_156(x):
    # x is a list (or vector) of length 256
    return max(0, x[93])
def l348_157(x):
    # x is a list (or vector) of length 256
    return max(0, x[94])
def l348_158(x):
    # x is a list (or vector) of length 256
    return max(0, x[95])
def l348_159(x):
    # x is a list (or vector) of length 256
    return max(0, x[96])
def l348_160(x):
    # x is a list (or vector) of length 256
    return max(0, x[97])
def l348_161(x):
    # x is a list (or vector) of length 256
    return max(0, x[98])
def l348_162(x):
    # x is a list (or vector) of length 256
    return max(0, x[99])
def l348_163(x):
    # x is a list (or vector) of length 256
    return max(0, x[100])
def l348_164(x):
    # x is a list (or vector) of length 256
    return max(0, x[101])
def l348_165(x):
    # x is a list (or vector) of length 256
    return max(0, x[102])
def l348_166(x):
    # x is a list (or vector) of length 256
    return max(0, x[103])
def l348_167(x):
    # x is a list (or vector) of length 256
    return max(0, x[104])
def l348_168(x):
    # x is a list (or vector) of length 256
    return max(0, x[105])
def l348_169(x):
    # x is a list (or vector) of length 256
    return max(0, x[106])
def l348_170(x):
    # x is a list (or vector) of length 256
    return max(0, x[107])
def l348_171(x):
    # x is a list (or vector) of length 256
    return max(0, x[108])
def l348_172(x):
    # x is a list (or vector) of length 256
    return max(0, x[109])
def l348_173(x):
    # x is a list (or vector) of length 256
    return max(0, x[110])
def l348_174(x):
    # x is a list (or vector) of length 256
    return max(0, x[111])
def l348_175(x):
    # x is a list (or vector) of length 256
    return max(0, x[112])
def l348_176(x):
    # x is a list (or vector) of length 256
    return max(0, x[113])
def l348_177(x):
    # x is a list (or vector) of length 256
    return max(0, x[114])
def l348_178(x):
    # x is a list (or vector) of length 256
    return max(0, x[115])
def l348_179(x):
    # x is a list (or vector) of length 256
    return max(0, x[116])
def l348_180(x):
    # x is a list (or vector) of length 256
    return max(0, x[117])
def l348_181(x):
    # x is a list (or vector) of length 256
    return max(0, x[118])
def l348_182(x):
    # x is a list (or vector) of length 256
    return max(0, x[119])
def l348_183(x):
    # x is a list (or vector) of length 256
    return max(0, x[120])
def l348_184(x):
    # x is a list (or vector) of length 256
    return max(0, x[121])
def l348_185(x):
    # x is a list (or vector) of length 256
    return max(0, x[122])
def l348_186(x):
    # x is a list (or vector) of length 256
    return max(0, x[123])
def l348_187(x):
    # x is a list (or vector) of length 256
    return max(0, x[124])
def l348_188(x):
    # x is a list (or vector) of length 256
    return max(0, x[125])
def l348_189(x):
    # x is a list (or vector) of length 256
    return max(0, x[126])
def l348_190(x):
    # x is a list (or vector) of length 256
    return max(0, x[127])
def l348_191(x):
    # x is a list (or vector) of length 256
    return max(0, x[128])
def l348_192(x):
    # x is a list (or vector) of length 256
    return max(0, x[129])
def l348_193(x):
    # x is a list (or vector) of length 256
    return max(0, x[130])
def l348_194(x):
    # x is a list (or vector) of length 256
    return max(0, x[131])
def l348_195(x):
    # x is a list (or vector) of length 256
    return max(0, x[132])
def l348_196(x):
    # x is a list (or vector) of length 256
    return max(0, x[133])
def l348_197(x):
    # x is a list (or vector) of length 256
    return max(0, x[134])
def l348_198(x):
    # x is a list (or vector) of length 256
    return max(0, x[135])
def l348_199(x):
    # x is a list (or vector) of length 256
    return max(0, x[136])
def l348_200(x):
    # x is a list (or vector) of length 256
    return max(0, x[137])
def l348_201(x):
    # x is a list (or vector) of length 256
    return max(0, x[138])
def l348_202(x):
    # x is a list (or vector) of length 256
    return max(0, x[139])
def l348_203(x):
    # x is a list (or vector) of length 256
    return max(0, x[140])
def l348_204(x):
    # x is a list (or vector) of length 256
    return max(0, x[141])
def l348_205(x):
    # x is a list (or vector) of length 256
    return max(0, x[142])
def l348_206(x):
    # x is a list (or vector) of length 256
    return max(0, x[143])
def l348_207(x):
    # x is a list (or vector) of length 256
    return max(0, x[144])
def l348_208(x):
    # x is a list (or vector) of length 256
    return max(0, x[145])
def l348_209(x):
    # x is a list (or vector) of length 256
    return max(0, x[146])
def l348_210(x):
    # x is a list (or vector) of length 256
    return max(0, x[147])
def l348_211(x):
    # x is a list (or vector) of length 256
    return max(0, x[148])
def l348_212(x):
    # x is a list (or vector) of length 256
    return max(0, x[149])
def l348_213(x):
    # x is a list (or vector) of length 256
    return max(0, x[150])
def l348_214(x):
    # x is a list (or vector) of length 256
    return max(0, x[151])
def l348_215(x):
    # x is a list (or vector) of length 256
    return max(0, x[152])
def l348_216(x):
    # x is a list (or vector) of length 256
    return max(0, x[153])
def l348_217(x):
    # x is a list (or vector) of length 256
    return max(0, x[154])
def l348_218(x):
    # x is a list (or vector) of length 256
    return max(0, x[155])
def l348_219(x):
    # x is a list (or vector) of length 256
    return max(0, x[156])
def l348_220(x):
    # x is a list (or vector) of length 256
    return max(0, x[157])
def l348_221(x):
    # x is a list (or vector) of length 256
    return max(0, x[158])
def l348_222(x):
    # x is a list (or vector) of length 256
    return max(0, x[159])
def l348_223(x):
    # x is a list (or vector) of length 256
    return max(0, x[160])
def l348_224(x):
    # x is a list (or vector) of length 256
    return max(0, x[161])
def l348_225(x):
    # x is a list (or vector) of length 256
    return max(0, x[162])
def l348_226(x):
    # x is a list (or vector) of length 256
    return max(0, x[163])
def l348_227(x):
    # x is a list (or vector) of length 256
    return max(0, x[164])
def l348_228(x):
    # x is a list (or vector) of length 256
    return max(0, x[165])
def l348_229(x):
    # x is a list (or vector) of length 256
    return max(0, x[166])
def l348_230(x):
    # x is a list (or vector) of length 256
    return max(0, x[167])
def l348_231(x):
    # x is a list (or vector) of length 256
    return max(0, x[168])
def l348_232(x):
    # x is a list (or vector) of length 256
    return max(0, x[169])
def l348_233(x):
    # x is a list (or vector) of length 256
    return max(0, x[170])
def l348_234(x):
    # x is a list (or vector) of length 256
    return max(0, x[171])
def l348_235(x):
    # x is a list (or vector) of length 256
    return max(0, x[172])
def l348_236(x):
    # x is a list (or vector) of length 256
    return max(0, x[173])
def l348_237(x):
    # x is a list (or vector) of length 256
    return max(0, x[174])
def l348_238(x):
    # x is a list (or vector) of length 256
    return max(0, x[175])
def l348_239(x):
    # x is a list (or vector) of length 256
    return max(0, x[176])
def l348_240(x):
    # x is a list (or vector) of length 256
    return max(0, x[177])
def l348_241(x):
    # x is a list (or vector) of length 256
    return max(0, x[178])
def l348_242(x):
    # x is a list (or vector) of length 256
    return max(0, x[179])
def l348_243(x):
    # x is a list (or vector) of length 256
    return max(0, x[180])
def l348_244(x):
    # x is a list (or vector) of length 256
    return max(0, x[181])
def l348_245(x):
    # x is a list (or vector) of length 256
    return max(0, x[182])
def l348_246(x):
    # x is a list (or vector) of length 256
    return max(0, x[183])
def l348_247(x):
    # x is a list (or vector) of length 256
    return max(0, x[184])
def l348_248(x):
    # x is a list (or vector) of length 256
    return max(0, x[185])
def l348_249(x):
    # x is a list (or vector) of length 256
    return max(0, x[186])
def l348_250(x):
    # x is a list (or vector) of length 256
    return max(0, x[187])
def l348_251(x):
    # x is a list (or vector) of length 256
    return max(0, x[188])
def l348_252(x):
    # x is a list (or vector) of length 256
    return max(0, x[189])
def l348_253(x):
    # x is a list (or vector) of length 256
    return max(0, x[190])
def l348_254(x):
    # x is a list (or vector) of length 256
    return max(0, x[191])
def l348_255(x):
    # x is a list (or vector) of length 256
    return max(0, x[192])
def l348_256(x):
    # x is a list (or vector) of length 256
    return max(0, x[193])
def l348_257(x):
    # x is a list (or vector) of length 256
    return max(0, x[194])
def l348_258(x):
    # x is a list (or vector) of length 256
    return max(0, x[195])
def l348_259(x):
    # x is a list (or vector) of length 256
    return max(0, x[196])
def l348_260(x):
    # x is a list (or vector) of length 256
    return max(0, x[197])
def l348_261(x):
    # x is a list (or vector) of length 256
    return max(0, x[198])
def l348_262(x):
    # x is a list (or vector) of length 256
    return max(0, x[199])
def l348_263(x):
    # x is a list (or vector) of length 256
    return max(0, x[200])
def l348_264(x):
    # x is a list (or vector) of length 256
    return max(0, x[201])
def l348_265(x):
    # x is a list (or vector) of length 256
    return max(0, x[202])
def l348_266(x):
    # x is a list (or vector) of length 256
    return max(0, x[203])
def l348_267(x):
    # x is a list (or vector) of length 256
    return max(0, x[204])
def l348_268(x):
    # x is a list (or vector) of length 256
    return max(0, x[205])
def l348_269(x):
    # x is a list (or vector) of length 256
    return max(0, x[206])
def l348_270(x):
    # x is a list (or vector) of length 256
    return max(0, x[207])
def l348_271(x):
    # x is a list (or vector) of length 256
    return max(0, x[208])
def l348_272(x):
    # x is a list (or vector) of length 256
    return max(0, x[209])
def l348_273(x):
    # x is a list (or vector) of length 256
    return max(0, x[210])
def l348_274(x):
    # x is a list (or vector) of length 256
    return max(0, x[211])
def l348_275(x):
    # x is a list (or vector) of length 256
    return max(0, x[212])
def l348_276(x):
    # x is a list (or vector) of length 256
    return max(0, x[213])
def l348_277(x):
    # x is a list (or vector) of length 256
    return max(0, x[214])
def l348_278(x):
    # x is a list (or vector) of length 256
    return max(0, x[215])
def l348_279(x):
    # x is a list (or vector) of length 256
    return max(0, x[216])
def l348_280(x):
    # x is a list (or vector) of length 256
    return max(0, x[217])
def l348_281(x):
    # x is a list (or vector) of length 256
    return max(0, x[218])
def l348_282(x):
    # x is a list (or vector) of length 256
    return max(0, x[219])
def l348_283(x):
    # x is a list (or vector) of length 256
    return max(0, x[220])
def l348_284(x):
    # x is a list (or vector) of length 256
    return max(0, x[221])
def l348_285(x):
    # x is a list (or vector) of length 256
    return max(0, x[222])
def l348_286(x):
    # x is a list (or vector) of length 256
    return max(0, x[223])
def l348_287(x):
    # x is a list (or vector) of length 256
    return max(0, x[224])
def l348_288(x):
    # x is a list (or vector) of length 256
    return max(0, x[225])
def l348_289(x):
    # x is a list (or vector) of length 256
    return max(0, x[226])
def l348_290(x):
    # x is a list (or vector) of length 256
    return max(0, x[227])
def l348_291(x):
    # x is a list (or vector) of length 256
    return max(0, x[228])
def l348_292(x):
    # x is a list (or vector) of length 256
    return max(0, x[229])
def l348_293(x):
    # x is a list (or vector) of length 256
    return max(0, x[230])
def l348_294(x):
    # x is a list (or vector) of length 256
    return max(0, x[231])
def l348_295(x):
    # x is a list (or vector) of length 256
    return max(0, x[232])
def l348_296(x):
    # x is a list (or vector) of length 256
    return max(0, x[233])
def l348_297(x):
    # x is a list (or vector) of length 256
    return max(0, x[234])
def l348_298(x):
    # x is a list (or vector) of length 256
    return max(0, x[235])
def l348_299(x):
    # x is a list (or vector) of length 256
    return max(0, x[236])
def l348_300(x):
    # x is a list (or vector) of length 256
    return max(0, x[237])
def l348_301(x):
    # x is a list (or vector) of length 256
    return max(0, x[238])
def l348_302(x):
    # x is a list (or vector) of length 256
    return max(0, x[239])
def l348_303(x):
    # x is a list (or vector) of length 256
    return max(0, x[240])
def l348_304(x):
    # x is a list (or vector) of length 256
    return max(0, x[241])
def l348_305(x):
    # x is a list (or vector) of length 256
    return max(0, x[242])
def l348_306(x):
    # x is a list (or vector) of length 256
    return max(0, x[243])
def l348_307(x):
    # x is a list (or vector) of length 256
    return max(0, x[244])
def l348_308(x):
    # x is a list (or vector) of length 256
    return max(0, x[245])
def l348_309(x):
    # x is a list (or vector) of length 256
    return max(0, x[246])
def l348_310(x):
    # x is a list (or vector) of length 256
    return max(0, x[247])
def l348_311(x):
    # x is a list (or vector) of length 256
    return max(0, x[248])
def l348_312(x):
    # x is a list (or vector) of length 256
    return max(0, x[249])
def l348_313(x):
    # x is a list (or vector) of length 256
    return max(0, x[250])
def l348_314(x):
    # x is a list (or vector) of length 256
    return max(0, x[251])
def l348_315(x):
    # x is a list (or vector) of length 256
    return max(0, x[252])
def l348_316(x):
    # x is a list (or vector) of length 256
    return max(0, x[253])
def l348_317(x):
    # x is a list (or vector) of length 256
    return max(0, x[254])
def l348_318(x):
    # x is a list (or vector) of length 256
    return max(0, x[255])
def l348_(x):
    # x is a list (or vector) of length 256
    return [
        l348_0(x),
        l348_1(x),
        l348_2(x),
        l348_3(x),
        l348_4(x),
        l348_5(x),
        l348_6(x),
        l348_7(x),
        l348_8(x),
        l348_9(x),
        l348_10(x),
        l348_11(x),
        l348_12(x),
        l348_13(x),
        l348_14(x),
        l348_15(x),
        l348_16(x),
        l348_17(x),
        l348_18(x),
        l348_19(x),
        l348_20(x),
        l348_21(x),
        l348_22(x),
        l348_23(x),
        l348_24(x),
        l348_25(x),
        l348_26(x),
        l348_27(x),
        l348_28(x),
        l348_29(x),
        l348_30(x),
        l348_31(x),
        l348_32(x),
        l348_33(x),
        l348_34(x),
        l348_35(x),
        l348_36(x),
        l348_37(x),
        l348_38(x),
        l348_39(x),
        l348_40(x),
        l348_41(x),
        l348_42(x),
        l348_43(x),
        l348_44(x),
        l348_45(x),
        l348_46(x),
        l348_47(x),
        l348_48(x),
        l348_49(x),
        l348_50(x),
        l348_51(x),
        l348_52(x),
        l348_53(x),
        l348_54(x),
        l348_55(x),
        l348_56(x),
        l348_57(x),
        l348_58(x),
        l348_59(x),
        l348_60(x),
        l348_61(x),
        l348_62(x),
        l348_63(x),
        l348_64(x),
        l348_65(x),
        l348_66(x),
        l348_67(x),
        l348_68(x),
        l348_69(x),
        l348_70(x),
        l348_71(x),
        l348_72(x),
        l348_73(x),
        l348_74(x),
        l348_75(x),
        l348_76(x),
        l348_77(x),
        l348_78(x),
        l348_79(x),
        l348_80(x),
        l348_81(x),
        l348_82(x),
        l348_83(x),
        l348_84(x),
        l348_85(x),
        l348_86(x),
        l348_87(x),
        l348_88(x),
        l348_89(x),
        l348_90(x),
        l348_91(x),
        l348_92(x),
        l348_93(x),
        l348_94(x),
        l348_95(x),
        l348_96(x),
        l348_97(x),
        l348_98(x),
        l348_99(x),
        l348_100(x),
        l348_101(x),
        l348_102(x),
        l348_103(x),
        l348_104(x),
        l348_105(x),
        l348_106(x),
        l348_107(x),
        l348_108(x),
        l348_109(x),
        l348_110(x),
        l348_111(x),
        l348_112(x),
        l348_113(x),
        l348_114(x),
        l348_115(x),
        l348_116(x),
        l348_117(x),
        l348_118(x),
        l348_119(x),
        l348_120(x),
        l348_121(x),
        l348_122(x),
        l348_123(x),
        l348_124(x),
        l348_125(x),
        l348_126(x),
        l348_127(x),
        l348_128(x),
        l348_129(x),
        l348_130(x),
        l348_131(x),
        l348_132(x),
        l348_133(x),
        l348_134(x),
        l348_135(x),
        l348_136(x),
        l348_137(x),
        l348_138(x),
        l348_139(x),
        l348_140(x),
        l348_141(x),
        l348_142(x),
        l348_143(x),
        l348_144(x),
        l348_145(x),
        l348_146(x),
        l348_147(x),
        l348_148(x),
        l348_149(x),
        l348_150(x),
        l348_151(x),
        l348_152(x),
        l348_153(x),
        l348_154(x),
        l348_155(x),
        l348_156(x),
        l348_157(x),
        l348_158(x),
        l348_159(x),
        l348_160(x),
        l348_161(x),
        l348_162(x),
        l348_163(x),
        l348_164(x),
        l348_165(x),
        l348_166(x),
        l348_167(x),
        l348_168(x),
        l348_169(x),
        l348_170(x),
        l348_171(x),
        l348_172(x),
        l348_173(x),
        l348_174(x),
        l348_175(x),
        l348_176(x),
        l348_177(x),
        l348_178(x),
        l348_179(x),
        l348_180(x),
        l348_181(x),
        l348_182(x),
        l348_183(x),
        l348_184(x),
        l348_185(x),
        l348_186(x),
        l348_187(x),
        l348_188(x),
        l348_189(x),
        l348_190(x),
        l348_191(x),
        l348_192(x),
        l348_193(x),
        l348_194(x),
        l348_195(x),
        l348_196(x),
        l348_197(x),
        l348_198(x),
        l348_199(x),
        l348_200(x),
        l348_201(x),
        l348_202(x),
        l348_203(x),
        l348_204(x),
        l348_205(x),
        l348_206(x),
        l348_207(x),
        l348_208(x),
        l348_209(x),
        l348_210(x),
        l348_211(x),
        l348_212(x),
        l348_213(x),
        l348_214(x),
        l348_215(x),
        l348_216(x),
        l348_217(x),
        l348_218(x),
        l348_219(x),
        l348_220(x),
        l348_221(x),
        l348_222(x),
        l348_223(x),
        l348_224(x),
        l348_225(x),
        l348_226(x),
        l348_227(x),
        l348_228(x),
        l348_229(x),
        l348_230(x),
        l348_231(x),
        l348_232(x),
        l348_233(x),
        l348_234(x),
        l348_235(x),
        l348_236(x),
        l348_237(x),
        l348_238(x),
        l348_239(x),
        l348_240(x),
        l348_241(x),
        l348_242(x),
        l348_243(x),
        l348_244(x),
        l348_245(x),
        l348_246(x),
        l348_247(x),
        l348_248(x),
        l348_249(x),
        l348_250(x),
        l348_251(x),
        l348_252(x),
        l348_253(x),
        l348_254(x),
        l348_255(x),
        l348_256(x),
        l348_257(x),
        l348_258(x),
        l348_259(x),
        l348_260(x),
        l348_261(x),
        l348_262(x),
        l348_263(x),
        l348_264(x),
        l348_265(x),
        l348_266(x),
        l348_267(x),
        l348_268(x),
        l348_269(x),
        l348_270(x),
        l348_271(x),
        l348_272(x),
        l348_273(x),
        l348_274(x),
        l348_275(x),
        l348_276(x),
        l348_277(x),
        l348_278(x),
        l348_279(x),
        l348_280(x),
        l348_281(x),
        l348_282(x),
        l348_283(x),
        l348_284(x),
        l348_285(x),
        l348_286(x),
        l348_287(x),
        l348_288(x),
        l348_289(x),
        l348_290(x),
        l348_291(x),
        l348_292(x),
        l348_293(x),
        l348_294(x),
        l348_295(x),
        l348_296(x),
        l348_297(x),
        l348_298(x),
        l348_299(x),
        l348_300(x),
        l348_301(x),
        l348_302(x),
        l348_303(x),
        l348_304(x),
        l348_305(x),
        l348_306(x),
        l348_307(x),
        l348_308(x),
        l348_309(x),
        l348_310(x),
        l348_311(x),
        l348_312(x),
        l348_313(x),
        l348_314(x),
        l348_315(x),
        l348_316(x),
        l348_317(x),
        l348_318(x),
    ]