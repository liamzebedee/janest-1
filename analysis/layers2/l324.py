import numpy as np




# Generated from reverse engineering
def l324_g(x: np.ndarray) -> np.ndarray:
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




def l324_0(x):
    # x is a list (or vector) of length 319
    return max(0, x[0])
def l324_1(x):
    # x is a list (or vector) of length 319
    return max(0, x[1])
def l324_2(x):
    # x is a list (or vector) of length 319
    return max(0, x[2])
def l324_3(x):
    # x is a list (or vector) of length 319
    return max(0, x[3])
def l324_4(x):
    # x is a list (or vector) of length 319
    return max(0, x[4])
def l324_5(x):
    # x is a list (or vector) of length 319
    return max(0, x[5])
def l324_6(x):
    # x is a list (or vector) of length 319
    return max(0, x[6])
def l324_7(x):
    # x is a list (or vector) of length 319
    return max(0, x[7])
def l324_8(x):
    # x is a list (or vector) of length 319
    return max(0, x[8])
def l324_9(x):
    # x is a list (or vector) of length 319
    return max(0, x[9])
def l324_10(x):
    # x is a list (or vector) of length 319
    return max(0, x[10])
def l324_11(x):
    # x is a list (or vector) of length 319
    return max(0, x[11])
def l324_12(x):
    # x is a list (or vector) of length 319
    return max(0, x[12])
def l324_13(x):
    # x is a list (or vector) of length 319
    return max(0, x[13])
def l324_14(x):
    # x is a list (or vector) of length 319
    return max(0, x[14])
def l324_15(x):
    # x is a list (or vector) of length 319
    return max(0, x[15])
def l324_16(x):
    # x is a list (or vector) of length 319
    return max(0, x[16])
def l324_17(x):
    # x is a list (or vector) of length 319
    return max(0, x[17])
def l324_18(x):
    # x is a list (or vector) of length 319
    return max(0, x[18])
def l324_19(x):
    # x is a list (or vector) of length 319
    return max(0, x[19])
def l324_20(x):
    # x is a list (or vector) of length 319
    return max(0, x[20])
def l324_21(x):
    # x is a list (or vector) of length 319
    return max(0, x[21])
def l324_22(x):
    # x is a list (or vector) of length 319
    return max(0, x[22])
def l324_23(x):
    # x is a list (or vector) of length 319
    return max(0, x[23])
def l324_24(x):
    # x is a list (or vector) of length 319
    return max(0, x[24])
def l324_25(x):
    # x is a list (or vector) of length 319
    return max(0, x[25])
def l324_26(x):
    # x is a list (or vector) of length 319
    return max(0, x[26])
def l324_27(x):
    # x is a list (or vector) of length 319
    return max(0, x[27])
def l324_28(x):
    # x is a list (or vector) of length 319
    return max(0, x[28])
def l324_29(x):
    # x is a list (or vector) of length 319
    return max(0, x[29])
def l324_30(x):
    # x is a list (or vector) of length 319
    return max(0, x[30])
def l324_31(x):
    # x is a list (or vector) of length 319
    return max(0, x[31])
def l324_32(x):
    # x is a list (or vector) of length 319
    return max(0, x[32])
def l324_33(x):
    # x is a list (or vector) of length 319
    return max(0, x[33])
def l324_34(x):
    # x is a list (or vector) of length 319
    return max(0, x[34])
def l324_35(x):
    # x is a list (or vector) of length 319
    return max(0, x[35])
def l324_36(x):
    # x is a list (or vector) of length 319
    return max(0, x[36])
def l324_37(x):
    # x is a list (or vector) of length 319
    return max(0, x[37])
def l324_38(x):
    # x is a list (or vector) of length 319
    return max(0, x[38])
def l324_39(x):
    # x is a list (or vector) of length 319
    return max(0, x[39])
def l324_40(x):
    # x is a list (or vector) of length 319
    return max(0, x[40])
def l324_41(x):
    # x is a list (or vector) of length 319
    return max(0, x[41])
def l324_42(x):
    # x is a list (or vector) of length 319
    return max(0, x[42])
def l324_43(x):
    # x is a list (or vector) of length 319
    return max(0, x[43])
def l324_44(x):
    # x is a list (or vector) of length 319
    return max(0, x[44])
def l324_45(x):
    # x is a list (or vector) of length 319
    return max(0, x[45])
def l324_46(x):
    # x is a list (or vector) of length 319
    return max(0, x[46])
def l324_47(x):
    # x is a list (or vector) of length 319
    return max(0, x[47])
def l324_48(x):
    # x is a list (or vector) of length 319
    return max(0, x[48])
def l324_49(x):
    # x is a list (or vector) of length 319
    return max(0, x[49])
def l324_50(x):
    # x is a list (or vector) of length 319
    return max(0, x[50])
def l324_51(x):
    # x is a list (or vector) of length 319
    return max(0, x[51])
def l324_52(x):
    # x is a list (or vector) of length 319
    return max(0, x[52])
def l324_53(x):
    # x is a list (or vector) of length 319
    return max(0, x[53])
def l324_54(x):
    # x is a list (or vector) of length 319
    return max(0, x[54])
def l324_55(x):
    # x is a list (or vector) of length 319
    return max(0, x[55])
def l324_56(x):
    # x is a list (or vector) of length 319
    return max(0, x[56])
def l324_57(x):
    # x is a list (or vector) of length 319
    return max(0, x[57])
def l324_58(x):
    # x is a list (or vector) of length 319
    return max(0, x[58])
def l324_59(x):
    # x is a list (or vector) of length 319
    return max(0, x[59])
def l324_60(x):
    # x is a list (or vector) of length 319
    return max(0, x[60])
def l324_61(x):
    # x is a list (or vector) of length 319
    return max(0, x[61])
def l324_62(x):
    # x is a list (or vector) of length 319
    return max(0, x[62])
def l324_63(x):
    # x is a list (or vector) of length 319
    return max(0, x[63])
def l324_64(x):
    # x is a list (or vector) of length 319
    return max(0, x[64])
def l324_65(x):
    # x is a list (or vector) of length 319
    return max(0, x[65])
def l324_66(x):
    # x is a list (or vector) of length 319
    return max(0, x[66])
def l324_67(x):
    # x is a list (or vector) of length 319
    return max(0, x[67])
def l324_68(x):
    # x is a list (or vector) of length 319
    return max(0, x[68])
def l324_69(x):
    # x is a list (or vector) of length 319
    return max(0, x[69])
def l324_70(x):
    # x is a list (or vector) of length 319
    return max(0, x[70])
def l324_71(x):
    # x is a list (or vector) of length 319
    return max(0, x[71])
def l324_72(x):
    # x is a list (or vector) of length 319
    return max(0, x[72])
def l324_73(x):
    # x is a list (or vector) of length 319
    return max(0, x[73])
def l324_74(x):
    # x is a list (or vector) of length 319
    return max(0, x[74])
def l324_75(x):
    # x is a list (or vector) of length 319
    return max(0, x[75])
def l324_76(x):
    # x is a list (or vector) of length 319
    return max(0, x[76])
def l324_77(x):
    # x is a list (or vector) of length 319
    return max(0, x[77])
def l324_78(x):
    # x is a list (or vector) of length 319
    return max(0, x[78])
def l324_79(x):
    # x is a list (or vector) of length 319
    return max(0, x[79])
def l324_80(x):
    # x is a list (or vector) of length 319
    return max(0, x[80])
def l324_81(x):
    # x is a list (or vector) of length 319
    return max(0, x[81])
def l324_82(x):
    # x is a list (or vector) of length 319
    return max(0, x[82])
def l324_83(x):
    # x is a list (or vector) of length 319
    return max(0, x[83])
def l324_84(x):
    # x is a list (or vector) of length 319
    return max(0, x[84])
def l324_85(x):
    # x is a list (or vector) of length 319
    return max(0, x[85])
def l324_86(x):
    # x is a list (or vector) of length 319
    return max(0, x[86])
def l324_87(x):
    # x is a list (or vector) of length 319
    return max(0, x[87])
def l324_88(x):
    # x is a list (or vector) of length 319
    return max(0, x[88])
def l324_89(x):
    # x is a list (or vector) of length 319
    return max(0, x[89])
def l324_90(x):
    # x is a list (or vector) of length 319
    return max(0, x[90])
def l324_91(x):
    # x is a list (or vector) of length 319
    return max(0, x[91])
def l324_92(x):
    # x is a list (or vector) of length 319
    return max(0, x[92])
def l324_93(x):
    # x is a list (or vector) of length 319
    return max(0, x[93])
def l324_94(x):
    # x is a list (or vector) of length 319
    return max(0, x[94])
def l324_95(x):
    # x is a list (or vector) of length 319
    return max(0, x[95])
def l324_96(x):
    # x is a list (or vector) of length 319
    return max(0, x[96])
def l324_97(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[97] + -1.0*x[128] + 1.0)
def l324_98(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[98] + -1.0*x[129] + 1.0)
def l324_99(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[99] + -1.0*x[130] + 1.0)
def l324_100(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[100] + -1.0*x[131] + 1.0)
def l324_101(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[101] + -1.0*x[132] + 1.0)
def l324_102(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[102] + -1.0*x[133] + 1.0)
def l324_103(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[103] + -1.0*x[134] + 1.0)
def l324_104(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[104] + -1.0*x[135] + 1.0)
def l324_105(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[105] + -1.0*x[136] + 1.0)
def l324_106(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[106] + -1.0*x[137] + 1.0)
def l324_107(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[107] + -1.0*x[138] + 1.0)
def l324_108(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[108] + -1.0*x[139] + 1.0)
def l324_109(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[109] + -1.0*x[140] + 1.0)
def l324_110(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[110] + -1.0*x[141] + 1.0)
def l324_111(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[111] + -1.0*x[142] + 1.0)
def l324_112(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[112] + -1.0*x[143] + 1.0)
def l324_113(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[113] + -1.0*x[144] + 1.0)
def l324_114(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[114] + -1.0*x[145] + 1.0)
def l324_115(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[115] + -1.0*x[146] + 1.0)
def l324_116(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[116] + -1.0*x[147] + 1.0)
def l324_117(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[117] + -1.0*x[148] + 1.0)
def l324_118(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[118] + -1.0*x[149] + 1.0)
def l324_119(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[119] + -1.0*x[150] + 1.0)
def l324_120(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[120] + -1.0*x[151] + 1.0)
def l324_121(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[121] + -1.0*x[152] + 1.0)
def l324_122(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[122] + -1.0*x[153] + 1.0)
def l324_123(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[123] + -1.0*x[154] + 1.0)
def l324_124(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[124] + -1.0*x[155] + 1.0)
def l324_125(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[125] + -1.0*x[156] + 1.0)
def l324_126(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[126] + -1.0*x[157] + 1.0)
def l324_127(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[127] + -1.0*x[158] + 1.0)
def l324_128(x):
    # x is a list (or vector) of length 319
    return max(0, x[190])
def l324_129(x):
    # x is a list (or vector) of length 319
    return max(0, x[159])
def l324_130(x):
    # x is a list (or vector) of length 319
    return max(0, x[160])
def l324_131(x):
    # x is a list (or vector) of length 319
    return max(0, x[161])
def l324_132(x):
    # x is a list (or vector) of length 319
    return max(0, x[162])
def l324_133(x):
    # x is a list (or vector) of length 319
    return max(0, x[163])
def l324_134(x):
    # x is a list (or vector) of length 319
    return max(0, x[164])
def l324_135(x):
    # x is a list (or vector) of length 319
    return max(0, x[165])
def l324_136(x):
    # x is a list (or vector) of length 319
    return max(0, x[166])
def l324_137(x):
    # x is a list (or vector) of length 319
    return max(0, x[167])
def l324_138(x):
    # x is a list (or vector) of length 319
    return max(0, x[168])
def l324_139(x):
    # x is a list (or vector) of length 319
    return max(0, x[169])
def l324_140(x):
    # x is a list (or vector) of length 319
    return max(0, x[170])
def l324_141(x):
    # x is a list (or vector) of length 319
    return max(0, x[171])
def l324_142(x):
    # x is a list (or vector) of length 319
    return max(0, x[172])
def l324_143(x):
    # x is a list (or vector) of length 319
    return max(0, x[173])
def l324_144(x):
    # x is a list (or vector) of length 319
    return max(0, x[174])
def l324_145(x):
    # x is a list (or vector) of length 319
    return max(0, x[175])
def l324_146(x):
    # x is a list (or vector) of length 319
    return max(0, x[176])
def l324_147(x):
    # x is a list (or vector) of length 319
    return max(0, x[177])
def l324_148(x):
    # x is a list (or vector) of length 319
    return max(0, x[178])
def l324_149(x):
    # x is a list (or vector) of length 319
    return max(0, x[179])
def l324_150(x):
    # x is a list (or vector) of length 319
    return max(0, x[180])
def l324_151(x):
    # x is a list (or vector) of length 319
    return max(0, x[181])
def l324_152(x):
    # x is a list (or vector) of length 319
    return max(0, x[182])
def l324_153(x):
    # x is a list (or vector) of length 319
    return max(0, x[183])
def l324_154(x):
    # x is a list (or vector) of length 319
    return max(0, x[184])
def l324_155(x):
    # x is a list (or vector) of length 319
    return max(0, x[185])
def l324_156(x):
    # x is a list (or vector) of length 319
    return max(0, x[186])
def l324_157(x):
    # x is a list (or vector) of length 319
    return max(0, x[187])
def l324_158(x):
    # x is a list (or vector) of length 319
    return max(0, x[188])
def l324_159(x):
    # x is a list (or vector) of length 319
    return max(0, x[189])
def l324_160(x):
    # x is a list (or vector) of length 319
    return max(0, x[191])
def l324_161(x):
    # x is a list (or vector) of length 319
    return max(0, x[192])
def l324_162(x):
    # x is a list (or vector) of length 319
    return max(0, x[193])
def l324_163(x):
    # x is a list (or vector) of length 319
    return max(0, x[194])
def l324_164(x):
    # x is a list (or vector) of length 319
    return max(0, x[195])
def l324_165(x):
    # x is a list (or vector) of length 319
    return max(0, x[196])
def l324_166(x):
    # x is a list (or vector) of length 319
    return max(0, x[197])
def l324_167(x):
    # x is a list (or vector) of length 319
    return max(0, x[198])
def l324_168(x):
    # x is a list (or vector) of length 319
    return max(0, x[199])
def l324_169(x):
    # x is a list (or vector) of length 319
    return max(0, x[200])
def l324_170(x):
    # x is a list (or vector) of length 319
    return max(0, x[201])
def l324_171(x):
    # x is a list (or vector) of length 319
    return max(0, x[202])
def l324_172(x):
    # x is a list (or vector) of length 319
    return max(0, x[203])
def l324_173(x):
    # x is a list (or vector) of length 319
    return max(0, x[204])
def l324_174(x):
    # x is a list (or vector) of length 319
    return max(0, x[205])
def l324_175(x):
    # x is a list (or vector) of length 319
    return max(0, x[206])
def l324_176(x):
    # x is a list (or vector) of length 319
    return max(0, x[207])
def l324_177(x):
    # x is a list (or vector) of length 319
    return max(0, x[208])
def l324_178(x):
    # x is a list (or vector) of length 319
    return max(0, x[209])
def l324_179(x):
    # x is a list (or vector) of length 319
    return max(0, x[210])
def l324_180(x):
    # x is a list (or vector) of length 319
    return max(0, x[211])
def l324_181(x):
    # x is a list (or vector) of length 319
    return max(0, x[212])
def l324_182(x):
    # x is a list (or vector) of length 319
    return max(0, x[213])
def l324_183(x):
    # x is a list (or vector) of length 319
    return max(0, x[214])
def l324_184(x):
    # x is a list (or vector) of length 319
    return max(0, x[215])
def l324_185(x):
    # x is a list (or vector) of length 319
    return max(0, x[216])
def l324_186(x):
    # x is a list (or vector) of length 319
    return max(0, x[217])
def l324_187(x):
    # x is a list (or vector) of length 319
    return max(0, x[218])
def l324_188(x):
    # x is a list (or vector) of length 319
    return max(0, x[219])
def l324_189(x):
    # x is a list (or vector) of length 319
    return max(0, x[220])
def l324_190(x):
    # x is a list (or vector) of length 319
    return max(0, x[221])
def l324_191(x):
    # x is a list (or vector) of length 319
    return max(0, x[222])
def l324_192(x):
    # x is a list (or vector) of length 319
    return max(0, x[223])
def l324_193(x):
    # x is a list (or vector) of length 319
    return max(0, x[224])
def l324_194(x):
    # x is a list (or vector) of length 319
    return max(0, x[225])
def l324_195(x):
    # x is a list (or vector) of length 319
    return max(0, x[226])
def l324_196(x):
    # x is a list (or vector) of length 319
    return max(0, x[227])
def l324_197(x):
    # x is a list (or vector) of length 319
    return max(0, x[228])
def l324_198(x):
    # x is a list (or vector) of length 319
    return max(0, x[229])
def l324_199(x):
    # x is a list (or vector) of length 319
    return max(0, x[230])
def l324_200(x):
    # x is a list (or vector) of length 319
    return max(0, x[231])
def l324_201(x):
    # x is a list (or vector) of length 319
    return max(0, x[232])
def l324_202(x):
    # x is a list (or vector) of length 319
    return max(0, x[233])
def l324_203(x):
    # x is a list (or vector) of length 319
    return max(0, x[234])
def l324_204(x):
    # x is a list (or vector) of length 319
    return max(0, x[235])
def l324_205(x):
    # x is a list (or vector) of length 319
    return max(0, x[236])
def l324_206(x):
    # x is a list (or vector) of length 319
    return max(0, x[237])
def l324_207(x):
    # x is a list (or vector) of length 319
    return max(0, x[238])
def l324_208(x):
    # x is a list (or vector) of length 319
    return max(0, x[239])
def l324_209(x):
    # x is a list (or vector) of length 319
    return max(0, x[240])
def l324_210(x):
    # x is a list (or vector) of length 319
    return max(0, x[241])
def l324_211(x):
    # x is a list (or vector) of length 319
    return max(0, x[242])
def l324_212(x):
    # x is a list (or vector) of length 319
    return max(0, x[243])
def l324_213(x):
    # x is a list (or vector) of length 319
    return max(0, x[244])
def l324_214(x):
    # x is a list (or vector) of length 319
    return max(0, x[245])
def l324_215(x):
    # x is a list (or vector) of length 319
    return max(0, x[246])
def l324_216(x):
    # x is a list (or vector) of length 319
    return max(0, x[247])
def l324_217(x):
    # x is a list (or vector) of length 319
    return max(0, x[248])
def l324_218(x):
    # x is a list (or vector) of length 319
    return max(0, x[249])
def l324_219(x):
    # x is a list (or vector) of length 319
    return max(0, x[250])
def l324_220(x):
    # x is a list (or vector) of length 319
    return max(0, x[251])
def l324_221(x):
    # x is a list (or vector) of length 319
    return max(0, x[252])
def l324_222(x):
    # x is a list (or vector) of length 319
    return max(0, x[253])
def l324_223(x):
    # x is a list (or vector) of length 319
    return max(0, x[254])
def l324_224(x):
    # x is a list (or vector) of length 319
    return max(0, x[255])
def l324_225(x):
    # x is a list (or vector) of length 319
    return max(0, x[256])
def l324_226(x):
    # x is a list (or vector) of length 319
    return max(0, x[257])
def l324_227(x):
    # x is a list (or vector) of length 319
    return max(0, x[258])
def l324_228(x):
    # x is a list (or vector) of length 319
    return max(0, x[259])
def l324_229(x):
    # x is a list (or vector) of length 319
    return max(0, x[260])
def l324_230(x):
    # x is a list (or vector) of length 319
    return max(0, x[261])
def l324_231(x):
    # x is a list (or vector) of length 319
    return max(0, x[262])
def l324_232(x):
    # x is a list (or vector) of length 319
    return max(0, x[263])
def l324_233(x):
    # x is a list (or vector) of length 319
    return max(0, x[264])
def l324_234(x):
    # x is a list (or vector) of length 319
    return max(0, x[265])
def l324_235(x):
    # x is a list (or vector) of length 319
    return max(0, x[266])
def l324_236(x):
    # x is a list (or vector) of length 319
    return max(0, x[267])
def l324_237(x):
    # x is a list (or vector) of length 319
    return max(0, x[268])
def l324_238(x):
    # x is a list (or vector) of length 319
    return max(0, x[269])
def l324_239(x):
    # x is a list (or vector) of length 319
    return max(0, x[270])
def l324_240(x):
    # x is a list (or vector) of length 319
    return max(0, x[271])
def l324_241(x):
    # x is a list (or vector) of length 319
    return max(0, x[272])
def l324_242(x):
    # x is a list (or vector) of length 319
    return max(0, x[273])
def l324_243(x):
    # x is a list (or vector) of length 319
    return max(0, x[274])
def l324_244(x):
    # x is a list (or vector) of length 319
    return max(0, x[275])
def l324_245(x):
    # x is a list (or vector) of length 319
    return max(0, x[276])
def l324_246(x):
    # x is a list (or vector) of length 319
    return max(0, x[277])
def l324_247(x):
    # x is a list (or vector) of length 319
    return max(0, x[278])
def l324_248(x):
    # x is a list (or vector) of length 319
    return max(0, x[279])
def l324_249(x):
    # x is a list (or vector) of length 319
    return max(0, x[280])
def l324_250(x):
    # x is a list (or vector) of length 319
    return max(0, x[281])
def l324_251(x):
    # x is a list (or vector) of length 319
    return max(0, x[282])
def l324_252(x):
    # x is a list (or vector) of length 319
    return max(0, x[283])
def l324_253(x):
    # x is a list (or vector) of length 319
    return max(0, x[284])
def l324_254(x):
    # x is a list (or vector) of length 319
    return max(0, x[285])
def l324_255(x):
    # x is a list (or vector) of length 319
    return max(0, x[286])
def l324_256(x):
    # x is a list (or vector) of length 319
    return max(0, x[287])
def l324_257(x):
    # x is a list (or vector) of length 319
    return max(0, x[288])
def l324_258(x):
    # x is a list (or vector) of length 319
    return max(0, x[289])
def l324_259(x):
    # x is a list (or vector) of length 319
    return max(0, x[290])
def l324_260(x):
    # x is a list (or vector) of length 319
    return max(0, x[291])
def l324_261(x):
    # x is a list (or vector) of length 319
    return max(0, x[292])
def l324_262(x):
    # x is a list (or vector) of length 319
    return max(0, x[293])
def l324_263(x):
    # x is a list (or vector) of length 319
    return max(0, x[294])
def l324_264(x):
    # x is a list (or vector) of length 319
    return max(0, x[295])
def l324_265(x):
    # x is a list (or vector) of length 319
    return max(0, x[296])
def l324_266(x):
    # x is a list (or vector) of length 319
    return max(0, x[297])
def l324_267(x):
    # x is a list (or vector) of length 319
    return max(0, x[298])
def l324_268(x):
    # x is a list (or vector) of length 319
    return max(0, x[299])
def l324_269(x):
    # x is a list (or vector) of length 319
    return max(0, x[300])
def l324_270(x):
    # x is a list (or vector) of length 319
    return max(0, x[301])
def l324_271(x):
    # x is a list (or vector) of length 319
    return max(0, x[302])
def l324_272(x):
    # x is a list (or vector) of length 319
    return max(0, x[303])
def l324_273(x):
    # x is a list (or vector) of length 319
    return max(0, x[304])
def l324_274(x):
    # x is a list (or vector) of length 319
    return max(0, x[305])
def l324_275(x):
    # x is a list (or vector) of length 319
    return max(0, x[306])
def l324_276(x):
    # x is a list (or vector) of length 319
    return max(0, x[307])
def l324_277(x):
    # x is a list (or vector) of length 319
    return max(0, x[308])
def l324_278(x):
    # x is a list (or vector) of length 319
    return max(0, x[309])
def l324_279(x):
    # x is a list (or vector) of length 319
    return max(0, x[310])
def l324_280(x):
    # x is a list (or vector) of length 319
    return max(0, x[311])
def l324_281(x):
    # x is a list (or vector) of length 319
    return max(0, x[312])
def l324_282(x):
    # x is a list (or vector) of length 319
    return max(0, x[313])
def l324_283(x):
    # x is a list (or vector) of length 319
    return max(0, x[314])
def l324_284(x):
    # x is a list (or vector) of length 319
    return max(0, x[315])
def l324_285(x):
    # x is a list (or vector) of length 319
    return max(0, x[316])
def l324_286(x):
    # x is a list (or vector) of length 319
    return max(0, x[317])
def l324_287(x):
    # x is a list (or vector) of length 319
    return max(0, x[318])
def l324_(x):
    # x is a list (or vector) of length 319
    return [
        l324_0(x),
        l324_1(x),
        l324_2(x),
        l324_3(x),
        l324_4(x),
        l324_5(x),
        l324_6(x),
        l324_7(x),
        l324_8(x),
        l324_9(x),
        l324_10(x),
        l324_11(x),
        l324_12(x),
        l324_13(x),
        l324_14(x),
        l324_15(x),
        l324_16(x),
        l324_17(x),
        l324_18(x),
        l324_19(x),
        l324_20(x),
        l324_21(x),
        l324_22(x),
        l324_23(x),
        l324_24(x),
        l324_25(x),
        l324_26(x),
        l324_27(x),
        l324_28(x),
        l324_29(x),
        l324_30(x),
        l324_31(x),
        l324_32(x),
        l324_33(x),
        l324_34(x),
        l324_35(x),
        l324_36(x),
        l324_37(x),
        l324_38(x),
        l324_39(x),
        l324_40(x),
        l324_41(x),
        l324_42(x),
        l324_43(x),
        l324_44(x),
        l324_45(x),
        l324_46(x),
        l324_47(x),
        l324_48(x),
        l324_49(x),
        l324_50(x),
        l324_51(x),
        l324_52(x),
        l324_53(x),
        l324_54(x),
        l324_55(x),
        l324_56(x),
        l324_57(x),
        l324_58(x),
        l324_59(x),
        l324_60(x),
        l324_61(x),
        l324_62(x),
        l324_63(x),
        l324_64(x),
        l324_65(x),
        l324_66(x),
        l324_67(x),
        l324_68(x),
        l324_69(x),
        l324_70(x),
        l324_71(x),
        l324_72(x),
        l324_73(x),
        l324_74(x),
        l324_75(x),
        l324_76(x),
        l324_77(x),
        l324_78(x),
        l324_79(x),
        l324_80(x),
        l324_81(x),
        l324_82(x),
        l324_83(x),
        l324_84(x),
        l324_85(x),
        l324_86(x),
        l324_87(x),
        l324_88(x),
        l324_89(x),
        l324_90(x),
        l324_91(x),
        l324_92(x),
        l324_93(x),
        l324_94(x),
        l324_95(x),
        l324_96(x),
        l324_97(x),
        l324_98(x),
        l324_99(x),
        l324_100(x),
        l324_101(x),
        l324_102(x),
        l324_103(x),
        l324_104(x),
        l324_105(x),
        l324_106(x),
        l324_107(x),
        l324_108(x),
        l324_109(x),
        l324_110(x),
        l324_111(x),
        l324_112(x),
        l324_113(x),
        l324_114(x),
        l324_115(x),
        l324_116(x),
        l324_117(x),
        l324_118(x),
        l324_119(x),
        l324_120(x),
        l324_121(x),
        l324_122(x),
        l324_123(x),
        l324_124(x),
        l324_125(x),
        l324_126(x),
        l324_127(x),
        l324_128(x),
        l324_129(x),
        l324_130(x),
        l324_131(x),
        l324_132(x),
        l324_133(x),
        l324_134(x),
        l324_135(x),
        l324_136(x),
        l324_137(x),
        l324_138(x),
        l324_139(x),
        l324_140(x),
        l324_141(x),
        l324_142(x),
        l324_143(x),
        l324_144(x),
        l324_145(x),
        l324_146(x),
        l324_147(x),
        l324_148(x),
        l324_149(x),
        l324_150(x),
        l324_151(x),
        l324_152(x),
        l324_153(x),
        l324_154(x),
        l324_155(x),
        l324_156(x),
        l324_157(x),
        l324_158(x),
        l324_159(x),
        l324_160(x),
        l324_161(x),
        l324_162(x),
        l324_163(x),
        l324_164(x),
        l324_165(x),
        l324_166(x),
        l324_167(x),
        l324_168(x),
        l324_169(x),
        l324_170(x),
        l324_171(x),
        l324_172(x),
        l324_173(x),
        l324_174(x),
        l324_175(x),
        l324_176(x),
        l324_177(x),
        l324_178(x),
        l324_179(x),
        l324_180(x),
        l324_181(x),
        l324_182(x),
        l324_183(x),
        l324_184(x),
        l324_185(x),
        l324_186(x),
        l324_187(x),
        l324_188(x),
        l324_189(x),
        l324_190(x),
        l324_191(x),
        l324_192(x),
        l324_193(x),
        l324_194(x),
        l324_195(x),
        l324_196(x),
        l324_197(x),
        l324_198(x),
        l324_199(x),
        l324_200(x),
        l324_201(x),
        l324_202(x),
        l324_203(x),
        l324_204(x),
        l324_205(x),
        l324_206(x),
        l324_207(x),
        l324_208(x),
        l324_209(x),
        l324_210(x),
        l324_211(x),
        l324_212(x),
        l324_213(x),
        l324_214(x),
        l324_215(x),
        l324_216(x),
        l324_217(x),
        l324_218(x),
        l324_219(x),
        l324_220(x),
        l324_221(x),
        l324_222(x),
        l324_223(x),
        l324_224(x),
        l324_225(x),
        l324_226(x),
        l324_227(x),
        l324_228(x),
        l324_229(x),
        l324_230(x),
        l324_231(x),
        l324_232(x),
        l324_233(x),
        l324_234(x),
        l324_235(x),
        l324_236(x),
        l324_237(x),
        l324_238(x),
        l324_239(x),
        l324_240(x),
        l324_241(x),
        l324_242(x),
        l324_243(x),
        l324_244(x),
        l324_245(x),
        l324_246(x),
        l324_247(x),
        l324_248(x),
        l324_249(x),
        l324_250(x),
        l324_251(x),
        l324_252(x),
        l324_253(x),
        l324_254(x),
        l324_255(x),
        l324_256(x),
        l324_257(x),
        l324_258(x),
        l324_259(x),
        l324_260(x),
        l324_261(x),
        l324_262(x),
        l324_263(x),
        l324_264(x),
        l324_265(x),
        l324_266(x),
        l324_267(x),
        l324_268(x),
        l324_269(x),
        l324_270(x),
        l324_271(x),
        l324_272(x),
        l324_273(x),
        l324_274(x),
        l324_275(x),
        l324_276(x),
        l324_277(x),
        l324_278(x),
        l324_279(x),
        l324_280(x),
        l324_281(x),
        l324_282(x),
        l324_283(x),
        l324_284(x),
        l324_285(x),
        l324_286(x),
        l324_287(x),
    ]