import numpy as np




# Generated from reverse engineering
def l204_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 296
    out = np.empty(296, dtype=np.float32)
    
    # for i in range(0, 128):
    for i in range(0, 128):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffffffff (len=32)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(128, 160):
    for i in range(0, 32):
        s = -1 * x[128 + i] + -1 * x[160 + i]
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 224):
    for i in range(0, 64):
        s = x[192 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xf (len=4)
    biases = [1.0, 1.0, 1.0, 1.0]
    # for i in range(224, 228):
    for i in range(0, 4):
        s = -1 * x[256 + i]
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(228, 232):
    for i in range(0, 4):
        s = x[260 + i] + -128.0 * x[i + 264] + 128.0 * x[i + 268]
        out[228 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(232, 296):
    for i in range(0, 64):
        s = x[272 + i]
        out[232 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l204_0(x):
    # x is a list (or vector) of length 336
    return max(0, x[0])
def l204_1(x):
    # x is a list (or vector) of length 336
    return max(0, x[1])
def l204_2(x):
    # x is a list (or vector) of length 336
    return max(0, x[2])
def l204_3(x):
    # x is a list (or vector) of length 336
    return max(0, x[3])
def l204_4(x):
    # x is a list (or vector) of length 336
    return max(0, x[4])
def l204_5(x):
    # x is a list (or vector) of length 336
    return max(0, x[5])
def l204_6(x):
    # x is a list (or vector) of length 336
    return max(0, x[6])
def l204_7(x):
    # x is a list (or vector) of length 336
    return max(0, x[7])
def l204_8(x):
    # x is a list (or vector) of length 336
    return max(0, x[8])
def l204_9(x):
    # x is a list (or vector) of length 336
    return max(0, x[9])
def l204_10(x):
    # x is a list (or vector) of length 336
    return max(0, x[10])
def l204_11(x):
    # x is a list (or vector) of length 336
    return max(0, x[11])
def l204_12(x):
    # x is a list (or vector) of length 336
    return max(0, x[12])
def l204_13(x):
    # x is a list (or vector) of length 336
    return max(0, x[13])
def l204_14(x):
    # x is a list (or vector) of length 336
    return max(0, x[14])
def l204_15(x):
    # x is a list (or vector) of length 336
    return max(0, x[15])
def l204_16(x):
    # x is a list (or vector) of length 336
    return max(0, x[16])
def l204_17(x):
    # x is a list (or vector) of length 336
    return max(0, x[17])
def l204_18(x):
    # x is a list (or vector) of length 336
    return max(0, x[18])
def l204_19(x):
    # x is a list (or vector) of length 336
    return max(0, x[19])
def l204_20(x):
    # x is a list (or vector) of length 336
    return max(0, x[20])
def l204_21(x):
    # x is a list (or vector) of length 336
    return max(0, x[21])
def l204_22(x):
    # x is a list (or vector) of length 336
    return max(0, x[22])
def l204_23(x):
    # x is a list (or vector) of length 336
    return max(0, x[23])
def l204_24(x):
    # x is a list (or vector) of length 336
    return max(0, x[24])
def l204_25(x):
    # x is a list (or vector) of length 336
    return max(0, x[25])
def l204_26(x):
    # x is a list (or vector) of length 336
    return max(0, x[26])
def l204_27(x):
    # x is a list (or vector) of length 336
    return max(0, x[27])
def l204_28(x):
    # x is a list (or vector) of length 336
    return max(0, x[28])
def l204_29(x):
    # x is a list (or vector) of length 336
    return max(0, x[29])
def l204_30(x):
    # x is a list (or vector) of length 336
    return max(0, x[30])
def l204_31(x):
    # x is a list (or vector) of length 336
    return max(0, x[31])
def l204_32(x):
    # x is a list (or vector) of length 336
    return max(0, x[32])
def l204_33(x):
    # x is a list (or vector) of length 336
    return max(0, x[33])
def l204_34(x):
    # x is a list (or vector) of length 336
    return max(0, x[34])
def l204_35(x):
    # x is a list (or vector) of length 336
    return max(0, x[35])
def l204_36(x):
    # x is a list (or vector) of length 336
    return max(0, x[36])
def l204_37(x):
    # x is a list (or vector) of length 336
    return max(0, x[37])
def l204_38(x):
    # x is a list (or vector) of length 336
    return max(0, x[38])
def l204_39(x):
    # x is a list (or vector) of length 336
    return max(0, x[39])
def l204_40(x):
    # x is a list (or vector) of length 336
    return max(0, x[40])
def l204_41(x):
    # x is a list (or vector) of length 336
    return max(0, x[41])
def l204_42(x):
    # x is a list (or vector) of length 336
    return max(0, x[42])
def l204_43(x):
    # x is a list (or vector) of length 336
    return max(0, x[43])
def l204_44(x):
    # x is a list (or vector) of length 336
    return max(0, x[44])
def l204_45(x):
    # x is a list (or vector) of length 336
    return max(0, x[45])
def l204_46(x):
    # x is a list (or vector) of length 336
    return max(0, x[46])
def l204_47(x):
    # x is a list (or vector) of length 336
    return max(0, x[47])
def l204_48(x):
    # x is a list (or vector) of length 336
    return max(0, x[48])
def l204_49(x):
    # x is a list (or vector) of length 336
    return max(0, x[49])
def l204_50(x):
    # x is a list (or vector) of length 336
    return max(0, x[50])
def l204_51(x):
    # x is a list (or vector) of length 336
    return max(0, x[51])
def l204_52(x):
    # x is a list (or vector) of length 336
    return max(0, x[52])
def l204_53(x):
    # x is a list (or vector) of length 336
    return max(0, x[53])
def l204_54(x):
    # x is a list (or vector) of length 336
    return max(0, x[54])
def l204_55(x):
    # x is a list (or vector) of length 336
    return max(0, x[55])
def l204_56(x):
    # x is a list (or vector) of length 336
    return max(0, x[56])
def l204_57(x):
    # x is a list (or vector) of length 336
    return max(0, x[57])
def l204_58(x):
    # x is a list (or vector) of length 336
    return max(0, x[58])
def l204_59(x):
    # x is a list (or vector) of length 336
    return max(0, x[59])
def l204_60(x):
    # x is a list (or vector) of length 336
    return max(0, x[60])
def l204_61(x):
    # x is a list (or vector) of length 336
    return max(0, x[61])
def l204_62(x):
    # x is a list (or vector) of length 336
    return max(0, x[62])
def l204_63(x):
    # x is a list (or vector) of length 336
    return max(0, x[63])
def l204_64(x):
    # x is a list (or vector) of length 336
    return max(0, x[64])
def l204_65(x):
    # x is a list (or vector) of length 336
    return max(0, x[65])
def l204_66(x):
    # x is a list (or vector) of length 336
    return max(0, x[66])
def l204_67(x):
    # x is a list (or vector) of length 336
    return max(0, x[67])
def l204_68(x):
    # x is a list (or vector) of length 336
    return max(0, x[68])
def l204_69(x):
    # x is a list (or vector) of length 336
    return max(0, x[69])
def l204_70(x):
    # x is a list (or vector) of length 336
    return max(0, x[70])
def l204_71(x):
    # x is a list (or vector) of length 336
    return max(0, x[71])
def l204_72(x):
    # x is a list (or vector) of length 336
    return max(0, x[72])
def l204_73(x):
    # x is a list (or vector) of length 336
    return max(0, x[73])
def l204_74(x):
    # x is a list (or vector) of length 336
    return max(0, x[74])
def l204_75(x):
    # x is a list (or vector) of length 336
    return max(0, x[75])
def l204_76(x):
    # x is a list (or vector) of length 336
    return max(0, x[76])
def l204_77(x):
    # x is a list (or vector) of length 336
    return max(0, x[77])
def l204_78(x):
    # x is a list (or vector) of length 336
    return max(0, x[78])
def l204_79(x):
    # x is a list (or vector) of length 336
    return max(0, x[79])
def l204_80(x):
    # x is a list (or vector) of length 336
    return max(0, x[80])
def l204_81(x):
    # x is a list (or vector) of length 336
    return max(0, x[81])
def l204_82(x):
    # x is a list (or vector) of length 336
    return max(0, x[82])
def l204_83(x):
    # x is a list (or vector) of length 336
    return max(0, x[83])
def l204_84(x):
    # x is a list (or vector) of length 336
    return max(0, x[84])
def l204_85(x):
    # x is a list (or vector) of length 336
    return max(0, x[85])
def l204_86(x):
    # x is a list (or vector) of length 336
    return max(0, x[86])
def l204_87(x):
    # x is a list (or vector) of length 336
    return max(0, x[87])
def l204_88(x):
    # x is a list (or vector) of length 336
    return max(0, x[88])
def l204_89(x):
    # x is a list (or vector) of length 336
    return max(0, x[89])
def l204_90(x):
    # x is a list (or vector) of length 336
    return max(0, x[90])
def l204_91(x):
    # x is a list (or vector) of length 336
    return max(0, x[91])
def l204_92(x):
    # x is a list (or vector) of length 336
    return max(0, x[92])
def l204_93(x):
    # x is a list (or vector) of length 336
    return max(0, x[93])
def l204_94(x):
    # x is a list (or vector) of length 336
    return max(0, x[94])
def l204_95(x):
    # x is a list (or vector) of length 336
    return max(0, x[95])
def l204_96(x):
    # x is a list (or vector) of length 336
    return max(0, x[96])
def l204_97(x):
    # x is a list (or vector) of length 336
    return max(0, x[97])
def l204_98(x):
    # x is a list (or vector) of length 336
    return max(0, x[98])
def l204_99(x):
    # x is a list (or vector) of length 336
    return max(0, x[99])
def l204_100(x):
    # x is a list (or vector) of length 336
    return max(0, x[100])
def l204_101(x):
    # x is a list (or vector) of length 336
    return max(0, x[101])
def l204_102(x):
    # x is a list (or vector) of length 336
    return max(0, x[102])
def l204_103(x):
    # x is a list (or vector) of length 336
    return max(0, x[103])
def l204_104(x):
    # x is a list (or vector) of length 336
    return max(0, x[104])
def l204_105(x):
    # x is a list (or vector) of length 336
    return max(0, x[105])
def l204_106(x):
    # x is a list (or vector) of length 336
    return max(0, x[106])
def l204_107(x):
    # x is a list (or vector) of length 336
    return max(0, x[107])
def l204_108(x):
    # x is a list (or vector) of length 336
    return max(0, x[108])
def l204_109(x):
    # x is a list (or vector) of length 336
    return max(0, x[109])
def l204_110(x):
    # x is a list (or vector) of length 336
    return max(0, x[110])
def l204_111(x):
    # x is a list (or vector) of length 336
    return max(0, x[111])
def l204_112(x):
    # x is a list (or vector) of length 336
    return max(0, x[112])
def l204_113(x):
    # x is a list (or vector) of length 336
    return max(0, x[113])
def l204_114(x):
    # x is a list (or vector) of length 336
    return max(0, x[114])
def l204_115(x):
    # x is a list (or vector) of length 336
    return max(0, x[115])
def l204_116(x):
    # x is a list (or vector) of length 336
    return max(0, x[116])
def l204_117(x):
    # x is a list (or vector) of length 336
    return max(0, x[117])
def l204_118(x):
    # x is a list (or vector) of length 336
    return max(0, x[118])
def l204_119(x):
    # x is a list (or vector) of length 336
    return max(0, x[119])
def l204_120(x):
    # x is a list (or vector) of length 336
    return max(0, x[120])
def l204_121(x):
    # x is a list (or vector) of length 336
    return max(0, x[121])
def l204_122(x):
    # x is a list (or vector) of length 336
    return max(0, x[122])
def l204_123(x):
    # x is a list (or vector) of length 336
    return max(0, x[123])
def l204_124(x):
    # x is a list (or vector) of length 336
    return max(0, x[124])
def l204_125(x):
    # x is a list (or vector) of length 336
    return max(0, x[125])
def l204_126(x):
    # x is a list (or vector) of length 336
    return max(0, x[126])
def l204_127(x):
    # x is a list (or vector) of length 336
    return max(0, x[127])
def l204_128(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[128] + -1.0*x[160] + 1.0)
def l204_129(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[129] + -1.0*x[161] + 1.0)
def l204_130(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[130] + -1.0*x[162] + 1.0)
def l204_131(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[131] + -1.0*x[163] + 1.0)
def l204_132(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[132] + -1.0*x[164] + 1.0)
def l204_133(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[133] + -1.0*x[165] + 1.0)
def l204_134(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[134] + -1.0*x[166] + 1.0)
def l204_135(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[135] + -1.0*x[167] + 1.0)
def l204_136(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[136] + -1.0*x[168] + 1.0)
def l204_137(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[137] + -1.0*x[169] + 1.0)
def l204_138(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[138] + -1.0*x[170] + 1.0)
def l204_139(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[139] + -1.0*x[171] + 1.0)
def l204_140(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[140] + -1.0*x[172] + 1.0)
def l204_141(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[141] + -1.0*x[173] + 1.0)
def l204_142(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[142] + -1.0*x[174] + 1.0)
def l204_143(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[143] + -1.0*x[175] + 1.0)
def l204_144(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[144] + -1.0*x[176] + 1.0)
def l204_145(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[145] + -1.0*x[177] + 1.0)
def l204_146(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[146] + -1.0*x[178] + 1.0)
def l204_147(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[147] + -1.0*x[179] + 1.0)
def l204_148(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[148] + -1.0*x[180] + 1.0)
def l204_149(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[149] + -1.0*x[181] + 1.0)
def l204_150(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[150] + -1.0*x[182] + 1.0)
def l204_151(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[151] + -1.0*x[183] + 1.0)
def l204_152(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[152] + -1.0*x[184] + 1.0)
def l204_153(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[153] + -1.0*x[185] + 1.0)
def l204_154(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[154] + -1.0*x[186] + 1.0)
def l204_155(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[155] + -1.0*x[187] + 1.0)
def l204_156(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[156] + -1.0*x[188] + 1.0)
def l204_157(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[157] + -1.0*x[189] + 1.0)
def l204_158(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[158] + -1.0*x[190] + 1.0)
def l204_159(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[159] + -1.0*x[191] + 1.0)
def l204_160(x):
    # x is a list (or vector) of length 336
    return max(0, x[192])
def l204_161(x):
    # x is a list (or vector) of length 336
    return max(0, x[193])
def l204_162(x):
    # x is a list (or vector) of length 336
    return max(0, x[194])
def l204_163(x):
    # x is a list (or vector) of length 336
    return max(0, x[195])
def l204_164(x):
    # x is a list (or vector) of length 336
    return max(0, x[196])
def l204_165(x):
    # x is a list (or vector) of length 336
    return max(0, x[197])
def l204_166(x):
    # x is a list (or vector) of length 336
    return max(0, x[198])
def l204_167(x):
    # x is a list (or vector) of length 336
    return max(0, x[199])
def l204_168(x):
    # x is a list (or vector) of length 336
    return max(0, x[200])
def l204_169(x):
    # x is a list (or vector) of length 336
    return max(0, x[201])
def l204_170(x):
    # x is a list (or vector) of length 336
    return max(0, x[202])
def l204_171(x):
    # x is a list (or vector) of length 336
    return max(0, x[203])
def l204_172(x):
    # x is a list (or vector) of length 336
    return max(0, x[204])
def l204_173(x):
    # x is a list (or vector) of length 336
    return max(0, x[205])
def l204_174(x):
    # x is a list (or vector) of length 336
    return max(0, x[206])
def l204_175(x):
    # x is a list (or vector) of length 336
    return max(0, x[207])
def l204_176(x):
    # x is a list (or vector) of length 336
    return max(0, x[208])
def l204_177(x):
    # x is a list (or vector) of length 336
    return max(0, x[209])
def l204_178(x):
    # x is a list (or vector) of length 336
    return max(0, x[210])
def l204_179(x):
    # x is a list (or vector) of length 336
    return max(0, x[211])
def l204_180(x):
    # x is a list (or vector) of length 336
    return max(0, x[212])
def l204_181(x):
    # x is a list (or vector) of length 336
    return max(0, x[213])
def l204_182(x):
    # x is a list (or vector) of length 336
    return max(0, x[214])
def l204_183(x):
    # x is a list (or vector) of length 336
    return max(0, x[215])
def l204_184(x):
    # x is a list (or vector) of length 336
    return max(0, x[216])
def l204_185(x):
    # x is a list (or vector) of length 336
    return max(0, x[217])
def l204_186(x):
    # x is a list (or vector) of length 336
    return max(0, x[218])
def l204_187(x):
    # x is a list (or vector) of length 336
    return max(0, x[219])
def l204_188(x):
    # x is a list (or vector) of length 336
    return max(0, x[220])
def l204_189(x):
    # x is a list (or vector) of length 336
    return max(0, x[221])
def l204_190(x):
    # x is a list (or vector) of length 336
    return max(0, x[222])
def l204_191(x):
    # x is a list (or vector) of length 336
    return max(0, x[223])
def l204_192(x):
    # x is a list (or vector) of length 336
    return max(0, x[224])
def l204_193(x):
    # x is a list (or vector) of length 336
    return max(0, x[225])
def l204_194(x):
    # x is a list (or vector) of length 336
    return max(0, x[226])
def l204_195(x):
    # x is a list (or vector) of length 336
    return max(0, x[227])
def l204_196(x):
    # x is a list (or vector) of length 336
    return max(0, x[228])
def l204_197(x):
    # x is a list (or vector) of length 336
    return max(0, x[229])
def l204_198(x):
    # x is a list (or vector) of length 336
    return max(0, x[230])
def l204_199(x):
    # x is a list (or vector) of length 336
    return max(0, x[231])
def l204_200(x):
    # x is a list (or vector) of length 336
    return max(0, x[232])
def l204_201(x):
    # x is a list (or vector) of length 336
    return max(0, x[233])
def l204_202(x):
    # x is a list (or vector) of length 336
    return max(0, x[234])
def l204_203(x):
    # x is a list (or vector) of length 336
    return max(0, x[235])
def l204_204(x):
    # x is a list (or vector) of length 336
    return max(0, x[236])
def l204_205(x):
    # x is a list (or vector) of length 336
    return max(0, x[237])
def l204_206(x):
    # x is a list (or vector) of length 336
    return max(0, x[238])
def l204_207(x):
    # x is a list (or vector) of length 336
    return max(0, x[239])
def l204_208(x):
    # x is a list (or vector) of length 336
    return max(0, x[240])
def l204_209(x):
    # x is a list (or vector) of length 336
    return max(0, x[241])
def l204_210(x):
    # x is a list (or vector) of length 336
    return max(0, x[242])
def l204_211(x):
    # x is a list (or vector) of length 336
    return max(0, x[243])
def l204_212(x):
    # x is a list (or vector) of length 336
    return max(0, x[244])
def l204_213(x):
    # x is a list (or vector) of length 336
    return max(0, x[245])
def l204_214(x):
    # x is a list (or vector) of length 336
    return max(0, x[246])
def l204_215(x):
    # x is a list (or vector) of length 336
    return max(0, x[247])
def l204_216(x):
    # x is a list (or vector) of length 336
    return max(0, x[248])
def l204_217(x):
    # x is a list (or vector) of length 336
    return max(0, x[249])
def l204_218(x):
    # x is a list (or vector) of length 336
    return max(0, x[250])
def l204_219(x):
    # x is a list (or vector) of length 336
    return max(0, x[251])
def l204_220(x):
    # x is a list (or vector) of length 336
    return max(0, x[252])
def l204_221(x):
    # x is a list (or vector) of length 336
    return max(0, x[253])
def l204_222(x):
    # x is a list (or vector) of length 336
    return max(0, x[254])
def l204_223(x):
    # x is a list (or vector) of length 336
    return max(0, x[255])
def l204_224(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[256] + 1.0)
def l204_225(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[257] + 1.0)
def l204_226(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[258] + 1.0)
def l204_227(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[259] + 1.0)
def l204_228(x):
    # x is a list (or vector) of length 336
    return max(0, x[260] + -128.0*x[264] + 128.0*x[268])
def l204_229(x):
    # x is a list (or vector) of length 336
    return max(0, x[261] + -128.0*x[265] + 128.0*x[269])
def l204_230(x):
    # x is a list (or vector) of length 336
    return max(0, x[262] + -128.0*x[266] + 128.0*x[270])
def l204_231(x):
    # x is a list (or vector) of length 336
    return max(0, x[263] + -128.0*x[267] + 128.0*x[271])
def l204_232(x):
    # x is a list (or vector) of length 336
    return max(0, x[272])
def l204_233(x):
    # x is a list (or vector) of length 336
    return max(0, x[273])
def l204_234(x):
    # x is a list (or vector) of length 336
    return max(0, x[274])
def l204_235(x):
    # x is a list (or vector) of length 336
    return max(0, x[275])
def l204_236(x):
    # x is a list (or vector) of length 336
    return max(0, x[276])
def l204_237(x):
    # x is a list (or vector) of length 336
    return max(0, x[277])
def l204_238(x):
    # x is a list (or vector) of length 336
    return max(0, x[278])
def l204_239(x):
    # x is a list (or vector) of length 336
    return max(0, x[279])
def l204_240(x):
    # x is a list (or vector) of length 336
    return max(0, x[280])
def l204_241(x):
    # x is a list (or vector) of length 336
    return max(0, x[281])
def l204_242(x):
    # x is a list (or vector) of length 336
    return max(0, x[282])
def l204_243(x):
    # x is a list (or vector) of length 336
    return max(0, x[283])
def l204_244(x):
    # x is a list (or vector) of length 336
    return max(0, x[284])
def l204_245(x):
    # x is a list (or vector) of length 336
    return max(0, x[285])
def l204_246(x):
    # x is a list (or vector) of length 336
    return max(0, x[286])
def l204_247(x):
    # x is a list (or vector) of length 336
    return max(0, x[287])
def l204_248(x):
    # x is a list (or vector) of length 336
    return max(0, x[288])
def l204_249(x):
    # x is a list (or vector) of length 336
    return max(0, x[289])
def l204_250(x):
    # x is a list (or vector) of length 336
    return max(0, x[290])
def l204_251(x):
    # x is a list (or vector) of length 336
    return max(0, x[291])
def l204_252(x):
    # x is a list (or vector) of length 336
    return max(0, x[292])
def l204_253(x):
    # x is a list (or vector) of length 336
    return max(0, x[293])
def l204_254(x):
    # x is a list (or vector) of length 336
    return max(0, x[294])
def l204_255(x):
    # x is a list (or vector) of length 336
    return max(0, x[295])
def l204_256(x):
    # x is a list (or vector) of length 336
    return max(0, x[296])
def l204_257(x):
    # x is a list (or vector) of length 336
    return max(0, x[297])
def l204_258(x):
    # x is a list (or vector) of length 336
    return max(0, x[298])
def l204_259(x):
    # x is a list (or vector) of length 336
    return max(0, x[299])
def l204_260(x):
    # x is a list (or vector) of length 336
    return max(0, x[300])
def l204_261(x):
    # x is a list (or vector) of length 336
    return max(0, x[301])
def l204_262(x):
    # x is a list (or vector) of length 336
    return max(0, x[302])
def l204_263(x):
    # x is a list (or vector) of length 336
    return max(0, x[303])
def l204_264(x):
    # x is a list (or vector) of length 336
    return max(0, x[304])
def l204_265(x):
    # x is a list (or vector) of length 336
    return max(0, x[305])
def l204_266(x):
    # x is a list (or vector) of length 336
    return max(0, x[306])
def l204_267(x):
    # x is a list (or vector) of length 336
    return max(0, x[307])
def l204_268(x):
    # x is a list (or vector) of length 336
    return max(0, x[308])
def l204_269(x):
    # x is a list (or vector) of length 336
    return max(0, x[309])
def l204_270(x):
    # x is a list (or vector) of length 336
    return max(0, x[310])
def l204_271(x):
    # x is a list (or vector) of length 336
    return max(0, x[311])
def l204_272(x):
    # x is a list (or vector) of length 336
    return max(0, x[312])
def l204_273(x):
    # x is a list (or vector) of length 336
    return max(0, x[313])
def l204_274(x):
    # x is a list (or vector) of length 336
    return max(0, x[314])
def l204_275(x):
    # x is a list (or vector) of length 336
    return max(0, x[315])
def l204_276(x):
    # x is a list (or vector) of length 336
    return max(0, x[316])
def l204_277(x):
    # x is a list (or vector) of length 336
    return max(0, x[317])
def l204_278(x):
    # x is a list (or vector) of length 336
    return max(0, x[318])
def l204_279(x):
    # x is a list (or vector) of length 336
    return max(0, x[319])
def l204_280(x):
    # x is a list (or vector) of length 336
    return max(0, x[320])
def l204_281(x):
    # x is a list (or vector) of length 336
    return max(0, x[321])
def l204_282(x):
    # x is a list (or vector) of length 336
    return max(0, x[322])
def l204_283(x):
    # x is a list (or vector) of length 336
    return max(0, x[323])
def l204_284(x):
    # x is a list (or vector) of length 336
    return max(0, x[324])
def l204_285(x):
    # x is a list (or vector) of length 336
    return max(0, x[325])
def l204_286(x):
    # x is a list (or vector) of length 336
    return max(0, x[326])
def l204_287(x):
    # x is a list (or vector) of length 336
    return max(0, x[327])
def l204_288(x):
    # x is a list (or vector) of length 336
    return max(0, x[328])
def l204_289(x):
    # x is a list (or vector) of length 336
    return max(0, x[329])
def l204_290(x):
    # x is a list (or vector) of length 336
    return max(0, x[330])
def l204_291(x):
    # x is a list (or vector) of length 336
    return max(0, x[331])
def l204_292(x):
    # x is a list (or vector) of length 336
    return max(0, x[332])
def l204_293(x):
    # x is a list (or vector) of length 336
    return max(0, x[333])
def l204_294(x):
    # x is a list (or vector) of length 336
    return max(0, x[334])
def l204_295(x):
    # x is a list (or vector) of length 336
    return max(0, x[335])
def l204_(x):
    # x is a list (or vector) of length 336
    return [
        l204_0(x),
        l204_1(x),
        l204_2(x),
        l204_3(x),
        l204_4(x),
        l204_5(x),
        l204_6(x),
        l204_7(x),
        l204_8(x),
        l204_9(x),
        l204_10(x),
        l204_11(x),
        l204_12(x),
        l204_13(x),
        l204_14(x),
        l204_15(x),
        l204_16(x),
        l204_17(x),
        l204_18(x),
        l204_19(x),
        l204_20(x),
        l204_21(x),
        l204_22(x),
        l204_23(x),
        l204_24(x),
        l204_25(x),
        l204_26(x),
        l204_27(x),
        l204_28(x),
        l204_29(x),
        l204_30(x),
        l204_31(x),
        l204_32(x),
        l204_33(x),
        l204_34(x),
        l204_35(x),
        l204_36(x),
        l204_37(x),
        l204_38(x),
        l204_39(x),
        l204_40(x),
        l204_41(x),
        l204_42(x),
        l204_43(x),
        l204_44(x),
        l204_45(x),
        l204_46(x),
        l204_47(x),
        l204_48(x),
        l204_49(x),
        l204_50(x),
        l204_51(x),
        l204_52(x),
        l204_53(x),
        l204_54(x),
        l204_55(x),
        l204_56(x),
        l204_57(x),
        l204_58(x),
        l204_59(x),
        l204_60(x),
        l204_61(x),
        l204_62(x),
        l204_63(x),
        l204_64(x),
        l204_65(x),
        l204_66(x),
        l204_67(x),
        l204_68(x),
        l204_69(x),
        l204_70(x),
        l204_71(x),
        l204_72(x),
        l204_73(x),
        l204_74(x),
        l204_75(x),
        l204_76(x),
        l204_77(x),
        l204_78(x),
        l204_79(x),
        l204_80(x),
        l204_81(x),
        l204_82(x),
        l204_83(x),
        l204_84(x),
        l204_85(x),
        l204_86(x),
        l204_87(x),
        l204_88(x),
        l204_89(x),
        l204_90(x),
        l204_91(x),
        l204_92(x),
        l204_93(x),
        l204_94(x),
        l204_95(x),
        l204_96(x),
        l204_97(x),
        l204_98(x),
        l204_99(x),
        l204_100(x),
        l204_101(x),
        l204_102(x),
        l204_103(x),
        l204_104(x),
        l204_105(x),
        l204_106(x),
        l204_107(x),
        l204_108(x),
        l204_109(x),
        l204_110(x),
        l204_111(x),
        l204_112(x),
        l204_113(x),
        l204_114(x),
        l204_115(x),
        l204_116(x),
        l204_117(x),
        l204_118(x),
        l204_119(x),
        l204_120(x),
        l204_121(x),
        l204_122(x),
        l204_123(x),
        l204_124(x),
        l204_125(x),
        l204_126(x),
        l204_127(x),
        l204_128(x),
        l204_129(x),
        l204_130(x),
        l204_131(x),
        l204_132(x),
        l204_133(x),
        l204_134(x),
        l204_135(x),
        l204_136(x),
        l204_137(x),
        l204_138(x),
        l204_139(x),
        l204_140(x),
        l204_141(x),
        l204_142(x),
        l204_143(x),
        l204_144(x),
        l204_145(x),
        l204_146(x),
        l204_147(x),
        l204_148(x),
        l204_149(x),
        l204_150(x),
        l204_151(x),
        l204_152(x),
        l204_153(x),
        l204_154(x),
        l204_155(x),
        l204_156(x),
        l204_157(x),
        l204_158(x),
        l204_159(x),
        l204_160(x),
        l204_161(x),
        l204_162(x),
        l204_163(x),
        l204_164(x),
        l204_165(x),
        l204_166(x),
        l204_167(x),
        l204_168(x),
        l204_169(x),
        l204_170(x),
        l204_171(x),
        l204_172(x),
        l204_173(x),
        l204_174(x),
        l204_175(x),
        l204_176(x),
        l204_177(x),
        l204_178(x),
        l204_179(x),
        l204_180(x),
        l204_181(x),
        l204_182(x),
        l204_183(x),
        l204_184(x),
        l204_185(x),
        l204_186(x),
        l204_187(x),
        l204_188(x),
        l204_189(x),
        l204_190(x),
        l204_191(x),
        l204_192(x),
        l204_193(x),
        l204_194(x),
        l204_195(x),
        l204_196(x),
        l204_197(x),
        l204_198(x),
        l204_199(x),
        l204_200(x),
        l204_201(x),
        l204_202(x),
        l204_203(x),
        l204_204(x),
        l204_205(x),
        l204_206(x),
        l204_207(x),
        l204_208(x),
        l204_209(x),
        l204_210(x),
        l204_211(x),
        l204_212(x),
        l204_213(x),
        l204_214(x),
        l204_215(x),
        l204_216(x),
        l204_217(x),
        l204_218(x),
        l204_219(x),
        l204_220(x),
        l204_221(x),
        l204_222(x),
        l204_223(x),
        l204_224(x),
        l204_225(x),
        l204_226(x),
        l204_227(x),
        l204_228(x),
        l204_229(x),
        l204_230(x),
        l204_231(x),
        l204_232(x),
        l204_233(x),
        l204_234(x),
        l204_235(x),
        l204_236(x),
        l204_237(x),
        l204_238(x),
        l204_239(x),
        l204_240(x),
        l204_241(x),
        l204_242(x),
        l204_243(x),
        l204_244(x),
        l204_245(x),
        l204_246(x),
        l204_247(x),
        l204_248(x),
        l204_249(x),
        l204_250(x),
        l204_251(x),
        l204_252(x),
        l204_253(x),
        l204_254(x),
        l204_255(x),
        l204_256(x),
        l204_257(x),
        l204_258(x),
        l204_259(x),
        l204_260(x),
        l204_261(x),
        l204_262(x),
        l204_263(x),
        l204_264(x),
        l204_265(x),
        l204_266(x),
        l204_267(x),
        l204_268(x),
        l204_269(x),
        l204_270(x),
        l204_271(x),
        l204_272(x),
        l204_273(x),
        l204_274(x),
        l204_275(x),
        l204_276(x),
        l204_277(x),
        l204_278(x),
        l204_279(x),
        l204_280(x),
        l204_281(x),
        l204_282(x),
        l204_283(x),
        l204_284(x),
        l204_285(x),
        l204_286(x),
        l204_287(x),
        l204_288(x),
        l204_289(x),
        l204_290(x),
        l204_291(x),
        l204_292(x),
        l204_293(x),
        l204_294(x),
        l204_295(x),
    ]