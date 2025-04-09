import numpy as np




# Generated from reverse engineering
def l288_g(x: np.ndarray) -> np.ndarray:
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




def l288_0(x):
    # x is a list (or vector) of length 336
    return max(0, x[0])
def l288_1(x):
    # x is a list (or vector) of length 336
    return max(0, x[1])
def l288_2(x):
    # x is a list (or vector) of length 336
    return max(0, x[2])
def l288_3(x):
    # x is a list (or vector) of length 336
    return max(0, x[3])
def l288_4(x):
    # x is a list (or vector) of length 336
    return max(0, x[4])
def l288_5(x):
    # x is a list (or vector) of length 336
    return max(0, x[5])
def l288_6(x):
    # x is a list (or vector) of length 336
    return max(0, x[6])
def l288_7(x):
    # x is a list (or vector) of length 336
    return max(0, x[7])
def l288_8(x):
    # x is a list (or vector) of length 336
    return max(0, x[8])
def l288_9(x):
    # x is a list (or vector) of length 336
    return max(0, x[9])
def l288_10(x):
    # x is a list (or vector) of length 336
    return max(0, x[10])
def l288_11(x):
    # x is a list (or vector) of length 336
    return max(0, x[11])
def l288_12(x):
    # x is a list (or vector) of length 336
    return max(0, x[12])
def l288_13(x):
    # x is a list (or vector) of length 336
    return max(0, x[13])
def l288_14(x):
    # x is a list (or vector) of length 336
    return max(0, x[14])
def l288_15(x):
    # x is a list (or vector) of length 336
    return max(0, x[15])
def l288_16(x):
    # x is a list (or vector) of length 336
    return max(0, x[16])
def l288_17(x):
    # x is a list (or vector) of length 336
    return max(0, x[17])
def l288_18(x):
    # x is a list (or vector) of length 336
    return max(0, x[18])
def l288_19(x):
    # x is a list (or vector) of length 336
    return max(0, x[19])
def l288_20(x):
    # x is a list (or vector) of length 336
    return max(0, x[20])
def l288_21(x):
    # x is a list (or vector) of length 336
    return max(0, x[21])
def l288_22(x):
    # x is a list (or vector) of length 336
    return max(0, x[22])
def l288_23(x):
    # x is a list (or vector) of length 336
    return max(0, x[23])
def l288_24(x):
    # x is a list (or vector) of length 336
    return max(0, x[24])
def l288_25(x):
    # x is a list (or vector) of length 336
    return max(0, x[25])
def l288_26(x):
    # x is a list (or vector) of length 336
    return max(0, x[26])
def l288_27(x):
    # x is a list (or vector) of length 336
    return max(0, x[27])
def l288_28(x):
    # x is a list (or vector) of length 336
    return max(0, x[28])
def l288_29(x):
    # x is a list (or vector) of length 336
    return max(0, x[29])
def l288_30(x):
    # x is a list (or vector) of length 336
    return max(0, x[30])
def l288_31(x):
    # x is a list (or vector) of length 336
    return max(0, x[31])
def l288_32(x):
    # x is a list (or vector) of length 336
    return max(0, x[32])
def l288_33(x):
    # x is a list (or vector) of length 336
    return max(0, x[33])
def l288_34(x):
    # x is a list (or vector) of length 336
    return max(0, x[34])
def l288_35(x):
    # x is a list (or vector) of length 336
    return max(0, x[35])
def l288_36(x):
    # x is a list (or vector) of length 336
    return max(0, x[36])
def l288_37(x):
    # x is a list (or vector) of length 336
    return max(0, x[37])
def l288_38(x):
    # x is a list (or vector) of length 336
    return max(0, x[38])
def l288_39(x):
    # x is a list (or vector) of length 336
    return max(0, x[39])
def l288_40(x):
    # x is a list (or vector) of length 336
    return max(0, x[40])
def l288_41(x):
    # x is a list (or vector) of length 336
    return max(0, x[41])
def l288_42(x):
    # x is a list (or vector) of length 336
    return max(0, x[42])
def l288_43(x):
    # x is a list (or vector) of length 336
    return max(0, x[43])
def l288_44(x):
    # x is a list (or vector) of length 336
    return max(0, x[44])
def l288_45(x):
    # x is a list (or vector) of length 336
    return max(0, x[45])
def l288_46(x):
    # x is a list (or vector) of length 336
    return max(0, x[46])
def l288_47(x):
    # x is a list (or vector) of length 336
    return max(0, x[47])
def l288_48(x):
    # x is a list (or vector) of length 336
    return max(0, x[48])
def l288_49(x):
    # x is a list (or vector) of length 336
    return max(0, x[49])
def l288_50(x):
    # x is a list (or vector) of length 336
    return max(0, x[50])
def l288_51(x):
    # x is a list (or vector) of length 336
    return max(0, x[51])
def l288_52(x):
    # x is a list (or vector) of length 336
    return max(0, x[52])
def l288_53(x):
    # x is a list (or vector) of length 336
    return max(0, x[53])
def l288_54(x):
    # x is a list (or vector) of length 336
    return max(0, x[54])
def l288_55(x):
    # x is a list (or vector) of length 336
    return max(0, x[55])
def l288_56(x):
    # x is a list (or vector) of length 336
    return max(0, x[56])
def l288_57(x):
    # x is a list (or vector) of length 336
    return max(0, x[57])
def l288_58(x):
    # x is a list (or vector) of length 336
    return max(0, x[58])
def l288_59(x):
    # x is a list (or vector) of length 336
    return max(0, x[59])
def l288_60(x):
    # x is a list (or vector) of length 336
    return max(0, x[60])
def l288_61(x):
    # x is a list (or vector) of length 336
    return max(0, x[61])
def l288_62(x):
    # x is a list (or vector) of length 336
    return max(0, x[62])
def l288_63(x):
    # x is a list (or vector) of length 336
    return max(0, x[63])
def l288_64(x):
    # x is a list (or vector) of length 336
    return max(0, x[64])
def l288_65(x):
    # x is a list (or vector) of length 336
    return max(0, x[65])
def l288_66(x):
    # x is a list (or vector) of length 336
    return max(0, x[66])
def l288_67(x):
    # x is a list (or vector) of length 336
    return max(0, x[67])
def l288_68(x):
    # x is a list (or vector) of length 336
    return max(0, x[68])
def l288_69(x):
    # x is a list (or vector) of length 336
    return max(0, x[69])
def l288_70(x):
    # x is a list (or vector) of length 336
    return max(0, x[70])
def l288_71(x):
    # x is a list (or vector) of length 336
    return max(0, x[71])
def l288_72(x):
    # x is a list (or vector) of length 336
    return max(0, x[72])
def l288_73(x):
    # x is a list (or vector) of length 336
    return max(0, x[73])
def l288_74(x):
    # x is a list (or vector) of length 336
    return max(0, x[74])
def l288_75(x):
    # x is a list (or vector) of length 336
    return max(0, x[75])
def l288_76(x):
    # x is a list (or vector) of length 336
    return max(0, x[76])
def l288_77(x):
    # x is a list (or vector) of length 336
    return max(0, x[77])
def l288_78(x):
    # x is a list (or vector) of length 336
    return max(0, x[78])
def l288_79(x):
    # x is a list (or vector) of length 336
    return max(0, x[79])
def l288_80(x):
    # x is a list (or vector) of length 336
    return max(0, x[80])
def l288_81(x):
    # x is a list (or vector) of length 336
    return max(0, x[81])
def l288_82(x):
    # x is a list (or vector) of length 336
    return max(0, x[82])
def l288_83(x):
    # x is a list (or vector) of length 336
    return max(0, x[83])
def l288_84(x):
    # x is a list (or vector) of length 336
    return max(0, x[84])
def l288_85(x):
    # x is a list (or vector) of length 336
    return max(0, x[85])
def l288_86(x):
    # x is a list (or vector) of length 336
    return max(0, x[86])
def l288_87(x):
    # x is a list (or vector) of length 336
    return max(0, x[87])
def l288_88(x):
    # x is a list (or vector) of length 336
    return max(0, x[88])
def l288_89(x):
    # x is a list (or vector) of length 336
    return max(0, x[89])
def l288_90(x):
    # x is a list (or vector) of length 336
    return max(0, x[90])
def l288_91(x):
    # x is a list (or vector) of length 336
    return max(0, x[91])
def l288_92(x):
    # x is a list (or vector) of length 336
    return max(0, x[92])
def l288_93(x):
    # x is a list (or vector) of length 336
    return max(0, x[93])
def l288_94(x):
    # x is a list (or vector) of length 336
    return max(0, x[94])
def l288_95(x):
    # x is a list (or vector) of length 336
    return max(0, x[95])
def l288_96(x):
    # x is a list (or vector) of length 336
    return max(0, x[96])
def l288_97(x):
    # x is a list (or vector) of length 336
    return max(0, x[97])
def l288_98(x):
    # x is a list (or vector) of length 336
    return max(0, x[98])
def l288_99(x):
    # x is a list (or vector) of length 336
    return max(0, x[99])
def l288_100(x):
    # x is a list (or vector) of length 336
    return max(0, x[100])
def l288_101(x):
    # x is a list (or vector) of length 336
    return max(0, x[101])
def l288_102(x):
    # x is a list (or vector) of length 336
    return max(0, x[102])
def l288_103(x):
    # x is a list (or vector) of length 336
    return max(0, x[103])
def l288_104(x):
    # x is a list (or vector) of length 336
    return max(0, x[104])
def l288_105(x):
    # x is a list (or vector) of length 336
    return max(0, x[105])
def l288_106(x):
    # x is a list (or vector) of length 336
    return max(0, x[106])
def l288_107(x):
    # x is a list (or vector) of length 336
    return max(0, x[107])
def l288_108(x):
    # x is a list (or vector) of length 336
    return max(0, x[108])
def l288_109(x):
    # x is a list (or vector) of length 336
    return max(0, x[109])
def l288_110(x):
    # x is a list (or vector) of length 336
    return max(0, x[110])
def l288_111(x):
    # x is a list (or vector) of length 336
    return max(0, x[111])
def l288_112(x):
    # x is a list (or vector) of length 336
    return max(0, x[112])
def l288_113(x):
    # x is a list (or vector) of length 336
    return max(0, x[113])
def l288_114(x):
    # x is a list (or vector) of length 336
    return max(0, x[114])
def l288_115(x):
    # x is a list (or vector) of length 336
    return max(0, x[115])
def l288_116(x):
    # x is a list (or vector) of length 336
    return max(0, x[116])
def l288_117(x):
    # x is a list (or vector) of length 336
    return max(0, x[117])
def l288_118(x):
    # x is a list (or vector) of length 336
    return max(0, x[118])
def l288_119(x):
    # x is a list (or vector) of length 336
    return max(0, x[119])
def l288_120(x):
    # x is a list (or vector) of length 336
    return max(0, x[120])
def l288_121(x):
    # x is a list (or vector) of length 336
    return max(0, x[121])
def l288_122(x):
    # x is a list (or vector) of length 336
    return max(0, x[122])
def l288_123(x):
    # x is a list (or vector) of length 336
    return max(0, x[123])
def l288_124(x):
    # x is a list (or vector) of length 336
    return max(0, x[124])
def l288_125(x):
    # x is a list (or vector) of length 336
    return max(0, x[125])
def l288_126(x):
    # x is a list (or vector) of length 336
    return max(0, x[126])
def l288_127(x):
    # x is a list (or vector) of length 336
    return max(0, x[127])
def l288_128(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[128] + -1.0*x[160] + 1.0)
def l288_129(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[129] + -1.0*x[161] + 1.0)
def l288_130(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[130] + -1.0*x[162] + 1.0)
def l288_131(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[131] + -1.0*x[163] + 1.0)
def l288_132(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[132] + -1.0*x[164] + 1.0)
def l288_133(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[133] + -1.0*x[165] + 1.0)
def l288_134(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[134] + -1.0*x[166] + 1.0)
def l288_135(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[135] + -1.0*x[167] + 1.0)
def l288_136(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[136] + -1.0*x[168] + 1.0)
def l288_137(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[137] + -1.0*x[169] + 1.0)
def l288_138(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[138] + -1.0*x[170] + 1.0)
def l288_139(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[139] + -1.0*x[171] + 1.0)
def l288_140(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[140] + -1.0*x[172] + 1.0)
def l288_141(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[141] + -1.0*x[173] + 1.0)
def l288_142(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[142] + -1.0*x[174] + 1.0)
def l288_143(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[143] + -1.0*x[175] + 1.0)
def l288_144(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[144] + -1.0*x[176] + 1.0)
def l288_145(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[145] + -1.0*x[177] + 1.0)
def l288_146(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[146] + -1.0*x[178] + 1.0)
def l288_147(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[147] + -1.0*x[179] + 1.0)
def l288_148(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[148] + -1.0*x[180] + 1.0)
def l288_149(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[149] + -1.0*x[181] + 1.0)
def l288_150(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[150] + -1.0*x[182] + 1.0)
def l288_151(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[151] + -1.0*x[183] + 1.0)
def l288_152(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[152] + -1.0*x[184] + 1.0)
def l288_153(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[153] + -1.0*x[185] + 1.0)
def l288_154(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[154] + -1.0*x[186] + 1.0)
def l288_155(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[155] + -1.0*x[187] + 1.0)
def l288_156(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[156] + -1.0*x[188] + 1.0)
def l288_157(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[157] + -1.0*x[189] + 1.0)
def l288_158(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[158] + -1.0*x[190] + 1.0)
def l288_159(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[159] + -1.0*x[191] + 1.0)
def l288_160(x):
    # x is a list (or vector) of length 336
    return max(0, x[192])
def l288_161(x):
    # x is a list (or vector) of length 336
    return max(0, x[193])
def l288_162(x):
    # x is a list (or vector) of length 336
    return max(0, x[194])
def l288_163(x):
    # x is a list (or vector) of length 336
    return max(0, x[195])
def l288_164(x):
    # x is a list (or vector) of length 336
    return max(0, x[196])
def l288_165(x):
    # x is a list (or vector) of length 336
    return max(0, x[197])
def l288_166(x):
    # x is a list (or vector) of length 336
    return max(0, x[198])
def l288_167(x):
    # x is a list (or vector) of length 336
    return max(0, x[199])
def l288_168(x):
    # x is a list (or vector) of length 336
    return max(0, x[200])
def l288_169(x):
    # x is a list (or vector) of length 336
    return max(0, x[201])
def l288_170(x):
    # x is a list (or vector) of length 336
    return max(0, x[202])
def l288_171(x):
    # x is a list (or vector) of length 336
    return max(0, x[203])
def l288_172(x):
    # x is a list (or vector) of length 336
    return max(0, x[204])
def l288_173(x):
    # x is a list (or vector) of length 336
    return max(0, x[205])
def l288_174(x):
    # x is a list (or vector) of length 336
    return max(0, x[206])
def l288_175(x):
    # x is a list (or vector) of length 336
    return max(0, x[207])
def l288_176(x):
    # x is a list (or vector) of length 336
    return max(0, x[208])
def l288_177(x):
    # x is a list (or vector) of length 336
    return max(0, x[209])
def l288_178(x):
    # x is a list (or vector) of length 336
    return max(0, x[210])
def l288_179(x):
    # x is a list (or vector) of length 336
    return max(0, x[211])
def l288_180(x):
    # x is a list (or vector) of length 336
    return max(0, x[212])
def l288_181(x):
    # x is a list (or vector) of length 336
    return max(0, x[213])
def l288_182(x):
    # x is a list (or vector) of length 336
    return max(0, x[214])
def l288_183(x):
    # x is a list (or vector) of length 336
    return max(0, x[215])
def l288_184(x):
    # x is a list (or vector) of length 336
    return max(0, x[216])
def l288_185(x):
    # x is a list (or vector) of length 336
    return max(0, x[217])
def l288_186(x):
    # x is a list (or vector) of length 336
    return max(0, x[218])
def l288_187(x):
    # x is a list (or vector) of length 336
    return max(0, x[219])
def l288_188(x):
    # x is a list (or vector) of length 336
    return max(0, x[220])
def l288_189(x):
    # x is a list (or vector) of length 336
    return max(0, x[221])
def l288_190(x):
    # x is a list (or vector) of length 336
    return max(0, x[222])
def l288_191(x):
    # x is a list (or vector) of length 336
    return max(0, x[223])
def l288_192(x):
    # x is a list (or vector) of length 336
    return max(0, x[224])
def l288_193(x):
    # x is a list (or vector) of length 336
    return max(0, x[225])
def l288_194(x):
    # x is a list (or vector) of length 336
    return max(0, x[226])
def l288_195(x):
    # x is a list (or vector) of length 336
    return max(0, x[227])
def l288_196(x):
    # x is a list (or vector) of length 336
    return max(0, x[228])
def l288_197(x):
    # x is a list (or vector) of length 336
    return max(0, x[229])
def l288_198(x):
    # x is a list (or vector) of length 336
    return max(0, x[230])
def l288_199(x):
    # x is a list (or vector) of length 336
    return max(0, x[231])
def l288_200(x):
    # x is a list (or vector) of length 336
    return max(0, x[232])
def l288_201(x):
    # x is a list (or vector) of length 336
    return max(0, x[233])
def l288_202(x):
    # x is a list (or vector) of length 336
    return max(0, x[234])
def l288_203(x):
    # x is a list (or vector) of length 336
    return max(0, x[235])
def l288_204(x):
    # x is a list (or vector) of length 336
    return max(0, x[236])
def l288_205(x):
    # x is a list (or vector) of length 336
    return max(0, x[237])
def l288_206(x):
    # x is a list (or vector) of length 336
    return max(0, x[238])
def l288_207(x):
    # x is a list (or vector) of length 336
    return max(0, x[239])
def l288_208(x):
    # x is a list (or vector) of length 336
    return max(0, x[240])
def l288_209(x):
    # x is a list (or vector) of length 336
    return max(0, x[241])
def l288_210(x):
    # x is a list (or vector) of length 336
    return max(0, x[242])
def l288_211(x):
    # x is a list (or vector) of length 336
    return max(0, x[243])
def l288_212(x):
    # x is a list (or vector) of length 336
    return max(0, x[244])
def l288_213(x):
    # x is a list (or vector) of length 336
    return max(0, x[245])
def l288_214(x):
    # x is a list (or vector) of length 336
    return max(0, x[246])
def l288_215(x):
    # x is a list (or vector) of length 336
    return max(0, x[247])
def l288_216(x):
    # x is a list (or vector) of length 336
    return max(0, x[248])
def l288_217(x):
    # x is a list (or vector) of length 336
    return max(0, x[249])
def l288_218(x):
    # x is a list (or vector) of length 336
    return max(0, x[250])
def l288_219(x):
    # x is a list (or vector) of length 336
    return max(0, x[251])
def l288_220(x):
    # x is a list (or vector) of length 336
    return max(0, x[252])
def l288_221(x):
    # x is a list (or vector) of length 336
    return max(0, x[253])
def l288_222(x):
    # x is a list (or vector) of length 336
    return max(0, x[254])
def l288_223(x):
    # x is a list (or vector) of length 336
    return max(0, x[255])
def l288_224(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[256] + 1.0)
def l288_225(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[257] + 1.0)
def l288_226(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[258] + 1.0)
def l288_227(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[259] + 1.0)
def l288_228(x):
    # x is a list (or vector) of length 336
    return max(0, x[260] + -128.0*x[264] + 128.0*x[268])
def l288_229(x):
    # x is a list (or vector) of length 336
    return max(0, x[261] + -128.0*x[265] + 128.0*x[269])
def l288_230(x):
    # x is a list (or vector) of length 336
    return max(0, x[262] + -128.0*x[266] + 128.0*x[270])
def l288_231(x):
    # x is a list (or vector) of length 336
    return max(0, x[263] + -128.0*x[267] + 128.0*x[271])
def l288_232(x):
    # x is a list (or vector) of length 336
    return max(0, x[272])
def l288_233(x):
    # x is a list (or vector) of length 336
    return max(0, x[273])
def l288_234(x):
    # x is a list (or vector) of length 336
    return max(0, x[274])
def l288_235(x):
    # x is a list (or vector) of length 336
    return max(0, x[275])
def l288_236(x):
    # x is a list (or vector) of length 336
    return max(0, x[276])
def l288_237(x):
    # x is a list (or vector) of length 336
    return max(0, x[277])
def l288_238(x):
    # x is a list (or vector) of length 336
    return max(0, x[278])
def l288_239(x):
    # x is a list (or vector) of length 336
    return max(0, x[279])
def l288_240(x):
    # x is a list (or vector) of length 336
    return max(0, x[280])
def l288_241(x):
    # x is a list (or vector) of length 336
    return max(0, x[281])
def l288_242(x):
    # x is a list (or vector) of length 336
    return max(0, x[282])
def l288_243(x):
    # x is a list (or vector) of length 336
    return max(0, x[283])
def l288_244(x):
    # x is a list (or vector) of length 336
    return max(0, x[284])
def l288_245(x):
    # x is a list (or vector) of length 336
    return max(0, x[285])
def l288_246(x):
    # x is a list (or vector) of length 336
    return max(0, x[286])
def l288_247(x):
    # x is a list (or vector) of length 336
    return max(0, x[287])
def l288_248(x):
    # x is a list (or vector) of length 336
    return max(0, x[288])
def l288_249(x):
    # x is a list (or vector) of length 336
    return max(0, x[289])
def l288_250(x):
    # x is a list (or vector) of length 336
    return max(0, x[290])
def l288_251(x):
    # x is a list (or vector) of length 336
    return max(0, x[291])
def l288_252(x):
    # x is a list (or vector) of length 336
    return max(0, x[292])
def l288_253(x):
    # x is a list (or vector) of length 336
    return max(0, x[293])
def l288_254(x):
    # x is a list (or vector) of length 336
    return max(0, x[294])
def l288_255(x):
    # x is a list (or vector) of length 336
    return max(0, x[295])
def l288_256(x):
    # x is a list (or vector) of length 336
    return max(0, x[296])
def l288_257(x):
    # x is a list (or vector) of length 336
    return max(0, x[297])
def l288_258(x):
    # x is a list (or vector) of length 336
    return max(0, x[298])
def l288_259(x):
    # x is a list (or vector) of length 336
    return max(0, x[299])
def l288_260(x):
    # x is a list (or vector) of length 336
    return max(0, x[300])
def l288_261(x):
    # x is a list (or vector) of length 336
    return max(0, x[301])
def l288_262(x):
    # x is a list (or vector) of length 336
    return max(0, x[302])
def l288_263(x):
    # x is a list (or vector) of length 336
    return max(0, x[303])
def l288_264(x):
    # x is a list (or vector) of length 336
    return max(0, x[304])
def l288_265(x):
    # x is a list (or vector) of length 336
    return max(0, x[305])
def l288_266(x):
    # x is a list (or vector) of length 336
    return max(0, x[306])
def l288_267(x):
    # x is a list (or vector) of length 336
    return max(0, x[307])
def l288_268(x):
    # x is a list (or vector) of length 336
    return max(0, x[308])
def l288_269(x):
    # x is a list (or vector) of length 336
    return max(0, x[309])
def l288_270(x):
    # x is a list (or vector) of length 336
    return max(0, x[310])
def l288_271(x):
    # x is a list (or vector) of length 336
    return max(0, x[311])
def l288_272(x):
    # x is a list (or vector) of length 336
    return max(0, x[312])
def l288_273(x):
    # x is a list (or vector) of length 336
    return max(0, x[313])
def l288_274(x):
    # x is a list (or vector) of length 336
    return max(0, x[314])
def l288_275(x):
    # x is a list (or vector) of length 336
    return max(0, x[315])
def l288_276(x):
    # x is a list (or vector) of length 336
    return max(0, x[316])
def l288_277(x):
    # x is a list (or vector) of length 336
    return max(0, x[317])
def l288_278(x):
    # x is a list (or vector) of length 336
    return max(0, x[318])
def l288_279(x):
    # x is a list (or vector) of length 336
    return max(0, x[319])
def l288_280(x):
    # x is a list (or vector) of length 336
    return max(0, x[320])
def l288_281(x):
    # x is a list (or vector) of length 336
    return max(0, x[321])
def l288_282(x):
    # x is a list (or vector) of length 336
    return max(0, x[322])
def l288_283(x):
    # x is a list (or vector) of length 336
    return max(0, x[323])
def l288_284(x):
    # x is a list (or vector) of length 336
    return max(0, x[324])
def l288_285(x):
    # x is a list (or vector) of length 336
    return max(0, x[325])
def l288_286(x):
    # x is a list (or vector) of length 336
    return max(0, x[326])
def l288_287(x):
    # x is a list (or vector) of length 336
    return max(0, x[327])
def l288_288(x):
    # x is a list (or vector) of length 336
    return max(0, x[328])
def l288_289(x):
    # x is a list (or vector) of length 336
    return max(0, x[329])
def l288_290(x):
    # x is a list (or vector) of length 336
    return max(0, x[330])
def l288_291(x):
    # x is a list (or vector) of length 336
    return max(0, x[331])
def l288_292(x):
    # x is a list (or vector) of length 336
    return max(0, x[332])
def l288_293(x):
    # x is a list (or vector) of length 336
    return max(0, x[333])
def l288_294(x):
    # x is a list (or vector) of length 336
    return max(0, x[334])
def l288_295(x):
    # x is a list (or vector) of length 336
    return max(0, x[335])
def l288_(x):
    # x is a list (or vector) of length 336
    return [
        l288_0(x),
        l288_1(x),
        l288_2(x),
        l288_3(x),
        l288_4(x),
        l288_5(x),
        l288_6(x),
        l288_7(x),
        l288_8(x),
        l288_9(x),
        l288_10(x),
        l288_11(x),
        l288_12(x),
        l288_13(x),
        l288_14(x),
        l288_15(x),
        l288_16(x),
        l288_17(x),
        l288_18(x),
        l288_19(x),
        l288_20(x),
        l288_21(x),
        l288_22(x),
        l288_23(x),
        l288_24(x),
        l288_25(x),
        l288_26(x),
        l288_27(x),
        l288_28(x),
        l288_29(x),
        l288_30(x),
        l288_31(x),
        l288_32(x),
        l288_33(x),
        l288_34(x),
        l288_35(x),
        l288_36(x),
        l288_37(x),
        l288_38(x),
        l288_39(x),
        l288_40(x),
        l288_41(x),
        l288_42(x),
        l288_43(x),
        l288_44(x),
        l288_45(x),
        l288_46(x),
        l288_47(x),
        l288_48(x),
        l288_49(x),
        l288_50(x),
        l288_51(x),
        l288_52(x),
        l288_53(x),
        l288_54(x),
        l288_55(x),
        l288_56(x),
        l288_57(x),
        l288_58(x),
        l288_59(x),
        l288_60(x),
        l288_61(x),
        l288_62(x),
        l288_63(x),
        l288_64(x),
        l288_65(x),
        l288_66(x),
        l288_67(x),
        l288_68(x),
        l288_69(x),
        l288_70(x),
        l288_71(x),
        l288_72(x),
        l288_73(x),
        l288_74(x),
        l288_75(x),
        l288_76(x),
        l288_77(x),
        l288_78(x),
        l288_79(x),
        l288_80(x),
        l288_81(x),
        l288_82(x),
        l288_83(x),
        l288_84(x),
        l288_85(x),
        l288_86(x),
        l288_87(x),
        l288_88(x),
        l288_89(x),
        l288_90(x),
        l288_91(x),
        l288_92(x),
        l288_93(x),
        l288_94(x),
        l288_95(x),
        l288_96(x),
        l288_97(x),
        l288_98(x),
        l288_99(x),
        l288_100(x),
        l288_101(x),
        l288_102(x),
        l288_103(x),
        l288_104(x),
        l288_105(x),
        l288_106(x),
        l288_107(x),
        l288_108(x),
        l288_109(x),
        l288_110(x),
        l288_111(x),
        l288_112(x),
        l288_113(x),
        l288_114(x),
        l288_115(x),
        l288_116(x),
        l288_117(x),
        l288_118(x),
        l288_119(x),
        l288_120(x),
        l288_121(x),
        l288_122(x),
        l288_123(x),
        l288_124(x),
        l288_125(x),
        l288_126(x),
        l288_127(x),
        l288_128(x),
        l288_129(x),
        l288_130(x),
        l288_131(x),
        l288_132(x),
        l288_133(x),
        l288_134(x),
        l288_135(x),
        l288_136(x),
        l288_137(x),
        l288_138(x),
        l288_139(x),
        l288_140(x),
        l288_141(x),
        l288_142(x),
        l288_143(x),
        l288_144(x),
        l288_145(x),
        l288_146(x),
        l288_147(x),
        l288_148(x),
        l288_149(x),
        l288_150(x),
        l288_151(x),
        l288_152(x),
        l288_153(x),
        l288_154(x),
        l288_155(x),
        l288_156(x),
        l288_157(x),
        l288_158(x),
        l288_159(x),
        l288_160(x),
        l288_161(x),
        l288_162(x),
        l288_163(x),
        l288_164(x),
        l288_165(x),
        l288_166(x),
        l288_167(x),
        l288_168(x),
        l288_169(x),
        l288_170(x),
        l288_171(x),
        l288_172(x),
        l288_173(x),
        l288_174(x),
        l288_175(x),
        l288_176(x),
        l288_177(x),
        l288_178(x),
        l288_179(x),
        l288_180(x),
        l288_181(x),
        l288_182(x),
        l288_183(x),
        l288_184(x),
        l288_185(x),
        l288_186(x),
        l288_187(x),
        l288_188(x),
        l288_189(x),
        l288_190(x),
        l288_191(x),
        l288_192(x),
        l288_193(x),
        l288_194(x),
        l288_195(x),
        l288_196(x),
        l288_197(x),
        l288_198(x),
        l288_199(x),
        l288_200(x),
        l288_201(x),
        l288_202(x),
        l288_203(x),
        l288_204(x),
        l288_205(x),
        l288_206(x),
        l288_207(x),
        l288_208(x),
        l288_209(x),
        l288_210(x),
        l288_211(x),
        l288_212(x),
        l288_213(x),
        l288_214(x),
        l288_215(x),
        l288_216(x),
        l288_217(x),
        l288_218(x),
        l288_219(x),
        l288_220(x),
        l288_221(x),
        l288_222(x),
        l288_223(x),
        l288_224(x),
        l288_225(x),
        l288_226(x),
        l288_227(x),
        l288_228(x),
        l288_229(x),
        l288_230(x),
        l288_231(x),
        l288_232(x),
        l288_233(x),
        l288_234(x),
        l288_235(x),
        l288_236(x),
        l288_237(x),
        l288_238(x),
        l288_239(x),
        l288_240(x),
        l288_241(x),
        l288_242(x),
        l288_243(x),
        l288_244(x),
        l288_245(x),
        l288_246(x),
        l288_247(x),
        l288_248(x),
        l288_249(x),
        l288_250(x),
        l288_251(x),
        l288_252(x),
        l288_253(x),
        l288_254(x),
        l288_255(x),
        l288_256(x),
        l288_257(x),
        l288_258(x),
        l288_259(x),
        l288_260(x),
        l288_261(x),
        l288_262(x),
        l288_263(x),
        l288_264(x),
        l288_265(x),
        l288_266(x),
        l288_267(x),
        l288_268(x),
        l288_269(x),
        l288_270(x),
        l288_271(x),
        l288_272(x),
        l288_273(x),
        l288_274(x),
        l288_275(x),
        l288_276(x),
        l288_277(x),
        l288_278(x),
        l288_279(x),
        l288_280(x),
        l288_281(x),
        l288_282(x),
        l288_283(x),
        l288_284(x),
        l288_285(x),
        l288_286(x),
        l288_287(x),
        l288_288(x),
        l288_289(x),
        l288_290(x),
        l288_291(x),
        l288_292(x),
        l288_293(x),
        l288_294(x),
        l288_295(x),
    ]