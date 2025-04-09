import numpy as np




# Generated from reverse engineering
def l526_g(x: np.ndarray) -> np.ndarray:
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




def l526_0(x):
    # x is a list (or vector) of length 316
    return max(0, x[0])
def l526_1(x):
    # x is a list (or vector) of length 316
    return max(0, x[1])
def l526_2(x):
    # x is a list (or vector) of length 316
    return max(0, x[2])
def l526_3(x):
    # x is a list (or vector) of length 316
    return max(0, x[3])
def l526_4(x):
    # x is a list (or vector) of length 316
    return max(0, x[4])
def l526_5(x):
    # x is a list (or vector) of length 316
    return max(0, x[5])
def l526_6(x):
    # x is a list (or vector) of length 316
    return max(0, x[6])
def l526_7(x):
    # x is a list (or vector) of length 316
    return max(0, x[7])
def l526_8(x):
    # x is a list (or vector) of length 316
    return max(0, x[8])
def l526_9(x):
    # x is a list (or vector) of length 316
    return max(0, x[9])
def l526_10(x):
    # x is a list (or vector) of length 316
    return max(0, x[10])
def l526_11(x):
    # x is a list (or vector) of length 316
    return max(0, x[11])
def l526_12(x):
    # x is a list (or vector) of length 316
    return max(0, x[12])
def l526_13(x):
    # x is a list (or vector) of length 316
    return max(0, x[13])
def l526_14(x):
    # x is a list (or vector) of length 316
    return max(0, x[14])
def l526_15(x):
    # x is a list (or vector) of length 316
    return max(0, x[15])
def l526_16(x):
    # x is a list (or vector) of length 316
    return max(0, x[16])
def l526_17(x):
    # x is a list (or vector) of length 316
    return max(0, x[17])
def l526_18(x):
    # x is a list (or vector) of length 316
    return max(0, x[18])
def l526_19(x):
    # x is a list (or vector) of length 316
    return max(0, x[19])
def l526_20(x):
    # x is a list (or vector) of length 316
    return max(0, x[20])
def l526_21(x):
    # x is a list (or vector) of length 316
    return max(0, x[21])
def l526_22(x):
    # x is a list (or vector) of length 316
    return max(0, x[22])
def l526_23(x):
    # x is a list (or vector) of length 316
    return max(0, x[23])
def l526_24(x):
    # x is a list (or vector) of length 316
    return max(0, x[24])
def l526_25(x):
    # x is a list (or vector) of length 316
    return max(0, x[25])
def l526_26(x):
    # x is a list (or vector) of length 316
    return max(0, x[26])
def l526_27(x):
    # x is a list (or vector) of length 316
    return max(0, x[27])
def l526_28(x):
    # x is a list (or vector) of length 316
    return max(0, x[28])
def l526_29(x):
    # x is a list (or vector) of length 316
    return max(0, x[29])
def l526_30(x):
    # x is a list (or vector) of length 316
    return max(0, x[30])
def l526_31(x):
    # x is a list (or vector) of length 316
    return max(0, x[31])
def l526_32(x):
    # x is a list (or vector) of length 316
    return max(0, x[32])
def l526_33(x):
    # x is a list (or vector) of length 316
    return max(0, x[33])
def l526_34(x):
    # x is a list (or vector) of length 316
    return max(0, x[34])
def l526_35(x):
    # x is a list (or vector) of length 316
    return max(0, x[35])
def l526_36(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[36] + -1.0*x[64] + 1.0)
def l526_37(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[37] + -1.0*x[65] + 1.0)
def l526_38(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[38] + -1.0*x[66] + 1.0)
def l526_39(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[39] + -1.0*x[67] + 1.0)
def l526_40(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[40] + -1.0*x[68] + 1.0)
def l526_41(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[41] + -1.0*x[69] + 1.0)
def l526_42(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[42] + -1.0*x[70] + 1.0)
def l526_43(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[43] + -1.0*x[71] + 1.0)
def l526_44(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[44] + -1.0*x[72] + 1.0)
def l526_45(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[45] + -1.0*x[73] + 1.0)
def l526_46(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[46] + -1.0*x[74] + 1.0)
def l526_47(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[47] + -1.0*x[75] + 1.0)
def l526_48(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[48] + -1.0*x[76] + 1.0)
def l526_49(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[49] + -1.0*x[77] + 1.0)
def l526_50(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[50] + -1.0*x[78] + 1.0)
def l526_51(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[51] + -1.0*x[79] + 1.0)
def l526_52(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[52] + -1.0*x[80] + 1.0)
def l526_53(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[53] + -1.0*x[81] + 1.0)
def l526_54(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[54] + -1.0*x[82] + 1.0)
def l526_55(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[55] + -1.0*x[83] + 1.0)
def l526_56(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[56] + -1.0*x[84] + 1.0)
def l526_57(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[57] + -1.0*x[85] + 1.0)
def l526_58(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[58] + -1.0*x[86] + 1.0)
def l526_59(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[59] + -1.0*x[87] + 1.0)
def l526_60(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[60] + -1.0*x[88] + 1.0)
def l526_61(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[61] + -1.0*x[89] + 1.0)
def l526_62(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[62] + -1.0*x[90] + 1.0)
def l526_63(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[63] + -1.0*x[91] + 1.0)
def l526_64(x):
    # x is a list (or vector) of length 316
    return max(0, x[120])
def l526_65(x):
    # x is a list (or vector) of length 316
    return max(0, x[121])
def l526_66(x):
    # x is a list (or vector) of length 316
    return max(0, x[122])
def l526_67(x):
    # x is a list (or vector) of length 316
    return max(0, x[123])
def l526_68(x):
    # x is a list (or vector) of length 316
    return max(0, x[92])
def l526_69(x):
    # x is a list (or vector) of length 316
    return max(0, x[93])
def l526_70(x):
    # x is a list (or vector) of length 316
    return max(0, x[94])
def l526_71(x):
    # x is a list (or vector) of length 316
    return max(0, x[95])
def l526_72(x):
    # x is a list (or vector) of length 316
    return max(0, x[96])
def l526_73(x):
    # x is a list (or vector) of length 316
    return max(0, x[97])
def l526_74(x):
    # x is a list (or vector) of length 316
    return max(0, x[98])
def l526_75(x):
    # x is a list (or vector) of length 316
    return max(0, x[99])
def l526_76(x):
    # x is a list (or vector) of length 316
    return max(0, x[100])
def l526_77(x):
    # x is a list (or vector) of length 316
    return max(0, x[101])
def l526_78(x):
    # x is a list (or vector) of length 316
    return max(0, x[102])
def l526_79(x):
    # x is a list (or vector) of length 316
    return max(0, x[103])
def l526_80(x):
    # x is a list (or vector) of length 316
    return max(0, x[104])
def l526_81(x):
    # x is a list (or vector) of length 316
    return max(0, x[105])
def l526_82(x):
    # x is a list (or vector) of length 316
    return max(0, x[106])
def l526_83(x):
    # x is a list (or vector) of length 316
    return max(0, x[107])
def l526_84(x):
    # x is a list (or vector) of length 316
    return max(0, x[108])
def l526_85(x):
    # x is a list (or vector) of length 316
    return max(0, x[109])
def l526_86(x):
    # x is a list (or vector) of length 316
    return max(0, x[110])
def l526_87(x):
    # x is a list (or vector) of length 316
    return max(0, x[111])
def l526_88(x):
    # x is a list (or vector) of length 316
    return max(0, x[112])
def l526_89(x):
    # x is a list (or vector) of length 316
    return max(0, x[113])
def l526_90(x):
    # x is a list (or vector) of length 316
    return max(0, x[114])
def l526_91(x):
    # x is a list (or vector) of length 316
    return max(0, x[115])
def l526_92(x):
    # x is a list (or vector) of length 316
    return max(0, x[116])
def l526_93(x):
    # x is a list (or vector) of length 316
    return max(0, x[117])
def l526_94(x):
    # x is a list (or vector) of length 316
    return max(0, x[118])
def l526_95(x):
    # x is a list (or vector) of length 316
    return max(0, x[119])
def l526_96(x):
    # x is a list (or vector) of length 316
    return max(0, x[124])
def l526_97(x):
    # x is a list (or vector) of length 316
    return max(0, x[125])
def l526_98(x):
    # x is a list (or vector) of length 316
    return max(0, x[126])
def l526_99(x):
    # x is a list (or vector) of length 316
    return max(0, x[127])
def l526_100(x):
    # x is a list (or vector) of length 316
    return max(0, x[128])
def l526_101(x):
    # x is a list (or vector) of length 316
    return max(0, x[129])
def l526_102(x):
    # x is a list (or vector) of length 316
    return max(0, x[130])
def l526_103(x):
    # x is a list (or vector) of length 316
    return max(0, x[131])
def l526_104(x):
    # x is a list (or vector) of length 316
    return max(0, x[132])
def l526_105(x):
    # x is a list (or vector) of length 316
    return max(0, x[133])
def l526_106(x):
    # x is a list (or vector) of length 316
    return max(0, x[134])
def l526_107(x):
    # x is a list (or vector) of length 316
    return max(0, x[135])
def l526_108(x):
    # x is a list (or vector) of length 316
    return max(0, x[136])
def l526_109(x):
    # x is a list (or vector) of length 316
    return max(0, x[137])
def l526_110(x):
    # x is a list (or vector) of length 316
    return max(0, x[138])
def l526_111(x):
    # x is a list (or vector) of length 316
    return max(0, x[139])
def l526_112(x):
    # x is a list (or vector) of length 316
    return max(0, x[140])
def l526_113(x):
    # x is a list (or vector) of length 316
    return max(0, x[141])
def l526_114(x):
    # x is a list (or vector) of length 316
    return max(0, x[142])
def l526_115(x):
    # x is a list (or vector) of length 316
    return max(0, x[143])
def l526_116(x):
    # x is a list (or vector) of length 316
    return max(0, x[144])
def l526_117(x):
    # x is a list (or vector) of length 316
    return max(0, x[145])
def l526_118(x):
    # x is a list (or vector) of length 316
    return max(0, x[146])
def l526_119(x):
    # x is a list (or vector) of length 316
    return max(0, x[147])
def l526_120(x):
    # x is a list (or vector) of length 316
    return max(0, x[148])
def l526_121(x):
    # x is a list (or vector) of length 316
    return max(0, x[149])
def l526_122(x):
    # x is a list (or vector) of length 316
    return max(0, x[150])
def l526_123(x):
    # x is a list (or vector) of length 316
    return max(0, x[151])
def l526_124(x):
    # x is a list (or vector) of length 316
    return max(0, x[152])
def l526_125(x):
    # x is a list (or vector) of length 316
    return max(0, x[153])
def l526_126(x):
    # x is a list (or vector) of length 316
    return max(0, x[154])
def l526_127(x):
    # x is a list (or vector) of length 316
    return max(0, x[155])
def l526_128(x):
    # x is a list (or vector) of length 316
    return max(0, x[156])
def l526_129(x):
    # x is a list (or vector) of length 316
    return max(0, x[157])
def l526_130(x):
    # x is a list (or vector) of length 316
    return max(0, x[158])
def l526_131(x):
    # x is a list (or vector) of length 316
    return max(0, x[159])
def l526_132(x):
    # x is a list (or vector) of length 316
    return max(0, x[160])
def l526_133(x):
    # x is a list (or vector) of length 316
    return max(0, x[161])
def l526_134(x):
    # x is a list (or vector) of length 316
    return max(0, x[162])
def l526_135(x):
    # x is a list (or vector) of length 316
    return max(0, x[163])
def l526_136(x):
    # x is a list (or vector) of length 316
    return max(0, x[164])
def l526_137(x):
    # x is a list (or vector) of length 316
    return max(0, x[165])
def l526_138(x):
    # x is a list (or vector) of length 316
    return max(0, x[166])
def l526_139(x):
    # x is a list (or vector) of length 316
    return max(0, x[167])
def l526_140(x):
    # x is a list (or vector) of length 316
    return max(0, x[168])
def l526_141(x):
    # x is a list (or vector) of length 316
    return max(0, x[169])
def l526_142(x):
    # x is a list (or vector) of length 316
    return max(0, x[170])
def l526_143(x):
    # x is a list (or vector) of length 316
    return max(0, x[171])
def l526_144(x):
    # x is a list (or vector) of length 316
    return max(0, x[172])
def l526_145(x):
    # x is a list (or vector) of length 316
    return max(0, x[173])
def l526_146(x):
    # x is a list (or vector) of length 316
    return max(0, x[174])
def l526_147(x):
    # x is a list (or vector) of length 316
    return max(0, x[175])
def l526_148(x):
    # x is a list (or vector) of length 316
    return max(0, x[176])
def l526_149(x):
    # x is a list (or vector) of length 316
    return max(0, x[177])
def l526_150(x):
    # x is a list (or vector) of length 316
    return max(0, x[178])
def l526_151(x):
    # x is a list (or vector) of length 316
    return max(0, x[179])
def l526_152(x):
    # x is a list (or vector) of length 316
    return max(0, x[180])
def l526_153(x):
    # x is a list (or vector) of length 316
    return max(0, x[181])
def l526_154(x):
    # x is a list (or vector) of length 316
    return max(0, x[182])
def l526_155(x):
    # x is a list (or vector) of length 316
    return max(0, x[183])
def l526_156(x):
    # x is a list (or vector) of length 316
    return max(0, x[184])
def l526_157(x):
    # x is a list (or vector) of length 316
    return max(0, x[185])
def l526_158(x):
    # x is a list (or vector) of length 316
    return max(0, x[186])
def l526_159(x):
    # x is a list (or vector) of length 316
    return max(0, x[187])
def l526_160(x):
    # x is a list (or vector) of length 316
    return max(0, x[188])
def l526_161(x):
    # x is a list (or vector) of length 316
    return max(0, x[189])
def l526_162(x):
    # x is a list (or vector) of length 316
    return max(0, x[190])
def l526_163(x):
    # x is a list (or vector) of length 316
    return max(0, x[191])
def l526_164(x):
    # x is a list (or vector) of length 316
    return max(0, x[192])
def l526_165(x):
    # x is a list (or vector) of length 316
    return max(0, x[193])
def l526_166(x):
    # x is a list (or vector) of length 316
    return max(0, x[194])
def l526_167(x):
    # x is a list (or vector) of length 316
    return max(0, x[195])
def l526_168(x):
    # x is a list (or vector) of length 316
    return max(0, x[196])
def l526_169(x):
    # x is a list (or vector) of length 316
    return max(0, x[197])
def l526_170(x):
    # x is a list (or vector) of length 316
    return max(0, x[198])
def l526_171(x):
    # x is a list (or vector) of length 316
    return max(0, x[199])
def l526_172(x):
    # x is a list (or vector) of length 316
    return max(0, x[200])
def l526_173(x):
    # x is a list (or vector) of length 316
    return max(0, x[201])
def l526_174(x):
    # x is a list (or vector) of length 316
    return max(0, x[202])
def l526_175(x):
    # x is a list (or vector) of length 316
    return max(0, x[203])
def l526_176(x):
    # x is a list (or vector) of length 316
    return max(0, x[204])
def l526_177(x):
    # x is a list (or vector) of length 316
    return max(0, x[205])
def l526_178(x):
    # x is a list (or vector) of length 316
    return max(0, x[206])
def l526_179(x):
    # x is a list (or vector) of length 316
    return max(0, x[207])
def l526_180(x):
    # x is a list (or vector) of length 316
    return max(0, x[208])
def l526_181(x):
    # x is a list (or vector) of length 316
    return max(0, x[209])
def l526_182(x):
    # x is a list (or vector) of length 316
    return max(0, x[210])
def l526_183(x):
    # x is a list (or vector) of length 316
    return max(0, x[211])
def l526_184(x):
    # x is a list (or vector) of length 316
    return max(0, x[212])
def l526_185(x):
    # x is a list (or vector) of length 316
    return max(0, x[213])
def l526_186(x):
    # x is a list (or vector) of length 316
    return max(0, x[214])
def l526_187(x):
    # x is a list (or vector) of length 316
    return max(0, x[215])
def l526_188(x):
    # x is a list (or vector) of length 316
    return max(0, x[216])
def l526_189(x):
    # x is a list (or vector) of length 316
    return max(0, x[217])
def l526_190(x):
    # x is a list (or vector) of length 316
    return max(0, x[218])
def l526_191(x):
    # x is a list (or vector) of length 316
    return max(0, x[219])
def l526_192(x):
    # x is a list (or vector) of length 316
    return max(0, x[220])
def l526_193(x):
    # x is a list (or vector) of length 316
    return max(0, x[221])
def l526_194(x):
    # x is a list (or vector) of length 316
    return max(0, x[222])
def l526_195(x):
    # x is a list (or vector) of length 316
    return max(0, x[223])
def l526_196(x):
    # x is a list (or vector) of length 316
    return max(0, x[224])
def l526_197(x):
    # x is a list (or vector) of length 316
    return max(0, x[225])
def l526_198(x):
    # x is a list (or vector) of length 316
    return max(0, x[226])
def l526_199(x):
    # x is a list (or vector) of length 316
    return max(0, x[227])
def l526_200(x):
    # x is a list (or vector) of length 316
    return max(0, x[228])
def l526_201(x):
    # x is a list (or vector) of length 316
    return max(0, x[229])
def l526_202(x):
    # x is a list (or vector) of length 316
    return max(0, x[230])
def l526_203(x):
    # x is a list (or vector) of length 316
    return max(0, x[231])
def l526_204(x):
    # x is a list (or vector) of length 316
    return max(0, x[232])
def l526_205(x):
    # x is a list (or vector) of length 316
    return max(0, x[233])
def l526_206(x):
    # x is a list (or vector) of length 316
    return max(0, x[234])
def l526_207(x):
    # x is a list (or vector) of length 316
    return max(0, x[235])
def l526_208(x):
    # x is a list (or vector) of length 316
    return max(0, x[236])
def l526_209(x):
    # x is a list (or vector) of length 316
    return max(0, x[237])
def l526_210(x):
    # x is a list (or vector) of length 316
    return max(0, x[238])
def l526_211(x):
    # x is a list (or vector) of length 316
    return max(0, x[239])
def l526_212(x):
    # x is a list (or vector) of length 316
    return max(0, x[240])
def l526_213(x):
    # x is a list (or vector) of length 316
    return max(0, x[241])
def l526_214(x):
    # x is a list (or vector) of length 316
    return max(0, x[242])
def l526_215(x):
    # x is a list (or vector) of length 316
    return max(0, x[243])
def l526_216(x):
    # x is a list (or vector) of length 316
    return max(0, x[244])
def l526_217(x):
    # x is a list (or vector) of length 316
    return max(0, x[245])
def l526_218(x):
    # x is a list (or vector) of length 316
    return max(0, x[246])
def l526_219(x):
    # x is a list (or vector) of length 316
    return max(0, x[247])
def l526_220(x):
    # x is a list (or vector) of length 316
    return max(0, x[248])
def l526_221(x):
    # x is a list (or vector) of length 316
    return max(0, x[249])
def l526_222(x):
    # x is a list (or vector) of length 316
    return max(0, x[250])
def l526_223(x):
    # x is a list (or vector) of length 316
    return max(0, x[251])
def l526_224(x):
    # x is a list (or vector) of length 316
    return max(0, x[252])
def l526_225(x):
    # x is a list (or vector) of length 316
    return max(0, x[253])
def l526_226(x):
    # x is a list (or vector) of length 316
    return max(0, x[254])
def l526_227(x):
    # x is a list (or vector) of length 316
    return max(0, x[255])
def l526_228(x):
    # x is a list (or vector) of length 316
    return max(0, x[256])
def l526_229(x):
    # x is a list (or vector) of length 316
    return max(0, x[257])
def l526_230(x):
    # x is a list (or vector) of length 316
    return max(0, x[258])
def l526_231(x):
    # x is a list (or vector) of length 316
    return max(0, x[259])
def l526_232(x):
    # x is a list (or vector) of length 316
    return max(0, x[260])
def l526_233(x):
    # x is a list (or vector) of length 316
    return max(0, x[261])
def l526_234(x):
    # x is a list (or vector) of length 316
    return max(0, x[262])
def l526_235(x):
    # x is a list (or vector) of length 316
    return max(0, x[263])
def l526_236(x):
    # x is a list (or vector) of length 316
    return max(0, x[264])
def l526_237(x):
    # x is a list (or vector) of length 316
    return max(0, x[265])
def l526_238(x):
    # x is a list (or vector) of length 316
    return max(0, x[266])
def l526_239(x):
    # x is a list (or vector) of length 316
    return max(0, x[267])
def l526_240(x):
    # x is a list (or vector) of length 316
    return max(0, x[268])
def l526_241(x):
    # x is a list (or vector) of length 316
    return max(0, x[269])
def l526_242(x):
    # x is a list (or vector) of length 316
    return max(0, x[270])
def l526_243(x):
    # x is a list (or vector) of length 316
    return max(0, x[271])
def l526_244(x):
    # x is a list (or vector) of length 316
    return max(0, x[272])
def l526_245(x):
    # x is a list (or vector) of length 316
    return max(0, x[273])
def l526_246(x):
    # x is a list (or vector) of length 316
    return max(0, x[274])
def l526_247(x):
    # x is a list (or vector) of length 316
    return max(0, x[275])
def l526_248(x):
    # x is a list (or vector) of length 316
    return max(0, x[276])
def l526_249(x):
    # x is a list (or vector) of length 316
    return max(0, x[277])
def l526_250(x):
    # x is a list (or vector) of length 316
    return max(0, x[278])
def l526_251(x):
    # x is a list (or vector) of length 316
    return max(0, x[279])
def l526_252(x):
    # x is a list (or vector) of length 316
    return max(0, x[280])
def l526_253(x):
    # x is a list (or vector) of length 316
    return max(0, x[281])
def l526_254(x):
    # x is a list (or vector) of length 316
    return max(0, x[282])
def l526_255(x):
    # x is a list (or vector) of length 316
    return max(0, x[283])
def l526_256(x):
    # x is a list (or vector) of length 316
    return max(0, x[284])
def l526_257(x):
    # x is a list (or vector) of length 316
    return max(0, x[285])
def l526_258(x):
    # x is a list (or vector) of length 316
    return max(0, x[286])
def l526_259(x):
    # x is a list (or vector) of length 316
    return max(0, x[287])
def l526_260(x):
    # x is a list (or vector) of length 316
    return max(0, x[288])
def l526_261(x):
    # x is a list (or vector) of length 316
    return max(0, x[289])
def l526_262(x):
    # x is a list (or vector) of length 316
    return max(0, x[290])
def l526_263(x):
    # x is a list (or vector) of length 316
    return max(0, x[291])
def l526_264(x):
    # x is a list (or vector) of length 316
    return max(0, x[292])
def l526_265(x):
    # x is a list (or vector) of length 316
    return max(0, x[293])
def l526_266(x):
    # x is a list (or vector) of length 316
    return max(0, x[294])
def l526_267(x):
    # x is a list (or vector) of length 316
    return max(0, x[295])
def l526_268(x):
    # x is a list (or vector) of length 316
    return max(0, x[296])
def l526_269(x):
    # x is a list (or vector) of length 316
    return max(0, x[297])
def l526_270(x):
    # x is a list (or vector) of length 316
    return max(0, x[298])
def l526_271(x):
    # x is a list (or vector) of length 316
    return max(0, x[299])
def l526_272(x):
    # x is a list (or vector) of length 316
    return max(0, x[300])
def l526_273(x):
    # x is a list (or vector) of length 316
    return max(0, x[301])
def l526_274(x):
    # x is a list (or vector) of length 316
    return max(0, x[302])
def l526_275(x):
    # x is a list (or vector) of length 316
    return max(0, x[303])
def l526_276(x):
    # x is a list (or vector) of length 316
    return max(0, x[304])
def l526_277(x):
    # x is a list (or vector) of length 316
    return max(0, x[305])
def l526_278(x):
    # x is a list (or vector) of length 316
    return max(0, x[306])
def l526_279(x):
    # x is a list (or vector) of length 316
    return max(0, x[307])
def l526_280(x):
    # x is a list (or vector) of length 316
    return max(0, x[308])
def l526_281(x):
    # x is a list (or vector) of length 316
    return max(0, x[309])
def l526_282(x):
    # x is a list (or vector) of length 316
    return max(0, x[310])
def l526_283(x):
    # x is a list (or vector) of length 316
    return max(0, x[311])
def l526_284(x):
    # x is a list (or vector) of length 316
    return max(0, x[312])
def l526_285(x):
    # x is a list (or vector) of length 316
    return max(0, x[313])
def l526_286(x):
    # x is a list (or vector) of length 316
    return max(0, x[314])
def l526_287(x):
    # x is a list (or vector) of length 316
    return max(0, x[315])
def l526_(x):
    # x is a list (or vector) of length 316
    return [
        l526_0(x),
        l526_1(x),
        l526_2(x),
        l526_3(x),
        l526_4(x),
        l526_5(x),
        l526_6(x),
        l526_7(x),
        l526_8(x),
        l526_9(x),
        l526_10(x),
        l526_11(x),
        l526_12(x),
        l526_13(x),
        l526_14(x),
        l526_15(x),
        l526_16(x),
        l526_17(x),
        l526_18(x),
        l526_19(x),
        l526_20(x),
        l526_21(x),
        l526_22(x),
        l526_23(x),
        l526_24(x),
        l526_25(x),
        l526_26(x),
        l526_27(x),
        l526_28(x),
        l526_29(x),
        l526_30(x),
        l526_31(x),
        l526_32(x),
        l526_33(x),
        l526_34(x),
        l526_35(x),
        l526_36(x),
        l526_37(x),
        l526_38(x),
        l526_39(x),
        l526_40(x),
        l526_41(x),
        l526_42(x),
        l526_43(x),
        l526_44(x),
        l526_45(x),
        l526_46(x),
        l526_47(x),
        l526_48(x),
        l526_49(x),
        l526_50(x),
        l526_51(x),
        l526_52(x),
        l526_53(x),
        l526_54(x),
        l526_55(x),
        l526_56(x),
        l526_57(x),
        l526_58(x),
        l526_59(x),
        l526_60(x),
        l526_61(x),
        l526_62(x),
        l526_63(x),
        l526_64(x),
        l526_65(x),
        l526_66(x),
        l526_67(x),
        l526_68(x),
        l526_69(x),
        l526_70(x),
        l526_71(x),
        l526_72(x),
        l526_73(x),
        l526_74(x),
        l526_75(x),
        l526_76(x),
        l526_77(x),
        l526_78(x),
        l526_79(x),
        l526_80(x),
        l526_81(x),
        l526_82(x),
        l526_83(x),
        l526_84(x),
        l526_85(x),
        l526_86(x),
        l526_87(x),
        l526_88(x),
        l526_89(x),
        l526_90(x),
        l526_91(x),
        l526_92(x),
        l526_93(x),
        l526_94(x),
        l526_95(x),
        l526_96(x),
        l526_97(x),
        l526_98(x),
        l526_99(x),
        l526_100(x),
        l526_101(x),
        l526_102(x),
        l526_103(x),
        l526_104(x),
        l526_105(x),
        l526_106(x),
        l526_107(x),
        l526_108(x),
        l526_109(x),
        l526_110(x),
        l526_111(x),
        l526_112(x),
        l526_113(x),
        l526_114(x),
        l526_115(x),
        l526_116(x),
        l526_117(x),
        l526_118(x),
        l526_119(x),
        l526_120(x),
        l526_121(x),
        l526_122(x),
        l526_123(x),
        l526_124(x),
        l526_125(x),
        l526_126(x),
        l526_127(x),
        l526_128(x),
        l526_129(x),
        l526_130(x),
        l526_131(x),
        l526_132(x),
        l526_133(x),
        l526_134(x),
        l526_135(x),
        l526_136(x),
        l526_137(x),
        l526_138(x),
        l526_139(x),
        l526_140(x),
        l526_141(x),
        l526_142(x),
        l526_143(x),
        l526_144(x),
        l526_145(x),
        l526_146(x),
        l526_147(x),
        l526_148(x),
        l526_149(x),
        l526_150(x),
        l526_151(x),
        l526_152(x),
        l526_153(x),
        l526_154(x),
        l526_155(x),
        l526_156(x),
        l526_157(x),
        l526_158(x),
        l526_159(x),
        l526_160(x),
        l526_161(x),
        l526_162(x),
        l526_163(x),
        l526_164(x),
        l526_165(x),
        l526_166(x),
        l526_167(x),
        l526_168(x),
        l526_169(x),
        l526_170(x),
        l526_171(x),
        l526_172(x),
        l526_173(x),
        l526_174(x),
        l526_175(x),
        l526_176(x),
        l526_177(x),
        l526_178(x),
        l526_179(x),
        l526_180(x),
        l526_181(x),
        l526_182(x),
        l526_183(x),
        l526_184(x),
        l526_185(x),
        l526_186(x),
        l526_187(x),
        l526_188(x),
        l526_189(x),
        l526_190(x),
        l526_191(x),
        l526_192(x),
        l526_193(x),
        l526_194(x),
        l526_195(x),
        l526_196(x),
        l526_197(x),
        l526_198(x),
        l526_199(x),
        l526_200(x),
        l526_201(x),
        l526_202(x),
        l526_203(x),
        l526_204(x),
        l526_205(x),
        l526_206(x),
        l526_207(x),
        l526_208(x),
        l526_209(x),
        l526_210(x),
        l526_211(x),
        l526_212(x),
        l526_213(x),
        l526_214(x),
        l526_215(x),
        l526_216(x),
        l526_217(x),
        l526_218(x),
        l526_219(x),
        l526_220(x),
        l526_221(x),
        l526_222(x),
        l526_223(x),
        l526_224(x),
        l526_225(x),
        l526_226(x),
        l526_227(x),
        l526_228(x),
        l526_229(x),
        l526_230(x),
        l526_231(x),
        l526_232(x),
        l526_233(x),
        l526_234(x),
        l526_235(x),
        l526_236(x),
        l526_237(x),
        l526_238(x),
        l526_239(x),
        l526_240(x),
        l526_241(x),
        l526_242(x),
        l526_243(x),
        l526_244(x),
        l526_245(x),
        l526_246(x),
        l526_247(x),
        l526_248(x),
        l526_249(x),
        l526_250(x),
        l526_251(x),
        l526_252(x),
        l526_253(x),
        l526_254(x),
        l526_255(x),
        l526_256(x),
        l526_257(x),
        l526_258(x),
        l526_259(x),
        l526_260(x),
        l526_261(x),
        l526_262(x),
        l526_263(x),
        l526_264(x),
        l526_265(x),
        l526_266(x),
        l526_267(x),
        l526_268(x),
        l526_269(x),
        l526_270(x),
        l526_271(x),
        l526_272(x),
        l526_273(x),
        l526_274(x),
        l526_275(x),
        l526_276(x),
        l526_277(x),
        l526_278(x),
        l526_279(x),
        l526_280(x),
        l526_281(x),
        l526_282(x),
        l526_283(x),
        l526_284(x),
        l526_285(x),
        l526_286(x),
        l526_287(x),
    ]