import numpy as np




# Generated from reverse engineering
def l76_g(x: np.ndarray) -> np.ndarray:
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




def l76_0(x):
    # x is a list (or vector) of length 318
    return max(0, x[0])
def l76_1(x):
    # x is a list (or vector) of length 318
    return max(0, x[1])
def l76_2(x):
    # x is a list (or vector) of length 318
    return max(0, x[2])
def l76_3(x):
    # x is a list (or vector) of length 318
    return max(0, x[3])
def l76_4(x):
    # x is a list (or vector) of length 318
    return max(0, x[4])
def l76_5(x):
    # x is a list (or vector) of length 318
    return max(0, x[5])
def l76_6(x):
    # x is a list (or vector) of length 318
    return max(0, x[6])
def l76_7(x):
    # x is a list (or vector) of length 318
    return max(0, x[7])
def l76_8(x):
    # x is a list (or vector) of length 318
    return max(0, x[8])
def l76_9(x):
    # x is a list (or vector) of length 318
    return max(0, x[9])
def l76_10(x):
    # x is a list (or vector) of length 318
    return max(0, x[10])
def l76_11(x):
    # x is a list (or vector) of length 318
    return max(0, x[11])
def l76_12(x):
    # x is a list (or vector) of length 318
    return max(0, x[12])
def l76_13(x):
    # x is a list (or vector) of length 318
    return max(0, x[13])
def l76_14(x):
    # x is a list (or vector) of length 318
    return max(0, x[14])
def l76_15(x):
    # x is a list (or vector) of length 318
    return max(0, x[15])
def l76_16(x):
    # x is a list (or vector) of length 318
    return max(0, x[16])
def l76_17(x):
    # x is a list (or vector) of length 318
    return max(0, x[17])
def l76_18(x):
    # x is a list (or vector) of length 318
    return max(0, x[18])
def l76_19(x):
    # x is a list (or vector) of length 318
    return max(0, x[19])
def l76_20(x):
    # x is a list (or vector) of length 318
    return max(0, x[20])
def l76_21(x):
    # x is a list (or vector) of length 318
    return max(0, x[21])
def l76_22(x):
    # x is a list (or vector) of length 318
    return max(0, x[22])
def l76_23(x):
    # x is a list (or vector) of length 318
    return max(0, x[23])
def l76_24(x):
    # x is a list (or vector) of length 318
    return max(0, x[24])
def l76_25(x):
    # x is a list (or vector) of length 318
    return max(0, x[25])
def l76_26(x):
    # x is a list (or vector) of length 318
    return max(0, x[26])
def l76_27(x):
    # x is a list (or vector) of length 318
    return max(0, x[27])
def l76_28(x):
    # x is a list (or vector) of length 318
    return max(0, x[28])
def l76_29(x):
    # x is a list (or vector) of length 318
    return max(0, x[29])
def l76_30(x):
    # x is a list (or vector) of length 318
    return max(0, x[30])
def l76_31(x):
    # x is a list (or vector) of length 318
    return max(0, x[31])
def l76_32(x):
    # x is a list (or vector) of length 318
    return max(0, x[32])
def l76_33(x):
    # x is a list (or vector) of length 318
    return max(0, x[33])
def l76_34(x):
    # x is a list (or vector) of length 318
    return max(0, x[34])
def l76_35(x):
    # x is a list (or vector) of length 318
    return max(0, x[35])
def l76_36(x):
    # x is a list (or vector) of length 318
    return max(0, x[36])
def l76_37(x):
    # x is a list (or vector) of length 318
    return max(0, x[37])
def l76_38(x):
    # x is a list (or vector) of length 318
    return max(0, x[38])
def l76_39(x):
    # x is a list (or vector) of length 318
    return max(0, x[39])
def l76_40(x):
    # x is a list (or vector) of length 318
    return max(0, x[40])
def l76_41(x):
    # x is a list (or vector) of length 318
    return max(0, x[41])
def l76_42(x):
    # x is a list (or vector) of length 318
    return max(0, x[42])
def l76_43(x):
    # x is a list (or vector) of length 318
    return max(0, x[43])
def l76_44(x):
    # x is a list (or vector) of length 318
    return max(0, x[44])
def l76_45(x):
    # x is a list (or vector) of length 318
    return max(0, x[45])
def l76_46(x):
    # x is a list (or vector) of length 318
    return max(0, x[46])
def l76_47(x):
    # x is a list (or vector) of length 318
    return max(0, x[47])
def l76_48(x):
    # x is a list (or vector) of length 318
    return max(0, x[48])
def l76_49(x):
    # x is a list (or vector) of length 318
    return max(0, x[49])
def l76_50(x):
    # x is a list (or vector) of length 318
    return max(0, x[50])
def l76_51(x):
    # x is a list (or vector) of length 318
    return max(0, x[51])
def l76_52(x):
    # x is a list (or vector) of length 318
    return max(0, x[52])
def l76_53(x):
    # x is a list (or vector) of length 318
    return max(0, x[53])
def l76_54(x):
    # x is a list (or vector) of length 318
    return max(0, x[54])
def l76_55(x):
    # x is a list (or vector) of length 318
    return max(0, x[55])
def l76_56(x):
    # x is a list (or vector) of length 318
    return max(0, x[56])
def l76_57(x):
    # x is a list (or vector) of length 318
    return max(0, x[57])
def l76_58(x):
    # x is a list (or vector) of length 318
    return max(0, x[58])
def l76_59(x):
    # x is a list (or vector) of length 318
    return max(0, x[59])
def l76_60(x):
    # x is a list (or vector) of length 318
    return max(0, x[60])
def l76_61(x):
    # x is a list (or vector) of length 318
    return max(0, x[61])
def l76_62(x):
    # x is a list (or vector) of length 318
    return max(0, x[62])
def l76_63(x):
    # x is a list (or vector) of length 318
    return max(0, x[63])
def l76_64(x):
    # x is a list (or vector) of length 318
    return max(0, x[64])
def l76_65(x):
    # x is a list (or vector) of length 318
    return max(0, x[65])
def l76_66(x):
    # x is a list (or vector) of length 318
    return max(0, x[66])
def l76_67(x):
    # x is a list (or vector) of length 318
    return max(0, x[67])
def l76_68(x):
    # x is a list (or vector) of length 318
    return max(0, x[68])
def l76_69(x):
    # x is a list (or vector) of length 318
    return max(0, x[69])
def l76_70(x):
    # x is a list (or vector) of length 318
    return max(0, x[70])
def l76_71(x):
    # x is a list (or vector) of length 318
    return max(0, x[71])
def l76_72(x):
    # x is a list (or vector) of length 318
    return max(0, x[72])
def l76_73(x):
    # x is a list (or vector) of length 318
    return max(0, x[73])
def l76_74(x):
    # x is a list (or vector) of length 318
    return max(0, x[74])
def l76_75(x):
    # x is a list (or vector) of length 318
    return max(0, x[75])
def l76_76(x):
    # x is a list (or vector) of length 318
    return max(0, x[76])
def l76_77(x):
    # x is a list (or vector) of length 318
    return max(0, x[77])
def l76_78(x):
    # x is a list (or vector) of length 318
    return max(0, x[78])
def l76_79(x):
    # x is a list (or vector) of length 318
    return max(0, x[79])
def l76_80(x):
    # x is a list (or vector) of length 318
    return max(0, x[80])
def l76_81(x):
    # x is a list (or vector) of length 318
    return max(0, x[81])
def l76_82(x):
    # x is a list (or vector) of length 318
    return max(0, x[82])
def l76_83(x):
    # x is a list (or vector) of length 318
    return max(0, x[83])
def l76_84(x):
    # x is a list (or vector) of length 318
    return max(0, x[84])
def l76_85(x):
    # x is a list (or vector) of length 318
    return max(0, x[85])
def l76_86(x):
    # x is a list (or vector) of length 318
    return max(0, x[86])
def l76_87(x):
    # x is a list (or vector) of length 318
    return max(0, x[87])
def l76_88(x):
    # x is a list (or vector) of length 318
    return max(0, x[88])
def l76_89(x):
    # x is a list (or vector) of length 318
    return max(0, x[89])
def l76_90(x):
    # x is a list (or vector) of length 318
    return max(0, x[90])
def l76_91(x):
    # x is a list (or vector) of length 318
    return max(0, x[91])
def l76_92(x):
    # x is a list (or vector) of length 318
    return max(0, x[92])
def l76_93(x):
    # x is a list (or vector) of length 318
    return max(0, x[93])
def l76_94(x):
    # x is a list (or vector) of length 318
    return max(0, x[94])
def l76_95(x):
    # x is a list (or vector) of length 318
    return max(0, x[95])
def l76_96(x):
    # x is a list (or vector) of length 318
    return max(0, x[96])
def l76_97(x):
    # x is a list (or vector) of length 318
    return max(0, x[97])
def l76_98(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[98] + -1.0*x[128] + 1.0)
def l76_99(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[99] + -1.0*x[129] + 1.0)
def l76_100(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[100] + -1.0*x[130] + 1.0)
def l76_101(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[101] + -1.0*x[131] + 1.0)
def l76_102(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[102] + -1.0*x[132] + 1.0)
def l76_103(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[103] + -1.0*x[133] + 1.0)
def l76_104(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[104] + -1.0*x[134] + 1.0)
def l76_105(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[105] + -1.0*x[135] + 1.0)
def l76_106(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[106] + -1.0*x[136] + 1.0)
def l76_107(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[107] + -1.0*x[137] + 1.0)
def l76_108(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[108] + -1.0*x[138] + 1.0)
def l76_109(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[109] + -1.0*x[139] + 1.0)
def l76_110(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[110] + -1.0*x[140] + 1.0)
def l76_111(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[111] + -1.0*x[141] + 1.0)
def l76_112(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[112] + -1.0*x[142] + 1.0)
def l76_113(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[113] + -1.0*x[143] + 1.0)
def l76_114(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[114] + -1.0*x[144] + 1.0)
def l76_115(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[115] + -1.0*x[145] + 1.0)
def l76_116(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[116] + -1.0*x[146] + 1.0)
def l76_117(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[117] + -1.0*x[147] + 1.0)
def l76_118(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[118] + -1.0*x[148] + 1.0)
def l76_119(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[119] + -1.0*x[149] + 1.0)
def l76_120(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[120] + -1.0*x[150] + 1.0)
def l76_121(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[121] + -1.0*x[151] + 1.0)
def l76_122(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[122] + -1.0*x[152] + 1.0)
def l76_123(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[123] + -1.0*x[153] + 1.0)
def l76_124(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[124] + -1.0*x[154] + 1.0)
def l76_125(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[125] + -1.0*x[155] + 1.0)
def l76_126(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[126] + -1.0*x[156] + 1.0)
def l76_127(x):
    # x is a list (or vector) of length 318
    return max(0, -1.0*x[127] + -1.0*x[157] + 1.0)
def l76_128(x):
    # x is a list (or vector) of length 318
    return max(0, x[188])
def l76_129(x):
    # x is a list (or vector) of length 318
    return max(0, x[189])
def l76_130(x):
    # x is a list (or vector) of length 318
    return max(0, x[158])
def l76_131(x):
    # x is a list (or vector) of length 318
    return max(0, x[159])
def l76_132(x):
    # x is a list (or vector) of length 318
    return max(0, x[160])
def l76_133(x):
    # x is a list (or vector) of length 318
    return max(0, x[161])
def l76_134(x):
    # x is a list (or vector) of length 318
    return max(0, x[162])
def l76_135(x):
    # x is a list (or vector) of length 318
    return max(0, x[163])
def l76_136(x):
    # x is a list (or vector) of length 318
    return max(0, x[164])
def l76_137(x):
    # x is a list (or vector) of length 318
    return max(0, x[165])
def l76_138(x):
    # x is a list (or vector) of length 318
    return max(0, x[166])
def l76_139(x):
    # x is a list (or vector) of length 318
    return max(0, x[167])
def l76_140(x):
    # x is a list (or vector) of length 318
    return max(0, x[168])
def l76_141(x):
    # x is a list (or vector) of length 318
    return max(0, x[169])
def l76_142(x):
    # x is a list (or vector) of length 318
    return max(0, x[170])
def l76_143(x):
    # x is a list (or vector) of length 318
    return max(0, x[171])
def l76_144(x):
    # x is a list (or vector) of length 318
    return max(0, x[172])
def l76_145(x):
    # x is a list (or vector) of length 318
    return max(0, x[173])
def l76_146(x):
    # x is a list (or vector) of length 318
    return max(0, x[174])
def l76_147(x):
    # x is a list (or vector) of length 318
    return max(0, x[175])
def l76_148(x):
    # x is a list (or vector) of length 318
    return max(0, x[176])
def l76_149(x):
    # x is a list (or vector) of length 318
    return max(0, x[177])
def l76_150(x):
    # x is a list (or vector) of length 318
    return max(0, x[178])
def l76_151(x):
    # x is a list (or vector) of length 318
    return max(0, x[179])
def l76_152(x):
    # x is a list (or vector) of length 318
    return max(0, x[180])
def l76_153(x):
    # x is a list (or vector) of length 318
    return max(0, x[181])
def l76_154(x):
    # x is a list (or vector) of length 318
    return max(0, x[182])
def l76_155(x):
    # x is a list (or vector) of length 318
    return max(0, x[183])
def l76_156(x):
    # x is a list (or vector) of length 318
    return max(0, x[184])
def l76_157(x):
    # x is a list (or vector) of length 318
    return max(0, x[185])
def l76_158(x):
    # x is a list (or vector) of length 318
    return max(0, x[186])
def l76_159(x):
    # x is a list (or vector) of length 318
    return max(0, x[187])
def l76_160(x):
    # x is a list (or vector) of length 318
    return max(0, x[190])
def l76_161(x):
    # x is a list (or vector) of length 318
    return max(0, x[191])
def l76_162(x):
    # x is a list (or vector) of length 318
    return max(0, x[192])
def l76_163(x):
    # x is a list (or vector) of length 318
    return max(0, x[193])
def l76_164(x):
    # x is a list (or vector) of length 318
    return max(0, x[194])
def l76_165(x):
    # x is a list (or vector) of length 318
    return max(0, x[195])
def l76_166(x):
    # x is a list (or vector) of length 318
    return max(0, x[196])
def l76_167(x):
    # x is a list (or vector) of length 318
    return max(0, x[197])
def l76_168(x):
    # x is a list (or vector) of length 318
    return max(0, x[198])
def l76_169(x):
    # x is a list (or vector) of length 318
    return max(0, x[199])
def l76_170(x):
    # x is a list (or vector) of length 318
    return max(0, x[200])
def l76_171(x):
    # x is a list (or vector) of length 318
    return max(0, x[201])
def l76_172(x):
    # x is a list (or vector) of length 318
    return max(0, x[202])
def l76_173(x):
    # x is a list (or vector) of length 318
    return max(0, x[203])
def l76_174(x):
    # x is a list (or vector) of length 318
    return max(0, x[204])
def l76_175(x):
    # x is a list (or vector) of length 318
    return max(0, x[205])
def l76_176(x):
    # x is a list (or vector) of length 318
    return max(0, x[206])
def l76_177(x):
    # x is a list (or vector) of length 318
    return max(0, x[207])
def l76_178(x):
    # x is a list (or vector) of length 318
    return max(0, x[208])
def l76_179(x):
    # x is a list (or vector) of length 318
    return max(0, x[209])
def l76_180(x):
    # x is a list (or vector) of length 318
    return max(0, x[210])
def l76_181(x):
    # x is a list (or vector) of length 318
    return max(0, x[211])
def l76_182(x):
    # x is a list (or vector) of length 318
    return max(0, x[212])
def l76_183(x):
    # x is a list (or vector) of length 318
    return max(0, x[213])
def l76_184(x):
    # x is a list (or vector) of length 318
    return max(0, x[214])
def l76_185(x):
    # x is a list (or vector) of length 318
    return max(0, x[215])
def l76_186(x):
    # x is a list (or vector) of length 318
    return max(0, x[216])
def l76_187(x):
    # x is a list (or vector) of length 318
    return max(0, x[217])
def l76_188(x):
    # x is a list (or vector) of length 318
    return max(0, x[218])
def l76_189(x):
    # x is a list (or vector) of length 318
    return max(0, x[219])
def l76_190(x):
    # x is a list (or vector) of length 318
    return max(0, x[220])
def l76_191(x):
    # x is a list (or vector) of length 318
    return max(0, x[221])
def l76_192(x):
    # x is a list (or vector) of length 318
    return max(0, x[222])
def l76_193(x):
    # x is a list (or vector) of length 318
    return max(0, x[223])
def l76_194(x):
    # x is a list (or vector) of length 318
    return max(0, x[224])
def l76_195(x):
    # x is a list (or vector) of length 318
    return max(0, x[225])
def l76_196(x):
    # x is a list (or vector) of length 318
    return max(0, x[226])
def l76_197(x):
    # x is a list (or vector) of length 318
    return max(0, x[227])
def l76_198(x):
    # x is a list (or vector) of length 318
    return max(0, x[228])
def l76_199(x):
    # x is a list (or vector) of length 318
    return max(0, x[229])
def l76_200(x):
    # x is a list (or vector) of length 318
    return max(0, x[230])
def l76_201(x):
    # x is a list (or vector) of length 318
    return max(0, x[231])
def l76_202(x):
    # x is a list (or vector) of length 318
    return max(0, x[232])
def l76_203(x):
    # x is a list (or vector) of length 318
    return max(0, x[233])
def l76_204(x):
    # x is a list (or vector) of length 318
    return max(0, x[234])
def l76_205(x):
    # x is a list (or vector) of length 318
    return max(0, x[235])
def l76_206(x):
    # x is a list (or vector) of length 318
    return max(0, x[236])
def l76_207(x):
    # x is a list (or vector) of length 318
    return max(0, x[237])
def l76_208(x):
    # x is a list (or vector) of length 318
    return max(0, x[238])
def l76_209(x):
    # x is a list (or vector) of length 318
    return max(0, x[239])
def l76_210(x):
    # x is a list (or vector) of length 318
    return max(0, x[240])
def l76_211(x):
    # x is a list (or vector) of length 318
    return max(0, x[241])
def l76_212(x):
    # x is a list (or vector) of length 318
    return max(0, x[242])
def l76_213(x):
    # x is a list (or vector) of length 318
    return max(0, x[243])
def l76_214(x):
    # x is a list (or vector) of length 318
    return max(0, x[244])
def l76_215(x):
    # x is a list (or vector) of length 318
    return max(0, x[245])
def l76_216(x):
    # x is a list (or vector) of length 318
    return max(0, x[246])
def l76_217(x):
    # x is a list (or vector) of length 318
    return max(0, x[247])
def l76_218(x):
    # x is a list (or vector) of length 318
    return max(0, x[248])
def l76_219(x):
    # x is a list (or vector) of length 318
    return max(0, x[249])
def l76_220(x):
    # x is a list (or vector) of length 318
    return max(0, x[250])
def l76_221(x):
    # x is a list (or vector) of length 318
    return max(0, x[251])
def l76_222(x):
    # x is a list (or vector) of length 318
    return max(0, x[252])
def l76_223(x):
    # x is a list (or vector) of length 318
    return max(0, x[253])
def l76_224(x):
    # x is a list (or vector) of length 318
    return max(0, x[254])
def l76_225(x):
    # x is a list (or vector) of length 318
    return max(0, x[255])
def l76_226(x):
    # x is a list (or vector) of length 318
    return max(0, x[256])
def l76_227(x):
    # x is a list (or vector) of length 318
    return max(0, x[257])
def l76_228(x):
    # x is a list (or vector) of length 318
    return max(0, x[258])
def l76_229(x):
    # x is a list (or vector) of length 318
    return max(0, x[259])
def l76_230(x):
    # x is a list (or vector) of length 318
    return max(0, x[260])
def l76_231(x):
    # x is a list (or vector) of length 318
    return max(0, x[261])
def l76_232(x):
    # x is a list (or vector) of length 318
    return max(0, x[262])
def l76_233(x):
    # x is a list (or vector) of length 318
    return max(0, x[263])
def l76_234(x):
    # x is a list (or vector) of length 318
    return max(0, x[264])
def l76_235(x):
    # x is a list (or vector) of length 318
    return max(0, x[265])
def l76_236(x):
    # x is a list (or vector) of length 318
    return max(0, x[266])
def l76_237(x):
    # x is a list (or vector) of length 318
    return max(0, x[267])
def l76_238(x):
    # x is a list (or vector) of length 318
    return max(0, x[268])
def l76_239(x):
    # x is a list (or vector) of length 318
    return max(0, x[269])
def l76_240(x):
    # x is a list (or vector) of length 318
    return max(0, x[270])
def l76_241(x):
    # x is a list (or vector) of length 318
    return max(0, x[271])
def l76_242(x):
    # x is a list (or vector) of length 318
    return max(0, x[272])
def l76_243(x):
    # x is a list (or vector) of length 318
    return max(0, x[273])
def l76_244(x):
    # x is a list (or vector) of length 318
    return max(0, x[274])
def l76_245(x):
    # x is a list (or vector) of length 318
    return max(0, x[275])
def l76_246(x):
    # x is a list (or vector) of length 318
    return max(0, x[276])
def l76_247(x):
    # x is a list (or vector) of length 318
    return max(0, x[277])
def l76_248(x):
    # x is a list (or vector) of length 318
    return max(0, x[278])
def l76_249(x):
    # x is a list (or vector) of length 318
    return max(0, x[279])
def l76_250(x):
    # x is a list (or vector) of length 318
    return max(0, x[280])
def l76_251(x):
    # x is a list (or vector) of length 318
    return max(0, x[281])
def l76_252(x):
    # x is a list (or vector) of length 318
    return max(0, x[282])
def l76_253(x):
    # x is a list (or vector) of length 318
    return max(0, x[283])
def l76_254(x):
    # x is a list (or vector) of length 318
    return max(0, x[284])
def l76_255(x):
    # x is a list (or vector) of length 318
    return max(0, x[285])
def l76_256(x):
    # x is a list (or vector) of length 318
    return max(0, x[286])
def l76_257(x):
    # x is a list (or vector) of length 318
    return max(0, x[287])
def l76_258(x):
    # x is a list (or vector) of length 318
    return max(0, x[288])
def l76_259(x):
    # x is a list (or vector) of length 318
    return max(0, x[289])
def l76_260(x):
    # x is a list (or vector) of length 318
    return max(0, x[290])
def l76_261(x):
    # x is a list (or vector) of length 318
    return max(0, x[291])
def l76_262(x):
    # x is a list (or vector) of length 318
    return max(0, x[292])
def l76_263(x):
    # x is a list (or vector) of length 318
    return max(0, x[293])
def l76_264(x):
    # x is a list (or vector) of length 318
    return max(0, x[294])
def l76_265(x):
    # x is a list (or vector) of length 318
    return max(0, x[295])
def l76_266(x):
    # x is a list (or vector) of length 318
    return max(0, x[296])
def l76_267(x):
    # x is a list (or vector) of length 318
    return max(0, x[297])
def l76_268(x):
    # x is a list (or vector) of length 318
    return max(0, x[298])
def l76_269(x):
    # x is a list (or vector) of length 318
    return max(0, x[299])
def l76_270(x):
    # x is a list (or vector) of length 318
    return max(0, x[300])
def l76_271(x):
    # x is a list (or vector) of length 318
    return max(0, x[301])
def l76_272(x):
    # x is a list (or vector) of length 318
    return max(0, x[302])
def l76_273(x):
    # x is a list (or vector) of length 318
    return max(0, x[303])
def l76_274(x):
    # x is a list (or vector) of length 318
    return max(0, x[304])
def l76_275(x):
    # x is a list (or vector) of length 318
    return max(0, x[305])
def l76_276(x):
    # x is a list (or vector) of length 318
    return max(0, x[306])
def l76_277(x):
    # x is a list (or vector) of length 318
    return max(0, x[307])
def l76_278(x):
    # x is a list (or vector) of length 318
    return max(0, x[308])
def l76_279(x):
    # x is a list (or vector) of length 318
    return max(0, x[309])
def l76_280(x):
    # x is a list (or vector) of length 318
    return max(0, x[310])
def l76_281(x):
    # x is a list (or vector) of length 318
    return max(0, x[311])
def l76_282(x):
    # x is a list (or vector) of length 318
    return max(0, x[312])
def l76_283(x):
    # x is a list (or vector) of length 318
    return max(0, x[313])
def l76_284(x):
    # x is a list (or vector) of length 318
    return max(0, x[314])
def l76_285(x):
    # x is a list (or vector) of length 318
    return max(0, x[315])
def l76_286(x):
    # x is a list (or vector) of length 318
    return max(0, x[316])
def l76_287(x):
    # x is a list (or vector) of length 318
    return max(0, x[317])
def l76_(x):
    # x is a list (or vector) of length 318
    return [
        l76_0(x),
        l76_1(x),
        l76_2(x),
        l76_3(x),
        l76_4(x),
        l76_5(x),
        l76_6(x),
        l76_7(x),
        l76_8(x),
        l76_9(x),
        l76_10(x),
        l76_11(x),
        l76_12(x),
        l76_13(x),
        l76_14(x),
        l76_15(x),
        l76_16(x),
        l76_17(x),
        l76_18(x),
        l76_19(x),
        l76_20(x),
        l76_21(x),
        l76_22(x),
        l76_23(x),
        l76_24(x),
        l76_25(x),
        l76_26(x),
        l76_27(x),
        l76_28(x),
        l76_29(x),
        l76_30(x),
        l76_31(x),
        l76_32(x),
        l76_33(x),
        l76_34(x),
        l76_35(x),
        l76_36(x),
        l76_37(x),
        l76_38(x),
        l76_39(x),
        l76_40(x),
        l76_41(x),
        l76_42(x),
        l76_43(x),
        l76_44(x),
        l76_45(x),
        l76_46(x),
        l76_47(x),
        l76_48(x),
        l76_49(x),
        l76_50(x),
        l76_51(x),
        l76_52(x),
        l76_53(x),
        l76_54(x),
        l76_55(x),
        l76_56(x),
        l76_57(x),
        l76_58(x),
        l76_59(x),
        l76_60(x),
        l76_61(x),
        l76_62(x),
        l76_63(x),
        l76_64(x),
        l76_65(x),
        l76_66(x),
        l76_67(x),
        l76_68(x),
        l76_69(x),
        l76_70(x),
        l76_71(x),
        l76_72(x),
        l76_73(x),
        l76_74(x),
        l76_75(x),
        l76_76(x),
        l76_77(x),
        l76_78(x),
        l76_79(x),
        l76_80(x),
        l76_81(x),
        l76_82(x),
        l76_83(x),
        l76_84(x),
        l76_85(x),
        l76_86(x),
        l76_87(x),
        l76_88(x),
        l76_89(x),
        l76_90(x),
        l76_91(x),
        l76_92(x),
        l76_93(x),
        l76_94(x),
        l76_95(x),
        l76_96(x),
        l76_97(x),
        l76_98(x),
        l76_99(x),
        l76_100(x),
        l76_101(x),
        l76_102(x),
        l76_103(x),
        l76_104(x),
        l76_105(x),
        l76_106(x),
        l76_107(x),
        l76_108(x),
        l76_109(x),
        l76_110(x),
        l76_111(x),
        l76_112(x),
        l76_113(x),
        l76_114(x),
        l76_115(x),
        l76_116(x),
        l76_117(x),
        l76_118(x),
        l76_119(x),
        l76_120(x),
        l76_121(x),
        l76_122(x),
        l76_123(x),
        l76_124(x),
        l76_125(x),
        l76_126(x),
        l76_127(x),
        l76_128(x),
        l76_129(x),
        l76_130(x),
        l76_131(x),
        l76_132(x),
        l76_133(x),
        l76_134(x),
        l76_135(x),
        l76_136(x),
        l76_137(x),
        l76_138(x),
        l76_139(x),
        l76_140(x),
        l76_141(x),
        l76_142(x),
        l76_143(x),
        l76_144(x),
        l76_145(x),
        l76_146(x),
        l76_147(x),
        l76_148(x),
        l76_149(x),
        l76_150(x),
        l76_151(x),
        l76_152(x),
        l76_153(x),
        l76_154(x),
        l76_155(x),
        l76_156(x),
        l76_157(x),
        l76_158(x),
        l76_159(x),
        l76_160(x),
        l76_161(x),
        l76_162(x),
        l76_163(x),
        l76_164(x),
        l76_165(x),
        l76_166(x),
        l76_167(x),
        l76_168(x),
        l76_169(x),
        l76_170(x),
        l76_171(x),
        l76_172(x),
        l76_173(x),
        l76_174(x),
        l76_175(x),
        l76_176(x),
        l76_177(x),
        l76_178(x),
        l76_179(x),
        l76_180(x),
        l76_181(x),
        l76_182(x),
        l76_183(x),
        l76_184(x),
        l76_185(x),
        l76_186(x),
        l76_187(x),
        l76_188(x),
        l76_189(x),
        l76_190(x),
        l76_191(x),
        l76_192(x),
        l76_193(x),
        l76_194(x),
        l76_195(x),
        l76_196(x),
        l76_197(x),
        l76_198(x),
        l76_199(x),
        l76_200(x),
        l76_201(x),
        l76_202(x),
        l76_203(x),
        l76_204(x),
        l76_205(x),
        l76_206(x),
        l76_207(x),
        l76_208(x),
        l76_209(x),
        l76_210(x),
        l76_211(x),
        l76_212(x),
        l76_213(x),
        l76_214(x),
        l76_215(x),
        l76_216(x),
        l76_217(x),
        l76_218(x),
        l76_219(x),
        l76_220(x),
        l76_221(x),
        l76_222(x),
        l76_223(x),
        l76_224(x),
        l76_225(x),
        l76_226(x),
        l76_227(x),
        l76_228(x),
        l76_229(x),
        l76_230(x),
        l76_231(x),
        l76_232(x),
        l76_233(x),
        l76_234(x),
        l76_235(x),
        l76_236(x),
        l76_237(x),
        l76_238(x),
        l76_239(x),
        l76_240(x),
        l76_241(x),
        l76_242(x),
        l76_243(x),
        l76_244(x),
        l76_245(x),
        l76_246(x),
        l76_247(x),
        l76_248(x),
        l76_249(x),
        l76_250(x),
        l76_251(x),
        l76_252(x),
        l76_253(x),
        l76_254(x),
        l76_255(x),
        l76_256(x),
        l76_257(x),
        l76_258(x),
        l76_259(x),
        l76_260(x),
        l76_261(x),
        l76_262(x),
        l76_263(x),
        l76_264(x),
        l76_265(x),
        l76_266(x),
        l76_267(x),
        l76_268(x),
        l76_269(x),
        l76_270(x),
        l76_271(x),
        l76_272(x),
        l76_273(x),
        l76_274(x),
        l76_275(x),
        l76_276(x),
        l76_277(x),
        l76_278(x),
        l76_279(x),
        l76_280(x),
        l76_281(x),
        l76_282(x),
        l76_283(x),
        l76_284(x),
        l76_285(x),
        l76_286(x),
        l76_287(x),
    ]