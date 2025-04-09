import numpy as np




# Generated from reverse engineering
def l98_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 288
    out = np.empty(288, dtype=np.float32)
    
    # for i in range(0, 33):
    for i in range(0, 33):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x7fffffff (len=31)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(33, 64):
    for i in range(0, 31):
        s = -1 * x[33 + i] + -1 * x[64 + i]
        s += biases[i]
        out[33 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 65):
    for i in range(0, 1):
        s = x[126 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(65, 96):
    for i in range(0, 31):
        s = x[95 + i]
        out[65 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 288):
    for i in range(0, 192):
        s = x[127 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l98_0(x):
    # x is a list (or vector) of length 319
    return max(0, x[0])
def l98_1(x):
    # x is a list (or vector) of length 319
    return max(0, x[1])
def l98_2(x):
    # x is a list (or vector) of length 319
    return max(0, x[2])
def l98_3(x):
    # x is a list (or vector) of length 319
    return max(0, x[3])
def l98_4(x):
    # x is a list (or vector) of length 319
    return max(0, x[4])
def l98_5(x):
    # x is a list (or vector) of length 319
    return max(0, x[5])
def l98_6(x):
    # x is a list (or vector) of length 319
    return max(0, x[6])
def l98_7(x):
    # x is a list (or vector) of length 319
    return max(0, x[7])
def l98_8(x):
    # x is a list (or vector) of length 319
    return max(0, x[8])
def l98_9(x):
    # x is a list (or vector) of length 319
    return max(0, x[9])
def l98_10(x):
    # x is a list (or vector) of length 319
    return max(0, x[10])
def l98_11(x):
    # x is a list (or vector) of length 319
    return max(0, x[11])
def l98_12(x):
    # x is a list (or vector) of length 319
    return max(0, x[12])
def l98_13(x):
    # x is a list (or vector) of length 319
    return max(0, x[13])
def l98_14(x):
    # x is a list (or vector) of length 319
    return max(0, x[14])
def l98_15(x):
    # x is a list (or vector) of length 319
    return max(0, x[15])
def l98_16(x):
    # x is a list (or vector) of length 319
    return max(0, x[16])
def l98_17(x):
    # x is a list (or vector) of length 319
    return max(0, x[17])
def l98_18(x):
    # x is a list (or vector) of length 319
    return max(0, x[18])
def l98_19(x):
    # x is a list (or vector) of length 319
    return max(0, x[19])
def l98_20(x):
    # x is a list (or vector) of length 319
    return max(0, x[20])
def l98_21(x):
    # x is a list (or vector) of length 319
    return max(0, x[21])
def l98_22(x):
    # x is a list (or vector) of length 319
    return max(0, x[22])
def l98_23(x):
    # x is a list (or vector) of length 319
    return max(0, x[23])
def l98_24(x):
    # x is a list (or vector) of length 319
    return max(0, x[24])
def l98_25(x):
    # x is a list (or vector) of length 319
    return max(0, x[25])
def l98_26(x):
    # x is a list (or vector) of length 319
    return max(0, x[26])
def l98_27(x):
    # x is a list (or vector) of length 319
    return max(0, x[27])
def l98_28(x):
    # x is a list (or vector) of length 319
    return max(0, x[28])
def l98_29(x):
    # x is a list (or vector) of length 319
    return max(0, x[29])
def l98_30(x):
    # x is a list (or vector) of length 319
    return max(0, x[30])
def l98_31(x):
    # x is a list (or vector) of length 319
    return max(0, x[31])
def l98_32(x):
    # x is a list (or vector) of length 319
    return max(0, x[32])
def l98_33(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[33] + -1.0*x[64] + 1.0)
def l98_34(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[34] + -1.0*x[65] + 1.0)
def l98_35(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[35] + -1.0*x[66] + 1.0)
def l98_36(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[36] + -1.0*x[67] + 1.0)
def l98_37(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[37] + -1.0*x[68] + 1.0)
def l98_38(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[38] + -1.0*x[69] + 1.0)
def l98_39(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[39] + -1.0*x[70] + 1.0)
def l98_40(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[40] + -1.0*x[71] + 1.0)
def l98_41(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[41] + -1.0*x[72] + 1.0)
def l98_42(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[42] + -1.0*x[73] + 1.0)
def l98_43(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[43] + -1.0*x[74] + 1.0)
def l98_44(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[44] + -1.0*x[75] + 1.0)
def l98_45(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[45] + -1.0*x[76] + 1.0)
def l98_46(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[46] + -1.0*x[77] + 1.0)
def l98_47(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[47] + -1.0*x[78] + 1.0)
def l98_48(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[48] + -1.0*x[79] + 1.0)
def l98_49(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[49] + -1.0*x[80] + 1.0)
def l98_50(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[50] + -1.0*x[81] + 1.0)
def l98_51(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[51] + -1.0*x[82] + 1.0)
def l98_52(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[52] + -1.0*x[83] + 1.0)
def l98_53(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[53] + -1.0*x[84] + 1.0)
def l98_54(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[54] + -1.0*x[85] + 1.0)
def l98_55(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[55] + -1.0*x[86] + 1.0)
def l98_56(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[56] + -1.0*x[87] + 1.0)
def l98_57(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[57] + -1.0*x[88] + 1.0)
def l98_58(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[58] + -1.0*x[89] + 1.0)
def l98_59(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[59] + -1.0*x[90] + 1.0)
def l98_60(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[60] + -1.0*x[91] + 1.0)
def l98_61(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[61] + -1.0*x[92] + 1.0)
def l98_62(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[62] + -1.0*x[93] + 1.0)
def l98_63(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[63] + -1.0*x[94] + 1.0)
def l98_64(x):
    # x is a list (or vector) of length 319
    return max(0, x[126])
def l98_65(x):
    # x is a list (or vector) of length 319
    return max(0, x[95])
def l98_66(x):
    # x is a list (or vector) of length 319
    return max(0, x[96])
def l98_67(x):
    # x is a list (or vector) of length 319
    return max(0, x[97])
def l98_68(x):
    # x is a list (or vector) of length 319
    return max(0, x[98])
def l98_69(x):
    # x is a list (or vector) of length 319
    return max(0, x[99])
def l98_70(x):
    # x is a list (or vector) of length 319
    return max(0, x[100])
def l98_71(x):
    # x is a list (or vector) of length 319
    return max(0, x[101])
def l98_72(x):
    # x is a list (or vector) of length 319
    return max(0, x[102])
def l98_73(x):
    # x is a list (or vector) of length 319
    return max(0, x[103])
def l98_74(x):
    # x is a list (or vector) of length 319
    return max(0, x[104])
def l98_75(x):
    # x is a list (or vector) of length 319
    return max(0, x[105])
def l98_76(x):
    # x is a list (or vector) of length 319
    return max(0, x[106])
def l98_77(x):
    # x is a list (or vector) of length 319
    return max(0, x[107])
def l98_78(x):
    # x is a list (or vector) of length 319
    return max(0, x[108])
def l98_79(x):
    # x is a list (or vector) of length 319
    return max(0, x[109])
def l98_80(x):
    # x is a list (or vector) of length 319
    return max(0, x[110])
def l98_81(x):
    # x is a list (or vector) of length 319
    return max(0, x[111])
def l98_82(x):
    # x is a list (or vector) of length 319
    return max(0, x[112])
def l98_83(x):
    # x is a list (or vector) of length 319
    return max(0, x[113])
def l98_84(x):
    # x is a list (or vector) of length 319
    return max(0, x[114])
def l98_85(x):
    # x is a list (or vector) of length 319
    return max(0, x[115])
def l98_86(x):
    # x is a list (or vector) of length 319
    return max(0, x[116])
def l98_87(x):
    # x is a list (or vector) of length 319
    return max(0, x[117])
def l98_88(x):
    # x is a list (or vector) of length 319
    return max(0, x[118])
def l98_89(x):
    # x is a list (or vector) of length 319
    return max(0, x[119])
def l98_90(x):
    # x is a list (or vector) of length 319
    return max(0, x[120])
def l98_91(x):
    # x is a list (or vector) of length 319
    return max(0, x[121])
def l98_92(x):
    # x is a list (or vector) of length 319
    return max(0, x[122])
def l98_93(x):
    # x is a list (or vector) of length 319
    return max(0, x[123])
def l98_94(x):
    # x is a list (or vector) of length 319
    return max(0, x[124])
def l98_95(x):
    # x is a list (or vector) of length 319
    return max(0, x[125])
def l98_96(x):
    # x is a list (or vector) of length 319
    return max(0, x[127])
def l98_97(x):
    # x is a list (or vector) of length 319
    return max(0, x[128])
def l98_98(x):
    # x is a list (or vector) of length 319
    return max(0, x[129])
def l98_99(x):
    # x is a list (or vector) of length 319
    return max(0, x[130])
def l98_100(x):
    # x is a list (or vector) of length 319
    return max(0, x[131])
def l98_101(x):
    # x is a list (or vector) of length 319
    return max(0, x[132])
def l98_102(x):
    # x is a list (or vector) of length 319
    return max(0, x[133])
def l98_103(x):
    # x is a list (or vector) of length 319
    return max(0, x[134])
def l98_104(x):
    # x is a list (or vector) of length 319
    return max(0, x[135])
def l98_105(x):
    # x is a list (or vector) of length 319
    return max(0, x[136])
def l98_106(x):
    # x is a list (or vector) of length 319
    return max(0, x[137])
def l98_107(x):
    # x is a list (or vector) of length 319
    return max(0, x[138])
def l98_108(x):
    # x is a list (or vector) of length 319
    return max(0, x[139])
def l98_109(x):
    # x is a list (or vector) of length 319
    return max(0, x[140])
def l98_110(x):
    # x is a list (or vector) of length 319
    return max(0, x[141])
def l98_111(x):
    # x is a list (or vector) of length 319
    return max(0, x[142])
def l98_112(x):
    # x is a list (or vector) of length 319
    return max(0, x[143])
def l98_113(x):
    # x is a list (or vector) of length 319
    return max(0, x[144])
def l98_114(x):
    # x is a list (or vector) of length 319
    return max(0, x[145])
def l98_115(x):
    # x is a list (or vector) of length 319
    return max(0, x[146])
def l98_116(x):
    # x is a list (or vector) of length 319
    return max(0, x[147])
def l98_117(x):
    # x is a list (or vector) of length 319
    return max(0, x[148])
def l98_118(x):
    # x is a list (or vector) of length 319
    return max(0, x[149])
def l98_119(x):
    # x is a list (or vector) of length 319
    return max(0, x[150])
def l98_120(x):
    # x is a list (or vector) of length 319
    return max(0, x[151])
def l98_121(x):
    # x is a list (or vector) of length 319
    return max(0, x[152])
def l98_122(x):
    # x is a list (or vector) of length 319
    return max(0, x[153])
def l98_123(x):
    # x is a list (or vector) of length 319
    return max(0, x[154])
def l98_124(x):
    # x is a list (or vector) of length 319
    return max(0, x[155])
def l98_125(x):
    # x is a list (or vector) of length 319
    return max(0, x[156])
def l98_126(x):
    # x is a list (or vector) of length 319
    return max(0, x[157])
def l98_127(x):
    # x is a list (or vector) of length 319
    return max(0, x[158])
def l98_128(x):
    # x is a list (or vector) of length 319
    return max(0, x[159])
def l98_129(x):
    # x is a list (or vector) of length 319
    return max(0, x[160])
def l98_130(x):
    # x is a list (or vector) of length 319
    return max(0, x[161])
def l98_131(x):
    # x is a list (or vector) of length 319
    return max(0, x[162])
def l98_132(x):
    # x is a list (or vector) of length 319
    return max(0, x[163])
def l98_133(x):
    # x is a list (or vector) of length 319
    return max(0, x[164])
def l98_134(x):
    # x is a list (or vector) of length 319
    return max(0, x[165])
def l98_135(x):
    # x is a list (or vector) of length 319
    return max(0, x[166])
def l98_136(x):
    # x is a list (or vector) of length 319
    return max(0, x[167])
def l98_137(x):
    # x is a list (or vector) of length 319
    return max(0, x[168])
def l98_138(x):
    # x is a list (or vector) of length 319
    return max(0, x[169])
def l98_139(x):
    # x is a list (or vector) of length 319
    return max(0, x[170])
def l98_140(x):
    # x is a list (or vector) of length 319
    return max(0, x[171])
def l98_141(x):
    # x is a list (or vector) of length 319
    return max(0, x[172])
def l98_142(x):
    # x is a list (or vector) of length 319
    return max(0, x[173])
def l98_143(x):
    # x is a list (or vector) of length 319
    return max(0, x[174])
def l98_144(x):
    # x is a list (or vector) of length 319
    return max(0, x[175])
def l98_145(x):
    # x is a list (or vector) of length 319
    return max(0, x[176])
def l98_146(x):
    # x is a list (or vector) of length 319
    return max(0, x[177])
def l98_147(x):
    # x is a list (or vector) of length 319
    return max(0, x[178])
def l98_148(x):
    # x is a list (or vector) of length 319
    return max(0, x[179])
def l98_149(x):
    # x is a list (or vector) of length 319
    return max(0, x[180])
def l98_150(x):
    # x is a list (or vector) of length 319
    return max(0, x[181])
def l98_151(x):
    # x is a list (or vector) of length 319
    return max(0, x[182])
def l98_152(x):
    # x is a list (or vector) of length 319
    return max(0, x[183])
def l98_153(x):
    # x is a list (or vector) of length 319
    return max(0, x[184])
def l98_154(x):
    # x is a list (or vector) of length 319
    return max(0, x[185])
def l98_155(x):
    # x is a list (or vector) of length 319
    return max(0, x[186])
def l98_156(x):
    # x is a list (or vector) of length 319
    return max(0, x[187])
def l98_157(x):
    # x is a list (or vector) of length 319
    return max(0, x[188])
def l98_158(x):
    # x is a list (or vector) of length 319
    return max(0, x[189])
def l98_159(x):
    # x is a list (or vector) of length 319
    return max(0, x[190])
def l98_160(x):
    # x is a list (or vector) of length 319
    return max(0, x[191])
def l98_161(x):
    # x is a list (or vector) of length 319
    return max(0, x[192])
def l98_162(x):
    # x is a list (or vector) of length 319
    return max(0, x[193])
def l98_163(x):
    # x is a list (or vector) of length 319
    return max(0, x[194])
def l98_164(x):
    # x is a list (or vector) of length 319
    return max(0, x[195])
def l98_165(x):
    # x is a list (or vector) of length 319
    return max(0, x[196])
def l98_166(x):
    # x is a list (or vector) of length 319
    return max(0, x[197])
def l98_167(x):
    # x is a list (or vector) of length 319
    return max(0, x[198])
def l98_168(x):
    # x is a list (or vector) of length 319
    return max(0, x[199])
def l98_169(x):
    # x is a list (or vector) of length 319
    return max(0, x[200])
def l98_170(x):
    # x is a list (or vector) of length 319
    return max(0, x[201])
def l98_171(x):
    # x is a list (or vector) of length 319
    return max(0, x[202])
def l98_172(x):
    # x is a list (or vector) of length 319
    return max(0, x[203])
def l98_173(x):
    # x is a list (or vector) of length 319
    return max(0, x[204])
def l98_174(x):
    # x is a list (or vector) of length 319
    return max(0, x[205])
def l98_175(x):
    # x is a list (or vector) of length 319
    return max(0, x[206])
def l98_176(x):
    # x is a list (or vector) of length 319
    return max(0, x[207])
def l98_177(x):
    # x is a list (or vector) of length 319
    return max(0, x[208])
def l98_178(x):
    # x is a list (or vector) of length 319
    return max(0, x[209])
def l98_179(x):
    # x is a list (or vector) of length 319
    return max(0, x[210])
def l98_180(x):
    # x is a list (or vector) of length 319
    return max(0, x[211])
def l98_181(x):
    # x is a list (or vector) of length 319
    return max(0, x[212])
def l98_182(x):
    # x is a list (or vector) of length 319
    return max(0, x[213])
def l98_183(x):
    # x is a list (or vector) of length 319
    return max(0, x[214])
def l98_184(x):
    # x is a list (or vector) of length 319
    return max(0, x[215])
def l98_185(x):
    # x is a list (or vector) of length 319
    return max(0, x[216])
def l98_186(x):
    # x is a list (or vector) of length 319
    return max(0, x[217])
def l98_187(x):
    # x is a list (or vector) of length 319
    return max(0, x[218])
def l98_188(x):
    # x is a list (or vector) of length 319
    return max(0, x[219])
def l98_189(x):
    # x is a list (or vector) of length 319
    return max(0, x[220])
def l98_190(x):
    # x is a list (or vector) of length 319
    return max(0, x[221])
def l98_191(x):
    # x is a list (or vector) of length 319
    return max(0, x[222])
def l98_192(x):
    # x is a list (or vector) of length 319
    return max(0, x[223])
def l98_193(x):
    # x is a list (or vector) of length 319
    return max(0, x[224])
def l98_194(x):
    # x is a list (or vector) of length 319
    return max(0, x[225])
def l98_195(x):
    # x is a list (or vector) of length 319
    return max(0, x[226])
def l98_196(x):
    # x is a list (or vector) of length 319
    return max(0, x[227])
def l98_197(x):
    # x is a list (or vector) of length 319
    return max(0, x[228])
def l98_198(x):
    # x is a list (or vector) of length 319
    return max(0, x[229])
def l98_199(x):
    # x is a list (or vector) of length 319
    return max(0, x[230])
def l98_200(x):
    # x is a list (or vector) of length 319
    return max(0, x[231])
def l98_201(x):
    # x is a list (or vector) of length 319
    return max(0, x[232])
def l98_202(x):
    # x is a list (or vector) of length 319
    return max(0, x[233])
def l98_203(x):
    # x is a list (or vector) of length 319
    return max(0, x[234])
def l98_204(x):
    # x is a list (or vector) of length 319
    return max(0, x[235])
def l98_205(x):
    # x is a list (or vector) of length 319
    return max(0, x[236])
def l98_206(x):
    # x is a list (or vector) of length 319
    return max(0, x[237])
def l98_207(x):
    # x is a list (or vector) of length 319
    return max(0, x[238])
def l98_208(x):
    # x is a list (or vector) of length 319
    return max(0, x[239])
def l98_209(x):
    # x is a list (or vector) of length 319
    return max(0, x[240])
def l98_210(x):
    # x is a list (or vector) of length 319
    return max(0, x[241])
def l98_211(x):
    # x is a list (or vector) of length 319
    return max(0, x[242])
def l98_212(x):
    # x is a list (or vector) of length 319
    return max(0, x[243])
def l98_213(x):
    # x is a list (or vector) of length 319
    return max(0, x[244])
def l98_214(x):
    # x is a list (or vector) of length 319
    return max(0, x[245])
def l98_215(x):
    # x is a list (or vector) of length 319
    return max(0, x[246])
def l98_216(x):
    # x is a list (or vector) of length 319
    return max(0, x[247])
def l98_217(x):
    # x is a list (or vector) of length 319
    return max(0, x[248])
def l98_218(x):
    # x is a list (or vector) of length 319
    return max(0, x[249])
def l98_219(x):
    # x is a list (or vector) of length 319
    return max(0, x[250])
def l98_220(x):
    # x is a list (or vector) of length 319
    return max(0, x[251])
def l98_221(x):
    # x is a list (or vector) of length 319
    return max(0, x[252])
def l98_222(x):
    # x is a list (or vector) of length 319
    return max(0, x[253])
def l98_223(x):
    # x is a list (or vector) of length 319
    return max(0, x[254])
def l98_224(x):
    # x is a list (or vector) of length 319
    return max(0, x[255])
def l98_225(x):
    # x is a list (or vector) of length 319
    return max(0, x[256])
def l98_226(x):
    # x is a list (or vector) of length 319
    return max(0, x[257])
def l98_227(x):
    # x is a list (or vector) of length 319
    return max(0, x[258])
def l98_228(x):
    # x is a list (or vector) of length 319
    return max(0, x[259])
def l98_229(x):
    # x is a list (or vector) of length 319
    return max(0, x[260])
def l98_230(x):
    # x is a list (or vector) of length 319
    return max(0, x[261])
def l98_231(x):
    # x is a list (or vector) of length 319
    return max(0, x[262])
def l98_232(x):
    # x is a list (or vector) of length 319
    return max(0, x[263])
def l98_233(x):
    # x is a list (or vector) of length 319
    return max(0, x[264])
def l98_234(x):
    # x is a list (or vector) of length 319
    return max(0, x[265])
def l98_235(x):
    # x is a list (or vector) of length 319
    return max(0, x[266])
def l98_236(x):
    # x is a list (or vector) of length 319
    return max(0, x[267])
def l98_237(x):
    # x is a list (or vector) of length 319
    return max(0, x[268])
def l98_238(x):
    # x is a list (or vector) of length 319
    return max(0, x[269])
def l98_239(x):
    # x is a list (or vector) of length 319
    return max(0, x[270])
def l98_240(x):
    # x is a list (or vector) of length 319
    return max(0, x[271])
def l98_241(x):
    # x is a list (or vector) of length 319
    return max(0, x[272])
def l98_242(x):
    # x is a list (or vector) of length 319
    return max(0, x[273])
def l98_243(x):
    # x is a list (or vector) of length 319
    return max(0, x[274])
def l98_244(x):
    # x is a list (or vector) of length 319
    return max(0, x[275])
def l98_245(x):
    # x is a list (or vector) of length 319
    return max(0, x[276])
def l98_246(x):
    # x is a list (or vector) of length 319
    return max(0, x[277])
def l98_247(x):
    # x is a list (or vector) of length 319
    return max(0, x[278])
def l98_248(x):
    # x is a list (or vector) of length 319
    return max(0, x[279])
def l98_249(x):
    # x is a list (or vector) of length 319
    return max(0, x[280])
def l98_250(x):
    # x is a list (or vector) of length 319
    return max(0, x[281])
def l98_251(x):
    # x is a list (or vector) of length 319
    return max(0, x[282])
def l98_252(x):
    # x is a list (or vector) of length 319
    return max(0, x[283])
def l98_253(x):
    # x is a list (or vector) of length 319
    return max(0, x[284])
def l98_254(x):
    # x is a list (or vector) of length 319
    return max(0, x[285])
def l98_255(x):
    # x is a list (or vector) of length 319
    return max(0, x[286])
def l98_256(x):
    # x is a list (or vector) of length 319
    return max(0, x[287])
def l98_257(x):
    # x is a list (or vector) of length 319
    return max(0, x[288])
def l98_258(x):
    # x is a list (or vector) of length 319
    return max(0, x[289])
def l98_259(x):
    # x is a list (or vector) of length 319
    return max(0, x[290])
def l98_260(x):
    # x is a list (or vector) of length 319
    return max(0, x[291])
def l98_261(x):
    # x is a list (or vector) of length 319
    return max(0, x[292])
def l98_262(x):
    # x is a list (or vector) of length 319
    return max(0, x[293])
def l98_263(x):
    # x is a list (or vector) of length 319
    return max(0, x[294])
def l98_264(x):
    # x is a list (or vector) of length 319
    return max(0, x[295])
def l98_265(x):
    # x is a list (or vector) of length 319
    return max(0, x[296])
def l98_266(x):
    # x is a list (or vector) of length 319
    return max(0, x[297])
def l98_267(x):
    # x is a list (or vector) of length 319
    return max(0, x[298])
def l98_268(x):
    # x is a list (or vector) of length 319
    return max(0, x[299])
def l98_269(x):
    # x is a list (or vector) of length 319
    return max(0, x[300])
def l98_270(x):
    # x is a list (or vector) of length 319
    return max(0, x[301])
def l98_271(x):
    # x is a list (or vector) of length 319
    return max(0, x[302])
def l98_272(x):
    # x is a list (or vector) of length 319
    return max(0, x[303])
def l98_273(x):
    # x is a list (or vector) of length 319
    return max(0, x[304])
def l98_274(x):
    # x is a list (or vector) of length 319
    return max(0, x[305])
def l98_275(x):
    # x is a list (or vector) of length 319
    return max(0, x[306])
def l98_276(x):
    # x is a list (or vector) of length 319
    return max(0, x[307])
def l98_277(x):
    # x is a list (or vector) of length 319
    return max(0, x[308])
def l98_278(x):
    # x is a list (or vector) of length 319
    return max(0, x[309])
def l98_279(x):
    # x is a list (or vector) of length 319
    return max(0, x[310])
def l98_280(x):
    # x is a list (or vector) of length 319
    return max(0, x[311])
def l98_281(x):
    # x is a list (or vector) of length 319
    return max(0, x[312])
def l98_282(x):
    # x is a list (or vector) of length 319
    return max(0, x[313])
def l98_283(x):
    # x is a list (or vector) of length 319
    return max(0, x[314])
def l98_284(x):
    # x is a list (or vector) of length 319
    return max(0, x[315])
def l98_285(x):
    # x is a list (or vector) of length 319
    return max(0, x[316])
def l98_286(x):
    # x is a list (or vector) of length 319
    return max(0, x[317])
def l98_287(x):
    # x is a list (or vector) of length 319
    return max(0, x[318])
def l98_(x):
    # x is a list (or vector) of length 319
    return [
        l98_0(x),
        l98_1(x),
        l98_2(x),
        l98_3(x),
        l98_4(x),
        l98_5(x),
        l98_6(x),
        l98_7(x),
        l98_8(x),
        l98_9(x),
        l98_10(x),
        l98_11(x),
        l98_12(x),
        l98_13(x),
        l98_14(x),
        l98_15(x),
        l98_16(x),
        l98_17(x),
        l98_18(x),
        l98_19(x),
        l98_20(x),
        l98_21(x),
        l98_22(x),
        l98_23(x),
        l98_24(x),
        l98_25(x),
        l98_26(x),
        l98_27(x),
        l98_28(x),
        l98_29(x),
        l98_30(x),
        l98_31(x),
        l98_32(x),
        l98_33(x),
        l98_34(x),
        l98_35(x),
        l98_36(x),
        l98_37(x),
        l98_38(x),
        l98_39(x),
        l98_40(x),
        l98_41(x),
        l98_42(x),
        l98_43(x),
        l98_44(x),
        l98_45(x),
        l98_46(x),
        l98_47(x),
        l98_48(x),
        l98_49(x),
        l98_50(x),
        l98_51(x),
        l98_52(x),
        l98_53(x),
        l98_54(x),
        l98_55(x),
        l98_56(x),
        l98_57(x),
        l98_58(x),
        l98_59(x),
        l98_60(x),
        l98_61(x),
        l98_62(x),
        l98_63(x),
        l98_64(x),
        l98_65(x),
        l98_66(x),
        l98_67(x),
        l98_68(x),
        l98_69(x),
        l98_70(x),
        l98_71(x),
        l98_72(x),
        l98_73(x),
        l98_74(x),
        l98_75(x),
        l98_76(x),
        l98_77(x),
        l98_78(x),
        l98_79(x),
        l98_80(x),
        l98_81(x),
        l98_82(x),
        l98_83(x),
        l98_84(x),
        l98_85(x),
        l98_86(x),
        l98_87(x),
        l98_88(x),
        l98_89(x),
        l98_90(x),
        l98_91(x),
        l98_92(x),
        l98_93(x),
        l98_94(x),
        l98_95(x),
        l98_96(x),
        l98_97(x),
        l98_98(x),
        l98_99(x),
        l98_100(x),
        l98_101(x),
        l98_102(x),
        l98_103(x),
        l98_104(x),
        l98_105(x),
        l98_106(x),
        l98_107(x),
        l98_108(x),
        l98_109(x),
        l98_110(x),
        l98_111(x),
        l98_112(x),
        l98_113(x),
        l98_114(x),
        l98_115(x),
        l98_116(x),
        l98_117(x),
        l98_118(x),
        l98_119(x),
        l98_120(x),
        l98_121(x),
        l98_122(x),
        l98_123(x),
        l98_124(x),
        l98_125(x),
        l98_126(x),
        l98_127(x),
        l98_128(x),
        l98_129(x),
        l98_130(x),
        l98_131(x),
        l98_132(x),
        l98_133(x),
        l98_134(x),
        l98_135(x),
        l98_136(x),
        l98_137(x),
        l98_138(x),
        l98_139(x),
        l98_140(x),
        l98_141(x),
        l98_142(x),
        l98_143(x),
        l98_144(x),
        l98_145(x),
        l98_146(x),
        l98_147(x),
        l98_148(x),
        l98_149(x),
        l98_150(x),
        l98_151(x),
        l98_152(x),
        l98_153(x),
        l98_154(x),
        l98_155(x),
        l98_156(x),
        l98_157(x),
        l98_158(x),
        l98_159(x),
        l98_160(x),
        l98_161(x),
        l98_162(x),
        l98_163(x),
        l98_164(x),
        l98_165(x),
        l98_166(x),
        l98_167(x),
        l98_168(x),
        l98_169(x),
        l98_170(x),
        l98_171(x),
        l98_172(x),
        l98_173(x),
        l98_174(x),
        l98_175(x),
        l98_176(x),
        l98_177(x),
        l98_178(x),
        l98_179(x),
        l98_180(x),
        l98_181(x),
        l98_182(x),
        l98_183(x),
        l98_184(x),
        l98_185(x),
        l98_186(x),
        l98_187(x),
        l98_188(x),
        l98_189(x),
        l98_190(x),
        l98_191(x),
        l98_192(x),
        l98_193(x),
        l98_194(x),
        l98_195(x),
        l98_196(x),
        l98_197(x),
        l98_198(x),
        l98_199(x),
        l98_200(x),
        l98_201(x),
        l98_202(x),
        l98_203(x),
        l98_204(x),
        l98_205(x),
        l98_206(x),
        l98_207(x),
        l98_208(x),
        l98_209(x),
        l98_210(x),
        l98_211(x),
        l98_212(x),
        l98_213(x),
        l98_214(x),
        l98_215(x),
        l98_216(x),
        l98_217(x),
        l98_218(x),
        l98_219(x),
        l98_220(x),
        l98_221(x),
        l98_222(x),
        l98_223(x),
        l98_224(x),
        l98_225(x),
        l98_226(x),
        l98_227(x),
        l98_228(x),
        l98_229(x),
        l98_230(x),
        l98_231(x),
        l98_232(x),
        l98_233(x),
        l98_234(x),
        l98_235(x),
        l98_236(x),
        l98_237(x),
        l98_238(x),
        l98_239(x),
        l98_240(x),
        l98_241(x),
        l98_242(x),
        l98_243(x),
        l98_244(x),
        l98_245(x),
        l98_246(x),
        l98_247(x),
        l98_248(x),
        l98_249(x),
        l98_250(x),
        l98_251(x),
        l98_252(x),
        l98_253(x),
        l98_254(x),
        l98_255(x),
        l98_256(x),
        l98_257(x),
        l98_258(x),
        l98_259(x),
        l98_260(x),
        l98_261(x),
        l98_262(x),
        l98_263(x),
        l98_264(x),
        l98_265(x),
        l98_266(x),
        l98_267(x),
        l98_268(x),
        l98_269(x),
        l98_270(x),
        l98_271(x),
        l98_272(x),
        l98_273(x),
        l98_274(x),
        l98_275(x),
        l98_276(x),
        l98_277(x),
        l98_278(x),
        l98_279(x),
        l98_280(x),
        l98_281(x),
        l98_282(x),
        l98_283(x),
        l98_284(x),
        l98_285(x),
        l98_286(x),
        l98_287(x),
    ]