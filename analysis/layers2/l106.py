import numpy as np




# Generated from reverse engineering
def l106_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 288
    out = np.empty(288, dtype=np.float32)
    
    # for i in range(0, 36):
    for i in range(0, 36):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xfffffff (len=28)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(36, 64):
    for i in range(0, 28):
        s = -1 * x[36 + i] + -1 * x[64 + i]
        s += biases[i]
        out[36 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 68):
    for i in range(0, 4):
        s = x[120 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(68, 96):
    for i in range(0, 28):
        s = x[92 + i]
        out[68 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 288):
    for i in range(0, 192):
        s = x[124 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l106_0(x):
    # x is a list (or vector) of length 316
    return max(0, x[0])
def l106_1(x):
    # x is a list (or vector) of length 316
    return max(0, x[1])
def l106_2(x):
    # x is a list (or vector) of length 316
    return max(0, x[2])
def l106_3(x):
    # x is a list (or vector) of length 316
    return max(0, x[3])
def l106_4(x):
    # x is a list (or vector) of length 316
    return max(0, x[4])
def l106_5(x):
    # x is a list (or vector) of length 316
    return max(0, x[5])
def l106_6(x):
    # x is a list (or vector) of length 316
    return max(0, x[6])
def l106_7(x):
    # x is a list (or vector) of length 316
    return max(0, x[7])
def l106_8(x):
    # x is a list (or vector) of length 316
    return max(0, x[8])
def l106_9(x):
    # x is a list (or vector) of length 316
    return max(0, x[9])
def l106_10(x):
    # x is a list (or vector) of length 316
    return max(0, x[10])
def l106_11(x):
    # x is a list (or vector) of length 316
    return max(0, x[11])
def l106_12(x):
    # x is a list (or vector) of length 316
    return max(0, x[12])
def l106_13(x):
    # x is a list (or vector) of length 316
    return max(0, x[13])
def l106_14(x):
    # x is a list (or vector) of length 316
    return max(0, x[14])
def l106_15(x):
    # x is a list (or vector) of length 316
    return max(0, x[15])
def l106_16(x):
    # x is a list (or vector) of length 316
    return max(0, x[16])
def l106_17(x):
    # x is a list (or vector) of length 316
    return max(0, x[17])
def l106_18(x):
    # x is a list (or vector) of length 316
    return max(0, x[18])
def l106_19(x):
    # x is a list (or vector) of length 316
    return max(0, x[19])
def l106_20(x):
    # x is a list (or vector) of length 316
    return max(0, x[20])
def l106_21(x):
    # x is a list (or vector) of length 316
    return max(0, x[21])
def l106_22(x):
    # x is a list (or vector) of length 316
    return max(0, x[22])
def l106_23(x):
    # x is a list (or vector) of length 316
    return max(0, x[23])
def l106_24(x):
    # x is a list (or vector) of length 316
    return max(0, x[24])
def l106_25(x):
    # x is a list (or vector) of length 316
    return max(0, x[25])
def l106_26(x):
    # x is a list (or vector) of length 316
    return max(0, x[26])
def l106_27(x):
    # x is a list (or vector) of length 316
    return max(0, x[27])
def l106_28(x):
    # x is a list (or vector) of length 316
    return max(0, x[28])
def l106_29(x):
    # x is a list (or vector) of length 316
    return max(0, x[29])
def l106_30(x):
    # x is a list (or vector) of length 316
    return max(0, x[30])
def l106_31(x):
    # x is a list (or vector) of length 316
    return max(0, x[31])
def l106_32(x):
    # x is a list (or vector) of length 316
    return max(0, x[32])
def l106_33(x):
    # x is a list (or vector) of length 316
    return max(0, x[33])
def l106_34(x):
    # x is a list (or vector) of length 316
    return max(0, x[34])
def l106_35(x):
    # x is a list (or vector) of length 316
    return max(0, x[35])
def l106_36(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[36] + -1.0*x[64] + 1.0)
def l106_37(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[37] + -1.0*x[65] + 1.0)
def l106_38(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[38] + -1.0*x[66] + 1.0)
def l106_39(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[39] + -1.0*x[67] + 1.0)
def l106_40(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[40] + -1.0*x[68] + 1.0)
def l106_41(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[41] + -1.0*x[69] + 1.0)
def l106_42(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[42] + -1.0*x[70] + 1.0)
def l106_43(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[43] + -1.0*x[71] + 1.0)
def l106_44(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[44] + -1.0*x[72] + 1.0)
def l106_45(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[45] + -1.0*x[73] + 1.0)
def l106_46(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[46] + -1.0*x[74] + 1.0)
def l106_47(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[47] + -1.0*x[75] + 1.0)
def l106_48(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[48] + -1.0*x[76] + 1.0)
def l106_49(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[49] + -1.0*x[77] + 1.0)
def l106_50(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[50] + -1.0*x[78] + 1.0)
def l106_51(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[51] + -1.0*x[79] + 1.0)
def l106_52(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[52] + -1.0*x[80] + 1.0)
def l106_53(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[53] + -1.0*x[81] + 1.0)
def l106_54(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[54] + -1.0*x[82] + 1.0)
def l106_55(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[55] + -1.0*x[83] + 1.0)
def l106_56(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[56] + -1.0*x[84] + 1.0)
def l106_57(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[57] + -1.0*x[85] + 1.0)
def l106_58(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[58] + -1.0*x[86] + 1.0)
def l106_59(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[59] + -1.0*x[87] + 1.0)
def l106_60(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[60] + -1.0*x[88] + 1.0)
def l106_61(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[61] + -1.0*x[89] + 1.0)
def l106_62(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[62] + -1.0*x[90] + 1.0)
def l106_63(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[63] + -1.0*x[91] + 1.0)
def l106_64(x):
    # x is a list (or vector) of length 316
    return max(0, x[120])
def l106_65(x):
    # x is a list (or vector) of length 316
    return max(0, x[121])
def l106_66(x):
    # x is a list (or vector) of length 316
    return max(0, x[122])
def l106_67(x):
    # x is a list (or vector) of length 316
    return max(0, x[123])
def l106_68(x):
    # x is a list (or vector) of length 316
    return max(0, x[92])
def l106_69(x):
    # x is a list (or vector) of length 316
    return max(0, x[93])
def l106_70(x):
    # x is a list (or vector) of length 316
    return max(0, x[94])
def l106_71(x):
    # x is a list (or vector) of length 316
    return max(0, x[95])
def l106_72(x):
    # x is a list (or vector) of length 316
    return max(0, x[96])
def l106_73(x):
    # x is a list (or vector) of length 316
    return max(0, x[97])
def l106_74(x):
    # x is a list (or vector) of length 316
    return max(0, x[98])
def l106_75(x):
    # x is a list (or vector) of length 316
    return max(0, x[99])
def l106_76(x):
    # x is a list (or vector) of length 316
    return max(0, x[100])
def l106_77(x):
    # x is a list (or vector) of length 316
    return max(0, x[101])
def l106_78(x):
    # x is a list (or vector) of length 316
    return max(0, x[102])
def l106_79(x):
    # x is a list (or vector) of length 316
    return max(0, x[103])
def l106_80(x):
    # x is a list (or vector) of length 316
    return max(0, x[104])
def l106_81(x):
    # x is a list (or vector) of length 316
    return max(0, x[105])
def l106_82(x):
    # x is a list (or vector) of length 316
    return max(0, x[106])
def l106_83(x):
    # x is a list (or vector) of length 316
    return max(0, x[107])
def l106_84(x):
    # x is a list (or vector) of length 316
    return max(0, x[108])
def l106_85(x):
    # x is a list (or vector) of length 316
    return max(0, x[109])
def l106_86(x):
    # x is a list (or vector) of length 316
    return max(0, x[110])
def l106_87(x):
    # x is a list (or vector) of length 316
    return max(0, x[111])
def l106_88(x):
    # x is a list (or vector) of length 316
    return max(0, x[112])
def l106_89(x):
    # x is a list (or vector) of length 316
    return max(0, x[113])
def l106_90(x):
    # x is a list (or vector) of length 316
    return max(0, x[114])
def l106_91(x):
    # x is a list (or vector) of length 316
    return max(0, x[115])
def l106_92(x):
    # x is a list (or vector) of length 316
    return max(0, x[116])
def l106_93(x):
    # x is a list (or vector) of length 316
    return max(0, x[117])
def l106_94(x):
    # x is a list (or vector) of length 316
    return max(0, x[118])
def l106_95(x):
    # x is a list (or vector) of length 316
    return max(0, x[119])
def l106_96(x):
    # x is a list (or vector) of length 316
    return max(0, x[124])
def l106_97(x):
    # x is a list (or vector) of length 316
    return max(0, x[125])
def l106_98(x):
    # x is a list (or vector) of length 316
    return max(0, x[126])
def l106_99(x):
    # x is a list (or vector) of length 316
    return max(0, x[127])
def l106_100(x):
    # x is a list (or vector) of length 316
    return max(0, x[128])
def l106_101(x):
    # x is a list (or vector) of length 316
    return max(0, x[129])
def l106_102(x):
    # x is a list (or vector) of length 316
    return max(0, x[130])
def l106_103(x):
    # x is a list (or vector) of length 316
    return max(0, x[131])
def l106_104(x):
    # x is a list (or vector) of length 316
    return max(0, x[132])
def l106_105(x):
    # x is a list (or vector) of length 316
    return max(0, x[133])
def l106_106(x):
    # x is a list (or vector) of length 316
    return max(0, x[134])
def l106_107(x):
    # x is a list (or vector) of length 316
    return max(0, x[135])
def l106_108(x):
    # x is a list (or vector) of length 316
    return max(0, x[136])
def l106_109(x):
    # x is a list (or vector) of length 316
    return max(0, x[137])
def l106_110(x):
    # x is a list (or vector) of length 316
    return max(0, x[138])
def l106_111(x):
    # x is a list (or vector) of length 316
    return max(0, x[139])
def l106_112(x):
    # x is a list (or vector) of length 316
    return max(0, x[140])
def l106_113(x):
    # x is a list (or vector) of length 316
    return max(0, x[141])
def l106_114(x):
    # x is a list (or vector) of length 316
    return max(0, x[142])
def l106_115(x):
    # x is a list (or vector) of length 316
    return max(0, x[143])
def l106_116(x):
    # x is a list (or vector) of length 316
    return max(0, x[144])
def l106_117(x):
    # x is a list (or vector) of length 316
    return max(0, x[145])
def l106_118(x):
    # x is a list (or vector) of length 316
    return max(0, x[146])
def l106_119(x):
    # x is a list (or vector) of length 316
    return max(0, x[147])
def l106_120(x):
    # x is a list (or vector) of length 316
    return max(0, x[148])
def l106_121(x):
    # x is a list (or vector) of length 316
    return max(0, x[149])
def l106_122(x):
    # x is a list (or vector) of length 316
    return max(0, x[150])
def l106_123(x):
    # x is a list (or vector) of length 316
    return max(0, x[151])
def l106_124(x):
    # x is a list (or vector) of length 316
    return max(0, x[152])
def l106_125(x):
    # x is a list (or vector) of length 316
    return max(0, x[153])
def l106_126(x):
    # x is a list (or vector) of length 316
    return max(0, x[154])
def l106_127(x):
    # x is a list (or vector) of length 316
    return max(0, x[155])
def l106_128(x):
    # x is a list (or vector) of length 316
    return max(0, x[156])
def l106_129(x):
    # x is a list (or vector) of length 316
    return max(0, x[157])
def l106_130(x):
    # x is a list (or vector) of length 316
    return max(0, x[158])
def l106_131(x):
    # x is a list (or vector) of length 316
    return max(0, x[159])
def l106_132(x):
    # x is a list (or vector) of length 316
    return max(0, x[160])
def l106_133(x):
    # x is a list (or vector) of length 316
    return max(0, x[161])
def l106_134(x):
    # x is a list (or vector) of length 316
    return max(0, x[162])
def l106_135(x):
    # x is a list (or vector) of length 316
    return max(0, x[163])
def l106_136(x):
    # x is a list (or vector) of length 316
    return max(0, x[164])
def l106_137(x):
    # x is a list (or vector) of length 316
    return max(0, x[165])
def l106_138(x):
    # x is a list (or vector) of length 316
    return max(0, x[166])
def l106_139(x):
    # x is a list (or vector) of length 316
    return max(0, x[167])
def l106_140(x):
    # x is a list (or vector) of length 316
    return max(0, x[168])
def l106_141(x):
    # x is a list (or vector) of length 316
    return max(0, x[169])
def l106_142(x):
    # x is a list (or vector) of length 316
    return max(0, x[170])
def l106_143(x):
    # x is a list (or vector) of length 316
    return max(0, x[171])
def l106_144(x):
    # x is a list (or vector) of length 316
    return max(0, x[172])
def l106_145(x):
    # x is a list (or vector) of length 316
    return max(0, x[173])
def l106_146(x):
    # x is a list (or vector) of length 316
    return max(0, x[174])
def l106_147(x):
    # x is a list (or vector) of length 316
    return max(0, x[175])
def l106_148(x):
    # x is a list (or vector) of length 316
    return max(0, x[176])
def l106_149(x):
    # x is a list (or vector) of length 316
    return max(0, x[177])
def l106_150(x):
    # x is a list (or vector) of length 316
    return max(0, x[178])
def l106_151(x):
    # x is a list (or vector) of length 316
    return max(0, x[179])
def l106_152(x):
    # x is a list (or vector) of length 316
    return max(0, x[180])
def l106_153(x):
    # x is a list (or vector) of length 316
    return max(0, x[181])
def l106_154(x):
    # x is a list (or vector) of length 316
    return max(0, x[182])
def l106_155(x):
    # x is a list (or vector) of length 316
    return max(0, x[183])
def l106_156(x):
    # x is a list (or vector) of length 316
    return max(0, x[184])
def l106_157(x):
    # x is a list (or vector) of length 316
    return max(0, x[185])
def l106_158(x):
    # x is a list (or vector) of length 316
    return max(0, x[186])
def l106_159(x):
    # x is a list (or vector) of length 316
    return max(0, x[187])
def l106_160(x):
    # x is a list (or vector) of length 316
    return max(0, x[188])
def l106_161(x):
    # x is a list (or vector) of length 316
    return max(0, x[189])
def l106_162(x):
    # x is a list (or vector) of length 316
    return max(0, x[190])
def l106_163(x):
    # x is a list (or vector) of length 316
    return max(0, x[191])
def l106_164(x):
    # x is a list (or vector) of length 316
    return max(0, x[192])
def l106_165(x):
    # x is a list (or vector) of length 316
    return max(0, x[193])
def l106_166(x):
    # x is a list (or vector) of length 316
    return max(0, x[194])
def l106_167(x):
    # x is a list (or vector) of length 316
    return max(0, x[195])
def l106_168(x):
    # x is a list (or vector) of length 316
    return max(0, x[196])
def l106_169(x):
    # x is a list (or vector) of length 316
    return max(0, x[197])
def l106_170(x):
    # x is a list (or vector) of length 316
    return max(0, x[198])
def l106_171(x):
    # x is a list (or vector) of length 316
    return max(0, x[199])
def l106_172(x):
    # x is a list (or vector) of length 316
    return max(0, x[200])
def l106_173(x):
    # x is a list (or vector) of length 316
    return max(0, x[201])
def l106_174(x):
    # x is a list (or vector) of length 316
    return max(0, x[202])
def l106_175(x):
    # x is a list (or vector) of length 316
    return max(0, x[203])
def l106_176(x):
    # x is a list (or vector) of length 316
    return max(0, x[204])
def l106_177(x):
    # x is a list (or vector) of length 316
    return max(0, x[205])
def l106_178(x):
    # x is a list (or vector) of length 316
    return max(0, x[206])
def l106_179(x):
    # x is a list (or vector) of length 316
    return max(0, x[207])
def l106_180(x):
    # x is a list (or vector) of length 316
    return max(0, x[208])
def l106_181(x):
    # x is a list (or vector) of length 316
    return max(0, x[209])
def l106_182(x):
    # x is a list (or vector) of length 316
    return max(0, x[210])
def l106_183(x):
    # x is a list (or vector) of length 316
    return max(0, x[211])
def l106_184(x):
    # x is a list (or vector) of length 316
    return max(0, x[212])
def l106_185(x):
    # x is a list (or vector) of length 316
    return max(0, x[213])
def l106_186(x):
    # x is a list (or vector) of length 316
    return max(0, x[214])
def l106_187(x):
    # x is a list (or vector) of length 316
    return max(0, x[215])
def l106_188(x):
    # x is a list (or vector) of length 316
    return max(0, x[216])
def l106_189(x):
    # x is a list (or vector) of length 316
    return max(0, x[217])
def l106_190(x):
    # x is a list (or vector) of length 316
    return max(0, x[218])
def l106_191(x):
    # x is a list (or vector) of length 316
    return max(0, x[219])
def l106_192(x):
    # x is a list (or vector) of length 316
    return max(0, x[220])
def l106_193(x):
    # x is a list (or vector) of length 316
    return max(0, x[221])
def l106_194(x):
    # x is a list (or vector) of length 316
    return max(0, x[222])
def l106_195(x):
    # x is a list (or vector) of length 316
    return max(0, x[223])
def l106_196(x):
    # x is a list (or vector) of length 316
    return max(0, x[224])
def l106_197(x):
    # x is a list (or vector) of length 316
    return max(0, x[225])
def l106_198(x):
    # x is a list (or vector) of length 316
    return max(0, x[226])
def l106_199(x):
    # x is a list (or vector) of length 316
    return max(0, x[227])
def l106_200(x):
    # x is a list (or vector) of length 316
    return max(0, x[228])
def l106_201(x):
    # x is a list (or vector) of length 316
    return max(0, x[229])
def l106_202(x):
    # x is a list (or vector) of length 316
    return max(0, x[230])
def l106_203(x):
    # x is a list (or vector) of length 316
    return max(0, x[231])
def l106_204(x):
    # x is a list (or vector) of length 316
    return max(0, x[232])
def l106_205(x):
    # x is a list (or vector) of length 316
    return max(0, x[233])
def l106_206(x):
    # x is a list (or vector) of length 316
    return max(0, x[234])
def l106_207(x):
    # x is a list (or vector) of length 316
    return max(0, x[235])
def l106_208(x):
    # x is a list (or vector) of length 316
    return max(0, x[236])
def l106_209(x):
    # x is a list (or vector) of length 316
    return max(0, x[237])
def l106_210(x):
    # x is a list (or vector) of length 316
    return max(0, x[238])
def l106_211(x):
    # x is a list (or vector) of length 316
    return max(0, x[239])
def l106_212(x):
    # x is a list (or vector) of length 316
    return max(0, x[240])
def l106_213(x):
    # x is a list (or vector) of length 316
    return max(0, x[241])
def l106_214(x):
    # x is a list (or vector) of length 316
    return max(0, x[242])
def l106_215(x):
    # x is a list (or vector) of length 316
    return max(0, x[243])
def l106_216(x):
    # x is a list (or vector) of length 316
    return max(0, x[244])
def l106_217(x):
    # x is a list (or vector) of length 316
    return max(0, x[245])
def l106_218(x):
    # x is a list (or vector) of length 316
    return max(0, x[246])
def l106_219(x):
    # x is a list (or vector) of length 316
    return max(0, x[247])
def l106_220(x):
    # x is a list (or vector) of length 316
    return max(0, x[248])
def l106_221(x):
    # x is a list (or vector) of length 316
    return max(0, x[249])
def l106_222(x):
    # x is a list (or vector) of length 316
    return max(0, x[250])
def l106_223(x):
    # x is a list (or vector) of length 316
    return max(0, x[251])
def l106_224(x):
    # x is a list (or vector) of length 316
    return max(0, x[252])
def l106_225(x):
    # x is a list (or vector) of length 316
    return max(0, x[253])
def l106_226(x):
    # x is a list (or vector) of length 316
    return max(0, x[254])
def l106_227(x):
    # x is a list (or vector) of length 316
    return max(0, x[255])
def l106_228(x):
    # x is a list (or vector) of length 316
    return max(0, x[256])
def l106_229(x):
    # x is a list (or vector) of length 316
    return max(0, x[257])
def l106_230(x):
    # x is a list (or vector) of length 316
    return max(0, x[258])
def l106_231(x):
    # x is a list (or vector) of length 316
    return max(0, x[259])
def l106_232(x):
    # x is a list (or vector) of length 316
    return max(0, x[260])
def l106_233(x):
    # x is a list (or vector) of length 316
    return max(0, x[261])
def l106_234(x):
    # x is a list (or vector) of length 316
    return max(0, x[262])
def l106_235(x):
    # x is a list (or vector) of length 316
    return max(0, x[263])
def l106_236(x):
    # x is a list (or vector) of length 316
    return max(0, x[264])
def l106_237(x):
    # x is a list (or vector) of length 316
    return max(0, x[265])
def l106_238(x):
    # x is a list (or vector) of length 316
    return max(0, x[266])
def l106_239(x):
    # x is a list (or vector) of length 316
    return max(0, x[267])
def l106_240(x):
    # x is a list (or vector) of length 316
    return max(0, x[268])
def l106_241(x):
    # x is a list (or vector) of length 316
    return max(0, x[269])
def l106_242(x):
    # x is a list (or vector) of length 316
    return max(0, x[270])
def l106_243(x):
    # x is a list (or vector) of length 316
    return max(0, x[271])
def l106_244(x):
    # x is a list (or vector) of length 316
    return max(0, x[272])
def l106_245(x):
    # x is a list (or vector) of length 316
    return max(0, x[273])
def l106_246(x):
    # x is a list (or vector) of length 316
    return max(0, x[274])
def l106_247(x):
    # x is a list (or vector) of length 316
    return max(0, x[275])
def l106_248(x):
    # x is a list (or vector) of length 316
    return max(0, x[276])
def l106_249(x):
    # x is a list (or vector) of length 316
    return max(0, x[277])
def l106_250(x):
    # x is a list (or vector) of length 316
    return max(0, x[278])
def l106_251(x):
    # x is a list (or vector) of length 316
    return max(0, x[279])
def l106_252(x):
    # x is a list (or vector) of length 316
    return max(0, x[280])
def l106_253(x):
    # x is a list (or vector) of length 316
    return max(0, x[281])
def l106_254(x):
    # x is a list (or vector) of length 316
    return max(0, x[282])
def l106_255(x):
    # x is a list (or vector) of length 316
    return max(0, x[283])
def l106_256(x):
    # x is a list (or vector) of length 316
    return max(0, x[284])
def l106_257(x):
    # x is a list (or vector) of length 316
    return max(0, x[285])
def l106_258(x):
    # x is a list (or vector) of length 316
    return max(0, x[286])
def l106_259(x):
    # x is a list (or vector) of length 316
    return max(0, x[287])
def l106_260(x):
    # x is a list (or vector) of length 316
    return max(0, x[288])
def l106_261(x):
    # x is a list (or vector) of length 316
    return max(0, x[289])
def l106_262(x):
    # x is a list (or vector) of length 316
    return max(0, x[290])
def l106_263(x):
    # x is a list (or vector) of length 316
    return max(0, x[291])
def l106_264(x):
    # x is a list (or vector) of length 316
    return max(0, x[292])
def l106_265(x):
    # x is a list (or vector) of length 316
    return max(0, x[293])
def l106_266(x):
    # x is a list (or vector) of length 316
    return max(0, x[294])
def l106_267(x):
    # x is a list (or vector) of length 316
    return max(0, x[295])
def l106_268(x):
    # x is a list (or vector) of length 316
    return max(0, x[296])
def l106_269(x):
    # x is a list (or vector) of length 316
    return max(0, x[297])
def l106_270(x):
    # x is a list (or vector) of length 316
    return max(0, x[298])
def l106_271(x):
    # x is a list (or vector) of length 316
    return max(0, x[299])
def l106_272(x):
    # x is a list (or vector) of length 316
    return max(0, x[300])
def l106_273(x):
    # x is a list (or vector) of length 316
    return max(0, x[301])
def l106_274(x):
    # x is a list (or vector) of length 316
    return max(0, x[302])
def l106_275(x):
    # x is a list (or vector) of length 316
    return max(0, x[303])
def l106_276(x):
    # x is a list (or vector) of length 316
    return max(0, x[304])
def l106_277(x):
    # x is a list (or vector) of length 316
    return max(0, x[305])
def l106_278(x):
    # x is a list (or vector) of length 316
    return max(0, x[306])
def l106_279(x):
    # x is a list (or vector) of length 316
    return max(0, x[307])
def l106_280(x):
    # x is a list (or vector) of length 316
    return max(0, x[308])
def l106_281(x):
    # x is a list (or vector) of length 316
    return max(0, x[309])
def l106_282(x):
    # x is a list (or vector) of length 316
    return max(0, x[310])
def l106_283(x):
    # x is a list (or vector) of length 316
    return max(0, x[311])
def l106_284(x):
    # x is a list (or vector) of length 316
    return max(0, x[312])
def l106_285(x):
    # x is a list (or vector) of length 316
    return max(0, x[313])
def l106_286(x):
    # x is a list (or vector) of length 316
    return max(0, x[314])
def l106_287(x):
    # x is a list (or vector) of length 316
    return max(0, x[315])
def l106_(x):
    # x is a list (or vector) of length 316
    return [
        l106_0(x),
        l106_1(x),
        l106_2(x),
        l106_3(x),
        l106_4(x),
        l106_5(x),
        l106_6(x),
        l106_7(x),
        l106_8(x),
        l106_9(x),
        l106_10(x),
        l106_11(x),
        l106_12(x),
        l106_13(x),
        l106_14(x),
        l106_15(x),
        l106_16(x),
        l106_17(x),
        l106_18(x),
        l106_19(x),
        l106_20(x),
        l106_21(x),
        l106_22(x),
        l106_23(x),
        l106_24(x),
        l106_25(x),
        l106_26(x),
        l106_27(x),
        l106_28(x),
        l106_29(x),
        l106_30(x),
        l106_31(x),
        l106_32(x),
        l106_33(x),
        l106_34(x),
        l106_35(x),
        l106_36(x),
        l106_37(x),
        l106_38(x),
        l106_39(x),
        l106_40(x),
        l106_41(x),
        l106_42(x),
        l106_43(x),
        l106_44(x),
        l106_45(x),
        l106_46(x),
        l106_47(x),
        l106_48(x),
        l106_49(x),
        l106_50(x),
        l106_51(x),
        l106_52(x),
        l106_53(x),
        l106_54(x),
        l106_55(x),
        l106_56(x),
        l106_57(x),
        l106_58(x),
        l106_59(x),
        l106_60(x),
        l106_61(x),
        l106_62(x),
        l106_63(x),
        l106_64(x),
        l106_65(x),
        l106_66(x),
        l106_67(x),
        l106_68(x),
        l106_69(x),
        l106_70(x),
        l106_71(x),
        l106_72(x),
        l106_73(x),
        l106_74(x),
        l106_75(x),
        l106_76(x),
        l106_77(x),
        l106_78(x),
        l106_79(x),
        l106_80(x),
        l106_81(x),
        l106_82(x),
        l106_83(x),
        l106_84(x),
        l106_85(x),
        l106_86(x),
        l106_87(x),
        l106_88(x),
        l106_89(x),
        l106_90(x),
        l106_91(x),
        l106_92(x),
        l106_93(x),
        l106_94(x),
        l106_95(x),
        l106_96(x),
        l106_97(x),
        l106_98(x),
        l106_99(x),
        l106_100(x),
        l106_101(x),
        l106_102(x),
        l106_103(x),
        l106_104(x),
        l106_105(x),
        l106_106(x),
        l106_107(x),
        l106_108(x),
        l106_109(x),
        l106_110(x),
        l106_111(x),
        l106_112(x),
        l106_113(x),
        l106_114(x),
        l106_115(x),
        l106_116(x),
        l106_117(x),
        l106_118(x),
        l106_119(x),
        l106_120(x),
        l106_121(x),
        l106_122(x),
        l106_123(x),
        l106_124(x),
        l106_125(x),
        l106_126(x),
        l106_127(x),
        l106_128(x),
        l106_129(x),
        l106_130(x),
        l106_131(x),
        l106_132(x),
        l106_133(x),
        l106_134(x),
        l106_135(x),
        l106_136(x),
        l106_137(x),
        l106_138(x),
        l106_139(x),
        l106_140(x),
        l106_141(x),
        l106_142(x),
        l106_143(x),
        l106_144(x),
        l106_145(x),
        l106_146(x),
        l106_147(x),
        l106_148(x),
        l106_149(x),
        l106_150(x),
        l106_151(x),
        l106_152(x),
        l106_153(x),
        l106_154(x),
        l106_155(x),
        l106_156(x),
        l106_157(x),
        l106_158(x),
        l106_159(x),
        l106_160(x),
        l106_161(x),
        l106_162(x),
        l106_163(x),
        l106_164(x),
        l106_165(x),
        l106_166(x),
        l106_167(x),
        l106_168(x),
        l106_169(x),
        l106_170(x),
        l106_171(x),
        l106_172(x),
        l106_173(x),
        l106_174(x),
        l106_175(x),
        l106_176(x),
        l106_177(x),
        l106_178(x),
        l106_179(x),
        l106_180(x),
        l106_181(x),
        l106_182(x),
        l106_183(x),
        l106_184(x),
        l106_185(x),
        l106_186(x),
        l106_187(x),
        l106_188(x),
        l106_189(x),
        l106_190(x),
        l106_191(x),
        l106_192(x),
        l106_193(x),
        l106_194(x),
        l106_195(x),
        l106_196(x),
        l106_197(x),
        l106_198(x),
        l106_199(x),
        l106_200(x),
        l106_201(x),
        l106_202(x),
        l106_203(x),
        l106_204(x),
        l106_205(x),
        l106_206(x),
        l106_207(x),
        l106_208(x),
        l106_209(x),
        l106_210(x),
        l106_211(x),
        l106_212(x),
        l106_213(x),
        l106_214(x),
        l106_215(x),
        l106_216(x),
        l106_217(x),
        l106_218(x),
        l106_219(x),
        l106_220(x),
        l106_221(x),
        l106_222(x),
        l106_223(x),
        l106_224(x),
        l106_225(x),
        l106_226(x),
        l106_227(x),
        l106_228(x),
        l106_229(x),
        l106_230(x),
        l106_231(x),
        l106_232(x),
        l106_233(x),
        l106_234(x),
        l106_235(x),
        l106_236(x),
        l106_237(x),
        l106_238(x),
        l106_239(x),
        l106_240(x),
        l106_241(x),
        l106_242(x),
        l106_243(x),
        l106_244(x),
        l106_245(x),
        l106_246(x),
        l106_247(x),
        l106_248(x),
        l106_249(x),
        l106_250(x),
        l106_251(x),
        l106_252(x),
        l106_253(x),
        l106_254(x),
        l106_255(x),
        l106_256(x),
        l106_257(x),
        l106_258(x),
        l106_259(x),
        l106_260(x),
        l106_261(x),
        l106_262(x),
        l106_263(x),
        l106_264(x),
        l106_265(x),
        l106_266(x),
        l106_267(x),
        l106_268(x),
        l106_269(x),
        l106_270(x),
        l106_271(x),
        l106_272(x),
        l106_273(x),
        l106_274(x),
        l106_275(x),
        l106_276(x),
        l106_277(x),
        l106_278(x),
        l106_279(x),
        l106_280(x),
        l106_281(x),
        l106_282(x),
        l106_283(x),
        l106_284(x),
        l106_285(x),
        l106_286(x),
        l106_287(x),
    ]