import numpy as np




# Generated from reverse engineering
def l328_g(x: np.ndarray) -> np.ndarray:
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




def l328_0(x):
    # x is a list (or vector) of length 318
    return max(0, x[0])
def l328_1(x):
    # x is a list (or vector) of length 318
    return max(0, x[1])
def l328_2(x):
    # x is a list (or vector) of length 318
    return max(0, x[2])
def l328_3(x):
    # x is a list (or vector) of length 318
    return max(0, x[3])
def l328_4(x):
    # x is a list (or vector) of length 318
    return max(0, x[4])
def l328_5(x):
    # x is a list (or vector) of length 318
    return max(0, x[5])
def l328_6(x):
    # x is a list (or vector) of length 318
    return max(0, x[6])
def l328_7(x):
    # x is a list (or vector) of length 318
    return max(0, x[7])
def l328_8(x):
    # x is a list (or vector) of length 318
    return max(0, x[8])
def l328_9(x):
    # x is a list (or vector) of length 318
    return max(0, x[9])
def l328_10(x):
    # x is a list (or vector) of length 318
    return max(0, x[10])
def l328_11(x):
    # x is a list (or vector) of length 318
    return max(0, x[11])
def l328_12(x):
    # x is a list (or vector) of length 318
    return max(0, x[12])
def l328_13(x):
    # x is a list (or vector) of length 318
    return max(0, x[13])
def l328_14(x):
    # x is a list (or vector) of length 318
    return max(0, x[14])
def l328_15(x):
    # x is a list (or vector) of length 318
    return max(0, x[15])
def l328_16(x):
    # x is a list (or vector) of length 318
    return max(0, x[16])
def l328_17(x):
    # x is a list (or vector) of length 318
    return max(0, x[17])
def l328_18(x):
    # x is a list (or vector) of length 318
    return max(0, x[18])
def l328_19(x):
    # x is a list (or vector) of length 318
    return max(0, x[19])
def l328_20(x):
    # x is a list (or vector) of length 318
    return max(0, x[20])
def l328_21(x):
    # x is a list (or vector) of length 318
    return max(0, x[21])
def l328_22(x):
    # x is a list (or vector) of length 318
    return max(0, x[22])
def l328_23(x):
    # x is a list (or vector) of length 318
    return max(0, x[23])
def l328_24(x):
    # x is a list (or vector) of length 318
    return max(0, x[24])
def l328_25(x):
    # x is a list (or vector) of length 318
    return max(0, x[25])
def l328_26(x):
    # x is a list (or vector) of length 318
    return max(0, x[26])
def l328_27(x):
    # x is a list (or vector) of length 318
    return max(0, x[27])
def l328_28(x):
    # x is a list (or vector) of length 318
    return max(0, x[28])
def l328_29(x):
    # x is a list (or vector) of length 318
    return max(0, x[29])
def l328_30(x):
    # x is a list (or vector) of length 318
    return max(0, x[30])
def l328_31(x):
    # x is a list (or vector) of length 318
    return max(0, x[31])
def l328_32(x):
    # x is a list (or vector) of length 318
    return max(0, x[32])
def l328_33(x):
    # x is a list (or vector) of length 318
    return max(0, x[33])
def l328_34(x):
    # x is a list (or vector) of length 318
    return max(0, x[34])
def l328_35(x):
    # x is a list (or vector) of length 318
    return max(0, x[35])
def l328_36(x):
    # x is a list (or vector) of length 318
    return max(0, x[36])
def l328_37(x):
    # x is a list (or vector) of length 318
    return max(0, x[37])
def l328_38(x):
    # x is a list (or vector) of length 318
    return max(0, x[38])
def l328_39(x):
    # x is a list (or vector) of length 318
    return max(0, x[39])
def l328_40(x):
    # x is a list (or vector) of length 318
    return max(0, x[40])
def l328_41(x):
    # x is a list (or vector) of length 318
    return max(0, x[41])
def l328_42(x):
    # x is a list (or vector) of length 318
    return max(0, x[42])
def l328_43(x):
    # x is a list (or vector) of length 318
    return max(0, x[43])
def l328_44(x):
    # x is a list (or vector) of length 318
    return max(0, x[44])
def l328_45(x):
    # x is a list (or vector) of length 318
    return max(0, x[45])
def l328_46(x):
    # x is a list (or vector) of length 318
    return max(0, x[46])
def l328_47(x):
    # x is a list (or vector) of length 318
    return max(0, x[47])
def l328_48(x):
    # x is a list (or vector) of length 318
    return max(0, x[48])
def l328_49(x):
    # x is a list (or vector) of length 318
    return max(0, x[49])
def l328_50(x):
    # x is a list (or vector) of length 318
    return max(0, x[50])
def l328_51(x):
    # x is a list (or vector) of length 318
    return max(0, x[51])
def l328_52(x):
    # x is a list (or vector) of length 318
    return max(0, x[52])
def l328_53(x):
    # x is a list (or vector) of length 318
    return max(0, x[53])
def l328_54(x):
    # x is a list (or vector) of length 318
    return max(0, x[54])
def l328_55(x):
    # x is a list (or vector) of length 318
    return max(0, x[55])
def l328_56(x):
    # x is a list (or vector) of length 318
    return max(0, x[56])
def l328_57(x):
    # x is a list (or vector) of length 318
    return max(0, x[57])
def l328_58(x):
    # x is a list (or vector) of length 318
    return max(0, x[58])
def l328_59(x):
    # x is a list (or vector) of length 318
    return max(0, x[59])
def l328_60(x):
    # x is a list (or vector) of length 318
    return max(0, x[60])
def l328_61(x):
    # x is a list (or vector) of length 318
    return max(0, x[61])
def l328_62(x):
    # x is a list (or vector) of length 318
    return max(0, x[62])
def l328_63(x):
    # x is a list (or vector) of length 318
    return max(0, x[63])
def l328_64(x):
    # x is a list (or vector) of length 318
    return max(0, x[64])
def l328_65(x):
    # x is a list (or vector) of length 318
    return max(0, x[65])
def l328_66(x):
    # x is a list (or vector) of length 318
    return max(0, x[66])
def l328_67(x):
    # x is a list (or vector) of length 318
    return max(0, x[67])
def l328_68(x):
    # x is a list (or vector) of length 318
    return max(0, x[68])
def l328_69(x):
    # x is a list (or vector) of length 318
    return max(0, x[69])
def l328_70(x):
    # x is a list (or vector) of length 318
    return max(0, x[70])
def l328_71(x):
    # x is a list (or vector) of length 318
    return max(0, x[71])
def l328_72(x):
    # x is a list (or vector) of length 318
    return max(0, x[72])
def l328_73(x):
    # x is a list (or vector) of length 318
    return max(0, x[73])
def l328_74(x):
    # x is a list (or vector) of length 318
    return max(0, x[74])
def l328_75(x):
    # x is a list (or vector) of length 318
    return max(0, x[75])
def l328_76(x):
    # x is a list (or vector) of length 318
    return max(0, x[76])
def l328_77(x):
    # x is a list (or vector) of length 318
    return max(0, x[77])
def l328_78(x):
    # x is a list (or vector) of length 318
    return max(0, x[78])
def l328_79(x):
    # x is a list (or vector) of length 318
    return max(0, x[79])
def l328_80(x):
    # x is a list (or vector) of length 318
    return max(0, x[80])
def l328_81(x):
    # x is a list (or vector) of length 318
    return max(0, x[81])
def l328_82(x):
    # x is a list (or vector) of length 318
    return max(0, x[82])
def l328_83(x):
    # x is a list (or vector) of length 318
    return max(0, x[83])
def l328_84(x):
    # x is a list (or vector) of length 318
    return max(0, x[84])
def l328_85(x):
    # x is a list (or vector) of length 318
    return max(0, x[85])
def l328_86(x):
    # x is a list (or vector) of length 318
    return max(0, x[86])
def l328_87(x):
    # x is a list (or vector) of length 318
    return max(0, x[87])
def l328_88(x):
    # x is a list (or vector) of length 318
    return max(0, x[88])
def l328_89(x):
    # x is a list (or vector) of length 318
    return max(0, x[89])
def l328_90(x):
    # x is a list (or vector) of length 318
    return max(0, x[90])
def l328_91(x):
    # x is a list (or vector) of length 318
    return max(0, x[91])
def l328_92(x):
    # x is a list (or vector) of length 318
    return max(0, x[92])
def l328_93(x):
    # x is a list (or vector) of length 318
    return max(0, x[93])
def l328_94(x):
    # x is a list (or vector) of length 318
    return max(0, x[94])
def l328_95(x):
    # x is a list (or vector) of length 318
    return max(0, x[95])
def l328_96(x):
    # x is a list (or vector) of length 318
    return max(0, x[96])
def l328_97(x):
    # x is a list (or vector) of length 318
    return max(0, x[97])
def l328_98(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[98] + -1.0*x[128] + 1.0)
def l328_99(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[99] + -1.0*x[129] + 1.0)
def l328_100(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[100] + -1.0*x[130] + 1.0)
def l328_101(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[101] + -1.0*x[131] + 1.0)
def l328_102(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[102] + -1.0*x[132] + 1.0)
def l328_103(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[103] + -1.0*x[133] + 1.0)
def l328_104(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[104] + -1.0*x[134] + 1.0)
def l328_105(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[105] + -1.0*x[135] + 1.0)
def l328_106(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[106] + -1.0*x[136] + 1.0)
def l328_107(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[107] + -1.0*x[137] + 1.0)
def l328_108(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[108] + -1.0*x[138] + 1.0)
def l328_109(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[109] + -1.0*x[139] + 1.0)
def l328_110(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[110] + -1.0*x[140] + 1.0)
def l328_111(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[111] + -1.0*x[141] + 1.0)
def l328_112(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[112] + -1.0*x[142] + 1.0)
def l328_113(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[113] + -1.0*x[143] + 1.0)
def l328_114(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[114] + -1.0*x[144] + 1.0)
def l328_115(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[115] + -1.0*x[145] + 1.0)
def l328_116(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[116] + -1.0*x[146] + 1.0)
def l328_117(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[117] + -1.0*x[147] + 1.0)
def l328_118(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[118] + -1.0*x[148] + 1.0)
def l328_119(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[119] + -1.0*x[149] + 1.0)
def l328_120(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[120] + -1.0*x[150] + 1.0)
def l328_121(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[121] + -1.0*x[151] + 1.0)
def l328_122(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[122] + -1.0*x[152] + 1.0)
def l328_123(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[123] + -1.0*x[153] + 1.0)
def l328_124(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[124] + -1.0*x[154] + 1.0)
def l328_125(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[125] + -1.0*x[155] + 1.0)
def l328_126(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[126] + -1.0*x[156] + 1.0)
def l328_127(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[127] + -1.0*x[157] + 1.0)
def l328_128(x):
    # x is a list (or vector) of length 318
    return max(0, x[188])
def l328_129(x):
    # x is a list (or vector) of length 318
    return max(0, x[189])
def l328_130(x):
    # x is a list (or vector) of length 318
    return max(0, x[158])
def l328_131(x):
    # x is a list (or vector) of length 318
    return max(0, x[159])
def l328_132(x):
    # x is a list (or vector) of length 318
    return max(0, x[160])
def l328_133(x):
    # x is a list (or vector) of length 318
    return max(0, x[161])
def l328_134(x):
    # x is a list (or vector) of length 318
    return max(0, x[162])
def l328_135(x):
    # x is a list (or vector) of length 318
    return max(0, x[163])
def l328_136(x):
    # x is a list (or vector) of length 318
    return max(0, x[164])
def l328_137(x):
    # x is a list (or vector) of length 318
    return max(0, x[165])
def l328_138(x):
    # x is a list (or vector) of length 318
    return max(0, x[166])
def l328_139(x):
    # x is a list (or vector) of length 318
    return max(0, x[167])
def l328_140(x):
    # x is a list (or vector) of length 318
    return max(0, x[168])
def l328_141(x):
    # x is a list (or vector) of length 318
    return max(0, x[169])
def l328_142(x):
    # x is a list (or vector) of length 318
    return max(0, x[170])
def l328_143(x):
    # x is a list (or vector) of length 318
    return max(0, x[171])
def l328_144(x):
    # x is a list (or vector) of length 318
    return max(0, x[172])
def l328_145(x):
    # x is a list (or vector) of length 318
    return max(0, x[173])
def l328_146(x):
    # x is a list (or vector) of length 318
    return max(0, x[174])
def l328_147(x):
    # x is a list (or vector) of length 318
    return max(0, x[175])
def l328_148(x):
    # x is a list (or vector) of length 318
    return max(0, x[176])
def l328_149(x):
    # x is a list (or vector) of length 318
    return max(0, x[177])
def l328_150(x):
    # x is a list (or vector) of length 318
    return max(0, x[178])
def l328_151(x):
    # x is a list (or vector) of length 318
    return max(0, x[179])
def l328_152(x):
    # x is a list (or vector) of length 318
    return max(0, x[180])
def l328_153(x):
    # x is a list (or vector) of length 318
    return max(0, x[181])
def l328_154(x):
    # x is a list (or vector) of length 318
    return max(0, x[182])
def l328_155(x):
    # x is a list (or vector) of length 318
    return max(0, x[183])
def l328_156(x):
    # x is a list (or vector) of length 318
    return max(0, x[184])
def l328_157(x):
    # x is a list (or vector) of length 318
    return max(0, x[185])
def l328_158(x):
    # x is a list (or vector) of length 318
    return max(0, x[186])
def l328_159(x):
    # x is a list (or vector) of length 318
    return max(0, x[187])
def l328_160(x):
    # x is a list (or vector) of length 318
    return max(0, x[190])
def l328_161(x):
    # x is a list (or vector) of length 318
    return max(0, x[191])
def l328_162(x):
    # x is a list (or vector) of length 318
    return max(0, x[192])
def l328_163(x):
    # x is a list (or vector) of length 318
    return max(0, x[193])
def l328_164(x):
    # x is a list (or vector) of length 318
    return max(0, x[194])
def l328_165(x):
    # x is a list (or vector) of length 318
    return max(0, x[195])
def l328_166(x):
    # x is a list (or vector) of length 318
    return max(0, x[196])
def l328_167(x):
    # x is a list (or vector) of length 318
    return max(0, x[197])
def l328_168(x):
    # x is a list (or vector) of length 318
    return max(0, x[198])
def l328_169(x):
    # x is a list (or vector) of length 318
    return max(0, x[199])
def l328_170(x):
    # x is a list (or vector) of length 318
    return max(0, x[200])
def l328_171(x):
    # x is a list (or vector) of length 318
    return max(0, x[201])
def l328_172(x):
    # x is a list (or vector) of length 318
    return max(0, x[202])
def l328_173(x):
    # x is a list (or vector) of length 318
    return max(0, x[203])
def l328_174(x):
    # x is a list (or vector) of length 318
    return max(0, x[204])
def l328_175(x):
    # x is a list (or vector) of length 318
    return max(0, x[205])
def l328_176(x):
    # x is a list (or vector) of length 318
    return max(0, x[206])
def l328_177(x):
    # x is a list (or vector) of length 318
    return max(0, x[207])
def l328_178(x):
    # x is a list (or vector) of length 318
    return max(0, x[208])
def l328_179(x):
    # x is a list (or vector) of length 318
    return max(0, x[209])
def l328_180(x):
    # x is a list (or vector) of length 318
    return max(0, x[210])
def l328_181(x):
    # x is a list (or vector) of length 318
    return max(0, x[211])
def l328_182(x):
    # x is a list (or vector) of length 318
    return max(0, x[212])
def l328_183(x):
    # x is a list (or vector) of length 318
    return max(0, x[213])
def l328_184(x):
    # x is a list (or vector) of length 318
    return max(0, x[214])
def l328_185(x):
    # x is a list (or vector) of length 318
    return max(0, x[215])
def l328_186(x):
    # x is a list (or vector) of length 318
    return max(0, x[216])
def l328_187(x):
    # x is a list (or vector) of length 318
    return max(0, x[217])
def l328_188(x):
    # x is a list (or vector) of length 318
    return max(0, x[218])
def l328_189(x):
    # x is a list (or vector) of length 318
    return max(0, x[219])
def l328_190(x):
    # x is a list (or vector) of length 318
    return max(0, x[220])
def l328_191(x):
    # x is a list (or vector) of length 318
    return max(0, x[221])
def l328_192(x):
    # x is a list (or vector) of length 318
    return max(0, x[222])
def l328_193(x):
    # x is a list (or vector) of length 318
    return max(0, x[223])
def l328_194(x):
    # x is a list (or vector) of length 318
    return max(0, x[224])
def l328_195(x):
    # x is a list (or vector) of length 318
    return max(0, x[225])
def l328_196(x):
    # x is a list (or vector) of length 318
    return max(0, x[226])
def l328_197(x):
    # x is a list (or vector) of length 318
    return max(0, x[227])
def l328_198(x):
    # x is a list (or vector) of length 318
    return max(0, x[228])
def l328_199(x):
    # x is a list (or vector) of length 318
    return max(0, x[229])
def l328_200(x):
    # x is a list (or vector) of length 318
    return max(0, x[230])
def l328_201(x):
    # x is a list (or vector) of length 318
    return max(0, x[231])
def l328_202(x):
    # x is a list (or vector) of length 318
    return max(0, x[232])
def l328_203(x):
    # x is a list (or vector) of length 318
    return max(0, x[233])
def l328_204(x):
    # x is a list (or vector) of length 318
    return max(0, x[234])
def l328_205(x):
    # x is a list (or vector) of length 318
    return max(0, x[235])
def l328_206(x):
    # x is a list (or vector) of length 318
    return max(0, x[236])
def l328_207(x):
    # x is a list (or vector) of length 318
    return max(0, x[237])
def l328_208(x):
    # x is a list (or vector) of length 318
    return max(0, x[238])
def l328_209(x):
    # x is a list (or vector) of length 318
    return max(0, x[239])
def l328_210(x):
    # x is a list (or vector) of length 318
    return max(0, x[240])
def l328_211(x):
    # x is a list (or vector) of length 318
    return max(0, x[241])
def l328_212(x):
    # x is a list (or vector) of length 318
    return max(0, x[242])
def l328_213(x):
    # x is a list (or vector) of length 318
    return max(0, x[243])
def l328_214(x):
    # x is a list (or vector) of length 318
    return max(0, x[244])
def l328_215(x):
    # x is a list (or vector) of length 318
    return max(0, x[245])
def l328_216(x):
    # x is a list (or vector) of length 318
    return max(0, x[246])
def l328_217(x):
    # x is a list (or vector) of length 318
    return max(0, x[247])
def l328_218(x):
    # x is a list (or vector) of length 318
    return max(0, x[248])
def l328_219(x):
    # x is a list (or vector) of length 318
    return max(0, x[249])
def l328_220(x):
    # x is a list (or vector) of length 318
    return max(0, x[250])
def l328_221(x):
    # x is a list (or vector) of length 318
    return max(0, x[251])
def l328_222(x):
    # x is a list (or vector) of length 318
    return max(0, x[252])
def l328_223(x):
    # x is a list (or vector) of length 318
    return max(0, x[253])
def l328_224(x):
    # x is a list (or vector) of length 318
    return max(0, x[254])
def l328_225(x):
    # x is a list (or vector) of length 318
    return max(0, x[255])
def l328_226(x):
    # x is a list (or vector) of length 318
    return max(0, x[256])
def l328_227(x):
    # x is a list (or vector) of length 318
    return max(0, x[257])
def l328_228(x):
    # x is a list (or vector) of length 318
    return max(0, x[258])
def l328_229(x):
    # x is a list (or vector) of length 318
    return max(0, x[259])
def l328_230(x):
    # x is a list (or vector) of length 318
    return max(0, x[260])
def l328_231(x):
    # x is a list (or vector) of length 318
    return max(0, x[261])
def l328_232(x):
    # x is a list (or vector) of length 318
    return max(0, x[262])
def l328_233(x):
    # x is a list (or vector) of length 318
    return max(0, x[263])
def l328_234(x):
    # x is a list (or vector) of length 318
    return max(0, x[264])
def l328_235(x):
    # x is a list (or vector) of length 318
    return max(0, x[265])
def l328_236(x):
    # x is a list (or vector) of length 318
    return max(0, x[266])
def l328_237(x):
    # x is a list (or vector) of length 318
    return max(0, x[267])
def l328_238(x):
    # x is a list (or vector) of length 318
    return max(0, x[268])
def l328_239(x):
    # x is a list (or vector) of length 318
    return max(0, x[269])
def l328_240(x):
    # x is a list (or vector) of length 318
    return max(0, x[270])
def l328_241(x):
    # x is a list (or vector) of length 318
    return max(0, x[271])
def l328_242(x):
    # x is a list (or vector) of length 318
    return max(0, x[272])
def l328_243(x):
    # x is a list (or vector) of length 318
    return max(0, x[273])
def l328_244(x):
    # x is a list (or vector) of length 318
    return max(0, x[274])
def l328_245(x):
    # x is a list (or vector) of length 318
    return max(0, x[275])
def l328_246(x):
    # x is a list (or vector) of length 318
    return max(0, x[276])
def l328_247(x):
    # x is a list (or vector) of length 318
    return max(0, x[277])
def l328_248(x):
    # x is a list (or vector) of length 318
    return max(0, x[278])
def l328_249(x):
    # x is a list (or vector) of length 318
    return max(0, x[279])
def l328_250(x):
    # x is a list (or vector) of length 318
    return max(0, x[280])
def l328_251(x):
    # x is a list (or vector) of length 318
    return max(0, x[281])
def l328_252(x):
    # x is a list (or vector) of length 318
    return max(0, x[282])
def l328_253(x):
    # x is a list (or vector) of length 318
    return max(0, x[283])
def l328_254(x):
    # x is a list (or vector) of length 318
    return max(0, x[284])
def l328_255(x):
    # x is a list (or vector) of length 318
    return max(0, x[285])
def l328_256(x):
    # x is a list (or vector) of length 318
    return max(0, x[286])
def l328_257(x):
    # x is a list (or vector) of length 318
    return max(0, x[287])
def l328_258(x):
    # x is a list (or vector) of length 318
    return max(0, x[288])
def l328_259(x):
    # x is a list (or vector) of length 318
    return max(0, x[289])
def l328_260(x):
    # x is a list (or vector) of length 318
    return max(0, x[290])
def l328_261(x):
    # x is a list (or vector) of length 318
    return max(0, x[291])
def l328_262(x):
    # x is a list (or vector) of length 318
    return max(0, x[292])
def l328_263(x):
    # x is a list (or vector) of length 318
    return max(0, x[293])
def l328_264(x):
    # x is a list (or vector) of length 318
    return max(0, x[294])
def l328_265(x):
    # x is a list (or vector) of length 318
    return max(0, x[295])
def l328_266(x):
    # x is a list (or vector) of length 318
    return max(0, x[296])
def l328_267(x):
    # x is a list (or vector) of length 318
    return max(0, x[297])
def l328_268(x):
    # x is a list (or vector) of length 318
    return max(0, x[298])
def l328_269(x):
    # x is a list (or vector) of length 318
    return max(0, x[299])
def l328_270(x):
    # x is a list (or vector) of length 318
    return max(0, x[300])
def l328_271(x):
    # x is a list (or vector) of length 318
    return max(0, x[301])
def l328_272(x):
    # x is a list (or vector) of length 318
    return max(0, x[302])
def l328_273(x):
    # x is a list (or vector) of length 318
    return max(0, x[303])
def l328_274(x):
    # x is a list (or vector) of length 318
    return max(0, x[304])
def l328_275(x):
    # x is a list (or vector) of length 318
    return max(0, x[305])
def l328_276(x):
    # x is a list (or vector) of length 318
    return max(0, x[306])
def l328_277(x):
    # x is a list (or vector) of length 318
    return max(0, x[307])
def l328_278(x):
    # x is a list (or vector) of length 318
    return max(0, x[308])
def l328_279(x):
    # x is a list (or vector) of length 318
    return max(0, x[309])
def l328_280(x):
    # x is a list (or vector) of length 318
    return max(0, x[310])
def l328_281(x):
    # x is a list (or vector) of length 318
    return max(0, x[311])
def l328_282(x):
    # x is a list (or vector) of length 318
    return max(0, x[312])
def l328_283(x):
    # x is a list (or vector) of length 318
    return max(0, x[313])
def l328_284(x):
    # x is a list (or vector) of length 318
    return max(0, x[314])
def l328_285(x):
    # x is a list (or vector) of length 318
    return max(0, x[315])
def l328_286(x):
    # x is a list (or vector) of length 318
    return max(0, x[316])
def l328_287(x):
    # x is a list (or vector) of length 318
    return max(0, x[317])
def l328_(x):
    # x is a list (or vector) of length 318
    return [
        l328_0(x),
        l328_1(x),
        l328_2(x),
        l328_3(x),
        l328_4(x),
        l328_5(x),
        l328_6(x),
        l328_7(x),
        l328_8(x),
        l328_9(x),
        l328_10(x),
        l328_11(x),
        l328_12(x),
        l328_13(x),
        l328_14(x),
        l328_15(x),
        l328_16(x),
        l328_17(x),
        l328_18(x),
        l328_19(x),
        l328_20(x),
        l328_21(x),
        l328_22(x),
        l328_23(x),
        l328_24(x),
        l328_25(x),
        l328_26(x),
        l328_27(x),
        l328_28(x),
        l328_29(x),
        l328_30(x),
        l328_31(x),
        l328_32(x),
        l328_33(x),
        l328_34(x),
        l328_35(x),
        l328_36(x),
        l328_37(x),
        l328_38(x),
        l328_39(x),
        l328_40(x),
        l328_41(x),
        l328_42(x),
        l328_43(x),
        l328_44(x),
        l328_45(x),
        l328_46(x),
        l328_47(x),
        l328_48(x),
        l328_49(x),
        l328_50(x),
        l328_51(x),
        l328_52(x),
        l328_53(x),
        l328_54(x),
        l328_55(x),
        l328_56(x),
        l328_57(x),
        l328_58(x),
        l328_59(x),
        l328_60(x),
        l328_61(x),
        l328_62(x),
        l328_63(x),
        l328_64(x),
        l328_65(x),
        l328_66(x),
        l328_67(x),
        l328_68(x),
        l328_69(x),
        l328_70(x),
        l328_71(x),
        l328_72(x),
        l328_73(x),
        l328_74(x),
        l328_75(x),
        l328_76(x),
        l328_77(x),
        l328_78(x),
        l328_79(x),
        l328_80(x),
        l328_81(x),
        l328_82(x),
        l328_83(x),
        l328_84(x),
        l328_85(x),
        l328_86(x),
        l328_87(x),
        l328_88(x),
        l328_89(x),
        l328_90(x),
        l328_91(x),
        l328_92(x),
        l328_93(x),
        l328_94(x),
        l328_95(x),
        l328_96(x),
        l328_97(x),
        l328_98(x),
        l328_99(x),
        l328_100(x),
        l328_101(x),
        l328_102(x),
        l328_103(x),
        l328_104(x),
        l328_105(x),
        l328_106(x),
        l328_107(x),
        l328_108(x),
        l328_109(x),
        l328_110(x),
        l328_111(x),
        l328_112(x),
        l328_113(x),
        l328_114(x),
        l328_115(x),
        l328_116(x),
        l328_117(x),
        l328_118(x),
        l328_119(x),
        l328_120(x),
        l328_121(x),
        l328_122(x),
        l328_123(x),
        l328_124(x),
        l328_125(x),
        l328_126(x),
        l328_127(x),
        l328_128(x),
        l328_129(x),
        l328_130(x),
        l328_131(x),
        l328_132(x),
        l328_133(x),
        l328_134(x),
        l328_135(x),
        l328_136(x),
        l328_137(x),
        l328_138(x),
        l328_139(x),
        l328_140(x),
        l328_141(x),
        l328_142(x),
        l328_143(x),
        l328_144(x),
        l328_145(x),
        l328_146(x),
        l328_147(x),
        l328_148(x),
        l328_149(x),
        l328_150(x),
        l328_151(x),
        l328_152(x),
        l328_153(x),
        l328_154(x),
        l328_155(x),
        l328_156(x),
        l328_157(x),
        l328_158(x),
        l328_159(x),
        l328_160(x),
        l328_161(x),
        l328_162(x),
        l328_163(x),
        l328_164(x),
        l328_165(x),
        l328_166(x),
        l328_167(x),
        l328_168(x),
        l328_169(x),
        l328_170(x),
        l328_171(x),
        l328_172(x),
        l328_173(x),
        l328_174(x),
        l328_175(x),
        l328_176(x),
        l328_177(x),
        l328_178(x),
        l328_179(x),
        l328_180(x),
        l328_181(x),
        l328_182(x),
        l328_183(x),
        l328_184(x),
        l328_185(x),
        l328_186(x),
        l328_187(x),
        l328_188(x),
        l328_189(x),
        l328_190(x),
        l328_191(x),
        l328_192(x),
        l328_193(x),
        l328_194(x),
        l328_195(x),
        l328_196(x),
        l328_197(x),
        l328_198(x),
        l328_199(x),
        l328_200(x),
        l328_201(x),
        l328_202(x),
        l328_203(x),
        l328_204(x),
        l328_205(x),
        l328_206(x),
        l328_207(x),
        l328_208(x),
        l328_209(x),
        l328_210(x),
        l328_211(x),
        l328_212(x),
        l328_213(x),
        l328_214(x),
        l328_215(x),
        l328_216(x),
        l328_217(x),
        l328_218(x),
        l328_219(x),
        l328_220(x),
        l328_221(x),
        l328_222(x),
        l328_223(x),
        l328_224(x),
        l328_225(x),
        l328_226(x),
        l328_227(x),
        l328_228(x),
        l328_229(x),
        l328_230(x),
        l328_231(x),
        l328_232(x),
        l328_233(x),
        l328_234(x),
        l328_235(x),
        l328_236(x),
        l328_237(x),
        l328_238(x),
        l328_239(x),
        l328_240(x),
        l328_241(x),
        l328_242(x),
        l328_243(x),
        l328_244(x),
        l328_245(x),
        l328_246(x),
        l328_247(x),
        l328_248(x),
        l328_249(x),
        l328_250(x),
        l328_251(x),
        l328_252(x),
        l328_253(x),
        l328_254(x),
        l328_255(x),
        l328_256(x),
        l328_257(x),
        l328_258(x),
        l328_259(x),
        l328_260(x),
        l328_261(x),
        l328_262(x),
        l328_263(x),
        l328_264(x),
        l328_265(x),
        l328_266(x),
        l328_267(x),
        l328_268(x),
        l328_269(x),
        l328_270(x),
        l328_271(x),
        l328_272(x),
        l328_273(x),
        l328_274(x),
        l328_275(x),
        l328_276(x),
        l328_277(x),
        l328_278(x),
        l328_279(x),
        l328_280(x),
        l328_281(x),
        l328_282(x),
        l328_283(x),
        l328_284(x),
        l328_285(x),
        l328_286(x),
        l328_287(x),
    ]