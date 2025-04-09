import numpy as np




# Generated from reverse engineering
def l522_g(x: np.ndarray) -> np.ndarray:
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




def l522_0(x):
    # x is a list (or vector) of length 318
    return max(0, x[0])
def l522_1(x):
    # x is a list (or vector) of length 318
    return max(0, x[1])
def l522_2(x):
    # x is a list (or vector) of length 318
    return max(0, x[2])
def l522_3(x):
    # x is a list (or vector) of length 318
    return max(0, x[3])
def l522_4(x):
    # x is a list (or vector) of length 318
    return max(0, x[4])
def l522_5(x):
    # x is a list (or vector) of length 318
    return max(0, x[5])
def l522_6(x):
    # x is a list (or vector) of length 318
    return max(0, x[6])
def l522_7(x):
    # x is a list (or vector) of length 318
    return max(0, x[7])
def l522_8(x):
    # x is a list (or vector) of length 318
    return max(0, x[8])
def l522_9(x):
    # x is a list (or vector) of length 318
    return max(0, x[9])
def l522_10(x):
    # x is a list (or vector) of length 318
    return max(0, x[10])
def l522_11(x):
    # x is a list (or vector) of length 318
    return max(0, x[11])
def l522_12(x):
    # x is a list (or vector) of length 318
    return max(0, x[12])
def l522_13(x):
    # x is a list (or vector) of length 318
    return max(0, x[13])
def l522_14(x):
    # x is a list (or vector) of length 318
    return max(0, x[14])
def l522_15(x):
    # x is a list (or vector) of length 318
    return max(0, x[15])
def l522_16(x):
    # x is a list (or vector) of length 318
    return max(0, x[16])
def l522_17(x):
    # x is a list (or vector) of length 318
    return max(0, x[17])
def l522_18(x):
    # x is a list (or vector) of length 318
    return max(0, x[18])
def l522_19(x):
    # x is a list (or vector) of length 318
    return max(0, x[19])
def l522_20(x):
    # x is a list (or vector) of length 318
    return max(0, x[20])
def l522_21(x):
    # x is a list (or vector) of length 318
    return max(0, x[21])
def l522_22(x):
    # x is a list (or vector) of length 318
    return max(0, x[22])
def l522_23(x):
    # x is a list (or vector) of length 318
    return max(0, x[23])
def l522_24(x):
    # x is a list (or vector) of length 318
    return max(0, x[24])
def l522_25(x):
    # x is a list (or vector) of length 318
    return max(0, x[25])
def l522_26(x):
    # x is a list (or vector) of length 318
    return max(0, x[26])
def l522_27(x):
    # x is a list (or vector) of length 318
    return max(0, x[27])
def l522_28(x):
    # x is a list (or vector) of length 318
    return max(0, x[28])
def l522_29(x):
    # x is a list (or vector) of length 318
    return max(0, x[29])
def l522_30(x):
    # x is a list (or vector) of length 318
    return max(0, x[30])
def l522_31(x):
    # x is a list (or vector) of length 318
    return max(0, x[31])
def l522_32(x):
    # x is a list (or vector) of length 318
    return max(0, x[32])
def l522_33(x):
    # x is a list (or vector) of length 318
    return max(0, x[33])
def l522_34(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[34] + -1.0*x[64] + 1.0)
def l522_35(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[35] + -1.0*x[65] + 1.0)
def l522_36(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[36] + -1.0*x[66] + 1.0)
def l522_37(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[37] + -1.0*x[67] + 1.0)
def l522_38(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[38] + -1.0*x[68] + 1.0)
def l522_39(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[39] + -1.0*x[69] + 1.0)
def l522_40(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[40] + -1.0*x[70] + 1.0)
def l522_41(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[41] + -1.0*x[71] + 1.0)
def l522_42(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[42] + -1.0*x[72] + 1.0)
def l522_43(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[43] + -1.0*x[73] + 1.0)
def l522_44(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[44] + -1.0*x[74] + 1.0)
def l522_45(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[45] + -1.0*x[75] + 1.0)
def l522_46(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[46] + -1.0*x[76] + 1.0)
def l522_47(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[47] + -1.0*x[77] + 1.0)
def l522_48(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[48] + -1.0*x[78] + 1.0)
def l522_49(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[49] + -1.0*x[79] + 1.0)
def l522_50(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[50] + -1.0*x[80] + 1.0)
def l522_51(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[51] + -1.0*x[81] + 1.0)
def l522_52(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[52] + -1.0*x[82] + 1.0)
def l522_53(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[53] + -1.0*x[83] + 1.0)
def l522_54(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[54] + -1.0*x[84] + 1.0)
def l522_55(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[55] + -1.0*x[85] + 1.0)
def l522_56(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[56] + -1.0*x[86] + 1.0)
def l522_57(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[57] + -1.0*x[87] + 1.0)
def l522_58(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[58] + -1.0*x[88] + 1.0)
def l522_59(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[59] + -1.0*x[89] + 1.0)
def l522_60(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[60] + -1.0*x[90] + 1.0)
def l522_61(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[61] + -1.0*x[91] + 1.0)
def l522_62(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[62] + -1.0*x[92] + 1.0)
def l522_63(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[63] + -1.0*x[93] + 1.0)
def l522_64(x):
    # x is a list (or vector) of length 318
    return max(0, x[124])
def l522_65(x):
    # x is a list (or vector) of length 318
    return max(0, x[125])
def l522_66(x):
    # x is a list (or vector) of length 318
    return max(0, x[94])
def l522_67(x):
    # x is a list (or vector) of length 318
    return max(0, x[95])
def l522_68(x):
    # x is a list (or vector) of length 318
    return max(0, x[96])
def l522_69(x):
    # x is a list (or vector) of length 318
    return max(0, x[97])
def l522_70(x):
    # x is a list (or vector) of length 318
    return max(0, x[98])
def l522_71(x):
    # x is a list (or vector) of length 318
    return max(0, x[99])
def l522_72(x):
    # x is a list (or vector) of length 318
    return max(0, x[100])
def l522_73(x):
    # x is a list (or vector) of length 318
    return max(0, x[101])
def l522_74(x):
    # x is a list (or vector) of length 318
    return max(0, x[102])
def l522_75(x):
    # x is a list (or vector) of length 318
    return max(0, x[103])
def l522_76(x):
    # x is a list (or vector) of length 318
    return max(0, x[104])
def l522_77(x):
    # x is a list (or vector) of length 318
    return max(0, x[105])
def l522_78(x):
    # x is a list (or vector) of length 318
    return max(0, x[106])
def l522_79(x):
    # x is a list (or vector) of length 318
    return max(0, x[107])
def l522_80(x):
    # x is a list (or vector) of length 318
    return max(0, x[108])
def l522_81(x):
    # x is a list (or vector) of length 318
    return max(0, x[109])
def l522_82(x):
    # x is a list (or vector) of length 318
    return max(0, x[110])
def l522_83(x):
    # x is a list (or vector) of length 318
    return max(0, x[111])
def l522_84(x):
    # x is a list (or vector) of length 318
    return max(0, x[112])
def l522_85(x):
    # x is a list (or vector) of length 318
    return max(0, x[113])
def l522_86(x):
    # x is a list (or vector) of length 318
    return max(0, x[114])
def l522_87(x):
    # x is a list (or vector) of length 318
    return max(0, x[115])
def l522_88(x):
    # x is a list (or vector) of length 318
    return max(0, x[116])
def l522_89(x):
    # x is a list (or vector) of length 318
    return max(0, x[117])
def l522_90(x):
    # x is a list (or vector) of length 318
    return max(0, x[118])
def l522_91(x):
    # x is a list (or vector) of length 318
    return max(0, x[119])
def l522_92(x):
    # x is a list (or vector) of length 318
    return max(0, x[120])
def l522_93(x):
    # x is a list (or vector) of length 318
    return max(0, x[121])
def l522_94(x):
    # x is a list (or vector) of length 318
    return max(0, x[122])
def l522_95(x):
    # x is a list (or vector) of length 318
    return max(0, x[123])
def l522_96(x):
    # x is a list (or vector) of length 318
    return max(0, x[126])
def l522_97(x):
    # x is a list (or vector) of length 318
    return max(0, x[127])
def l522_98(x):
    # x is a list (or vector) of length 318
    return max(0, x[128])
def l522_99(x):
    # x is a list (or vector) of length 318
    return max(0, x[129])
def l522_100(x):
    # x is a list (or vector) of length 318
    return max(0, x[130])
def l522_101(x):
    # x is a list (or vector) of length 318
    return max(0, x[131])
def l522_102(x):
    # x is a list (or vector) of length 318
    return max(0, x[132])
def l522_103(x):
    # x is a list (or vector) of length 318
    return max(0, x[133])
def l522_104(x):
    # x is a list (or vector) of length 318
    return max(0, x[134])
def l522_105(x):
    # x is a list (or vector) of length 318
    return max(0, x[135])
def l522_106(x):
    # x is a list (or vector) of length 318
    return max(0, x[136])
def l522_107(x):
    # x is a list (or vector) of length 318
    return max(0, x[137])
def l522_108(x):
    # x is a list (or vector) of length 318
    return max(0, x[138])
def l522_109(x):
    # x is a list (or vector) of length 318
    return max(0, x[139])
def l522_110(x):
    # x is a list (or vector) of length 318
    return max(0, x[140])
def l522_111(x):
    # x is a list (or vector) of length 318
    return max(0, x[141])
def l522_112(x):
    # x is a list (or vector) of length 318
    return max(0, x[142])
def l522_113(x):
    # x is a list (or vector) of length 318
    return max(0, x[143])
def l522_114(x):
    # x is a list (or vector) of length 318
    return max(0, x[144])
def l522_115(x):
    # x is a list (or vector) of length 318
    return max(0, x[145])
def l522_116(x):
    # x is a list (or vector) of length 318
    return max(0, x[146])
def l522_117(x):
    # x is a list (or vector) of length 318
    return max(0, x[147])
def l522_118(x):
    # x is a list (or vector) of length 318
    return max(0, x[148])
def l522_119(x):
    # x is a list (or vector) of length 318
    return max(0, x[149])
def l522_120(x):
    # x is a list (or vector) of length 318
    return max(0, x[150])
def l522_121(x):
    # x is a list (or vector) of length 318
    return max(0, x[151])
def l522_122(x):
    # x is a list (or vector) of length 318
    return max(0, x[152])
def l522_123(x):
    # x is a list (or vector) of length 318
    return max(0, x[153])
def l522_124(x):
    # x is a list (or vector) of length 318
    return max(0, x[154])
def l522_125(x):
    # x is a list (or vector) of length 318
    return max(0, x[155])
def l522_126(x):
    # x is a list (or vector) of length 318
    return max(0, x[156])
def l522_127(x):
    # x is a list (or vector) of length 318
    return max(0, x[157])
def l522_128(x):
    # x is a list (or vector) of length 318
    return max(0, x[158])
def l522_129(x):
    # x is a list (or vector) of length 318
    return max(0, x[159])
def l522_130(x):
    # x is a list (or vector) of length 318
    return max(0, x[160])
def l522_131(x):
    # x is a list (or vector) of length 318
    return max(0, x[161])
def l522_132(x):
    # x is a list (or vector) of length 318
    return max(0, x[162])
def l522_133(x):
    # x is a list (or vector) of length 318
    return max(0, x[163])
def l522_134(x):
    # x is a list (or vector) of length 318
    return max(0, x[164])
def l522_135(x):
    # x is a list (or vector) of length 318
    return max(0, x[165])
def l522_136(x):
    # x is a list (or vector) of length 318
    return max(0, x[166])
def l522_137(x):
    # x is a list (or vector) of length 318
    return max(0, x[167])
def l522_138(x):
    # x is a list (or vector) of length 318
    return max(0, x[168])
def l522_139(x):
    # x is a list (or vector) of length 318
    return max(0, x[169])
def l522_140(x):
    # x is a list (or vector) of length 318
    return max(0, x[170])
def l522_141(x):
    # x is a list (or vector) of length 318
    return max(0, x[171])
def l522_142(x):
    # x is a list (or vector) of length 318
    return max(0, x[172])
def l522_143(x):
    # x is a list (or vector) of length 318
    return max(0, x[173])
def l522_144(x):
    # x is a list (or vector) of length 318
    return max(0, x[174])
def l522_145(x):
    # x is a list (or vector) of length 318
    return max(0, x[175])
def l522_146(x):
    # x is a list (or vector) of length 318
    return max(0, x[176])
def l522_147(x):
    # x is a list (or vector) of length 318
    return max(0, x[177])
def l522_148(x):
    # x is a list (or vector) of length 318
    return max(0, x[178])
def l522_149(x):
    # x is a list (or vector) of length 318
    return max(0, x[179])
def l522_150(x):
    # x is a list (or vector) of length 318
    return max(0, x[180])
def l522_151(x):
    # x is a list (or vector) of length 318
    return max(0, x[181])
def l522_152(x):
    # x is a list (or vector) of length 318
    return max(0, x[182])
def l522_153(x):
    # x is a list (or vector) of length 318
    return max(0, x[183])
def l522_154(x):
    # x is a list (or vector) of length 318
    return max(0, x[184])
def l522_155(x):
    # x is a list (or vector) of length 318
    return max(0, x[185])
def l522_156(x):
    # x is a list (or vector) of length 318
    return max(0, x[186])
def l522_157(x):
    # x is a list (or vector) of length 318
    return max(0, x[187])
def l522_158(x):
    # x is a list (or vector) of length 318
    return max(0, x[188])
def l522_159(x):
    # x is a list (or vector) of length 318
    return max(0, x[189])
def l522_160(x):
    # x is a list (or vector) of length 318
    return max(0, x[190])
def l522_161(x):
    # x is a list (or vector) of length 318
    return max(0, x[191])
def l522_162(x):
    # x is a list (or vector) of length 318
    return max(0, x[192])
def l522_163(x):
    # x is a list (or vector) of length 318
    return max(0, x[193])
def l522_164(x):
    # x is a list (or vector) of length 318
    return max(0, x[194])
def l522_165(x):
    # x is a list (or vector) of length 318
    return max(0, x[195])
def l522_166(x):
    # x is a list (or vector) of length 318
    return max(0, x[196])
def l522_167(x):
    # x is a list (or vector) of length 318
    return max(0, x[197])
def l522_168(x):
    # x is a list (or vector) of length 318
    return max(0, x[198])
def l522_169(x):
    # x is a list (or vector) of length 318
    return max(0, x[199])
def l522_170(x):
    # x is a list (or vector) of length 318
    return max(0, x[200])
def l522_171(x):
    # x is a list (or vector) of length 318
    return max(0, x[201])
def l522_172(x):
    # x is a list (or vector) of length 318
    return max(0, x[202])
def l522_173(x):
    # x is a list (or vector) of length 318
    return max(0, x[203])
def l522_174(x):
    # x is a list (or vector) of length 318
    return max(0, x[204])
def l522_175(x):
    # x is a list (or vector) of length 318
    return max(0, x[205])
def l522_176(x):
    # x is a list (or vector) of length 318
    return max(0, x[206])
def l522_177(x):
    # x is a list (or vector) of length 318
    return max(0, x[207])
def l522_178(x):
    # x is a list (or vector) of length 318
    return max(0, x[208])
def l522_179(x):
    # x is a list (or vector) of length 318
    return max(0, x[209])
def l522_180(x):
    # x is a list (or vector) of length 318
    return max(0, x[210])
def l522_181(x):
    # x is a list (or vector) of length 318
    return max(0, x[211])
def l522_182(x):
    # x is a list (or vector) of length 318
    return max(0, x[212])
def l522_183(x):
    # x is a list (or vector) of length 318
    return max(0, x[213])
def l522_184(x):
    # x is a list (or vector) of length 318
    return max(0, x[214])
def l522_185(x):
    # x is a list (or vector) of length 318
    return max(0, x[215])
def l522_186(x):
    # x is a list (or vector) of length 318
    return max(0, x[216])
def l522_187(x):
    # x is a list (or vector) of length 318
    return max(0, x[217])
def l522_188(x):
    # x is a list (or vector) of length 318
    return max(0, x[218])
def l522_189(x):
    # x is a list (or vector) of length 318
    return max(0, x[219])
def l522_190(x):
    # x is a list (or vector) of length 318
    return max(0, x[220])
def l522_191(x):
    # x is a list (or vector) of length 318
    return max(0, x[221])
def l522_192(x):
    # x is a list (or vector) of length 318
    return max(0, x[222])
def l522_193(x):
    # x is a list (or vector) of length 318
    return max(0, x[223])
def l522_194(x):
    # x is a list (or vector) of length 318
    return max(0, x[224])
def l522_195(x):
    # x is a list (or vector) of length 318
    return max(0, x[225])
def l522_196(x):
    # x is a list (or vector) of length 318
    return max(0, x[226])
def l522_197(x):
    # x is a list (or vector) of length 318
    return max(0, x[227])
def l522_198(x):
    # x is a list (or vector) of length 318
    return max(0, x[228])
def l522_199(x):
    # x is a list (or vector) of length 318
    return max(0, x[229])
def l522_200(x):
    # x is a list (or vector) of length 318
    return max(0, x[230])
def l522_201(x):
    # x is a list (or vector) of length 318
    return max(0, x[231])
def l522_202(x):
    # x is a list (or vector) of length 318
    return max(0, x[232])
def l522_203(x):
    # x is a list (or vector) of length 318
    return max(0, x[233])
def l522_204(x):
    # x is a list (or vector) of length 318
    return max(0, x[234])
def l522_205(x):
    # x is a list (or vector) of length 318
    return max(0, x[235])
def l522_206(x):
    # x is a list (or vector) of length 318
    return max(0, x[236])
def l522_207(x):
    # x is a list (or vector) of length 318
    return max(0, x[237])
def l522_208(x):
    # x is a list (or vector) of length 318
    return max(0, x[238])
def l522_209(x):
    # x is a list (or vector) of length 318
    return max(0, x[239])
def l522_210(x):
    # x is a list (or vector) of length 318
    return max(0, x[240])
def l522_211(x):
    # x is a list (or vector) of length 318
    return max(0, x[241])
def l522_212(x):
    # x is a list (or vector) of length 318
    return max(0, x[242])
def l522_213(x):
    # x is a list (or vector) of length 318
    return max(0, x[243])
def l522_214(x):
    # x is a list (or vector) of length 318
    return max(0, x[244])
def l522_215(x):
    # x is a list (or vector) of length 318
    return max(0, x[245])
def l522_216(x):
    # x is a list (or vector) of length 318
    return max(0, x[246])
def l522_217(x):
    # x is a list (or vector) of length 318
    return max(0, x[247])
def l522_218(x):
    # x is a list (or vector) of length 318
    return max(0, x[248])
def l522_219(x):
    # x is a list (or vector) of length 318
    return max(0, x[249])
def l522_220(x):
    # x is a list (or vector) of length 318
    return max(0, x[250])
def l522_221(x):
    # x is a list (or vector) of length 318
    return max(0, x[251])
def l522_222(x):
    # x is a list (or vector) of length 318
    return max(0, x[252])
def l522_223(x):
    # x is a list (or vector) of length 318
    return max(0, x[253])
def l522_224(x):
    # x is a list (or vector) of length 318
    return max(0, x[254])
def l522_225(x):
    # x is a list (or vector) of length 318
    return max(0, x[255])
def l522_226(x):
    # x is a list (or vector) of length 318
    return max(0, x[256])
def l522_227(x):
    # x is a list (or vector) of length 318
    return max(0, x[257])
def l522_228(x):
    # x is a list (or vector) of length 318
    return max(0, x[258])
def l522_229(x):
    # x is a list (or vector) of length 318
    return max(0, x[259])
def l522_230(x):
    # x is a list (or vector) of length 318
    return max(0, x[260])
def l522_231(x):
    # x is a list (or vector) of length 318
    return max(0, x[261])
def l522_232(x):
    # x is a list (or vector) of length 318
    return max(0, x[262])
def l522_233(x):
    # x is a list (or vector) of length 318
    return max(0, x[263])
def l522_234(x):
    # x is a list (or vector) of length 318
    return max(0, x[264])
def l522_235(x):
    # x is a list (or vector) of length 318
    return max(0, x[265])
def l522_236(x):
    # x is a list (or vector) of length 318
    return max(0, x[266])
def l522_237(x):
    # x is a list (or vector) of length 318
    return max(0, x[267])
def l522_238(x):
    # x is a list (or vector) of length 318
    return max(0, x[268])
def l522_239(x):
    # x is a list (or vector) of length 318
    return max(0, x[269])
def l522_240(x):
    # x is a list (or vector) of length 318
    return max(0, x[270])
def l522_241(x):
    # x is a list (or vector) of length 318
    return max(0, x[271])
def l522_242(x):
    # x is a list (or vector) of length 318
    return max(0, x[272])
def l522_243(x):
    # x is a list (or vector) of length 318
    return max(0, x[273])
def l522_244(x):
    # x is a list (or vector) of length 318
    return max(0, x[274])
def l522_245(x):
    # x is a list (or vector) of length 318
    return max(0, x[275])
def l522_246(x):
    # x is a list (or vector) of length 318
    return max(0, x[276])
def l522_247(x):
    # x is a list (or vector) of length 318
    return max(0, x[277])
def l522_248(x):
    # x is a list (or vector) of length 318
    return max(0, x[278])
def l522_249(x):
    # x is a list (or vector) of length 318
    return max(0, x[279])
def l522_250(x):
    # x is a list (or vector) of length 318
    return max(0, x[280])
def l522_251(x):
    # x is a list (or vector) of length 318
    return max(0, x[281])
def l522_252(x):
    # x is a list (or vector) of length 318
    return max(0, x[282])
def l522_253(x):
    # x is a list (or vector) of length 318
    return max(0, x[283])
def l522_254(x):
    # x is a list (or vector) of length 318
    return max(0, x[284])
def l522_255(x):
    # x is a list (or vector) of length 318
    return max(0, x[285])
def l522_256(x):
    # x is a list (or vector) of length 318
    return max(0, x[286])
def l522_257(x):
    # x is a list (or vector) of length 318
    return max(0, x[287])
def l522_258(x):
    # x is a list (or vector) of length 318
    return max(0, x[288])
def l522_259(x):
    # x is a list (or vector) of length 318
    return max(0, x[289])
def l522_260(x):
    # x is a list (or vector) of length 318
    return max(0, x[290])
def l522_261(x):
    # x is a list (or vector) of length 318
    return max(0, x[291])
def l522_262(x):
    # x is a list (or vector) of length 318
    return max(0, x[292])
def l522_263(x):
    # x is a list (or vector) of length 318
    return max(0, x[293])
def l522_264(x):
    # x is a list (or vector) of length 318
    return max(0, x[294])
def l522_265(x):
    # x is a list (or vector) of length 318
    return max(0, x[295])
def l522_266(x):
    # x is a list (or vector) of length 318
    return max(0, x[296])
def l522_267(x):
    # x is a list (or vector) of length 318
    return max(0, x[297])
def l522_268(x):
    # x is a list (or vector) of length 318
    return max(0, x[298])
def l522_269(x):
    # x is a list (or vector) of length 318
    return max(0, x[299])
def l522_270(x):
    # x is a list (or vector) of length 318
    return max(0, x[300])
def l522_271(x):
    # x is a list (or vector) of length 318
    return max(0, x[301])
def l522_272(x):
    # x is a list (or vector) of length 318
    return max(0, x[302])
def l522_273(x):
    # x is a list (or vector) of length 318
    return max(0, x[303])
def l522_274(x):
    # x is a list (or vector) of length 318
    return max(0, x[304])
def l522_275(x):
    # x is a list (or vector) of length 318
    return max(0, x[305])
def l522_276(x):
    # x is a list (or vector) of length 318
    return max(0, x[306])
def l522_277(x):
    # x is a list (or vector) of length 318
    return max(0, x[307])
def l522_278(x):
    # x is a list (or vector) of length 318
    return max(0, x[308])
def l522_279(x):
    # x is a list (or vector) of length 318
    return max(0, x[309])
def l522_280(x):
    # x is a list (or vector) of length 318
    return max(0, x[310])
def l522_281(x):
    # x is a list (or vector) of length 318
    return max(0, x[311])
def l522_282(x):
    # x is a list (or vector) of length 318
    return max(0, x[312])
def l522_283(x):
    # x is a list (or vector) of length 318
    return max(0, x[313])
def l522_284(x):
    # x is a list (or vector) of length 318
    return max(0, x[314])
def l522_285(x):
    # x is a list (or vector) of length 318
    return max(0, x[315])
def l522_286(x):
    # x is a list (or vector) of length 318
    return max(0, x[316])
def l522_287(x):
    # x is a list (or vector) of length 318
    return max(0, x[317])
def l522_(x):
    # x is a list (or vector) of length 318
    return [
        l522_0(x),
        l522_1(x),
        l522_2(x),
        l522_3(x),
        l522_4(x),
        l522_5(x),
        l522_6(x),
        l522_7(x),
        l522_8(x),
        l522_9(x),
        l522_10(x),
        l522_11(x),
        l522_12(x),
        l522_13(x),
        l522_14(x),
        l522_15(x),
        l522_16(x),
        l522_17(x),
        l522_18(x),
        l522_19(x),
        l522_20(x),
        l522_21(x),
        l522_22(x),
        l522_23(x),
        l522_24(x),
        l522_25(x),
        l522_26(x),
        l522_27(x),
        l522_28(x),
        l522_29(x),
        l522_30(x),
        l522_31(x),
        l522_32(x),
        l522_33(x),
        l522_34(x),
        l522_35(x),
        l522_36(x),
        l522_37(x),
        l522_38(x),
        l522_39(x),
        l522_40(x),
        l522_41(x),
        l522_42(x),
        l522_43(x),
        l522_44(x),
        l522_45(x),
        l522_46(x),
        l522_47(x),
        l522_48(x),
        l522_49(x),
        l522_50(x),
        l522_51(x),
        l522_52(x),
        l522_53(x),
        l522_54(x),
        l522_55(x),
        l522_56(x),
        l522_57(x),
        l522_58(x),
        l522_59(x),
        l522_60(x),
        l522_61(x),
        l522_62(x),
        l522_63(x),
        l522_64(x),
        l522_65(x),
        l522_66(x),
        l522_67(x),
        l522_68(x),
        l522_69(x),
        l522_70(x),
        l522_71(x),
        l522_72(x),
        l522_73(x),
        l522_74(x),
        l522_75(x),
        l522_76(x),
        l522_77(x),
        l522_78(x),
        l522_79(x),
        l522_80(x),
        l522_81(x),
        l522_82(x),
        l522_83(x),
        l522_84(x),
        l522_85(x),
        l522_86(x),
        l522_87(x),
        l522_88(x),
        l522_89(x),
        l522_90(x),
        l522_91(x),
        l522_92(x),
        l522_93(x),
        l522_94(x),
        l522_95(x),
        l522_96(x),
        l522_97(x),
        l522_98(x),
        l522_99(x),
        l522_100(x),
        l522_101(x),
        l522_102(x),
        l522_103(x),
        l522_104(x),
        l522_105(x),
        l522_106(x),
        l522_107(x),
        l522_108(x),
        l522_109(x),
        l522_110(x),
        l522_111(x),
        l522_112(x),
        l522_113(x),
        l522_114(x),
        l522_115(x),
        l522_116(x),
        l522_117(x),
        l522_118(x),
        l522_119(x),
        l522_120(x),
        l522_121(x),
        l522_122(x),
        l522_123(x),
        l522_124(x),
        l522_125(x),
        l522_126(x),
        l522_127(x),
        l522_128(x),
        l522_129(x),
        l522_130(x),
        l522_131(x),
        l522_132(x),
        l522_133(x),
        l522_134(x),
        l522_135(x),
        l522_136(x),
        l522_137(x),
        l522_138(x),
        l522_139(x),
        l522_140(x),
        l522_141(x),
        l522_142(x),
        l522_143(x),
        l522_144(x),
        l522_145(x),
        l522_146(x),
        l522_147(x),
        l522_148(x),
        l522_149(x),
        l522_150(x),
        l522_151(x),
        l522_152(x),
        l522_153(x),
        l522_154(x),
        l522_155(x),
        l522_156(x),
        l522_157(x),
        l522_158(x),
        l522_159(x),
        l522_160(x),
        l522_161(x),
        l522_162(x),
        l522_163(x),
        l522_164(x),
        l522_165(x),
        l522_166(x),
        l522_167(x),
        l522_168(x),
        l522_169(x),
        l522_170(x),
        l522_171(x),
        l522_172(x),
        l522_173(x),
        l522_174(x),
        l522_175(x),
        l522_176(x),
        l522_177(x),
        l522_178(x),
        l522_179(x),
        l522_180(x),
        l522_181(x),
        l522_182(x),
        l522_183(x),
        l522_184(x),
        l522_185(x),
        l522_186(x),
        l522_187(x),
        l522_188(x),
        l522_189(x),
        l522_190(x),
        l522_191(x),
        l522_192(x),
        l522_193(x),
        l522_194(x),
        l522_195(x),
        l522_196(x),
        l522_197(x),
        l522_198(x),
        l522_199(x),
        l522_200(x),
        l522_201(x),
        l522_202(x),
        l522_203(x),
        l522_204(x),
        l522_205(x),
        l522_206(x),
        l522_207(x),
        l522_208(x),
        l522_209(x),
        l522_210(x),
        l522_211(x),
        l522_212(x),
        l522_213(x),
        l522_214(x),
        l522_215(x),
        l522_216(x),
        l522_217(x),
        l522_218(x),
        l522_219(x),
        l522_220(x),
        l522_221(x),
        l522_222(x),
        l522_223(x),
        l522_224(x),
        l522_225(x),
        l522_226(x),
        l522_227(x),
        l522_228(x),
        l522_229(x),
        l522_230(x),
        l522_231(x),
        l522_232(x),
        l522_233(x),
        l522_234(x),
        l522_235(x),
        l522_236(x),
        l522_237(x),
        l522_238(x),
        l522_239(x),
        l522_240(x),
        l522_241(x),
        l522_242(x),
        l522_243(x),
        l522_244(x),
        l522_245(x),
        l522_246(x),
        l522_247(x),
        l522_248(x),
        l522_249(x),
        l522_250(x),
        l522_251(x),
        l522_252(x),
        l522_253(x),
        l522_254(x),
        l522_255(x),
        l522_256(x),
        l522_257(x),
        l522_258(x),
        l522_259(x),
        l522_260(x),
        l522_261(x),
        l522_262(x),
        l522_263(x),
        l522_264(x),
        l522_265(x),
        l522_266(x),
        l522_267(x),
        l522_268(x),
        l522_269(x),
        l522_270(x),
        l522_271(x),
        l522_272(x),
        l522_273(x),
        l522_274(x),
        l522_275(x),
        l522_276(x),
        l522_277(x),
        l522_278(x),
        l522_279(x),
        l522_280(x),
        l522_281(x),
        l522_282(x),
        l522_283(x),
        l522_284(x),
        l522_285(x),
        l522_286(x),
        l522_287(x),
    ]