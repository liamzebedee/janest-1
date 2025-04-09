import numpy as np




# Generated from reverse engineering
def l336_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 288
    out = np.empty(288, dtype=np.float32)
    
    # for i in range(0, 104):
    for i in range(0, 104):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffffff (len=24)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(104, 128):
    for i in range(0, 24):
        s = -1 * x[104 + i] + -1 * x[128 + i]
        s += biases[i]
        out[104 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 136):
    for i in range(0, 8):
        s = x[176 + i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(136, 160):
    for i in range(0, 24):
        s = x[152 + i]
        out[136 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 288):
    for i in range(0, 128):
        s = x[184 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l336_0(x):
    # x is a list (or vector) of length 312
    return max(0, x[0])
def l336_1(x):
    # x is a list (or vector) of length 312
    return max(0, x[1])
def l336_2(x):
    # x is a list (or vector) of length 312
    return max(0, x[2])
def l336_3(x):
    # x is a list (or vector) of length 312
    return max(0, x[3])
def l336_4(x):
    # x is a list (or vector) of length 312
    return max(0, x[4])
def l336_5(x):
    # x is a list (or vector) of length 312
    return max(0, x[5])
def l336_6(x):
    # x is a list (or vector) of length 312
    return max(0, x[6])
def l336_7(x):
    # x is a list (or vector) of length 312
    return max(0, x[7])
def l336_8(x):
    # x is a list (or vector) of length 312
    return max(0, x[8])
def l336_9(x):
    # x is a list (or vector) of length 312
    return max(0, x[9])
def l336_10(x):
    # x is a list (or vector) of length 312
    return max(0, x[10])
def l336_11(x):
    # x is a list (or vector) of length 312
    return max(0, x[11])
def l336_12(x):
    # x is a list (or vector) of length 312
    return max(0, x[12])
def l336_13(x):
    # x is a list (or vector) of length 312
    return max(0, x[13])
def l336_14(x):
    # x is a list (or vector) of length 312
    return max(0, x[14])
def l336_15(x):
    # x is a list (or vector) of length 312
    return max(0, x[15])
def l336_16(x):
    # x is a list (or vector) of length 312
    return max(0, x[16])
def l336_17(x):
    # x is a list (or vector) of length 312
    return max(0, x[17])
def l336_18(x):
    # x is a list (or vector) of length 312
    return max(0, x[18])
def l336_19(x):
    # x is a list (or vector) of length 312
    return max(0, x[19])
def l336_20(x):
    # x is a list (or vector) of length 312
    return max(0, x[20])
def l336_21(x):
    # x is a list (or vector) of length 312
    return max(0, x[21])
def l336_22(x):
    # x is a list (or vector) of length 312
    return max(0, x[22])
def l336_23(x):
    # x is a list (or vector) of length 312
    return max(0, x[23])
def l336_24(x):
    # x is a list (or vector) of length 312
    return max(0, x[24])
def l336_25(x):
    # x is a list (or vector) of length 312
    return max(0, x[25])
def l336_26(x):
    # x is a list (or vector) of length 312
    return max(0, x[26])
def l336_27(x):
    # x is a list (or vector) of length 312
    return max(0, x[27])
def l336_28(x):
    # x is a list (or vector) of length 312
    return max(0, x[28])
def l336_29(x):
    # x is a list (or vector) of length 312
    return max(0, x[29])
def l336_30(x):
    # x is a list (or vector) of length 312
    return max(0, x[30])
def l336_31(x):
    # x is a list (or vector) of length 312
    return max(0, x[31])
def l336_32(x):
    # x is a list (or vector) of length 312
    return max(0, x[32])
def l336_33(x):
    # x is a list (or vector) of length 312
    return max(0, x[33])
def l336_34(x):
    # x is a list (or vector) of length 312
    return max(0, x[34])
def l336_35(x):
    # x is a list (or vector) of length 312
    return max(0, x[35])
def l336_36(x):
    # x is a list (or vector) of length 312
    return max(0, x[36])
def l336_37(x):
    # x is a list (or vector) of length 312
    return max(0, x[37])
def l336_38(x):
    # x is a list (or vector) of length 312
    return max(0, x[38])
def l336_39(x):
    # x is a list (or vector) of length 312
    return max(0, x[39])
def l336_40(x):
    # x is a list (or vector) of length 312
    return max(0, x[40])
def l336_41(x):
    # x is a list (or vector) of length 312
    return max(0, x[41])
def l336_42(x):
    # x is a list (or vector) of length 312
    return max(0, x[42])
def l336_43(x):
    # x is a list (or vector) of length 312
    return max(0, x[43])
def l336_44(x):
    # x is a list (or vector) of length 312
    return max(0, x[44])
def l336_45(x):
    # x is a list (or vector) of length 312
    return max(0, x[45])
def l336_46(x):
    # x is a list (or vector) of length 312
    return max(0, x[46])
def l336_47(x):
    # x is a list (or vector) of length 312
    return max(0, x[47])
def l336_48(x):
    # x is a list (or vector) of length 312
    return max(0, x[48])
def l336_49(x):
    # x is a list (or vector) of length 312
    return max(0, x[49])
def l336_50(x):
    # x is a list (or vector) of length 312
    return max(0, x[50])
def l336_51(x):
    # x is a list (or vector) of length 312
    return max(0, x[51])
def l336_52(x):
    # x is a list (or vector) of length 312
    return max(0, x[52])
def l336_53(x):
    # x is a list (or vector) of length 312
    return max(0, x[53])
def l336_54(x):
    # x is a list (or vector) of length 312
    return max(0, x[54])
def l336_55(x):
    # x is a list (or vector) of length 312
    return max(0, x[55])
def l336_56(x):
    # x is a list (or vector) of length 312
    return max(0, x[56])
def l336_57(x):
    # x is a list (or vector) of length 312
    return max(0, x[57])
def l336_58(x):
    # x is a list (or vector) of length 312
    return max(0, x[58])
def l336_59(x):
    # x is a list (or vector) of length 312
    return max(0, x[59])
def l336_60(x):
    # x is a list (or vector) of length 312
    return max(0, x[60])
def l336_61(x):
    # x is a list (or vector) of length 312
    return max(0, x[61])
def l336_62(x):
    # x is a list (or vector) of length 312
    return max(0, x[62])
def l336_63(x):
    # x is a list (or vector) of length 312
    return max(0, x[63])
def l336_64(x):
    # x is a list (or vector) of length 312
    return max(0, x[64])
def l336_65(x):
    # x is a list (or vector) of length 312
    return max(0, x[65])
def l336_66(x):
    # x is a list (or vector) of length 312
    return max(0, x[66])
def l336_67(x):
    # x is a list (or vector) of length 312
    return max(0, x[67])
def l336_68(x):
    # x is a list (or vector) of length 312
    return max(0, x[68])
def l336_69(x):
    # x is a list (or vector) of length 312
    return max(0, x[69])
def l336_70(x):
    # x is a list (or vector) of length 312
    return max(0, x[70])
def l336_71(x):
    # x is a list (or vector) of length 312
    return max(0, x[71])
def l336_72(x):
    # x is a list (or vector) of length 312
    return max(0, x[72])
def l336_73(x):
    # x is a list (or vector) of length 312
    return max(0, x[73])
def l336_74(x):
    # x is a list (or vector) of length 312
    return max(0, x[74])
def l336_75(x):
    # x is a list (or vector) of length 312
    return max(0, x[75])
def l336_76(x):
    # x is a list (or vector) of length 312
    return max(0, x[76])
def l336_77(x):
    # x is a list (or vector) of length 312
    return max(0, x[77])
def l336_78(x):
    # x is a list (or vector) of length 312
    return max(0, x[78])
def l336_79(x):
    # x is a list (or vector) of length 312
    return max(0, x[79])
def l336_80(x):
    # x is a list (or vector) of length 312
    return max(0, x[80])
def l336_81(x):
    # x is a list (or vector) of length 312
    return max(0, x[81])
def l336_82(x):
    # x is a list (or vector) of length 312
    return max(0, x[82])
def l336_83(x):
    # x is a list (or vector) of length 312
    return max(0, x[83])
def l336_84(x):
    # x is a list (or vector) of length 312
    return max(0, x[84])
def l336_85(x):
    # x is a list (or vector) of length 312
    return max(0, x[85])
def l336_86(x):
    # x is a list (or vector) of length 312
    return max(0, x[86])
def l336_87(x):
    # x is a list (or vector) of length 312
    return max(0, x[87])
def l336_88(x):
    # x is a list (or vector) of length 312
    return max(0, x[88])
def l336_89(x):
    # x is a list (or vector) of length 312
    return max(0, x[89])
def l336_90(x):
    # x is a list (or vector) of length 312
    return max(0, x[90])
def l336_91(x):
    # x is a list (or vector) of length 312
    return max(0, x[91])
def l336_92(x):
    # x is a list (or vector) of length 312
    return max(0, x[92])
def l336_93(x):
    # x is a list (or vector) of length 312
    return max(0, x[93])
def l336_94(x):
    # x is a list (or vector) of length 312
    return max(0, x[94])
def l336_95(x):
    # x is a list (or vector) of length 312
    return max(0, x[95])
def l336_96(x):
    # x is a list (or vector) of length 312
    return max(0, x[96])
def l336_97(x):
    # x is a list (or vector) of length 312
    return max(0, x[97])
def l336_98(x):
    # x is a list (or vector) of length 312
    return max(0, x[98])
def l336_99(x):
    # x is a list (or vector) of length 312
    return max(0, x[99])
def l336_100(x):
    # x is a list (or vector) of length 312
    return max(0, x[100])
def l336_101(x):
    # x is a list (or vector) of length 312
    return max(0, x[101])
def l336_102(x):
    # x is a list (or vector) of length 312
    return max(0, x[102])
def l336_103(x):
    # x is a list (or vector) of length 312
    return max(0, x[103])
def l336_104(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[104] + -1.0*x[128] + 1.0)
def l336_105(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[105] + -1.0*x[129] + 1.0)
def l336_106(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[106] + -1.0*x[130] + 1.0)
def l336_107(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[107] + -1.0*x[131] + 1.0)
def l336_108(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[108] + -1.0*x[132] + 1.0)
def l336_109(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[109] + -1.0*x[133] + 1.0)
def l336_110(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[110] + -1.0*x[134] + 1.0)
def l336_111(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[111] + -1.0*x[135] + 1.0)
def l336_112(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[112] + -1.0*x[136] + 1.0)
def l336_113(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[113] + -1.0*x[137] + 1.0)
def l336_114(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[114] + -1.0*x[138] + 1.0)
def l336_115(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[115] + -1.0*x[139] + 1.0)
def l336_116(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[116] + -1.0*x[140] + 1.0)
def l336_117(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[117] + -1.0*x[141] + 1.0)
def l336_118(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[118] + -1.0*x[142] + 1.0)
def l336_119(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[119] + -1.0*x[143] + 1.0)
def l336_120(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[120] + -1.0*x[144] + 1.0)
def l336_121(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[121] + -1.0*x[145] + 1.0)
def l336_122(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[122] + -1.0*x[146] + 1.0)
def l336_123(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[123] + -1.0*x[147] + 1.0)
def l336_124(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[124] + -1.0*x[148] + 1.0)
def l336_125(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[125] + -1.0*x[149] + 1.0)
def l336_126(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[126] + -1.0*x[150] + 1.0)
def l336_127(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[127] + -1.0*x[151] + 1.0)
def l336_128(x):
    # x is a list (or vector) of length 312
    return max(0, x[176])
def l336_129(x):
    # x is a list (or vector) of length 312
    return max(0, x[177])
def l336_130(x):
    # x is a list (or vector) of length 312
    return max(0, x[178])
def l336_131(x):
    # x is a list (or vector) of length 312
    return max(0, x[179])
def l336_132(x):
    # x is a list (or vector) of length 312
    return max(0, x[180])
def l336_133(x):
    # x is a list (or vector) of length 312
    return max(0, x[181])
def l336_134(x):
    # x is a list (or vector) of length 312
    return max(0, x[182])
def l336_135(x):
    # x is a list (or vector) of length 312
    return max(0, x[183])
def l336_136(x):
    # x is a list (or vector) of length 312
    return max(0, x[152])
def l336_137(x):
    # x is a list (or vector) of length 312
    return max(0, x[153])
def l336_138(x):
    # x is a list (or vector) of length 312
    return max(0, x[154])
def l336_139(x):
    # x is a list (or vector) of length 312
    return max(0, x[155])
def l336_140(x):
    # x is a list (or vector) of length 312
    return max(0, x[156])
def l336_141(x):
    # x is a list (or vector) of length 312
    return max(0, x[157])
def l336_142(x):
    # x is a list (or vector) of length 312
    return max(0, x[158])
def l336_143(x):
    # x is a list (or vector) of length 312
    return max(0, x[159])
def l336_144(x):
    # x is a list (or vector) of length 312
    return max(0, x[160])
def l336_145(x):
    # x is a list (or vector) of length 312
    return max(0, x[161])
def l336_146(x):
    # x is a list (or vector) of length 312
    return max(0, x[162])
def l336_147(x):
    # x is a list (or vector) of length 312
    return max(0, x[163])
def l336_148(x):
    # x is a list (or vector) of length 312
    return max(0, x[164])
def l336_149(x):
    # x is a list (or vector) of length 312
    return max(0, x[165])
def l336_150(x):
    # x is a list (or vector) of length 312
    return max(0, x[166])
def l336_151(x):
    # x is a list (or vector) of length 312
    return max(0, x[167])
def l336_152(x):
    # x is a list (or vector) of length 312
    return max(0, x[168])
def l336_153(x):
    # x is a list (or vector) of length 312
    return max(0, x[169])
def l336_154(x):
    # x is a list (or vector) of length 312
    return max(0, x[170])
def l336_155(x):
    # x is a list (or vector) of length 312
    return max(0, x[171])
def l336_156(x):
    # x is a list (or vector) of length 312
    return max(0, x[172])
def l336_157(x):
    # x is a list (or vector) of length 312
    return max(0, x[173])
def l336_158(x):
    # x is a list (or vector) of length 312
    return max(0, x[174])
def l336_159(x):
    # x is a list (or vector) of length 312
    return max(0, x[175])
def l336_160(x):
    # x is a list (or vector) of length 312
    return max(0, x[184])
def l336_161(x):
    # x is a list (or vector) of length 312
    return max(0, x[185])
def l336_162(x):
    # x is a list (or vector) of length 312
    return max(0, x[186])
def l336_163(x):
    # x is a list (or vector) of length 312
    return max(0, x[187])
def l336_164(x):
    # x is a list (or vector) of length 312
    return max(0, x[188])
def l336_165(x):
    # x is a list (or vector) of length 312
    return max(0, x[189])
def l336_166(x):
    # x is a list (or vector) of length 312
    return max(0, x[190])
def l336_167(x):
    # x is a list (or vector) of length 312
    return max(0, x[191])
def l336_168(x):
    # x is a list (or vector) of length 312
    return max(0, x[192])
def l336_169(x):
    # x is a list (or vector) of length 312
    return max(0, x[193])
def l336_170(x):
    # x is a list (or vector) of length 312
    return max(0, x[194])
def l336_171(x):
    # x is a list (or vector) of length 312
    return max(0, x[195])
def l336_172(x):
    # x is a list (or vector) of length 312
    return max(0, x[196])
def l336_173(x):
    # x is a list (or vector) of length 312
    return max(0, x[197])
def l336_174(x):
    # x is a list (or vector) of length 312
    return max(0, x[198])
def l336_175(x):
    # x is a list (or vector) of length 312
    return max(0, x[199])
def l336_176(x):
    # x is a list (or vector) of length 312
    return max(0, x[200])
def l336_177(x):
    # x is a list (or vector) of length 312
    return max(0, x[201])
def l336_178(x):
    # x is a list (or vector) of length 312
    return max(0, x[202])
def l336_179(x):
    # x is a list (or vector) of length 312
    return max(0, x[203])
def l336_180(x):
    # x is a list (or vector) of length 312
    return max(0, x[204])
def l336_181(x):
    # x is a list (or vector) of length 312
    return max(0, x[205])
def l336_182(x):
    # x is a list (or vector) of length 312
    return max(0, x[206])
def l336_183(x):
    # x is a list (or vector) of length 312
    return max(0, x[207])
def l336_184(x):
    # x is a list (or vector) of length 312
    return max(0, x[208])
def l336_185(x):
    # x is a list (or vector) of length 312
    return max(0, x[209])
def l336_186(x):
    # x is a list (or vector) of length 312
    return max(0, x[210])
def l336_187(x):
    # x is a list (or vector) of length 312
    return max(0, x[211])
def l336_188(x):
    # x is a list (or vector) of length 312
    return max(0, x[212])
def l336_189(x):
    # x is a list (or vector) of length 312
    return max(0, x[213])
def l336_190(x):
    # x is a list (or vector) of length 312
    return max(0, x[214])
def l336_191(x):
    # x is a list (or vector) of length 312
    return max(0, x[215])
def l336_192(x):
    # x is a list (or vector) of length 312
    return max(0, x[216])
def l336_193(x):
    # x is a list (or vector) of length 312
    return max(0, x[217])
def l336_194(x):
    # x is a list (or vector) of length 312
    return max(0, x[218])
def l336_195(x):
    # x is a list (or vector) of length 312
    return max(0, x[219])
def l336_196(x):
    # x is a list (or vector) of length 312
    return max(0, x[220])
def l336_197(x):
    # x is a list (or vector) of length 312
    return max(0, x[221])
def l336_198(x):
    # x is a list (or vector) of length 312
    return max(0, x[222])
def l336_199(x):
    # x is a list (or vector) of length 312
    return max(0, x[223])
def l336_200(x):
    # x is a list (or vector) of length 312
    return max(0, x[224])
def l336_201(x):
    # x is a list (or vector) of length 312
    return max(0, x[225])
def l336_202(x):
    # x is a list (or vector) of length 312
    return max(0, x[226])
def l336_203(x):
    # x is a list (or vector) of length 312
    return max(0, x[227])
def l336_204(x):
    # x is a list (or vector) of length 312
    return max(0, x[228])
def l336_205(x):
    # x is a list (or vector) of length 312
    return max(0, x[229])
def l336_206(x):
    # x is a list (or vector) of length 312
    return max(0, x[230])
def l336_207(x):
    # x is a list (or vector) of length 312
    return max(0, x[231])
def l336_208(x):
    # x is a list (or vector) of length 312
    return max(0, x[232])
def l336_209(x):
    # x is a list (or vector) of length 312
    return max(0, x[233])
def l336_210(x):
    # x is a list (or vector) of length 312
    return max(0, x[234])
def l336_211(x):
    # x is a list (or vector) of length 312
    return max(0, x[235])
def l336_212(x):
    # x is a list (or vector) of length 312
    return max(0, x[236])
def l336_213(x):
    # x is a list (or vector) of length 312
    return max(0, x[237])
def l336_214(x):
    # x is a list (or vector) of length 312
    return max(0, x[238])
def l336_215(x):
    # x is a list (or vector) of length 312
    return max(0, x[239])
def l336_216(x):
    # x is a list (or vector) of length 312
    return max(0, x[240])
def l336_217(x):
    # x is a list (or vector) of length 312
    return max(0, x[241])
def l336_218(x):
    # x is a list (or vector) of length 312
    return max(0, x[242])
def l336_219(x):
    # x is a list (or vector) of length 312
    return max(0, x[243])
def l336_220(x):
    # x is a list (or vector) of length 312
    return max(0, x[244])
def l336_221(x):
    # x is a list (or vector) of length 312
    return max(0, x[245])
def l336_222(x):
    # x is a list (or vector) of length 312
    return max(0, x[246])
def l336_223(x):
    # x is a list (or vector) of length 312
    return max(0, x[247])
def l336_224(x):
    # x is a list (or vector) of length 312
    return max(0, x[248])
def l336_225(x):
    # x is a list (or vector) of length 312
    return max(0, x[249])
def l336_226(x):
    # x is a list (or vector) of length 312
    return max(0, x[250])
def l336_227(x):
    # x is a list (or vector) of length 312
    return max(0, x[251])
def l336_228(x):
    # x is a list (or vector) of length 312
    return max(0, x[252])
def l336_229(x):
    # x is a list (or vector) of length 312
    return max(0, x[253])
def l336_230(x):
    # x is a list (or vector) of length 312
    return max(0, x[254])
def l336_231(x):
    # x is a list (or vector) of length 312
    return max(0, x[255])
def l336_232(x):
    # x is a list (or vector) of length 312
    return max(0, x[256])
def l336_233(x):
    # x is a list (or vector) of length 312
    return max(0, x[257])
def l336_234(x):
    # x is a list (or vector) of length 312
    return max(0, x[258])
def l336_235(x):
    # x is a list (or vector) of length 312
    return max(0, x[259])
def l336_236(x):
    # x is a list (or vector) of length 312
    return max(0, x[260])
def l336_237(x):
    # x is a list (or vector) of length 312
    return max(0, x[261])
def l336_238(x):
    # x is a list (or vector) of length 312
    return max(0, x[262])
def l336_239(x):
    # x is a list (or vector) of length 312
    return max(0, x[263])
def l336_240(x):
    # x is a list (or vector) of length 312
    return max(0, x[264])
def l336_241(x):
    # x is a list (or vector) of length 312
    return max(0, x[265])
def l336_242(x):
    # x is a list (or vector) of length 312
    return max(0, x[266])
def l336_243(x):
    # x is a list (or vector) of length 312
    return max(0, x[267])
def l336_244(x):
    # x is a list (or vector) of length 312
    return max(0, x[268])
def l336_245(x):
    # x is a list (or vector) of length 312
    return max(0, x[269])
def l336_246(x):
    # x is a list (or vector) of length 312
    return max(0, x[270])
def l336_247(x):
    # x is a list (or vector) of length 312
    return max(0, x[271])
def l336_248(x):
    # x is a list (or vector) of length 312
    return max(0, x[272])
def l336_249(x):
    # x is a list (or vector) of length 312
    return max(0, x[273])
def l336_250(x):
    # x is a list (or vector) of length 312
    return max(0, x[274])
def l336_251(x):
    # x is a list (or vector) of length 312
    return max(0, x[275])
def l336_252(x):
    # x is a list (or vector) of length 312
    return max(0, x[276])
def l336_253(x):
    # x is a list (or vector) of length 312
    return max(0, x[277])
def l336_254(x):
    # x is a list (or vector) of length 312
    return max(0, x[278])
def l336_255(x):
    # x is a list (or vector) of length 312
    return max(0, x[279])
def l336_256(x):
    # x is a list (or vector) of length 312
    return max(0, x[280])
def l336_257(x):
    # x is a list (or vector) of length 312
    return max(0, x[281])
def l336_258(x):
    # x is a list (or vector) of length 312
    return max(0, x[282])
def l336_259(x):
    # x is a list (or vector) of length 312
    return max(0, x[283])
def l336_260(x):
    # x is a list (or vector) of length 312
    return max(0, x[284])
def l336_261(x):
    # x is a list (or vector) of length 312
    return max(0, x[285])
def l336_262(x):
    # x is a list (or vector) of length 312
    return max(0, x[286])
def l336_263(x):
    # x is a list (or vector) of length 312
    return max(0, x[287])
def l336_264(x):
    # x is a list (or vector) of length 312
    return max(0, x[288])
def l336_265(x):
    # x is a list (or vector) of length 312
    return max(0, x[289])
def l336_266(x):
    # x is a list (or vector) of length 312
    return max(0, x[290])
def l336_267(x):
    # x is a list (or vector) of length 312
    return max(0, x[291])
def l336_268(x):
    # x is a list (or vector) of length 312
    return max(0, x[292])
def l336_269(x):
    # x is a list (or vector) of length 312
    return max(0, x[293])
def l336_270(x):
    # x is a list (or vector) of length 312
    return max(0, x[294])
def l336_271(x):
    # x is a list (or vector) of length 312
    return max(0, x[295])
def l336_272(x):
    # x is a list (or vector) of length 312
    return max(0, x[296])
def l336_273(x):
    # x is a list (or vector) of length 312
    return max(0, x[297])
def l336_274(x):
    # x is a list (or vector) of length 312
    return max(0, x[298])
def l336_275(x):
    # x is a list (or vector) of length 312
    return max(0, x[299])
def l336_276(x):
    # x is a list (or vector) of length 312
    return max(0, x[300])
def l336_277(x):
    # x is a list (or vector) of length 312
    return max(0, x[301])
def l336_278(x):
    # x is a list (or vector) of length 312
    return max(0, x[302])
def l336_279(x):
    # x is a list (or vector) of length 312
    return max(0, x[303])
def l336_280(x):
    # x is a list (or vector) of length 312
    return max(0, x[304])
def l336_281(x):
    # x is a list (or vector) of length 312
    return max(0, x[305])
def l336_282(x):
    # x is a list (or vector) of length 312
    return max(0, x[306])
def l336_283(x):
    # x is a list (or vector) of length 312
    return max(0, x[307])
def l336_284(x):
    # x is a list (or vector) of length 312
    return max(0, x[308])
def l336_285(x):
    # x is a list (or vector) of length 312
    return max(0, x[309])
def l336_286(x):
    # x is a list (or vector) of length 312
    return max(0, x[310])
def l336_287(x):
    # x is a list (or vector) of length 312
    return max(0, x[311])
def l336_(x):
    # x is a list (or vector) of length 312
    return [
        l336_0(x),
        l336_1(x),
        l336_2(x),
        l336_3(x),
        l336_4(x),
        l336_5(x),
        l336_6(x),
        l336_7(x),
        l336_8(x),
        l336_9(x),
        l336_10(x),
        l336_11(x),
        l336_12(x),
        l336_13(x),
        l336_14(x),
        l336_15(x),
        l336_16(x),
        l336_17(x),
        l336_18(x),
        l336_19(x),
        l336_20(x),
        l336_21(x),
        l336_22(x),
        l336_23(x),
        l336_24(x),
        l336_25(x),
        l336_26(x),
        l336_27(x),
        l336_28(x),
        l336_29(x),
        l336_30(x),
        l336_31(x),
        l336_32(x),
        l336_33(x),
        l336_34(x),
        l336_35(x),
        l336_36(x),
        l336_37(x),
        l336_38(x),
        l336_39(x),
        l336_40(x),
        l336_41(x),
        l336_42(x),
        l336_43(x),
        l336_44(x),
        l336_45(x),
        l336_46(x),
        l336_47(x),
        l336_48(x),
        l336_49(x),
        l336_50(x),
        l336_51(x),
        l336_52(x),
        l336_53(x),
        l336_54(x),
        l336_55(x),
        l336_56(x),
        l336_57(x),
        l336_58(x),
        l336_59(x),
        l336_60(x),
        l336_61(x),
        l336_62(x),
        l336_63(x),
        l336_64(x),
        l336_65(x),
        l336_66(x),
        l336_67(x),
        l336_68(x),
        l336_69(x),
        l336_70(x),
        l336_71(x),
        l336_72(x),
        l336_73(x),
        l336_74(x),
        l336_75(x),
        l336_76(x),
        l336_77(x),
        l336_78(x),
        l336_79(x),
        l336_80(x),
        l336_81(x),
        l336_82(x),
        l336_83(x),
        l336_84(x),
        l336_85(x),
        l336_86(x),
        l336_87(x),
        l336_88(x),
        l336_89(x),
        l336_90(x),
        l336_91(x),
        l336_92(x),
        l336_93(x),
        l336_94(x),
        l336_95(x),
        l336_96(x),
        l336_97(x),
        l336_98(x),
        l336_99(x),
        l336_100(x),
        l336_101(x),
        l336_102(x),
        l336_103(x),
        l336_104(x),
        l336_105(x),
        l336_106(x),
        l336_107(x),
        l336_108(x),
        l336_109(x),
        l336_110(x),
        l336_111(x),
        l336_112(x),
        l336_113(x),
        l336_114(x),
        l336_115(x),
        l336_116(x),
        l336_117(x),
        l336_118(x),
        l336_119(x),
        l336_120(x),
        l336_121(x),
        l336_122(x),
        l336_123(x),
        l336_124(x),
        l336_125(x),
        l336_126(x),
        l336_127(x),
        l336_128(x),
        l336_129(x),
        l336_130(x),
        l336_131(x),
        l336_132(x),
        l336_133(x),
        l336_134(x),
        l336_135(x),
        l336_136(x),
        l336_137(x),
        l336_138(x),
        l336_139(x),
        l336_140(x),
        l336_141(x),
        l336_142(x),
        l336_143(x),
        l336_144(x),
        l336_145(x),
        l336_146(x),
        l336_147(x),
        l336_148(x),
        l336_149(x),
        l336_150(x),
        l336_151(x),
        l336_152(x),
        l336_153(x),
        l336_154(x),
        l336_155(x),
        l336_156(x),
        l336_157(x),
        l336_158(x),
        l336_159(x),
        l336_160(x),
        l336_161(x),
        l336_162(x),
        l336_163(x),
        l336_164(x),
        l336_165(x),
        l336_166(x),
        l336_167(x),
        l336_168(x),
        l336_169(x),
        l336_170(x),
        l336_171(x),
        l336_172(x),
        l336_173(x),
        l336_174(x),
        l336_175(x),
        l336_176(x),
        l336_177(x),
        l336_178(x),
        l336_179(x),
        l336_180(x),
        l336_181(x),
        l336_182(x),
        l336_183(x),
        l336_184(x),
        l336_185(x),
        l336_186(x),
        l336_187(x),
        l336_188(x),
        l336_189(x),
        l336_190(x),
        l336_191(x),
        l336_192(x),
        l336_193(x),
        l336_194(x),
        l336_195(x),
        l336_196(x),
        l336_197(x),
        l336_198(x),
        l336_199(x),
        l336_200(x),
        l336_201(x),
        l336_202(x),
        l336_203(x),
        l336_204(x),
        l336_205(x),
        l336_206(x),
        l336_207(x),
        l336_208(x),
        l336_209(x),
        l336_210(x),
        l336_211(x),
        l336_212(x),
        l336_213(x),
        l336_214(x),
        l336_215(x),
        l336_216(x),
        l336_217(x),
        l336_218(x),
        l336_219(x),
        l336_220(x),
        l336_221(x),
        l336_222(x),
        l336_223(x),
        l336_224(x),
        l336_225(x),
        l336_226(x),
        l336_227(x),
        l336_228(x),
        l336_229(x),
        l336_230(x),
        l336_231(x),
        l336_232(x),
        l336_233(x),
        l336_234(x),
        l336_235(x),
        l336_236(x),
        l336_237(x),
        l336_238(x),
        l336_239(x),
        l336_240(x),
        l336_241(x),
        l336_242(x),
        l336_243(x),
        l336_244(x),
        l336_245(x),
        l336_246(x),
        l336_247(x),
        l336_248(x),
        l336_249(x),
        l336_250(x),
        l336_251(x),
        l336_252(x),
        l336_253(x),
        l336_254(x),
        l336_255(x),
        l336_256(x),
        l336_257(x),
        l336_258(x),
        l336_259(x),
        l336_260(x),
        l336_261(x),
        l336_262(x),
        l336_263(x),
        l336_264(x),
        l336_265(x),
        l336_266(x),
        l336_267(x),
        l336_268(x),
        l336_269(x),
        l336_270(x),
        l336_271(x),
        l336_272(x),
        l336_273(x),
        l336_274(x),
        l336_275(x),
        l336_276(x),
        l336_277(x),
        l336_278(x),
        l336_279(x),
        l336_280(x),
        l336_281(x),
        l336_282(x),
        l336_283(x),
        l336_284(x),
        l336_285(x),
        l336_286(x),
        l336_287(x),
    ]