import numpy as np




# Generated from reverse engineering
def l240_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 288
    out = np.empty(288, dtype=np.float32)
    
    # for i in range(0, 97):
    for i in range(0, 97):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x7fffffff (len=31)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(97, 128):
    for i in range(0, 31):
        s = -1 * x[97 + i] + -1 * x[128 + i]
        s += biases[i]
        out[97 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 129):
    for i in range(0, 1):
        s = x[190 + i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(129, 160):
    for i in range(0, 31):
        s = x[159 + i]
        out[129 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 288):
    for i in range(0, 128):
        s = x[191 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l240_0(x):
    # x is a list (or vector) of length 319
    return max(0, x[0])
def l240_1(x):
    # x is a list (or vector) of length 319
    return max(0, x[1])
def l240_2(x):
    # x is a list (or vector) of length 319
    return max(0, x[2])
def l240_3(x):
    # x is a list (or vector) of length 319
    return max(0, x[3])
def l240_4(x):
    # x is a list (or vector) of length 319
    return max(0, x[4])
def l240_5(x):
    # x is a list (or vector) of length 319
    return max(0, x[5])
def l240_6(x):
    # x is a list (or vector) of length 319
    return max(0, x[6])
def l240_7(x):
    # x is a list (or vector) of length 319
    return max(0, x[7])
def l240_8(x):
    # x is a list (or vector) of length 319
    return max(0, x[8])
def l240_9(x):
    # x is a list (or vector) of length 319
    return max(0, x[9])
def l240_10(x):
    # x is a list (or vector) of length 319
    return max(0, x[10])
def l240_11(x):
    # x is a list (or vector) of length 319
    return max(0, x[11])
def l240_12(x):
    # x is a list (or vector) of length 319
    return max(0, x[12])
def l240_13(x):
    # x is a list (or vector) of length 319
    return max(0, x[13])
def l240_14(x):
    # x is a list (or vector) of length 319
    return max(0, x[14])
def l240_15(x):
    # x is a list (or vector) of length 319
    return max(0, x[15])
def l240_16(x):
    # x is a list (or vector) of length 319
    return max(0, x[16])
def l240_17(x):
    # x is a list (or vector) of length 319
    return max(0, x[17])
def l240_18(x):
    # x is a list (or vector) of length 319
    return max(0, x[18])
def l240_19(x):
    # x is a list (or vector) of length 319
    return max(0, x[19])
def l240_20(x):
    # x is a list (or vector) of length 319
    return max(0, x[20])
def l240_21(x):
    # x is a list (or vector) of length 319
    return max(0, x[21])
def l240_22(x):
    # x is a list (or vector) of length 319
    return max(0, x[22])
def l240_23(x):
    # x is a list (or vector) of length 319
    return max(0, x[23])
def l240_24(x):
    # x is a list (or vector) of length 319
    return max(0, x[24])
def l240_25(x):
    # x is a list (or vector) of length 319
    return max(0, x[25])
def l240_26(x):
    # x is a list (or vector) of length 319
    return max(0, x[26])
def l240_27(x):
    # x is a list (or vector) of length 319
    return max(0, x[27])
def l240_28(x):
    # x is a list (or vector) of length 319
    return max(0, x[28])
def l240_29(x):
    # x is a list (or vector) of length 319
    return max(0, x[29])
def l240_30(x):
    # x is a list (or vector) of length 319
    return max(0, x[30])
def l240_31(x):
    # x is a list (or vector) of length 319
    return max(0, x[31])
def l240_32(x):
    # x is a list (or vector) of length 319
    return max(0, x[32])
def l240_33(x):
    # x is a list (or vector) of length 319
    return max(0, x[33])
def l240_34(x):
    # x is a list (or vector) of length 319
    return max(0, x[34])
def l240_35(x):
    # x is a list (or vector) of length 319
    return max(0, x[35])
def l240_36(x):
    # x is a list (or vector) of length 319
    return max(0, x[36])
def l240_37(x):
    # x is a list (or vector) of length 319
    return max(0, x[37])
def l240_38(x):
    # x is a list (or vector) of length 319
    return max(0, x[38])
def l240_39(x):
    # x is a list (or vector) of length 319
    return max(0, x[39])
def l240_40(x):
    # x is a list (or vector) of length 319
    return max(0, x[40])
def l240_41(x):
    # x is a list (or vector) of length 319
    return max(0, x[41])
def l240_42(x):
    # x is a list (or vector) of length 319
    return max(0, x[42])
def l240_43(x):
    # x is a list (or vector) of length 319
    return max(0, x[43])
def l240_44(x):
    # x is a list (or vector) of length 319
    return max(0, x[44])
def l240_45(x):
    # x is a list (or vector) of length 319
    return max(0, x[45])
def l240_46(x):
    # x is a list (or vector) of length 319
    return max(0, x[46])
def l240_47(x):
    # x is a list (or vector) of length 319
    return max(0, x[47])
def l240_48(x):
    # x is a list (or vector) of length 319
    return max(0, x[48])
def l240_49(x):
    # x is a list (or vector) of length 319
    return max(0, x[49])
def l240_50(x):
    # x is a list (or vector) of length 319
    return max(0, x[50])
def l240_51(x):
    # x is a list (or vector) of length 319
    return max(0, x[51])
def l240_52(x):
    # x is a list (or vector) of length 319
    return max(0, x[52])
def l240_53(x):
    # x is a list (or vector) of length 319
    return max(0, x[53])
def l240_54(x):
    # x is a list (or vector) of length 319
    return max(0, x[54])
def l240_55(x):
    # x is a list (or vector) of length 319
    return max(0, x[55])
def l240_56(x):
    # x is a list (or vector) of length 319
    return max(0, x[56])
def l240_57(x):
    # x is a list (or vector) of length 319
    return max(0, x[57])
def l240_58(x):
    # x is a list (or vector) of length 319
    return max(0, x[58])
def l240_59(x):
    # x is a list (or vector) of length 319
    return max(0, x[59])
def l240_60(x):
    # x is a list (or vector) of length 319
    return max(0, x[60])
def l240_61(x):
    # x is a list (or vector) of length 319
    return max(0, x[61])
def l240_62(x):
    # x is a list (or vector) of length 319
    return max(0, x[62])
def l240_63(x):
    # x is a list (or vector) of length 319
    return max(0, x[63])
def l240_64(x):
    # x is a list (or vector) of length 319
    return max(0, x[64])
def l240_65(x):
    # x is a list (or vector) of length 319
    return max(0, x[65])
def l240_66(x):
    # x is a list (or vector) of length 319
    return max(0, x[66])
def l240_67(x):
    # x is a list (or vector) of length 319
    return max(0, x[67])
def l240_68(x):
    # x is a list (or vector) of length 319
    return max(0, x[68])
def l240_69(x):
    # x is a list (or vector) of length 319
    return max(0, x[69])
def l240_70(x):
    # x is a list (or vector) of length 319
    return max(0, x[70])
def l240_71(x):
    # x is a list (or vector) of length 319
    return max(0, x[71])
def l240_72(x):
    # x is a list (or vector) of length 319
    return max(0, x[72])
def l240_73(x):
    # x is a list (or vector) of length 319
    return max(0, x[73])
def l240_74(x):
    # x is a list (or vector) of length 319
    return max(0, x[74])
def l240_75(x):
    # x is a list (or vector) of length 319
    return max(0, x[75])
def l240_76(x):
    # x is a list (or vector) of length 319
    return max(0, x[76])
def l240_77(x):
    # x is a list (or vector) of length 319
    return max(0, x[77])
def l240_78(x):
    # x is a list (or vector) of length 319
    return max(0, x[78])
def l240_79(x):
    # x is a list (or vector) of length 319
    return max(0, x[79])
def l240_80(x):
    # x is a list (or vector) of length 319
    return max(0, x[80])
def l240_81(x):
    # x is a list (or vector) of length 319
    return max(0, x[81])
def l240_82(x):
    # x is a list (or vector) of length 319
    return max(0, x[82])
def l240_83(x):
    # x is a list (or vector) of length 319
    return max(0, x[83])
def l240_84(x):
    # x is a list (or vector) of length 319
    return max(0, x[84])
def l240_85(x):
    # x is a list (or vector) of length 319
    return max(0, x[85])
def l240_86(x):
    # x is a list (or vector) of length 319
    return max(0, x[86])
def l240_87(x):
    # x is a list (or vector) of length 319
    return max(0, x[87])
def l240_88(x):
    # x is a list (or vector) of length 319
    return max(0, x[88])
def l240_89(x):
    # x is a list (or vector) of length 319
    return max(0, x[89])
def l240_90(x):
    # x is a list (or vector) of length 319
    return max(0, x[90])
def l240_91(x):
    # x is a list (or vector) of length 319
    return max(0, x[91])
def l240_92(x):
    # x is a list (or vector) of length 319
    return max(0, x[92])
def l240_93(x):
    # x is a list (or vector) of length 319
    return max(0, x[93])
def l240_94(x):
    # x is a list (or vector) of length 319
    return max(0, x[94])
def l240_95(x):
    # x is a list (or vector) of length 319
    return max(0, x[95])
def l240_96(x):
    # x is a list (or vector) of length 319
    return max(0, x[96])
def l240_97(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[97] + -1.0*x[128] + 1.0)
def l240_98(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[98] + -1.0*x[129] + 1.0)
def l240_99(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[99] + -1.0*x[130] + 1.0)
def l240_100(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[100] + -1.0*x[131] + 1.0)
def l240_101(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[101] + -1.0*x[132] + 1.0)
def l240_102(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[102] + -1.0*x[133] + 1.0)
def l240_103(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[103] + -1.0*x[134] + 1.0)
def l240_104(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[104] + -1.0*x[135] + 1.0)
def l240_105(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[105] + -1.0*x[136] + 1.0)
def l240_106(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[106] + -1.0*x[137] + 1.0)
def l240_107(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[107] + -1.0*x[138] + 1.0)
def l240_108(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[108] + -1.0*x[139] + 1.0)
def l240_109(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[109] + -1.0*x[140] + 1.0)
def l240_110(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[110] + -1.0*x[141] + 1.0)
def l240_111(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[111] + -1.0*x[142] + 1.0)
def l240_112(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[112] + -1.0*x[143] + 1.0)
def l240_113(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[113] + -1.0*x[144] + 1.0)
def l240_114(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[114] + -1.0*x[145] + 1.0)
def l240_115(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[115] + -1.0*x[146] + 1.0)
def l240_116(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[116] + -1.0*x[147] + 1.0)
def l240_117(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[117] + -1.0*x[148] + 1.0)
def l240_118(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[118] + -1.0*x[149] + 1.0)
def l240_119(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[119] + -1.0*x[150] + 1.0)
def l240_120(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[120] + -1.0*x[151] + 1.0)
def l240_121(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[121] + -1.0*x[152] + 1.0)
def l240_122(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[122] + -1.0*x[153] + 1.0)
def l240_123(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[123] + -1.0*x[154] + 1.0)
def l240_124(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[124] + -1.0*x[155] + 1.0)
def l240_125(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[125] + -1.0*x[156] + 1.0)
def l240_126(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[126] + -1.0*x[157] + 1.0)
def l240_127(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[127] + -1.0*x[158] + 1.0)
def l240_128(x):
    # x is a list (or vector) of length 319
    return max(0, x[190])
def l240_129(x):
    # x is a list (or vector) of length 319
    return max(0, x[159])
def l240_130(x):
    # x is a list (or vector) of length 319
    return max(0, x[160])
def l240_131(x):
    # x is a list (or vector) of length 319
    return max(0, x[161])
def l240_132(x):
    # x is a list (or vector) of length 319
    return max(0, x[162])
def l240_133(x):
    # x is a list (or vector) of length 319
    return max(0, x[163])
def l240_134(x):
    # x is a list (or vector) of length 319
    return max(0, x[164])
def l240_135(x):
    # x is a list (or vector) of length 319
    return max(0, x[165])
def l240_136(x):
    # x is a list (or vector) of length 319
    return max(0, x[166])
def l240_137(x):
    # x is a list (or vector) of length 319
    return max(0, x[167])
def l240_138(x):
    # x is a list (or vector) of length 319
    return max(0, x[168])
def l240_139(x):
    # x is a list (or vector) of length 319
    return max(0, x[169])
def l240_140(x):
    # x is a list (or vector) of length 319
    return max(0, x[170])
def l240_141(x):
    # x is a list (or vector) of length 319
    return max(0, x[171])
def l240_142(x):
    # x is a list (or vector) of length 319
    return max(0, x[172])
def l240_143(x):
    # x is a list (or vector) of length 319
    return max(0, x[173])
def l240_144(x):
    # x is a list (or vector) of length 319
    return max(0, x[174])
def l240_145(x):
    # x is a list (or vector) of length 319
    return max(0, x[175])
def l240_146(x):
    # x is a list (or vector) of length 319
    return max(0, x[176])
def l240_147(x):
    # x is a list (or vector) of length 319
    return max(0, x[177])
def l240_148(x):
    # x is a list (or vector) of length 319
    return max(0, x[178])
def l240_149(x):
    # x is a list (or vector) of length 319
    return max(0, x[179])
def l240_150(x):
    # x is a list (or vector) of length 319
    return max(0, x[180])
def l240_151(x):
    # x is a list (or vector) of length 319
    return max(0, x[181])
def l240_152(x):
    # x is a list (or vector) of length 319
    return max(0, x[182])
def l240_153(x):
    # x is a list (or vector) of length 319
    return max(0, x[183])
def l240_154(x):
    # x is a list (or vector) of length 319
    return max(0, x[184])
def l240_155(x):
    # x is a list (or vector) of length 319
    return max(0, x[185])
def l240_156(x):
    # x is a list (or vector) of length 319
    return max(0, x[186])
def l240_157(x):
    # x is a list (or vector) of length 319
    return max(0, x[187])
def l240_158(x):
    # x is a list (or vector) of length 319
    return max(0, x[188])
def l240_159(x):
    # x is a list (or vector) of length 319
    return max(0, x[189])
def l240_160(x):
    # x is a list (or vector) of length 319
    return max(0, x[191])
def l240_161(x):
    # x is a list (or vector) of length 319
    return max(0, x[192])
def l240_162(x):
    # x is a list (or vector) of length 319
    return max(0, x[193])
def l240_163(x):
    # x is a list (or vector) of length 319
    return max(0, x[194])
def l240_164(x):
    # x is a list (or vector) of length 319
    return max(0, x[195])
def l240_165(x):
    # x is a list (or vector) of length 319
    return max(0, x[196])
def l240_166(x):
    # x is a list (or vector) of length 319
    return max(0, x[197])
def l240_167(x):
    # x is a list (or vector) of length 319
    return max(0, x[198])
def l240_168(x):
    # x is a list (or vector) of length 319
    return max(0, x[199])
def l240_169(x):
    # x is a list (or vector) of length 319
    return max(0, x[200])
def l240_170(x):
    # x is a list (or vector) of length 319
    return max(0, x[201])
def l240_171(x):
    # x is a list (or vector) of length 319
    return max(0, x[202])
def l240_172(x):
    # x is a list (or vector) of length 319
    return max(0, x[203])
def l240_173(x):
    # x is a list (or vector) of length 319
    return max(0, x[204])
def l240_174(x):
    # x is a list (or vector) of length 319
    return max(0, x[205])
def l240_175(x):
    # x is a list (or vector) of length 319
    return max(0, x[206])
def l240_176(x):
    # x is a list (or vector) of length 319
    return max(0, x[207])
def l240_177(x):
    # x is a list (or vector) of length 319
    return max(0, x[208])
def l240_178(x):
    # x is a list (or vector) of length 319
    return max(0, x[209])
def l240_179(x):
    # x is a list (or vector) of length 319
    return max(0, x[210])
def l240_180(x):
    # x is a list (or vector) of length 319
    return max(0, x[211])
def l240_181(x):
    # x is a list (or vector) of length 319
    return max(0, x[212])
def l240_182(x):
    # x is a list (or vector) of length 319
    return max(0, x[213])
def l240_183(x):
    # x is a list (or vector) of length 319
    return max(0, x[214])
def l240_184(x):
    # x is a list (or vector) of length 319
    return max(0, x[215])
def l240_185(x):
    # x is a list (or vector) of length 319
    return max(0, x[216])
def l240_186(x):
    # x is a list (or vector) of length 319
    return max(0, x[217])
def l240_187(x):
    # x is a list (or vector) of length 319
    return max(0, x[218])
def l240_188(x):
    # x is a list (or vector) of length 319
    return max(0, x[219])
def l240_189(x):
    # x is a list (or vector) of length 319
    return max(0, x[220])
def l240_190(x):
    # x is a list (or vector) of length 319
    return max(0, x[221])
def l240_191(x):
    # x is a list (or vector) of length 319
    return max(0, x[222])
def l240_192(x):
    # x is a list (or vector) of length 319
    return max(0, x[223])
def l240_193(x):
    # x is a list (or vector) of length 319
    return max(0, x[224])
def l240_194(x):
    # x is a list (or vector) of length 319
    return max(0, x[225])
def l240_195(x):
    # x is a list (or vector) of length 319
    return max(0, x[226])
def l240_196(x):
    # x is a list (or vector) of length 319
    return max(0, x[227])
def l240_197(x):
    # x is a list (or vector) of length 319
    return max(0, x[228])
def l240_198(x):
    # x is a list (or vector) of length 319
    return max(0, x[229])
def l240_199(x):
    # x is a list (or vector) of length 319
    return max(0, x[230])
def l240_200(x):
    # x is a list (or vector) of length 319
    return max(0, x[231])
def l240_201(x):
    # x is a list (or vector) of length 319
    return max(0, x[232])
def l240_202(x):
    # x is a list (or vector) of length 319
    return max(0, x[233])
def l240_203(x):
    # x is a list (or vector) of length 319
    return max(0, x[234])
def l240_204(x):
    # x is a list (or vector) of length 319
    return max(0, x[235])
def l240_205(x):
    # x is a list (or vector) of length 319
    return max(0, x[236])
def l240_206(x):
    # x is a list (or vector) of length 319
    return max(0, x[237])
def l240_207(x):
    # x is a list (or vector) of length 319
    return max(0, x[238])
def l240_208(x):
    # x is a list (or vector) of length 319
    return max(0, x[239])
def l240_209(x):
    # x is a list (or vector) of length 319
    return max(0, x[240])
def l240_210(x):
    # x is a list (or vector) of length 319
    return max(0, x[241])
def l240_211(x):
    # x is a list (or vector) of length 319
    return max(0, x[242])
def l240_212(x):
    # x is a list (or vector) of length 319
    return max(0, x[243])
def l240_213(x):
    # x is a list (or vector) of length 319
    return max(0, x[244])
def l240_214(x):
    # x is a list (or vector) of length 319
    return max(0, x[245])
def l240_215(x):
    # x is a list (or vector) of length 319
    return max(0, x[246])
def l240_216(x):
    # x is a list (or vector) of length 319
    return max(0, x[247])
def l240_217(x):
    # x is a list (or vector) of length 319
    return max(0, x[248])
def l240_218(x):
    # x is a list (or vector) of length 319
    return max(0, x[249])
def l240_219(x):
    # x is a list (or vector) of length 319
    return max(0, x[250])
def l240_220(x):
    # x is a list (or vector) of length 319
    return max(0, x[251])
def l240_221(x):
    # x is a list (or vector) of length 319
    return max(0, x[252])
def l240_222(x):
    # x is a list (or vector) of length 319
    return max(0, x[253])
def l240_223(x):
    # x is a list (or vector) of length 319
    return max(0, x[254])
def l240_224(x):
    # x is a list (or vector) of length 319
    return max(0, x[255])
def l240_225(x):
    # x is a list (or vector) of length 319
    return max(0, x[256])
def l240_226(x):
    # x is a list (or vector) of length 319
    return max(0, x[257])
def l240_227(x):
    # x is a list (or vector) of length 319
    return max(0, x[258])
def l240_228(x):
    # x is a list (or vector) of length 319
    return max(0, x[259])
def l240_229(x):
    # x is a list (or vector) of length 319
    return max(0, x[260])
def l240_230(x):
    # x is a list (or vector) of length 319
    return max(0, x[261])
def l240_231(x):
    # x is a list (or vector) of length 319
    return max(0, x[262])
def l240_232(x):
    # x is a list (or vector) of length 319
    return max(0, x[263])
def l240_233(x):
    # x is a list (or vector) of length 319
    return max(0, x[264])
def l240_234(x):
    # x is a list (or vector) of length 319
    return max(0, x[265])
def l240_235(x):
    # x is a list (or vector) of length 319
    return max(0, x[266])
def l240_236(x):
    # x is a list (or vector) of length 319
    return max(0, x[267])
def l240_237(x):
    # x is a list (or vector) of length 319
    return max(0, x[268])
def l240_238(x):
    # x is a list (or vector) of length 319
    return max(0, x[269])
def l240_239(x):
    # x is a list (or vector) of length 319
    return max(0, x[270])
def l240_240(x):
    # x is a list (or vector) of length 319
    return max(0, x[271])
def l240_241(x):
    # x is a list (or vector) of length 319
    return max(0, x[272])
def l240_242(x):
    # x is a list (or vector) of length 319
    return max(0, x[273])
def l240_243(x):
    # x is a list (or vector) of length 319
    return max(0, x[274])
def l240_244(x):
    # x is a list (or vector) of length 319
    return max(0, x[275])
def l240_245(x):
    # x is a list (or vector) of length 319
    return max(0, x[276])
def l240_246(x):
    # x is a list (or vector) of length 319
    return max(0, x[277])
def l240_247(x):
    # x is a list (or vector) of length 319
    return max(0, x[278])
def l240_248(x):
    # x is a list (or vector) of length 319
    return max(0, x[279])
def l240_249(x):
    # x is a list (or vector) of length 319
    return max(0, x[280])
def l240_250(x):
    # x is a list (or vector) of length 319
    return max(0, x[281])
def l240_251(x):
    # x is a list (or vector) of length 319
    return max(0, x[282])
def l240_252(x):
    # x is a list (or vector) of length 319
    return max(0, x[283])
def l240_253(x):
    # x is a list (or vector) of length 319
    return max(0, x[284])
def l240_254(x):
    # x is a list (or vector) of length 319
    return max(0, x[285])
def l240_255(x):
    # x is a list (or vector) of length 319
    return max(0, x[286])
def l240_256(x):
    # x is a list (or vector) of length 319
    return max(0, x[287])
def l240_257(x):
    # x is a list (or vector) of length 319
    return max(0, x[288])
def l240_258(x):
    # x is a list (or vector) of length 319
    return max(0, x[289])
def l240_259(x):
    # x is a list (or vector) of length 319
    return max(0, x[290])
def l240_260(x):
    # x is a list (or vector) of length 319
    return max(0, x[291])
def l240_261(x):
    # x is a list (or vector) of length 319
    return max(0, x[292])
def l240_262(x):
    # x is a list (or vector) of length 319
    return max(0, x[293])
def l240_263(x):
    # x is a list (or vector) of length 319
    return max(0, x[294])
def l240_264(x):
    # x is a list (or vector) of length 319
    return max(0, x[295])
def l240_265(x):
    # x is a list (or vector) of length 319
    return max(0, x[296])
def l240_266(x):
    # x is a list (or vector) of length 319
    return max(0, x[297])
def l240_267(x):
    # x is a list (or vector) of length 319
    return max(0, x[298])
def l240_268(x):
    # x is a list (or vector) of length 319
    return max(0, x[299])
def l240_269(x):
    # x is a list (or vector) of length 319
    return max(0, x[300])
def l240_270(x):
    # x is a list (or vector) of length 319
    return max(0, x[301])
def l240_271(x):
    # x is a list (or vector) of length 319
    return max(0, x[302])
def l240_272(x):
    # x is a list (or vector) of length 319
    return max(0, x[303])
def l240_273(x):
    # x is a list (or vector) of length 319
    return max(0, x[304])
def l240_274(x):
    # x is a list (or vector) of length 319
    return max(0, x[305])
def l240_275(x):
    # x is a list (or vector) of length 319
    return max(0, x[306])
def l240_276(x):
    # x is a list (or vector) of length 319
    return max(0, x[307])
def l240_277(x):
    # x is a list (or vector) of length 319
    return max(0, x[308])
def l240_278(x):
    # x is a list (or vector) of length 319
    return max(0, x[309])
def l240_279(x):
    # x is a list (or vector) of length 319
    return max(0, x[310])
def l240_280(x):
    # x is a list (or vector) of length 319
    return max(0, x[311])
def l240_281(x):
    # x is a list (or vector) of length 319
    return max(0, x[312])
def l240_282(x):
    # x is a list (or vector) of length 319
    return max(0, x[313])
def l240_283(x):
    # x is a list (or vector) of length 319
    return max(0, x[314])
def l240_284(x):
    # x is a list (or vector) of length 319
    return max(0, x[315])
def l240_285(x):
    # x is a list (or vector) of length 319
    return max(0, x[316])
def l240_286(x):
    # x is a list (or vector) of length 319
    return max(0, x[317])
def l240_287(x):
    # x is a list (or vector) of length 319
    return max(0, x[318])
def l240_(x):
    # x is a list (or vector) of length 319
    return [
        l240_0(x),
        l240_1(x),
        l240_2(x),
        l240_3(x),
        l240_4(x),
        l240_5(x),
        l240_6(x),
        l240_7(x),
        l240_8(x),
        l240_9(x),
        l240_10(x),
        l240_11(x),
        l240_12(x),
        l240_13(x),
        l240_14(x),
        l240_15(x),
        l240_16(x),
        l240_17(x),
        l240_18(x),
        l240_19(x),
        l240_20(x),
        l240_21(x),
        l240_22(x),
        l240_23(x),
        l240_24(x),
        l240_25(x),
        l240_26(x),
        l240_27(x),
        l240_28(x),
        l240_29(x),
        l240_30(x),
        l240_31(x),
        l240_32(x),
        l240_33(x),
        l240_34(x),
        l240_35(x),
        l240_36(x),
        l240_37(x),
        l240_38(x),
        l240_39(x),
        l240_40(x),
        l240_41(x),
        l240_42(x),
        l240_43(x),
        l240_44(x),
        l240_45(x),
        l240_46(x),
        l240_47(x),
        l240_48(x),
        l240_49(x),
        l240_50(x),
        l240_51(x),
        l240_52(x),
        l240_53(x),
        l240_54(x),
        l240_55(x),
        l240_56(x),
        l240_57(x),
        l240_58(x),
        l240_59(x),
        l240_60(x),
        l240_61(x),
        l240_62(x),
        l240_63(x),
        l240_64(x),
        l240_65(x),
        l240_66(x),
        l240_67(x),
        l240_68(x),
        l240_69(x),
        l240_70(x),
        l240_71(x),
        l240_72(x),
        l240_73(x),
        l240_74(x),
        l240_75(x),
        l240_76(x),
        l240_77(x),
        l240_78(x),
        l240_79(x),
        l240_80(x),
        l240_81(x),
        l240_82(x),
        l240_83(x),
        l240_84(x),
        l240_85(x),
        l240_86(x),
        l240_87(x),
        l240_88(x),
        l240_89(x),
        l240_90(x),
        l240_91(x),
        l240_92(x),
        l240_93(x),
        l240_94(x),
        l240_95(x),
        l240_96(x),
        l240_97(x),
        l240_98(x),
        l240_99(x),
        l240_100(x),
        l240_101(x),
        l240_102(x),
        l240_103(x),
        l240_104(x),
        l240_105(x),
        l240_106(x),
        l240_107(x),
        l240_108(x),
        l240_109(x),
        l240_110(x),
        l240_111(x),
        l240_112(x),
        l240_113(x),
        l240_114(x),
        l240_115(x),
        l240_116(x),
        l240_117(x),
        l240_118(x),
        l240_119(x),
        l240_120(x),
        l240_121(x),
        l240_122(x),
        l240_123(x),
        l240_124(x),
        l240_125(x),
        l240_126(x),
        l240_127(x),
        l240_128(x),
        l240_129(x),
        l240_130(x),
        l240_131(x),
        l240_132(x),
        l240_133(x),
        l240_134(x),
        l240_135(x),
        l240_136(x),
        l240_137(x),
        l240_138(x),
        l240_139(x),
        l240_140(x),
        l240_141(x),
        l240_142(x),
        l240_143(x),
        l240_144(x),
        l240_145(x),
        l240_146(x),
        l240_147(x),
        l240_148(x),
        l240_149(x),
        l240_150(x),
        l240_151(x),
        l240_152(x),
        l240_153(x),
        l240_154(x),
        l240_155(x),
        l240_156(x),
        l240_157(x),
        l240_158(x),
        l240_159(x),
        l240_160(x),
        l240_161(x),
        l240_162(x),
        l240_163(x),
        l240_164(x),
        l240_165(x),
        l240_166(x),
        l240_167(x),
        l240_168(x),
        l240_169(x),
        l240_170(x),
        l240_171(x),
        l240_172(x),
        l240_173(x),
        l240_174(x),
        l240_175(x),
        l240_176(x),
        l240_177(x),
        l240_178(x),
        l240_179(x),
        l240_180(x),
        l240_181(x),
        l240_182(x),
        l240_183(x),
        l240_184(x),
        l240_185(x),
        l240_186(x),
        l240_187(x),
        l240_188(x),
        l240_189(x),
        l240_190(x),
        l240_191(x),
        l240_192(x),
        l240_193(x),
        l240_194(x),
        l240_195(x),
        l240_196(x),
        l240_197(x),
        l240_198(x),
        l240_199(x),
        l240_200(x),
        l240_201(x),
        l240_202(x),
        l240_203(x),
        l240_204(x),
        l240_205(x),
        l240_206(x),
        l240_207(x),
        l240_208(x),
        l240_209(x),
        l240_210(x),
        l240_211(x),
        l240_212(x),
        l240_213(x),
        l240_214(x),
        l240_215(x),
        l240_216(x),
        l240_217(x),
        l240_218(x),
        l240_219(x),
        l240_220(x),
        l240_221(x),
        l240_222(x),
        l240_223(x),
        l240_224(x),
        l240_225(x),
        l240_226(x),
        l240_227(x),
        l240_228(x),
        l240_229(x),
        l240_230(x),
        l240_231(x),
        l240_232(x),
        l240_233(x),
        l240_234(x),
        l240_235(x),
        l240_236(x),
        l240_237(x),
        l240_238(x),
        l240_239(x),
        l240_240(x),
        l240_241(x),
        l240_242(x),
        l240_243(x),
        l240_244(x),
        l240_245(x),
        l240_246(x),
        l240_247(x),
        l240_248(x),
        l240_249(x),
        l240_250(x),
        l240_251(x),
        l240_252(x),
        l240_253(x),
        l240_254(x),
        l240_255(x),
        l240_256(x),
        l240_257(x),
        l240_258(x),
        l240_259(x),
        l240_260(x),
        l240_261(x),
        l240_262(x),
        l240_263(x),
        l240_264(x),
        l240_265(x),
        l240_266(x),
        l240_267(x),
        l240_268(x),
        l240_269(x),
        l240_270(x),
        l240_271(x),
        l240_272(x),
        l240_273(x),
        l240_274(x),
        l240_275(x),
        l240_276(x),
        l240_277(x),
        l240_278(x),
        l240_279(x),
        l240_280(x),
        l240_281(x),
        l240_282(x),
        l240_283(x),
        l240_284(x),
        l240_285(x),
        l240_286(x),
        l240_287(x),
    ]