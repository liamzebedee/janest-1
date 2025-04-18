import numpy as np




# Generated from reverse engineering
def l274_g(x: np.ndarray) -> np.ndarray:
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




def l274_0(x):
    # x is a list (or vector) of length 316
    return max(0, x[0])
def l274_1(x):
    # x is a list (or vector) of length 316
    return max(0, x[1])
def l274_2(x):
    # x is a list (or vector) of length 316
    return max(0, x[2])
def l274_3(x):
    # x is a list (or vector) of length 316
    return max(0, x[3])
def l274_4(x):
    # x is a list (or vector) of length 316
    return max(0, x[4])
def l274_5(x):
    # x is a list (or vector) of length 316
    return max(0, x[5])
def l274_6(x):
    # x is a list (or vector) of length 316
    return max(0, x[6])
def l274_7(x):
    # x is a list (or vector) of length 316
    return max(0, x[7])
def l274_8(x):
    # x is a list (or vector) of length 316
    return max(0, x[8])
def l274_9(x):
    # x is a list (or vector) of length 316
    return max(0, x[9])
def l274_10(x):
    # x is a list (or vector) of length 316
    return max(0, x[10])
def l274_11(x):
    # x is a list (or vector) of length 316
    return max(0, x[11])
def l274_12(x):
    # x is a list (or vector) of length 316
    return max(0, x[12])
def l274_13(x):
    # x is a list (or vector) of length 316
    return max(0, x[13])
def l274_14(x):
    # x is a list (or vector) of length 316
    return max(0, x[14])
def l274_15(x):
    # x is a list (or vector) of length 316
    return max(0, x[15])
def l274_16(x):
    # x is a list (or vector) of length 316
    return max(0, x[16])
def l274_17(x):
    # x is a list (or vector) of length 316
    return max(0, x[17])
def l274_18(x):
    # x is a list (or vector) of length 316
    return max(0, x[18])
def l274_19(x):
    # x is a list (or vector) of length 316
    return max(0, x[19])
def l274_20(x):
    # x is a list (or vector) of length 316
    return max(0, x[20])
def l274_21(x):
    # x is a list (or vector) of length 316
    return max(0, x[21])
def l274_22(x):
    # x is a list (or vector) of length 316
    return max(0, x[22])
def l274_23(x):
    # x is a list (or vector) of length 316
    return max(0, x[23])
def l274_24(x):
    # x is a list (or vector) of length 316
    return max(0, x[24])
def l274_25(x):
    # x is a list (or vector) of length 316
    return max(0, x[25])
def l274_26(x):
    # x is a list (or vector) of length 316
    return max(0, x[26])
def l274_27(x):
    # x is a list (or vector) of length 316
    return max(0, x[27])
def l274_28(x):
    # x is a list (or vector) of length 316
    return max(0, x[28])
def l274_29(x):
    # x is a list (or vector) of length 316
    return max(0, x[29])
def l274_30(x):
    # x is a list (or vector) of length 316
    return max(0, x[30])
def l274_31(x):
    # x is a list (or vector) of length 316
    return max(0, x[31])
def l274_32(x):
    # x is a list (or vector) of length 316
    return max(0, x[32])
def l274_33(x):
    # x is a list (or vector) of length 316
    return max(0, x[33])
def l274_34(x):
    # x is a list (or vector) of length 316
    return max(0, x[34])
def l274_35(x):
    # x is a list (or vector) of length 316
    return max(0, x[35])
def l274_36(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[36] + -1.0*x[64] + 1.0)
def l274_37(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[37] + -1.0*x[65] + 1.0)
def l274_38(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[38] + -1.0*x[66] + 1.0)
def l274_39(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[39] + -1.0*x[67] + 1.0)
def l274_40(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[40] + -1.0*x[68] + 1.0)
def l274_41(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[41] + -1.0*x[69] + 1.0)
def l274_42(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[42] + -1.0*x[70] + 1.0)
def l274_43(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[43] + -1.0*x[71] + 1.0)
def l274_44(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[44] + -1.0*x[72] + 1.0)
def l274_45(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[45] + -1.0*x[73] + 1.0)
def l274_46(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[46] + -1.0*x[74] + 1.0)
def l274_47(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[47] + -1.0*x[75] + 1.0)
def l274_48(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[48] + -1.0*x[76] + 1.0)
def l274_49(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[49] + -1.0*x[77] + 1.0)
def l274_50(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[50] + -1.0*x[78] + 1.0)
def l274_51(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[51] + -1.0*x[79] + 1.0)
def l274_52(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[52] + -1.0*x[80] + 1.0)
def l274_53(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[53] + -1.0*x[81] + 1.0)
def l274_54(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[54] + -1.0*x[82] + 1.0)
def l274_55(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[55] + -1.0*x[83] + 1.0)
def l274_56(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[56] + -1.0*x[84] + 1.0)
def l274_57(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[57] + -1.0*x[85] + 1.0)
def l274_58(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[58] + -1.0*x[86] + 1.0)
def l274_59(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[59] + -1.0*x[87] + 1.0)
def l274_60(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[60] + -1.0*x[88] + 1.0)
def l274_61(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[61] + -1.0*x[89] + 1.0)
def l274_62(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[62] + -1.0*x[90] + 1.0)
def l274_63(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[63] + -1.0*x[91] + 1.0)
def l274_64(x):
    # x is a list (or vector) of length 316
    return max(0, x[120])
def l274_65(x):
    # x is a list (or vector) of length 316
    return max(0, x[121])
def l274_66(x):
    # x is a list (or vector) of length 316
    return max(0, x[122])
def l274_67(x):
    # x is a list (or vector) of length 316
    return max(0, x[123])
def l274_68(x):
    # x is a list (or vector) of length 316
    return max(0, x[92])
def l274_69(x):
    # x is a list (or vector) of length 316
    return max(0, x[93])
def l274_70(x):
    # x is a list (or vector) of length 316
    return max(0, x[94])
def l274_71(x):
    # x is a list (or vector) of length 316
    return max(0, x[95])
def l274_72(x):
    # x is a list (or vector) of length 316
    return max(0, x[96])
def l274_73(x):
    # x is a list (or vector) of length 316
    return max(0, x[97])
def l274_74(x):
    # x is a list (or vector) of length 316
    return max(0, x[98])
def l274_75(x):
    # x is a list (or vector) of length 316
    return max(0, x[99])
def l274_76(x):
    # x is a list (or vector) of length 316
    return max(0, x[100])
def l274_77(x):
    # x is a list (or vector) of length 316
    return max(0, x[101])
def l274_78(x):
    # x is a list (or vector) of length 316
    return max(0, x[102])
def l274_79(x):
    # x is a list (or vector) of length 316
    return max(0, x[103])
def l274_80(x):
    # x is a list (or vector) of length 316
    return max(0, x[104])
def l274_81(x):
    # x is a list (or vector) of length 316
    return max(0, x[105])
def l274_82(x):
    # x is a list (or vector) of length 316
    return max(0, x[106])
def l274_83(x):
    # x is a list (or vector) of length 316
    return max(0, x[107])
def l274_84(x):
    # x is a list (or vector) of length 316
    return max(0, x[108])
def l274_85(x):
    # x is a list (or vector) of length 316
    return max(0, x[109])
def l274_86(x):
    # x is a list (or vector) of length 316
    return max(0, x[110])
def l274_87(x):
    # x is a list (or vector) of length 316
    return max(0, x[111])
def l274_88(x):
    # x is a list (or vector) of length 316
    return max(0, x[112])
def l274_89(x):
    # x is a list (or vector) of length 316
    return max(0, x[113])
def l274_90(x):
    # x is a list (or vector) of length 316
    return max(0, x[114])
def l274_91(x):
    # x is a list (or vector) of length 316
    return max(0, x[115])
def l274_92(x):
    # x is a list (or vector) of length 316
    return max(0, x[116])
def l274_93(x):
    # x is a list (or vector) of length 316
    return max(0, x[117])
def l274_94(x):
    # x is a list (or vector) of length 316
    return max(0, x[118])
def l274_95(x):
    # x is a list (or vector) of length 316
    return max(0, x[119])
def l274_96(x):
    # x is a list (or vector) of length 316
    return max(0, x[124])
def l274_97(x):
    # x is a list (or vector) of length 316
    return max(0, x[125])
def l274_98(x):
    # x is a list (or vector) of length 316
    return max(0, x[126])
def l274_99(x):
    # x is a list (or vector) of length 316
    return max(0, x[127])
def l274_100(x):
    # x is a list (or vector) of length 316
    return max(0, x[128])
def l274_101(x):
    # x is a list (or vector) of length 316
    return max(0, x[129])
def l274_102(x):
    # x is a list (or vector) of length 316
    return max(0, x[130])
def l274_103(x):
    # x is a list (or vector) of length 316
    return max(0, x[131])
def l274_104(x):
    # x is a list (or vector) of length 316
    return max(0, x[132])
def l274_105(x):
    # x is a list (or vector) of length 316
    return max(0, x[133])
def l274_106(x):
    # x is a list (or vector) of length 316
    return max(0, x[134])
def l274_107(x):
    # x is a list (or vector) of length 316
    return max(0, x[135])
def l274_108(x):
    # x is a list (or vector) of length 316
    return max(0, x[136])
def l274_109(x):
    # x is a list (or vector) of length 316
    return max(0, x[137])
def l274_110(x):
    # x is a list (or vector) of length 316
    return max(0, x[138])
def l274_111(x):
    # x is a list (or vector) of length 316
    return max(0, x[139])
def l274_112(x):
    # x is a list (or vector) of length 316
    return max(0, x[140])
def l274_113(x):
    # x is a list (or vector) of length 316
    return max(0, x[141])
def l274_114(x):
    # x is a list (or vector) of length 316
    return max(0, x[142])
def l274_115(x):
    # x is a list (or vector) of length 316
    return max(0, x[143])
def l274_116(x):
    # x is a list (or vector) of length 316
    return max(0, x[144])
def l274_117(x):
    # x is a list (or vector) of length 316
    return max(0, x[145])
def l274_118(x):
    # x is a list (or vector) of length 316
    return max(0, x[146])
def l274_119(x):
    # x is a list (or vector) of length 316
    return max(0, x[147])
def l274_120(x):
    # x is a list (or vector) of length 316
    return max(0, x[148])
def l274_121(x):
    # x is a list (or vector) of length 316
    return max(0, x[149])
def l274_122(x):
    # x is a list (or vector) of length 316
    return max(0, x[150])
def l274_123(x):
    # x is a list (or vector) of length 316
    return max(0, x[151])
def l274_124(x):
    # x is a list (or vector) of length 316
    return max(0, x[152])
def l274_125(x):
    # x is a list (or vector) of length 316
    return max(0, x[153])
def l274_126(x):
    # x is a list (or vector) of length 316
    return max(0, x[154])
def l274_127(x):
    # x is a list (or vector) of length 316
    return max(0, x[155])
def l274_128(x):
    # x is a list (or vector) of length 316
    return max(0, x[156])
def l274_129(x):
    # x is a list (or vector) of length 316
    return max(0, x[157])
def l274_130(x):
    # x is a list (or vector) of length 316
    return max(0, x[158])
def l274_131(x):
    # x is a list (or vector) of length 316
    return max(0, x[159])
def l274_132(x):
    # x is a list (or vector) of length 316
    return max(0, x[160])
def l274_133(x):
    # x is a list (or vector) of length 316
    return max(0, x[161])
def l274_134(x):
    # x is a list (or vector) of length 316
    return max(0, x[162])
def l274_135(x):
    # x is a list (or vector) of length 316
    return max(0, x[163])
def l274_136(x):
    # x is a list (or vector) of length 316
    return max(0, x[164])
def l274_137(x):
    # x is a list (or vector) of length 316
    return max(0, x[165])
def l274_138(x):
    # x is a list (or vector) of length 316
    return max(0, x[166])
def l274_139(x):
    # x is a list (or vector) of length 316
    return max(0, x[167])
def l274_140(x):
    # x is a list (or vector) of length 316
    return max(0, x[168])
def l274_141(x):
    # x is a list (or vector) of length 316
    return max(0, x[169])
def l274_142(x):
    # x is a list (or vector) of length 316
    return max(0, x[170])
def l274_143(x):
    # x is a list (or vector) of length 316
    return max(0, x[171])
def l274_144(x):
    # x is a list (or vector) of length 316
    return max(0, x[172])
def l274_145(x):
    # x is a list (or vector) of length 316
    return max(0, x[173])
def l274_146(x):
    # x is a list (or vector) of length 316
    return max(0, x[174])
def l274_147(x):
    # x is a list (or vector) of length 316
    return max(0, x[175])
def l274_148(x):
    # x is a list (or vector) of length 316
    return max(0, x[176])
def l274_149(x):
    # x is a list (or vector) of length 316
    return max(0, x[177])
def l274_150(x):
    # x is a list (or vector) of length 316
    return max(0, x[178])
def l274_151(x):
    # x is a list (or vector) of length 316
    return max(0, x[179])
def l274_152(x):
    # x is a list (or vector) of length 316
    return max(0, x[180])
def l274_153(x):
    # x is a list (or vector) of length 316
    return max(0, x[181])
def l274_154(x):
    # x is a list (or vector) of length 316
    return max(0, x[182])
def l274_155(x):
    # x is a list (or vector) of length 316
    return max(0, x[183])
def l274_156(x):
    # x is a list (or vector) of length 316
    return max(0, x[184])
def l274_157(x):
    # x is a list (or vector) of length 316
    return max(0, x[185])
def l274_158(x):
    # x is a list (or vector) of length 316
    return max(0, x[186])
def l274_159(x):
    # x is a list (or vector) of length 316
    return max(0, x[187])
def l274_160(x):
    # x is a list (or vector) of length 316
    return max(0, x[188])
def l274_161(x):
    # x is a list (or vector) of length 316
    return max(0, x[189])
def l274_162(x):
    # x is a list (or vector) of length 316
    return max(0, x[190])
def l274_163(x):
    # x is a list (or vector) of length 316
    return max(0, x[191])
def l274_164(x):
    # x is a list (or vector) of length 316
    return max(0, x[192])
def l274_165(x):
    # x is a list (or vector) of length 316
    return max(0, x[193])
def l274_166(x):
    # x is a list (or vector) of length 316
    return max(0, x[194])
def l274_167(x):
    # x is a list (or vector) of length 316
    return max(0, x[195])
def l274_168(x):
    # x is a list (or vector) of length 316
    return max(0, x[196])
def l274_169(x):
    # x is a list (or vector) of length 316
    return max(0, x[197])
def l274_170(x):
    # x is a list (or vector) of length 316
    return max(0, x[198])
def l274_171(x):
    # x is a list (or vector) of length 316
    return max(0, x[199])
def l274_172(x):
    # x is a list (or vector) of length 316
    return max(0, x[200])
def l274_173(x):
    # x is a list (or vector) of length 316
    return max(0, x[201])
def l274_174(x):
    # x is a list (or vector) of length 316
    return max(0, x[202])
def l274_175(x):
    # x is a list (or vector) of length 316
    return max(0, x[203])
def l274_176(x):
    # x is a list (or vector) of length 316
    return max(0, x[204])
def l274_177(x):
    # x is a list (or vector) of length 316
    return max(0, x[205])
def l274_178(x):
    # x is a list (or vector) of length 316
    return max(0, x[206])
def l274_179(x):
    # x is a list (or vector) of length 316
    return max(0, x[207])
def l274_180(x):
    # x is a list (or vector) of length 316
    return max(0, x[208])
def l274_181(x):
    # x is a list (or vector) of length 316
    return max(0, x[209])
def l274_182(x):
    # x is a list (or vector) of length 316
    return max(0, x[210])
def l274_183(x):
    # x is a list (or vector) of length 316
    return max(0, x[211])
def l274_184(x):
    # x is a list (or vector) of length 316
    return max(0, x[212])
def l274_185(x):
    # x is a list (or vector) of length 316
    return max(0, x[213])
def l274_186(x):
    # x is a list (or vector) of length 316
    return max(0, x[214])
def l274_187(x):
    # x is a list (or vector) of length 316
    return max(0, x[215])
def l274_188(x):
    # x is a list (or vector) of length 316
    return max(0, x[216])
def l274_189(x):
    # x is a list (or vector) of length 316
    return max(0, x[217])
def l274_190(x):
    # x is a list (or vector) of length 316
    return max(0, x[218])
def l274_191(x):
    # x is a list (or vector) of length 316
    return max(0, x[219])
def l274_192(x):
    # x is a list (or vector) of length 316
    return max(0, x[220])
def l274_193(x):
    # x is a list (or vector) of length 316
    return max(0, x[221])
def l274_194(x):
    # x is a list (or vector) of length 316
    return max(0, x[222])
def l274_195(x):
    # x is a list (or vector) of length 316
    return max(0, x[223])
def l274_196(x):
    # x is a list (or vector) of length 316
    return max(0, x[224])
def l274_197(x):
    # x is a list (or vector) of length 316
    return max(0, x[225])
def l274_198(x):
    # x is a list (or vector) of length 316
    return max(0, x[226])
def l274_199(x):
    # x is a list (or vector) of length 316
    return max(0, x[227])
def l274_200(x):
    # x is a list (or vector) of length 316
    return max(0, x[228])
def l274_201(x):
    # x is a list (or vector) of length 316
    return max(0, x[229])
def l274_202(x):
    # x is a list (or vector) of length 316
    return max(0, x[230])
def l274_203(x):
    # x is a list (or vector) of length 316
    return max(0, x[231])
def l274_204(x):
    # x is a list (or vector) of length 316
    return max(0, x[232])
def l274_205(x):
    # x is a list (or vector) of length 316
    return max(0, x[233])
def l274_206(x):
    # x is a list (or vector) of length 316
    return max(0, x[234])
def l274_207(x):
    # x is a list (or vector) of length 316
    return max(0, x[235])
def l274_208(x):
    # x is a list (or vector) of length 316
    return max(0, x[236])
def l274_209(x):
    # x is a list (or vector) of length 316
    return max(0, x[237])
def l274_210(x):
    # x is a list (or vector) of length 316
    return max(0, x[238])
def l274_211(x):
    # x is a list (or vector) of length 316
    return max(0, x[239])
def l274_212(x):
    # x is a list (or vector) of length 316
    return max(0, x[240])
def l274_213(x):
    # x is a list (or vector) of length 316
    return max(0, x[241])
def l274_214(x):
    # x is a list (or vector) of length 316
    return max(0, x[242])
def l274_215(x):
    # x is a list (or vector) of length 316
    return max(0, x[243])
def l274_216(x):
    # x is a list (or vector) of length 316
    return max(0, x[244])
def l274_217(x):
    # x is a list (or vector) of length 316
    return max(0, x[245])
def l274_218(x):
    # x is a list (or vector) of length 316
    return max(0, x[246])
def l274_219(x):
    # x is a list (or vector) of length 316
    return max(0, x[247])
def l274_220(x):
    # x is a list (or vector) of length 316
    return max(0, x[248])
def l274_221(x):
    # x is a list (or vector) of length 316
    return max(0, x[249])
def l274_222(x):
    # x is a list (or vector) of length 316
    return max(0, x[250])
def l274_223(x):
    # x is a list (or vector) of length 316
    return max(0, x[251])
def l274_224(x):
    # x is a list (or vector) of length 316
    return max(0, x[252])
def l274_225(x):
    # x is a list (or vector) of length 316
    return max(0, x[253])
def l274_226(x):
    # x is a list (or vector) of length 316
    return max(0, x[254])
def l274_227(x):
    # x is a list (or vector) of length 316
    return max(0, x[255])
def l274_228(x):
    # x is a list (or vector) of length 316
    return max(0, x[256])
def l274_229(x):
    # x is a list (or vector) of length 316
    return max(0, x[257])
def l274_230(x):
    # x is a list (or vector) of length 316
    return max(0, x[258])
def l274_231(x):
    # x is a list (or vector) of length 316
    return max(0, x[259])
def l274_232(x):
    # x is a list (or vector) of length 316
    return max(0, x[260])
def l274_233(x):
    # x is a list (or vector) of length 316
    return max(0, x[261])
def l274_234(x):
    # x is a list (or vector) of length 316
    return max(0, x[262])
def l274_235(x):
    # x is a list (or vector) of length 316
    return max(0, x[263])
def l274_236(x):
    # x is a list (or vector) of length 316
    return max(0, x[264])
def l274_237(x):
    # x is a list (or vector) of length 316
    return max(0, x[265])
def l274_238(x):
    # x is a list (or vector) of length 316
    return max(0, x[266])
def l274_239(x):
    # x is a list (or vector) of length 316
    return max(0, x[267])
def l274_240(x):
    # x is a list (or vector) of length 316
    return max(0, x[268])
def l274_241(x):
    # x is a list (or vector) of length 316
    return max(0, x[269])
def l274_242(x):
    # x is a list (or vector) of length 316
    return max(0, x[270])
def l274_243(x):
    # x is a list (or vector) of length 316
    return max(0, x[271])
def l274_244(x):
    # x is a list (or vector) of length 316
    return max(0, x[272])
def l274_245(x):
    # x is a list (or vector) of length 316
    return max(0, x[273])
def l274_246(x):
    # x is a list (or vector) of length 316
    return max(0, x[274])
def l274_247(x):
    # x is a list (or vector) of length 316
    return max(0, x[275])
def l274_248(x):
    # x is a list (or vector) of length 316
    return max(0, x[276])
def l274_249(x):
    # x is a list (or vector) of length 316
    return max(0, x[277])
def l274_250(x):
    # x is a list (or vector) of length 316
    return max(0, x[278])
def l274_251(x):
    # x is a list (or vector) of length 316
    return max(0, x[279])
def l274_252(x):
    # x is a list (or vector) of length 316
    return max(0, x[280])
def l274_253(x):
    # x is a list (or vector) of length 316
    return max(0, x[281])
def l274_254(x):
    # x is a list (or vector) of length 316
    return max(0, x[282])
def l274_255(x):
    # x is a list (or vector) of length 316
    return max(0, x[283])
def l274_256(x):
    # x is a list (or vector) of length 316
    return max(0, x[284])
def l274_257(x):
    # x is a list (or vector) of length 316
    return max(0, x[285])
def l274_258(x):
    # x is a list (or vector) of length 316
    return max(0, x[286])
def l274_259(x):
    # x is a list (or vector) of length 316
    return max(0, x[287])
def l274_260(x):
    # x is a list (or vector) of length 316
    return max(0, x[288])
def l274_261(x):
    # x is a list (or vector) of length 316
    return max(0, x[289])
def l274_262(x):
    # x is a list (or vector) of length 316
    return max(0, x[290])
def l274_263(x):
    # x is a list (or vector) of length 316
    return max(0, x[291])
def l274_264(x):
    # x is a list (or vector) of length 316
    return max(0, x[292])
def l274_265(x):
    # x is a list (or vector) of length 316
    return max(0, x[293])
def l274_266(x):
    # x is a list (or vector) of length 316
    return max(0, x[294])
def l274_267(x):
    # x is a list (or vector) of length 316
    return max(0, x[295])
def l274_268(x):
    # x is a list (or vector) of length 316
    return max(0, x[296])
def l274_269(x):
    # x is a list (or vector) of length 316
    return max(0, x[297])
def l274_270(x):
    # x is a list (or vector) of length 316
    return max(0, x[298])
def l274_271(x):
    # x is a list (or vector) of length 316
    return max(0, x[299])
def l274_272(x):
    # x is a list (or vector) of length 316
    return max(0, x[300])
def l274_273(x):
    # x is a list (or vector) of length 316
    return max(0, x[301])
def l274_274(x):
    # x is a list (or vector) of length 316
    return max(0, x[302])
def l274_275(x):
    # x is a list (or vector) of length 316
    return max(0, x[303])
def l274_276(x):
    # x is a list (or vector) of length 316
    return max(0, x[304])
def l274_277(x):
    # x is a list (or vector) of length 316
    return max(0, x[305])
def l274_278(x):
    # x is a list (or vector) of length 316
    return max(0, x[306])
def l274_279(x):
    # x is a list (or vector) of length 316
    return max(0, x[307])
def l274_280(x):
    # x is a list (or vector) of length 316
    return max(0, x[308])
def l274_281(x):
    # x is a list (or vector) of length 316
    return max(0, x[309])
def l274_282(x):
    # x is a list (or vector) of length 316
    return max(0, x[310])
def l274_283(x):
    # x is a list (or vector) of length 316
    return max(0, x[311])
def l274_284(x):
    # x is a list (or vector) of length 316
    return max(0, x[312])
def l274_285(x):
    # x is a list (or vector) of length 316
    return max(0, x[313])
def l274_286(x):
    # x is a list (or vector) of length 316
    return max(0, x[314])
def l274_287(x):
    # x is a list (or vector) of length 316
    return max(0, x[315])
def l274_(x):
    # x is a list (or vector) of length 316
    return [
        l274_0(x),
        l274_1(x),
        l274_2(x),
        l274_3(x),
        l274_4(x),
        l274_5(x),
        l274_6(x),
        l274_7(x),
        l274_8(x),
        l274_9(x),
        l274_10(x),
        l274_11(x),
        l274_12(x),
        l274_13(x),
        l274_14(x),
        l274_15(x),
        l274_16(x),
        l274_17(x),
        l274_18(x),
        l274_19(x),
        l274_20(x),
        l274_21(x),
        l274_22(x),
        l274_23(x),
        l274_24(x),
        l274_25(x),
        l274_26(x),
        l274_27(x),
        l274_28(x),
        l274_29(x),
        l274_30(x),
        l274_31(x),
        l274_32(x),
        l274_33(x),
        l274_34(x),
        l274_35(x),
        l274_36(x),
        l274_37(x),
        l274_38(x),
        l274_39(x),
        l274_40(x),
        l274_41(x),
        l274_42(x),
        l274_43(x),
        l274_44(x),
        l274_45(x),
        l274_46(x),
        l274_47(x),
        l274_48(x),
        l274_49(x),
        l274_50(x),
        l274_51(x),
        l274_52(x),
        l274_53(x),
        l274_54(x),
        l274_55(x),
        l274_56(x),
        l274_57(x),
        l274_58(x),
        l274_59(x),
        l274_60(x),
        l274_61(x),
        l274_62(x),
        l274_63(x),
        l274_64(x),
        l274_65(x),
        l274_66(x),
        l274_67(x),
        l274_68(x),
        l274_69(x),
        l274_70(x),
        l274_71(x),
        l274_72(x),
        l274_73(x),
        l274_74(x),
        l274_75(x),
        l274_76(x),
        l274_77(x),
        l274_78(x),
        l274_79(x),
        l274_80(x),
        l274_81(x),
        l274_82(x),
        l274_83(x),
        l274_84(x),
        l274_85(x),
        l274_86(x),
        l274_87(x),
        l274_88(x),
        l274_89(x),
        l274_90(x),
        l274_91(x),
        l274_92(x),
        l274_93(x),
        l274_94(x),
        l274_95(x),
        l274_96(x),
        l274_97(x),
        l274_98(x),
        l274_99(x),
        l274_100(x),
        l274_101(x),
        l274_102(x),
        l274_103(x),
        l274_104(x),
        l274_105(x),
        l274_106(x),
        l274_107(x),
        l274_108(x),
        l274_109(x),
        l274_110(x),
        l274_111(x),
        l274_112(x),
        l274_113(x),
        l274_114(x),
        l274_115(x),
        l274_116(x),
        l274_117(x),
        l274_118(x),
        l274_119(x),
        l274_120(x),
        l274_121(x),
        l274_122(x),
        l274_123(x),
        l274_124(x),
        l274_125(x),
        l274_126(x),
        l274_127(x),
        l274_128(x),
        l274_129(x),
        l274_130(x),
        l274_131(x),
        l274_132(x),
        l274_133(x),
        l274_134(x),
        l274_135(x),
        l274_136(x),
        l274_137(x),
        l274_138(x),
        l274_139(x),
        l274_140(x),
        l274_141(x),
        l274_142(x),
        l274_143(x),
        l274_144(x),
        l274_145(x),
        l274_146(x),
        l274_147(x),
        l274_148(x),
        l274_149(x),
        l274_150(x),
        l274_151(x),
        l274_152(x),
        l274_153(x),
        l274_154(x),
        l274_155(x),
        l274_156(x),
        l274_157(x),
        l274_158(x),
        l274_159(x),
        l274_160(x),
        l274_161(x),
        l274_162(x),
        l274_163(x),
        l274_164(x),
        l274_165(x),
        l274_166(x),
        l274_167(x),
        l274_168(x),
        l274_169(x),
        l274_170(x),
        l274_171(x),
        l274_172(x),
        l274_173(x),
        l274_174(x),
        l274_175(x),
        l274_176(x),
        l274_177(x),
        l274_178(x),
        l274_179(x),
        l274_180(x),
        l274_181(x),
        l274_182(x),
        l274_183(x),
        l274_184(x),
        l274_185(x),
        l274_186(x),
        l274_187(x),
        l274_188(x),
        l274_189(x),
        l274_190(x),
        l274_191(x),
        l274_192(x),
        l274_193(x),
        l274_194(x),
        l274_195(x),
        l274_196(x),
        l274_197(x),
        l274_198(x),
        l274_199(x),
        l274_200(x),
        l274_201(x),
        l274_202(x),
        l274_203(x),
        l274_204(x),
        l274_205(x),
        l274_206(x),
        l274_207(x),
        l274_208(x),
        l274_209(x),
        l274_210(x),
        l274_211(x),
        l274_212(x),
        l274_213(x),
        l274_214(x),
        l274_215(x),
        l274_216(x),
        l274_217(x),
        l274_218(x),
        l274_219(x),
        l274_220(x),
        l274_221(x),
        l274_222(x),
        l274_223(x),
        l274_224(x),
        l274_225(x),
        l274_226(x),
        l274_227(x),
        l274_228(x),
        l274_229(x),
        l274_230(x),
        l274_231(x),
        l274_232(x),
        l274_233(x),
        l274_234(x),
        l274_235(x),
        l274_236(x),
        l274_237(x),
        l274_238(x),
        l274_239(x),
        l274_240(x),
        l274_241(x),
        l274_242(x),
        l274_243(x),
        l274_244(x),
        l274_245(x),
        l274_246(x),
        l274_247(x),
        l274_248(x),
        l274_249(x),
        l274_250(x),
        l274_251(x),
        l274_252(x),
        l274_253(x),
        l274_254(x),
        l274_255(x),
        l274_256(x),
        l274_257(x),
        l274_258(x),
        l274_259(x),
        l274_260(x),
        l274_261(x),
        l274_262(x),
        l274_263(x),
        l274_264(x),
        l274_265(x),
        l274_266(x),
        l274_267(x),
        l274_268(x),
        l274_269(x),
        l274_270(x),
        l274_271(x),
        l274_272(x),
        l274_273(x),
        l274_274(x),
        l274_275(x),
        l274_276(x),
        l274_277(x),
        l274_278(x),
        l274_279(x),
        l274_280(x),
        l274_281(x),
        l274_282(x),
        l274_283(x),
        l274_284(x),
        l274_285(x),
        l274_286(x),
        l274_287(x),
    ]