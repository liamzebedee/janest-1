import numpy as np




# Generated from reverse engineering
def l372_g(x: np.ndarray) -> np.ndarray:
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




def l372_0(x):
    # x is a list (or vector) of length 336
    return max(0, x[0])
def l372_1(x):
    # x is a list (or vector) of length 336
    return max(0, x[1])
def l372_2(x):
    # x is a list (or vector) of length 336
    return max(0, x[2])
def l372_3(x):
    # x is a list (or vector) of length 336
    return max(0, x[3])
def l372_4(x):
    # x is a list (or vector) of length 336
    return max(0, x[4])
def l372_5(x):
    # x is a list (or vector) of length 336
    return max(0, x[5])
def l372_6(x):
    # x is a list (or vector) of length 336
    return max(0, x[6])
def l372_7(x):
    # x is a list (or vector) of length 336
    return max(0, x[7])
def l372_8(x):
    # x is a list (or vector) of length 336
    return max(0, x[8])
def l372_9(x):
    # x is a list (or vector) of length 336
    return max(0, x[9])
def l372_10(x):
    # x is a list (or vector) of length 336
    return max(0, x[10])
def l372_11(x):
    # x is a list (or vector) of length 336
    return max(0, x[11])
def l372_12(x):
    # x is a list (or vector) of length 336
    return max(0, x[12])
def l372_13(x):
    # x is a list (or vector) of length 336
    return max(0, x[13])
def l372_14(x):
    # x is a list (or vector) of length 336
    return max(0, x[14])
def l372_15(x):
    # x is a list (or vector) of length 336
    return max(0, x[15])
def l372_16(x):
    # x is a list (or vector) of length 336
    return max(0, x[16])
def l372_17(x):
    # x is a list (or vector) of length 336
    return max(0, x[17])
def l372_18(x):
    # x is a list (or vector) of length 336
    return max(0, x[18])
def l372_19(x):
    # x is a list (or vector) of length 336
    return max(0, x[19])
def l372_20(x):
    # x is a list (or vector) of length 336
    return max(0, x[20])
def l372_21(x):
    # x is a list (or vector) of length 336
    return max(0, x[21])
def l372_22(x):
    # x is a list (or vector) of length 336
    return max(0, x[22])
def l372_23(x):
    # x is a list (or vector) of length 336
    return max(0, x[23])
def l372_24(x):
    # x is a list (or vector) of length 336
    return max(0, x[24])
def l372_25(x):
    # x is a list (or vector) of length 336
    return max(0, x[25])
def l372_26(x):
    # x is a list (or vector) of length 336
    return max(0, x[26])
def l372_27(x):
    # x is a list (or vector) of length 336
    return max(0, x[27])
def l372_28(x):
    # x is a list (or vector) of length 336
    return max(0, x[28])
def l372_29(x):
    # x is a list (or vector) of length 336
    return max(0, x[29])
def l372_30(x):
    # x is a list (or vector) of length 336
    return max(0, x[30])
def l372_31(x):
    # x is a list (or vector) of length 336
    return max(0, x[31])
def l372_32(x):
    # x is a list (or vector) of length 336
    return max(0, x[32])
def l372_33(x):
    # x is a list (or vector) of length 336
    return max(0, x[33])
def l372_34(x):
    # x is a list (or vector) of length 336
    return max(0, x[34])
def l372_35(x):
    # x is a list (or vector) of length 336
    return max(0, x[35])
def l372_36(x):
    # x is a list (or vector) of length 336
    return max(0, x[36])
def l372_37(x):
    # x is a list (or vector) of length 336
    return max(0, x[37])
def l372_38(x):
    # x is a list (or vector) of length 336
    return max(0, x[38])
def l372_39(x):
    # x is a list (or vector) of length 336
    return max(0, x[39])
def l372_40(x):
    # x is a list (or vector) of length 336
    return max(0, x[40])
def l372_41(x):
    # x is a list (or vector) of length 336
    return max(0, x[41])
def l372_42(x):
    # x is a list (or vector) of length 336
    return max(0, x[42])
def l372_43(x):
    # x is a list (or vector) of length 336
    return max(0, x[43])
def l372_44(x):
    # x is a list (or vector) of length 336
    return max(0, x[44])
def l372_45(x):
    # x is a list (or vector) of length 336
    return max(0, x[45])
def l372_46(x):
    # x is a list (or vector) of length 336
    return max(0, x[46])
def l372_47(x):
    # x is a list (or vector) of length 336
    return max(0, x[47])
def l372_48(x):
    # x is a list (or vector) of length 336
    return max(0, x[48])
def l372_49(x):
    # x is a list (or vector) of length 336
    return max(0, x[49])
def l372_50(x):
    # x is a list (or vector) of length 336
    return max(0, x[50])
def l372_51(x):
    # x is a list (or vector) of length 336
    return max(0, x[51])
def l372_52(x):
    # x is a list (or vector) of length 336
    return max(0, x[52])
def l372_53(x):
    # x is a list (or vector) of length 336
    return max(0, x[53])
def l372_54(x):
    # x is a list (or vector) of length 336
    return max(0, x[54])
def l372_55(x):
    # x is a list (or vector) of length 336
    return max(0, x[55])
def l372_56(x):
    # x is a list (or vector) of length 336
    return max(0, x[56])
def l372_57(x):
    # x is a list (or vector) of length 336
    return max(0, x[57])
def l372_58(x):
    # x is a list (or vector) of length 336
    return max(0, x[58])
def l372_59(x):
    # x is a list (or vector) of length 336
    return max(0, x[59])
def l372_60(x):
    # x is a list (or vector) of length 336
    return max(0, x[60])
def l372_61(x):
    # x is a list (or vector) of length 336
    return max(0, x[61])
def l372_62(x):
    # x is a list (or vector) of length 336
    return max(0, x[62])
def l372_63(x):
    # x is a list (or vector) of length 336
    return max(0, x[63])
def l372_64(x):
    # x is a list (or vector) of length 336
    return max(0, x[64])
def l372_65(x):
    # x is a list (or vector) of length 336
    return max(0, x[65])
def l372_66(x):
    # x is a list (or vector) of length 336
    return max(0, x[66])
def l372_67(x):
    # x is a list (or vector) of length 336
    return max(0, x[67])
def l372_68(x):
    # x is a list (or vector) of length 336
    return max(0, x[68])
def l372_69(x):
    # x is a list (or vector) of length 336
    return max(0, x[69])
def l372_70(x):
    # x is a list (or vector) of length 336
    return max(0, x[70])
def l372_71(x):
    # x is a list (or vector) of length 336
    return max(0, x[71])
def l372_72(x):
    # x is a list (or vector) of length 336
    return max(0, x[72])
def l372_73(x):
    # x is a list (or vector) of length 336
    return max(0, x[73])
def l372_74(x):
    # x is a list (or vector) of length 336
    return max(0, x[74])
def l372_75(x):
    # x is a list (or vector) of length 336
    return max(0, x[75])
def l372_76(x):
    # x is a list (or vector) of length 336
    return max(0, x[76])
def l372_77(x):
    # x is a list (or vector) of length 336
    return max(0, x[77])
def l372_78(x):
    # x is a list (or vector) of length 336
    return max(0, x[78])
def l372_79(x):
    # x is a list (or vector) of length 336
    return max(0, x[79])
def l372_80(x):
    # x is a list (or vector) of length 336
    return max(0, x[80])
def l372_81(x):
    # x is a list (or vector) of length 336
    return max(0, x[81])
def l372_82(x):
    # x is a list (or vector) of length 336
    return max(0, x[82])
def l372_83(x):
    # x is a list (or vector) of length 336
    return max(0, x[83])
def l372_84(x):
    # x is a list (or vector) of length 336
    return max(0, x[84])
def l372_85(x):
    # x is a list (or vector) of length 336
    return max(0, x[85])
def l372_86(x):
    # x is a list (or vector) of length 336
    return max(0, x[86])
def l372_87(x):
    # x is a list (or vector) of length 336
    return max(0, x[87])
def l372_88(x):
    # x is a list (or vector) of length 336
    return max(0, x[88])
def l372_89(x):
    # x is a list (or vector) of length 336
    return max(0, x[89])
def l372_90(x):
    # x is a list (or vector) of length 336
    return max(0, x[90])
def l372_91(x):
    # x is a list (or vector) of length 336
    return max(0, x[91])
def l372_92(x):
    # x is a list (or vector) of length 336
    return max(0, x[92])
def l372_93(x):
    # x is a list (or vector) of length 336
    return max(0, x[93])
def l372_94(x):
    # x is a list (or vector) of length 336
    return max(0, x[94])
def l372_95(x):
    # x is a list (or vector) of length 336
    return max(0, x[95])
def l372_96(x):
    # x is a list (or vector) of length 336
    return max(0, x[96])
def l372_97(x):
    # x is a list (or vector) of length 336
    return max(0, x[97])
def l372_98(x):
    # x is a list (or vector) of length 336
    return max(0, x[98])
def l372_99(x):
    # x is a list (or vector) of length 336
    return max(0, x[99])
def l372_100(x):
    # x is a list (or vector) of length 336
    return max(0, x[100])
def l372_101(x):
    # x is a list (or vector) of length 336
    return max(0, x[101])
def l372_102(x):
    # x is a list (or vector) of length 336
    return max(0, x[102])
def l372_103(x):
    # x is a list (or vector) of length 336
    return max(0, x[103])
def l372_104(x):
    # x is a list (or vector) of length 336
    return max(0, x[104])
def l372_105(x):
    # x is a list (or vector) of length 336
    return max(0, x[105])
def l372_106(x):
    # x is a list (or vector) of length 336
    return max(0, x[106])
def l372_107(x):
    # x is a list (or vector) of length 336
    return max(0, x[107])
def l372_108(x):
    # x is a list (or vector) of length 336
    return max(0, x[108])
def l372_109(x):
    # x is a list (or vector) of length 336
    return max(0, x[109])
def l372_110(x):
    # x is a list (or vector) of length 336
    return max(0, x[110])
def l372_111(x):
    # x is a list (or vector) of length 336
    return max(0, x[111])
def l372_112(x):
    # x is a list (or vector) of length 336
    return max(0, x[112])
def l372_113(x):
    # x is a list (or vector) of length 336
    return max(0, x[113])
def l372_114(x):
    # x is a list (or vector) of length 336
    return max(0, x[114])
def l372_115(x):
    # x is a list (or vector) of length 336
    return max(0, x[115])
def l372_116(x):
    # x is a list (or vector) of length 336
    return max(0, x[116])
def l372_117(x):
    # x is a list (or vector) of length 336
    return max(0, x[117])
def l372_118(x):
    # x is a list (or vector) of length 336
    return max(0, x[118])
def l372_119(x):
    # x is a list (or vector) of length 336
    return max(0, x[119])
def l372_120(x):
    # x is a list (or vector) of length 336
    return max(0, x[120])
def l372_121(x):
    # x is a list (or vector) of length 336
    return max(0, x[121])
def l372_122(x):
    # x is a list (or vector) of length 336
    return max(0, x[122])
def l372_123(x):
    # x is a list (or vector) of length 336
    return max(0, x[123])
def l372_124(x):
    # x is a list (or vector) of length 336
    return max(0, x[124])
def l372_125(x):
    # x is a list (or vector) of length 336
    return max(0, x[125])
def l372_126(x):
    # x is a list (or vector) of length 336
    return max(0, x[126])
def l372_127(x):
    # x is a list (or vector) of length 336
    return max(0, x[127])
def l372_128(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[128] + -1.0*x[160] + 1.0)
def l372_129(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[129] + -1.0*x[161] + 1.0)
def l372_130(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[130] + -1.0*x[162] + 1.0)
def l372_131(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[131] + -1.0*x[163] + 1.0)
def l372_132(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[132] + -1.0*x[164] + 1.0)
def l372_133(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[133] + -1.0*x[165] + 1.0)
def l372_134(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[134] + -1.0*x[166] + 1.0)
def l372_135(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[135] + -1.0*x[167] + 1.0)
def l372_136(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[136] + -1.0*x[168] + 1.0)
def l372_137(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[137] + -1.0*x[169] + 1.0)
def l372_138(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[138] + -1.0*x[170] + 1.0)
def l372_139(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[139] + -1.0*x[171] + 1.0)
def l372_140(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[140] + -1.0*x[172] + 1.0)
def l372_141(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[141] + -1.0*x[173] + 1.0)
def l372_142(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[142] + -1.0*x[174] + 1.0)
def l372_143(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[143] + -1.0*x[175] + 1.0)
def l372_144(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[144] + -1.0*x[176] + 1.0)
def l372_145(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[145] + -1.0*x[177] + 1.0)
def l372_146(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[146] + -1.0*x[178] + 1.0)
def l372_147(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[147] + -1.0*x[179] + 1.0)
def l372_148(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[148] + -1.0*x[180] + 1.0)
def l372_149(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[149] + -1.0*x[181] + 1.0)
def l372_150(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[150] + -1.0*x[182] + 1.0)
def l372_151(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[151] + -1.0*x[183] + 1.0)
def l372_152(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[152] + -1.0*x[184] + 1.0)
def l372_153(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[153] + -1.0*x[185] + 1.0)
def l372_154(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[154] + -1.0*x[186] + 1.0)
def l372_155(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[155] + -1.0*x[187] + 1.0)
def l372_156(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[156] + -1.0*x[188] + 1.0)
def l372_157(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[157] + -1.0*x[189] + 1.0)
def l372_158(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[158] + -1.0*x[190] + 1.0)
def l372_159(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[159] + -1.0*x[191] + 1.0)
def l372_160(x):
    # x is a list (or vector) of length 336
    return max(0, x[192])
def l372_161(x):
    # x is a list (or vector) of length 336
    return max(0, x[193])
def l372_162(x):
    # x is a list (or vector) of length 336
    return max(0, x[194])
def l372_163(x):
    # x is a list (or vector) of length 336
    return max(0, x[195])
def l372_164(x):
    # x is a list (or vector) of length 336
    return max(0, x[196])
def l372_165(x):
    # x is a list (or vector) of length 336
    return max(0, x[197])
def l372_166(x):
    # x is a list (or vector) of length 336
    return max(0, x[198])
def l372_167(x):
    # x is a list (or vector) of length 336
    return max(0, x[199])
def l372_168(x):
    # x is a list (or vector) of length 336
    return max(0, x[200])
def l372_169(x):
    # x is a list (or vector) of length 336
    return max(0, x[201])
def l372_170(x):
    # x is a list (or vector) of length 336
    return max(0, x[202])
def l372_171(x):
    # x is a list (or vector) of length 336
    return max(0, x[203])
def l372_172(x):
    # x is a list (or vector) of length 336
    return max(0, x[204])
def l372_173(x):
    # x is a list (or vector) of length 336
    return max(0, x[205])
def l372_174(x):
    # x is a list (or vector) of length 336
    return max(0, x[206])
def l372_175(x):
    # x is a list (or vector) of length 336
    return max(0, x[207])
def l372_176(x):
    # x is a list (or vector) of length 336
    return max(0, x[208])
def l372_177(x):
    # x is a list (or vector) of length 336
    return max(0, x[209])
def l372_178(x):
    # x is a list (or vector) of length 336
    return max(0, x[210])
def l372_179(x):
    # x is a list (or vector) of length 336
    return max(0, x[211])
def l372_180(x):
    # x is a list (or vector) of length 336
    return max(0, x[212])
def l372_181(x):
    # x is a list (or vector) of length 336
    return max(0, x[213])
def l372_182(x):
    # x is a list (or vector) of length 336
    return max(0, x[214])
def l372_183(x):
    # x is a list (or vector) of length 336
    return max(0, x[215])
def l372_184(x):
    # x is a list (or vector) of length 336
    return max(0, x[216])
def l372_185(x):
    # x is a list (or vector) of length 336
    return max(0, x[217])
def l372_186(x):
    # x is a list (or vector) of length 336
    return max(0, x[218])
def l372_187(x):
    # x is a list (or vector) of length 336
    return max(0, x[219])
def l372_188(x):
    # x is a list (or vector) of length 336
    return max(0, x[220])
def l372_189(x):
    # x is a list (or vector) of length 336
    return max(0, x[221])
def l372_190(x):
    # x is a list (or vector) of length 336
    return max(0, x[222])
def l372_191(x):
    # x is a list (or vector) of length 336
    return max(0, x[223])
def l372_192(x):
    # x is a list (or vector) of length 336
    return max(0, x[224])
def l372_193(x):
    # x is a list (or vector) of length 336
    return max(0, x[225])
def l372_194(x):
    # x is a list (or vector) of length 336
    return max(0, x[226])
def l372_195(x):
    # x is a list (or vector) of length 336
    return max(0, x[227])
def l372_196(x):
    # x is a list (or vector) of length 336
    return max(0, x[228])
def l372_197(x):
    # x is a list (or vector) of length 336
    return max(0, x[229])
def l372_198(x):
    # x is a list (or vector) of length 336
    return max(0, x[230])
def l372_199(x):
    # x is a list (or vector) of length 336
    return max(0, x[231])
def l372_200(x):
    # x is a list (or vector) of length 336
    return max(0, x[232])
def l372_201(x):
    # x is a list (or vector) of length 336
    return max(0, x[233])
def l372_202(x):
    # x is a list (or vector) of length 336
    return max(0, x[234])
def l372_203(x):
    # x is a list (or vector) of length 336
    return max(0, x[235])
def l372_204(x):
    # x is a list (or vector) of length 336
    return max(0, x[236])
def l372_205(x):
    # x is a list (or vector) of length 336
    return max(0, x[237])
def l372_206(x):
    # x is a list (or vector) of length 336
    return max(0, x[238])
def l372_207(x):
    # x is a list (or vector) of length 336
    return max(0, x[239])
def l372_208(x):
    # x is a list (or vector) of length 336
    return max(0, x[240])
def l372_209(x):
    # x is a list (or vector) of length 336
    return max(0, x[241])
def l372_210(x):
    # x is a list (or vector) of length 336
    return max(0, x[242])
def l372_211(x):
    # x is a list (or vector) of length 336
    return max(0, x[243])
def l372_212(x):
    # x is a list (or vector) of length 336
    return max(0, x[244])
def l372_213(x):
    # x is a list (or vector) of length 336
    return max(0, x[245])
def l372_214(x):
    # x is a list (or vector) of length 336
    return max(0, x[246])
def l372_215(x):
    # x is a list (or vector) of length 336
    return max(0, x[247])
def l372_216(x):
    # x is a list (or vector) of length 336
    return max(0, x[248])
def l372_217(x):
    # x is a list (or vector) of length 336
    return max(0, x[249])
def l372_218(x):
    # x is a list (or vector) of length 336
    return max(0, x[250])
def l372_219(x):
    # x is a list (or vector) of length 336
    return max(0, x[251])
def l372_220(x):
    # x is a list (or vector) of length 336
    return max(0, x[252])
def l372_221(x):
    # x is a list (or vector) of length 336
    return max(0, x[253])
def l372_222(x):
    # x is a list (or vector) of length 336
    return max(0, x[254])
def l372_223(x):
    # x is a list (or vector) of length 336
    return max(0, x[255])
def l372_224(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[256] + 1.0)
def l372_225(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[257] + 1.0)
def l372_226(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[258] + 1.0)
def l372_227(x):
    # x is a list (or vector) of length 336
    return max(0, -1.0*x[259] + 1.0)
def l372_228(x):
    # x is a list (or vector) of length 336
    return max(0, x[260] + -128.0*x[264] + 128.0*x[268])
def l372_229(x):
    # x is a list (or vector) of length 336
    return max(0, x[261] + -128.0*x[265] + 128.0*x[269])
def l372_230(x):
    # x is a list (or vector) of length 336
    return max(0, x[262] + -128.0*x[266] + 128.0*x[270])
def l372_231(x):
    # x is a list (or vector) of length 336
    return max(0, x[263] + -128.0*x[267] + 128.0*x[271])
def l372_232(x):
    # x is a list (or vector) of length 336
    return max(0, x[272])
def l372_233(x):
    # x is a list (or vector) of length 336
    return max(0, x[273])
def l372_234(x):
    # x is a list (or vector) of length 336
    return max(0, x[274])
def l372_235(x):
    # x is a list (or vector) of length 336
    return max(0, x[275])
def l372_236(x):
    # x is a list (or vector) of length 336
    return max(0, x[276])
def l372_237(x):
    # x is a list (or vector) of length 336
    return max(0, x[277])
def l372_238(x):
    # x is a list (or vector) of length 336
    return max(0, x[278])
def l372_239(x):
    # x is a list (or vector) of length 336
    return max(0, x[279])
def l372_240(x):
    # x is a list (or vector) of length 336
    return max(0, x[280])
def l372_241(x):
    # x is a list (or vector) of length 336
    return max(0, x[281])
def l372_242(x):
    # x is a list (or vector) of length 336
    return max(0, x[282])
def l372_243(x):
    # x is a list (or vector) of length 336
    return max(0, x[283])
def l372_244(x):
    # x is a list (or vector) of length 336
    return max(0, x[284])
def l372_245(x):
    # x is a list (or vector) of length 336
    return max(0, x[285])
def l372_246(x):
    # x is a list (or vector) of length 336
    return max(0, x[286])
def l372_247(x):
    # x is a list (or vector) of length 336
    return max(0, x[287])
def l372_248(x):
    # x is a list (or vector) of length 336
    return max(0, x[288])
def l372_249(x):
    # x is a list (or vector) of length 336
    return max(0, x[289])
def l372_250(x):
    # x is a list (or vector) of length 336
    return max(0, x[290])
def l372_251(x):
    # x is a list (or vector) of length 336
    return max(0, x[291])
def l372_252(x):
    # x is a list (or vector) of length 336
    return max(0, x[292])
def l372_253(x):
    # x is a list (or vector) of length 336
    return max(0, x[293])
def l372_254(x):
    # x is a list (or vector) of length 336
    return max(0, x[294])
def l372_255(x):
    # x is a list (or vector) of length 336
    return max(0, x[295])
def l372_256(x):
    # x is a list (or vector) of length 336
    return max(0, x[296])
def l372_257(x):
    # x is a list (or vector) of length 336
    return max(0, x[297])
def l372_258(x):
    # x is a list (or vector) of length 336
    return max(0, x[298])
def l372_259(x):
    # x is a list (or vector) of length 336
    return max(0, x[299])
def l372_260(x):
    # x is a list (or vector) of length 336
    return max(0, x[300])
def l372_261(x):
    # x is a list (or vector) of length 336
    return max(0, x[301])
def l372_262(x):
    # x is a list (or vector) of length 336
    return max(0, x[302])
def l372_263(x):
    # x is a list (or vector) of length 336
    return max(0, x[303])
def l372_264(x):
    # x is a list (or vector) of length 336
    return max(0, x[304])
def l372_265(x):
    # x is a list (or vector) of length 336
    return max(0, x[305])
def l372_266(x):
    # x is a list (or vector) of length 336
    return max(0, x[306])
def l372_267(x):
    # x is a list (or vector) of length 336
    return max(0, x[307])
def l372_268(x):
    # x is a list (or vector) of length 336
    return max(0, x[308])
def l372_269(x):
    # x is a list (or vector) of length 336
    return max(0, x[309])
def l372_270(x):
    # x is a list (or vector) of length 336
    return max(0, x[310])
def l372_271(x):
    # x is a list (or vector) of length 336
    return max(0, x[311])
def l372_272(x):
    # x is a list (or vector) of length 336
    return max(0, x[312])
def l372_273(x):
    # x is a list (or vector) of length 336
    return max(0, x[313])
def l372_274(x):
    # x is a list (or vector) of length 336
    return max(0, x[314])
def l372_275(x):
    # x is a list (or vector) of length 336
    return max(0, x[315])
def l372_276(x):
    # x is a list (or vector) of length 336
    return max(0, x[316])
def l372_277(x):
    # x is a list (or vector) of length 336
    return max(0, x[317])
def l372_278(x):
    # x is a list (or vector) of length 336
    return max(0, x[318])
def l372_279(x):
    # x is a list (or vector) of length 336
    return max(0, x[319])
def l372_280(x):
    # x is a list (or vector) of length 336
    return max(0, x[320])
def l372_281(x):
    # x is a list (or vector) of length 336
    return max(0, x[321])
def l372_282(x):
    # x is a list (or vector) of length 336
    return max(0, x[322])
def l372_283(x):
    # x is a list (or vector) of length 336
    return max(0, x[323])
def l372_284(x):
    # x is a list (or vector) of length 336
    return max(0, x[324])
def l372_285(x):
    # x is a list (or vector) of length 336
    return max(0, x[325])
def l372_286(x):
    # x is a list (or vector) of length 336
    return max(0, x[326])
def l372_287(x):
    # x is a list (or vector) of length 336
    return max(0, x[327])
def l372_288(x):
    # x is a list (or vector) of length 336
    return max(0, x[328])
def l372_289(x):
    # x is a list (or vector) of length 336
    return max(0, x[329])
def l372_290(x):
    # x is a list (or vector) of length 336
    return max(0, x[330])
def l372_291(x):
    # x is a list (or vector) of length 336
    return max(0, x[331])
def l372_292(x):
    # x is a list (or vector) of length 336
    return max(0, x[332])
def l372_293(x):
    # x is a list (or vector) of length 336
    return max(0, x[333])
def l372_294(x):
    # x is a list (or vector) of length 336
    return max(0, x[334])
def l372_295(x):
    # x is a list (or vector) of length 336
    return max(0, x[335])
def l372_(x):
    # x is a list (or vector) of length 336
    return [
        l372_0(x),
        l372_1(x),
        l372_2(x),
        l372_3(x),
        l372_4(x),
        l372_5(x),
        l372_6(x),
        l372_7(x),
        l372_8(x),
        l372_9(x),
        l372_10(x),
        l372_11(x),
        l372_12(x),
        l372_13(x),
        l372_14(x),
        l372_15(x),
        l372_16(x),
        l372_17(x),
        l372_18(x),
        l372_19(x),
        l372_20(x),
        l372_21(x),
        l372_22(x),
        l372_23(x),
        l372_24(x),
        l372_25(x),
        l372_26(x),
        l372_27(x),
        l372_28(x),
        l372_29(x),
        l372_30(x),
        l372_31(x),
        l372_32(x),
        l372_33(x),
        l372_34(x),
        l372_35(x),
        l372_36(x),
        l372_37(x),
        l372_38(x),
        l372_39(x),
        l372_40(x),
        l372_41(x),
        l372_42(x),
        l372_43(x),
        l372_44(x),
        l372_45(x),
        l372_46(x),
        l372_47(x),
        l372_48(x),
        l372_49(x),
        l372_50(x),
        l372_51(x),
        l372_52(x),
        l372_53(x),
        l372_54(x),
        l372_55(x),
        l372_56(x),
        l372_57(x),
        l372_58(x),
        l372_59(x),
        l372_60(x),
        l372_61(x),
        l372_62(x),
        l372_63(x),
        l372_64(x),
        l372_65(x),
        l372_66(x),
        l372_67(x),
        l372_68(x),
        l372_69(x),
        l372_70(x),
        l372_71(x),
        l372_72(x),
        l372_73(x),
        l372_74(x),
        l372_75(x),
        l372_76(x),
        l372_77(x),
        l372_78(x),
        l372_79(x),
        l372_80(x),
        l372_81(x),
        l372_82(x),
        l372_83(x),
        l372_84(x),
        l372_85(x),
        l372_86(x),
        l372_87(x),
        l372_88(x),
        l372_89(x),
        l372_90(x),
        l372_91(x),
        l372_92(x),
        l372_93(x),
        l372_94(x),
        l372_95(x),
        l372_96(x),
        l372_97(x),
        l372_98(x),
        l372_99(x),
        l372_100(x),
        l372_101(x),
        l372_102(x),
        l372_103(x),
        l372_104(x),
        l372_105(x),
        l372_106(x),
        l372_107(x),
        l372_108(x),
        l372_109(x),
        l372_110(x),
        l372_111(x),
        l372_112(x),
        l372_113(x),
        l372_114(x),
        l372_115(x),
        l372_116(x),
        l372_117(x),
        l372_118(x),
        l372_119(x),
        l372_120(x),
        l372_121(x),
        l372_122(x),
        l372_123(x),
        l372_124(x),
        l372_125(x),
        l372_126(x),
        l372_127(x),
        l372_128(x),
        l372_129(x),
        l372_130(x),
        l372_131(x),
        l372_132(x),
        l372_133(x),
        l372_134(x),
        l372_135(x),
        l372_136(x),
        l372_137(x),
        l372_138(x),
        l372_139(x),
        l372_140(x),
        l372_141(x),
        l372_142(x),
        l372_143(x),
        l372_144(x),
        l372_145(x),
        l372_146(x),
        l372_147(x),
        l372_148(x),
        l372_149(x),
        l372_150(x),
        l372_151(x),
        l372_152(x),
        l372_153(x),
        l372_154(x),
        l372_155(x),
        l372_156(x),
        l372_157(x),
        l372_158(x),
        l372_159(x),
        l372_160(x),
        l372_161(x),
        l372_162(x),
        l372_163(x),
        l372_164(x),
        l372_165(x),
        l372_166(x),
        l372_167(x),
        l372_168(x),
        l372_169(x),
        l372_170(x),
        l372_171(x),
        l372_172(x),
        l372_173(x),
        l372_174(x),
        l372_175(x),
        l372_176(x),
        l372_177(x),
        l372_178(x),
        l372_179(x),
        l372_180(x),
        l372_181(x),
        l372_182(x),
        l372_183(x),
        l372_184(x),
        l372_185(x),
        l372_186(x),
        l372_187(x),
        l372_188(x),
        l372_189(x),
        l372_190(x),
        l372_191(x),
        l372_192(x),
        l372_193(x),
        l372_194(x),
        l372_195(x),
        l372_196(x),
        l372_197(x),
        l372_198(x),
        l372_199(x),
        l372_200(x),
        l372_201(x),
        l372_202(x),
        l372_203(x),
        l372_204(x),
        l372_205(x),
        l372_206(x),
        l372_207(x),
        l372_208(x),
        l372_209(x),
        l372_210(x),
        l372_211(x),
        l372_212(x),
        l372_213(x),
        l372_214(x),
        l372_215(x),
        l372_216(x),
        l372_217(x),
        l372_218(x),
        l372_219(x),
        l372_220(x),
        l372_221(x),
        l372_222(x),
        l372_223(x),
        l372_224(x),
        l372_225(x),
        l372_226(x),
        l372_227(x),
        l372_228(x),
        l372_229(x),
        l372_230(x),
        l372_231(x),
        l372_232(x),
        l372_233(x),
        l372_234(x),
        l372_235(x),
        l372_236(x),
        l372_237(x),
        l372_238(x),
        l372_239(x),
        l372_240(x),
        l372_241(x),
        l372_242(x),
        l372_243(x),
        l372_244(x),
        l372_245(x),
        l372_246(x),
        l372_247(x),
        l372_248(x),
        l372_249(x),
        l372_250(x),
        l372_251(x),
        l372_252(x),
        l372_253(x),
        l372_254(x),
        l372_255(x),
        l372_256(x),
        l372_257(x),
        l372_258(x),
        l372_259(x),
        l372_260(x),
        l372_261(x),
        l372_262(x),
        l372_263(x),
        l372_264(x),
        l372_265(x),
        l372_266(x),
        l372_267(x),
        l372_268(x),
        l372_269(x),
        l372_270(x),
        l372_271(x),
        l372_272(x),
        l372_273(x),
        l372_274(x),
        l372_275(x),
        l372_276(x),
        l372_277(x),
        l372_278(x),
        l372_279(x),
        l372_280(x),
        l372_281(x),
        l372_282(x),
        l372_283(x),
        l372_284(x),
        l372_285(x),
        l372_286(x),
        l372_287(x),
        l372_288(x),
        l372_289(x),
        l372_290(x),
        l372_291(x),
        l372_292(x),
        l372_293(x),
        l372_294(x),
        l372_295(x),
    ]