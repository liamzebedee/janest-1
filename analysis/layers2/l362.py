import numpy as np




# Generated from reverse engineering
def l362_g(x: np.ndarray) -> np.ndarray:
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




def l362_0(x):
    # x is a list (or vector) of length 312
    return max(0, x[0])
def l362_1(x):
    # x is a list (or vector) of length 312
    return max(0, x[1])
def l362_2(x):
    # x is a list (or vector) of length 312
    return max(0, x[2])
def l362_3(x):
    # x is a list (or vector) of length 312
    return max(0, x[3])
def l362_4(x):
    # x is a list (or vector) of length 312
    return max(0, x[4])
def l362_5(x):
    # x is a list (or vector) of length 312
    return max(0, x[5])
def l362_6(x):
    # x is a list (or vector) of length 312
    return max(0, x[6])
def l362_7(x):
    # x is a list (or vector) of length 312
    return max(0, x[7])
def l362_8(x):
    # x is a list (or vector) of length 312
    return max(0, x[8])
def l362_9(x):
    # x is a list (or vector) of length 312
    return max(0, x[9])
def l362_10(x):
    # x is a list (or vector) of length 312
    return max(0, x[10])
def l362_11(x):
    # x is a list (or vector) of length 312
    return max(0, x[11])
def l362_12(x):
    # x is a list (or vector) of length 312
    return max(0, x[12])
def l362_13(x):
    # x is a list (or vector) of length 312
    return max(0, x[13])
def l362_14(x):
    # x is a list (or vector) of length 312
    return max(0, x[14])
def l362_15(x):
    # x is a list (or vector) of length 312
    return max(0, x[15])
def l362_16(x):
    # x is a list (or vector) of length 312
    return max(0, x[16])
def l362_17(x):
    # x is a list (or vector) of length 312
    return max(0, x[17])
def l362_18(x):
    # x is a list (or vector) of length 312
    return max(0, x[18])
def l362_19(x):
    # x is a list (or vector) of length 312
    return max(0, x[19])
def l362_20(x):
    # x is a list (or vector) of length 312
    return max(0, x[20])
def l362_21(x):
    # x is a list (or vector) of length 312
    return max(0, x[21])
def l362_22(x):
    # x is a list (or vector) of length 312
    return max(0, x[22])
def l362_23(x):
    # x is a list (or vector) of length 312
    return max(0, x[23])
def l362_24(x):
    # x is a list (or vector) of length 312
    return max(0, x[24])
def l362_25(x):
    # x is a list (or vector) of length 312
    return max(0, x[25])
def l362_26(x):
    # x is a list (or vector) of length 312
    return max(0, x[26])
def l362_27(x):
    # x is a list (or vector) of length 312
    return max(0, x[27])
def l362_28(x):
    # x is a list (or vector) of length 312
    return max(0, x[28])
def l362_29(x):
    # x is a list (or vector) of length 312
    return max(0, x[29])
def l362_30(x):
    # x is a list (or vector) of length 312
    return max(0, x[30])
def l362_31(x):
    # x is a list (or vector) of length 312
    return max(0, x[31])
def l362_32(x):
    # x is a list (or vector) of length 312
    return max(0, x[32])
def l362_33(x):
    # x is a list (or vector) of length 312
    return max(0, x[33])
def l362_34(x):
    # x is a list (or vector) of length 312
    return max(0, x[34])
def l362_35(x):
    # x is a list (or vector) of length 312
    return max(0, x[35])
def l362_36(x):
    # x is a list (or vector) of length 312
    return max(0, x[36])
def l362_37(x):
    # x is a list (or vector) of length 312
    return max(0, x[37])
def l362_38(x):
    # x is a list (or vector) of length 312
    return max(0, x[38])
def l362_39(x):
    # x is a list (or vector) of length 312
    return max(0, x[39])
def l362_40(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[40] + -1.0*x[64] + 1.0)
def l362_41(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[41] + -1.0*x[65] + 1.0)
def l362_42(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[42] + -1.0*x[66] + 1.0)
def l362_43(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[43] + -1.0*x[67] + 1.0)
def l362_44(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[44] + -1.0*x[68] + 1.0)
def l362_45(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[45] + -1.0*x[69] + 1.0)
def l362_46(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[46] + -1.0*x[70] + 1.0)
def l362_47(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[47] + -1.0*x[71] + 1.0)
def l362_48(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[48] + -1.0*x[72] + 1.0)
def l362_49(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[49] + -1.0*x[73] + 1.0)
def l362_50(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[50] + -1.0*x[74] + 1.0)
def l362_51(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[51] + -1.0*x[75] + 1.0)
def l362_52(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[52] + -1.0*x[76] + 1.0)
def l362_53(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[53] + -1.0*x[77] + 1.0)
def l362_54(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[54] + -1.0*x[78] + 1.0)
def l362_55(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[55] + -1.0*x[79] + 1.0)
def l362_56(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[56] + -1.0*x[80] + 1.0)
def l362_57(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[57] + -1.0*x[81] + 1.0)
def l362_58(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[58] + -1.0*x[82] + 1.0)
def l362_59(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[59] + -1.0*x[83] + 1.0)
def l362_60(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[60] + -1.0*x[84] + 1.0)
def l362_61(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[61] + -1.0*x[85] + 1.0)
def l362_62(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[62] + -1.0*x[86] + 1.0)
def l362_63(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[63] + -1.0*x[87] + 1.0)
def l362_64(x):
    # x is a list (or vector) of length 312
    return max(0, x[112])
def l362_65(x):
    # x is a list (or vector) of length 312
    return max(0, x[113])
def l362_66(x):
    # x is a list (or vector) of length 312
    return max(0, x[114])
def l362_67(x):
    # x is a list (or vector) of length 312
    return max(0, x[115])
def l362_68(x):
    # x is a list (or vector) of length 312
    return max(0, x[116])
def l362_69(x):
    # x is a list (or vector) of length 312
    return max(0, x[117])
def l362_70(x):
    # x is a list (or vector) of length 312
    return max(0, x[118])
def l362_71(x):
    # x is a list (or vector) of length 312
    return max(0, x[119])
def l362_72(x):
    # x is a list (or vector) of length 312
    return max(0, x[88])
def l362_73(x):
    # x is a list (or vector) of length 312
    return max(0, x[89])
def l362_74(x):
    # x is a list (or vector) of length 312
    return max(0, x[90])
def l362_75(x):
    # x is a list (or vector) of length 312
    return max(0, x[91])
def l362_76(x):
    # x is a list (or vector) of length 312
    return max(0, x[92])
def l362_77(x):
    # x is a list (or vector) of length 312
    return max(0, x[93])
def l362_78(x):
    # x is a list (or vector) of length 312
    return max(0, x[94])
def l362_79(x):
    # x is a list (or vector) of length 312
    return max(0, x[95])
def l362_80(x):
    # x is a list (or vector) of length 312
    return max(0, x[96])
def l362_81(x):
    # x is a list (or vector) of length 312
    return max(0, x[97])
def l362_82(x):
    # x is a list (or vector) of length 312
    return max(0, x[98])
def l362_83(x):
    # x is a list (or vector) of length 312
    return max(0, x[99])
def l362_84(x):
    # x is a list (or vector) of length 312
    return max(0, x[100])
def l362_85(x):
    # x is a list (or vector) of length 312
    return max(0, x[101])
def l362_86(x):
    # x is a list (or vector) of length 312
    return max(0, x[102])
def l362_87(x):
    # x is a list (or vector) of length 312
    return max(0, x[103])
def l362_88(x):
    # x is a list (or vector) of length 312
    return max(0, x[104])
def l362_89(x):
    # x is a list (or vector) of length 312
    return max(0, x[105])
def l362_90(x):
    # x is a list (or vector) of length 312
    return max(0, x[106])
def l362_91(x):
    # x is a list (or vector) of length 312
    return max(0, x[107])
def l362_92(x):
    # x is a list (or vector) of length 312
    return max(0, x[108])
def l362_93(x):
    # x is a list (or vector) of length 312
    return max(0, x[109])
def l362_94(x):
    # x is a list (or vector) of length 312
    return max(0, x[110])
def l362_95(x):
    # x is a list (or vector) of length 312
    return max(0, x[111])
def l362_96(x):
    # x is a list (or vector) of length 312
    return max(0, x[120])
def l362_97(x):
    # x is a list (or vector) of length 312
    return max(0, x[121])
def l362_98(x):
    # x is a list (or vector) of length 312
    return max(0, x[122])
def l362_99(x):
    # x is a list (or vector) of length 312
    return max(0, x[123])
def l362_100(x):
    # x is a list (or vector) of length 312
    return max(0, x[124])
def l362_101(x):
    # x is a list (or vector) of length 312
    return max(0, x[125])
def l362_102(x):
    # x is a list (or vector) of length 312
    return max(0, x[126])
def l362_103(x):
    # x is a list (or vector) of length 312
    return max(0, x[127])
def l362_104(x):
    # x is a list (or vector) of length 312
    return max(0, x[128])
def l362_105(x):
    # x is a list (or vector) of length 312
    return max(0, x[129])
def l362_106(x):
    # x is a list (or vector) of length 312
    return max(0, x[130])
def l362_107(x):
    # x is a list (or vector) of length 312
    return max(0, x[131])
def l362_108(x):
    # x is a list (or vector) of length 312
    return max(0, x[132])
def l362_109(x):
    # x is a list (or vector) of length 312
    return max(0, x[133])
def l362_110(x):
    # x is a list (or vector) of length 312
    return max(0, x[134])
def l362_111(x):
    # x is a list (or vector) of length 312
    return max(0, x[135])
def l362_112(x):
    # x is a list (or vector) of length 312
    return max(0, x[136])
def l362_113(x):
    # x is a list (or vector) of length 312
    return max(0, x[137])
def l362_114(x):
    # x is a list (or vector) of length 312
    return max(0, x[138])
def l362_115(x):
    # x is a list (or vector) of length 312
    return max(0, x[139])
def l362_116(x):
    # x is a list (or vector) of length 312
    return max(0, x[140])
def l362_117(x):
    # x is a list (or vector) of length 312
    return max(0, x[141])
def l362_118(x):
    # x is a list (or vector) of length 312
    return max(0, x[142])
def l362_119(x):
    # x is a list (or vector) of length 312
    return max(0, x[143])
def l362_120(x):
    # x is a list (or vector) of length 312
    return max(0, x[144])
def l362_121(x):
    # x is a list (or vector) of length 312
    return max(0, x[145])
def l362_122(x):
    # x is a list (or vector) of length 312
    return max(0, x[146])
def l362_123(x):
    # x is a list (or vector) of length 312
    return max(0, x[147])
def l362_124(x):
    # x is a list (or vector) of length 312
    return max(0, x[148])
def l362_125(x):
    # x is a list (or vector) of length 312
    return max(0, x[149])
def l362_126(x):
    # x is a list (or vector) of length 312
    return max(0, x[150])
def l362_127(x):
    # x is a list (or vector) of length 312
    return max(0, x[151])
def l362_128(x):
    # x is a list (or vector) of length 312
    return max(0, x[152])
def l362_129(x):
    # x is a list (or vector) of length 312
    return max(0, x[153])
def l362_130(x):
    # x is a list (or vector) of length 312
    return max(0, x[154])
def l362_131(x):
    # x is a list (or vector) of length 312
    return max(0, x[155])
def l362_132(x):
    # x is a list (or vector) of length 312
    return max(0, x[156])
def l362_133(x):
    # x is a list (or vector) of length 312
    return max(0, x[157])
def l362_134(x):
    # x is a list (or vector) of length 312
    return max(0, x[158])
def l362_135(x):
    # x is a list (or vector) of length 312
    return max(0, x[159])
def l362_136(x):
    # x is a list (or vector) of length 312
    return max(0, x[160])
def l362_137(x):
    # x is a list (or vector) of length 312
    return max(0, x[161])
def l362_138(x):
    # x is a list (or vector) of length 312
    return max(0, x[162])
def l362_139(x):
    # x is a list (or vector) of length 312
    return max(0, x[163])
def l362_140(x):
    # x is a list (or vector) of length 312
    return max(0, x[164])
def l362_141(x):
    # x is a list (or vector) of length 312
    return max(0, x[165])
def l362_142(x):
    # x is a list (or vector) of length 312
    return max(0, x[166])
def l362_143(x):
    # x is a list (or vector) of length 312
    return max(0, x[167])
def l362_144(x):
    # x is a list (or vector) of length 312
    return max(0, x[168])
def l362_145(x):
    # x is a list (or vector) of length 312
    return max(0, x[169])
def l362_146(x):
    # x is a list (or vector) of length 312
    return max(0, x[170])
def l362_147(x):
    # x is a list (or vector) of length 312
    return max(0, x[171])
def l362_148(x):
    # x is a list (or vector) of length 312
    return max(0, x[172])
def l362_149(x):
    # x is a list (or vector) of length 312
    return max(0, x[173])
def l362_150(x):
    # x is a list (or vector) of length 312
    return max(0, x[174])
def l362_151(x):
    # x is a list (or vector) of length 312
    return max(0, x[175])
def l362_152(x):
    # x is a list (or vector) of length 312
    return max(0, x[176])
def l362_153(x):
    # x is a list (or vector) of length 312
    return max(0, x[177])
def l362_154(x):
    # x is a list (or vector) of length 312
    return max(0, x[178])
def l362_155(x):
    # x is a list (or vector) of length 312
    return max(0, x[179])
def l362_156(x):
    # x is a list (or vector) of length 312
    return max(0, x[180])
def l362_157(x):
    # x is a list (or vector) of length 312
    return max(0, x[181])
def l362_158(x):
    # x is a list (or vector) of length 312
    return max(0, x[182])
def l362_159(x):
    # x is a list (or vector) of length 312
    return max(0, x[183])
def l362_160(x):
    # x is a list (or vector) of length 312
    return max(0, x[184])
def l362_161(x):
    # x is a list (or vector) of length 312
    return max(0, x[185])
def l362_162(x):
    # x is a list (or vector) of length 312
    return max(0, x[186])
def l362_163(x):
    # x is a list (or vector) of length 312
    return max(0, x[187])
def l362_164(x):
    # x is a list (or vector) of length 312
    return max(0, x[188])
def l362_165(x):
    # x is a list (or vector) of length 312
    return max(0, x[189])
def l362_166(x):
    # x is a list (or vector) of length 312
    return max(0, x[190])
def l362_167(x):
    # x is a list (or vector) of length 312
    return max(0, x[191])
def l362_168(x):
    # x is a list (or vector) of length 312
    return max(0, x[192])
def l362_169(x):
    # x is a list (or vector) of length 312
    return max(0, x[193])
def l362_170(x):
    # x is a list (or vector) of length 312
    return max(0, x[194])
def l362_171(x):
    # x is a list (or vector) of length 312
    return max(0, x[195])
def l362_172(x):
    # x is a list (or vector) of length 312
    return max(0, x[196])
def l362_173(x):
    # x is a list (or vector) of length 312
    return max(0, x[197])
def l362_174(x):
    # x is a list (or vector) of length 312
    return max(0, x[198])
def l362_175(x):
    # x is a list (or vector) of length 312
    return max(0, x[199])
def l362_176(x):
    # x is a list (or vector) of length 312
    return max(0, x[200])
def l362_177(x):
    # x is a list (or vector) of length 312
    return max(0, x[201])
def l362_178(x):
    # x is a list (or vector) of length 312
    return max(0, x[202])
def l362_179(x):
    # x is a list (or vector) of length 312
    return max(0, x[203])
def l362_180(x):
    # x is a list (or vector) of length 312
    return max(0, x[204])
def l362_181(x):
    # x is a list (or vector) of length 312
    return max(0, x[205])
def l362_182(x):
    # x is a list (or vector) of length 312
    return max(0, x[206])
def l362_183(x):
    # x is a list (or vector) of length 312
    return max(0, x[207])
def l362_184(x):
    # x is a list (or vector) of length 312
    return max(0, x[208])
def l362_185(x):
    # x is a list (or vector) of length 312
    return max(0, x[209])
def l362_186(x):
    # x is a list (or vector) of length 312
    return max(0, x[210])
def l362_187(x):
    # x is a list (or vector) of length 312
    return max(0, x[211])
def l362_188(x):
    # x is a list (or vector) of length 312
    return max(0, x[212])
def l362_189(x):
    # x is a list (or vector) of length 312
    return max(0, x[213])
def l362_190(x):
    # x is a list (or vector) of length 312
    return max(0, x[214])
def l362_191(x):
    # x is a list (or vector) of length 312
    return max(0, x[215])
def l362_192(x):
    # x is a list (or vector) of length 312
    return max(0, x[216])
def l362_193(x):
    # x is a list (or vector) of length 312
    return max(0, x[217])
def l362_194(x):
    # x is a list (or vector) of length 312
    return max(0, x[218])
def l362_195(x):
    # x is a list (or vector) of length 312
    return max(0, x[219])
def l362_196(x):
    # x is a list (or vector) of length 312
    return max(0, x[220])
def l362_197(x):
    # x is a list (or vector) of length 312
    return max(0, x[221])
def l362_198(x):
    # x is a list (or vector) of length 312
    return max(0, x[222])
def l362_199(x):
    # x is a list (or vector) of length 312
    return max(0, x[223])
def l362_200(x):
    # x is a list (or vector) of length 312
    return max(0, x[224])
def l362_201(x):
    # x is a list (or vector) of length 312
    return max(0, x[225])
def l362_202(x):
    # x is a list (or vector) of length 312
    return max(0, x[226])
def l362_203(x):
    # x is a list (or vector) of length 312
    return max(0, x[227])
def l362_204(x):
    # x is a list (or vector) of length 312
    return max(0, x[228])
def l362_205(x):
    # x is a list (or vector) of length 312
    return max(0, x[229])
def l362_206(x):
    # x is a list (or vector) of length 312
    return max(0, x[230])
def l362_207(x):
    # x is a list (or vector) of length 312
    return max(0, x[231])
def l362_208(x):
    # x is a list (or vector) of length 312
    return max(0, x[232])
def l362_209(x):
    # x is a list (or vector) of length 312
    return max(0, x[233])
def l362_210(x):
    # x is a list (or vector) of length 312
    return max(0, x[234])
def l362_211(x):
    # x is a list (or vector) of length 312
    return max(0, x[235])
def l362_212(x):
    # x is a list (or vector) of length 312
    return max(0, x[236])
def l362_213(x):
    # x is a list (or vector) of length 312
    return max(0, x[237])
def l362_214(x):
    # x is a list (or vector) of length 312
    return max(0, x[238])
def l362_215(x):
    # x is a list (or vector) of length 312
    return max(0, x[239])
def l362_216(x):
    # x is a list (or vector) of length 312
    return max(0, x[240])
def l362_217(x):
    # x is a list (or vector) of length 312
    return max(0, x[241])
def l362_218(x):
    # x is a list (or vector) of length 312
    return max(0, x[242])
def l362_219(x):
    # x is a list (or vector) of length 312
    return max(0, x[243])
def l362_220(x):
    # x is a list (or vector) of length 312
    return max(0, x[244])
def l362_221(x):
    # x is a list (or vector) of length 312
    return max(0, x[245])
def l362_222(x):
    # x is a list (or vector) of length 312
    return max(0, x[246])
def l362_223(x):
    # x is a list (or vector) of length 312
    return max(0, x[247])
def l362_224(x):
    # x is a list (or vector) of length 312
    return max(0, x[248])
def l362_225(x):
    # x is a list (or vector) of length 312
    return max(0, x[249])
def l362_226(x):
    # x is a list (or vector) of length 312
    return max(0, x[250])
def l362_227(x):
    # x is a list (or vector) of length 312
    return max(0, x[251])
def l362_228(x):
    # x is a list (or vector) of length 312
    return max(0, x[252])
def l362_229(x):
    # x is a list (or vector) of length 312
    return max(0, x[253])
def l362_230(x):
    # x is a list (or vector) of length 312
    return max(0, x[254])
def l362_231(x):
    # x is a list (or vector) of length 312
    return max(0, x[255])
def l362_232(x):
    # x is a list (or vector) of length 312
    return max(0, x[256])
def l362_233(x):
    # x is a list (or vector) of length 312
    return max(0, x[257])
def l362_234(x):
    # x is a list (or vector) of length 312
    return max(0, x[258])
def l362_235(x):
    # x is a list (or vector) of length 312
    return max(0, x[259])
def l362_236(x):
    # x is a list (or vector) of length 312
    return max(0, x[260])
def l362_237(x):
    # x is a list (or vector) of length 312
    return max(0, x[261])
def l362_238(x):
    # x is a list (or vector) of length 312
    return max(0, x[262])
def l362_239(x):
    # x is a list (or vector) of length 312
    return max(0, x[263])
def l362_240(x):
    # x is a list (or vector) of length 312
    return max(0, x[264])
def l362_241(x):
    # x is a list (or vector) of length 312
    return max(0, x[265])
def l362_242(x):
    # x is a list (or vector) of length 312
    return max(0, x[266])
def l362_243(x):
    # x is a list (or vector) of length 312
    return max(0, x[267])
def l362_244(x):
    # x is a list (or vector) of length 312
    return max(0, x[268])
def l362_245(x):
    # x is a list (or vector) of length 312
    return max(0, x[269])
def l362_246(x):
    # x is a list (or vector) of length 312
    return max(0, x[270])
def l362_247(x):
    # x is a list (or vector) of length 312
    return max(0, x[271])
def l362_248(x):
    # x is a list (or vector) of length 312
    return max(0, x[272])
def l362_249(x):
    # x is a list (or vector) of length 312
    return max(0, x[273])
def l362_250(x):
    # x is a list (or vector) of length 312
    return max(0, x[274])
def l362_251(x):
    # x is a list (or vector) of length 312
    return max(0, x[275])
def l362_252(x):
    # x is a list (or vector) of length 312
    return max(0, x[276])
def l362_253(x):
    # x is a list (or vector) of length 312
    return max(0, x[277])
def l362_254(x):
    # x is a list (or vector) of length 312
    return max(0, x[278])
def l362_255(x):
    # x is a list (or vector) of length 312
    return max(0, x[279])
def l362_256(x):
    # x is a list (or vector) of length 312
    return max(0, x[280])
def l362_257(x):
    # x is a list (or vector) of length 312
    return max(0, x[281])
def l362_258(x):
    # x is a list (or vector) of length 312
    return max(0, x[282])
def l362_259(x):
    # x is a list (or vector) of length 312
    return max(0, x[283])
def l362_260(x):
    # x is a list (or vector) of length 312
    return max(0, x[284])
def l362_261(x):
    # x is a list (or vector) of length 312
    return max(0, x[285])
def l362_262(x):
    # x is a list (or vector) of length 312
    return max(0, x[286])
def l362_263(x):
    # x is a list (or vector) of length 312
    return max(0, x[287])
def l362_264(x):
    # x is a list (or vector) of length 312
    return max(0, x[288])
def l362_265(x):
    # x is a list (or vector) of length 312
    return max(0, x[289])
def l362_266(x):
    # x is a list (or vector) of length 312
    return max(0, x[290])
def l362_267(x):
    # x is a list (or vector) of length 312
    return max(0, x[291])
def l362_268(x):
    # x is a list (or vector) of length 312
    return max(0, x[292])
def l362_269(x):
    # x is a list (or vector) of length 312
    return max(0, x[293])
def l362_270(x):
    # x is a list (or vector) of length 312
    return max(0, x[294])
def l362_271(x):
    # x is a list (or vector) of length 312
    return max(0, x[295])
def l362_272(x):
    # x is a list (or vector) of length 312
    return max(0, x[296])
def l362_273(x):
    # x is a list (or vector) of length 312
    return max(0, x[297])
def l362_274(x):
    # x is a list (or vector) of length 312
    return max(0, x[298])
def l362_275(x):
    # x is a list (or vector) of length 312
    return max(0, x[299])
def l362_276(x):
    # x is a list (or vector) of length 312
    return max(0, x[300])
def l362_277(x):
    # x is a list (or vector) of length 312
    return max(0, x[301])
def l362_278(x):
    # x is a list (or vector) of length 312
    return max(0, x[302])
def l362_279(x):
    # x is a list (or vector) of length 312
    return max(0, x[303])
def l362_280(x):
    # x is a list (or vector) of length 312
    return max(0, x[304])
def l362_281(x):
    # x is a list (or vector) of length 312
    return max(0, x[305])
def l362_282(x):
    # x is a list (or vector) of length 312
    return max(0, x[306])
def l362_283(x):
    # x is a list (or vector) of length 312
    return max(0, x[307])
def l362_284(x):
    # x is a list (or vector) of length 312
    return max(0, x[308])
def l362_285(x):
    # x is a list (or vector) of length 312
    return max(0, x[309])
def l362_286(x):
    # x is a list (or vector) of length 312
    return max(0, x[310])
def l362_287(x):
    # x is a list (or vector) of length 312
    return max(0, x[311])
def l362_(x):
    # x is a list (or vector) of length 312
    return [
        l362_0(x),
        l362_1(x),
        l362_2(x),
        l362_3(x),
        l362_4(x),
        l362_5(x),
        l362_6(x),
        l362_7(x),
        l362_8(x),
        l362_9(x),
        l362_10(x),
        l362_11(x),
        l362_12(x),
        l362_13(x),
        l362_14(x),
        l362_15(x),
        l362_16(x),
        l362_17(x),
        l362_18(x),
        l362_19(x),
        l362_20(x),
        l362_21(x),
        l362_22(x),
        l362_23(x),
        l362_24(x),
        l362_25(x),
        l362_26(x),
        l362_27(x),
        l362_28(x),
        l362_29(x),
        l362_30(x),
        l362_31(x),
        l362_32(x),
        l362_33(x),
        l362_34(x),
        l362_35(x),
        l362_36(x),
        l362_37(x),
        l362_38(x),
        l362_39(x),
        l362_40(x),
        l362_41(x),
        l362_42(x),
        l362_43(x),
        l362_44(x),
        l362_45(x),
        l362_46(x),
        l362_47(x),
        l362_48(x),
        l362_49(x),
        l362_50(x),
        l362_51(x),
        l362_52(x),
        l362_53(x),
        l362_54(x),
        l362_55(x),
        l362_56(x),
        l362_57(x),
        l362_58(x),
        l362_59(x),
        l362_60(x),
        l362_61(x),
        l362_62(x),
        l362_63(x),
        l362_64(x),
        l362_65(x),
        l362_66(x),
        l362_67(x),
        l362_68(x),
        l362_69(x),
        l362_70(x),
        l362_71(x),
        l362_72(x),
        l362_73(x),
        l362_74(x),
        l362_75(x),
        l362_76(x),
        l362_77(x),
        l362_78(x),
        l362_79(x),
        l362_80(x),
        l362_81(x),
        l362_82(x),
        l362_83(x),
        l362_84(x),
        l362_85(x),
        l362_86(x),
        l362_87(x),
        l362_88(x),
        l362_89(x),
        l362_90(x),
        l362_91(x),
        l362_92(x),
        l362_93(x),
        l362_94(x),
        l362_95(x),
        l362_96(x),
        l362_97(x),
        l362_98(x),
        l362_99(x),
        l362_100(x),
        l362_101(x),
        l362_102(x),
        l362_103(x),
        l362_104(x),
        l362_105(x),
        l362_106(x),
        l362_107(x),
        l362_108(x),
        l362_109(x),
        l362_110(x),
        l362_111(x),
        l362_112(x),
        l362_113(x),
        l362_114(x),
        l362_115(x),
        l362_116(x),
        l362_117(x),
        l362_118(x),
        l362_119(x),
        l362_120(x),
        l362_121(x),
        l362_122(x),
        l362_123(x),
        l362_124(x),
        l362_125(x),
        l362_126(x),
        l362_127(x),
        l362_128(x),
        l362_129(x),
        l362_130(x),
        l362_131(x),
        l362_132(x),
        l362_133(x),
        l362_134(x),
        l362_135(x),
        l362_136(x),
        l362_137(x),
        l362_138(x),
        l362_139(x),
        l362_140(x),
        l362_141(x),
        l362_142(x),
        l362_143(x),
        l362_144(x),
        l362_145(x),
        l362_146(x),
        l362_147(x),
        l362_148(x),
        l362_149(x),
        l362_150(x),
        l362_151(x),
        l362_152(x),
        l362_153(x),
        l362_154(x),
        l362_155(x),
        l362_156(x),
        l362_157(x),
        l362_158(x),
        l362_159(x),
        l362_160(x),
        l362_161(x),
        l362_162(x),
        l362_163(x),
        l362_164(x),
        l362_165(x),
        l362_166(x),
        l362_167(x),
        l362_168(x),
        l362_169(x),
        l362_170(x),
        l362_171(x),
        l362_172(x),
        l362_173(x),
        l362_174(x),
        l362_175(x),
        l362_176(x),
        l362_177(x),
        l362_178(x),
        l362_179(x),
        l362_180(x),
        l362_181(x),
        l362_182(x),
        l362_183(x),
        l362_184(x),
        l362_185(x),
        l362_186(x),
        l362_187(x),
        l362_188(x),
        l362_189(x),
        l362_190(x),
        l362_191(x),
        l362_192(x),
        l362_193(x),
        l362_194(x),
        l362_195(x),
        l362_196(x),
        l362_197(x),
        l362_198(x),
        l362_199(x),
        l362_200(x),
        l362_201(x),
        l362_202(x),
        l362_203(x),
        l362_204(x),
        l362_205(x),
        l362_206(x),
        l362_207(x),
        l362_208(x),
        l362_209(x),
        l362_210(x),
        l362_211(x),
        l362_212(x),
        l362_213(x),
        l362_214(x),
        l362_215(x),
        l362_216(x),
        l362_217(x),
        l362_218(x),
        l362_219(x),
        l362_220(x),
        l362_221(x),
        l362_222(x),
        l362_223(x),
        l362_224(x),
        l362_225(x),
        l362_226(x),
        l362_227(x),
        l362_228(x),
        l362_229(x),
        l362_230(x),
        l362_231(x),
        l362_232(x),
        l362_233(x),
        l362_234(x),
        l362_235(x),
        l362_236(x),
        l362_237(x),
        l362_238(x),
        l362_239(x),
        l362_240(x),
        l362_241(x),
        l362_242(x),
        l362_243(x),
        l362_244(x),
        l362_245(x),
        l362_246(x),
        l362_247(x),
        l362_248(x),
        l362_249(x),
        l362_250(x),
        l362_251(x),
        l362_252(x),
        l362_253(x),
        l362_254(x),
        l362_255(x),
        l362_256(x),
        l362_257(x),
        l362_258(x),
        l362_259(x),
        l362_260(x),
        l362_261(x),
        l362_262(x),
        l362_263(x),
        l362_264(x),
        l362_265(x),
        l362_266(x),
        l362_267(x),
        l362_268(x),
        l362_269(x),
        l362_270(x),
        l362_271(x),
        l362_272(x),
        l362_273(x),
        l362_274(x),
        l362_275(x),
        l362_276(x),
        l362_277(x),
        l362_278(x),
        l362_279(x),
        l362_280(x),
        l362_281(x),
        l362_282(x),
        l362_283(x),
        l362_284(x),
        l362_285(x),
        l362_286(x),
        l362_287(x),
    ]