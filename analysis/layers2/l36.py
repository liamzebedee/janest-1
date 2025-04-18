import numpy as np




# Generated from reverse engineering
def l36_g(x: np.ndarray) -> np.ndarray:
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




def l36_0(x):
    # x is a list (or vector) of length 336
    return max(0, x[0])
def l36_1(x):
    # x is a list (or vector) of length 336
    return max(0, x[1])
def l36_2(x):
    # x is a list (or vector) of length 336
    return max(0, x[2])
def l36_3(x):
    # x is a list (or vector) of length 336
    return max(0, x[3])
def l36_4(x):
    # x is a list (or vector) of length 336
    return max(0, x[4])
def l36_5(x):
    # x is a list (or vector) of length 336
    return max(0, x[5])
def l36_6(x):
    # x is a list (or vector) of length 336
    return max(0, x[6])
def l36_7(x):
    # x is a list (or vector) of length 336
    return max(0, x[7])
def l36_8(x):
    # x is a list (or vector) of length 336
    return max(0, x[8])
def l36_9(x):
    # x is a list (or vector) of length 336
    return max(0, x[9])
def l36_10(x):
    # x is a list (or vector) of length 336
    return max(0, x[10])
def l36_11(x):
    # x is a list (or vector) of length 336
    return max(0, x[11])
def l36_12(x):
    # x is a list (or vector) of length 336
    return max(0, x[12])
def l36_13(x):
    # x is a list (or vector) of length 336
    return max(0, x[13])
def l36_14(x):
    # x is a list (or vector) of length 336
    return max(0, x[14])
def l36_15(x):
    # x is a list (or vector) of length 336
    return max(0, x[15])
def l36_16(x):
    # x is a list (or vector) of length 336
    return max(0, x[16])
def l36_17(x):
    # x is a list (or vector) of length 336
    return max(0, x[17])
def l36_18(x):
    # x is a list (or vector) of length 336
    return max(0, x[18])
def l36_19(x):
    # x is a list (or vector) of length 336
    return max(0, x[19])
def l36_20(x):
    # x is a list (or vector) of length 336
    return max(0, x[20])
def l36_21(x):
    # x is a list (or vector) of length 336
    return max(0, x[21])
def l36_22(x):
    # x is a list (or vector) of length 336
    return max(0, x[22])
def l36_23(x):
    # x is a list (or vector) of length 336
    return max(0, x[23])
def l36_24(x):
    # x is a list (or vector) of length 336
    return max(0, x[24])
def l36_25(x):
    # x is a list (or vector) of length 336
    return max(0, x[25])
def l36_26(x):
    # x is a list (or vector) of length 336
    return max(0, x[26])
def l36_27(x):
    # x is a list (or vector) of length 336
    return max(0, x[27])
def l36_28(x):
    # x is a list (or vector) of length 336
    return max(0, x[28])
def l36_29(x):
    # x is a list (or vector) of length 336
    return max(0, x[29])
def l36_30(x):
    # x is a list (or vector) of length 336
    return max(0, x[30])
def l36_31(x):
    # x is a list (or vector) of length 336
    return max(0, x[31])
def l36_32(x):
    # x is a list (or vector) of length 336
    return max(0, x[32])
def l36_33(x):
    # x is a list (or vector) of length 336
    return max(0, x[33])
def l36_34(x):
    # x is a list (or vector) of length 336
    return max(0, x[34])
def l36_35(x):
    # x is a list (or vector) of length 336
    return max(0, x[35])
def l36_36(x):
    # x is a list (or vector) of length 336
    return max(0, x[36])
def l36_37(x):
    # x is a list (or vector) of length 336
    return max(0, x[37])
def l36_38(x):
    # x is a list (or vector) of length 336
    return max(0, x[38])
def l36_39(x):
    # x is a list (or vector) of length 336
    return max(0, x[39])
def l36_40(x):
    # x is a list (or vector) of length 336
    return max(0, x[40])
def l36_41(x):
    # x is a list (or vector) of length 336
    return max(0, x[41])
def l36_42(x):
    # x is a list (or vector) of length 336
    return max(0, x[42])
def l36_43(x):
    # x is a list (or vector) of length 336
    return max(0, x[43])
def l36_44(x):
    # x is a list (or vector) of length 336
    return max(0, x[44])
def l36_45(x):
    # x is a list (or vector) of length 336
    return max(0, x[45])
def l36_46(x):
    # x is a list (or vector) of length 336
    return max(0, x[46])
def l36_47(x):
    # x is a list (or vector) of length 336
    return max(0, x[47])
def l36_48(x):
    # x is a list (or vector) of length 336
    return max(0, x[48])
def l36_49(x):
    # x is a list (or vector) of length 336
    return max(0, x[49])
def l36_50(x):
    # x is a list (or vector) of length 336
    return max(0, x[50])
def l36_51(x):
    # x is a list (or vector) of length 336
    return max(0, x[51])
def l36_52(x):
    # x is a list (or vector) of length 336
    return max(0, x[52])
def l36_53(x):
    # x is a list (or vector) of length 336
    return max(0, x[53])
def l36_54(x):
    # x is a list (or vector) of length 336
    return max(0, x[54])
def l36_55(x):
    # x is a list (or vector) of length 336
    return max(0, x[55])
def l36_56(x):
    # x is a list (or vector) of length 336
    return max(0, x[56])
def l36_57(x):
    # x is a list (or vector) of length 336
    return max(0, x[57])
def l36_58(x):
    # x is a list (or vector) of length 336
    return max(0, x[58])
def l36_59(x):
    # x is a list (or vector) of length 336
    return max(0, x[59])
def l36_60(x):
    # x is a list (or vector) of length 336
    return max(0, x[60])
def l36_61(x):
    # x is a list (or vector) of length 336
    return max(0, x[61])
def l36_62(x):
    # x is a list (or vector) of length 336
    return max(0, x[62])
def l36_63(x):
    # x is a list (or vector) of length 336
    return max(0, x[63])
def l36_64(x):
    # x is a list (or vector) of length 336
    return max(0, x[64])
def l36_65(x):
    # x is a list (or vector) of length 336
    return max(0, x[65])
def l36_66(x):
    # x is a list (or vector) of length 336
    return max(0, x[66])
def l36_67(x):
    # x is a list (or vector) of length 336
    return max(0, x[67])
def l36_68(x):
    # x is a list (or vector) of length 336
    return max(0, x[68])
def l36_69(x):
    # x is a list (or vector) of length 336
    return max(0, x[69])
def l36_70(x):
    # x is a list (or vector) of length 336
    return max(0, x[70])
def l36_71(x):
    # x is a list (or vector) of length 336
    return max(0, x[71])
def l36_72(x):
    # x is a list (or vector) of length 336
    return max(0, x[72])
def l36_73(x):
    # x is a list (or vector) of length 336
    return max(0, x[73])
def l36_74(x):
    # x is a list (or vector) of length 336
    return max(0, x[74])
def l36_75(x):
    # x is a list (or vector) of length 336
    return max(0, x[75])
def l36_76(x):
    # x is a list (or vector) of length 336
    return max(0, x[76])
def l36_77(x):
    # x is a list (or vector) of length 336
    return max(0, x[77])
def l36_78(x):
    # x is a list (or vector) of length 336
    return max(0, x[78])
def l36_79(x):
    # x is a list (or vector) of length 336
    return max(0, x[79])
def l36_80(x):
    # x is a list (or vector) of length 336
    return max(0, x[80])
def l36_81(x):
    # x is a list (or vector) of length 336
    return max(0, x[81])
def l36_82(x):
    # x is a list (or vector) of length 336
    return max(0, x[82])
def l36_83(x):
    # x is a list (or vector) of length 336
    return max(0, x[83])
def l36_84(x):
    # x is a list (or vector) of length 336
    return max(0, x[84])
def l36_85(x):
    # x is a list (or vector) of length 336
    return max(0, x[85])
def l36_86(x):
    # x is a list (or vector) of length 336
    return max(0, x[86])
def l36_87(x):
    # x is a list (or vector) of length 336
    return max(0, x[87])
def l36_88(x):
    # x is a list (or vector) of length 336
    return max(0, x[88])
def l36_89(x):
    # x is a list (or vector) of length 336
    return max(0, x[89])
def l36_90(x):
    # x is a list (or vector) of length 336
    return max(0, x[90])
def l36_91(x):
    # x is a list (or vector) of length 336
    return max(0, x[91])
def l36_92(x):
    # x is a list (or vector) of length 336
    return max(0, x[92])
def l36_93(x):
    # x is a list (or vector) of length 336
    return max(0, x[93])
def l36_94(x):
    # x is a list (or vector) of length 336
    return max(0, x[94])
def l36_95(x):
    # x is a list (or vector) of length 336
    return max(0, x[95])
def l36_96(x):
    # x is a list (or vector) of length 336
    return max(0, x[96])
def l36_97(x):
    # x is a list (or vector) of length 336
    return max(0, x[97])
def l36_98(x):
    # x is a list (or vector) of length 336
    return max(0, x[98])
def l36_99(x):
    # x is a list (or vector) of length 336
    return max(0, x[99])
def l36_100(x):
    # x is a list (or vector) of length 336
    return max(0, x[100])
def l36_101(x):
    # x is a list (or vector) of length 336
    return max(0, x[101])
def l36_102(x):
    # x is a list (or vector) of length 336
    return max(0, x[102])
def l36_103(x):
    # x is a list (or vector) of length 336
    return max(0, x[103])
def l36_104(x):
    # x is a list (or vector) of length 336
    return max(0, x[104])
def l36_105(x):
    # x is a list (or vector) of length 336
    return max(0, x[105])
def l36_106(x):
    # x is a list (or vector) of length 336
    return max(0, x[106])
def l36_107(x):
    # x is a list (or vector) of length 336
    return max(0, x[107])
def l36_108(x):
    # x is a list (or vector) of length 336
    return max(0, x[108])
def l36_109(x):
    # x is a list (or vector) of length 336
    return max(0, x[109])
def l36_110(x):
    # x is a list (or vector) of length 336
    return max(0, x[110])
def l36_111(x):
    # x is a list (or vector) of length 336
    return max(0, x[111])
def l36_112(x):
    # x is a list (or vector) of length 336
    return max(0, x[112])
def l36_113(x):
    # x is a list (or vector) of length 336
    return max(0, x[113])
def l36_114(x):
    # x is a list (or vector) of length 336
    return max(0, x[114])
def l36_115(x):
    # x is a list (or vector) of length 336
    return max(0, x[115])
def l36_116(x):
    # x is a list (or vector) of length 336
    return max(0, x[116])
def l36_117(x):
    # x is a list (or vector) of length 336
    return max(0, x[117])
def l36_118(x):
    # x is a list (or vector) of length 336
    return max(0, x[118])
def l36_119(x):
    # x is a list (or vector) of length 336
    return max(0, x[119])
def l36_120(x):
    # x is a list (or vector) of length 336
    return max(0, x[120])
def l36_121(x):
    # x is a list (or vector) of length 336
    return max(0, x[121])
def l36_122(x):
    # x is a list (or vector) of length 336
    return max(0, x[122])
def l36_123(x):
    # x is a list (or vector) of length 336
    return max(0, x[123])
def l36_124(x):
    # x is a list (or vector) of length 336
    return max(0, x[124])
def l36_125(x):
    # x is a list (or vector) of length 336
    return max(0, x[125])
def l36_126(x):
    # x is a list (or vector) of length 336
    return max(0, x[126])
def l36_127(x):
    # x is a list (or vector) of length 336
    return max(0, x[127])
def l36_128(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[128] + -1.0*x[160] + 1.0)
def l36_129(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[129] + -1.0*x[161] + 1.0)
def l36_130(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[130] + -1.0*x[162] + 1.0)
def l36_131(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[131] + -1.0*x[163] + 1.0)
def l36_132(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[132] + -1.0*x[164] + 1.0)
def l36_133(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[133] + -1.0*x[165] + 1.0)
def l36_134(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[134] + -1.0*x[166] + 1.0)
def l36_135(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[135] + -1.0*x[167] + 1.0)
def l36_136(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[136] + -1.0*x[168] + 1.0)
def l36_137(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[137] + -1.0*x[169] + 1.0)
def l36_138(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[138] + -1.0*x[170] + 1.0)
def l36_139(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[139] + -1.0*x[171] + 1.0)
def l36_140(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[140] + -1.0*x[172] + 1.0)
def l36_141(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[141] + -1.0*x[173] + 1.0)
def l36_142(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[142] + -1.0*x[174] + 1.0)
def l36_143(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[143] + -1.0*x[175] + 1.0)
def l36_144(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[144] + -1.0*x[176] + 1.0)
def l36_145(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[145] + -1.0*x[177] + 1.0)
def l36_146(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[146] + -1.0*x[178] + 1.0)
def l36_147(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[147] + -1.0*x[179] + 1.0)
def l36_148(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[148] + -1.0*x[180] + 1.0)
def l36_149(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[149] + -1.0*x[181] + 1.0)
def l36_150(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[150] + -1.0*x[182] + 1.0)
def l36_151(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[151] + -1.0*x[183] + 1.0)
def l36_152(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[152] + -1.0*x[184] + 1.0)
def l36_153(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[153] + -1.0*x[185] + 1.0)
def l36_154(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[154] + -1.0*x[186] + 1.0)
def l36_155(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[155] + -1.0*x[187] + 1.0)
def l36_156(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[156] + -1.0*x[188] + 1.0)
def l36_157(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[157] + -1.0*x[189] + 1.0)
def l36_158(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[158] + -1.0*x[190] + 1.0)
def l36_159(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[159] + -1.0*x[191] + 1.0)
def l36_160(x):
    # x is a list (or vector) of length 336
    return max(0, x[192])
def l36_161(x):
    # x is a list (or vector) of length 336
    return max(0, x[193])
def l36_162(x):
    # x is a list (or vector) of length 336
    return max(0, x[194])
def l36_163(x):
    # x is a list (or vector) of length 336
    return max(0, x[195])
def l36_164(x):
    # x is a list (or vector) of length 336
    return max(0, x[196])
def l36_165(x):
    # x is a list (or vector) of length 336
    return max(0, x[197])
def l36_166(x):
    # x is a list (or vector) of length 336
    return max(0, x[198])
def l36_167(x):
    # x is a list (or vector) of length 336
    return max(0, x[199])
def l36_168(x):
    # x is a list (or vector) of length 336
    return max(0, x[200])
def l36_169(x):
    # x is a list (or vector) of length 336
    return max(0, x[201])
def l36_170(x):
    # x is a list (or vector) of length 336
    return max(0, x[202])
def l36_171(x):
    # x is a list (or vector) of length 336
    return max(0, x[203])
def l36_172(x):
    # x is a list (or vector) of length 336
    return max(0, x[204])
def l36_173(x):
    # x is a list (or vector) of length 336
    return max(0, x[205])
def l36_174(x):
    # x is a list (or vector) of length 336
    return max(0, x[206])
def l36_175(x):
    # x is a list (or vector) of length 336
    return max(0, x[207])
def l36_176(x):
    # x is a list (or vector) of length 336
    return max(0, x[208])
def l36_177(x):
    # x is a list (or vector) of length 336
    return max(0, x[209])
def l36_178(x):
    # x is a list (or vector) of length 336
    return max(0, x[210])
def l36_179(x):
    # x is a list (or vector) of length 336
    return max(0, x[211])
def l36_180(x):
    # x is a list (or vector) of length 336
    return max(0, x[212])
def l36_181(x):
    # x is a list (or vector) of length 336
    return max(0, x[213])
def l36_182(x):
    # x is a list (or vector) of length 336
    return max(0, x[214])
def l36_183(x):
    # x is a list (or vector) of length 336
    return max(0, x[215])
def l36_184(x):
    # x is a list (or vector) of length 336
    return max(0, x[216])
def l36_185(x):
    # x is a list (or vector) of length 336
    return max(0, x[217])
def l36_186(x):
    # x is a list (or vector) of length 336
    return max(0, x[218])
def l36_187(x):
    # x is a list (or vector) of length 336
    return max(0, x[219])
def l36_188(x):
    # x is a list (or vector) of length 336
    return max(0, x[220])
def l36_189(x):
    # x is a list (or vector) of length 336
    return max(0, x[221])
def l36_190(x):
    # x is a list (or vector) of length 336
    return max(0, x[222])
def l36_191(x):
    # x is a list (or vector) of length 336
    return max(0, x[223])
def l36_192(x):
    # x is a list (or vector) of length 336
    return max(0, x[224])
def l36_193(x):
    # x is a list (or vector) of length 336
    return max(0, x[225])
def l36_194(x):
    # x is a list (or vector) of length 336
    return max(0, x[226])
def l36_195(x):
    # x is a list (or vector) of length 336
    return max(0, x[227])
def l36_196(x):
    # x is a list (or vector) of length 336
    return max(0, x[228])
def l36_197(x):
    # x is a list (or vector) of length 336
    return max(0, x[229])
def l36_198(x):
    # x is a list (or vector) of length 336
    return max(0, x[230])
def l36_199(x):
    # x is a list (or vector) of length 336
    return max(0, x[231])
def l36_200(x):
    # x is a list (or vector) of length 336
    return max(0, x[232])
def l36_201(x):
    # x is a list (or vector) of length 336
    return max(0, x[233])
def l36_202(x):
    # x is a list (or vector) of length 336
    return max(0, x[234])
def l36_203(x):
    # x is a list (or vector) of length 336
    return max(0, x[235])
def l36_204(x):
    # x is a list (or vector) of length 336
    return max(0, x[236])
def l36_205(x):
    # x is a list (or vector) of length 336
    return max(0, x[237])
def l36_206(x):
    # x is a list (or vector) of length 336
    return max(0, x[238])
def l36_207(x):
    # x is a list (or vector) of length 336
    return max(0, x[239])
def l36_208(x):
    # x is a list (or vector) of length 336
    return max(0, x[240])
def l36_209(x):
    # x is a list (or vector) of length 336
    return max(0, x[241])
def l36_210(x):
    # x is a list (or vector) of length 336
    return max(0, x[242])
def l36_211(x):
    # x is a list (or vector) of length 336
    return max(0, x[243])
def l36_212(x):
    # x is a list (or vector) of length 336
    return max(0, x[244])
def l36_213(x):
    # x is a list (or vector) of length 336
    return max(0, x[245])
def l36_214(x):
    # x is a list (or vector) of length 336
    return max(0, x[246])
def l36_215(x):
    # x is a list (or vector) of length 336
    return max(0, x[247])
def l36_216(x):
    # x is a list (or vector) of length 336
    return max(0, x[248])
def l36_217(x):
    # x is a list (or vector) of length 336
    return max(0, x[249])
def l36_218(x):
    # x is a list (or vector) of length 336
    return max(0, x[250])
def l36_219(x):
    # x is a list (or vector) of length 336
    return max(0, x[251])
def l36_220(x):
    # x is a list (or vector) of length 336
    return max(0, x[252])
def l36_221(x):
    # x is a list (or vector) of length 336
    return max(0, x[253])
def l36_222(x):
    # x is a list (or vector) of length 336
    return max(0, x[254])
def l36_223(x):
    # x is a list (or vector) of length 336
    return max(0, x[255])
def l36_224(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[256] + 1.0)
def l36_225(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[257] + 1.0)
def l36_226(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[258] + 1.0)
def l36_227(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[259] + 1.0)
def l36_228(x):
    # x is a list (or vector) of length 336
    return max(0, x[260] + -128.0*x[264] + 128.0*x[268])
def l36_229(x):
    # x is a list (or vector) of length 336
    return max(0, x[261] + -128.0*x[265] + 128.0*x[269])
def l36_230(x):
    # x is a list (or vector) of length 336
    return max(0, x[262] + -128.0*x[266] + 128.0*x[270])
def l36_231(x):
    # x is a list (or vector) of length 336
    return max(0, x[263] + -128.0*x[267] + 128.0*x[271])
def l36_232(x):
    # x is a list (or vector) of length 336
    return max(0, x[272])
def l36_233(x):
    # x is a list (or vector) of length 336
    return max(0, x[273])
def l36_234(x):
    # x is a list (or vector) of length 336
    return max(0, x[274])
def l36_235(x):
    # x is a list (or vector) of length 336
    return max(0, x[275])
def l36_236(x):
    # x is a list (or vector) of length 336
    return max(0, x[276])
def l36_237(x):
    # x is a list (or vector) of length 336
    return max(0, x[277])
def l36_238(x):
    # x is a list (or vector) of length 336
    return max(0, x[278])
def l36_239(x):
    # x is a list (or vector) of length 336
    return max(0, x[279])
def l36_240(x):
    # x is a list (or vector) of length 336
    return max(0, x[280])
def l36_241(x):
    # x is a list (or vector) of length 336
    return max(0, x[281])
def l36_242(x):
    # x is a list (or vector) of length 336
    return max(0, x[282])
def l36_243(x):
    # x is a list (or vector) of length 336
    return max(0, x[283])
def l36_244(x):
    # x is a list (or vector) of length 336
    return max(0, x[284])
def l36_245(x):
    # x is a list (or vector) of length 336
    return max(0, x[285])
def l36_246(x):
    # x is a list (or vector) of length 336
    return max(0, x[286])
def l36_247(x):
    # x is a list (or vector) of length 336
    return max(0, x[287])
def l36_248(x):
    # x is a list (or vector) of length 336
    return max(0, x[288])
def l36_249(x):
    # x is a list (or vector) of length 336
    return max(0, x[289])
def l36_250(x):
    # x is a list (or vector) of length 336
    return max(0, x[290])
def l36_251(x):
    # x is a list (or vector) of length 336
    return max(0, x[291])
def l36_252(x):
    # x is a list (or vector) of length 336
    return max(0, x[292])
def l36_253(x):
    # x is a list (or vector) of length 336
    return max(0, x[293])
def l36_254(x):
    # x is a list (or vector) of length 336
    return max(0, x[294])
def l36_255(x):
    # x is a list (or vector) of length 336
    return max(0, x[295])
def l36_256(x):
    # x is a list (or vector) of length 336
    return max(0, x[296])
def l36_257(x):
    # x is a list (or vector) of length 336
    return max(0, x[297])
def l36_258(x):
    # x is a list (or vector) of length 336
    return max(0, x[298])
def l36_259(x):
    # x is a list (or vector) of length 336
    return max(0, x[299])
def l36_260(x):
    # x is a list (or vector) of length 336
    return max(0, x[300])
def l36_261(x):
    # x is a list (or vector) of length 336
    return max(0, x[301])
def l36_262(x):
    # x is a list (or vector) of length 336
    return max(0, x[302])
def l36_263(x):
    # x is a list (or vector) of length 336
    return max(0, x[303])
def l36_264(x):
    # x is a list (or vector) of length 336
    return max(0, x[304])
def l36_265(x):
    # x is a list (or vector) of length 336
    return max(0, x[305])
def l36_266(x):
    # x is a list (or vector) of length 336
    return max(0, x[306])
def l36_267(x):
    # x is a list (or vector) of length 336
    return max(0, x[307])
def l36_268(x):
    # x is a list (or vector) of length 336
    return max(0, x[308])
def l36_269(x):
    # x is a list (or vector) of length 336
    return max(0, x[309])
def l36_270(x):
    # x is a list (or vector) of length 336
    return max(0, x[310])
def l36_271(x):
    # x is a list (or vector) of length 336
    return max(0, x[311])
def l36_272(x):
    # x is a list (or vector) of length 336
    return max(0, x[312])
def l36_273(x):
    # x is a list (or vector) of length 336
    return max(0, x[313])
def l36_274(x):
    # x is a list (or vector) of length 336
    return max(0, x[314])
def l36_275(x):
    # x is a list (or vector) of length 336
    return max(0, x[315])
def l36_276(x):
    # x is a list (or vector) of length 336
    return max(0, x[316])
def l36_277(x):
    # x is a list (or vector) of length 336
    return max(0, x[317])
def l36_278(x):
    # x is a list (or vector) of length 336
    return max(0, x[318])
def l36_279(x):
    # x is a list (or vector) of length 336
    return max(0, x[319])
def l36_280(x):
    # x is a list (or vector) of length 336
    return max(0, x[320])
def l36_281(x):
    # x is a list (or vector) of length 336
    return max(0, x[321])
def l36_282(x):
    # x is a list (or vector) of length 336
    return max(0, x[322])
def l36_283(x):
    # x is a list (or vector) of length 336
    return max(0, x[323])
def l36_284(x):
    # x is a list (or vector) of length 336
    return max(0, x[324])
def l36_285(x):
    # x is a list (or vector) of length 336
    return max(0, x[325])
def l36_286(x):
    # x is a list (or vector) of length 336
    return max(0, x[326])
def l36_287(x):
    # x is a list (or vector) of length 336
    return max(0, x[327])
def l36_288(x):
    # x is a list (or vector) of length 336
    return max(0, x[328])
def l36_289(x):
    # x is a list (or vector) of length 336
    return max(0, x[329])
def l36_290(x):
    # x is a list (or vector) of length 336
    return max(0, x[330])
def l36_291(x):
    # x is a list (or vector) of length 336
    return max(0, x[331])
def l36_292(x):
    # x is a list (or vector) of length 336
    return max(0, x[332])
def l36_293(x):
    # x is a list (or vector) of length 336
    return max(0, x[333])
def l36_294(x):
    # x is a list (or vector) of length 336
    return max(0, x[334])
def l36_295(x):
    # x is a list (or vector) of length 336
    return max(0, x[335])
def l36_(x):
    # x is a list (or vector) of length 336
    return [
        l36_0(x),
        l36_1(x),
        l36_2(x),
        l36_3(x),
        l36_4(x),
        l36_5(x),
        l36_6(x),
        l36_7(x),
        l36_8(x),
        l36_9(x),
        l36_10(x),
        l36_11(x),
        l36_12(x),
        l36_13(x),
        l36_14(x),
        l36_15(x),
        l36_16(x),
        l36_17(x),
        l36_18(x),
        l36_19(x),
        l36_20(x),
        l36_21(x),
        l36_22(x),
        l36_23(x),
        l36_24(x),
        l36_25(x),
        l36_26(x),
        l36_27(x),
        l36_28(x),
        l36_29(x),
        l36_30(x),
        l36_31(x),
        l36_32(x),
        l36_33(x),
        l36_34(x),
        l36_35(x),
        l36_36(x),
        l36_37(x),
        l36_38(x),
        l36_39(x),
        l36_40(x),
        l36_41(x),
        l36_42(x),
        l36_43(x),
        l36_44(x),
        l36_45(x),
        l36_46(x),
        l36_47(x),
        l36_48(x),
        l36_49(x),
        l36_50(x),
        l36_51(x),
        l36_52(x),
        l36_53(x),
        l36_54(x),
        l36_55(x),
        l36_56(x),
        l36_57(x),
        l36_58(x),
        l36_59(x),
        l36_60(x),
        l36_61(x),
        l36_62(x),
        l36_63(x),
        l36_64(x),
        l36_65(x),
        l36_66(x),
        l36_67(x),
        l36_68(x),
        l36_69(x),
        l36_70(x),
        l36_71(x),
        l36_72(x),
        l36_73(x),
        l36_74(x),
        l36_75(x),
        l36_76(x),
        l36_77(x),
        l36_78(x),
        l36_79(x),
        l36_80(x),
        l36_81(x),
        l36_82(x),
        l36_83(x),
        l36_84(x),
        l36_85(x),
        l36_86(x),
        l36_87(x),
        l36_88(x),
        l36_89(x),
        l36_90(x),
        l36_91(x),
        l36_92(x),
        l36_93(x),
        l36_94(x),
        l36_95(x),
        l36_96(x),
        l36_97(x),
        l36_98(x),
        l36_99(x),
        l36_100(x),
        l36_101(x),
        l36_102(x),
        l36_103(x),
        l36_104(x),
        l36_105(x),
        l36_106(x),
        l36_107(x),
        l36_108(x),
        l36_109(x),
        l36_110(x),
        l36_111(x),
        l36_112(x),
        l36_113(x),
        l36_114(x),
        l36_115(x),
        l36_116(x),
        l36_117(x),
        l36_118(x),
        l36_119(x),
        l36_120(x),
        l36_121(x),
        l36_122(x),
        l36_123(x),
        l36_124(x),
        l36_125(x),
        l36_126(x),
        l36_127(x),
        l36_128(x),
        l36_129(x),
        l36_130(x),
        l36_131(x),
        l36_132(x),
        l36_133(x),
        l36_134(x),
        l36_135(x),
        l36_136(x),
        l36_137(x),
        l36_138(x),
        l36_139(x),
        l36_140(x),
        l36_141(x),
        l36_142(x),
        l36_143(x),
        l36_144(x),
        l36_145(x),
        l36_146(x),
        l36_147(x),
        l36_148(x),
        l36_149(x),
        l36_150(x),
        l36_151(x),
        l36_152(x),
        l36_153(x),
        l36_154(x),
        l36_155(x),
        l36_156(x),
        l36_157(x),
        l36_158(x),
        l36_159(x),
        l36_160(x),
        l36_161(x),
        l36_162(x),
        l36_163(x),
        l36_164(x),
        l36_165(x),
        l36_166(x),
        l36_167(x),
        l36_168(x),
        l36_169(x),
        l36_170(x),
        l36_171(x),
        l36_172(x),
        l36_173(x),
        l36_174(x),
        l36_175(x),
        l36_176(x),
        l36_177(x),
        l36_178(x),
        l36_179(x),
        l36_180(x),
        l36_181(x),
        l36_182(x),
        l36_183(x),
        l36_184(x),
        l36_185(x),
        l36_186(x),
        l36_187(x),
        l36_188(x),
        l36_189(x),
        l36_190(x),
        l36_191(x),
        l36_192(x),
        l36_193(x),
        l36_194(x),
        l36_195(x),
        l36_196(x),
        l36_197(x),
        l36_198(x),
        l36_199(x),
        l36_200(x),
        l36_201(x),
        l36_202(x),
        l36_203(x),
        l36_204(x),
        l36_205(x),
        l36_206(x),
        l36_207(x),
        l36_208(x),
        l36_209(x),
        l36_210(x),
        l36_211(x),
        l36_212(x),
        l36_213(x),
        l36_214(x),
        l36_215(x),
        l36_216(x),
        l36_217(x),
        l36_218(x),
        l36_219(x),
        l36_220(x),
        l36_221(x),
        l36_222(x),
        l36_223(x),
        l36_224(x),
        l36_225(x),
        l36_226(x),
        l36_227(x),
        l36_228(x),
        l36_229(x),
        l36_230(x),
        l36_231(x),
        l36_232(x),
        l36_233(x),
        l36_234(x),
        l36_235(x),
        l36_236(x),
        l36_237(x),
        l36_238(x),
        l36_239(x),
        l36_240(x),
        l36_241(x),
        l36_242(x),
        l36_243(x),
        l36_244(x),
        l36_245(x),
        l36_246(x),
        l36_247(x),
        l36_248(x),
        l36_249(x),
        l36_250(x),
        l36_251(x),
        l36_252(x),
        l36_253(x),
        l36_254(x),
        l36_255(x),
        l36_256(x),
        l36_257(x),
        l36_258(x),
        l36_259(x),
        l36_260(x),
        l36_261(x),
        l36_262(x),
        l36_263(x),
        l36_264(x),
        l36_265(x),
        l36_266(x),
        l36_267(x),
        l36_268(x),
        l36_269(x),
        l36_270(x),
        l36_271(x),
        l36_272(x),
        l36_273(x),
        l36_274(x),
        l36_275(x),
        l36_276(x),
        l36_277(x),
        l36_278(x),
        l36_279(x),
        l36_280(x),
        l36_281(x),
        l36_282(x),
        l36_283(x),
        l36_284(x),
        l36_285(x),
        l36_286(x),
        l36_287(x),
        l36_288(x),
        l36_289(x),
        l36_290(x),
        l36_291(x),
        l36_292(x),
        l36_293(x),
        l36_294(x),
        l36_295(x),
    ]