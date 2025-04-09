import numpy as np




# Generated from reverse engineering
def l412_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 288
    out = np.empty(288, dtype=np.float32)
    
    # for i in range(0, 98):
    for i in range(0, 98):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3fffffff (len=30)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(98, 128):
    for i in range(0, 30):
        s = -1 * x[98 + i] + -1 * x[128 + i]
        s += biases[i]
        out[98 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 130):
    for i in range(0, 2):
        s = x[188 + i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(130, 160):
    for i in range(0, 30):
        s = x[158 + i]
        out[130 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 288):
    for i in range(0, 128):
        s = x[190 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l412_0(x):
    # x is a list (or vector) of length 318
    return max(0, x[0])
def l412_1(x):
    # x is a list (or vector) of length 318
    return max(0, x[1])
def l412_2(x):
    # x is a list (or vector) of length 318
    return max(0, x[2])
def l412_3(x):
    # x is a list (or vector) of length 318
    return max(0, x[3])
def l412_4(x):
    # x is a list (or vector) of length 318
    return max(0, x[4])
def l412_5(x):
    # x is a list (or vector) of length 318
    return max(0, x[5])
def l412_6(x):
    # x is a list (or vector) of length 318
    return max(0, x[6])
def l412_7(x):
    # x is a list (or vector) of length 318
    return max(0, x[7])
def l412_8(x):
    # x is a list (or vector) of length 318
    return max(0, x[8])
def l412_9(x):
    # x is a list (or vector) of length 318
    return max(0, x[9])
def l412_10(x):
    # x is a list (or vector) of length 318
    return max(0, x[10])
def l412_11(x):
    # x is a list (or vector) of length 318
    return max(0, x[11])
def l412_12(x):
    # x is a list (or vector) of length 318
    return max(0, x[12])
def l412_13(x):
    # x is a list (or vector) of length 318
    return max(0, x[13])
def l412_14(x):
    # x is a list (or vector) of length 318
    return max(0, x[14])
def l412_15(x):
    # x is a list (or vector) of length 318
    return max(0, x[15])
def l412_16(x):
    # x is a list (or vector) of length 318
    return max(0, x[16])
def l412_17(x):
    # x is a list (or vector) of length 318
    return max(0, x[17])
def l412_18(x):
    # x is a list (or vector) of length 318
    return max(0, x[18])
def l412_19(x):
    # x is a list (or vector) of length 318
    return max(0, x[19])
def l412_20(x):
    # x is a list (or vector) of length 318
    return max(0, x[20])
def l412_21(x):
    # x is a list (or vector) of length 318
    return max(0, x[21])
def l412_22(x):
    # x is a list (or vector) of length 318
    return max(0, x[22])
def l412_23(x):
    # x is a list (or vector) of length 318
    return max(0, x[23])
def l412_24(x):
    # x is a list (or vector) of length 318
    return max(0, x[24])
def l412_25(x):
    # x is a list (or vector) of length 318
    return max(0, x[25])
def l412_26(x):
    # x is a list (or vector) of length 318
    return max(0, x[26])
def l412_27(x):
    # x is a list (or vector) of length 318
    return max(0, x[27])
def l412_28(x):
    # x is a list (or vector) of length 318
    return max(0, x[28])
def l412_29(x):
    # x is a list (or vector) of length 318
    return max(0, x[29])
def l412_30(x):
    # x is a list (or vector) of length 318
    return max(0, x[30])
def l412_31(x):
    # x is a list (or vector) of length 318
    return max(0, x[31])
def l412_32(x):
    # x is a list (or vector) of length 318
    return max(0, x[32])
def l412_33(x):
    # x is a list (or vector) of length 318
    return max(0, x[33])
def l412_34(x):
    # x is a list (or vector) of length 318
    return max(0, x[34])
def l412_35(x):
    # x is a list (or vector) of length 318
    return max(0, x[35])
def l412_36(x):
    # x is a list (or vector) of length 318
    return max(0, x[36])
def l412_37(x):
    # x is a list (or vector) of length 318
    return max(0, x[37])
def l412_38(x):
    # x is a list (or vector) of length 318
    return max(0, x[38])
def l412_39(x):
    # x is a list (or vector) of length 318
    return max(0, x[39])
def l412_40(x):
    # x is a list (or vector) of length 318
    return max(0, x[40])
def l412_41(x):
    # x is a list (or vector) of length 318
    return max(0, x[41])
def l412_42(x):
    # x is a list (or vector) of length 318
    return max(0, x[42])
def l412_43(x):
    # x is a list (or vector) of length 318
    return max(0, x[43])
def l412_44(x):
    # x is a list (or vector) of length 318
    return max(0, x[44])
def l412_45(x):
    # x is a list (or vector) of length 318
    return max(0, x[45])
def l412_46(x):
    # x is a list (or vector) of length 318
    return max(0, x[46])
def l412_47(x):
    # x is a list (or vector) of length 318
    return max(0, x[47])
def l412_48(x):
    # x is a list (or vector) of length 318
    return max(0, x[48])
def l412_49(x):
    # x is a list (or vector) of length 318
    return max(0, x[49])
def l412_50(x):
    # x is a list (or vector) of length 318
    return max(0, x[50])
def l412_51(x):
    # x is a list (or vector) of length 318
    return max(0, x[51])
def l412_52(x):
    # x is a list (or vector) of length 318
    return max(0, x[52])
def l412_53(x):
    # x is a list (or vector) of length 318
    return max(0, x[53])
def l412_54(x):
    # x is a list (or vector) of length 318
    return max(0, x[54])
def l412_55(x):
    # x is a list (or vector) of length 318
    return max(0, x[55])
def l412_56(x):
    # x is a list (or vector) of length 318
    return max(0, x[56])
def l412_57(x):
    # x is a list (or vector) of length 318
    return max(0, x[57])
def l412_58(x):
    # x is a list (or vector) of length 318
    return max(0, x[58])
def l412_59(x):
    # x is a list (or vector) of length 318
    return max(0, x[59])
def l412_60(x):
    # x is a list (or vector) of length 318
    return max(0, x[60])
def l412_61(x):
    # x is a list (or vector) of length 318
    return max(0, x[61])
def l412_62(x):
    # x is a list (or vector) of length 318
    return max(0, x[62])
def l412_63(x):
    # x is a list (or vector) of length 318
    return max(0, x[63])
def l412_64(x):
    # x is a list (or vector) of length 318
    return max(0, x[64])
def l412_65(x):
    # x is a list (or vector) of length 318
    return max(0, x[65])
def l412_66(x):
    # x is a list (or vector) of length 318
    return max(0, x[66])
def l412_67(x):
    # x is a list (or vector) of length 318
    return max(0, x[67])
def l412_68(x):
    # x is a list (or vector) of length 318
    return max(0, x[68])
def l412_69(x):
    # x is a list (or vector) of length 318
    return max(0, x[69])
def l412_70(x):
    # x is a list (or vector) of length 318
    return max(0, x[70])
def l412_71(x):
    # x is a list (or vector) of length 318
    return max(0, x[71])
def l412_72(x):
    # x is a list (or vector) of length 318
    return max(0, x[72])
def l412_73(x):
    # x is a list (or vector) of length 318
    return max(0, x[73])
def l412_74(x):
    # x is a list (or vector) of length 318
    return max(0, x[74])
def l412_75(x):
    # x is a list (or vector) of length 318
    return max(0, x[75])
def l412_76(x):
    # x is a list (or vector) of length 318
    return max(0, x[76])
def l412_77(x):
    # x is a list (or vector) of length 318
    return max(0, x[77])
def l412_78(x):
    # x is a list (or vector) of length 318
    return max(0, x[78])
def l412_79(x):
    # x is a list (or vector) of length 318
    return max(0, x[79])
def l412_80(x):
    # x is a list (or vector) of length 318
    return max(0, x[80])
def l412_81(x):
    # x is a list (or vector) of length 318
    return max(0, x[81])
def l412_82(x):
    # x is a list (or vector) of length 318
    return max(0, x[82])
def l412_83(x):
    # x is a list (or vector) of length 318
    return max(0, x[83])
def l412_84(x):
    # x is a list (or vector) of length 318
    return max(0, x[84])
def l412_85(x):
    # x is a list (or vector) of length 318
    return max(0, x[85])
def l412_86(x):
    # x is a list (or vector) of length 318
    return max(0, x[86])
def l412_87(x):
    # x is a list (or vector) of length 318
    return max(0, x[87])
def l412_88(x):
    # x is a list (or vector) of length 318
    return max(0, x[88])
def l412_89(x):
    # x is a list (or vector) of length 318
    return max(0, x[89])
def l412_90(x):
    # x is a list (or vector) of length 318
    return max(0, x[90])
def l412_91(x):
    # x is a list (or vector) of length 318
    return max(0, x[91])
def l412_92(x):
    # x is a list (or vector) of length 318
    return max(0, x[92])
def l412_93(x):
    # x is a list (or vector) of length 318
    return max(0, x[93])
def l412_94(x):
    # x is a list (or vector) of length 318
    return max(0, x[94])
def l412_95(x):
    # x is a list (or vector) of length 318
    return max(0, x[95])
def l412_96(x):
    # x is a list (or vector) of length 318
    return max(0, x[96])
def l412_97(x):
    # x is a list (or vector) of length 318
    return max(0, x[97])
def l412_98(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[98] + -1.0*x[128] + 1.0)
def l412_99(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[99] + -1.0*x[129] + 1.0)
def l412_100(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[100] + -1.0*x[130] + 1.0)
def l412_101(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[101] + -1.0*x[131] + 1.0)
def l412_102(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[102] + -1.0*x[132] + 1.0)
def l412_103(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[103] + -1.0*x[133] + 1.0)
def l412_104(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[104] + -1.0*x[134] + 1.0)
def l412_105(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[105] + -1.0*x[135] + 1.0)
def l412_106(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[106] + -1.0*x[136] + 1.0)
def l412_107(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[107] + -1.0*x[137] + 1.0)
def l412_108(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[108] + -1.0*x[138] + 1.0)
def l412_109(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[109] + -1.0*x[139] + 1.0)
def l412_110(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[110] + -1.0*x[140] + 1.0)
def l412_111(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[111] + -1.0*x[141] + 1.0)
def l412_112(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[112] + -1.0*x[142] + 1.0)
def l412_113(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[113] + -1.0*x[143] + 1.0)
def l412_114(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[114] + -1.0*x[144] + 1.0)
def l412_115(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[115] + -1.0*x[145] + 1.0)
def l412_116(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[116] + -1.0*x[146] + 1.0)
def l412_117(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[117] + -1.0*x[147] + 1.0)
def l412_118(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[118] + -1.0*x[148] + 1.0)
def l412_119(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[119] + -1.0*x[149] + 1.0)
def l412_120(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[120] + -1.0*x[150] + 1.0)
def l412_121(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[121] + -1.0*x[151] + 1.0)
def l412_122(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[122] + -1.0*x[152] + 1.0)
def l412_123(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[123] + -1.0*x[153] + 1.0)
def l412_124(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[124] + -1.0*x[154] + 1.0)
def l412_125(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[125] + -1.0*x[155] + 1.0)
def l412_126(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[126] + -1.0*x[156] + 1.0)
def l412_127(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[127] + -1.0*x[157] + 1.0)
def l412_128(x):
    # x is a list (or vector) of length 318
    return max(0, x[188])
def l412_129(x):
    # x is a list (or vector) of length 318
    return max(0, x[189])
def l412_130(x):
    # x is a list (or vector) of length 318
    return max(0, x[158])
def l412_131(x):
    # x is a list (or vector) of length 318
    return max(0, x[159])
def l412_132(x):
    # x is a list (or vector) of length 318
    return max(0, x[160])
def l412_133(x):
    # x is a list (or vector) of length 318
    return max(0, x[161])
def l412_134(x):
    # x is a list (or vector) of length 318
    return max(0, x[162])
def l412_135(x):
    # x is a list (or vector) of length 318
    return max(0, x[163])
def l412_136(x):
    # x is a list (or vector) of length 318
    return max(0, x[164])
def l412_137(x):
    # x is a list (or vector) of length 318
    return max(0, x[165])
def l412_138(x):
    # x is a list (or vector) of length 318
    return max(0, x[166])
def l412_139(x):
    # x is a list (or vector) of length 318
    return max(0, x[167])
def l412_140(x):
    # x is a list (or vector) of length 318
    return max(0, x[168])
def l412_141(x):
    # x is a list (or vector) of length 318
    return max(0, x[169])
def l412_142(x):
    # x is a list (or vector) of length 318
    return max(0, x[170])
def l412_143(x):
    # x is a list (or vector) of length 318
    return max(0, x[171])
def l412_144(x):
    # x is a list (or vector) of length 318
    return max(0, x[172])
def l412_145(x):
    # x is a list (or vector) of length 318
    return max(0, x[173])
def l412_146(x):
    # x is a list (or vector) of length 318
    return max(0, x[174])
def l412_147(x):
    # x is a list (or vector) of length 318
    return max(0, x[175])
def l412_148(x):
    # x is a list (or vector) of length 318
    return max(0, x[176])
def l412_149(x):
    # x is a list (or vector) of length 318
    return max(0, x[177])
def l412_150(x):
    # x is a list (or vector) of length 318
    return max(0, x[178])
def l412_151(x):
    # x is a list (or vector) of length 318
    return max(0, x[179])
def l412_152(x):
    # x is a list (or vector) of length 318
    return max(0, x[180])
def l412_153(x):
    # x is a list (or vector) of length 318
    return max(0, x[181])
def l412_154(x):
    # x is a list (or vector) of length 318
    return max(0, x[182])
def l412_155(x):
    # x is a list (or vector) of length 318
    return max(0, x[183])
def l412_156(x):
    # x is a list (or vector) of length 318
    return max(0, x[184])
def l412_157(x):
    # x is a list (or vector) of length 318
    return max(0, x[185])
def l412_158(x):
    # x is a list (or vector) of length 318
    return max(0, x[186])
def l412_159(x):
    # x is a list (or vector) of length 318
    return max(0, x[187])
def l412_160(x):
    # x is a list (or vector) of length 318
    return max(0, x[190])
def l412_161(x):
    # x is a list (or vector) of length 318
    return max(0, x[191])
def l412_162(x):
    # x is a list (or vector) of length 318
    return max(0, x[192])
def l412_163(x):
    # x is a list (or vector) of length 318
    return max(0, x[193])
def l412_164(x):
    # x is a list (or vector) of length 318
    return max(0, x[194])
def l412_165(x):
    # x is a list (or vector) of length 318
    return max(0, x[195])
def l412_166(x):
    # x is a list (or vector) of length 318
    return max(0, x[196])
def l412_167(x):
    # x is a list (or vector) of length 318
    return max(0, x[197])
def l412_168(x):
    # x is a list (or vector) of length 318
    return max(0, x[198])
def l412_169(x):
    # x is a list (or vector) of length 318
    return max(0, x[199])
def l412_170(x):
    # x is a list (or vector) of length 318
    return max(0, x[200])
def l412_171(x):
    # x is a list (or vector) of length 318
    return max(0, x[201])
def l412_172(x):
    # x is a list (or vector) of length 318
    return max(0, x[202])
def l412_173(x):
    # x is a list (or vector) of length 318
    return max(0, x[203])
def l412_174(x):
    # x is a list (or vector) of length 318
    return max(0, x[204])
def l412_175(x):
    # x is a list (or vector) of length 318
    return max(0, x[205])
def l412_176(x):
    # x is a list (or vector) of length 318
    return max(0, x[206])
def l412_177(x):
    # x is a list (or vector) of length 318
    return max(0, x[207])
def l412_178(x):
    # x is a list (or vector) of length 318
    return max(0, x[208])
def l412_179(x):
    # x is a list (or vector) of length 318
    return max(0, x[209])
def l412_180(x):
    # x is a list (or vector) of length 318
    return max(0, x[210])
def l412_181(x):
    # x is a list (or vector) of length 318
    return max(0, x[211])
def l412_182(x):
    # x is a list (or vector) of length 318
    return max(0, x[212])
def l412_183(x):
    # x is a list (or vector) of length 318
    return max(0, x[213])
def l412_184(x):
    # x is a list (or vector) of length 318
    return max(0, x[214])
def l412_185(x):
    # x is a list (or vector) of length 318
    return max(0, x[215])
def l412_186(x):
    # x is a list (or vector) of length 318
    return max(0, x[216])
def l412_187(x):
    # x is a list (or vector) of length 318
    return max(0, x[217])
def l412_188(x):
    # x is a list (or vector) of length 318
    return max(0, x[218])
def l412_189(x):
    # x is a list (or vector) of length 318
    return max(0, x[219])
def l412_190(x):
    # x is a list (or vector) of length 318
    return max(0, x[220])
def l412_191(x):
    # x is a list (or vector) of length 318
    return max(0, x[221])
def l412_192(x):
    # x is a list (or vector) of length 318
    return max(0, x[222])
def l412_193(x):
    # x is a list (or vector) of length 318
    return max(0, x[223])
def l412_194(x):
    # x is a list (or vector) of length 318
    return max(0, x[224])
def l412_195(x):
    # x is a list (or vector) of length 318
    return max(0, x[225])
def l412_196(x):
    # x is a list (or vector) of length 318
    return max(0, x[226])
def l412_197(x):
    # x is a list (or vector) of length 318
    return max(0, x[227])
def l412_198(x):
    # x is a list (or vector) of length 318
    return max(0, x[228])
def l412_199(x):
    # x is a list (or vector) of length 318
    return max(0, x[229])
def l412_200(x):
    # x is a list (or vector) of length 318
    return max(0, x[230])
def l412_201(x):
    # x is a list (or vector) of length 318
    return max(0, x[231])
def l412_202(x):
    # x is a list (or vector) of length 318
    return max(0, x[232])
def l412_203(x):
    # x is a list (or vector) of length 318
    return max(0, x[233])
def l412_204(x):
    # x is a list (or vector) of length 318
    return max(0, x[234])
def l412_205(x):
    # x is a list (or vector) of length 318
    return max(0, x[235])
def l412_206(x):
    # x is a list (or vector) of length 318
    return max(0, x[236])
def l412_207(x):
    # x is a list (or vector) of length 318
    return max(0, x[237])
def l412_208(x):
    # x is a list (or vector) of length 318
    return max(0, x[238])
def l412_209(x):
    # x is a list (or vector) of length 318
    return max(0, x[239])
def l412_210(x):
    # x is a list (or vector) of length 318
    return max(0, x[240])
def l412_211(x):
    # x is a list (or vector) of length 318
    return max(0, x[241])
def l412_212(x):
    # x is a list (or vector) of length 318
    return max(0, x[242])
def l412_213(x):
    # x is a list (or vector) of length 318
    return max(0, x[243])
def l412_214(x):
    # x is a list (or vector) of length 318
    return max(0, x[244])
def l412_215(x):
    # x is a list (or vector) of length 318
    return max(0, x[245])
def l412_216(x):
    # x is a list (or vector) of length 318
    return max(0, x[246])
def l412_217(x):
    # x is a list (or vector) of length 318
    return max(0, x[247])
def l412_218(x):
    # x is a list (or vector) of length 318
    return max(0, x[248])
def l412_219(x):
    # x is a list (or vector) of length 318
    return max(0, x[249])
def l412_220(x):
    # x is a list (or vector) of length 318
    return max(0, x[250])
def l412_221(x):
    # x is a list (or vector) of length 318
    return max(0, x[251])
def l412_222(x):
    # x is a list (or vector) of length 318
    return max(0, x[252])
def l412_223(x):
    # x is a list (or vector) of length 318
    return max(0, x[253])
def l412_224(x):
    # x is a list (or vector) of length 318
    return max(0, x[254])
def l412_225(x):
    # x is a list (or vector) of length 318
    return max(0, x[255])
def l412_226(x):
    # x is a list (or vector) of length 318
    return max(0, x[256])
def l412_227(x):
    # x is a list (or vector) of length 318
    return max(0, x[257])
def l412_228(x):
    # x is a list (or vector) of length 318
    return max(0, x[258])
def l412_229(x):
    # x is a list (or vector) of length 318
    return max(0, x[259])
def l412_230(x):
    # x is a list (or vector) of length 318
    return max(0, x[260])
def l412_231(x):
    # x is a list (or vector) of length 318
    return max(0, x[261])
def l412_232(x):
    # x is a list (or vector) of length 318
    return max(0, x[262])
def l412_233(x):
    # x is a list (or vector) of length 318
    return max(0, x[263])
def l412_234(x):
    # x is a list (or vector) of length 318
    return max(0, x[264])
def l412_235(x):
    # x is a list (or vector) of length 318
    return max(0, x[265])
def l412_236(x):
    # x is a list (or vector) of length 318
    return max(0, x[266])
def l412_237(x):
    # x is a list (or vector) of length 318
    return max(0, x[267])
def l412_238(x):
    # x is a list (or vector) of length 318
    return max(0, x[268])
def l412_239(x):
    # x is a list (or vector) of length 318
    return max(0, x[269])
def l412_240(x):
    # x is a list (or vector) of length 318
    return max(0, x[270])
def l412_241(x):
    # x is a list (or vector) of length 318
    return max(0, x[271])
def l412_242(x):
    # x is a list (or vector) of length 318
    return max(0, x[272])
def l412_243(x):
    # x is a list (or vector) of length 318
    return max(0, x[273])
def l412_244(x):
    # x is a list (or vector) of length 318
    return max(0, x[274])
def l412_245(x):
    # x is a list (or vector) of length 318
    return max(0, x[275])
def l412_246(x):
    # x is a list (or vector) of length 318
    return max(0, x[276])
def l412_247(x):
    # x is a list (or vector) of length 318
    return max(0, x[277])
def l412_248(x):
    # x is a list (or vector) of length 318
    return max(0, x[278])
def l412_249(x):
    # x is a list (or vector) of length 318
    return max(0, x[279])
def l412_250(x):
    # x is a list (or vector) of length 318
    return max(0, x[280])
def l412_251(x):
    # x is a list (or vector) of length 318
    return max(0, x[281])
def l412_252(x):
    # x is a list (or vector) of length 318
    return max(0, x[282])
def l412_253(x):
    # x is a list (or vector) of length 318
    return max(0, x[283])
def l412_254(x):
    # x is a list (or vector) of length 318
    return max(0, x[284])
def l412_255(x):
    # x is a list (or vector) of length 318
    return max(0, x[285])
def l412_256(x):
    # x is a list (or vector) of length 318
    return max(0, x[286])
def l412_257(x):
    # x is a list (or vector) of length 318
    return max(0, x[287])
def l412_258(x):
    # x is a list (or vector) of length 318
    return max(0, x[288])
def l412_259(x):
    # x is a list (or vector) of length 318
    return max(0, x[289])
def l412_260(x):
    # x is a list (or vector) of length 318
    return max(0, x[290])
def l412_261(x):
    # x is a list (or vector) of length 318
    return max(0, x[291])
def l412_262(x):
    # x is a list (or vector) of length 318
    return max(0, x[292])
def l412_263(x):
    # x is a list (or vector) of length 318
    return max(0, x[293])
def l412_264(x):
    # x is a list (or vector) of length 318
    return max(0, x[294])
def l412_265(x):
    # x is a list (or vector) of length 318
    return max(0, x[295])
def l412_266(x):
    # x is a list (or vector) of length 318
    return max(0, x[296])
def l412_267(x):
    # x is a list (or vector) of length 318
    return max(0, x[297])
def l412_268(x):
    # x is a list (or vector) of length 318
    return max(0, x[298])
def l412_269(x):
    # x is a list (or vector) of length 318
    return max(0, x[299])
def l412_270(x):
    # x is a list (or vector) of length 318
    return max(0, x[300])
def l412_271(x):
    # x is a list (or vector) of length 318
    return max(0, x[301])
def l412_272(x):
    # x is a list (or vector) of length 318
    return max(0, x[302])
def l412_273(x):
    # x is a list (or vector) of length 318
    return max(0, x[303])
def l412_274(x):
    # x is a list (or vector) of length 318
    return max(0, x[304])
def l412_275(x):
    # x is a list (or vector) of length 318
    return max(0, x[305])
def l412_276(x):
    # x is a list (or vector) of length 318
    return max(0, x[306])
def l412_277(x):
    # x is a list (or vector) of length 318
    return max(0, x[307])
def l412_278(x):
    # x is a list (or vector) of length 318
    return max(0, x[308])
def l412_279(x):
    # x is a list (or vector) of length 318
    return max(0, x[309])
def l412_280(x):
    # x is a list (or vector) of length 318
    return max(0, x[310])
def l412_281(x):
    # x is a list (or vector) of length 318
    return max(0, x[311])
def l412_282(x):
    # x is a list (or vector) of length 318
    return max(0, x[312])
def l412_283(x):
    # x is a list (or vector) of length 318
    return max(0, x[313])
def l412_284(x):
    # x is a list (or vector) of length 318
    return max(0, x[314])
def l412_285(x):
    # x is a list (or vector) of length 318
    return max(0, x[315])
def l412_286(x):
    # x is a list (or vector) of length 318
    return max(0, x[316])
def l412_287(x):
    # x is a list (or vector) of length 318
    return max(0, x[317])
def l412_(x):
    # x is a list (or vector) of length 318
    return [
        l412_0(x),
        l412_1(x),
        l412_2(x),
        l412_3(x),
        l412_4(x),
        l412_5(x),
        l412_6(x),
        l412_7(x),
        l412_8(x),
        l412_9(x),
        l412_10(x),
        l412_11(x),
        l412_12(x),
        l412_13(x),
        l412_14(x),
        l412_15(x),
        l412_16(x),
        l412_17(x),
        l412_18(x),
        l412_19(x),
        l412_20(x),
        l412_21(x),
        l412_22(x),
        l412_23(x),
        l412_24(x),
        l412_25(x),
        l412_26(x),
        l412_27(x),
        l412_28(x),
        l412_29(x),
        l412_30(x),
        l412_31(x),
        l412_32(x),
        l412_33(x),
        l412_34(x),
        l412_35(x),
        l412_36(x),
        l412_37(x),
        l412_38(x),
        l412_39(x),
        l412_40(x),
        l412_41(x),
        l412_42(x),
        l412_43(x),
        l412_44(x),
        l412_45(x),
        l412_46(x),
        l412_47(x),
        l412_48(x),
        l412_49(x),
        l412_50(x),
        l412_51(x),
        l412_52(x),
        l412_53(x),
        l412_54(x),
        l412_55(x),
        l412_56(x),
        l412_57(x),
        l412_58(x),
        l412_59(x),
        l412_60(x),
        l412_61(x),
        l412_62(x),
        l412_63(x),
        l412_64(x),
        l412_65(x),
        l412_66(x),
        l412_67(x),
        l412_68(x),
        l412_69(x),
        l412_70(x),
        l412_71(x),
        l412_72(x),
        l412_73(x),
        l412_74(x),
        l412_75(x),
        l412_76(x),
        l412_77(x),
        l412_78(x),
        l412_79(x),
        l412_80(x),
        l412_81(x),
        l412_82(x),
        l412_83(x),
        l412_84(x),
        l412_85(x),
        l412_86(x),
        l412_87(x),
        l412_88(x),
        l412_89(x),
        l412_90(x),
        l412_91(x),
        l412_92(x),
        l412_93(x),
        l412_94(x),
        l412_95(x),
        l412_96(x),
        l412_97(x),
        l412_98(x),
        l412_99(x),
        l412_100(x),
        l412_101(x),
        l412_102(x),
        l412_103(x),
        l412_104(x),
        l412_105(x),
        l412_106(x),
        l412_107(x),
        l412_108(x),
        l412_109(x),
        l412_110(x),
        l412_111(x),
        l412_112(x),
        l412_113(x),
        l412_114(x),
        l412_115(x),
        l412_116(x),
        l412_117(x),
        l412_118(x),
        l412_119(x),
        l412_120(x),
        l412_121(x),
        l412_122(x),
        l412_123(x),
        l412_124(x),
        l412_125(x),
        l412_126(x),
        l412_127(x),
        l412_128(x),
        l412_129(x),
        l412_130(x),
        l412_131(x),
        l412_132(x),
        l412_133(x),
        l412_134(x),
        l412_135(x),
        l412_136(x),
        l412_137(x),
        l412_138(x),
        l412_139(x),
        l412_140(x),
        l412_141(x),
        l412_142(x),
        l412_143(x),
        l412_144(x),
        l412_145(x),
        l412_146(x),
        l412_147(x),
        l412_148(x),
        l412_149(x),
        l412_150(x),
        l412_151(x),
        l412_152(x),
        l412_153(x),
        l412_154(x),
        l412_155(x),
        l412_156(x),
        l412_157(x),
        l412_158(x),
        l412_159(x),
        l412_160(x),
        l412_161(x),
        l412_162(x),
        l412_163(x),
        l412_164(x),
        l412_165(x),
        l412_166(x),
        l412_167(x),
        l412_168(x),
        l412_169(x),
        l412_170(x),
        l412_171(x),
        l412_172(x),
        l412_173(x),
        l412_174(x),
        l412_175(x),
        l412_176(x),
        l412_177(x),
        l412_178(x),
        l412_179(x),
        l412_180(x),
        l412_181(x),
        l412_182(x),
        l412_183(x),
        l412_184(x),
        l412_185(x),
        l412_186(x),
        l412_187(x),
        l412_188(x),
        l412_189(x),
        l412_190(x),
        l412_191(x),
        l412_192(x),
        l412_193(x),
        l412_194(x),
        l412_195(x),
        l412_196(x),
        l412_197(x),
        l412_198(x),
        l412_199(x),
        l412_200(x),
        l412_201(x),
        l412_202(x),
        l412_203(x),
        l412_204(x),
        l412_205(x),
        l412_206(x),
        l412_207(x),
        l412_208(x),
        l412_209(x),
        l412_210(x),
        l412_211(x),
        l412_212(x),
        l412_213(x),
        l412_214(x),
        l412_215(x),
        l412_216(x),
        l412_217(x),
        l412_218(x),
        l412_219(x),
        l412_220(x),
        l412_221(x),
        l412_222(x),
        l412_223(x),
        l412_224(x),
        l412_225(x),
        l412_226(x),
        l412_227(x),
        l412_228(x),
        l412_229(x),
        l412_230(x),
        l412_231(x),
        l412_232(x),
        l412_233(x),
        l412_234(x),
        l412_235(x),
        l412_236(x),
        l412_237(x),
        l412_238(x),
        l412_239(x),
        l412_240(x),
        l412_241(x),
        l412_242(x),
        l412_243(x),
        l412_244(x),
        l412_245(x),
        l412_246(x),
        l412_247(x),
        l412_248(x),
        l412_249(x),
        l412_250(x),
        l412_251(x),
        l412_252(x),
        l412_253(x),
        l412_254(x),
        l412_255(x),
        l412_256(x),
        l412_257(x),
        l412_258(x),
        l412_259(x),
        l412_260(x),
        l412_261(x),
        l412_262(x),
        l412_263(x),
        l412_264(x),
        l412_265(x),
        l412_266(x),
        l412_267(x),
        l412_268(x),
        l412_269(x),
        l412_270(x),
        l412_271(x),
        l412_272(x),
        l412_273(x),
        l412_274(x),
        l412_275(x),
        l412_276(x),
        l412_277(x),
        l412_278(x),
        l412_279(x),
        l412_280(x),
        l412_281(x),
        l412_282(x),
        l412_283(x),
        l412_284(x),
        l412_285(x),
        l412_286(x),
        l412_287(x),
    ]