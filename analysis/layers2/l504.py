import numpy as np




# Generated from reverse engineering
def l504_g(x: np.ndarray) -> np.ndarray:
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




def l504_0(x):
    # x is a list (or vector) of length 312
    return max(0, x[0])
def l504_1(x):
    # x is a list (or vector) of length 312
    return max(0, x[1])
def l504_2(x):
    # x is a list (or vector) of length 312
    return max(0, x[2])
def l504_3(x):
    # x is a list (or vector) of length 312
    return max(0, x[3])
def l504_4(x):
    # x is a list (or vector) of length 312
    return max(0, x[4])
def l504_5(x):
    # x is a list (or vector) of length 312
    return max(0, x[5])
def l504_6(x):
    # x is a list (or vector) of length 312
    return max(0, x[6])
def l504_7(x):
    # x is a list (or vector) of length 312
    return max(0, x[7])
def l504_8(x):
    # x is a list (or vector) of length 312
    return max(0, x[8])
def l504_9(x):
    # x is a list (or vector) of length 312
    return max(0, x[9])
def l504_10(x):
    # x is a list (or vector) of length 312
    return max(0, x[10])
def l504_11(x):
    # x is a list (or vector) of length 312
    return max(0, x[11])
def l504_12(x):
    # x is a list (or vector) of length 312
    return max(0, x[12])
def l504_13(x):
    # x is a list (or vector) of length 312
    return max(0, x[13])
def l504_14(x):
    # x is a list (or vector) of length 312
    return max(0, x[14])
def l504_15(x):
    # x is a list (or vector) of length 312
    return max(0, x[15])
def l504_16(x):
    # x is a list (or vector) of length 312
    return max(0, x[16])
def l504_17(x):
    # x is a list (or vector) of length 312
    return max(0, x[17])
def l504_18(x):
    # x is a list (or vector) of length 312
    return max(0, x[18])
def l504_19(x):
    # x is a list (or vector) of length 312
    return max(0, x[19])
def l504_20(x):
    # x is a list (or vector) of length 312
    return max(0, x[20])
def l504_21(x):
    # x is a list (or vector) of length 312
    return max(0, x[21])
def l504_22(x):
    # x is a list (or vector) of length 312
    return max(0, x[22])
def l504_23(x):
    # x is a list (or vector) of length 312
    return max(0, x[23])
def l504_24(x):
    # x is a list (or vector) of length 312
    return max(0, x[24])
def l504_25(x):
    # x is a list (or vector) of length 312
    return max(0, x[25])
def l504_26(x):
    # x is a list (or vector) of length 312
    return max(0, x[26])
def l504_27(x):
    # x is a list (or vector) of length 312
    return max(0, x[27])
def l504_28(x):
    # x is a list (or vector) of length 312
    return max(0, x[28])
def l504_29(x):
    # x is a list (or vector) of length 312
    return max(0, x[29])
def l504_30(x):
    # x is a list (or vector) of length 312
    return max(0, x[30])
def l504_31(x):
    # x is a list (or vector) of length 312
    return max(0, x[31])
def l504_32(x):
    # x is a list (or vector) of length 312
    return max(0, x[32])
def l504_33(x):
    # x is a list (or vector) of length 312
    return max(0, x[33])
def l504_34(x):
    # x is a list (or vector) of length 312
    return max(0, x[34])
def l504_35(x):
    # x is a list (or vector) of length 312
    return max(0, x[35])
def l504_36(x):
    # x is a list (or vector) of length 312
    return max(0, x[36])
def l504_37(x):
    # x is a list (or vector) of length 312
    return max(0, x[37])
def l504_38(x):
    # x is a list (or vector) of length 312
    return max(0, x[38])
def l504_39(x):
    # x is a list (or vector) of length 312
    return max(0, x[39])
def l504_40(x):
    # x is a list (or vector) of length 312
    return max(0, x[40])
def l504_41(x):
    # x is a list (or vector) of length 312
    return max(0, x[41])
def l504_42(x):
    # x is a list (or vector) of length 312
    return max(0, x[42])
def l504_43(x):
    # x is a list (or vector) of length 312
    return max(0, x[43])
def l504_44(x):
    # x is a list (or vector) of length 312
    return max(0, x[44])
def l504_45(x):
    # x is a list (or vector) of length 312
    return max(0, x[45])
def l504_46(x):
    # x is a list (or vector) of length 312
    return max(0, x[46])
def l504_47(x):
    # x is a list (or vector) of length 312
    return max(0, x[47])
def l504_48(x):
    # x is a list (or vector) of length 312
    return max(0, x[48])
def l504_49(x):
    # x is a list (or vector) of length 312
    return max(0, x[49])
def l504_50(x):
    # x is a list (or vector) of length 312
    return max(0, x[50])
def l504_51(x):
    # x is a list (or vector) of length 312
    return max(0, x[51])
def l504_52(x):
    # x is a list (or vector) of length 312
    return max(0, x[52])
def l504_53(x):
    # x is a list (or vector) of length 312
    return max(0, x[53])
def l504_54(x):
    # x is a list (or vector) of length 312
    return max(0, x[54])
def l504_55(x):
    # x is a list (or vector) of length 312
    return max(0, x[55])
def l504_56(x):
    # x is a list (or vector) of length 312
    return max(0, x[56])
def l504_57(x):
    # x is a list (or vector) of length 312
    return max(0, x[57])
def l504_58(x):
    # x is a list (or vector) of length 312
    return max(0, x[58])
def l504_59(x):
    # x is a list (or vector) of length 312
    return max(0, x[59])
def l504_60(x):
    # x is a list (or vector) of length 312
    return max(0, x[60])
def l504_61(x):
    # x is a list (or vector) of length 312
    return max(0, x[61])
def l504_62(x):
    # x is a list (or vector) of length 312
    return max(0, x[62])
def l504_63(x):
    # x is a list (or vector) of length 312
    return max(0, x[63])
def l504_64(x):
    # x is a list (or vector) of length 312
    return max(0, x[64])
def l504_65(x):
    # x is a list (or vector) of length 312
    return max(0, x[65])
def l504_66(x):
    # x is a list (or vector) of length 312
    return max(0, x[66])
def l504_67(x):
    # x is a list (or vector) of length 312
    return max(0, x[67])
def l504_68(x):
    # x is a list (or vector) of length 312
    return max(0, x[68])
def l504_69(x):
    # x is a list (or vector) of length 312
    return max(0, x[69])
def l504_70(x):
    # x is a list (or vector) of length 312
    return max(0, x[70])
def l504_71(x):
    # x is a list (or vector) of length 312
    return max(0, x[71])
def l504_72(x):
    # x is a list (or vector) of length 312
    return max(0, x[72])
def l504_73(x):
    # x is a list (or vector) of length 312
    return max(0, x[73])
def l504_74(x):
    # x is a list (or vector) of length 312
    return max(0, x[74])
def l504_75(x):
    # x is a list (or vector) of length 312
    return max(0, x[75])
def l504_76(x):
    # x is a list (or vector) of length 312
    return max(0, x[76])
def l504_77(x):
    # x is a list (or vector) of length 312
    return max(0, x[77])
def l504_78(x):
    # x is a list (or vector) of length 312
    return max(0, x[78])
def l504_79(x):
    # x is a list (or vector) of length 312
    return max(0, x[79])
def l504_80(x):
    # x is a list (or vector) of length 312
    return max(0, x[80])
def l504_81(x):
    # x is a list (or vector) of length 312
    return max(0, x[81])
def l504_82(x):
    # x is a list (or vector) of length 312
    return max(0, x[82])
def l504_83(x):
    # x is a list (or vector) of length 312
    return max(0, x[83])
def l504_84(x):
    # x is a list (or vector) of length 312
    return max(0, x[84])
def l504_85(x):
    # x is a list (or vector) of length 312
    return max(0, x[85])
def l504_86(x):
    # x is a list (or vector) of length 312
    return max(0, x[86])
def l504_87(x):
    # x is a list (or vector) of length 312
    return max(0, x[87])
def l504_88(x):
    # x is a list (or vector) of length 312
    return max(0, x[88])
def l504_89(x):
    # x is a list (or vector) of length 312
    return max(0, x[89])
def l504_90(x):
    # x is a list (or vector) of length 312
    return max(0, x[90])
def l504_91(x):
    # x is a list (or vector) of length 312
    return max(0, x[91])
def l504_92(x):
    # x is a list (or vector) of length 312
    return max(0, x[92])
def l504_93(x):
    # x is a list (or vector) of length 312
    return max(0, x[93])
def l504_94(x):
    # x is a list (or vector) of length 312
    return max(0, x[94])
def l504_95(x):
    # x is a list (or vector) of length 312
    return max(0, x[95])
def l504_96(x):
    # x is a list (or vector) of length 312
    return max(0, x[96])
def l504_97(x):
    # x is a list (or vector) of length 312
    return max(0, x[97])
def l504_98(x):
    # x is a list (or vector) of length 312
    return max(0, x[98])
def l504_99(x):
    # x is a list (or vector) of length 312
    return max(0, x[99])
def l504_100(x):
    # x is a list (or vector) of length 312
    return max(0, x[100])
def l504_101(x):
    # x is a list (or vector) of length 312
    return max(0, x[101])
def l504_102(x):
    # x is a list (or vector) of length 312
    return max(0, x[102])
def l504_103(x):
    # x is a list (or vector) of length 312
    return max(0, x[103])
def l504_104(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[104] + -1.0*x[128] + 1.0)
def l504_105(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[105] + -1.0*x[129] + 1.0)
def l504_106(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[106] + -1.0*x[130] + 1.0)
def l504_107(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[107] + -1.0*x[131] + 1.0)
def l504_108(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[108] + -1.0*x[132] + 1.0)
def l504_109(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[109] + -1.0*x[133] + 1.0)
def l504_110(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[110] + -1.0*x[134] + 1.0)
def l504_111(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[111] + -1.0*x[135] + 1.0)
def l504_112(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[112] + -1.0*x[136] + 1.0)
def l504_113(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[113] + -1.0*x[137] + 1.0)
def l504_114(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[114] + -1.0*x[138] + 1.0)
def l504_115(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[115] + -1.0*x[139] + 1.0)
def l504_116(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[116] + -1.0*x[140] + 1.0)
def l504_117(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[117] + -1.0*x[141] + 1.0)
def l504_118(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[118] + -1.0*x[142] + 1.0)
def l504_119(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[119] + -1.0*x[143] + 1.0)
def l504_120(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[120] + -1.0*x[144] + 1.0)
def l504_121(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[121] + -1.0*x[145] + 1.0)
def l504_122(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[122] + -1.0*x[146] + 1.0)
def l504_123(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[123] + -1.0*x[147] + 1.0)
def l504_124(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[124] + -1.0*x[148] + 1.0)
def l504_125(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[125] + -1.0*x[149] + 1.0)
def l504_126(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[126] + -1.0*x[150] + 1.0)
def l504_127(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[127] + -1.0*x[151] + 1.0)
def l504_128(x):
    # x is a list (or vector) of length 312
    return max(0, x[176])
def l504_129(x):
    # x is a list (or vector) of length 312
    return max(0, x[177])
def l504_130(x):
    # x is a list (or vector) of length 312
    return max(0, x[178])
def l504_131(x):
    # x is a list (or vector) of length 312
    return max(0, x[179])
def l504_132(x):
    # x is a list (or vector) of length 312
    return max(0, x[180])
def l504_133(x):
    # x is a list (or vector) of length 312
    return max(0, x[181])
def l504_134(x):
    # x is a list (or vector) of length 312
    return max(0, x[182])
def l504_135(x):
    # x is a list (or vector) of length 312
    return max(0, x[183])
def l504_136(x):
    # x is a list (or vector) of length 312
    return max(0, x[152])
def l504_137(x):
    # x is a list (or vector) of length 312
    return max(0, x[153])
def l504_138(x):
    # x is a list (or vector) of length 312
    return max(0, x[154])
def l504_139(x):
    # x is a list (or vector) of length 312
    return max(0, x[155])
def l504_140(x):
    # x is a list (or vector) of length 312
    return max(0, x[156])
def l504_141(x):
    # x is a list (or vector) of length 312
    return max(0, x[157])
def l504_142(x):
    # x is a list (or vector) of length 312
    return max(0, x[158])
def l504_143(x):
    # x is a list (or vector) of length 312
    return max(0, x[159])
def l504_144(x):
    # x is a list (or vector) of length 312
    return max(0, x[160])
def l504_145(x):
    # x is a list (or vector) of length 312
    return max(0, x[161])
def l504_146(x):
    # x is a list (or vector) of length 312
    return max(0, x[162])
def l504_147(x):
    # x is a list (or vector) of length 312
    return max(0, x[163])
def l504_148(x):
    # x is a list (or vector) of length 312
    return max(0, x[164])
def l504_149(x):
    # x is a list (or vector) of length 312
    return max(0, x[165])
def l504_150(x):
    # x is a list (or vector) of length 312
    return max(0, x[166])
def l504_151(x):
    # x is a list (or vector) of length 312
    return max(0, x[167])
def l504_152(x):
    # x is a list (or vector) of length 312
    return max(0, x[168])
def l504_153(x):
    # x is a list (or vector) of length 312
    return max(0, x[169])
def l504_154(x):
    # x is a list (or vector) of length 312
    return max(0, x[170])
def l504_155(x):
    # x is a list (or vector) of length 312
    return max(0, x[171])
def l504_156(x):
    # x is a list (or vector) of length 312
    return max(0, x[172])
def l504_157(x):
    # x is a list (or vector) of length 312
    return max(0, x[173])
def l504_158(x):
    # x is a list (or vector) of length 312
    return max(0, x[174])
def l504_159(x):
    # x is a list (or vector) of length 312
    return max(0, x[175])
def l504_160(x):
    # x is a list (or vector) of length 312
    return max(0, x[184])
def l504_161(x):
    # x is a list (or vector) of length 312
    return max(0, x[185])
def l504_162(x):
    # x is a list (or vector) of length 312
    return max(0, x[186])
def l504_163(x):
    # x is a list (or vector) of length 312
    return max(0, x[187])
def l504_164(x):
    # x is a list (or vector) of length 312
    return max(0, x[188])
def l504_165(x):
    # x is a list (or vector) of length 312
    return max(0, x[189])
def l504_166(x):
    # x is a list (or vector) of length 312
    return max(0, x[190])
def l504_167(x):
    # x is a list (or vector) of length 312
    return max(0, x[191])
def l504_168(x):
    # x is a list (or vector) of length 312
    return max(0, x[192])
def l504_169(x):
    # x is a list (or vector) of length 312
    return max(0, x[193])
def l504_170(x):
    # x is a list (or vector) of length 312
    return max(0, x[194])
def l504_171(x):
    # x is a list (or vector) of length 312
    return max(0, x[195])
def l504_172(x):
    # x is a list (or vector) of length 312
    return max(0, x[196])
def l504_173(x):
    # x is a list (or vector) of length 312
    return max(0, x[197])
def l504_174(x):
    # x is a list (or vector) of length 312
    return max(0, x[198])
def l504_175(x):
    # x is a list (or vector) of length 312
    return max(0, x[199])
def l504_176(x):
    # x is a list (or vector) of length 312
    return max(0, x[200])
def l504_177(x):
    # x is a list (or vector) of length 312
    return max(0, x[201])
def l504_178(x):
    # x is a list (or vector) of length 312
    return max(0, x[202])
def l504_179(x):
    # x is a list (or vector) of length 312
    return max(0, x[203])
def l504_180(x):
    # x is a list (or vector) of length 312
    return max(0, x[204])
def l504_181(x):
    # x is a list (or vector) of length 312
    return max(0, x[205])
def l504_182(x):
    # x is a list (or vector) of length 312
    return max(0, x[206])
def l504_183(x):
    # x is a list (or vector) of length 312
    return max(0, x[207])
def l504_184(x):
    # x is a list (or vector) of length 312
    return max(0, x[208])
def l504_185(x):
    # x is a list (or vector) of length 312
    return max(0, x[209])
def l504_186(x):
    # x is a list (or vector) of length 312
    return max(0, x[210])
def l504_187(x):
    # x is a list (or vector) of length 312
    return max(0, x[211])
def l504_188(x):
    # x is a list (or vector) of length 312
    return max(0, x[212])
def l504_189(x):
    # x is a list (or vector) of length 312
    return max(0, x[213])
def l504_190(x):
    # x is a list (or vector) of length 312
    return max(0, x[214])
def l504_191(x):
    # x is a list (or vector) of length 312
    return max(0, x[215])
def l504_192(x):
    # x is a list (or vector) of length 312
    return max(0, x[216])
def l504_193(x):
    # x is a list (or vector) of length 312
    return max(0, x[217])
def l504_194(x):
    # x is a list (or vector) of length 312
    return max(0, x[218])
def l504_195(x):
    # x is a list (or vector) of length 312
    return max(0, x[219])
def l504_196(x):
    # x is a list (or vector) of length 312
    return max(0, x[220])
def l504_197(x):
    # x is a list (or vector) of length 312
    return max(0, x[221])
def l504_198(x):
    # x is a list (or vector) of length 312
    return max(0, x[222])
def l504_199(x):
    # x is a list (or vector) of length 312
    return max(0, x[223])
def l504_200(x):
    # x is a list (or vector) of length 312
    return max(0, x[224])
def l504_201(x):
    # x is a list (or vector) of length 312
    return max(0, x[225])
def l504_202(x):
    # x is a list (or vector) of length 312
    return max(0, x[226])
def l504_203(x):
    # x is a list (or vector) of length 312
    return max(0, x[227])
def l504_204(x):
    # x is a list (or vector) of length 312
    return max(0, x[228])
def l504_205(x):
    # x is a list (or vector) of length 312
    return max(0, x[229])
def l504_206(x):
    # x is a list (or vector) of length 312
    return max(0, x[230])
def l504_207(x):
    # x is a list (or vector) of length 312
    return max(0, x[231])
def l504_208(x):
    # x is a list (or vector) of length 312
    return max(0, x[232])
def l504_209(x):
    # x is a list (or vector) of length 312
    return max(0, x[233])
def l504_210(x):
    # x is a list (or vector) of length 312
    return max(0, x[234])
def l504_211(x):
    # x is a list (or vector) of length 312
    return max(0, x[235])
def l504_212(x):
    # x is a list (or vector) of length 312
    return max(0, x[236])
def l504_213(x):
    # x is a list (or vector) of length 312
    return max(0, x[237])
def l504_214(x):
    # x is a list (or vector) of length 312
    return max(0, x[238])
def l504_215(x):
    # x is a list (or vector) of length 312
    return max(0, x[239])
def l504_216(x):
    # x is a list (or vector) of length 312
    return max(0, x[240])
def l504_217(x):
    # x is a list (or vector) of length 312
    return max(0, x[241])
def l504_218(x):
    # x is a list (or vector) of length 312
    return max(0, x[242])
def l504_219(x):
    # x is a list (or vector) of length 312
    return max(0, x[243])
def l504_220(x):
    # x is a list (or vector) of length 312
    return max(0, x[244])
def l504_221(x):
    # x is a list (or vector) of length 312
    return max(0, x[245])
def l504_222(x):
    # x is a list (or vector) of length 312
    return max(0, x[246])
def l504_223(x):
    # x is a list (or vector) of length 312
    return max(0, x[247])
def l504_224(x):
    # x is a list (or vector) of length 312
    return max(0, x[248])
def l504_225(x):
    # x is a list (or vector) of length 312
    return max(0, x[249])
def l504_226(x):
    # x is a list (or vector) of length 312
    return max(0, x[250])
def l504_227(x):
    # x is a list (or vector) of length 312
    return max(0, x[251])
def l504_228(x):
    # x is a list (or vector) of length 312
    return max(0, x[252])
def l504_229(x):
    # x is a list (or vector) of length 312
    return max(0, x[253])
def l504_230(x):
    # x is a list (or vector) of length 312
    return max(0, x[254])
def l504_231(x):
    # x is a list (or vector) of length 312
    return max(0, x[255])
def l504_232(x):
    # x is a list (or vector) of length 312
    return max(0, x[256])
def l504_233(x):
    # x is a list (or vector) of length 312
    return max(0, x[257])
def l504_234(x):
    # x is a list (or vector) of length 312
    return max(0, x[258])
def l504_235(x):
    # x is a list (or vector) of length 312
    return max(0, x[259])
def l504_236(x):
    # x is a list (or vector) of length 312
    return max(0, x[260])
def l504_237(x):
    # x is a list (or vector) of length 312
    return max(0, x[261])
def l504_238(x):
    # x is a list (or vector) of length 312
    return max(0, x[262])
def l504_239(x):
    # x is a list (or vector) of length 312
    return max(0, x[263])
def l504_240(x):
    # x is a list (or vector) of length 312
    return max(0, x[264])
def l504_241(x):
    # x is a list (or vector) of length 312
    return max(0, x[265])
def l504_242(x):
    # x is a list (or vector) of length 312
    return max(0, x[266])
def l504_243(x):
    # x is a list (or vector) of length 312
    return max(0, x[267])
def l504_244(x):
    # x is a list (or vector) of length 312
    return max(0, x[268])
def l504_245(x):
    # x is a list (or vector) of length 312
    return max(0, x[269])
def l504_246(x):
    # x is a list (or vector) of length 312
    return max(0, x[270])
def l504_247(x):
    # x is a list (or vector) of length 312
    return max(0, x[271])
def l504_248(x):
    # x is a list (or vector) of length 312
    return max(0, x[272])
def l504_249(x):
    # x is a list (or vector) of length 312
    return max(0, x[273])
def l504_250(x):
    # x is a list (or vector) of length 312
    return max(0, x[274])
def l504_251(x):
    # x is a list (or vector) of length 312
    return max(0, x[275])
def l504_252(x):
    # x is a list (or vector) of length 312
    return max(0, x[276])
def l504_253(x):
    # x is a list (or vector) of length 312
    return max(0, x[277])
def l504_254(x):
    # x is a list (or vector) of length 312
    return max(0, x[278])
def l504_255(x):
    # x is a list (or vector) of length 312
    return max(0, x[279])
def l504_256(x):
    # x is a list (or vector) of length 312
    return max(0, x[280])
def l504_257(x):
    # x is a list (or vector) of length 312
    return max(0, x[281])
def l504_258(x):
    # x is a list (or vector) of length 312
    return max(0, x[282])
def l504_259(x):
    # x is a list (or vector) of length 312
    return max(0, x[283])
def l504_260(x):
    # x is a list (or vector) of length 312
    return max(0, x[284])
def l504_261(x):
    # x is a list (or vector) of length 312
    return max(0, x[285])
def l504_262(x):
    # x is a list (or vector) of length 312
    return max(0, x[286])
def l504_263(x):
    # x is a list (or vector) of length 312
    return max(0, x[287])
def l504_264(x):
    # x is a list (or vector) of length 312
    return max(0, x[288])
def l504_265(x):
    # x is a list (or vector) of length 312
    return max(0, x[289])
def l504_266(x):
    # x is a list (or vector) of length 312
    return max(0, x[290])
def l504_267(x):
    # x is a list (or vector) of length 312
    return max(0, x[291])
def l504_268(x):
    # x is a list (or vector) of length 312
    return max(0, x[292])
def l504_269(x):
    # x is a list (or vector) of length 312
    return max(0, x[293])
def l504_270(x):
    # x is a list (or vector) of length 312
    return max(0, x[294])
def l504_271(x):
    # x is a list (or vector) of length 312
    return max(0, x[295])
def l504_272(x):
    # x is a list (or vector) of length 312
    return max(0, x[296])
def l504_273(x):
    # x is a list (or vector) of length 312
    return max(0, x[297])
def l504_274(x):
    # x is a list (or vector) of length 312
    return max(0, x[298])
def l504_275(x):
    # x is a list (or vector) of length 312
    return max(0, x[299])
def l504_276(x):
    # x is a list (or vector) of length 312
    return max(0, x[300])
def l504_277(x):
    # x is a list (or vector) of length 312
    return max(0, x[301])
def l504_278(x):
    # x is a list (or vector) of length 312
    return max(0, x[302])
def l504_279(x):
    # x is a list (or vector) of length 312
    return max(0, x[303])
def l504_280(x):
    # x is a list (or vector) of length 312
    return max(0, x[304])
def l504_281(x):
    # x is a list (or vector) of length 312
    return max(0, x[305])
def l504_282(x):
    # x is a list (or vector) of length 312
    return max(0, x[306])
def l504_283(x):
    # x is a list (or vector) of length 312
    return max(0, x[307])
def l504_284(x):
    # x is a list (or vector) of length 312
    return max(0, x[308])
def l504_285(x):
    # x is a list (or vector) of length 312
    return max(0, x[309])
def l504_286(x):
    # x is a list (or vector) of length 312
    return max(0, x[310])
def l504_287(x):
    # x is a list (or vector) of length 312
    return max(0, x[311])
def l504_(x):
    # x is a list (or vector) of length 312
    return [
        l504_0(x),
        l504_1(x),
        l504_2(x),
        l504_3(x),
        l504_4(x),
        l504_5(x),
        l504_6(x),
        l504_7(x),
        l504_8(x),
        l504_9(x),
        l504_10(x),
        l504_11(x),
        l504_12(x),
        l504_13(x),
        l504_14(x),
        l504_15(x),
        l504_16(x),
        l504_17(x),
        l504_18(x),
        l504_19(x),
        l504_20(x),
        l504_21(x),
        l504_22(x),
        l504_23(x),
        l504_24(x),
        l504_25(x),
        l504_26(x),
        l504_27(x),
        l504_28(x),
        l504_29(x),
        l504_30(x),
        l504_31(x),
        l504_32(x),
        l504_33(x),
        l504_34(x),
        l504_35(x),
        l504_36(x),
        l504_37(x),
        l504_38(x),
        l504_39(x),
        l504_40(x),
        l504_41(x),
        l504_42(x),
        l504_43(x),
        l504_44(x),
        l504_45(x),
        l504_46(x),
        l504_47(x),
        l504_48(x),
        l504_49(x),
        l504_50(x),
        l504_51(x),
        l504_52(x),
        l504_53(x),
        l504_54(x),
        l504_55(x),
        l504_56(x),
        l504_57(x),
        l504_58(x),
        l504_59(x),
        l504_60(x),
        l504_61(x),
        l504_62(x),
        l504_63(x),
        l504_64(x),
        l504_65(x),
        l504_66(x),
        l504_67(x),
        l504_68(x),
        l504_69(x),
        l504_70(x),
        l504_71(x),
        l504_72(x),
        l504_73(x),
        l504_74(x),
        l504_75(x),
        l504_76(x),
        l504_77(x),
        l504_78(x),
        l504_79(x),
        l504_80(x),
        l504_81(x),
        l504_82(x),
        l504_83(x),
        l504_84(x),
        l504_85(x),
        l504_86(x),
        l504_87(x),
        l504_88(x),
        l504_89(x),
        l504_90(x),
        l504_91(x),
        l504_92(x),
        l504_93(x),
        l504_94(x),
        l504_95(x),
        l504_96(x),
        l504_97(x),
        l504_98(x),
        l504_99(x),
        l504_100(x),
        l504_101(x),
        l504_102(x),
        l504_103(x),
        l504_104(x),
        l504_105(x),
        l504_106(x),
        l504_107(x),
        l504_108(x),
        l504_109(x),
        l504_110(x),
        l504_111(x),
        l504_112(x),
        l504_113(x),
        l504_114(x),
        l504_115(x),
        l504_116(x),
        l504_117(x),
        l504_118(x),
        l504_119(x),
        l504_120(x),
        l504_121(x),
        l504_122(x),
        l504_123(x),
        l504_124(x),
        l504_125(x),
        l504_126(x),
        l504_127(x),
        l504_128(x),
        l504_129(x),
        l504_130(x),
        l504_131(x),
        l504_132(x),
        l504_133(x),
        l504_134(x),
        l504_135(x),
        l504_136(x),
        l504_137(x),
        l504_138(x),
        l504_139(x),
        l504_140(x),
        l504_141(x),
        l504_142(x),
        l504_143(x),
        l504_144(x),
        l504_145(x),
        l504_146(x),
        l504_147(x),
        l504_148(x),
        l504_149(x),
        l504_150(x),
        l504_151(x),
        l504_152(x),
        l504_153(x),
        l504_154(x),
        l504_155(x),
        l504_156(x),
        l504_157(x),
        l504_158(x),
        l504_159(x),
        l504_160(x),
        l504_161(x),
        l504_162(x),
        l504_163(x),
        l504_164(x),
        l504_165(x),
        l504_166(x),
        l504_167(x),
        l504_168(x),
        l504_169(x),
        l504_170(x),
        l504_171(x),
        l504_172(x),
        l504_173(x),
        l504_174(x),
        l504_175(x),
        l504_176(x),
        l504_177(x),
        l504_178(x),
        l504_179(x),
        l504_180(x),
        l504_181(x),
        l504_182(x),
        l504_183(x),
        l504_184(x),
        l504_185(x),
        l504_186(x),
        l504_187(x),
        l504_188(x),
        l504_189(x),
        l504_190(x),
        l504_191(x),
        l504_192(x),
        l504_193(x),
        l504_194(x),
        l504_195(x),
        l504_196(x),
        l504_197(x),
        l504_198(x),
        l504_199(x),
        l504_200(x),
        l504_201(x),
        l504_202(x),
        l504_203(x),
        l504_204(x),
        l504_205(x),
        l504_206(x),
        l504_207(x),
        l504_208(x),
        l504_209(x),
        l504_210(x),
        l504_211(x),
        l504_212(x),
        l504_213(x),
        l504_214(x),
        l504_215(x),
        l504_216(x),
        l504_217(x),
        l504_218(x),
        l504_219(x),
        l504_220(x),
        l504_221(x),
        l504_222(x),
        l504_223(x),
        l504_224(x),
        l504_225(x),
        l504_226(x),
        l504_227(x),
        l504_228(x),
        l504_229(x),
        l504_230(x),
        l504_231(x),
        l504_232(x),
        l504_233(x),
        l504_234(x),
        l504_235(x),
        l504_236(x),
        l504_237(x),
        l504_238(x),
        l504_239(x),
        l504_240(x),
        l504_241(x),
        l504_242(x),
        l504_243(x),
        l504_244(x),
        l504_245(x),
        l504_246(x),
        l504_247(x),
        l504_248(x),
        l504_249(x),
        l504_250(x),
        l504_251(x),
        l504_252(x),
        l504_253(x),
        l504_254(x),
        l504_255(x),
        l504_256(x),
        l504_257(x),
        l504_258(x),
        l504_259(x),
        l504_260(x),
        l504_261(x),
        l504_262(x),
        l504_263(x),
        l504_264(x),
        l504_265(x),
        l504_266(x),
        l504_267(x),
        l504_268(x),
        l504_269(x),
        l504_270(x),
        l504_271(x),
        l504_272(x),
        l504_273(x),
        l504_274(x),
        l504_275(x),
        l504_276(x),
        l504_277(x),
        l504_278(x),
        l504_279(x),
        l504_280(x),
        l504_281(x),
        l504_282(x),
        l504_283(x),
        l504_284(x),
        l504_285(x),
        l504_286(x),
        l504_287(x),
    ]