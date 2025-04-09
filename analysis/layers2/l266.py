import numpy as np




# Generated from reverse engineering
def l266_g(x: np.ndarray) -> np.ndarray:
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




def l266_0(x):
    # x is a list (or vector) of length 319
    return max(0, x[0])
def l266_1(x):
    # x is a list (or vector) of length 319
    return max(0, x[1])
def l266_2(x):
    # x is a list (or vector) of length 319
    return max(0, x[2])
def l266_3(x):
    # x is a list (or vector) of length 319
    return max(0, x[3])
def l266_4(x):
    # x is a list (or vector) of length 319
    return max(0, x[4])
def l266_5(x):
    # x is a list (or vector) of length 319
    return max(0, x[5])
def l266_6(x):
    # x is a list (or vector) of length 319
    return max(0, x[6])
def l266_7(x):
    # x is a list (or vector) of length 319
    return max(0, x[7])
def l266_8(x):
    # x is a list (or vector) of length 319
    return max(0, x[8])
def l266_9(x):
    # x is a list (or vector) of length 319
    return max(0, x[9])
def l266_10(x):
    # x is a list (or vector) of length 319
    return max(0, x[10])
def l266_11(x):
    # x is a list (or vector) of length 319
    return max(0, x[11])
def l266_12(x):
    # x is a list (or vector) of length 319
    return max(0, x[12])
def l266_13(x):
    # x is a list (or vector) of length 319
    return max(0, x[13])
def l266_14(x):
    # x is a list (or vector) of length 319
    return max(0, x[14])
def l266_15(x):
    # x is a list (or vector) of length 319
    return max(0, x[15])
def l266_16(x):
    # x is a list (or vector) of length 319
    return max(0, x[16])
def l266_17(x):
    # x is a list (or vector) of length 319
    return max(0, x[17])
def l266_18(x):
    # x is a list (or vector) of length 319
    return max(0, x[18])
def l266_19(x):
    # x is a list (or vector) of length 319
    return max(0, x[19])
def l266_20(x):
    # x is a list (or vector) of length 319
    return max(0, x[20])
def l266_21(x):
    # x is a list (or vector) of length 319
    return max(0, x[21])
def l266_22(x):
    # x is a list (or vector) of length 319
    return max(0, x[22])
def l266_23(x):
    # x is a list (or vector) of length 319
    return max(0, x[23])
def l266_24(x):
    # x is a list (or vector) of length 319
    return max(0, x[24])
def l266_25(x):
    # x is a list (or vector) of length 319
    return max(0, x[25])
def l266_26(x):
    # x is a list (or vector) of length 319
    return max(0, x[26])
def l266_27(x):
    # x is a list (or vector) of length 319
    return max(0, x[27])
def l266_28(x):
    # x is a list (or vector) of length 319
    return max(0, x[28])
def l266_29(x):
    # x is a list (or vector) of length 319
    return max(0, x[29])
def l266_30(x):
    # x is a list (or vector) of length 319
    return max(0, x[30])
def l266_31(x):
    # x is a list (or vector) of length 319
    return max(0, x[31])
def l266_32(x):
    # x is a list (or vector) of length 319
    return max(0, x[32])
def l266_33(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[33] + -1.0*x[64] + 1.0)
def l266_34(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[34] + -1.0*x[65] + 1.0)
def l266_35(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[35] + -1.0*x[66] + 1.0)
def l266_36(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[36] + -1.0*x[67] + 1.0)
def l266_37(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[37] + -1.0*x[68] + 1.0)
def l266_38(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[38] + -1.0*x[69] + 1.0)
def l266_39(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[39] + -1.0*x[70] + 1.0)
def l266_40(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[40] + -1.0*x[71] + 1.0)
def l266_41(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[41] + -1.0*x[72] + 1.0)
def l266_42(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[42] + -1.0*x[73] + 1.0)
def l266_43(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[43] + -1.0*x[74] + 1.0)
def l266_44(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[44] + -1.0*x[75] + 1.0)
def l266_45(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[45] + -1.0*x[76] + 1.0)
def l266_46(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[46] + -1.0*x[77] + 1.0)
def l266_47(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[47] + -1.0*x[78] + 1.0)
def l266_48(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[48] + -1.0*x[79] + 1.0)
def l266_49(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[49] + -1.0*x[80] + 1.0)
def l266_50(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[50] + -1.0*x[81] + 1.0)
def l266_51(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[51] + -1.0*x[82] + 1.0)
def l266_52(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[52] + -1.0*x[83] + 1.0)
def l266_53(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[53] + -1.0*x[84] + 1.0)
def l266_54(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[54] + -1.0*x[85] + 1.0)
def l266_55(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[55] + -1.0*x[86] + 1.0)
def l266_56(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[56] + -1.0*x[87] + 1.0)
def l266_57(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[57] + -1.0*x[88] + 1.0)
def l266_58(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[58] + -1.0*x[89] + 1.0)
def l266_59(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[59] + -1.0*x[90] + 1.0)
def l266_60(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[60] + -1.0*x[91] + 1.0)
def l266_61(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[61] + -1.0*x[92] + 1.0)
def l266_62(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[62] + -1.0*x[93] + 1.0)
def l266_63(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[63] + -1.0*x[94] + 1.0)
def l266_64(x):
    # x is a list (or vector) of length 319
    return max(0, x[126])
def l266_65(x):
    # x is a list (or vector) of length 319
    return max(0, x[95])
def l266_66(x):
    # x is a list (or vector) of length 319
    return max(0, x[96])
def l266_67(x):
    # x is a list (or vector) of length 319
    return max(0, x[97])
def l266_68(x):
    # x is a list (or vector) of length 319
    return max(0, x[98])
def l266_69(x):
    # x is a list (or vector) of length 319
    return max(0, x[99])
def l266_70(x):
    # x is a list (or vector) of length 319
    return max(0, x[100])
def l266_71(x):
    # x is a list (or vector) of length 319
    return max(0, x[101])
def l266_72(x):
    # x is a list (or vector) of length 319
    return max(0, x[102])
def l266_73(x):
    # x is a list (or vector) of length 319
    return max(0, x[103])
def l266_74(x):
    # x is a list (or vector) of length 319
    return max(0, x[104])
def l266_75(x):
    # x is a list (or vector) of length 319
    return max(0, x[105])
def l266_76(x):
    # x is a list (or vector) of length 319
    return max(0, x[106])
def l266_77(x):
    # x is a list (or vector) of length 319
    return max(0, x[107])
def l266_78(x):
    # x is a list (or vector) of length 319
    return max(0, x[108])
def l266_79(x):
    # x is a list (or vector) of length 319
    return max(0, x[109])
def l266_80(x):
    # x is a list (or vector) of length 319
    return max(0, x[110])
def l266_81(x):
    # x is a list (or vector) of length 319
    return max(0, x[111])
def l266_82(x):
    # x is a list (or vector) of length 319
    return max(0, x[112])
def l266_83(x):
    # x is a list (or vector) of length 319
    return max(0, x[113])
def l266_84(x):
    # x is a list (or vector) of length 319
    return max(0, x[114])
def l266_85(x):
    # x is a list (or vector) of length 319
    return max(0, x[115])
def l266_86(x):
    # x is a list (or vector) of length 319
    return max(0, x[116])
def l266_87(x):
    # x is a list (or vector) of length 319
    return max(0, x[117])
def l266_88(x):
    # x is a list (or vector) of length 319
    return max(0, x[118])
def l266_89(x):
    # x is a list (or vector) of length 319
    return max(0, x[119])
def l266_90(x):
    # x is a list (or vector) of length 319
    return max(0, x[120])
def l266_91(x):
    # x is a list (or vector) of length 319
    return max(0, x[121])
def l266_92(x):
    # x is a list (or vector) of length 319
    return max(0, x[122])
def l266_93(x):
    # x is a list (or vector) of length 319
    return max(0, x[123])
def l266_94(x):
    # x is a list (or vector) of length 319
    return max(0, x[124])
def l266_95(x):
    # x is a list (or vector) of length 319
    return max(0, x[125])
def l266_96(x):
    # x is a list (or vector) of length 319
    return max(0, x[127])
def l266_97(x):
    # x is a list (or vector) of length 319
    return max(0, x[128])
def l266_98(x):
    # x is a list (or vector) of length 319
    return max(0, x[129])
def l266_99(x):
    # x is a list (or vector) of length 319
    return max(0, x[130])
def l266_100(x):
    # x is a list (or vector) of length 319
    return max(0, x[131])
def l266_101(x):
    # x is a list (or vector) of length 319
    return max(0, x[132])
def l266_102(x):
    # x is a list (or vector) of length 319
    return max(0, x[133])
def l266_103(x):
    # x is a list (or vector) of length 319
    return max(0, x[134])
def l266_104(x):
    # x is a list (or vector) of length 319
    return max(0, x[135])
def l266_105(x):
    # x is a list (or vector) of length 319
    return max(0, x[136])
def l266_106(x):
    # x is a list (or vector) of length 319
    return max(0, x[137])
def l266_107(x):
    # x is a list (or vector) of length 319
    return max(0, x[138])
def l266_108(x):
    # x is a list (or vector) of length 319
    return max(0, x[139])
def l266_109(x):
    # x is a list (or vector) of length 319
    return max(0, x[140])
def l266_110(x):
    # x is a list (or vector) of length 319
    return max(0, x[141])
def l266_111(x):
    # x is a list (or vector) of length 319
    return max(0, x[142])
def l266_112(x):
    # x is a list (or vector) of length 319
    return max(0, x[143])
def l266_113(x):
    # x is a list (or vector) of length 319
    return max(0, x[144])
def l266_114(x):
    # x is a list (or vector) of length 319
    return max(0, x[145])
def l266_115(x):
    # x is a list (or vector) of length 319
    return max(0, x[146])
def l266_116(x):
    # x is a list (or vector) of length 319
    return max(0, x[147])
def l266_117(x):
    # x is a list (or vector) of length 319
    return max(0, x[148])
def l266_118(x):
    # x is a list (or vector) of length 319
    return max(0, x[149])
def l266_119(x):
    # x is a list (or vector) of length 319
    return max(0, x[150])
def l266_120(x):
    # x is a list (or vector) of length 319
    return max(0, x[151])
def l266_121(x):
    # x is a list (or vector) of length 319
    return max(0, x[152])
def l266_122(x):
    # x is a list (or vector) of length 319
    return max(0, x[153])
def l266_123(x):
    # x is a list (or vector) of length 319
    return max(0, x[154])
def l266_124(x):
    # x is a list (or vector) of length 319
    return max(0, x[155])
def l266_125(x):
    # x is a list (or vector) of length 319
    return max(0, x[156])
def l266_126(x):
    # x is a list (or vector) of length 319
    return max(0, x[157])
def l266_127(x):
    # x is a list (or vector) of length 319
    return max(0, x[158])
def l266_128(x):
    # x is a list (or vector) of length 319
    return max(0, x[159])
def l266_129(x):
    # x is a list (or vector) of length 319
    return max(0, x[160])
def l266_130(x):
    # x is a list (or vector) of length 319
    return max(0, x[161])
def l266_131(x):
    # x is a list (or vector) of length 319
    return max(0, x[162])
def l266_132(x):
    # x is a list (or vector) of length 319
    return max(0, x[163])
def l266_133(x):
    # x is a list (or vector) of length 319
    return max(0, x[164])
def l266_134(x):
    # x is a list (or vector) of length 319
    return max(0, x[165])
def l266_135(x):
    # x is a list (or vector) of length 319
    return max(0, x[166])
def l266_136(x):
    # x is a list (or vector) of length 319
    return max(0, x[167])
def l266_137(x):
    # x is a list (or vector) of length 319
    return max(0, x[168])
def l266_138(x):
    # x is a list (or vector) of length 319
    return max(0, x[169])
def l266_139(x):
    # x is a list (or vector) of length 319
    return max(0, x[170])
def l266_140(x):
    # x is a list (or vector) of length 319
    return max(0, x[171])
def l266_141(x):
    # x is a list (or vector) of length 319
    return max(0, x[172])
def l266_142(x):
    # x is a list (or vector) of length 319
    return max(0, x[173])
def l266_143(x):
    # x is a list (or vector) of length 319
    return max(0, x[174])
def l266_144(x):
    # x is a list (or vector) of length 319
    return max(0, x[175])
def l266_145(x):
    # x is a list (or vector) of length 319
    return max(0, x[176])
def l266_146(x):
    # x is a list (or vector) of length 319
    return max(0, x[177])
def l266_147(x):
    # x is a list (or vector) of length 319
    return max(0, x[178])
def l266_148(x):
    # x is a list (or vector) of length 319
    return max(0, x[179])
def l266_149(x):
    # x is a list (or vector) of length 319
    return max(0, x[180])
def l266_150(x):
    # x is a list (or vector) of length 319
    return max(0, x[181])
def l266_151(x):
    # x is a list (or vector) of length 319
    return max(0, x[182])
def l266_152(x):
    # x is a list (or vector) of length 319
    return max(0, x[183])
def l266_153(x):
    # x is a list (or vector) of length 319
    return max(0, x[184])
def l266_154(x):
    # x is a list (or vector) of length 319
    return max(0, x[185])
def l266_155(x):
    # x is a list (or vector) of length 319
    return max(0, x[186])
def l266_156(x):
    # x is a list (or vector) of length 319
    return max(0, x[187])
def l266_157(x):
    # x is a list (or vector) of length 319
    return max(0, x[188])
def l266_158(x):
    # x is a list (or vector) of length 319
    return max(0, x[189])
def l266_159(x):
    # x is a list (or vector) of length 319
    return max(0, x[190])
def l266_160(x):
    # x is a list (or vector) of length 319
    return max(0, x[191])
def l266_161(x):
    # x is a list (or vector) of length 319
    return max(0, x[192])
def l266_162(x):
    # x is a list (or vector) of length 319
    return max(0, x[193])
def l266_163(x):
    # x is a list (or vector) of length 319
    return max(0, x[194])
def l266_164(x):
    # x is a list (or vector) of length 319
    return max(0, x[195])
def l266_165(x):
    # x is a list (or vector) of length 319
    return max(0, x[196])
def l266_166(x):
    # x is a list (or vector) of length 319
    return max(0, x[197])
def l266_167(x):
    # x is a list (or vector) of length 319
    return max(0, x[198])
def l266_168(x):
    # x is a list (or vector) of length 319
    return max(0, x[199])
def l266_169(x):
    # x is a list (or vector) of length 319
    return max(0, x[200])
def l266_170(x):
    # x is a list (or vector) of length 319
    return max(0, x[201])
def l266_171(x):
    # x is a list (or vector) of length 319
    return max(0, x[202])
def l266_172(x):
    # x is a list (or vector) of length 319
    return max(0, x[203])
def l266_173(x):
    # x is a list (or vector) of length 319
    return max(0, x[204])
def l266_174(x):
    # x is a list (or vector) of length 319
    return max(0, x[205])
def l266_175(x):
    # x is a list (or vector) of length 319
    return max(0, x[206])
def l266_176(x):
    # x is a list (or vector) of length 319
    return max(0, x[207])
def l266_177(x):
    # x is a list (or vector) of length 319
    return max(0, x[208])
def l266_178(x):
    # x is a list (or vector) of length 319
    return max(0, x[209])
def l266_179(x):
    # x is a list (or vector) of length 319
    return max(0, x[210])
def l266_180(x):
    # x is a list (or vector) of length 319
    return max(0, x[211])
def l266_181(x):
    # x is a list (or vector) of length 319
    return max(0, x[212])
def l266_182(x):
    # x is a list (or vector) of length 319
    return max(0, x[213])
def l266_183(x):
    # x is a list (or vector) of length 319
    return max(0, x[214])
def l266_184(x):
    # x is a list (or vector) of length 319
    return max(0, x[215])
def l266_185(x):
    # x is a list (or vector) of length 319
    return max(0, x[216])
def l266_186(x):
    # x is a list (or vector) of length 319
    return max(0, x[217])
def l266_187(x):
    # x is a list (or vector) of length 319
    return max(0, x[218])
def l266_188(x):
    # x is a list (or vector) of length 319
    return max(0, x[219])
def l266_189(x):
    # x is a list (or vector) of length 319
    return max(0, x[220])
def l266_190(x):
    # x is a list (or vector) of length 319
    return max(0, x[221])
def l266_191(x):
    # x is a list (or vector) of length 319
    return max(0, x[222])
def l266_192(x):
    # x is a list (or vector) of length 319
    return max(0, x[223])
def l266_193(x):
    # x is a list (or vector) of length 319
    return max(0, x[224])
def l266_194(x):
    # x is a list (or vector) of length 319
    return max(0, x[225])
def l266_195(x):
    # x is a list (or vector) of length 319
    return max(0, x[226])
def l266_196(x):
    # x is a list (or vector) of length 319
    return max(0, x[227])
def l266_197(x):
    # x is a list (or vector) of length 319
    return max(0, x[228])
def l266_198(x):
    # x is a list (or vector) of length 319
    return max(0, x[229])
def l266_199(x):
    # x is a list (or vector) of length 319
    return max(0, x[230])
def l266_200(x):
    # x is a list (or vector) of length 319
    return max(0, x[231])
def l266_201(x):
    # x is a list (or vector) of length 319
    return max(0, x[232])
def l266_202(x):
    # x is a list (or vector) of length 319
    return max(0, x[233])
def l266_203(x):
    # x is a list (or vector) of length 319
    return max(0, x[234])
def l266_204(x):
    # x is a list (or vector) of length 319
    return max(0, x[235])
def l266_205(x):
    # x is a list (or vector) of length 319
    return max(0, x[236])
def l266_206(x):
    # x is a list (or vector) of length 319
    return max(0, x[237])
def l266_207(x):
    # x is a list (or vector) of length 319
    return max(0, x[238])
def l266_208(x):
    # x is a list (or vector) of length 319
    return max(0, x[239])
def l266_209(x):
    # x is a list (or vector) of length 319
    return max(0, x[240])
def l266_210(x):
    # x is a list (or vector) of length 319
    return max(0, x[241])
def l266_211(x):
    # x is a list (or vector) of length 319
    return max(0, x[242])
def l266_212(x):
    # x is a list (or vector) of length 319
    return max(0, x[243])
def l266_213(x):
    # x is a list (or vector) of length 319
    return max(0, x[244])
def l266_214(x):
    # x is a list (or vector) of length 319
    return max(0, x[245])
def l266_215(x):
    # x is a list (or vector) of length 319
    return max(0, x[246])
def l266_216(x):
    # x is a list (or vector) of length 319
    return max(0, x[247])
def l266_217(x):
    # x is a list (or vector) of length 319
    return max(0, x[248])
def l266_218(x):
    # x is a list (or vector) of length 319
    return max(0, x[249])
def l266_219(x):
    # x is a list (or vector) of length 319
    return max(0, x[250])
def l266_220(x):
    # x is a list (or vector) of length 319
    return max(0, x[251])
def l266_221(x):
    # x is a list (or vector) of length 319
    return max(0, x[252])
def l266_222(x):
    # x is a list (or vector) of length 319
    return max(0, x[253])
def l266_223(x):
    # x is a list (or vector) of length 319
    return max(0, x[254])
def l266_224(x):
    # x is a list (or vector) of length 319
    return max(0, x[255])
def l266_225(x):
    # x is a list (or vector) of length 319
    return max(0, x[256])
def l266_226(x):
    # x is a list (or vector) of length 319
    return max(0, x[257])
def l266_227(x):
    # x is a list (or vector) of length 319
    return max(0, x[258])
def l266_228(x):
    # x is a list (or vector) of length 319
    return max(0, x[259])
def l266_229(x):
    # x is a list (or vector) of length 319
    return max(0, x[260])
def l266_230(x):
    # x is a list (or vector) of length 319
    return max(0, x[261])
def l266_231(x):
    # x is a list (or vector) of length 319
    return max(0, x[262])
def l266_232(x):
    # x is a list (or vector) of length 319
    return max(0, x[263])
def l266_233(x):
    # x is a list (or vector) of length 319
    return max(0, x[264])
def l266_234(x):
    # x is a list (or vector) of length 319
    return max(0, x[265])
def l266_235(x):
    # x is a list (or vector) of length 319
    return max(0, x[266])
def l266_236(x):
    # x is a list (or vector) of length 319
    return max(0, x[267])
def l266_237(x):
    # x is a list (or vector) of length 319
    return max(0, x[268])
def l266_238(x):
    # x is a list (or vector) of length 319
    return max(0, x[269])
def l266_239(x):
    # x is a list (or vector) of length 319
    return max(0, x[270])
def l266_240(x):
    # x is a list (or vector) of length 319
    return max(0, x[271])
def l266_241(x):
    # x is a list (or vector) of length 319
    return max(0, x[272])
def l266_242(x):
    # x is a list (or vector) of length 319
    return max(0, x[273])
def l266_243(x):
    # x is a list (or vector) of length 319
    return max(0, x[274])
def l266_244(x):
    # x is a list (or vector) of length 319
    return max(0, x[275])
def l266_245(x):
    # x is a list (or vector) of length 319
    return max(0, x[276])
def l266_246(x):
    # x is a list (or vector) of length 319
    return max(0, x[277])
def l266_247(x):
    # x is a list (or vector) of length 319
    return max(0, x[278])
def l266_248(x):
    # x is a list (or vector) of length 319
    return max(0, x[279])
def l266_249(x):
    # x is a list (or vector) of length 319
    return max(0, x[280])
def l266_250(x):
    # x is a list (or vector) of length 319
    return max(0, x[281])
def l266_251(x):
    # x is a list (or vector) of length 319
    return max(0, x[282])
def l266_252(x):
    # x is a list (or vector) of length 319
    return max(0, x[283])
def l266_253(x):
    # x is a list (or vector) of length 319
    return max(0, x[284])
def l266_254(x):
    # x is a list (or vector) of length 319
    return max(0, x[285])
def l266_255(x):
    # x is a list (or vector) of length 319
    return max(0, x[286])
def l266_256(x):
    # x is a list (or vector) of length 319
    return max(0, x[287])
def l266_257(x):
    # x is a list (or vector) of length 319
    return max(0, x[288])
def l266_258(x):
    # x is a list (or vector) of length 319
    return max(0, x[289])
def l266_259(x):
    # x is a list (or vector) of length 319
    return max(0, x[290])
def l266_260(x):
    # x is a list (or vector) of length 319
    return max(0, x[291])
def l266_261(x):
    # x is a list (or vector) of length 319
    return max(0, x[292])
def l266_262(x):
    # x is a list (or vector) of length 319
    return max(0, x[293])
def l266_263(x):
    # x is a list (or vector) of length 319
    return max(0, x[294])
def l266_264(x):
    # x is a list (or vector) of length 319
    return max(0, x[295])
def l266_265(x):
    # x is a list (or vector) of length 319
    return max(0, x[296])
def l266_266(x):
    # x is a list (or vector) of length 319
    return max(0, x[297])
def l266_267(x):
    # x is a list (or vector) of length 319
    return max(0, x[298])
def l266_268(x):
    # x is a list (or vector) of length 319
    return max(0, x[299])
def l266_269(x):
    # x is a list (or vector) of length 319
    return max(0, x[300])
def l266_270(x):
    # x is a list (or vector) of length 319
    return max(0, x[301])
def l266_271(x):
    # x is a list (or vector) of length 319
    return max(0, x[302])
def l266_272(x):
    # x is a list (or vector) of length 319
    return max(0, x[303])
def l266_273(x):
    # x is a list (or vector) of length 319
    return max(0, x[304])
def l266_274(x):
    # x is a list (or vector) of length 319
    return max(0, x[305])
def l266_275(x):
    # x is a list (or vector) of length 319
    return max(0, x[306])
def l266_276(x):
    # x is a list (or vector) of length 319
    return max(0, x[307])
def l266_277(x):
    # x is a list (or vector) of length 319
    return max(0, x[308])
def l266_278(x):
    # x is a list (or vector) of length 319
    return max(0, x[309])
def l266_279(x):
    # x is a list (or vector) of length 319
    return max(0, x[310])
def l266_280(x):
    # x is a list (or vector) of length 319
    return max(0, x[311])
def l266_281(x):
    # x is a list (or vector) of length 319
    return max(0, x[312])
def l266_282(x):
    # x is a list (or vector) of length 319
    return max(0, x[313])
def l266_283(x):
    # x is a list (or vector) of length 319
    return max(0, x[314])
def l266_284(x):
    # x is a list (or vector) of length 319
    return max(0, x[315])
def l266_285(x):
    # x is a list (or vector) of length 319
    return max(0, x[316])
def l266_286(x):
    # x is a list (or vector) of length 319
    return max(0, x[317])
def l266_287(x):
    # x is a list (or vector) of length 319
    return max(0, x[318])
def l266_(x):
    # x is a list (or vector) of length 319
    return [
        l266_0(x),
        l266_1(x),
        l266_2(x),
        l266_3(x),
        l266_4(x),
        l266_5(x),
        l266_6(x),
        l266_7(x),
        l266_8(x),
        l266_9(x),
        l266_10(x),
        l266_11(x),
        l266_12(x),
        l266_13(x),
        l266_14(x),
        l266_15(x),
        l266_16(x),
        l266_17(x),
        l266_18(x),
        l266_19(x),
        l266_20(x),
        l266_21(x),
        l266_22(x),
        l266_23(x),
        l266_24(x),
        l266_25(x),
        l266_26(x),
        l266_27(x),
        l266_28(x),
        l266_29(x),
        l266_30(x),
        l266_31(x),
        l266_32(x),
        l266_33(x),
        l266_34(x),
        l266_35(x),
        l266_36(x),
        l266_37(x),
        l266_38(x),
        l266_39(x),
        l266_40(x),
        l266_41(x),
        l266_42(x),
        l266_43(x),
        l266_44(x),
        l266_45(x),
        l266_46(x),
        l266_47(x),
        l266_48(x),
        l266_49(x),
        l266_50(x),
        l266_51(x),
        l266_52(x),
        l266_53(x),
        l266_54(x),
        l266_55(x),
        l266_56(x),
        l266_57(x),
        l266_58(x),
        l266_59(x),
        l266_60(x),
        l266_61(x),
        l266_62(x),
        l266_63(x),
        l266_64(x),
        l266_65(x),
        l266_66(x),
        l266_67(x),
        l266_68(x),
        l266_69(x),
        l266_70(x),
        l266_71(x),
        l266_72(x),
        l266_73(x),
        l266_74(x),
        l266_75(x),
        l266_76(x),
        l266_77(x),
        l266_78(x),
        l266_79(x),
        l266_80(x),
        l266_81(x),
        l266_82(x),
        l266_83(x),
        l266_84(x),
        l266_85(x),
        l266_86(x),
        l266_87(x),
        l266_88(x),
        l266_89(x),
        l266_90(x),
        l266_91(x),
        l266_92(x),
        l266_93(x),
        l266_94(x),
        l266_95(x),
        l266_96(x),
        l266_97(x),
        l266_98(x),
        l266_99(x),
        l266_100(x),
        l266_101(x),
        l266_102(x),
        l266_103(x),
        l266_104(x),
        l266_105(x),
        l266_106(x),
        l266_107(x),
        l266_108(x),
        l266_109(x),
        l266_110(x),
        l266_111(x),
        l266_112(x),
        l266_113(x),
        l266_114(x),
        l266_115(x),
        l266_116(x),
        l266_117(x),
        l266_118(x),
        l266_119(x),
        l266_120(x),
        l266_121(x),
        l266_122(x),
        l266_123(x),
        l266_124(x),
        l266_125(x),
        l266_126(x),
        l266_127(x),
        l266_128(x),
        l266_129(x),
        l266_130(x),
        l266_131(x),
        l266_132(x),
        l266_133(x),
        l266_134(x),
        l266_135(x),
        l266_136(x),
        l266_137(x),
        l266_138(x),
        l266_139(x),
        l266_140(x),
        l266_141(x),
        l266_142(x),
        l266_143(x),
        l266_144(x),
        l266_145(x),
        l266_146(x),
        l266_147(x),
        l266_148(x),
        l266_149(x),
        l266_150(x),
        l266_151(x),
        l266_152(x),
        l266_153(x),
        l266_154(x),
        l266_155(x),
        l266_156(x),
        l266_157(x),
        l266_158(x),
        l266_159(x),
        l266_160(x),
        l266_161(x),
        l266_162(x),
        l266_163(x),
        l266_164(x),
        l266_165(x),
        l266_166(x),
        l266_167(x),
        l266_168(x),
        l266_169(x),
        l266_170(x),
        l266_171(x),
        l266_172(x),
        l266_173(x),
        l266_174(x),
        l266_175(x),
        l266_176(x),
        l266_177(x),
        l266_178(x),
        l266_179(x),
        l266_180(x),
        l266_181(x),
        l266_182(x),
        l266_183(x),
        l266_184(x),
        l266_185(x),
        l266_186(x),
        l266_187(x),
        l266_188(x),
        l266_189(x),
        l266_190(x),
        l266_191(x),
        l266_192(x),
        l266_193(x),
        l266_194(x),
        l266_195(x),
        l266_196(x),
        l266_197(x),
        l266_198(x),
        l266_199(x),
        l266_200(x),
        l266_201(x),
        l266_202(x),
        l266_203(x),
        l266_204(x),
        l266_205(x),
        l266_206(x),
        l266_207(x),
        l266_208(x),
        l266_209(x),
        l266_210(x),
        l266_211(x),
        l266_212(x),
        l266_213(x),
        l266_214(x),
        l266_215(x),
        l266_216(x),
        l266_217(x),
        l266_218(x),
        l266_219(x),
        l266_220(x),
        l266_221(x),
        l266_222(x),
        l266_223(x),
        l266_224(x),
        l266_225(x),
        l266_226(x),
        l266_227(x),
        l266_228(x),
        l266_229(x),
        l266_230(x),
        l266_231(x),
        l266_232(x),
        l266_233(x),
        l266_234(x),
        l266_235(x),
        l266_236(x),
        l266_237(x),
        l266_238(x),
        l266_239(x),
        l266_240(x),
        l266_241(x),
        l266_242(x),
        l266_243(x),
        l266_244(x),
        l266_245(x),
        l266_246(x),
        l266_247(x),
        l266_248(x),
        l266_249(x),
        l266_250(x),
        l266_251(x),
        l266_252(x),
        l266_253(x),
        l266_254(x),
        l266_255(x),
        l266_256(x),
        l266_257(x),
        l266_258(x),
        l266_259(x),
        l266_260(x),
        l266_261(x),
        l266_262(x),
        l266_263(x),
        l266_264(x),
        l266_265(x),
        l266_266(x),
        l266_267(x),
        l266_268(x),
        l266_269(x),
        l266_270(x),
        l266_271(x),
        l266_272(x),
        l266_273(x),
        l266_274(x),
        l266_275(x),
        l266_276(x),
        l266_277(x),
        l266_278(x),
        l266_279(x),
        l266_280(x),
        l266_281(x),
        l266_282(x),
        l266_283(x),
        l266_284(x),
        l266_285(x),
        l266_286(x),
        l266_287(x),
    ]