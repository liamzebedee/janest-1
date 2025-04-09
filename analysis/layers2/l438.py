import numpy as np




# Generated from reverse engineering
def l438_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 288
    out = np.empty(288, dtype=np.float32)
    
    # for i in range(0, 34):
    for i in range(0, 34):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3fffffff (len=30)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(34, 64):
    for i in range(0, 30):
        s = -1 * x[34 + i] + -1 * x[64 + i]
        s += biases[i]
        out[34 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 66):
    for i in range(0, 2):
        s = x[124 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(66, 96):
    for i in range(0, 30):
        s = x[94 + i]
        out[66 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 288):
    for i in range(0, 192):
        s = x[126 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l438_0(x):
    # x is a list (or vector) of length 318
    return max(0, x[0])
def l438_1(x):
    # x is a list (or vector) of length 318
    return max(0, x[1])
def l438_2(x):
    # x is a list (or vector) of length 318
    return max(0, x[2])
def l438_3(x):
    # x is a list (or vector) of length 318
    return max(0, x[3])
def l438_4(x):
    # x is a list (or vector) of length 318
    return max(0, x[4])
def l438_5(x):
    # x is a list (or vector) of length 318
    return max(0, x[5])
def l438_6(x):
    # x is a list (or vector) of length 318
    return max(0, x[6])
def l438_7(x):
    # x is a list (or vector) of length 318
    return max(0, x[7])
def l438_8(x):
    # x is a list (or vector) of length 318
    return max(0, x[8])
def l438_9(x):
    # x is a list (or vector) of length 318
    return max(0, x[9])
def l438_10(x):
    # x is a list (or vector) of length 318
    return max(0, x[10])
def l438_11(x):
    # x is a list (or vector) of length 318
    return max(0, x[11])
def l438_12(x):
    # x is a list (or vector) of length 318
    return max(0, x[12])
def l438_13(x):
    # x is a list (or vector) of length 318
    return max(0, x[13])
def l438_14(x):
    # x is a list (or vector) of length 318
    return max(0, x[14])
def l438_15(x):
    # x is a list (or vector) of length 318
    return max(0, x[15])
def l438_16(x):
    # x is a list (or vector) of length 318
    return max(0, x[16])
def l438_17(x):
    # x is a list (or vector) of length 318
    return max(0, x[17])
def l438_18(x):
    # x is a list (or vector) of length 318
    return max(0, x[18])
def l438_19(x):
    # x is a list (or vector) of length 318
    return max(0, x[19])
def l438_20(x):
    # x is a list (or vector) of length 318
    return max(0, x[20])
def l438_21(x):
    # x is a list (or vector) of length 318
    return max(0, x[21])
def l438_22(x):
    # x is a list (or vector) of length 318
    return max(0, x[22])
def l438_23(x):
    # x is a list (or vector) of length 318
    return max(0, x[23])
def l438_24(x):
    # x is a list (or vector) of length 318
    return max(0, x[24])
def l438_25(x):
    # x is a list (or vector) of length 318
    return max(0, x[25])
def l438_26(x):
    # x is a list (or vector) of length 318
    return max(0, x[26])
def l438_27(x):
    # x is a list (or vector) of length 318
    return max(0, x[27])
def l438_28(x):
    # x is a list (or vector) of length 318
    return max(0, x[28])
def l438_29(x):
    # x is a list (or vector) of length 318
    return max(0, x[29])
def l438_30(x):
    # x is a list (or vector) of length 318
    return max(0, x[30])
def l438_31(x):
    # x is a list (or vector) of length 318
    return max(0, x[31])
def l438_32(x):
    # x is a list (or vector) of length 318
    return max(0, x[32])
def l438_33(x):
    # x is a list (or vector) of length 318
    return max(0, x[33])
def l438_34(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[34] + -1.0*x[64] + 1.0)
def l438_35(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[35] + -1.0*x[65] + 1.0)
def l438_36(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[36] + -1.0*x[66] + 1.0)
def l438_37(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[37] + -1.0*x[67] + 1.0)
def l438_38(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[38] + -1.0*x[68] + 1.0)
def l438_39(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[39] + -1.0*x[69] + 1.0)
def l438_40(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[40] + -1.0*x[70] + 1.0)
def l438_41(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[41] + -1.0*x[71] + 1.0)
def l438_42(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[42] + -1.0*x[72] + 1.0)
def l438_43(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[43] + -1.0*x[73] + 1.0)
def l438_44(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[44] + -1.0*x[74] + 1.0)
def l438_45(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[45] + -1.0*x[75] + 1.0)
def l438_46(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[46] + -1.0*x[76] + 1.0)
def l438_47(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[47] + -1.0*x[77] + 1.0)
def l438_48(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[48] + -1.0*x[78] + 1.0)
def l438_49(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[49] + -1.0*x[79] + 1.0)
def l438_50(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[50] + -1.0*x[80] + 1.0)
def l438_51(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[51] + -1.0*x[81] + 1.0)
def l438_52(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[52] + -1.0*x[82] + 1.0)
def l438_53(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[53] + -1.0*x[83] + 1.0)
def l438_54(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[54] + -1.0*x[84] + 1.0)
def l438_55(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[55] + -1.0*x[85] + 1.0)
def l438_56(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[56] + -1.0*x[86] + 1.0)
def l438_57(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[57] + -1.0*x[87] + 1.0)
def l438_58(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[58] + -1.0*x[88] + 1.0)
def l438_59(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[59] + -1.0*x[89] + 1.0)
def l438_60(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[60] + -1.0*x[90] + 1.0)
def l438_61(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[61] + -1.0*x[91] + 1.0)
def l438_62(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[62] + -1.0*x[92] + 1.0)
def l438_63(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[63] + -1.0*x[93] + 1.0)
def l438_64(x):
    # x is a list (or vector) of length 318
    return max(0, x[124])
def l438_65(x):
    # x is a list (or vector) of length 318
    return max(0, x[125])
def l438_66(x):
    # x is a list (or vector) of length 318
    return max(0, x[94])
def l438_67(x):
    # x is a list (or vector) of length 318
    return max(0, x[95])
def l438_68(x):
    # x is a list (or vector) of length 318
    return max(0, x[96])
def l438_69(x):
    # x is a list (or vector) of length 318
    return max(0, x[97])
def l438_70(x):
    # x is a list (or vector) of length 318
    return max(0, x[98])
def l438_71(x):
    # x is a list (or vector) of length 318
    return max(0, x[99])
def l438_72(x):
    # x is a list (or vector) of length 318
    return max(0, x[100])
def l438_73(x):
    # x is a list (or vector) of length 318
    return max(0, x[101])
def l438_74(x):
    # x is a list (or vector) of length 318
    return max(0, x[102])
def l438_75(x):
    # x is a list (or vector) of length 318
    return max(0, x[103])
def l438_76(x):
    # x is a list (or vector) of length 318
    return max(0, x[104])
def l438_77(x):
    # x is a list (or vector) of length 318
    return max(0, x[105])
def l438_78(x):
    # x is a list (or vector) of length 318
    return max(0, x[106])
def l438_79(x):
    # x is a list (or vector) of length 318
    return max(0, x[107])
def l438_80(x):
    # x is a list (or vector) of length 318
    return max(0, x[108])
def l438_81(x):
    # x is a list (or vector) of length 318
    return max(0, x[109])
def l438_82(x):
    # x is a list (or vector) of length 318
    return max(0, x[110])
def l438_83(x):
    # x is a list (or vector) of length 318
    return max(0, x[111])
def l438_84(x):
    # x is a list (or vector) of length 318
    return max(0, x[112])
def l438_85(x):
    # x is a list (or vector) of length 318
    return max(0, x[113])
def l438_86(x):
    # x is a list (or vector) of length 318
    return max(0, x[114])
def l438_87(x):
    # x is a list (or vector) of length 318
    return max(0, x[115])
def l438_88(x):
    # x is a list (or vector) of length 318
    return max(0, x[116])
def l438_89(x):
    # x is a list (or vector) of length 318
    return max(0, x[117])
def l438_90(x):
    # x is a list (or vector) of length 318
    return max(0, x[118])
def l438_91(x):
    # x is a list (or vector) of length 318
    return max(0, x[119])
def l438_92(x):
    # x is a list (or vector) of length 318
    return max(0, x[120])
def l438_93(x):
    # x is a list (or vector) of length 318
    return max(0, x[121])
def l438_94(x):
    # x is a list (or vector) of length 318
    return max(0, x[122])
def l438_95(x):
    # x is a list (or vector) of length 318
    return max(0, x[123])
def l438_96(x):
    # x is a list (or vector) of length 318
    return max(0, x[126])
def l438_97(x):
    # x is a list (or vector) of length 318
    return max(0, x[127])
def l438_98(x):
    # x is a list (or vector) of length 318
    return max(0, x[128])
def l438_99(x):
    # x is a list (or vector) of length 318
    return max(0, x[129])
def l438_100(x):
    # x is a list (or vector) of length 318
    return max(0, x[130])
def l438_101(x):
    # x is a list (or vector) of length 318
    return max(0, x[131])
def l438_102(x):
    # x is a list (or vector) of length 318
    return max(0, x[132])
def l438_103(x):
    # x is a list (or vector) of length 318
    return max(0, x[133])
def l438_104(x):
    # x is a list (or vector) of length 318
    return max(0, x[134])
def l438_105(x):
    # x is a list (or vector) of length 318
    return max(0, x[135])
def l438_106(x):
    # x is a list (or vector) of length 318
    return max(0, x[136])
def l438_107(x):
    # x is a list (or vector) of length 318
    return max(0, x[137])
def l438_108(x):
    # x is a list (or vector) of length 318
    return max(0, x[138])
def l438_109(x):
    # x is a list (or vector) of length 318
    return max(0, x[139])
def l438_110(x):
    # x is a list (or vector) of length 318
    return max(0, x[140])
def l438_111(x):
    # x is a list (or vector) of length 318
    return max(0, x[141])
def l438_112(x):
    # x is a list (or vector) of length 318
    return max(0, x[142])
def l438_113(x):
    # x is a list (or vector) of length 318
    return max(0, x[143])
def l438_114(x):
    # x is a list (or vector) of length 318
    return max(0, x[144])
def l438_115(x):
    # x is a list (or vector) of length 318
    return max(0, x[145])
def l438_116(x):
    # x is a list (or vector) of length 318
    return max(0, x[146])
def l438_117(x):
    # x is a list (or vector) of length 318
    return max(0, x[147])
def l438_118(x):
    # x is a list (or vector) of length 318
    return max(0, x[148])
def l438_119(x):
    # x is a list (or vector) of length 318
    return max(0, x[149])
def l438_120(x):
    # x is a list (or vector) of length 318
    return max(0, x[150])
def l438_121(x):
    # x is a list (or vector) of length 318
    return max(0, x[151])
def l438_122(x):
    # x is a list (or vector) of length 318
    return max(0, x[152])
def l438_123(x):
    # x is a list (or vector) of length 318
    return max(0, x[153])
def l438_124(x):
    # x is a list (or vector) of length 318
    return max(0, x[154])
def l438_125(x):
    # x is a list (or vector) of length 318
    return max(0, x[155])
def l438_126(x):
    # x is a list (or vector) of length 318
    return max(0, x[156])
def l438_127(x):
    # x is a list (or vector) of length 318
    return max(0, x[157])
def l438_128(x):
    # x is a list (or vector) of length 318
    return max(0, x[158])
def l438_129(x):
    # x is a list (or vector) of length 318
    return max(0, x[159])
def l438_130(x):
    # x is a list (or vector) of length 318
    return max(0, x[160])
def l438_131(x):
    # x is a list (or vector) of length 318
    return max(0, x[161])
def l438_132(x):
    # x is a list (or vector) of length 318
    return max(0, x[162])
def l438_133(x):
    # x is a list (or vector) of length 318
    return max(0, x[163])
def l438_134(x):
    # x is a list (or vector) of length 318
    return max(0, x[164])
def l438_135(x):
    # x is a list (or vector) of length 318
    return max(0, x[165])
def l438_136(x):
    # x is a list (or vector) of length 318
    return max(0, x[166])
def l438_137(x):
    # x is a list (or vector) of length 318
    return max(0, x[167])
def l438_138(x):
    # x is a list (or vector) of length 318
    return max(0, x[168])
def l438_139(x):
    # x is a list (or vector) of length 318
    return max(0, x[169])
def l438_140(x):
    # x is a list (or vector) of length 318
    return max(0, x[170])
def l438_141(x):
    # x is a list (or vector) of length 318
    return max(0, x[171])
def l438_142(x):
    # x is a list (or vector) of length 318
    return max(0, x[172])
def l438_143(x):
    # x is a list (or vector) of length 318
    return max(0, x[173])
def l438_144(x):
    # x is a list (or vector) of length 318
    return max(0, x[174])
def l438_145(x):
    # x is a list (or vector) of length 318
    return max(0, x[175])
def l438_146(x):
    # x is a list (or vector) of length 318
    return max(0, x[176])
def l438_147(x):
    # x is a list (or vector) of length 318
    return max(0, x[177])
def l438_148(x):
    # x is a list (or vector) of length 318
    return max(0, x[178])
def l438_149(x):
    # x is a list (or vector) of length 318
    return max(0, x[179])
def l438_150(x):
    # x is a list (or vector) of length 318
    return max(0, x[180])
def l438_151(x):
    # x is a list (or vector) of length 318
    return max(0, x[181])
def l438_152(x):
    # x is a list (or vector) of length 318
    return max(0, x[182])
def l438_153(x):
    # x is a list (or vector) of length 318
    return max(0, x[183])
def l438_154(x):
    # x is a list (or vector) of length 318
    return max(0, x[184])
def l438_155(x):
    # x is a list (or vector) of length 318
    return max(0, x[185])
def l438_156(x):
    # x is a list (or vector) of length 318
    return max(0, x[186])
def l438_157(x):
    # x is a list (or vector) of length 318
    return max(0, x[187])
def l438_158(x):
    # x is a list (or vector) of length 318
    return max(0, x[188])
def l438_159(x):
    # x is a list (or vector) of length 318
    return max(0, x[189])
def l438_160(x):
    # x is a list (or vector) of length 318
    return max(0, x[190])
def l438_161(x):
    # x is a list (or vector) of length 318
    return max(0, x[191])
def l438_162(x):
    # x is a list (or vector) of length 318
    return max(0, x[192])
def l438_163(x):
    # x is a list (or vector) of length 318
    return max(0, x[193])
def l438_164(x):
    # x is a list (or vector) of length 318
    return max(0, x[194])
def l438_165(x):
    # x is a list (or vector) of length 318
    return max(0, x[195])
def l438_166(x):
    # x is a list (or vector) of length 318
    return max(0, x[196])
def l438_167(x):
    # x is a list (or vector) of length 318
    return max(0, x[197])
def l438_168(x):
    # x is a list (or vector) of length 318
    return max(0, x[198])
def l438_169(x):
    # x is a list (or vector) of length 318
    return max(0, x[199])
def l438_170(x):
    # x is a list (or vector) of length 318
    return max(0, x[200])
def l438_171(x):
    # x is a list (or vector) of length 318
    return max(0, x[201])
def l438_172(x):
    # x is a list (or vector) of length 318
    return max(0, x[202])
def l438_173(x):
    # x is a list (or vector) of length 318
    return max(0, x[203])
def l438_174(x):
    # x is a list (or vector) of length 318
    return max(0, x[204])
def l438_175(x):
    # x is a list (or vector) of length 318
    return max(0, x[205])
def l438_176(x):
    # x is a list (or vector) of length 318
    return max(0, x[206])
def l438_177(x):
    # x is a list (or vector) of length 318
    return max(0, x[207])
def l438_178(x):
    # x is a list (or vector) of length 318
    return max(0, x[208])
def l438_179(x):
    # x is a list (or vector) of length 318
    return max(0, x[209])
def l438_180(x):
    # x is a list (or vector) of length 318
    return max(0, x[210])
def l438_181(x):
    # x is a list (or vector) of length 318
    return max(0, x[211])
def l438_182(x):
    # x is a list (or vector) of length 318
    return max(0, x[212])
def l438_183(x):
    # x is a list (or vector) of length 318
    return max(0, x[213])
def l438_184(x):
    # x is a list (or vector) of length 318
    return max(0, x[214])
def l438_185(x):
    # x is a list (or vector) of length 318
    return max(0, x[215])
def l438_186(x):
    # x is a list (or vector) of length 318
    return max(0, x[216])
def l438_187(x):
    # x is a list (or vector) of length 318
    return max(0, x[217])
def l438_188(x):
    # x is a list (or vector) of length 318
    return max(0, x[218])
def l438_189(x):
    # x is a list (or vector) of length 318
    return max(0, x[219])
def l438_190(x):
    # x is a list (or vector) of length 318
    return max(0, x[220])
def l438_191(x):
    # x is a list (or vector) of length 318
    return max(0, x[221])
def l438_192(x):
    # x is a list (or vector) of length 318
    return max(0, x[222])
def l438_193(x):
    # x is a list (or vector) of length 318
    return max(0, x[223])
def l438_194(x):
    # x is a list (or vector) of length 318
    return max(0, x[224])
def l438_195(x):
    # x is a list (or vector) of length 318
    return max(0, x[225])
def l438_196(x):
    # x is a list (or vector) of length 318
    return max(0, x[226])
def l438_197(x):
    # x is a list (or vector) of length 318
    return max(0, x[227])
def l438_198(x):
    # x is a list (or vector) of length 318
    return max(0, x[228])
def l438_199(x):
    # x is a list (or vector) of length 318
    return max(0, x[229])
def l438_200(x):
    # x is a list (or vector) of length 318
    return max(0, x[230])
def l438_201(x):
    # x is a list (or vector) of length 318
    return max(0, x[231])
def l438_202(x):
    # x is a list (or vector) of length 318
    return max(0, x[232])
def l438_203(x):
    # x is a list (or vector) of length 318
    return max(0, x[233])
def l438_204(x):
    # x is a list (or vector) of length 318
    return max(0, x[234])
def l438_205(x):
    # x is a list (or vector) of length 318
    return max(0, x[235])
def l438_206(x):
    # x is a list (or vector) of length 318
    return max(0, x[236])
def l438_207(x):
    # x is a list (or vector) of length 318
    return max(0, x[237])
def l438_208(x):
    # x is a list (or vector) of length 318
    return max(0, x[238])
def l438_209(x):
    # x is a list (or vector) of length 318
    return max(0, x[239])
def l438_210(x):
    # x is a list (or vector) of length 318
    return max(0, x[240])
def l438_211(x):
    # x is a list (or vector) of length 318
    return max(0, x[241])
def l438_212(x):
    # x is a list (or vector) of length 318
    return max(0, x[242])
def l438_213(x):
    # x is a list (or vector) of length 318
    return max(0, x[243])
def l438_214(x):
    # x is a list (or vector) of length 318
    return max(0, x[244])
def l438_215(x):
    # x is a list (or vector) of length 318
    return max(0, x[245])
def l438_216(x):
    # x is a list (or vector) of length 318
    return max(0, x[246])
def l438_217(x):
    # x is a list (or vector) of length 318
    return max(0, x[247])
def l438_218(x):
    # x is a list (or vector) of length 318
    return max(0, x[248])
def l438_219(x):
    # x is a list (or vector) of length 318
    return max(0, x[249])
def l438_220(x):
    # x is a list (or vector) of length 318
    return max(0, x[250])
def l438_221(x):
    # x is a list (or vector) of length 318
    return max(0, x[251])
def l438_222(x):
    # x is a list (or vector) of length 318
    return max(0, x[252])
def l438_223(x):
    # x is a list (or vector) of length 318
    return max(0, x[253])
def l438_224(x):
    # x is a list (or vector) of length 318
    return max(0, x[254])
def l438_225(x):
    # x is a list (or vector) of length 318
    return max(0, x[255])
def l438_226(x):
    # x is a list (or vector) of length 318
    return max(0, x[256])
def l438_227(x):
    # x is a list (or vector) of length 318
    return max(0, x[257])
def l438_228(x):
    # x is a list (or vector) of length 318
    return max(0, x[258])
def l438_229(x):
    # x is a list (or vector) of length 318
    return max(0, x[259])
def l438_230(x):
    # x is a list (or vector) of length 318
    return max(0, x[260])
def l438_231(x):
    # x is a list (or vector) of length 318
    return max(0, x[261])
def l438_232(x):
    # x is a list (or vector) of length 318
    return max(0, x[262])
def l438_233(x):
    # x is a list (or vector) of length 318
    return max(0, x[263])
def l438_234(x):
    # x is a list (or vector) of length 318
    return max(0, x[264])
def l438_235(x):
    # x is a list (or vector) of length 318
    return max(0, x[265])
def l438_236(x):
    # x is a list (or vector) of length 318
    return max(0, x[266])
def l438_237(x):
    # x is a list (or vector) of length 318
    return max(0, x[267])
def l438_238(x):
    # x is a list (or vector) of length 318
    return max(0, x[268])
def l438_239(x):
    # x is a list (or vector) of length 318
    return max(0, x[269])
def l438_240(x):
    # x is a list (or vector) of length 318
    return max(0, x[270])
def l438_241(x):
    # x is a list (or vector) of length 318
    return max(0, x[271])
def l438_242(x):
    # x is a list (or vector) of length 318
    return max(0, x[272])
def l438_243(x):
    # x is a list (or vector) of length 318
    return max(0, x[273])
def l438_244(x):
    # x is a list (or vector) of length 318
    return max(0, x[274])
def l438_245(x):
    # x is a list (or vector) of length 318
    return max(0, x[275])
def l438_246(x):
    # x is a list (or vector) of length 318
    return max(0, x[276])
def l438_247(x):
    # x is a list (or vector) of length 318
    return max(0, x[277])
def l438_248(x):
    # x is a list (or vector) of length 318
    return max(0, x[278])
def l438_249(x):
    # x is a list (or vector) of length 318
    return max(0, x[279])
def l438_250(x):
    # x is a list (or vector) of length 318
    return max(0, x[280])
def l438_251(x):
    # x is a list (or vector) of length 318
    return max(0, x[281])
def l438_252(x):
    # x is a list (or vector) of length 318
    return max(0, x[282])
def l438_253(x):
    # x is a list (or vector) of length 318
    return max(0, x[283])
def l438_254(x):
    # x is a list (or vector) of length 318
    return max(0, x[284])
def l438_255(x):
    # x is a list (or vector) of length 318
    return max(0, x[285])
def l438_256(x):
    # x is a list (or vector) of length 318
    return max(0, x[286])
def l438_257(x):
    # x is a list (or vector) of length 318
    return max(0, x[287])
def l438_258(x):
    # x is a list (or vector) of length 318
    return max(0, x[288])
def l438_259(x):
    # x is a list (or vector) of length 318
    return max(0, x[289])
def l438_260(x):
    # x is a list (or vector) of length 318
    return max(0, x[290])
def l438_261(x):
    # x is a list (or vector) of length 318
    return max(0, x[291])
def l438_262(x):
    # x is a list (or vector) of length 318
    return max(0, x[292])
def l438_263(x):
    # x is a list (or vector) of length 318
    return max(0, x[293])
def l438_264(x):
    # x is a list (or vector) of length 318
    return max(0, x[294])
def l438_265(x):
    # x is a list (or vector) of length 318
    return max(0, x[295])
def l438_266(x):
    # x is a list (or vector) of length 318
    return max(0, x[296])
def l438_267(x):
    # x is a list (or vector) of length 318
    return max(0, x[297])
def l438_268(x):
    # x is a list (or vector) of length 318
    return max(0, x[298])
def l438_269(x):
    # x is a list (or vector) of length 318
    return max(0, x[299])
def l438_270(x):
    # x is a list (or vector) of length 318
    return max(0, x[300])
def l438_271(x):
    # x is a list (or vector) of length 318
    return max(0, x[301])
def l438_272(x):
    # x is a list (or vector) of length 318
    return max(0, x[302])
def l438_273(x):
    # x is a list (or vector) of length 318
    return max(0, x[303])
def l438_274(x):
    # x is a list (or vector) of length 318
    return max(0, x[304])
def l438_275(x):
    # x is a list (or vector) of length 318
    return max(0, x[305])
def l438_276(x):
    # x is a list (or vector) of length 318
    return max(0, x[306])
def l438_277(x):
    # x is a list (or vector) of length 318
    return max(0, x[307])
def l438_278(x):
    # x is a list (or vector) of length 318
    return max(0, x[308])
def l438_279(x):
    # x is a list (or vector) of length 318
    return max(0, x[309])
def l438_280(x):
    # x is a list (or vector) of length 318
    return max(0, x[310])
def l438_281(x):
    # x is a list (or vector) of length 318
    return max(0, x[311])
def l438_282(x):
    # x is a list (or vector) of length 318
    return max(0, x[312])
def l438_283(x):
    # x is a list (or vector) of length 318
    return max(0, x[313])
def l438_284(x):
    # x is a list (or vector) of length 318
    return max(0, x[314])
def l438_285(x):
    # x is a list (or vector) of length 318
    return max(0, x[315])
def l438_286(x):
    # x is a list (or vector) of length 318
    return max(0, x[316])
def l438_287(x):
    # x is a list (or vector) of length 318
    return max(0, x[317])
def l438_(x):
    # x is a list (or vector) of length 318
    return [
        l438_0(x),
        l438_1(x),
        l438_2(x),
        l438_3(x),
        l438_4(x),
        l438_5(x),
        l438_6(x),
        l438_7(x),
        l438_8(x),
        l438_9(x),
        l438_10(x),
        l438_11(x),
        l438_12(x),
        l438_13(x),
        l438_14(x),
        l438_15(x),
        l438_16(x),
        l438_17(x),
        l438_18(x),
        l438_19(x),
        l438_20(x),
        l438_21(x),
        l438_22(x),
        l438_23(x),
        l438_24(x),
        l438_25(x),
        l438_26(x),
        l438_27(x),
        l438_28(x),
        l438_29(x),
        l438_30(x),
        l438_31(x),
        l438_32(x),
        l438_33(x),
        l438_34(x),
        l438_35(x),
        l438_36(x),
        l438_37(x),
        l438_38(x),
        l438_39(x),
        l438_40(x),
        l438_41(x),
        l438_42(x),
        l438_43(x),
        l438_44(x),
        l438_45(x),
        l438_46(x),
        l438_47(x),
        l438_48(x),
        l438_49(x),
        l438_50(x),
        l438_51(x),
        l438_52(x),
        l438_53(x),
        l438_54(x),
        l438_55(x),
        l438_56(x),
        l438_57(x),
        l438_58(x),
        l438_59(x),
        l438_60(x),
        l438_61(x),
        l438_62(x),
        l438_63(x),
        l438_64(x),
        l438_65(x),
        l438_66(x),
        l438_67(x),
        l438_68(x),
        l438_69(x),
        l438_70(x),
        l438_71(x),
        l438_72(x),
        l438_73(x),
        l438_74(x),
        l438_75(x),
        l438_76(x),
        l438_77(x),
        l438_78(x),
        l438_79(x),
        l438_80(x),
        l438_81(x),
        l438_82(x),
        l438_83(x),
        l438_84(x),
        l438_85(x),
        l438_86(x),
        l438_87(x),
        l438_88(x),
        l438_89(x),
        l438_90(x),
        l438_91(x),
        l438_92(x),
        l438_93(x),
        l438_94(x),
        l438_95(x),
        l438_96(x),
        l438_97(x),
        l438_98(x),
        l438_99(x),
        l438_100(x),
        l438_101(x),
        l438_102(x),
        l438_103(x),
        l438_104(x),
        l438_105(x),
        l438_106(x),
        l438_107(x),
        l438_108(x),
        l438_109(x),
        l438_110(x),
        l438_111(x),
        l438_112(x),
        l438_113(x),
        l438_114(x),
        l438_115(x),
        l438_116(x),
        l438_117(x),
        l438_118(x),
        l438_119(x),
        l438_120(x),
        l438_121(x),
        l438_122(x),
        l438_123(x),
        l438_124(x),
        l438_125(x),
        l438_126(x),
        l438_127(x),
        l438_128(x),
        l438_129(x),
        l438_130(x),
        l438_131(x),
        l438_132(x),
        l438_133(x),
        l438_134(x),
        l438_135(x),
        l438_136(x),
        l438_137(x),
        l438_138(x),
        l438_139(x),
        l438_140(x),
        l438_141(x),
        l438_142(x),
        l438_143(x),
        l438_144(x),
        l438_145(x),
        l438_146(x),
        l438_147(x),
        l438_148(x),
        l438_149(x),
        l438_150(x),
        l438_151(x),
        l438_152(x),
        l438_153(x),
        l438_154(x),
        l438_155(x),
        l438_156(x),
        l438_157(x),
        l438_158(x),
        l438_159(x),
        l438_160(x),
        l438_161(x),
        l438_162(x),
        l438_163(x),
        l438_164(x),
        l438_165(x),
        l438_166(x),
        l438_167(x),
        l438_168(x),
        l438_169(x),
        l438_170(x),
        l438_171(x),
        l438_172(x),
        l438_173(x),
        l438_174(x),
        l438_175(x),
        l438_176(x),
        l438_177(x),
        l438_178(x),
        l438_179(x),
        l438_180(x),
        l438_181(x),
        l438_182(x),
        l438_183(x),
        l438_184(x),
        l438_185(x),
        l438_186(x),
        l438_187(x),
        l438_188(x),
        l438_189(x),
        l438_190(x),
        l438_191(x),
        l438_192(x),
        l438_193(x),
        l438_194(x),
        l438_195(x),
        l438_196(x),
        l438_197(x),
        l438_198(x),
        l438_199(x),
        l438_200(x),
        l438_201(x),
        l438_202(x),
        l438_203(x),
        l438_204(x),
        l438_205(x),
        l438_206(x),
        l438_207(x),
        l438_208(x),
        l438_209(x),
        l438_210(x),
        l438_211(x),
        l438_212(x),
        l438_213(x),
        l438_214(x),
        l438_215(x),
        l438_216(x),
        l438_217(x),
        l438_218(x),
        l438_219(x),
        l438_220(x),
        l438_221(x),
        l438_222(x),
        l438_223(x),
        l438_224(x),
        l438_225(x),
        l438_226(x),
        l438_227(x),
        l438_228(x),
        l438_229(x),
        l438_230(x),
        l438_231(x),
        l438_232(x),
        l438_233(x),
        l438_234(x),
        l438_235(x),
        l438_236(x),
        l438_237(x),
        l438_238(x),
        l438_239(x),
        l438_240(x),
        l438_241(x),
        l438_242(x),
        l438_243(x),
        l438_244(x),
        l438_245(x),
        l438_246(x),
        l438_247(x),
        l438_248(x),
        l438_249(x),
        l438_250(x),
        l438_251(x),
        l438_252(x),
        l438_253(x),
        l438_254(x),
        l438_255(x),
        l438_256(x),
        l438_257(x),
        l438_258(x),
        l438_259(x),
        l438_260(x),
        l438_261(x),
        l438_262(x),
        l438_263(x),
        l438_264(x),
        l438_265(x),
        l438_266(x),
        l438_267(x),
        l438_268(x),
        l438_269(x),
        l438_270(x),
        l438_271(x),
        l438_272(x),
        l438_273(x),
        l438_274(x),
        l438_275(x),
        l438_276(x),
        l438_277(x),
        l438_278(x),
        l438_279(x),
        l438_280(x),
        l438_281(x),
        l438_282(x),
        l438_283(x),
        l438_284(x),
        l438_285(x),
        l438_286(x),
        l438_287(x),
    ]