import numpy as np




# Generated from reverse engineering
def l530_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 288
    out = np.empty(288, dtype=np.float32)
    
    # for i in range(0, 40):
    for i in range(0, 40):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffffff (len=24)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(40, 64):
    for i in range(0, 24):
        s = -1 * x[40 + i] + -1 * x[64 + i]
        s += biases[i]
        out[40 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 72):
    for i in range(0, 8):
        s = x[112 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(72, 96):
    for i in range(0, 24):
        s = x[88 + i]
        out[72 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 288):
    for i in range(0, 192):
        s = x[120 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l530_0(x):
    # x is a list (or vector) of length 312
    return max(0, x[0])
def l530_1(x):
    # x is a list (or vector) of length 312
    return max(0, x[1])
def l530_2(x):
    # x is a list (or vector) of length 312
    return max(0, x[2])
def l530_3(x):
    # x is a list (or vector) of length 312
    return max(0, x[3])
def l530_4(x):
    # x is a list (or vector) of length 312
    return max(0, x[4])
def l530_5(x):
    # x is a list (or vector) of length 312
    return max(0, x[5])
def l530_6(x):
    # x is a list (or vector) of length 312
    return max(0, x[6])
def l530_7(x):
    # x is a list (or vector) of length 312
    return max(0, x[7])
def l530_8(x):
    # x is a list (or vector) of length 312
    return max(0, x[8])
def l530_9(x):
    # x is a list (or vector) of length 312
    return max(0, x[9])
def l530_10(x):
    # x is a list (or vector) of length 312
    return max(0, x[10])
def l530_11(x):
    # x is a list (or vector) of length 312
    return max(0, x[11])
def l530_12(x):
    # x is a list (or vector) of length 312
    return max(0, x[12])
def l530_13(x):
    # x is a list (or vector) of length 312
    return max(0, x[13])
def l530_14(x):
    # x is a list (or vector) of length 312
    return max(0, x[14])
def l530_15(x):
    # x is a list (or vector) of length 312
    return max(0, x[15])
def l530_16(x):
    # x is a list (or vector) of length 312
    return max(0, x[16])
def l530_17(x):
    # x is a list (or vector) of length 312
    return max(0, x[17])
def l530_18(x):
    # x is a list (or vector) of length 312
    return max(0, x[18])
def l530_19(x):
    # x is a list (or vector) of length 312
    return max(0, x[19])
def l530_20(x):
    # x is a list (or vector) of length 312
    return max(0, x[20])
def l530_21(x):
    # x is a list (or vector) of length 312
    return max(0, x[21])
def l530_22(x):
    # x is a list (or vector) of length 312
    return max(0, x[22])
def l530_23(x):
    # x is a list (or vector) of length 312
    return max(0, x[23])
def l530_24(x):
    # x is a list (or vector) of length 312
    return max(0, x[24])
def l530_25(x):
    # x is a list (or vector) of length 312
    return max(0, x[25])
def l530_26(x):
    # x is a list (or vector) of length 312
    return max(0, x[26])
def l530_27(x):
    # x is a list (or vector) of length 312
    return max(0, x[27])
def l530_28(x):
    # x is a list (or vector) of length 312
    return max(0, x[28])
def l530_29(x):
    # x is a list (or vector) of length 312
    return max(0, x[29])
def l530_30(x):
    # x is a list (or vector) of length 312
    return max(0, x[30])
def l530_31(x):
    # x is a list (or vector) of length 312
    return max(0, x[31])
def l530_32(x):
    # x is a list (or vector) of length 312
    return max(0, x[32])
def l530_33(x):
    # x is a list (or vector) of length 312
    return max(0, x[33])
def l530_34(x):
    # x is a list (or vector) of length 312
    return max(0, x[34])
def l530_35(x):
    # x is a list (or vector) of length 312
    return max(0, x[35])
def l530_36(x):
    # x is a list (or vector) of length 312
    return max(0, x[36])
def l530_37(x):
    # x is a list (or vector) of length 312
    return max(0, x[37])
def l530_38(x):
    # x is a list (or vector) of length 312
    return max(0, x[38])
def l530_39(x):
    # x is a list (or vector) of length 312
    return max(0, x[39])
def l530_40(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[40] + -1.0*x[64] + 1.0)
def l530_41(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[41] + -1.0*x[65] + 1.0)
def l530_42(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[42] + -1.0*x[66] + 1.0)
def l530_43(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[43] + -1.0*x[67] + 1.0)
def l530_44(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[44] + -1.0*x[68] + 1.0)
def l530_45(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[45] + -1.0*x[69] + 1.0)
def l530_46(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[46] + -1.0*x[70] + 1.0)
def l530_47(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[47] + -1.0*x[71] + 1.0)
def l530_48(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[48] + -1.0*x[72] + 1.0)
def l530_49(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[49] + -1.0*x[73] + 1.0)
def l530_50(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[50] + -1.0*x[74] + 1.0)
def l530_51(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[51] + -1.0*x[75] + 1.0)
def l530_52(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[52] + -1.0*x[76] + 1.0)
def l530_53(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[53] + -1.0*x[77] + 1.0)
def l530_54(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[54] + -1.0*x[78] + 1.0)
def l530_55(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[55] + -1.0*x[79] + 1.0)
def l530_56(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[56] + -1.0*x[80] + 1.0)
def l530_57(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[57] + -1.0*x[81] + 1.0)
def l530_58(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[58] + -1.0*x[82] + 1.0)
def l530_59(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[59] + -1.0*x[83] + 1.0)
def l530_60(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[60] + -1.0*x[84] + 1.0)
def l530_61(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[61] + -1.0*x[85] + 1.0)
def l530_62(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[62] + -1.0*x[86] + 1.0)
def l530_63(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[63] + -1.0*x[87] + 1.0)
def l530_64(x):
    # x is a list (or vector) of length 312
    return max(0, x[112])
def l530_65(x):
    # x is a list (or vector) of length 312
    return max(0, x[113])
def l530_66(x):
    # x is a list (or vector) of length 312
    return max(0, x[114])
def l530_67(x):
    # x is a list (or vector) of length 312
    return max(0, x[115])
def l530_68(x):
    # x is a list (or vector) of length 312
    return max(0, x[116])
def l530_69(x):
    # x is a list (or vector) of length 312
    return max(0, x[117])
def l530_70(x):
    # x is a list (or vector) of length 312
    return max(0, x[118])
def l530_71(x):
    # x is a list (or vector) of length 312
    return max(0, x[119])
def l530_72(x):
    # x is a list (or vector) of length 312
    return max(0, x[88])
def l530_73(x):
    # x is a list (or vector) of length 312
    return max(0, x[89])
def l530_74(x):
    # x is a list (or vector) of length 312
    return max(0, x[90])
def l530_75(x):
    # x is a list (or vector) of length 312
    return max(0, x[91])
def l530_76(x):
    # x is a list (or vector) of length 312
    return max(0, x[92])
def l530_77(x):
    # x is a list (or vector) of length 312
    return max(0, x[93])
def l530_78(x):
    # x is a list (or vector) of length 312
    return max(0, x[94])
def l530_79(x):
    # x is a list (or vector) of length 312
    return max(0, x[95])
def l530_80(x):
    # x is a list (or vector) of length 312
    return max(0, x[96])
def l530_81(x):
    # x is a list (or vector) of length 312
    return max(0, x[97])
def l530_82(x):
    # x is a list (or vector) of length 312
    return max(0, x[98])
def l530_83(x):
    # x is a list (or vector) of length 312
    return max(0, x[99])
def l530_84(x):
    # x is a list (or vector) of length 312
    return max(0, x[100])
def l530_85(x):
    # x is a list (or vector) of length 312
    return max(0, x[101])
def l530_86(x):
    # x is a list (or vector) of length 312
    return max(0, x[102])
def l530_87(x):
    # x is a list (or vector) of length 312
    return max(0, x[103])
def l530_88(x):
    # x is a list (or vector) of length 312
    return max(0, x[104])
def l530_89(x):
    # x is a list (or vector) of length 312
    return max(0, x[105])
def l530_90(x):
    # x is a list (or vector) of length 312
    return max(0, x[106])
def l530_91(x):
    # x is a list (or vector) of length 312
    return max(0, x[107])
def l530_92(x):
    # x is a list (or vector) of length 312
    return max(0, x[108])
def l530_93(x):
    # x is a list (or vector) of length 312
    return max(0, x[109])
def l530_94(x):
    # x is a list (or vector) of length 312
    return max(0, x[110])
def l530_95(x):
    # x is a list (or vector) of length 312
    return max(0, x[111])
def l530_96(x):
    # x is a list (or vector) of length 312
    return max(0, x[120])
def l530_97(x):
    # x is a list (or vector) of length 312
    return max(0, x[121])
def l530_98(x):
    # x is a list (or vector) of length 312
    return max(0, x[122])
def l530_99(x):
    # x is a list (or vector) of length 312
    return max(0, x[123])
def l530_100(x):
    # x is a list (or vector) of length 312
    return max(0, x[124])
def l530_101(x):
    # x is a list (or vector) of length 312
    return max(0, x[125])
def l530_102(x):
    # x is a list (or vector) of length 312
    return max(0, x[126])
def l530_103(x):
    # x is a list (or vector) of length 312
    return max(0, x[127])
def l530_104(x):
    # x is a list (or vector) of length 312
    return max(0, x[128])
def l530_105(x):
    # x is a list (or vector) of length 312
    return max(0, x[129])
def l530_106(x):
    # x is a list (or vector) of length 312
    return max(0, x[130])
def l530_107(x):
    # x is a list (or vector) of length 312
    return max(0, x[131])
def l530_108(x):
    # x is a list (or vector) of length 312
    return max(0, x[132])
def l530_109(x):
    # x is a list (or vector) of length 312
    return max(0, x[133])
def l530_110(x):
    # x is a list (or vector) of length 312
    return max(0, x[134])
def l530_111(x):
    # x is a list (or vector) of length 312
    return max(0, x[135])
def l530_112(x):
    # x is a list (or vector) of length 312
    return max(0, x[136])
def l530_113(x):
    # x is a list (or vector) of length 312
    return max(0, x[137])
def l530_114(x):
    # x is a list (or vector) of length 312
    return max(0, x[138])
def l530_115(x):
    # x is a list (or vector) of length 312
    return max(0, x[139])
def l530_116(x):
    # x is a list (or vector) of length 312
    return max(0, x[140])
def l530_117(x):
    # x is a list (or vector) of length 312
    return max(0, x[141])
def l530_118(x):
    # x is a list (or vector) of length 312
    return max(0, x[142])
def l530_119(x):
    # x is a list (or vector) of length 312
    return max(0, x[143])
def l530_120(x):
    # x is a list (or vector) of length 312
    return max(0, x[144])
def l530_121(x):
    # x is a list (or vector) of length 312
    return max(0, x[145])
def l530_122(x):
    # x is a list (or vector) of length 312
    return max(0, x[146])
def l530_123(x):
    # x is a list (or vector) of length 312
    return max(0, x[147])
def l530_124(x):
    # x is a list (or vector) of length 312
    return max(0, x[148])
def l530_125(x):
    # x is a list (or vector) of length 312
    return max(0, x[149])
def l530_126(x):
    # x is a list (or vector) of length 312
    return max(0, x[150])
def l530_127(x):
    # x is a list (or vector) of length 312
    return max(0, x[151])
def l530_128(x):
    # x is a list (or vector) of length 312
    return max(0, x[152])
def l530_129(x):
    # x is a list (or vector) of length 312
    return max(0, x[153])
def l530_130(x):
    # x is a list (or vector) of length 312
    return max(0, x[154])
def l530_131(x):
    # x is a list (or vector) of length 312
    return max(0, x[155])
def l530_132(x):
    # x is a list (or vector) of length 312
    return max(0, x[156])
def l530_133(x):
    # x is a list (or vector) of length 312
    return max(0, x[157])
def l530_134(x):
    # x is a list (or vector) of length 312
    return max(0, x[158])
def l530_135(x):
    # x is a list (or vector) of length 312
    return max(0, x[159])
def l530_136(x):
    # x is a list (or vector) of length 312
    return max(0, x[160])
def l530_137(x):
    # x is a list (or vector) of length 312
    return max(0, x[161])
def l530_138(x):
    # x is a list (or vector) of length 312
    return max(0, x[162])
def l530_139(x):
    # x is a list (or vector) of length 312
    return max(0, x[163])
def l530_140(x):
    # x is a list (or vector) of length 312
    return max(0, x[164])
def l530_141(x):
    # x is a list (or vector) of length 312
    return max(0, x[165])
def l530_142(x):
    # x is a list (or vector) of length 312
    return max(0, x[166])
def l530_143(x):
    # x is a list (or vector) of length 312
    return max(0, x[167])
def l530_144(x):
    # x is a list (or vector) of length 312
    return max(0, x[168])
def l530_145(x):
    # x is a list (or vector) of length 312
    return max(0, x[169])
def l530_146(x):
    # x is a list (or vector) of length 312
    return max(0, x[170])
def l530_147(x):
    # x is a list (or vector) of length 312
    return max(0, x[171])
def l530_148(x):
    # x is a list (or vector) of length 312
    return max(0, x[172])
def l530_149(x):
    # x is a list (or vector) of length 312
    return max(0, x[173])
def l530_150(x):
    # x is a list (or vector) of length 312
    return max(0, x[174])
def l530_151(x):
    # x is a list (or vector) of length 312
    return max(0, x[175])
def l530_152(x):
    # x is a list (or vector) of length 312
    return max(0, x[176])
def l530_153(x):
    # x is a list (or vector) of length 312
    return max(0, x[177])
def l530_154(x):
    # x is a list (or vector) of length 312
    return max(0, x[178])
def l530_155(x):
    # x is a list (or vector) of length 312
    return max(0, x[179])
def l530_156(x):
    # x is a list (or vector) of length 312
    return max(0, x[180])
def l530_157(x):
    # x is a list (or vector) of length 312
    return max(0, x[181])
def l530_158(x):
    # x is a list (or vector) of length 312
    return max(0, x[182])
def l530_159(x):
    # x is a list (or vector) of length 312
    return max(0, x[183])
def l530_160(x):
    # x is a list (or vector) of length 312
    return max(0, x[184])
def l530_161(x):
    # x is a list (or vector) of length 312
    return max(0, x[185])
def l530_162(x):
    # x is a list (or vector) of length 312
    return max(0, x[186])
def l530_163(x):
    # x is a list (or vector) of length 312
    return max(0, x[187])
def l530_164(x):
    # x is a list (or vector) of length 312
    return max(0, x[188])
def l530_165(x):
    # x is a list (or vector) of length 312
    return max(0, x[189])
def l530_166(x):
    # x is a list (or vector) of length 312
    return max(0, x[190])
def l530_167(x):
    # x is a list (or vector) of length 312
    return max(0, x[191])
def l530_168(x):
    # x is a list (or vector) of length 312
    return max(0, x[192])
def l530_169(x):
    # x is a list (or vector) of length 312
    return max(0, x[193])
def l530_170(x):
    # x is a list (or vector) of length 312
    return max(0, x[194])
def l530_171(x):
    # x is a list (or vector) of length 312
    return max(0, x[195])
def l530_172(x):
    # x is a list (or vector) of length 312
    return max(0, x[196])
def l530_173(x):
    # x is a list (or vector) of length 312
    return max(0, x[197])
def l530_174(x):
    # x is a list (or vector) of length 312
    return max(0, x[198])
def l530_175(x):
    # x is a list (or vector) of length 312
    return max(0, x[199])
def l530_176(x):
    # x is a list (or vector) of length 312
    return max(0, x[200])
def l530_177(x):
    # x is a list (or vector) of length 312
    return max(0, x[201])
def l530_178(x):
    # x is a list (or vector) of length 312
    return max(0, x[202])
def l530_179(x):
    # x is a list (or vector) of length 312
    return max(0, x[203])
def l530_180(x):
    # x is a list (or vector) of length 312
    return max(0, x[204])
def l530_181(x):
    # x is a list (or vector) of length 312
    return max(0, x[205])
def l530_182(x):
    # x is a list (or vector) of length 312
    return max(0, x[206])
def l530_183(x):
    # x is a list (or vector) of length 312
    return max(0, x[207])
def l530_184(x):
    # x is a list (or vector) of length 312
    return max(0, x[208])
def l530_185(x):
    # x is a list (or vector) of length 312
    return max(0, x[209])
def l530_186(x):
    # x is a list (or vector) of length 312
    return max(0, x[210])
def l530_187(x):
    # x is a list (or vector) of length 312
    return max(0, x[211])
def l530_188(x):
    # x is a list (or vector) of length 312
    return max(0, x[212])
def l530_189(x):
    # x is a list (or vector) of length 312
    return max(0, x[213])
def l530_190(x):
    # x is a list (or vector) of length 312
    return max(0, x[214])
def l530_191(x):
    # x is a list (or vector) of length 312
    return max(0, x[215])
def l530_192(x):
    # x is a list (or vector) of length 312
    return max(0, x[216])
def l530_193(x):
    # x is a list (or vector) of length 312
    return max(0, x[217])
def l530_194(x):
    # x is a list (or vector) of length 312
    return max(0, x[218])
def l530_195(x):
    # x is a list (or vector) of length 312
    return max(0, x[219])
def l530_196(x):
    # x is a list (or vector) of length 312
    return max(0, x[220])
def l530_197(x):
    # x is a list (or vector) of length 312
    return max(0, x[221])
def l530_198(x):
    # x is a list (or vector) of length 312
    return max(0, x[222])
def l530_199(x):
    # x is a list (or vector) of length 312
    return max(0, x[223])
def l530_200(x):
    # x is a list (or vector) of length 312
    return max(0, x[224])
def l530_201(x):
    # x is a list (or vector) of length 312
    return max(0, x[225])
def l530_202(x):
    # x is a list (or vector) of length 312
    return max(0, x[226])
def l530_203(x):
    # x is a list (or vector) of length 312
    return max(0, x[227])
def l530_204(x):
    # x is a list (or vector) of length 312
    return max(0, x[228])
def l530_205(x):
    # x is a list (or vector) of length 312
    return max(0, x[229])
def l530_206(x):
    # x is a list (or vector) of length 312
    return max(0, x[230])
def l530_207(x):
    # x is a list (or vector) of length 312
    return max(0, x[231])
def l530_208(x):
    # x is a list (or vector) of length 312
    return max(0, x[232])
def l530_209(x):
    # x is a list (or vector) of length 312
    return max(0, x[233])
def l530_210(x):
    # x is a list (or vector) of length 312
    return max(0, x[234])
def l530_211(x):
    # x is a list (or vector) of length 312
    return max(0, x[235])
def l530_212(x):
    # x is a list (or vector) of length 312
    return max(0, x[236])
def l530_213(x):
    # x is a list (or vector) of length 312
    return max(0, x[237])
def l530_214(x):
    # x is a list (or vector) of length 312
    return max(0, x[238])
def l530_215(x):
    # x is a list (or vector) of length 312
    return max(0, x[239])
def l530_216(x):
    # x is a list (or vector) of length 312
    return max(0, x[240])
def l530_217(x):
    # x is a list (or vector) of length 312
    return max(0, x[241])
def l530_218(x):
    # x is a list (or vector) of length 312
    return max(0, x[242])
def l530_219(x):
    # x is a list (or vector) of length 312
    return max(0, x[243])
def l530_220(x):
    # x is a list (or vector) of length 312
    return max(0, x[244])
def l530_221(x):
    # x is a list (or vector) of length 312
    return max(0, x[245])
def l530_222(x):
    # x is a list (or vector) of length 312
    return max(0, x[246])
def l530_223(x):
    # x is a list (or vector) of length 312
    return max(0, x[247])
def l530_224(x):
    # x is a list (or vector) of length 312
    return max(0, x[248])
def l530_225(x):
    # x is a list (or vector) of length 312
    return max(0, x[249])
def l530_226(x):
    # x is a list (or vector) of length 312
    return max(0, x[250])
def l530_227(x):
    # x is a list (or vector) of length 312
    return max(0, x[251])
def l530_228(x):
    # x is a list (or vector) of length 312
    return max(0, x[252])
def l530_229(x):
    # x is a list (or vector) of length 312
    return max(0, x[253])
def l530_230(x):
    # x is a list (or vector) of length 312
    return max(0, x[254])
def l530_231(x):
    # x is a list (or vector) of length 312
    return max(0, x[255])
def l530_232(x):
    # x is a list (or vector) of length 312
    return max(0, x[256])
def l530_233(x):
    # x is a list (or vector) of length 312
    return max(0, x[257])
def l530_234(x):
    # x is a list (or vector) of length 312
    return max(0, x[258])
def l530_235(x):
    # x is a list (or vector) of length 312
    return max(0, x[259])
def l530_236(x):
    # x is a list (or vector) of length 312
    return max(0, x[260])
def l530_237(x):
    # x is a list (or vector) of length 312
    return max(0, x[261])
def l530_238(x):
    # x is a list (or vector) of length 312
    return max(0, x[262])
def l530_239(x):
    # x is a list (or vector) of length 312
    return max(0, x[263])
def l530_240(x):
    # x is a list (or vector) of length 312
    return max(0, x[264])
def l530_241(x):
    # x is a list (or vector) of length 312
    return max(0, x[265])
def l530_242(x):
    # x is a list (or vector) of length 312
    return max(0, x[266])
def l530_243(x):
    # x is a list (or vector) of length 312
    return max(0, x[267])
def l530_244(x):
    # x is a list (or vector) of length 312
    return max(0, x[268])
def l530_245(x):
    # x is a list (or vector) of length 312
    return max(0, x[269])
def l530_246(x):
    # x is a list (or vector) of length 312
    return max(0, x[270])
def l530_247(x):
    # x is a list (or vector) of length 312
    return max(0, x[271])
def l530_248(x):
    # x is a list (or vector) of length 312
    return max(0, x[272])
def l530_249(x):
    # x is a list (or vector) of length 312
    return max(0, x[273])
def l530_250(x):
    # x is a list (or vector) of length 312
    return max(0, x[274])
def l530_251(x):
    # x is a list (or vector) of length 312
    return max(0, x[275])
def l530_252(x):
    # x is a list (or vector) of length 312
    return max(0, x[276])
def l530_253(x):
    # x is a list (or vector) of length 312
    return max(0, x[277])
def l530_254(x):
    # x is a list (or vector) of length 312
    return max(0, x[278])
def l530_255(x):
    # x is a list (or vector) of length 312
    return max(0, x[279])
def l530_256(x):
    # x is a list (or vector) of length 312
    return max(0, x[280])
def l530_257(x):
    # x is a list (or vector) of length 312
    return max(0, x[281])
def l530_258(x):
    # x is a list (or vector) of length 312
    return max(0, x[282])
def l530_259(x):
    # x is a list (or vector) of length 312
    return max(0, x[283])
def l530_260(x):
    # x is a list (or vector) of length 312
    return max(0, x[284])
def l530_261(x):
    # x is a list (or vector) of length 312
    return max(0, x[285])
def l530_262(x):
    # x is a list (or vector) of length 312
    return max(0, x[286])
def l530_263(x):
    # x is a list (or vector) of length 312
    return max(0, x[287])
def l530_264(x):
    # x is a list (or vector) of length 312
    return max(0, x[288])
def l530_265(x):
    # x is a list (or vector) of length 312
    return max(0, x[289])
def l530_266(x):
    # x is a list (or vector) of length 312
    return max(0, x[290])
def l530_267(x):
    # x is a list (or vector) of length 312
    return max(0, x[291])
def l530_268(x):
    # x is a list (or vector) of length 312
    return max(0, x[292])
def l530_269(x):
    # x is a list (or vector) of length 312
    return max(0, x[293])
def l530_270(x):
    # x is a list (or vector) of length 312
    return max(0, x[294])
def l530_271(x):
    # x is a list (or vector) of length 312
    return max(0, x[295])
def l530_272(x):
    # x is a list (or vector) of length 312
    return max(0, x[296])
def l530_273(x):
    # x is a list (or vector) of length 312
    return max(0, x[297])
def l530_274(x):
    # x is a list (or vector) of length 312
    return max(0, x[298])
def l530_275(x):
    # x is a list (or vector) of length 312
    return max(0, x[299])
def l530_276(x):
    # x is a list (or vector) of length 312
    return max(0, x[300])
def l530_277(x):
    # x is a list (or vector) of length 312
    return max(0, x[301])
def l530_278(x):
    # x is a list (or vector) of length 312
    return max(0, x[302])
def l530_279(x):
    # x is a list (or vector) of length 312
    return max(0, x[303])
def l530_280(x):
    # x is a list (or vector) of length 312
    return max(0, x[304])
def l530_281(x):
    # x is a list (or vector) of length 312
    return max(0, x[305])
def l530_282(x):
    # x is a list (or vector) of length 312
    return max(0, x[306])
def l530_283(x):
    # x is a list (or vector) of length 312
    return max(0, x[307])
def l530_284(x):
    # x is a list (or vector) of length 312
    return max(0, x[308])
def l530_285(x):
    # x is a list (or vector) of length 312
    return max(0, x[309])
def l530_286(x):
    # x is a list (or vector) of length 312
    return max(0, x[310])
def l530_287(x):
    # x is a list (or vector) of length 312
    return max(0, x[311])
def l530_(x):
    # x is a list (or vector) of length 312
    return [
        l530_0(x),
        l530_1(x),
        l530_2(x),
        l530_3(x),
        l530_4(x),
        l530_5(x),
        l530_6(x),
        l530_7(x),
        l530_8(x),
        l530_9(x),
        l530_10(x),
        l530_11(x),
        l530_12(x),
        l530_13(x),
        l530_14(x),
        l530_15(x),
        l530_16(x),
        l530_17(x),
        l530_18(x),
        l530_19(x),
        l530_20(x),
        l530_21(x),
        l530_22(x),
        l530_23(x),
        l530_24(x),
        l530_25(x),
        l530_26(x),
        l530_27(x),
        l530_28(x),
        l530_29(x),
        l530_30(x),
        l530_31(x),
        l530_32(x),
        l530_33(x),
        l530_34(x),
        l530_35(x),
        l530_36(x),
        l530_37(x),
        l530_38(x),
        l530_39(x),
        l530_40(x),
        l530_41(x),
        l530_42(x),
        l530_43(x),
        l530_44(x),
        l530_45(x),
        l530_46(x),
        l530_47(x),
        l530_48(x),
        l530_49(x),
        l530_50(x),
        l530_51(x),
        l530_52(x),
        l530_53(x),
        l530_54(x),
        l530_55(x),
        l530_56(x),
        l530_57(x),
        l530_58(x),
        l530_59(x),
        l530_60(x),
        l530_61(x),
        l530_62(x),
        l530_63(x),
        l530_64(x),
        l530_65(x),
        l530_66(x),
        l530_67(x),
        l530_68(x),
        l530_69(x),
        l530_70(x),
        l530_71(x),
        l530_72(x),
        l530_73(x),
        l530_74(x),
        l530_75(x),
        l530_76(x),
        l530_77(x),
        l530_78(x),
        l530_79(x),
        l530_80(x),
        l530_81(x),
        l530_82(x),
        l530_83(x),
        l530_84(x),
        l530_85(x),
        l530_86(x),
        l530_87(x),
        l530_88(x),
        l530_89(x),
        l530_90(x),
        l530_91(x),
        l530_92(x),
        l530_93(x),
        l530_94(x),
        l530_95(x),
        l530_96(x),
        l530_97(x),
        l530_98(x),
        l530_99(x),
        l530_100(x),
        l530_101(x),
        l530_102(x),
        l530_103(x),
        l530_104(x),
        l530_105(x),
        l530_106(x),
        l530_107(x),
        l530_108(x),
        l530_109(x),
        l530_110(x),
        l530_111(x),
        l530_112(x),
        l530_113(x),
        l530_114(x),
        l530_115(x),
        l530_116(x),
        l530_117(x),
        l530_118(x),
        l530_119(x),
        l530_120(x),
        l530_121(x),
        l530_122(x),
        l530_123(x),
        l530_124(x),
        l530_125(x),
        l530_126(x),
        l530_127(x),
        l530_128(x),
        l530_129(x),
        l530_130(x),
        l530_131(x),
        l530_132(x),
        l530_133(x),
        l530_134(x),
        l530_135(x),
        l530_136(x),
        l530_137(x),
        l530_138(x),
        l530_139(x),
        l530_140(x),
        l530_141(x),
        l530_142(x),
        l530_143(x),
        l530_144(x),
        l530_145(x),
        l530_146(x),
        l530_147(x),
        l530_148(x),
        l530_149(x),
        l530_150(x),
        l530_151(x),
        l530_152(x),
        l530_153(x),
        l530_154(x),
        l530_155(x),
        l530_156(x),
        l530_157(x),
        l530_158(x),
        l530_159(x),
        l530_160(x),
        l530_161(x),
        l530_162(x),
        l530_163(x),
        l530_164(x),
        l530_165(x),
        l530_166(x),
        l530_167(x),
        l530_168(x),
        l530_169(x),
        l530_170(x),
        l530_171(x),
        l530_172(x),
        l530_173(x),
        l530_174(x),
        l530_175(x),
        l530_176(x),
        l530_177(x),
        l530_178(x),
        l530_179(x),
        l530_180(x),
        l530_181(x),
        l530_182(x),
        l530_183(x),
        l530_184(x),
        l530_185(x),
        l530_186(x),
        l530_187(x),
        l530_188(x),
        l530_189(x),
        l530_190(x),
        l530_191(x),
        l530_192(x),
        l530_193(x),
        l530_194(x),
        l530_195(x),
        l530_196(x),
        l530_197(x),
        l530_198(x),
        l530_199(x),
        l530_200(x),
        l530_201(x),
        l530_202(x),
        l530_203(x),
        l530_204(x),
        l530_205(x),
        l530_206(x),
        l530_207(x),
        l530_208(x),
        l530_209(x),
        l530_210(x),
        l530_211(x),
        l530_212(x),
        l530_213(x),
        l530_214(x),
        l530_215(x),
        l530_216(x),
        l530_217(x),
        l530_218(x),
        l530_219(x),
        l530_220(x),
        l530_221(x),
        l530_222(x),
        l530_223(x),
        l530_224(x),
        l530_225(x),
        l530_226(x),
        l530_227(x),
        l530_228(x),
        l530_229(x),
        l530_230(x),
        l530_231(x),
        l530_232(x),
        l530_233(x),
        l530_234(x),
        l530_235(x),
        l530_236(x),
        l530_237(x),
        l530_238(x),
        l530_239(x),
        l530_240(x),
        l530_241(x),
        l530_242(x),
        l530_243(x),
        l530_244(x),
        l530_245(x),
        l530_246(x),
        l530_247(x),
        l530_248(x),
        l530_249(x),
        l530_250(x),
        l530_251(x),
        l530_252(x),
        l530_253(x),
        l530_254(x),
        l530_255(x),
        l530_256(x),
        l530_257(x),
        l530_258(x),
        l530_259(x),
        l530_260(x),
        l530_261(x),
        l530_262(x),
        l530_263(x),
        l530_264(x),
        l530_265(x),
        l530_266(x),
        l530_267(x),
        l530_268(x),
        l530_269(x),
        l530_270(x),
        l530_271(x),
        l530_272(x),
        l530_273(x),
        l530_274(x),
        l530_275(x),
        l530_276(x),
        l530_277(x),
        l530_278(x),
        l530_279(x),
        l530_280(x),
        l530_281(x),
        l530_282(x),
        l530_283(x),
        l530_284(x),
        l530_285(x),
        l530_286(x),
        l530_287(x),
    ]