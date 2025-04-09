import numpy as np




# Generated from reverse engineering
def l416_g(x: np.ndarray) -> np.ndarray:
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




def l416_0(x):
    # x is a list (or vector) of length 316
    return max(0, x[0])
def l416_1(x):
    # x is a list (or vector) of length 316
    return max(0, x[1])
def l416_2(x):
    # x is a list (or vector) of length 316
    return max(0, x[2])
def l416_3(x):
    # x is a list (or vector) of length 316
    return max(0, x[3])
def l416_4(x):
    # x is a list (or vector) of length 316
    return max(0, x[4])
def l416_5(x):
    # x is a list (or vector) of length 316
    return max(0, x[5])
def l416_6(x):
    # x is a list (or vector) of length 316
    return max(0, x[6])
def l416_7(x):
    # x is a list (or vector) of length 316
    return max(0, x[7])
def l416_8(x):
    # x is a list (or vector) of length 316
    return max(0, x[8])
def l416_9(x):
    # x is a list (or vector) of length 316
    return max(0, x[9])
def l416_10(x):
    # x is a list (or vector) of length 316
    return max(0, x[10])
def l416_11(x):
    # x is a list (or vector) of length 316
    return max(0, x[11])
def l416_12(x):
    # x is a list (or vector) of length 316
    return max(0, x[12])
def l416_13(x):
    # x is a list (or vector) of length 316
    return max(0, x[13])
def l416_14(x):
    # x is a list (or vector) of length 316
    return max(0, x[14])
def l416_15(x):
    # x is a list (or vector) of length 316
    return max(0, x[15])
def l416_16(x):
    # x is a list (or vector) of length 316
    return max(0, x[16])
def l416_17(x):
    # x is a list (or vector) of length 316
    return max(0, x[17])
def l416_18(x):
    # x is a list (or vector) of length 316
    return max(0, x[18])
def l416_19(x):
    # x is a list (or vector) of length 316
    return max(0, x[19])
def l416_20(x):
    # x is a list (or vector) of length 316
    return max(0, x[20])
def l416_21(x):
    # x is a list (or vector) of length 316
    return max(0, x[21])
def l416_22(x):
    # x is a list (or vector) of length 316
    return max(0, x[22])
def l416_23(x):
    # x is a list (or vector) of length 316
    return max(0, x[23])
def l416_24(x):
    # x is a list (or vector) of length 316
    return max(0, x[24])
def l416_25(x):
    # x is a list (or vector) of length 316
    return max(0, x[25])
def l416_26(x):
    # x is a list (or vector) of length 316
    return max(0, x[26])
def l416_27(x):
    # x is a list (or vector) of length 316
    return max(0, x[27])
def l416_28(x):
    # x is a list (or vector) of length 316
    return max(0, x[28])
def l416_29(x):
    # x is a list (or vector) of length 316
    return max(0, x[29])
def l416_30(x):
    # x is a list (or vector) of length 316
    return max(0, x[30])
def l416_31(x):
    # x is a list (or vector) of length 316
    return max(0, x[31])
def l416_32(x):
    # x is a list (or vector) of length 316
    return max(0, x[32])
def l416_33(x):
    # x is a list (or vector) of length 316
    return max(0, x[33])
def l416_34(x):
    # x is a list (or vector) of length 316
    return max(0, x[34])
def l416_35(x):
    # x is a list (or vector) of length 316
    return max(0, x[35])
def l416_36(x):
    # x is a list (or vector) of length 316
    return max(0, x[36])
def l416_37(x):
    # x is a list (or vector) of length 316
    return max(0, x[37])
def l416_38(x):
    # x is a list (or vector) of length 316
    return max(0, x[38])
def l416_39(x):
    # x is a list (or vector) of length 316
    return max(0, x[39])
def l416_40(x):
    # x is a list (or vector) of length 316
    return max(0, x[40])
def l416_41(x):
    # x is a list (or vector) of length 316
    return max(0, x[41])
def l416_42(x):
    # x is a list (or vector) of length 316
    return max(0, x[42])
def l416_43(x):
    # x is a list (or vector) of length 316
    return max(0, x[43])
def l416_44(x):
    # x is a list (or vector) of length 316
    return max(0, x[44])
def l416_45(x):
    # x is a list (or vector) of length 316
    return max(0, x[45])
def l416_46(x):
    # x is a list (or vector) of length 316
    return max(0, x[46])
def l416_47(x):
    # x is a list (or vector) of length 316
    return max(0, x[47])
def l416_48(x):
    # x is a list (or vector) of length 316
    return max(0, x[48])
def l416_49(x):
    # x is a list (or vector) of length 316
    return max(0, x[49])
def l416_50(x):
    # x is a list (or vector) of length 316
    return max(0, x[50])
def l416_51(x):
    # x is a list (or vector) of length 316
    return max(0, x[51])
def l416_52(x):
    # x is a list (or vector) of length 316
    return max(0, x[52])
def l416_53(x):
    # x is a list (or vector) of length 316
    return max(0, x[53])
def l416_54(x):
    # x is a list (or vector) of length 316
    return max(0, x[54])
def l416_55(x):
    # x is a list (or vector) of length 316
    return max(0, x[55])
def l416_56(x):
    # x is a list (or vector) of length 316
    return max(0, x[56])
def l416_57(x):
    # x is a list (or vector) of length 316
    return max(0, x[57])
def l416_58(x):
    # x is a list (or vector) of length 316
    return max(0, x[58])
def l416_59(x):
    # x is a list (or vector) of length 316
    return max(0, x[59])
def l416_60(x):
    # x is a list (or vector) of length 316
    return max(0, x[60])
def l416_61(x):
    # x is a list (or vector) of length 316
    return max(0, x[61])
def l416_62(x):
    # x is a list (or vector) of length 316
    return max(0, x[62])
def l416_63(x):
    # x is a list (or vector) of length 316
    return max(0, x[63])
def l416_64(x):
    # x is a list (or vector) of length 316
    return max(0, x[64])
def l416_65(x):
    # x is a list (or vector) of length 316
    return max(0, x[65])
def l416_66(x):
    # x is a list (or vector) of length 316
    return max(0, x[66])
def l416_67(x):
    # x is a list (or vector) of length 316
    return max(0, x[67])
def l416_68(x):
    # x is a list (or vector) of length 316
    return max(0, x[68])
def l416_69(x):
    # x is a list (or vector) of length 316
    return max(0, x[69])
def l416_70(x):
    # x is a list (or vector) of length 316
    return max(0, x[70])
def l416_71(x):
    # x is a list (or vector) of length 316
    return max(0, x[71])
def l416_72(x):
    # x is a list (or vector) of length 316
    return max(0, x[72])
def l416_73(x):
    # x is a list (or vector) of length 316
    return max(0, x[73])
def l416_74(x):
    # x is a list (or vector) of length 316
    return max(0, x[74])
def l416_75(x):
    # x is a list (or vector) of length 316
    return max(0, x[75])
def l416_76(x):
    # x is a list (or vector) of length 316
    return max(0, x[76])
def l416_77(x):
    # x is a list (or vector) of length 316
    return max(0, x[77])
def l416_78(x):
    # x is a list (or vector) of length 316
    return max(0, x[78])
def l416_79(x):
    # x is a list (or vector) of length 316
    return max(0, x[79])
def l416_80(x):
    # x is a list (or vector) of length 316
    return max(0, x[80])
def l416_81(x):
    # x is a list (or vector) of length 316
    return max(0, x[81])
def l416_82(x):
    # x is a list (or vector) of length 316
    return max(0, x[82])
def l416_83(x):
    # x is a list (or vector) of length 316
    return max(0, x[83])
def l416_84(x):
    # x is a list (or vector) of length 316
    return max(0, x[84])
def l416_85(x):
    # x is a list (or vector) of length 316
    return max(0, x[85])
def l416_86(x):
    # x is a list (or vector) of length 316
    return max(0, x[86])
def l416_87(x):
    # x is a list (or vector) of length 316
    return max(0, x[87])
def l416_88(x):
    # x is a list (or vector) of length 316
    return max(0, x[88])
def l416_89(x):
    # x is a list (or vector) of length 316
    return max(0, x[89])
def l416_90(x):
    # x is a list (or vector) of length 316
    return max(0, x[90])
def l416_91(x):
    # x is a list (or vector) of length 316
    return max(0, x[91])
def l416_92(x):
    # x is a list (or vector) of length 316
    return max(0, x[92])
def l416_93(x):
    # x is a list (or vector) of length 316
    return max(0, x[93])
def l416_94(x):
    # x is a list (or vector) of length 316
    return max(0, x[94])
def l416_95(x):
    # x is a list (or vector) of length 316
    return max(0, x[95])
def l416_96(x):
    # x is a list (or vector) of length 316
    return max(0, x[96])
def l416_97(x):
    # x is a list (or vector) of length 316
    return max(0, x[97])
def l416_98(x):
    # x is a list (or vector) of length 316
    return max(0, x[98])
def l416_99(x):
    # x is a list (or vector) of length 316
    return max(0, x[99])
def l416_100(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[100] + -1.0*x[128] + 1.0)
def l416_101(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[101] + -1.0*x[129] + 1.0)
def l416_102(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[102] + -1.0*x[130] + 1.0)
def l416_103(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[103] + -1.0*x[131] + 1.0)
def l416_104(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[104] + -1.0*x[132] + 1.0)
def l416_105(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[105] + -1.0*x[133] + 1.0)
def l416_106(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[106] + -1.0*x[134] + 1.0)
def l416_107(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[107] + -1.0*x[135] + 1.0)
def l416_108(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[108] + -1.0*x[136] + 1.0)
def l416_109(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[109] + -1.0*x[137] + 1.0)
def l416_110(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[110] + -1.0*x[138] + 1.0)
def l416_111(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[111] + -1.0*x[139] + 1.0)
def l416_112(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[112] + -1.0*x[140] + 1.0)
def l416_113(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[113] + -1.0*x[141] + 1.0)
def l416_114(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[114] + -1.0*x[142] + 1.0)
def l416_115(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[115] + -1.0*x[143] + 1.0)
def l416_116(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[116] + -1.0*x[144] + 1.0)
def l416_117(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[117] + -1.0*x[145] + 1.0)
def l416_118(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[118] + -1.0*x[146] + 1.0)
def l416_119(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[119] + -1.0*x[147] + 1.0)
def l416_120(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[120] + -1.0*x[148] + 1.0)
def l416_121(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[121] + -1.0*x[149] + 1.0)
def l416_122(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[122] + -1.0*x[150] + 1.0)
def l416_123(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[123] + -1.0*x[151] + 1.0)
def l416_124(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[124] + -1.0*x[152] + 1.0)
def l416_125(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[125] + -1.0*x[153] + 1.0)
def l416_126(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[126] + -1.0*x[154] + 1.0)
def l416_127(x):
    # x is a list (or vector) of length 316
    return max(0, -1.0*x[127] + -1.0*x[155] + 1.0)
def l416_128(x):
    # x is a list (or vector) of length 316
    return max(0, x[184])
def l416_129(x):
    # x is a list (or vector) of length 316
    return max(0, x[185])
def l416_130(x):
    # x is a list (or vector) of length 316
    return max(0, x[186])
def l416_131(x):
    # x is a list (or vector) of length 316
    return max(0, x[187])
def l416_132(x):
    # x is a list (or vector) of length 316
    return max(0, x[156])
def l416_133(x):
    # x is a list (or vector) of length 316
    return max(0, x[157])
def l416_134(x):
    # x is a list (or vector) of length 316
    return max(0, x[158])
def l416_135(x):
    # x is a list (or vector) of length 316
    return max(0, x[159])
def l416_136(x):
    # x is a list (or vector) of length 316
    return max(0, x[160])
def l416_137(x):
    # x is a list (or vector) of length 316
    return max(0, x[161])
def l416_138(x):
    # x is a list (or vector) of length 316
    return max(0, x[162])
def l416_139(x):
    # x is a list (or vector) of length 316
    return max(0, x[163])
def l416_140(x):
    # x is a list (or vector) of length 316
    return max(0, x[164])
def l416_141(x):
    # x is a list (or vector) of length 316
    return max(0, x[165])
def l416_142(x):
    # x is a list (or vector) of length 316
    return max(0, x[166])
def l416_143(x):
    # x is a list (or vector) of length 316
    return max(0, x[167])
def l416_144(x):
    # x is a list (or vector) of length 316
    return max(0, x[168])
def l416_145(x):
    # x is a list (or vector) of length 316
    return max(0, x[169])
def l416_146(x):
    # x is a list (or vector) of length 316
    return max(0, x[170])
def l416_147(x):
    # x is a list (or vector) of length 316
    return max(0, x[171])
def l416_148(x):
    # x is a list (or vector) of length 316
    return max(0, x[172])
def l416_149(x):
    # x is a list (or vector) of length 316
    return max(0, x[173])
def l416_150(x):
    # x is a list (or vector) of length 316
    return max(0, x[174])
def l416_151(x):
    # x is a list (or vector) of length 316
    return max(0, x[175])
def l416_152(x):
    # x is a list (or vector) of length 316
    return max(0, x[176])
def l416_153(x):
    # x is a list (or vector) of length 316
    return max(0, x[177])
def l416_154(x):
    # x is a list (or vector) of length 316
    return max(0, x[178])
def l416_155(x):
    # x is a list (or vector) of length 316
    return max(0, x[179])
def l416_156(x):
    # x is a list (or vector) of length 316
    return max(0, x[180])
def l416_157(x):
    # x is a list (or vector) of length 316
    return max(0, x[181])
def l416_158(x):
    # x is a list (or vector) of length 316
    return max(0, x[182])
def l416_159(x):
    # x is a list (or vector) of length 316
    return max(0, x[183])
def l416_160(x):
    # x is a list (or vector) of length 316
    return max(0, x[188])
def l416_161(x):
    # x is a list (or vector) of length 316
    return max(0, x[189])
def l416_162(x):
    # x is a list (or vector) of length 316
    return max(0, x[190])
def l416_163(x):
    # x is a list (or vector) of length 316
    return max(0, x[191])
def l416_164(x):
    # x is a list (or vector) of length 316
    return max(0, x[192])
def l416_165(x):
    # x is a list (or vector) of length 316
    return max(0, x[193])
def l416_166(x):
    # x is a list (or vector) of length 316
    return max(0, x[194])
def l416_167(x):
    # x is a list (or vector) of length 316
    return max(0, x[195])
def l416_168(x):
    # x is a list (or vector) of length 316
    return max(0, x[196])
def l416_169(x):
    # x is a list (or vector) of length 316
    return max(0, x[197])
def l416_170(x):
    # x is a list (or vector) of length 316
    return max(0, x[198])
def l416_171(x):
    # x is a list (or vector) of length 316
    return max(0, x[199])
def l416_172(x):
    # x is a list (or vector) of length 316
    return max(0, x[200])
def l416_173(x):
    # x is a list (or vector) of length 316
    return max(0, x[201])
def l416_174(x):
    # x is a list (or vector) of length 316
    return max(0, x[202])
def l416_175(x):
    # x is a list (or vector) of length 316
    return max(0, x[203])
def l416_176(x):
    # x is a list (or vector) of length 316
    return max(0, x[204])
def l416_177(x):
    # x is a list (or vector) of length 316
    return max(0, x[205])
def l416_178(x):
    # x is a list (or vector) of length 316
    return max(0, x[206])
def l416_179(x):
    # x is a list (or vector) of length 316
    return max(0, x[207])
def l416_180(x):
    # x is a list (or vector) of length 316
    return max(0, x[208])
def l416_181(x):
    # x is a list (or vector) of length 316
    return max(0, x[209])
def l416_182(x):
    # x is a list (or vector) of length 316
    return max(0, x[210])
def l416_183(x):
    # x is a list (or vector) of length 316
    return max(0, x[211])
def l416_184(x):
    # x is a list (or vector) of length 316
    return max(0, x[212])
def l416_185(x):
    # x is a list (or vector) of length 316
    return max(0, x[213])
def l416_186(x):
    # x is a list (or vector) of length 316
    return max(0, x[214])
def l416_187(x):
    # x is a list (or vector) of length 316
    return max(0, x[215])
def l416_188(x):
    # x is a list (or vector) of length 316
    return max(0, x[216])
def l416_189(x):
    # x is a list (or vector) of length 316
    return max(0, x[217])
def l416_190(x):
    # x is a list (or vector) of length 316
    return max(0, x[218])
def l416_191(x):
    # x is a list (or vector) of length 316
    return max(0, x[219])
def l416_192(x):
    # x is a list (or vector) of length 316
    return max(0, x[220])
def l416_193(x):
    # x is a list (or vector) of length 316
    return max(0, x[221])
def l416_194(x):
    # x is a list (or vector) of length 316
    return max(0, x[222])
def l416_195(x):
    # x is a list (or vector) of length 316
    return max(0, x[223])
def l416_196(x):
    # x is a list (or vector) of length 316
    return max(0, x[224])
def l416_197(x):
    # x is a list (or vector) of length 316
    return max(0, x[225])
def l416_198(x):
    # x is a list (or vector) of length 316
    return max(0, x[226])
def l416_199(x):
    # x is a list (or vector) of length 316
    return max(0, x[227])
def l416_200(x):
    # x is a list (or vector) of length 316
    return max(0, x[228])
def l416_201(x):
    # x is a list (or vector) of length 316
    return max(0, x[229])
def l416_202(x):
    # x is a list (or vector) of length 316
    return max(0, x[230])
def l416_203(x):
    # x is a list (or vector) of length 316
    return max(0, x[231])
def l416_204(x):
    # x is a list (or vector) of length 316
    return max(0, x[232])
def l416_205(x):
    # x is a list (or vector) of length 316
    return max(0, x[233])
def l416_206(x):
    # x is a list (or vector) of length 316
    return max(0, x[234])
def l416_207(x):
    # x is a list (or vector) of length 316
    return max(0, x[235])
def l416_208(x):
    # x is a list (or vector) of length 316
    return max(0, x[236])
def l416_209(x):
    # x is a list (or vector) of length 316
    return max(0, x[237])
def l416_210(x):
    # x is a list (or vector) of length 316
    return max(0, x[238])
def l416_211(x):
    # x is a list (or vector) of length 316
    return max(0, x[239])
def l416_212(x):
    # x is a list (or vector) of length 316
    return max(0, x[240])
def l416_213(x):
    # x is a list (or vector) of length 316
    return max(0, x[241])
def l416_214(x):
    # x is a list (or vector) of length 316
    return max(0, x[242])
def l416_215(x):
    # x is a list (or vector) of length 316
    return max(0, x[243])
def l416_216(x):
    # x is a list (or vector) of length 316
    return max(0, x[244])
def l416_217(x):
    # x is a list (or vector) of length 316
    return max(0, x[245])
def l416_218(x):
    # x is a list (or vector) of length 316
    return max(0, x[246])
def l416_219(x):
    # x is a list (or vector) of length 316
    return max(0, x[247])
def l416_220(x):
    # x is a list (or vector) of length 316
    return max(0, x[248])
def l416_221(x):
    # x is a list (or vector) of length 316
    return max(0, x[249])
def l416_222(x):
    # x is a list (or vector) of length 316
    return max(0, x[250])
def l416_223(x):
    # x is a list (or vector) of length 316
    return max(0, x[251])
def l416_224(x):
    # x is a list (or vector) of length 316
    return max(0, x[252])
def l416_225(x):
    # x is a list (or vector) of length 316
    return max(0, x[253])
def l416_226(x):
    # x is a list (or vector) of length 316
    return max(0, x[254])
def l416_227(x):
    # x is a list (or vector) of length 316
    return max(0, x[255])
def l416_228(x):
    # x is a list (or vector) of length 316
    return max(0, x[256])
def l416_229(x):
    # x is a list (or vector) of length 316
    return max(0, x[257])
def l416_230(x):
    # x is a list (or vector) of length 316
    return max(0, x[258])
def l416_231(x):
    # x is a list (or vector) of length 316
    return max(0, x[259])
def l416_232(x):
    # x is a list (or vector) of length 316
    return max(0, x[260])
def l416_233(x):
    # x is a list (or vector) of length 316
    return max(0, x[261])
def l416_234(x):
    # x is a list (or vector) of length 316
    return max(0, x[262])
def l416_235(x):
    # x is a list (or vector) of length 316
    return max(0, x[263])
def l416_236(x):
    # x is a list (or vector) of length 316
    return max(0, x[264])
def l416_237(x):
    # x is a list (or vector) of length 316
    return max(0, x[265])
def l416_238(x):
    # x is a list (or vector) of length 316
    return max(0, x[266])
def l416_239(x):
    # x is a list (or vector) of length 316
    return max(0, x[267])
def l416_240(x):
    # x is a list (or vector) of length 316
    return max(0, x[268])
def l416_241(x):
    # x is a list (or vector) of length 316
    return max(0, x[269])
def l416_242(x):
    # x is a list (or vector) of length 316
    return max(0, x[270])
def l416_243(x):
    # x is a list (or vector) of length 316
    return max(0, x[271])
def l416_244(x):
    # x is a list (or vector) of length 316
    return max(0, x[272])
def l416_245(x):
    # x is a list (or vector) of length 316
    return max(0, x[273])
def l416_246(x):
    # x is a list (or vector) of length 316
    return max(0, x[274])
def l416_247(x):
    # x is a list (or vector) of length 316
    return max(0, x[275])
def l416_248(x):
    # x is a list (or vector) of length 316
    return max(0, x[276])
def l416_249(x):
    # x is a list (or vector) of length 316
    return max(0, x[277])
def l416_250(x):
    # x is a list (or vector) of length 316
    return max(0, x[278])
def l416_251(x):
    # x is a list (or vector) of length 316
    return max(0, x[279])
def l416_252(x):
    # x is a list (or vector) of length 316
    return max(0, x[280])
def l416_253(x):
    # x is a list (or vector) of length 316
    return max(0, x[281])
def l416_254(x):
    # x is a list (or vector) of length 316
    return max(0, x[282])
def l416_255(x):
    # x is a list (or vector) of length 316
    return max(0, x[283])
def l416_256(x):
    # x is a list (or vector) of length 316
    return max(0, x[284])
def l416_257(x):
    # x is a list (or vector) of length 316
    return max(0, x[285])
def l416_258(x):
    # x is a list (or vector) of length 316
    return max(0, x[286])
def l416_259(x):
    # x is a list (or vector) of length 316
    return max(0, x[287])
def l416_260(x):
    # x is a list (or vector) of length 316
    return max(0, x[288])
def l416_261(x):
    # x is a list (or vector) of length 316
    return max(0, x[289])
def l416_262(x):
    # x is a list (or vector) of length 316
    return max(0, x[290])
def l416_263(x):
    # x is a list (or vector) of length 316
    return max(0, x[291])
def l416_264(x):
    # x is a list (or vector) of length 316
    return max(0, x[292])
def l416_265(x):
    # x is a list (or vector) of length 316
    return max(0, x[293])
def l416_266(x):
    # x is a list (or vector) of length 316
    return max(0, x[294])
def l416_267(x):
    # x is a list (or vector) of length 316
    return max(0, x[295])
def l416_268(x):
    # x is a list (or vector) of length 316
    return max(0, x[296])
def l416_269(x):
    # x is a list (or vector) of length 316
    return max(0, x[297])
def l416_270(x):
    # x is a list (or vector) of length 316
    return max(0, x[298])
def l416_271(x):
    # x is a list (or vector) of length 316
    return max(0, x[299])
def l416_272(x):
    # x is a list (or vector) of length 316
    return max(0, x[300])
def l416_273(x):
    # x is a list (or vector) of length 316
    return max(0, x[301])
def l416_274(x):
    # x is a list (or vector) of length 316
    return max(0, x[302])
def l416_275(x):
    # x is a list (or vector) of length 316
    return max(0, x[303])
def l416_276(x):
    # x is a list (or vector) of length 316
    return max(0, x[304])
def l416_277(x):
    # x is a list (or vector) of length 316
    return max(0, x[305])
def l416_278(x):
    # x is a list (or vector) of length 316
    return max(0, x[306])
def l416_279(x):
    # x is a list (or vector) of length 316
    return max(0, x[307])
def l416_280(x):
    # x is a list (or vector) of length 316
    return max(0, x[308])
def l416_281(x):
    # x is a list (or vector) of length 316
    return max(0, x[309])
def l416_282(x):
    # x is a list (or vector) of length 316
    return max(0, x[310])
def l416_283(x):
    # x is a list (or vector) of length 316
    return max(0, x[311])
def l416_284(x):
    # x is a list (or vector) of length 316
    return max(0, x[312])
def l416_285(x):
    # x is a list (or vector) of length 316
    return max(0, x[313])
def l416_286(x):
    # x is a list (or vector) of length 316
    return max(0, x[314])
def l416_287(x):
    # x is a list (or vector) of length 316
    return max(0, x[315])
def l416_(x):
    # x is a list (or vector) of length 316
    return [
        l416_0(x),
        l416_1(x),
        l416_2(x),
        l416_3(x),
        l416_4(x),
        l416_5(x),
        l416_6(x),
        l416_7(x),
        l416_8(x),
        l416_9(x),
        l416_10(x),
        l416_11(x),
        l416_12(x),
        l416_13(x),
        l416_14(x),
        l416_15(x),
        l416_16(x),
        l416_17(x),
        l416_18(x),
        l416_19(x),
        l416_20(x),
        l416_21(x),
        l416_22(x),
        l416_23(x),
        l416_24(x),
        l416_25(x),
        l416_26(x),
        l416_27(x),
        l416_28(x),
        l416_29(x),
        l416_30(x),
        l416_31(x),
        l416_32(x),
        l416_33(x),
        l416_34(x),
        l416_35(x),
        l416_36(x),
        l416_37(x),
        l416_38(x),
        l416_39(x),
        l416_40(x),
        l416_41(x),
        l416_42(x),
        l416_43(x),
        l416_44(x),
        l416_45(x),
        l416_46(x),
        l416_47(x),
        l416_48(x),
        l416_49(x),
        l416_50(x),
        l416_51(x),
        l416_52(x),
        l416_53(x),
        l416_54(x),
        l416_55(x),
        l416_56(x),
        l416_57(x),
        l416_58(x),
        l416_59(x),
        l416_60(x),
        l416_61(x),
        l416_62(x),
        l416_63(x),
        l416_64(x),
        l416_65(x),
        l416_66(x),
        l416_67(x),
        l416_68(x),
        l416_69(x),
        l416_70(x),
        l416_71(x),
        l416_72(x),
        l416_73(x),
        l416_74(x),
        l416_75(x),
        l416_76(x),
        l416_77(x),
        l416_78(x),
        l416_79(x),
        l416_80(x),
        l416_81(x),
        l416_82(x),
        l416_83(x),
        l416_84(x),
        l416_85(x),
        l416_86(x),
        l416_87(x),
        l416_88(x),
        l416_89(x),
        l416_90(x),
        l416_91(x),
        l416_92(x),
        l416_93(x),
        l416_94(x),
        l416_95(x),
        l416_96(x),
        l416_97(x),
        l416_98(x),
        l416_99(x),
        l416_100(x),
        l416_101(x),
        l416_102(x),
        l416_103(x),
        l416_104(x),
        l416_105(x),
        l416_106(x),
        l416_107(x),
        l416_108(x),
        l416_109(x),
        l416_110(x),
        l416_111(x),
        l416_112(x),
        l416_113(x),
        l416_114(x),
        l416_115(x),
        l416_116(x),
        l416_117(x),
        l416_118(x),
        l416_119(x),
        l416_120(x),
        l416_121(x),
        l416_122(x),
        l416_123(x),
        l416_124(x),
        l416_125(x),
        l416_126(x),
        l416_127(x),
        l416_128(x),
        l416_129(x),
        l416_130(x),
        l416_131(x),
        l416_132(x),
        l416_133(x),
        l416_134(x),
        l416_135(x),
        l416_136(x),
        l416_137(x),
        l416_138(x),
        l416_139(x),
        l416_140(x),
        l416_141(x),
        l416_142(x),
        l416_143(x),
        l416_144(x),
        l416_145(x),
        l416_146(x),
        l416_147(x),
        l416_148(x),
        l416_149(x),
        l416_150(x),
        l416_151(x),
        l416_152(x),
        l416_153(x),
        l416_154(x),
        l416_155(x),
        l416_156(x),
        l416_157(x),
        l416_158(x),
        l416_159(x),
        l416_160(x),
        l416_161(x),
        l416_162(x),
        l416_163(x),
        l416_164(x),
        l416_165(x),
        l416_166(x),
        l416_167(x),
        l416_168(x),
        l416_169(x),
        l416_170(x),
        l416_171(x),
        l416_172(x),
        l416_173(x),
        l416_174(x),
        l416_175(x),
        l416_176(x),
        l416_177(x),
        l416_178(x),
        l416_179(x),
        l416_180(x),
        l416_181(x),
        l416_182(x),
        l416_183(x),
        l416_184(x),
        l416_185(x),
        l416_186(x),
        l416_187(x),
        l416_188(x),
        l416_189(x),
        l416_190(x),
        l416_191(x),
        l416_192(x),
        l416_193(x),
        l416_194(x),
        l416_195(x),
        l416_196(x),
        l416_197(x),
        l416_198(x),
        l416_199(x),
        l416_200(x),
        l416_201(x),
        l416_202(x),
        l416_203(x),
        l416_204(x),
        l416_205(x),
        l416_206(x),
        l416_207(x),
        l416_208(x),
        l416_209(x),
        l416_210(x),
        l416_211(x),
        l416_212(x),
        l416_213(x),
        l416_214(x),
        l416_215(x),
        l416_216(x),
        l416_217(x),
        l416_218(x),
        l416_219(x),
        l416_220(x),
        l416_221(x),
        l416_222(x),
        l416_223(x),
        l416_224(x),
        l416_225(x),
        l416_226(x),
        l416_227(x),
        l416_228(x),
        l416_229(x),
        l416_230(x),
        l416_231(x),
        l416_232(x),
        l416_233(x),
        l416_234(x),
        l416_235(x),
        l416_236(x),
        l416_237(x),
        l416_238(x),
        l416_239(x),
        l416_240(x),
        l416_241(x),
        l416_242(x),
        l416_243(x),
        l416_244(x),
        l416_245(x),
        l416_246(x),
        l416_247(x),
        l416_248(x),
        l416_249(x),
        l416_250(x),
        l416_251(x),
        l416_252(x),
        l416_253(x),
        l416_254(x),
        l416_255(x),
        l416_256(x),
        l416_257(x),
        l416_258(x),
        l416_259(x),
        l416_260(x),
        l416_261(x),
        l416_262(x),
        l416_263(x),
        l416_264(x),
        l416_265(x),
        l416_266(x),
        l416_267(x),
        l416_268(x),
        l416_269(x),
        l416_270(x),
        l416_271(x),
        l416_272(x),
        l416_273(x),
        l416_274(x),
        l416_275(x),
        l416_276(x),
        l416_277(x),
        l416_278(x),
        l416_279(x),
        l416_280(x),
        l416_281(x),
        l416_282(x),
        l416_283(x),
        l416_284(x),
        l416_285(x),
        l416_286(x),
        l416_287(x),
    ]