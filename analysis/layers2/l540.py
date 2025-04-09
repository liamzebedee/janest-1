import numpy as np




# Generated from reverse engineering
def l540_g(x: np.ndarray) -> np.ndarray:
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




def l540_0(x):
    # x is a list (or vector) of length 336
    return max(0, x[0])
def l540_1(x):
    # x is a list (or vector) of length 336
    return max(0, x[1])
def l540_2(x):
    # x is a list (or vector) of length 336
    return max(0, x[2])
def l540_3(x):
    # x is a list (or vector) of length 336
    return max(0, x[3])
def l540_4(x):
    # x is a list (or vector) of length 336
    return max(0, x[4])
def l540_5(x):
    # x is a list (or vector) of length 336
    return max(0, x[5])
def l540_6(x):
    # x is a list (or vector) of length 336
    return max(0, x[6])
def l540_7(x):
    # x is a list (or vector) of length 336
    return max(0, x[7])
def l540_8(x):
    # x is a list (or vector) of length 336
    return max(0, x[8])
def l540_9(x):
    # x is a list (or vector) of length 336
    return max(0, x[9])
def l540_10(x):
    # x is a list (or vector) of length 336
    return max(0, x[10])
def l540_11(x):
    # x is a list (or vector) of length 336
    return max(0, x[11])
def l540_12(x):
    # x is a list (or vector) of length 336
    return max(0, x[12])
def l540_13(x):
    # x is a list (or vector) of length 336
    return max(0, x[13])
def l540_14(x):
    # x is a list (or vector) of length 336
    return max(0, x[14])
def l540_15(x):
    # x is a list (or vector) of length 336
    return max(0, x[15])
def l540_16(x):
    # x is a list (or vector) of length 336
    return max(0, x[16])
def l540_17(x):
    # x is a list (or vector) of length 336
    return max(0, x[17])
def l540_18(x):
    # x is a list (or vector) of length 336
    return max(0, x[18])
def l540_19(x):
    # x is a list (or vector) of length 336
    return max(0, x[19])
def l540_20(x):
    # x is a list (or vector) of length 336
    return max(0, x[20])
def l540_21(x):
    # x is a list (or vector) of length 336
    return max(0, x[21])
def l540_22(x):
    # x is a list (or vector) of length 336
    return max(0, x[22])
def l540_23(x):
    # x is a list (or vector) of length 336
    return max(0, x[23])
def l540_24(x):
    # x is a list (or vector) of length 336
    return max(0, x[24])
def l540_25(x):
    # x is a list (or vector) of length 336
    return max(0, x[25])
def l540_26(x):
    # x is a list (or vector) of length 336
    return max(0, x[26])
def l540_27(x):
    # x is a list (or vector) of length 336
    return max(0, x[27])
def l540_28(x):
    # x is a list (or vector) of length 336
    return max(0, x[28])
def l540_29(x):
    # x is a list (or vector) of length 336
    return max(0, x[29])
def l540_30(x):
    # x is a list (or vector) of length 336
    return max(0, x[30])
def l540_31(x):
    # x is a list (or vector) of length 336
    return max(0, x[31])
def l540_32(x):
    # x is a list (or vector) of length 336
    return max(0, x[32])
def l540_33(x):
    # x is a list (or vector) of length 336
    return max(0, x[33])
def l540_34(x):
    # x is a list (or vector) of length 336
    return max(0, x[34])
def l540_35(x):
    # x is a list (or vector) of length 336
    return max(0, x[35])
def l540_36(x):
    # x is a list (or vector) of length 336
    return max(0, x[36])
def l540_37(x):
    # x is a list (or vector) of length 336
    return max(0, x[37])
def l540_38(x):
    # x is a list (or vector) of length 336
    return max(0, x[38])
def l540_39(x):
    # x is a list (or vector) of length 336
    return max(0, x[39])
def l540_40(x):
    # x is a list (or vector) of length 336
    return max(0, x[40])
def l540_41(x):
    # x is a list (or vector) of length 336
    return max(0, x[41])
def l540_42(x):
    # x is a list (or vector) of length 336
    return max(0, x[42])
def l540_43(x):
    # x is a list (or vector) of length 336
    return max(0, x[43])
def l540_44(x):
    # x is a list (or vector) of length 336
    return max(0, x[44])
def l540_45(x):
    # x is a list (or vector) of length 336
    return max(0, x[45])
def l540_46(x):
    # x is a list (or vector) of length 336
    return max(0, x[46])
def l540_47(x):
    # x is a list (or vector) of length 336
    return max(0, x[47])
def l540_48(x):
    # x is a list (or vector) of length 336
    return max(0, x[48])
def l540_49(x):
    # x is a list (or vector) of length 336
    return max(0, x[49])
def l540_50(x):
    # x is a list (or vector) of length 336
    return max(0, x[50])
def l540_51(x):
    # x is a list (or vector) of length 336
    return max(0, x[51])
def l540_52(x):
    # x is a list (or vector) of length 336
    return max(0, x[52])
def l540_53(x):
    # x is a list (or vector) of length 336
    return max(0, x[53])
def l540_54(x):
    # x is a list (or vector) of length 336
    return max(0, x[54])
def l540_55(x):
    # x is a list (or vector) of length 336
    return max(0, x[55])
def l540_56(x):
    # x is a list (or vector) of length 336
    return max(0, x[56])
def l540_57(x):
    # x is a list (or vector) of length 336
    return max(0, x[57])
def l540_58(x):
    # x is a list (or vector) of length 336
    return max(0, x[58])
def l540_59(x):
    # x is a list (or vector) of length 336
    return max(0, x[59])
def l540_60(x):
    # x is a list (or vector) of length 336
    return max(0, x[60])
def l540_61(x):
    # x is a list (or vector) of length 336
    return max(0, x[61])
def l540_62(x):
    # x is a list (or vector) of length 336
    return max(0, x[62])
def l540_63(x):
    # x is a list (or vector) of length 336
    return max(0, x[63])
def l540_64(x):
    # x is a list (or vector) of length 336
    return max(0, x[64])
def l540_65(x):
    # x is a list (or vector) of length 336
    return max(0, x[65])
def l540_66(x):
    # x is a list (or vector) of length 336
    return max(0, x[66])
def l540_67(x):
    # x is a list (or vector) of length 336
    return max(0, x[67])
def l540_68(x):
    # x is a list (or vector) of length 336
    return max(0, x[68])
def l540_69(x):
    # x is a list (or vector) of length 336
    return max(0, x[69])
def l540_70(x):
    # x is a list (or vector) of length 336
    return max(0, x[70])
def l540_71(x):
    # x is a list (or vector) of length 336
    return max(0, x[71])
def l540_72(x):
    # x is a list (or vector) of length 336
    return max(0, x[72])
def l540_73(x):
    # x is a list (or vector) of length 336
    return max(0, x[73])
def l540_74(x):
    # x is a list (or vector) of length 336
    return max(0, x[74])
def l540_75(x):
    # x is a list (or vector) of length 336
    return max(0, x[75])
def l540_76(x):
    # x is a list (or vector) of length 336
    return max(0, x[76])
def l540_77(x):
    # x is a list (or vector) of length 336
    return max(0, x[77])
def l540_78(x):
    # x is a list (or vector) of length 336
    return max(0, x[78])
def l540_79(x):
    # x is a list (or vector) of length 336
    return max(0, x[79])
def l540_80(x):
    # x is a list (or vector) of length 336
    return max(0, x[80])
def l540_81(x):
    # x is a list (or vector) of length 336
    return max(0, x[81])
def l540_82(x):
    # x is a list (or vector) of length 336
    return max(0, x[82])
def l540_83(x):
    # x is a list (or vector) of length 336
    return max(0, x[83])
def l540_84(x):
    # x is a list (or vector) of length 336
    return max(0, x[84])
def l540_85(x):
    # x is a list (or vector) of length 336
    return max(0, x[85])
def l540_86(x):
    # x is a list (or vector) of length 336
    return max(0, x[86])
def l540_87(x):
    # x is a list (or vector) of length 336
    return max(0, x[87])
def l540_88(x):
    # x is a list (or vector) of length 336
    return max(0, x[88])
def l540_89(x):
    # x is a list (or vector) of length 336
    return max(0, x[89])
def l540_90(x):
    # x is a list (or vector) of length 336
    return max(0, x[90])
def l540_91(x):
    # x is a list (or vector) of length 336
    return max(0, x[91])
def l540_92(x):
    # x is a list (or vector) of length 336
    return max(0, x[92])
def l540_93(x):
    # x is a list (or vector) of length 336
    return max(0, x[93])
def l540_94(x):
    # x is a list (or vector) of length 336
    return max(0, x[94])
def l540_95(x):
    # x is a list (or vector) of length 336
    return max(0, x[95])
def l540_96(x):
    # x is a list (or vector) of length 336
    return max(0, x[96])
def l540_97(x):
    # x is a list (or vector) of length 336
    return max(0, x[97])
def l540_98(x):
    # x is a list (or vector) of length 336
    return max(0, x[98])
def l540_99(x):
    # x is a list (or vector) of length 336
    return max(0, x[99])
def l540_100(x):
    # x is a list (or vector) of length 336
    return max(0, x[100])
def l540_101(x):
    # x is a list (or vector) of length 336
    return max(0, x[101])
def l540_102(x):
    # x is a list (or vector) of length 336
    return max(0, x[102])
def l540_103(x):
    # x is a list (or vector) of length 336
    return max(0, x[103])
def l540_104(x):
    # x is a list (or vector) of length 336
    return max(0, x[104])
def l540_105(x):
    # x is a list (or vector) of length 336
    return max(0, x[105])
def l540_106(x):
    # x is a list (or vector) of length 336
    return max(0, x[106])
def l540_107(x):
    # x is a list (or vector) of length 336
    return max(0, x[107])
def l540_108(x):
    # x is a list (or vector) of length 336
    return max(0, x[108])
def l540_109(x):
    # x is a list (or vector) of length 336
    return max(0, x[109])
def l540_110(x):
    # x is a list (or vector) of length 336
    return max(0, x[110])
def l540_111(x):
    # x is a list (or vector) of length 336
    return max(0, x[111])
def l540_112(x):
    # x is a list (or vector) of length 336
    return max(0, x[112])
def l540_113(x):
    # x is a list (or vector) of length 336
    return max(0, x[113])
def l540_114(x):
    # x is a list (or vector) of length 336
    return max(0, x[114])
def l540_115(x):
    # x is a list (or vector) of length 336
    return max(0, x[115])
def l540_116(x):
    # x is a list (or vector) of length 336
    return max(0, x[116])
def l540_117(x):
    # x is a list (or vector) of length 336
    return max(0, x[117])
def l540_118(x):
    # x is a list (or vector) of length 336
    return max(0, x[118])
def l540_119(x):
    # x is a list (or vector) of length 336
    return max(0, x[119])
def l540_120(x):
    # x is a list (or vector) of length 336
    return max(0, x[120])
def l540_121(x):
    # x is a list (or vector) of length 336
    return max(0, x[121])
def l540_122(x):
    # x is a list (or vector) of length 336
    return max(0, x[122])
def l540_123(x):
    # x is a list (or vector) of length 336
    return max(0, x[123])
def l540_124(x):
    # x is a list (or vector) of length 336
    return max(0, x[124])
def l540_125(x):
    # x is a list (or vector) of length 336
    return max(0, x[125])
def l540_126(x):
    # x is a list (or vector) of length 336
    return max(0, x[126])
def l540_127(x):
    # x is a list (or vector) of length 336
    return max(0, x[127])
def l540_128(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[128] + -1.0*x[160] + 1.0)
def l540_129(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[129] + -1.0*x[161] + 1.0)
def l540_130(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[130] + -1.0*x[162] + 1.0)
def l540_131(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[131] + -1.0*x[163] + 1.0)
def l540_132(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[132] + -1.0*x[164] + 1.0)
def l540_133(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[133] + -1.0*x[165] + 1.0)
def l540_134(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[134] + -1.0*x[166] + 1.0)
def l540_135(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[135] + -1.0*x[167] + 1.0)
def l540_136(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[136] + -1.0*x[168] + 1.0)
def l540_137(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[137] + -1.0*x[169] + 1.0)
def l540_138(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[138] + -1.0*x[170] + 1.0)
def l540_139(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[139] + -1.0*x[171] + 1.0)
def l540_140(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[140] + -1.0*x[172] + 1.0)
def l540_141(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[141] + -1.0*x[173] + 1.0)
def l540_142(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[142] + -1.0*x[174] + 1.0)
def l540_143(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[143] + -1.0*x[175] + 1.0)
def l540_144(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[144] + -1.0*x[176] + 1.0)
def l540_145(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[145] + -1.0*x[177] + 1.0)
def l540_146(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[146] + -1.0*x[178] + 1.0)
def l540_147(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[147] + -1.0*x[179] + 1.0)
def l540_148(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[148] + -1.0*x[180] + 1.0)
def l540_149(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[149] + -1.0*x[181] + 1.0)
def l540_150(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[150] + -1.0*x[182] + 1.0)
def l540_151(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[151] + -1.0*x[183] + 1.0)
def l540_152(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[152] + -1.0*x[184] + 1.0)
def l540_153(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[153] + -1.0*x[185] + 1.0)
def l540_154(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[154] + -1.0*x[186] + 1.0)
def l540_155(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[155] + -1.0*x[187] + 1.0)
def l540_156(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[156] + -1.0*x[188] + 1.0)
def l540_157(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[157] + -1.0*x[189] + 1.0)
def l540_158(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[158] + -1.0*x[190] + 1.0)
def l540_159(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[159] + -1.0*x[191] + 1.0)
def l540_160(x):
    # x is a list (or vector) of length 336
    return max(0, x[192])
def l540_161(x):
    # x is a list (or vector) of length 336
    return max(0, x[193])
def l540_162(x):
    # x is a list (or vector) of length 336
    return max(0, x[194])
def l540_163(x):
    # x is a list (or vector) of length 336
    return max(0, x[195])
def l540_164(x):
    # x is a list (or vector) of length 336
    return max(0, x[196])
def l540_165(x):
    # x is a list (or vector) of length 336
    return max(0, x[197])
def l540_166(x):
    # x is a list (or vector) of length 336
    return max(0, x[198])
def l540_167(x):
    # x is a list (or vector) of length 336
    return max(0, x[199])
def l540_168(x):
    # x is a list (or vector) of length 336
    return max(0, x[200])
def l540_169(x):
    # x is a list (or vector) of length 336
    return max(0, x[201])
def l540_170(x):
    # x is a list (or vector) of length 336
    return max(0, x[202])
def l540_171(x):
    # x is a list (or vector) of length 336
    return max(0, x[203])
def l540_172(x):
    # x is a list (or vector) of length 336
    return max(0, x[204])
def l540_173(x):
    # x is a list (or vector) of length 336
    return max(0, x[205])
def l540_174(x):
    # x is a list (or vector) of length 336
    return max(0, x[206])
def l540_175(x):
    # x is a list (or vector) of length 336
    return max(0, x[207])
def l540_176(x):
    # x is a list (or vector) of length 336
    return max(0, x[208])
def l540_177(x):
    # x is a list (or vector) of length 336
    return max(0, x[209])
def l540_178(x):
    # x is a list (or vector) of length 336
    return max(0, x[210])
def l540_179(x):
    # x is a list (or vector) of length 336
    return max(0, x[211])
def l540_180(x):
    # x is a list (or vector) of length 336
    return max(0, x[212])
def l540_181(x):
    # x is a list (or vector) of length 336
    return max(0, x[213])
def l540_182(x):
    # x is a list (or vector) of length 336
    return max(0, x[214])
def l540_183(x):
    # x is a list (or vector) of length 336
    return max(0, x[215])
def l540_184(x):
    # x is a list (or vector) of length 336
    return max(0, x[216])
def l540_185(x):
    # x is a list (or vector) of length 336
    return max(0, x[217])
def l540_186(x):
    # x is a list (or vector) of length 336
    return max(0, x[218])
def l540_187(x):
    # x is a list (or vector) of length 336
    return max(0, x[219])
def l540_188(x):
    # x is a list (or vector) of length 336
    return max(0, x[220])
def l540_189(x):
    # x is a list (or vector) of length 336
    return max(0, x[221])
def l540_190(x):
    # x is a list (or vector) of length 336
    return max(0, x[222])
def l540_191(x):
    # x is a list (or vector) of length 336
    return max(0, x[223])
def l540_192(x):
    # x is a list (or vector) of length 336
    return max(0, x[224])
def l540_193(x):
    # x is a list (or vector) of length 336
    return max(0, x[225])
def l540_194(x):
    # x is a list (or vector) of length 336
    return max(0, x[226])
def l540_195(x):
    # x is a list (or vector) of length 336
    return max(0, x[227])
def l540_196(x):
    # x is a list (or vector) of length 336
    return max(0, x[228])
def l540_197(x):
    # x is a list (or vector) of length 336
    return max(0, x[229])
def l540_198(x):
    # x is a list (or vector) of length 336
    return max(0, x[230])
def l540_199(x):
    # x is a list (or vector) of length 336
    return max(0, x[231])
def l540_200(x):
    # x is a list (or vector) of length 336
    return max(0, x[232])
def l540_201(x):
    # x is a list (or vector) of length 336
    return max(0, x[233])
def l540_202(x):
    # x is a list (or vector) of length 336
    return max(0, x[234])
def l540_203(x):
    # x is a list (or vector) of length 336
    return max(0, x[235])
def l540_204(x):
    # x is a list (or vector) of length 336
    return max(0, x[236])
def l540_205(x):
    # x is a list (or vector) of length 336
    return max(0, x[237])
def l540_206(x):
    # x is a list (or vector) of length 336
    return max(0, x[238])
def l540_207(x):
    # x is a list (or vector) of length 336
    return max(0, x[239])
def l540_208(x):
    # x is a list (or vector) of length 336
    return max(0, x[240])
def l540_209(x):
    # x is a list (or vector) of length 336
    return max(0, x[241])
def l540_210(x):
    # x is a list (or vector) of length 336
    return max(0, x[242])
def l540_211(x):
    # x is a list (or vector) of length 336
    return max(0, x[243])
def l540_212(x):
    # x is a list (or vector) of length 336
    return max(0, x[244])
def l540_213(x):
    # x is a list (or vector) of length 336
    return max(0, x[245])
def l540_214(x):
    # x is a list (or vector) of length 336
    return max(0, x[246])
def l540_215(x):
    # x is a list (or vector) of length 336
    return max(0, x[247])
def l540_216(x):
    # x is a list (or vector) of length 336
    return max(0, x[248])
def l540_217(x):
    # x is a list (or vector) of length 336
    return max(0, x[249])
def l540_218(x):
    # x is a list (or vector) of length 336
    return max(0, x[250])
def l540_219(x):
    # x is a list (or vector) of length 336
    return max(0, x[251])
def l540_220(x):
    # x is a list (or vector) of length 336
    return max(0, x[252])
def l540_221(x):
    # x is a list (or vector) of length 336
    return max(0, x[253])
def l540_222(x):
    # x is a list (or vector) of length 336
    return max(0, x[254])
def l540_223(x):
    # x is a list (or vector) of length 336
    return max(0, x[255])
def l540_224(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[256] + 1.0)
def l540_225(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[257] + 1.0)
def l540_226(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[258] + 1.0)
def l540_227(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[259] + 1.0)
def l540_228(x):
    # x is a list (or vector) of length 336
    return max(0, x[260] + -128.0*x[264] + 128.0*x[268])
def l540_229(x):
    # x is a list (or vector) of length 336
    return max(0, x[261] + -128.0*x[265] + 128.0*x[269])
def l540_230(x):
    # x is a list (or vector) of length 336
    return max(0, x[262] + -128.0*x[266] + 128.0*x[270])
def l540_231(x):
    # x is a list (or vector) of length 336
    return max(0, x[263] + -128.0*x[267] + 128.0*x[271])
def l540_232(x):
    # x is a list (or vector) of length 336
    return max(0, x[272])
def l540_233(x):
    # x is a list (or vector) of length 336
    return max(0, x[273])
def l540_234(x):
    # x is a list (or vector) of length 336
    return max(0, x[274])
def l540_235(x):
    # x is a list (or vector) of length 336
    return max(0, x[275])
def l540_236(x):
    # x is a list (or vector) of length 336
    return max(0, x[276])
def l540_237(x):
    # x is a list (or vector) of length 336
    return max(0, x[277])
def l540_238(x):
    # x is a list (or vector) of length 336
    return max(0, x[278])
def l540_239(x):
    # x is a list (or vector) of length 336
    return max(0, x[279])
def l540_240(x):
    # x is a list (or vector) of length 336
    return max(0, x[280])
def l540_241(x):
    # x is a list (or vector) of length 336
    return max(0, x[281])
def l540_242(x):
    # x is a list (or vector) of length 336
    return max(0, x[282])
def l540_243(x):
    # x is a list (or vector) of length 336
    return max(0, x[283])
def l540_244(x):
    # x is a list (or vector) of length 336
    return max(0, x[284])
def l540_245(x):
    # x is a list (or vector) of length 336
    return max(0, x[285])
def l540_246(x):
    # x is a list (or vector) of length 336
    return max(0, x[286])
def l540_247(x):
    # x is a list (or vector) of length 336
    return max(0, x[287])
def l540_248(x):
    # x is a list (or vector) of length 336
    return max(0, x[288])
def l540_249(x):
    # x is a list (or vector) of length 336
    return max(0, x[289])
def l540_250(x):
    # x is a list (or vector) of length 336
    return max(0, x[290])
def l540_251(x):
    # x is a list (or vector) of length 336
    return max(0, x[291])
def l540_252(x):
    # x is a list (or vector) of length 336
    return max(0, x[292])
def l540_253(x):
    # x is a list (or vector) of length 336
    return max(0, x[293])
def l540_254(x):
    # x is a list (or vector) of length 336
    return max(0, x[294])
def l540_255(x):
    # x is a list (or vector) of length 336
    return max(0, x[295])
def l540_256(x):
    # x is a list (or vector) of length 336
    return max(0, x[296])
def l540_257(x):
    # x is a list (or vector) of length 336
    return max(0, x[297])
def l540_258(x):
    # x is a list (or vector) of length 336
    return max(0, x[298])
def l540_259(x):
    # x is a list (or vector) of length 336
    return max(0, x[299])
def l540_260(x):
    # x is a list (or vector) of length 336
    return max(0, x[300])
def l540_261(x):
    # x is a list (or vector) of length 336
    return max(0, x[301])
def l540_262(x):
    # x is a list (or vector) of length 336
    return max(0, x[302])
def l540_263(x):
    # x is a list (or vector) of length 336
    return max(0, x[303])
def l540_264(x):
    # x is a list (or vector) of length 336
    return max(0, x[304])
def l540_265(x):
    # x is a list (or vector) of length 336
    return max(0, x[305])
def l540_266(x):
    # x is a list (or vector) of length 336
    return max(0, x[306])
def l540_267(x):
    # x is a list (or vector) of length 336
    return max(0, x[307])
def l540_268(x):
    # x is a list (or vector) of length 336
    return max(0, x[308])
def l540_269(x):
    # x is a list (or vector) of length 336
    return max(0, x[309])
def l540_270(x):
    # x is a list (or vector) of length 336
    return max(0, x[310])
def l540_271(x):
    # x is a list (or vector) of length 336
    return max(0, x[311])
def l540_272(x):
    # x is a list (or vector) of length 336
    return max(0, x[312])
def l540_273(x):
    # x is a list (or vector) of length 336
    return max(0, x[313])
def l540_274(x):
    # x is a list (or vector) of length 336
    return max(0, x[314])
def l540_275(x):
    # x is a list (or vector) of length 336
    return max(0, x[315])
def l540_276(x):
    # x is a list (or vector) of length 336
    return max(0, x[316])
def l540_277(x):
    # x is a list (or vector) of length 336
    return max(0, x[317])
def l540_278(x):
    # x is a list (or vector) of length 336
    return max(0, x[318])
def l540_279(x):
    # x is a list (or vector) of length 336
    return max(0, x[319])
def l540_280(x):
    # x is a list (or vector) of length 336
    return max(0, x[320])
def l540_281(x):
    # x is a list (or vector) of length 336
    return max(0, x[321])
def l540_282(x):
    # x is a list (or vector) of length 336
    return max(0, x[322])
def l540_283(x):
    # x is a list (or vector) of length 336
    return max(0, x[323])
def l540_284(x):
    # x is a list (or vector) of length 336
    return max(0, x[324])
def l540_285(x):
    # x is a list (or vector) of length 336
    return max(0, x[325])
def l540_286(x):
    # x is a list (or vector) of length 336
    return max(0, x[326])
def l540_287(x):
    # x is a list (or vector) of length 336
    return max(0, x[327])
def l540_288(x):
    # x is a list (or vector) of length 336
    return max(0, x[328])
def l540_289(x):
    # x is a list (or vector) of length 336
    return max(0, x[329])
def l540_290(x):
    # x is a list (or vector) of length 336
    return max(0, x[330])
def l540_291(x):
    # x is a list (or vector) of length 336
    return max(0, x[331])
def l540_292(x):
    # x is a list (or vector) of length 336
    return max(0, x[332])
def l540_293(x):
    # x is a list (or vector) of length 336
    return max(0, x[333])
def l540_294(x):
    # x is a list (or vector) of length 336
    return max(0, x[334])
def l540_295(x):
    # x is a list (or vector) of length 336
    return max(0, x[335])
def l540_(x):
    # x is a list (or vector) of length 336
    return [
        l540_0(x),
        l540_1(x),
        l540_2(x),
        l540_3(x),
        l540_4(x),
        l540_5(x),
        l540_6(x),
        l540_7(x),
        l540_8(x),
        l540_9(x),
        l540_10(x),
        l540_11(x),
        l540_12(x),
        l540_13(x),
        l540_14(x),
        l540_15(x),
        l540_16(x),
        l540_17(x),
        l540_18(x),
        l540_19(x),
        l540_20(x),
        l540_21(x),
        l540_22(x),
        l540_23(x),
        l540_24(x),
        l540_25(x),
        l540_26(x),
        l540_27(x),
        l540_28(x),
        l540_29(x),
        l540_30(x),
        l540_31(x),
        l540_32(x),
        l540_33(x),
        l540_34(x),
        l540_35(x),
        l540_36(x),
        l540_37(x),
        l540_38(x),
        l540_39(x),
        l540_40(x),
        l540_41(x),
        l540_42(x),
        l540_43(x),
        l540_44(x),
        l540_45(x),
        l540_46(x),
        l540_47(x),
        l540_48(x),
        l540_49(x),
        l540_50(x),
        l540_51(x),
        l540_52(x),
        l540_53(x),
        l540_54(x),
        l540_55(x),
        l540_56(x),
        l540_57(x),
        l540_58(x),
        l540_59(x),
        l540_60(x),
        l540_61(x),
        l540_62(x),
        l540_63(x),
        l540_64(x),
        l540_65(x),
        l540_66(x),
        l540_67(x),
        l540_68(x),
        l540_69(x),
        l540_70(x),
        l540_71(x),
        l540_72(x),
        l540_73(x),
        l540_74(x),
        l540_75(x),
        l540_76(x),
        l540_77(x),
        l540_78(x),
        l540_79(x),
        l540_80(x),
        l540_81(x),
        l540_82(x),
        l540_83(x),
        l540_84(x),
        l540_85(x),
        l540_86(x),
        l540_87(x),
        l540_88(x),
        l540_89(x),
        l540_90(x),
        l540_91(x),
        l540_92(x),
        l540_93(x),
        l540_94(x),
        l540_95(x),
        l540_96(x),
        l540_97(x),
        l540_98(x),
        l540_99(x),
        l540_100(x),
        l540_101(x),
        l540_102(x),
        l540_103(x),
        l540_104(x),
        l540_105(x),
        l540_106(x),
        l540_107(x),
        l540_108(x),
        l540_109(x),
        l540_110(x),
        l540_111(x),
        l540_112(x),
        l540_113(x),
        l540_114(x),
        l540_115(x),
        l540_116(x),
        l540_117(x),
        l540_118(x),
        l540_119(x),
        l540_120(x),
        l540_121(x),
        l540_122(x),
        l540_123(x),
        l540_124(x),
        l540_125(x),
        l540_126(x),
        l540_127(x),
        l540_128(x),
        l540_129(x),
        l540_130(x),
        l540_131(x),
        l540_132(x),
        l540_133(x),
        l540_134(x),
        l540_135(x),
        l540_136(x),
        l540_137(x),
        l540_138(x),
        l540_139(x),
        l540_140(x),
        l540_141(x),
        l540_142(x),
        l540_143(x),
        l540_144(x),
        l540_145(x),
        l540_146(x),
        l540_147(x),
        l540_148(x),
        l540_149(x),
        l540_150(x),
        l540_151(x),
        l540_152(x),
        l540_153(x),
        l540_154(x),
        l540_155(x),
        l540_156(x),
        l540_157(x),
        l540_158(x),
        l540_159(x),
        l540_160(x),
        l540_161(x),
        l540_162(x),
        l540_163(x),
        l540_164(x),
        l540_165(x),
        l540_166(x),
        l540_167(x),
        l540_168(x),
        l540_169(x),
        l540_170(x),
        l540_171(x),
        l540_172(x),
        l540_173(x),
        l540_174(x),
        l540_175(x),
        l540_176(x),
        l540_177(x),
        l540_178(x),
        l540_179(x),
        l540_180(x),
        l540_181(x),
        l540_182(x),
        l540_183(x),
        l540_184(x),
        l540_185(x),
        l540_186(x),
        l540_187(x),
        l540_188(x),
        l540_189(x),
        l540_190(x),
        l540_191(x),
        l540_192(x),
        l540_193(x),
        l540_194(x),
        l540_195(x),
        l540_196(x),
        l540_197(x),
        l540_198(x),
        l540_199(x),
        l540_200(x),
        l540_201(x),
        l540_202(x),
        l540_203(x),
        l540_204(x),
        l540_205(x),
        l540_206(x),
        l540_207(x),
        l540_208(x),
        l540_209(x),
        l540_210(x),
        l540_211(x),
        l540_212(x),
        l540_213(x),
        l540_214(x),
        l540_215(x),
        l540_216(x),
        l540_217(x),
        l540_218(x),
        l540_219(x),
        l540_220(x),
        l540_221(x),
        l540_222(x),
        l540_223(x),
        l540_224(x),
        l540_225(x),
        l540_226(x),
        l540_227(x),
        l540_228(x),
        l540_229(x),
        l540_230(x),
        l540_231(x),
        l540_232(x),
        l540_233(x),
        l540_234(x),
        l540_235(x),
        l540_236(x),
        l540_237(x),
        l540_238(x),
        l540_239(x),
        l540_240(x),
        l540_241(x),
        l540_242(x),
        l540_243(x),
        l540_244(x),
        l540_245(x),
        l540_246(x),
        l540_247(x),
        l540_248(x),
        l540_249(x),
        l540_250(x),
        l540_251(x),
        l540_252(x),
        l540_253(x),
        l540_254(x),
        l540_255(x),
        l540_256(x),
        l540_257(x),
        l540_258(x),
        l540_259(x),
        l540_260(x),
        l540_261(x),
        l540_262(x),
        l540_263(x),
        l540_264(x),
        l540_265(x),
        l540_266(x),
        l540_267(x),
        l540_268(x),
        l540_269(x),
        l540_270(x),
        l540_271(x),
        l540_272(x),
        l540_273(x),
        l540_274(x),
        l540_275(x),
        l540_276(x),
        l540_277(x),
        l540_278(x),
        l540_279(x),
        l540_280(x),
        l540_281(x),
        l540_282(x),
        l540_283(x),
        l540_284(x),
        l540_285(x),
        l540_286(x),
        l540_287(x),
        l540_288(x),
        l540_289(x),
        l540_290(x),
        l540_291(x),
        l540_292(x),
        l540_293(x),
        l540_294(x),
        l540_295(x),
    ]