import numpy as np




# Generated from reverse engineering
def l80_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 288
    out = np.empty(288, dtype=np.float32)
    
    # for i in range(0, 100):
    for i in range(0, 100):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xfffffff (len=28)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(100, 128):
    for i in range(0, 28):
        s = -1 * x[100 + i] + -1 * x[128 + i]
        s += biases[i]
        out[100 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 132):
    for i in range(0, 4):
        s = x[184 + i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(132, 160):
    for i in range(0, 28):
        s = x[156 + i]
        out[132 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 288):
    for i in range(0, 128):
        s = x[188 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l80_0(x):
    # x is a list (or vector) of length 316
    return max(0, x[0])
def l80_1(x):
    # x is a list (or vector) of length 316
    return max(0, x[1])
def l80_2(x):
    # x is a list (or vector) of length 316
    return max(0, x[2])
def l80_3(x):
    # x is a list (or vector) of length 316
    return max(0, x[3])
def l80_4(x):
    # x is a list (or vector) of length 316
    return max(0, x[4])
def l80_5(x):
    # x is a list (or vector) of length 316
    return max(0, x[5])
def l80_6(x):
    # x is a list (or vector) of length 316
    return max(0, x[6])
def l80_7(x):
    # x is a list (or vector) of length 316
    return max(0, x[7])
def l80_8(x):
    # x is a list (or vector) of length 316
    return max(0, x[8])
def l80_9(x):
    # x is a list (or vector) of length 316
    return max(0, x[9])
def l80_10(x):
    # x is a list (or vector) of length 316
    return max(0, x[10])
def l80_11(x):
    # x is a list (or vector) of length 316
    return max(0, x[11])
def l80_12(x):
    # x is a list (or vector) of length 316
    return max(0, x[12])
def l80_13(x):
    # x is a list (or vector) of length 316
    return max(0, x[13])
def l80_14(x):
    # x is a list (or vector) of length 316
    return max(0, x[14])
def l80_15(x):
    # x is a list (or vector) of length 316
    return max(0, x[15])
def l80_16(x):
    # x is a list (or vector) of length 316
    return max(0, x[16])
def l80_17(x):
    # x is a list (or vector) of length 316
    return max(0, x[17])
def l80_18(x):
    # x is a list (or vector) of length 316
    return max(0, x[18])
def l80_19(x):
    # x is a list (or vector) of length 316
    return max(0, x[19])
def l80_20(x):
    # x is a list (or vector) of length 316
    return max(0, x[20])
def l80_21(x):
    # x is a list (or vector) of length 316
    return max(0, x[21])
def l80_22(x):
    # x is a list (or vector) of length 316
    return max(0, x[22])
def l80_23(x):
    # x is a list (or vector) of length 316
    return max(0, x[23])
def l80_24(x):
    # x is a list (or vector) of length 316
    return max(0, x[24])
def l80_25(x):
    # x is a list (or vector) of length 316
    return max(0, x[25])
def l80_26(x):
    # x is a list (or vector) of length 316
    return max(0, x[26])
def l80_27(x):
    # x is a list (or vector) of length 316
    return max(0, x[27])
def l80_28(x):
    # x is a list (or vector) of length 316
    return max(0, x[28])
def l80_29(x):
    # x is a list (or vector) of length 316
    return max(0, x[29])
def l80_30(x):
    # x is a list (or vector) of length 316
    return max(0, x[30])
def l80_31(x):
    # x is a list (or vector) of length 316
    return max(0, x[31])
def l80_32(x):
    # x is a list (or vector) of length 316
    return max(0, x[32])
def l80_33(x):
    # x is a list (or vector) of length 316
    return max(0, x[33])
def l80_34(x):
    # x is a list (or vector) of length 316
    return max(0, x[34])
def l80_35(x):
    # x is a list (or vector) of length 316
    return max(0, x[35])
def l80_36(x):
    # x is a list (or vector) of length 316
    return max(0, x[36])
def l80_37(x):
    # x is a list (or vector) of length 316
    return max(0, x[37])
def l80_38(x):
    # x is a list (or vector) of length 316
    return max(0, x[38])
def l80_39(x):
    # x is a list (or vector) of length 316
    return max(0, x[39])
def l80_40(x):
    # x is a list (or vector) of length 316
    return max(0, x[40])
def l80_41(x):
    # x is a list (or vector) of length 316
    return max(0, x[41])
def l80_42(x):
    # x is a list (or vector) of length 316
    return max(0, x[42])
def l80_43(x):
    # x is a list (or vector) of length 316
    return max(0, x[43])
def l80_44(x):
    # x is a list (or vector) of length 316
    return max(0, x[44])
def l80_45(x):
    # x is a list (or vector) of length 316
    return max(0, x[45])
def l80_46(x):
    # x is a list (or vector) of length 316
    return max(0, x[46])
def l80_47(x):
    # x is a list (or vector) of length 316
    return max(0, x[47])
def l80_48(x):
    # x is a list (or vector) of length 316
    return max(0, x[48])
def l80_49(x):
    # x is a list (or vector) of length 316
    return max(0, x[49])
def l80_50(x):
    # x is a list (or vector) of length 316
    return max(0, x[50])
def l80_51(x):
    # x is a list (or vector) of length 316
    return max(0, x[51])
def l80_52(x):
    # x is a list (or vector) of length 316
    return max(0, x[52])
def l80_53(x):
    # x is a list (or vector) of length 316
    return max(0, x[53])
def l80_54(x):
    # x is a list (or vector) of length 316
    return max(0, x[54])
def l80_55(x):
    # x is a list (or vector) of length 316
    return max(0, x[55])
def l80_56(x):
    # x is a list (or vector) of length 316
    return max(0, x[56])
def l80_57(x):
    # x is a list (or vector) of length 316
    return max(0, x[57])
def l80_58(x):
    # x is a list (or vector) of length 316
    return max(0, x[58])
def l80_59(x):
    # x is a list (or vector) of length 316
    return max(0, x[59])
def l80_60(x):
    # x is a list (or vector) of length 316
    return max(0, x[60])
def l80_61(x):
    # x is a list (or vector) of length 316
    return max(0, x[61])
def l80_62(x):
    # x is a list (or vector) of length 316
    return max(0, x[62])
def l80_63(x):
    # x is a list (or vector) of length 316
    return max(0, x[63])
def l80_64(x):
    # x is a list (or vector) of length 316
    return max(0, x[64])
def l80_65(x):
    # x is a list (or vector) of length 316
    return max(0, x[65])
def l80_66(x):
    # x is a list (or vector) of length 316
    return max(0, x[66])
def l80_67(x):
    # x is a list (or vector) of length 316
    return max(0, x[67])
def l80_68(x):
    # x is a list (or vector) of length 316
    return max(0, x[68])
def l80_69(x):
    # x is a list (or vector) of length 316
    return max(0, x[69])
def l80_70(x):
    # x is a list (or vector) of length 316
    return max(0, x[70])
def l80_71(x):
    # x is a list (or vector) of length 316
    return max(0, x[71])
def l80_72(x):
    # x is a list (or vector) of length 316
    return max(0, x[72])
def l80_73(x):
    # x is a list (or vector) of length 316
    return max(0, x[73])
def l80_74(x):
    # x is a list (or vector) of length 316
    return max(0, x[74])
def l80_75(x):
    # x is a list (or vector) of length 316
    return max(0, x[75])
def l80_76(x):
    # x is a list (or vector) of length 316
    return max(0, x[76])
def l80_77(x):
    # x is a list (or vector) of length 316
    return max(0, x[77])
def l80_78(x):
    # x is a list (or vector) of length 316
    return max(0, x[78])
def l80_79(x):
    # x is a list (or vector) of length 316
    return max(0, x[79])
def l80_80(x):
    # x is a list (or vector) of length 316
    return max(0, x[80])
def l80_81(x):
    # x is a list (or vector) of length 316
    return max(0, x[81])
def l80_82(x):
    # x is a list (or vector) of length 316
    return max(0, x[82])
def l80_83(x):
    # x is a list (or vector) of length 316
    return max(0, x[83])
def l80_84(x):
    # x is a list (or vector) of length 316
    return max(0, x[84])
def l80_85(x):
    # x is a list (or vector) of length 316
    return max(0, x[85])
def l80_86(x):
    # x is a list (or vector) of length 316
    return max(0, x[86])
def l80_87(x):
    # x is a list (or vector) of length 316
    return max(0, x[87])
def l80_88(x):
    # x is a list (or vector) of length 316
    return max(0, x[88])
def l80_89(x):
    # x is a list (or vector) of length 316
    return max(0, x[89])
def l80_90(x):
    # x is a list (or vector) of length 316
    return max(0, x[90])
def l80_91(x):
    # x is a list (or vector) of length 316
    return max(0, x[91])
def l80_92(x):
    # x is a list (or vector) of length 316
    return max(0, x[92])
def l80_93(x):
    # x is a list (or vector) of length 316
    return max(0, x[93])
def l80_94(x):
    # x is a list (or vector) of length 316
    return max(0, x[94])
def l80_95(x):
    # x is a list (or vector) of length 316
    return max(0, x[95])
def l80_96(x):
    # x is a list (or vector) of length 316
    return max(0, x[96])
def l80_97(x):
    # x is a list (or vector) of length 316
    return max(0, x[97])
def l80_98(x):
    # x is a list (or vector) of length 316
    return max(0, x[98])
def l80_99(x):
    # x is a list (or vector) of length 316
    return max(0, x[99])
def l80_100(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[100] + -1.0*x[128] + 1.0)
def l80_101(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[101] + -1.0*x[129] + 1.0)
def l80_102(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[102] + -1.0*x[130] + 1.0)
def l80_103(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[103] + -1.0*x[131] + 1.0)
def l80_104(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[104] + -1.0*x[132] + 1.0)
def l80_105(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[105] + -1.0*x[133] + 1.0)
def l80_106(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[106] + -1.0*x[134] + 1.0)
def l80_107(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[107] + -1.0*x[135] + 1.0)
def l80_108(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[108] + -1.0*x[136] + 1.0)
def l80_109(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[109] + -1.0*x[137] + 1.0)
def l80_110(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[110] + -1.0*x[138] + 1.0)
def l80_111(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[111] + -1.0*x[139] + 1.0)
def l80_112(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[112] + -1.0*x[140] + 1.0)
def l80_113(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[113] + -1.0*x[141] + 1.0)
def l80_114(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[114] + -1.0*x[142] + 1.0)
def l80_115(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[115] + -1.0*x[143] + 1.0)
def l80_116(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[116] + -1.0*x[144] + 1.0)
def l80_117(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[117] + -1.0*x[145] + 1.0)
def l80_118(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[118] + -1.0*x[146] + 1.0)
def l80_119(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[119] + -1.0*x[147] + 1.0)
def l80_120(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[120] + -1.0*x[148] + 1.0)
def l80_121(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[121] + -1.0*x[149] + 1.0)
def l80_122(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[122] + -1.0*x[150] + 1.0)
def l80_123(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[123] + -1.0*x[151] + 1.0)
def l80_124(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[124] + -1.0*x[152] + 1.0)
def l80_125(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[125] + -1.0*x[153] + 1.0)
def l80_126(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[126] + -1.0*x[154] + 1.0)
def l80_127(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[127] + -1.0*x[155] + 1.0)
def l80_128(x):
    # x is a list (or vector) of length 316
    return max(0, x[184])
def l80_129(x):
    # x is a list (or vector) of length 316
    return max(0, x[185])
def l80_130(x):
    # x is a list (or vector) of length 316
    return max(0, x[186])
def l80_131(x):
    # x is a list (or vector) of length 316
    return max(0, x[187])
def l80_132(x):
    # x is a list (or vector) of length 316
    return max(0, x[156])
def l80_133(x):
    # x is a list (or vector) of length 316
    return max(0, x[157])
def l80_134(x):
    # x is a list (or vector) of length 316
    return max(0, x[158])
def l80_135(x):
    # x is a list (or vector) of length 316
    return max(0, x[159])
def l80_136(x):
    # x is a list (or vector) of length 316
    return max(0, x[160])
def l80_137(x):
    # x is a list (or vector) of length 316
    return max(0, x[161])
def l80_138(x):
    # x is a list (or vector) of length 316
    return max(0, x[162])
def l80_139(x):
    # x is a list (or vector) of length 316
    return max(0, x[163])
def l80_140(x):
    # x is a list (or vector) of length 316
    return max(0, x[164])
def l80_141(x):
    # x is a list (or vector) of length 316
    return max(0, x[165])
def l80_142(x):
    # x is a list (or vector) of length 316
    return max(0, x[166])
def l80_143(x):
    # x is a list (or vector) of length 316
    return max(0, x[167])
def l80_144(x):
    # x is a list (or vector) of length 316
    return max(0, x[168])
def l80_145(x):
    # x is a list (or vector) of length 316
    return max(0, x[169])
def l80_146(x):
    # x is a list (or vector) of length 316
    return max(0, x[170])
def l80_147(x):
    # x is a list (or vector) of length 316
    return max(0, x[171])
def l80_148(x):
    # x is a list (or vector) of length 316
    return max(0, x[172])
def l80_149(x):
    # x is a list (or vector) of length 316
    return max(0, x[173])
def l80_150(x):
    # x is a list (or vector) of length 316
    return max(0, x[174])
def l80_151(x):
    # x is a list (or vector) of length 316
    return max(0, x[175])
def l80_152(x):
    # x is a list (or vector) of length 316
    return max(0, x[176])
def l80_153(x):
    # x is a list (or vector) of length 316
    return max(0, x[177])
def l80_154(x):
    # x is a list (or vector) of length 316
    return max(0, x[178])
def l80_155(x):
    # x is a list (or vector) of length 316
    return max(0, x[179])
def l80_156(x):
    # x is a list (or vector) of length 316
    return max(0, x[180])
def l80_157(x):
    # x is a list (or vector) of length 316
    return max(0, x[181])
def l80_158(x):
    # x is a list (or vector) of length 316
    return max(0, x[182])
def l80_159(x):
    # x is a list (or vector) of length 316
    return max(0, x[183])
def l80_160(x):
    # x is a list (or vector) of length 316
    return max(0, x[188])
def l80_161(x):
    # x is a list (or vector) of length 316
    return max(0, x[189])
def l80_162(x):
    # x is a list (or vector) of length 316
    return max(0, x[190])
def l80_163(x):
    # x is a list (or vector) of length 316
    return max(0, x[191])
def l80_164(x):
    # x is a list (or vector) of length 316
    return max(0, x[192])
def l80_165(x):
    # x is a list (or vector) of length 316
    return max(0, x[193])
def l80_166(x):
    # x is a list (or vector) of length 316
    return max(0, x[194])
def l80_167(x):
    # x is a list (or vector) of length 316
    return max(0, x[195])
def l80_168(x):
    # x is a list (or vector) of length 316
    return max(0, x[196])
def l80_169(x):
    # x is a list (or vector) of length 316
    return max(0, x[197])
def l80_170(x):
    # x is a list (or vector) of length 316
    return max(0, x[198])
def l80_171(x):
    # x is a list (or vector) of length 316
    return max(0, x[199])
def l80_172(x):
    # x is a list (or vector) of length 316
    return max(0, x[200])
def l80_173(x):
    # x is a list (or vector) of length 316
    return max(0, x[201])
def l80_174(x):
    # x is a list (or vector) of length 316
    return max(0, x[202])
def l80_175(x):
    # x is a list (or vector) of length 316
    return max(0, x[203])
def l80_176(x):
    # x is a list (or vector) of length 316
    return max(0, x[204])
def l80_177(x):
    # x is a list (or vector) of length 316
    return max(0, x[205])
def l80_178(x):
    # x is a list (or vector) of length 316
    return max(0, x[206])
def l80_179(x):
    # x is a list (or vector) of length 316
    return max(0, x[207])
def l80_180(x):
    # x is a list (or vector) of length 316
    return max(0, x[208])
def l80_181(x):
    # x is a list (or vector) of length 316
    return max(0, x[209])
def l80_182(x):
    # x is a list (or vector) of length 316
    return max(0, x[210])
def l80_183(x):
    # x is a list (or vector) of length 316
    return max(0, x[211])
def l80_184(x):
    # x is a list (or vector) of length 316
    return max(0, x[212])
def l80_185(x):
    # x is a list (or vector) of length 316
    return max(0, x[213])
def l80_186(x):
    # x is a list (or vector) of length 316
    return max(0, x[214])
def l80_187(x):
    # x is a list (or vector) of length 316
    return max(0, x[215])
def l80_188(x):
    # x is a list (or vector) of length 316
    return max(0, x[216])
def l80_189(x):
    # x is a list (or vector) of length 316
    return max(0, x[217])
def l80_190(x):
    # x is a list (or vector) of length 316
    return max(0, x[218])
def l80_191(x):
    # x is a list (or vector) of length 316
    return max(0, x[219])
def l80_192(x):
    # x is a list (or vector) of length 316
    return max(0, x[220])
def l80_193(x):
    # x is a list (or vector) of length 316
    return max(0, x[221])
def l80_194(x):
    # x is a list (or vector) of length 316
    return max(0, x[222])
def l80_195(x):
    # x is a list (or vector) of length 316
    return max(0, x[223])
def l80_196(x):
    # x is a list (or vector) of length 316
    return max(0, x[224])
def l80_197(x):
    # x is a list (or vector) of length 316
    return max(0, x[225])
def l80_198(x):
    # x is a list (or vector) of length 316
    return max(0, x[226])
def l80_199(x):
    # x is a list (or vector) of length 316
    return max(0, x[227])
def l80_200(x):
    # x is a list (or vector) of length 316
    return max(0, x[228])
def l80_201(x):
    # x is a list (or vector) of length 316
    return max(0, x[229])
def l80_202(x):
    # x is a list (or vector) of length 316
    return max(0, x[230])
def l80_203(x):
    # x is a list (or vector) of length 316
    return max(0, x[231])
def l80_204(x):
    # x is a list (or vector) of length 316
    return max(0, x[232])
def l80_205(x):
    # x is a list (or vector) of length 316
    return max(0, x[233])
def l80_206(x):
    # x is a list (or vector) of length 316
    return max(0, x[234])
def l80_207(x):
    # x is a list (or vector) of length 316
    return max(0, x[235])
def l80_208(x):
    # x is a list (or vector) of length 316
    return max(0, x[236])
def l80_209(x):
    # x is a list (or vector) of length 316
    return max(0, x[237])
def l80_210(x):
    # x is a list (or vector) of length 316
    return max(0, x[238])
def l80_211(x):
    # x is a list (or vector) of length 316
    return max(0, x[239])
def l80_212(x):
    # x is a list (or vector) of length 316
    return max(0, x[240])
def l80_213(x):
    # x is a list (or vector) of length 316
    return max(0, x[241])
def l80_214(x):
    # x is a list (or vector) of length 316
    return max(0, x[242])
def l80_215(x):
    # x is a list (or vector) of length 316
    return max(0, x[243])
def l80_216(x):
    # x is a list (or vector) of length 316
    return max(0, x[244])
def l80_217(x):
    # x is a list (or vector) of length 316
    return max(0, x[245])
def l80_218(x):
    # x is a list (or vector) of length 316
    return max(0, x[246])
def l80_219(x):
    # x is a list (or vector) of length 316
    return max(0, x[247])
def l80_220(x):
    # x is a list (or vector) of length 316
    return max(0, x[248])
def l80_221(x):
    # x is a list (or vector) of length 316
    return max(0, x[249])
def l80_222(x):
    # x is a list (or vector) of length 316
    return max(0, x[250])
def l80_223(x):
    # x is a list (or vector) of length 316
    return max(0, x[251])
def l80_224(x):
    # x is a list (or vector) of length 316
    return max(0, x[252])
def l80_225(x):
    # x is a list (or vector) of length 316
    return max(0, x[253])
def l80_226(x):
    # x is a list (or vector) of length 316
    return max(0, x[254])
def l80_227(x):
    # x is a list (or vector) of length 316
    return max(0, x[255])
def l80_228(x):
    # x is a list (or vector) of length 316
    return max(0, x[256])
def l80_229(x):
    # x is a list (or vector) of length 316
    return max(0, x[257])
def l80_230(x):
    # x is a list (or vector) of length 316
    return max(0, x[258])
def l80_231(x):
    # x is a list (or vector) of length 316
    return max(0, x[259])
def l80_232(x):
    # x is a list (or vector) of length 316
    return max(0, x[260])
def l80_233(x):
    # x is a list (or vector) of length 316
    return max(0, x[261])
def l80_234(x):
    # x is a list (or vector) of length 316
    return max(0, x[262])
def l80_235(x):
    # x is a list (or vector) of length 316
    return max(0, x[263])
def l80_236(x):
    # x is a list (or vector) of length 316
    return max(0, x[264])
def l80_237(x):
    # x is a list (or vector) of length 316
    return max(0, x[265])
def l80_238(x):
    # x is a list (or vector) of length 316
    return max(0, x[266])
def l80_239(x):
    # x is a list (or vector) of length 316
    return max(0, x[267])
def l80_240(x):
    # x is a list (or vector) of length 316
    return max(0, x[268])
def l80_241(x):
    # x is a list (or vector) of length 316
    return max(0, x[269])
def l80_242(x):
    # x is a list (or vector) of length 316
    return max(0, x[270])
def l80_243(x):
    # x is a list (or vector) of length 316
    return max(0, x[271])
def l80_244(x):
    # x is a list (or vector) of length 316
    return max(0, x[272])
def l80_245(x):
    # x is a list (or vector) of length 316
    return max(0, x[273])
def l80_246(x):
    # x is a list (or vector) of length 316
    return max(0, x[274])
def l80_247(x):
    # x is a list (or vector) of length 316
    return max(0, x[275])
def l80_248(x):
    # x is a list (or vector) of length 316
    return max(0, x[276])
def l80_249(x):
    # x is a list (or vector) of length 316
    return max(0, x[277])
def l80_250(x):
    # x is a list (or vector) of length 316
    return max(0, x[278])
def l80_251(x):
    # x is a list (or vector) of length 316
    return max(0, x[279])
def l80_252(x):
    # x is a list (or vector) of length 316
    return max(0, x[280])
def l80_253(x):
    # x is a list (or vector) of length 316
    return max(0, x[281])
def l80_254(x):
    # x is a list (or vector) of length 316
    return max(0, x[282])
def l80_255(x):
    # x is a list (or vector) of length 316
    return max(0, x[283])
def l80_256(x):
    # x is a list (or vector) of length 316
    return max(0, x[284])
def l80_257(x):
    # x is a list (or vector) of length 316
    return max(0, x[285])
def l80_258(x):
    # x is a list (or vector) of length 316
    return max(0, x[286])
def l80_259(x):
    # x is a list (or vector) of length 316
    return max(0, x[287])
def l80_260(x):
    # x is a list (or vector) of length 316
    return max(0, x[288])
def l80_261(x):
    # x is a list (or vector) of length 316
    return max(0, x[289])
def l80_262(x):
    # x is a list (or vector) of length 316
    return max(0, x[290])
def l80_263(x):
    # x is a list (or vector) of length 316
    return max(0, x[291])
def l80_264(x):
    # x is a list (or vector) of length 316
    return max(0, x[292])
def l80_265(x):
    # x is a list (or vector) of length 316
    return max(0, x[293])
def l80_266(x):
    # x is a list (or vector) of length 316
    return max(0, x[294])
def l80_267(x):
    # x is a list (or vector) of length 316
    return max(0, x[295])
def l80_268(x):
    # x is a list (or vector) of length 316
    return max(0, x[296])
def l80_269(x):
    # x is a list (or vector) of length 316
    return max(0, x[297])
def l80_270(x):
    # x is a list (or vector) of length 316
    return max(0, x[298])
def l80_271(x):
    # x is a list (or vector) of length 316
    return max(0, x[299])
def l80_272(x):
    # x is a list (or vector) of length 316
    return max(0, x[300])
def l80_273(x):
    # x is a list (or vector) of length 316
    return max(0, x[301])
def l80_274(x):
    # x is a list (or vector) of length 316
    return max(0, x[302])
def l80_275(x):
    # x is a list (or vector) of length 316
    return max(0, x[303])
def l80_276(x):
    # x is a list (or vector) of length 316
    return max(0, x[304])
def l80_277(x):
    # x is a list (or vector) of length 316
    return max(0, x[305])
def l80_278(x):
    # x is a list (or vector) of length 316
    return max(0, x[306])
def l80_279(x):
    # x is a list (or vector) of length 316
    return max(0, x[307])
def l80_280(x):
    # x is a list (or vector) of length 316
    return max(0, x[308])
def l80_281(x):
    # x is a list (or vector) of length 316
    return max(0, x[309])
def l80_282(x):
    # x is a list (or vector) of length 316
    return max(0, x[310])
def l80_283(x):
    # x is a list (or vector) of length 316
    return max(0, x[311])
def l80_284(x):
    # x is a list (or vector) of length 316
    return max(0, x[312])
def l80_285(x):
    # x is a list (or vector) of length 316
    return max(0, x[313])
def l80_286(x):
    # x is a list (or vector) of length 316
    return max(0, x[314])
def l80_287(x):
    # x is a list (or vector) of length 316
    return max(0, x[315])
def l80_(x):
    # x is a list (or vector) of length 316
    return [
        l80_0(x),
        l80_1(x),
        l80_2(x),
        l80_3(x),
        l80_4(x),
        l80_5(x),
        l80_6(x),
        l80_7(x),
        l80_8(x),
        l80_9(x),
        l80_10(x),
        l80_11(x),
        l80_12(x),
        l80_13(x),
        l80_14(x),
        l80_15(x),
        l80_16(x),
        l80_17(x),
        l80_18(x),
        l80_19(x),
        l80_20(x),
        l80_21(x),
        l80_22(x),
        l80_23(x),
        l80_24(x),
        l80_25(x),
        l80_26(x),
        l80_27(x),
        l80_28(x),
        l80_29(x),
        l80_30(x),
        l80_31(x),
        l80_32(x),
        l80_33(x),
        l80_34(x),
        l80_35(x),
        l80_36(x),
        l80_37(x),
        l80_38(x),
        l80_39(x),
        l80_40(x),
        l80_41(x),
        l80_42(x),
        l80_43(x),
        l80_44(x),
        l80_45(x),
        l80_46(x),
        l80_47(x),
        l80_48(x),
        l80_49(x),
        l80_50(x),
        l80_51(x),
        l80_52(x),
        l80_53(x),
        l80_54(x),
        l80_55(x),
        l80_56(x),
        l80_57(x),
        l80_58(x),
        l80_59(x),
        l80_60(x),
        l80_61(x),
        l80_62(x),
        l80_63(x),
        l80_64(x),
        l80_65(x),
        l80_66(x),
        l80_67(x),
        l80_68(x),
        l80_69(x),
        l80_70(x),
        l80_71(x),
        l80_72(x),
        l80_73(x),
        l80_74(x),
        l80_75(x),
        l80_76(x),
        l80_77(x),
        l80_78(x),
        l80_79(x),
        l80_80(x),
        l80_81(x),
        l80_82(x),
        l80_83(x),
        l80_84(x),
        l80_85(x),
        l80_86(x),
        l80_87(x),
        l80_88(x),
        l80_89(x),
        l80_90(x),
        l80_91(x),
        l80_92(x),
        l80_93(x),
        l80_94(x),
        l80_95(x),
        l80_96(x),
        l80_97(x),
        l80_98(x),
        l80_99(x),
        l80_100(x),
        l80_101(x),
        l80_102(x),
        l80_103(x),
        l80_104(x),
        l80_105(x),
        l80_106(x),
        l80_107(x),
        l80_108(x),
        l80_109(x),
        l80_110(x),
        l80_111(x),
        l80_112(x),
        l80_113(x),
        l80_114(x),
        l80_115(x),
        l80_116(x),
        l80_117(x),
        l80_118(x),
        l80_119(x),
        l80_120(x),
        l80_121(x),
        l80_122(x),
        l80_123(x),
        l80_124(x),
        l80_125(x),
        l80_126(x),
        l80_127(x),
        l80_128(x),
        l80_129(x),
        l80_130(x),
        l80_131(x),
        l80_132(x),
        l80_133(x),
        l80_134(x),
        l80_135(x),
        l80_136(x),
        l80_137(x),
        l80_138(x),
        l80_139(x),
        l80_140(x),
        l80_141(x),
        l80_142(x),
        l80_143(x),
        l80_144(x),
        l80_145(x),
        l80_146(x),
        l80_147(x),
        l80_148(x),
        l80_149(x),
        l80_150(x),
        l80_151(x),
        l80_152(x),
        l80_153(x),
        l80_154(x),
        l80_155(x),
        l80_156(x),
        l80_157(x),
        l80_158(x),
        l80_159(x),
        l80_160(x),
        l80_161(x),
        l80_162(x),
        l80_163(x),
        l80_164(x),
        l80_165(x),
        l80_166(x),
        l80_167(x),
        l80_168(x),
        l80_169(x),
        l80_170(x),
        l80_171(x),
        l80_172(x),
        l80_173(x),
        l80_174(x),
        l80_175(x),
        l80_176(x),
        l80_177(x),
        l80_178(x),
        l80_179(x),
        l80_180(x),
        l80_181(x),
        l80_182(x),
        l80_183(x),
        l80_184(x),
        l80_185(x),
        l80_186(x),
        l80_187(x),
        l80_188(x),
        l80_189(x),
        l80_190(x),
        l80_191(x),
        l80_192(x),
        l80_193(x),
        l80_194(x),
        l80_195(x),
        l80_196(x),
        l80_197(x),
        l80_198(x),
        l80_199(x),
        l80_200(x),
        l80_201(x),
        l80_202(x),
        l80_203(x),
        l80_204(x),
        l80_205(x),
        l80_206(x),
        l80_207(x),
        l80_208(x),
        l80_209(x),
        l80_210(x),
        l80_211(x),
        l80_212(x),
        l80_213(x),
        l80_214(x),
        l80_215(x),
        l80_216(x),
        l80_217(x),
        l80_218(x),
        l80_219(x),
        l80_220(x),
        l80_221(x),
        l80_222(x),
        l80_223(x),
        l80_224(x),
        l80_225(x),
        l80_226(x),
        l80_227(x),
        l80_228(x),
        l80_229(x),
        l80_230(x),
        l80_231(x),
        l80_232(x),
        l80_233(x),
        l80_234(x),
        l80_235(x),
        l80_236(x),
        l80_237(x),
        l80_238(x),
        l80_239(x),
        l80_240(x),
        l80_241(x),
        l80_242(x),
        l80_243(x),
        l80_244(x),
        l80_245(x),
        l80_246(x),
        l80_247(x),
        l80_248(x),
        l80_249(x),
        l80_250(x),
        l80_251(x),
        l80_252(x),
        l80_253(x),
        l80_254(x),
        l80_255(x),
        l80_256(x),
        l80_257(x),
        l80_258(x),
        l80_259(x),
        l80_260(x),
        l80_261(x),
        l80_262(x),
        l80_263(x),
        l80_264(x),
        l80_265(x),
        l80_266(x),
        l80_267(x),
        l80_268(x),
        l80_269(x),
        l80_270(x),
        l80_271(x),
        l80_272(x),
        l80_273(x),
        l80_274(x),
        l80_275(x),
        l80_276(x),
        l80_277(x),
        l80_278(x),
        l80_279(x),
        l80_280(x),
        l80_281(x),
        l80_282(x),
        l80_283(x),
        l80_284(x),
        l80_285(x),
        l80_286(x),
        l80_287(x),
    ]