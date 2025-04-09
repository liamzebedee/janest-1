import numpy as np




# Generated from reverse engineering
def l72_g(x: np.ndarray) -> np.ndarray:
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




def l72_0(x):
    # x is a list (or vector) of length 319
    return max(0, x[0])
def l72_1(x):
    # x is a list (or vector) of length 319
    return max(0, x[1])
def l72_2(x):
    # x is a list (or vector) of length 319
    return max(0, x[2])
def l72_3(x):
    # x is a list (or vector) of length 319
    return max(0, x[3])
def l72_4(x):
    # x is a list (or vector) of length 319
    return max(0, x[4])
def l72_5(x):
    # x is a list (or vector) of length 319
    return max(0, x[5])
def l72_6(x):
    # x is a list (or vector) of length 319
    return max(0, x[6])
def l72_7(x):
    # x is a list (or vector) of length 319
    return max(0, x[7])
def l72_8(x):
    # x is a list (or vector) of length 319
    return max(0, x[8])
def l72_9(x):
    # x is a list (or vector) of length 319
    return max(0, x[9])
def l72_10(x):
    # x is a list (or vector) of length 319
    return max(0, x[10])
def l72_11(x):
    # x is a list (or vector) of length 319
    return max(0, x[11])
def l72_12(x):
    # x is a list (or vector) of length 319
    return max(0, x[12])
def l72_13(x):
    # x is a list (or vector) of length 319
    return max(0, x[13])
def l72_14(x):
    # x is a list (or vector) of length 319
    return max(0, x[14])
def l72_15(x):
    # x is a list (or vector) of length 319
    return max(0, x[15])
def l72_16(x):
    # x is a list (or vector) of length 319
    return max(0, x[16])
def l72_17(x):
    # x is a list (or vector) of length 319
    return max(0, x[17])
def l72_18(x):
    # x is a list (or vector) of length 319
    return max(0, x[18])
def l72_19(x):
    # x is a list (or vector) of length 319
    return max(0, x[19])
def l72_20(x):
    # x is a list (or vector) of length 319
    return max(0, x[20])
def l72_21(x):
    # x is a list (or vector) of length 319
    return max(0, x[21])
def l72_22(x):
    # x is a list (or vector) of length 319
    return max(0, x[22])
def l72_23(x):
    # x is a list (or vector) of length 319
    return max(0, x[23])
def l72_24(x):
    # x is a list (or vector) of length 319
    return max(0, x[24])
def l72_25(x):
    # x is a list (or vector) of length 319
    return max(0, x[25])
def l72_26(x):
    # x is a list (or vector) of length 319
    return max(0, x[26])
def l72_27(x):
    # x is a list (or vector) of length 319
    return max(0, x[27])
def l72_28(x):
    # x is a list (or vector) of length 319
    return max(0, x[28])
def l72_29(x):
    # x is a list (or vector) of length 319
    return max(0, x[29])
def l72_30(x):
    # x is a list (or vector) of length 319
    return max(0, x[30])
def l72_31(x):
    # x is a list (or vector) of length 319
    return max(0, x[31])
def l72_32(x):
    # x is a list (or vector) of length 319
    return max(0, x[32])
def l72_33(x):
    # x is a list (or vector) of length 319
    return max(0, x[33])
def l72_34(x):
    # x is a list (or vector) of length 319
    return max(0, x[34])
def l72_35(x):
    # x is a list (or vector) of length 319
    return max(0, x[35])
def l72_36(x):
    # x is a list (or vector) of length 319
    return max(0, x[36])
def l72_37(x):
    # x is a list (or vector) of length 319
    return max(0, x[37])
def l72_38(x):
    # x is a list (or vector) of length 319
    return max(0, x[38])
def l72_39(x):
    # x is a list (or vector) of length 319
    return max(0, x[39])
def l72_40(x):
    # x is a list (or vector) of length 319
    return max(0, x[40])
def l72_41(x):
    # x is a list (or vector) of length 319
    return max(0, x[41])
def l72_42(x):
    # x is a list (or vector) of length 319
    return max(0, x[42])
def l72_43(x):
    # x is a list (or vector) of length 319
    return max(0, x[43])
def l72_44(x):
    # x is a list (or vector) of length 319
    return max(0, x[44])
def l72_45(x):
    # x is a list (or vector) of length 319
    return max(0, x[45])
def l72_46(x):
    # x is a list (or vector) of length 319
    return max(0, x[46])
def l72_47(x):
    # x is a list (or vector) of length 319
    return max(0, x[47])
def l72_48(x):
    # x is a list (or vector) of length 319
    return max(0, x[48])
def l72_49(x):
    # x is a list (or vector) of length 319
    return max(0, x[49])
def l72_50(x):
    # x is a list (or vector) of length 319
    return max(0, x[50])
def l72_51(x):
    # x is a list (or vector) of length 319
    return max(0, x[51])
def l72_52(x):
    # x is a list (or vector) of length 319
    return max(0, x[52])
def l72_53(x):
    # x is a list (or vector) of length 319
    return max(0, x[53])
def l72_54(x):
    # x is a list (or vector) of length 319
    return max(0, x[54])
def l72_55(x):
    # x is a list (or vector) of length 319
    return max(0, x[55])
def l72_56(x):
    # x is a list (or vector) of length 319
    return max(0, x[56])
def l72_57(x):
    # x is a list (or vector) of length 319
    return max(0, x[57])
def l72_58(x):
    # x is a list (or vector) of length 319
    return max(0, x[58])
def l72_59(x):
    # x is a list (or vector) of length 319
    return max(0, x[59])
def l72_60(x):
    # x is a list (or vector) of length 319
    return max(0, x[60])
def l72_61(x):
    # x is a list (or vector) of length 319
    return max(0, x[61])
def l72_62(x):
    # x is a list (or vector) of length 319
    return max(0, x[62])
def l72_63(x):
    # x is a list (or vector) of length 319
    return max(0, x[63])
def l72_64(x):
    # x is a list (or vector) of length 319
    return max(0, x[64])
def l72_65(x):
    # x is a list (or vector) of length 319
    return max(0, x[65])
def l72_66(x):
    # x is a list (or vector) of length 319
    return max(0, x[66])
def l72_67(x):
    # x is a list (or vector) of length 319
    return max(0, x[67])
def l72_68(x):
    # x is a list (or vector) of length 319
    return max(0, x[68])
def l72_69(x):
    # x is a list (or vector) of length 319
    return max(0, x[69])
def l72_70(x):
    # x is a list (or vector) of length 319
    return max(0, x[70])
def l72_71(x):
    # x is a list (or vector) of length 319
    return max(0, x[71])
def l72_72(x):
    # x is a list (or vector) of length 319
    return max(0, x[72])
def l72_73(x):
    # x is a list (or vector) of length 319
    return max(0, x[73])
def l72_74(x):
    # x is a list (or vector) of length 319
    return max(0, x[74])
def l72_75(x):
    # x is a list (or vector) of length 319
    return max(0, x[75])
def l72_76(x):
    # x is a list (or vector) of length 319
    return max(0, x[76])
def l72_77(x):
    # x is a list (or vector) of length 319
    return max(0, x[77])
def l72_78(x):
    # x is a list (or vector) of length 319
    return max(0, x[78])
def l72_79(x):
    # x is a list (or vector) of length 319
    return max(0, x[79])
def l72_80(x):
    # x is a list (or vector) of length 319
    return max(0, x[80])
def l72_81(x):
    # x is a list (or vector) of length 319
    return max(0, x[81])
def l72_82(x):
    # x is a list (or vector) of length 319
    return max(0, x[82])
def l72_83(x):
    # x is a list (or vector) of length 319
    return max(0, x[83])
def l72_84(x):
    # x is a list (or vector) of length 319
    return max(0, x[84])
def l72_85(x):
    # x is a list (or vector) of length 319
    return max(0, x[85])
def l72_86(x):
    # x is a list (or vector) of length 319
    return max(0, x[86])
def l72_87(x):
    # x is a list (or vector) of length 319
    return max(0, x[87])
def l72_88(x):
    # x is a list (or vector) of length 319
    return max(0, x[88])
def l72_89(x):
    # x is a list (or vector) of length 319
    return max(0, x[89])
def l72_90(x):
    # x is a list (or vector) of length 319
    return max(0, x[90])
def l72_91(x):
    # x is a list (or vector) of length 319
    return max(0, x[91])
def l72_92(x):
    # x is a list (or vector) of length 319
    return max(0, x[92])
def l72_93(x):
    # x is a list (or vector) of length 319
    return max(0, x[93])
def l72_94(x):
    # x is a list (or vector) of length 319
    return max(0, x[94])
def l72_95(x):
    # x is a list (or vector) of length 319
    return max(0, x[95])
def l72_96(x):
    # x is a list (or vector) of length 319
    return max(0, x[96])
def l72_97(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[97] + -1.0*x[128] + 1.0)
def l72_98(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[98] + -1.0*x[129] + 1.0)
def l72_99(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[99] + -1.0*x[130] + 1.0)
def l72_100(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[100] + -1.0*x[131] + 1.0)
def l72_101(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[101] + -1.0*x[132] + 1.0)
def l72_102(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[102] + -1.0*x[133] + 1.0)
def l72_103(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[103] + -1.0*x[134] + 1.0)
def l72_104(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[104] + -1.0*x[135] + 1.0)
def l72_105(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[105] + -1.0*x[136] + 1.0)
def l72_106(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[106] + -1.0*x[137] + 1.0)
def l72_107(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[107] + -1.0*x[138] + 1.0)
def l72_108(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[108] + -1.0*x[139] + 1.0)
def l72_109(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[109] + -1.0*x[140] + 1.0)
def l72_110(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[110] + -1.0*x[141] + 1.0)
def l72_111(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[111] + -1.0*x[142] + 1.0)
def l72_112(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[112] + -1.0*x[143] + 1.0)
def l72_113(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[113] + -1.0*x[144] + 1.0)
def l72_114(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[114] + -1.0*x[145] + 1.0)
def l72_115(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[115] + -1.0*x[146] + 1.0)
def l72_116(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[116] + -1.0*x[147] + 1.0)
def l72_117(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[117] + -1.0*x[148] + 1.0)
def l72_118(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[118] + -1.0*x[149] + 1.0)
def l72_119(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[119] + -1.0*x[150] + 1.0)
def l72_120(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[120] + -1.0*x[151] + 1.0)
def l72_121(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[121] + -1.0*x[152] + 1.0)
def l72_122(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[122] + -1.0*x[153] + 1.0)
def l72_123(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[123] + -1.0*x[154] + 1.0)
def l72_124(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[124] + -1.0*x[155] + 1.0)
def l72_125(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[125] + -1.0*x[156] + 1.0)
def l72_126(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[126] + -1.0*x[157] + 1.0)
def l72_127(x):
    # x is a list (or vector) of length 319
    return max(0, -1.0*x[127] + -1.0*x[158] + 1.0)
def l72_128(x):
    # x is a list (or vector) of length 319
    return max(0, x[190])
def l72_129(x):
    # x is a list (or vector) of length 319
    return max(0, x[159])
def l72_130(x):
    # x is a list (or vector) of length 319
    return max(0, x[160])
def l72_131(x):
    # x is a list (or vector) of length 319
    return max(0, x[161])
def l72_132(x):
    # x is a list (or vector) of length 319
    return max(0, x[162])
def l72_133(x):
    # x is a list (or vector) of length 319
    return max(0, x[163])
def l72_134(x):
    # x is a list (or vector) of length 319
    return max(0, x[164])
def l72_135(x):
    # x is a list (or vector) of length 319
    return max(0, x[165])
def l72_136(x):
    # x is a list (or vector) of length 319
    return max(0, x[166])
def l72_137(x):
    # x is a list (or vector) of length 319
    return max(0, x[167])
def l72_138(x):
    # x is a list (or vector) of length 319
    return max(0, x[168])
def l72_139(x):
    # x is a list (or vector) of length 319
    return max(0, x[169])
def l72_140(x):
    # x is a list (or vector) of length 319
    return max(0, x[170])
def l72_141(x):
    # x is a list (or vector) of length 319
    return max(0, x[171])
def l72_142(x):
    # x is a list (or vector) of length 319
    return max(0, x[172])
def l72_143(x):
    # x is a list (or vector) of length 319
    return max(0, x[173])
def l72_144(x):
    # x is a list (or vector) of length 319
    return max(0, x[174])
def l72_145(x):
    # x is a list (or vector) of length 319
    return max(0, x[175])
def l72_146(x):
    # x is a list (or vector) of length 319
    return max(0, x[176])
def l72_147(x):
    # x is a list (or vector) of length 319
    return max(0, x[177])
def l72_148(x):
    # x is a list (or vector) of length 319
    return max(0, x[178])
def l72_149(x):
    # x is a list (or vector) of length 319
    return max(0, x[179])
def l72_150(x):
    # x is a list (or vector) of length 319
    return max(0, x[180])
def l72_151(x):
    # x is a list (or vector) of length 319
    return max(0, x[181])
def l72_152(x):
    # x is a list (or vector) of length 319
    return max(0, x[182])
def l72_153(x):
    # x is a list (or vector) of length 319
    return max(0, x[183])
def l72_154(x):
    # x is a list (or vector) of length 319
    return max(0, x[184])
def l72_155(x):
    # x is a list (or vector) of length 319
    return max(0, x[185])
def l72_156(x):
    # x is a list (or vector) of length 319
    return max(0, x[186])
def l72_157(x):
    # x is a list (or vector) of length 319
    return max(0, x[187])
def l72_158(x):
    # x is a list (or vector) of length 319
    return max(0, x[188])
def l72_159(x):
    # x is a list (or vector) of length 319
    return max(0, x[189])
def l72_160(x):
    # x is a list (or vector) of length 319
    return max(0, x[191])
def l72_161(x):
    # x is a list (or vector) of length 319
    return max(0, x[192])
def l72_162(x):
    # x is a list (or vector) of length 319
    return max(0, x[193])
def l72_163(x):
    # x is a list (or vector) of length 319
    return max(0, x[194])
def l72_164(x):
    # x is a list (or vector) of length 319
    return max(0, x[195])
def l72_165(x):
    # x is a list (or vector) of length 319
    return max(0, x[196])
def l72_166(x):
    # x is a list (or vector) of length 319
    return max(0, x[197])
def l72_167(x):
    # x is a list (or vector) of length 319
    return max(0, x[198])
def l72_168(x):
    # x is a list (or vector) of length 319
    return max(0, x[199])
def l72_169(x):
    # x is a list (or vector) of length 319
    return max(0, x[200])
def l72_170(x):
    # x is a list (or vector) of length 319
    return max(0, x[201])
def l72_171(x):
    # x is a list (or vector) of length 319
    return max(0, x[202])
def l72_172(x):
    # x is a list (or vector) of length 319
    return max(0, x[203])
def l72_173(x):
    # x is a list (or vector) of length 319
    return max(0, x[204])
def l72_174(x):
    # x is a list (or vector) of length 319
    return max(0, x[205])
def l72_175(x):
    # x is a list (or vector) of length 319
    return max(0, x[206])
def l72_176(x):
    # x is a list (or vector) of length 319
    return max(0, x[207])
def l72_177(x):
    # x is a list (or vector) of length 319
    return max(0, x[208])
def l72_178(x):
    # x is a list (or vector) of length 319
    return max(0, x[209])
def l72_179(x):
    # x is a list (or vector) of length 319
    return max(0, x[210])
def l72_180(x):
    # x is a list (or vector) of length 319
    return max(0, x[211])
def l72_181(x):
    # x is a list (or vector) of length 319
    return max(0, x[212])
def l72_182(x):
    # x is a list (or vector) of length 319
    return max(0, x[213])
def l72_183(x):
    # x is a list (or vector) of length 319
    return max(0, x[214])
def l72_184(x):
    # x is a list (or vector) of length 319
    return max(0, x[215])
def l72_185(x):
    # x is a list (or vector) of length 319
    return max(0, x[216])
def l72_186(x):
    # x is a list (or vector) of length 319
    return max(0, x[217])
def l72_187(x):
    # x is a list (or vector) of length 319
    return max(0, x[218])
def l72_188(x):
    # x is a list (or vector) of length 319
    return max(0, x[219])
def l72_189(x):
    # x is a list (or vector) of length 319
    return max(0, x[220])
def l72_190(x):
    # x is a list (or vector) of length 319
    return max(0, x[221])
def l72_191(x):
    # x is a list (or vector) of length 319
    return max(0, x[222])
def l72_192(x):
    # x is a list (or vector) of length 319
    return max(0, x[223])
def l72_193(x):
    # x is a list (or vector) of length 319
    return max(0, x[224])
def l72_194(x):
    # x is a list (or vector) of length 319
    return max(0, x[225])
def l72_195(x):
    # x is a list (or vector) of length 319
    return max(0, x[226])
def l72_196(x):
    # x is a list (or vector) of length 319
    return max(0, x[227])
def l72_197(x):
    # x is a list (or vector) of length 319
    return max(0, x[228])
def l72_198(x):
    # x is a list (or vector) of length 319
    return max(0, x[229])
def l72_199(x):
    # x is a list (or vector) of length 319
    return max(0, x[230])
def l72_200(x):
    # x is a list (or vector) of length 319
    return max(0, x[231])
def l72_201(x):
    # x is a list (or vector) of length 319
    return max(0, x[232])
def l72_202(x):
    # x is a list (or vector) of length 319
    return max(0, x[233])
def l72_203(x):
    # x is a list (or vector) of length 319
    return max(0, x[234])
def l72_204(x):
    # x is a list (or vector) of length 319
    return max(0, x[235])
def l72_205(x):
    # x is a list (or vector) of length 319
    return max(0, x[236])
def l72_206(x):
    # x is a list (or vector) of length 319
    return max(0, x[237])
def l72_207(x):
    # x is a list (or vector) of length 319
    return max(0, x[238])
def l72_208(x):
    # x is a list (or vector) of length 319
    return max(0, x[239])
def l72_209(x):
    # x is a list (or vector) of length 319
    return max(0, x[240])
def l72_210(x):
    # x is a list (or vector) of length 319
    return max(0, x[241])
def l72_211(x):
    # x is a list (or vector) of length 319
    return max(0, x[242])
def l72_212(x):
    # x is a list (or vector) of length 319
    return max(0, x[243])
def l72_213(x):
    # x is a list (or vector) of length 319
    return max(0, x[244])
def l72_214(x):
    # x is a list (or vector) of length 319
    return max(0, x[245])
def l72_215(x):
    # x is a list (or vector) of length 319
    return max(0, x[246])
def l72_216(x):
    # x is a list (or vector) of length 319
    return max(0, x[247])
def l72_217(x):
    # x is a list (or vector) of length 319
    return max(0, x[248])
def l72_218(x):
    # x is a list (or vector) of length 319
    return max(0, x[249])
def l72_219(x):
    # x is a list (or vector) of length 319
    return max(0, x[250])
def l72_220(x):
    # x is a list (or vector) of length 319
    return max(0, x[251])
def l72_221(x):
    # x is a list (or vector) of length 319
    return max(0, x[252])
def l72_222(x):
    # x is a list (or vector) of length 319
    return max(0, x[253])
def l72_223(x):
    # x is a list (or vector) of length 319
    return max(0, x[254])
def l72_224(x):
    # x is a list (or vector) of length 319
    return max(0, x[255])
def l72_225(x):
    # x is a list (or vector) of length 319
    return max(0, x[256])
def l72_226(x):
    # x is a list (or vector) of length 319
    return max(0, x[257])
def l72_227(x):
    # x is a list (or vector) of length 319
    return max(0, x[258])
def l72_228(x):
    # x is a list (or vector) of length 319
    return max(0, x[259])
def l72_229(x):
    # x is a list (or vector) of length 319
    return max(0, x[260])
def l72_230(x):
    # x is a list (or vector) of length 319
    return max(0, x[261])
def l72_231(x):
    # x is a list (or vector) of length 319
    return max(0, x[262])
def l72_232(x):
    # x is a list (or vector) of length 319
    return max(0, x[263])
def l72_233(x):
    # x is a list (or vector) of length 319
    return max(0, x[264])
def l72_234(x):
    # x is a list (or vector) of length 319
    return max(0, x[265])
def l72_235(x):
    # x is a list (or vector) of length 319
    return max(0, x[266])
def l72_236(x):
    # x is a list (or vector) of length 319
    return max(0, x[267])
def l72_237(x):
    # x is a list (or vector) of length 319
    return max(0, x[268])
def l72_238(x):
    # x is a list (or vector) of length 319
    return max(0, x[269])
def l72_239(x):
    # x is a list (or vector) of length 319
    return max(0, x[270])
def l72_240(x):
    # x is a list (or vector) of length 319
    return max(0, x[271])
def l72_241(x):
    # x is a list (or vector) of length 319
    return max(0, x[272])
def l72_242(x):
    # x is a list (or vector) of length 319
    return max(0, x[273])
def l72_243(x):
    # x is a list (or vector) of length 319
    return max(0, x[274])
def l72_244(x):
    # x is a list (or vector) of length 319
    return max(0, x[275])
def l72_245(x):
    # x is a list (or vector) of length 319
    return max(0, x[276])
def l72_246(x):
    # x is a list (or vector) of length 319
    return max(0, x[277])
def l72_247(x):
    # x is a list (or vector) of length 319
    return max(0, x[278])
def l72_248(x):
    # x is a list (or vector) of length 319
    return max(0, x[279])
def l72_249(x):
    # x is a list (or vector) of length 319
    return max(0, x[280])
def l72_250(x):
    # x is a list (or vector) of length 319
    return max(0, x[281])
def l72_251(x):
    # x is a list (or vector) of length 319
    return max(0, x[282])
def l72_252(x):
    # x is a list (or vector) of length 319
    return max(0, x[283])
def l72_253(x):
    # x is a list (or vector) of length 319
    return max(0, x[284])
def l72_254(x):
    # x is a list (or vector) of length 319
    return max(0, x[285])
def l72_255(x):
    # x is a list (or vector) of length 319
    return max(0, x[286])
def l72_256(x):
    # x is a list (or vector) of length 319
    return max(0, x[287])
def l72_257(x):
    # x is a list (or vector) of length 319
    return max(0, x[288])
def l72_258(x):
    # x is a list (or vector) of length 319
    return max(0, x[289])
def l72_259(x):
    # x is a list (or vector) of length 319
    return max(0, x[290])
def l72_260(x):
    # x is a list (or vector) of length 319
    return max(0, x[291])
def l72_261(x):
    # x is a list (or vector) of length 319
    return max(0, x[292])
def l72_262(x):
    # x is a list (or vector) of length 319
    return max(0, x[293])
def l72_263(x):
    # x is a list (or vector) of length 319
    return max(0, x[294])
def l72_264(x):
    # x is a list (or vector) of length 319
    return max(0, x[295])
def l72_265(x):
    # x is a list (or vector) of length 319
    return max(0, x[296])
def l72_266(x):
    # x is a list (or vector) of length 319
    return max(0, x[297])
def l72_267(x):
    # x is a list (or vector) of length 319
    return max(0, x[298])
def l72_268(x):
    # x is a list (or vector) of length 319
    return max(0, x[299])
def l72_269(x):
    # x is a list (or vector) of length 319
    return max(0, x[300])
def l72_270(x):
    # x is a list (or vector) of length 319
    return max(0, x[301])
def l72_271(x):
    # x is a list (or vector) of length 319
    return max(0, x[302])
def l72_272(x):
    # x is a list (or vector) of length 319
    return max(0, x[303])
def l72_273(x):
    # x is a list (or vector) of length 319
    return max(0, x[304])
def l72_274(x):
    # x is a list (or vector) of length 319
    return max(0, x[305])
def l72_275(x):
    # x is a list (or vector) of length 319
    return max(0, x[306])
def l72_276(x):
    # x is a list (or vector) of length 319
    return max(0, x[307])
def l72_277(x):
    # x is a list (or vector) of length 319
    return max(0, x[308])
def l72_278(x):
    # x is a list (or vector) of length 319
    return max(0, x[309])
def l72_279(x):
    # x is a list (or vector) of length 319
    return max(0, x[310])
def l72_280(x):
    # x is a list (or vector) of length 319
    return max(0, x[311])
def l72_281(x):
    # x is a list (or vector) of length 319
    return max(0, x[312])
def l72_282(x):
    # x is a list (or vector) of length 319
    return max(0, x[313])
def l72_283(x):
    # x is a list (or vector) of length 319
    return max(0, x[314])
def l72_284(x):
    # x is a list (or vector) of length 319
    return max(0, x[315])
def l72_285(x):
    # x is a list (or vector) of length 319
    return max(0, x[316])
def l72_286(x):
    # x is a list (or vector) of length 319
    return max(0, x[317])
def l72_287(x):
    # x is a list (or vector) of length 319
    return max(0, x[318])
def l72_(x):
    # x is a list (or vector) of length 319
    return [
        l72_0(x),
        l72_1(x),
        l72_2(x),
        l72_3(x),
        l72_4(x),
        l72_5(x),
        l72_6(x),
        l72_7(x),
        l72_8(x),
        l72_9(x),
        l72_10(x),
        l72_11(x),
        l72_12(x),
        l72_13(x),
        l72_14(x),
        l72_15(x),
        l72_16(x),
        l72_17(x),
        l72_18(x),
        l72_19(x),
        l72_20(x),
        l72_21(x),
        l72_22(x),
        l72_23(x),
        l72_24(x),
        l72_25(x),
        l72_26(x),
        l72_27(x),
        l72_28(x),
        l72_29(x),
        l72_30(x),
        l72_31(x),
        l72_32(x),
        l72_33(x),
        l72_34(x),
        l72_35(x),
        l72_36(x),
        l72_37(x),
        l72_38(x),
        l72_39(x),
        l72_40(x),
        l72_41(x),
        l72_42(x),
        l72_43(x),
        l72_44(x),
        l72_45(x),
        l72_46(x),
        l72_47(x),
        l72_48(x),
        l72_49(x),
        l72_50(x),
        l72_51(x),
        l72_52(x),
        l72_53(x),
        l72_54(x),
        l72_55(x),
        l72_56(x),
        l72_57(x),
        l72_58(x),
        l72_59(x),
        l72_60(x),
        l72_61(x),
        l72_62(x),
        l72_63(x),
        l72_64(x),
        l72_65(x),
        l72_66(x),
        l72_67(x),
        l72_68(x),
        l72_69(x),
        l72_70(x),
        l72_71(x),
        l72_72(x),
        l72_73(x),
        l72_74(x),
        l72_75(x),
        l72_76(x),
        l72_77(x),
        l72_78(x),
        l72_79(x),
        l72_80(x),
        l72_81(x),
        l72_82(x),
        l72_83(x),
        l72_84(x),
        l72_85(x),
        l72_86(x),
        l72_87(x),
        l72_88(x),
        l72_89(x),
        l72_90(x),
        l72_91(x),
        l72_92(x),
        l72_93(x),
        l72_94(x),
        l72_95(x),
        l72_96(x),
        l72_97(x),
        l72_98(x),
        l72_99(x),
        l72_100(x),
        l72_101(x),
        l72_102(x),
        l72_103(x),
        l72_104(x),
        l72_105(x),
        l72_106(x),
        l72_107(x),
        l72_108(x),
        l72_109(x),
        l72_110(x),
        l72_111(x),
        l72_112(x),
        l72_113(x),
        l72_114(x),
        l72_115(x),
        l72_116(x),
        l72_117(x),
        l72_118(x),
        l72_119(x),
        l72_120(x),
        l72_121(x),
        l72_122(x),
        l72_123(x),
        l72_124(x),
        l72_125(x),
        l72_126(x),
        l72_127(x),
        l72_128(x),
        l72_129(x),
        l72_130(x),
        l72_131(x),
        l72_132(x),
        l72_133(x),
        l72_134(x),
        l72_135(x),
        l72_136(x),
        l72_137(x),
        l72_138(x),
        l72_139(x),
        l72_140(x),
        l72_141(x),
        l72_142(x),
        l72_143(x),
        l72_144(x),
        l72_145(x),
        l72_146(x),
        l72_147(x),
        l72_148(x),
        l72_149(x),
        l72_150(x),
        l72_151(x),
        l72_152(x),
        l72_153(x),
        l72_154(x),
        l72_155(x),
        l72_156(x),
        l72_157(x),
        l72_158(x),
        l72_159(x),
        l72_160(x),
        l72_161(x),
        l72_162(x),
        l72_163(x),
        l72_164(x),
        l72_165(x),
        l72_166(x),
        l72_167(x),
        l72_168(x),
        l72_169(x),
        l72_170(x),
        l72_171(x),
        l72_172(x),
        l72_173(x),
        l72_174(x),
        l72_175(x),
        l72_176(x),
        l72_177(x),
        l72_178(x),
        l72_179(x),
        l72_180(x),
        l72_181(x),
        l72_182(x),
        l72_183(x),
        l72_184(x),
        l72_185(x),
        l72_186(x),
        l72_187(x),
        l72_188(x),
        l72_189(x),
        l72_190(x),
        l72_191(x),
        l72_192(x),
        l72_193(x),
        l72_194(x),
        l72_195(x),
        l72_196(x),
        l72_197(x),
        l72_198(x),
        l72_199(x),
        l72_200(x),
        l72_201(x),
        l72_202(x),
        l72_203(x),
        l72_204(x),
        l72_205(x),
        l72_206(x),
        l72_207(x),
        l72_208(x),
        l72_209(x),
        l72_210(x),
        l72_211(x),
        l72_212(x),
        l72_213(x),
        l72_214(x),
        l72_215(x),
        l72_216(x),
        l72_217(x),
        l72_218(x),
        l72_219(x),
        l72_220(x),
        l72_221(x),
        l72_222(x),
        l72_223(x),
        l72_224(x),
        l72_225(x),
        l72_226(x),
        l72_227(x),
        l72_228(x),
        l72_229(x),
        l72_230(x),
        l72_231(x),
        l72_232(x),
        l72_233(x),
        l72_234(x),
        l72_235(x),
        l72_236(x),
        l72_237(x),
        l72_238(x),
        l72_239(x),
        l72_240(x),
        l72_241(x),
        l72_242(x),
        l72_243(x),
        l72_244(x),
        l72_245(x),
        l72_246(x),
        l72_247(x),
        l72_248(x),
        l72_249(x),
        l72_250(x),
        l72_251(x),
        l72_252(x),
        l72_253(x),
        l72_254(x),
        l72_255(x),
        l72_256(x),
        l72_257(x),
        l72_258(x),
        l72_259(x),
        l72_260(x),
        l72_261(x),
        l72_262(x),
        l72_263(x),
        l72_264(x),
        l72_265(x),
        l72_266(x),
        l72_267(x),
        l72_268(x),
        l72_269(x),
        l72_270(x),
        l72_271(x),
        l72_272(x),
        l72_273(x),
        l72_274(x),
        l72_275(x),
        l72_276(x),
        l72_277(x),
        l72_278(x),
        l72_279(x),
        l72_280(x),
        l72_281(x),
        l72_282(x),
        l72_283(x),
        l72_284(x),
        l72_285(x),
        l72_286(x),
        l72_287(x),
    ]