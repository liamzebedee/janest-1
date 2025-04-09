import numpy as np




# Generated from reverse engineering
def l168_g(x: np.ndarray) -> np.ndarray:
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




def l168_0(x):
    # x is a list (or vector) of length 312
    return max(0, x[0])
def l168_1(x):
    # x is a list (or vector) of length 312
    return max(0, x[1])
def l168_2(x):
    # x is a list (or vector) of length 312
    return max(0, x[2])
def l168_3(x):
    # x is a list (or vector) of length 312
    return max(0, x[3])
def l168_4(x):
    # x is a list (or vector) of length 312
    return max(0, x[4])
def l168_5(x):
    # x is a list (or vector) of length 312
    return max(0, x[5])
def l168_6(x):
    # x is a list (or vector) of length 312
    return max(0, x[6])
def l168_7(x):
    # x is a list (or vector) of length 312
    return max(0, x[7])
def l168_8(x):
    # x is a list (or vector) of length 312
    return max(0, x[8])
def l168_9(x):
    # x is a list (or vector) of length 312
    return max(0, x[9])
def l168_10(x):
    # x is a list (or vector) of length 312
    return max(0, x[10])
def l168_11(x):
    # x is a list (or vector) of length 312
    return max(0, x[11])
def l168_12(x):
    # x is a list (or vector) of length 312
    return max(0, x[12])
def l168_13(x):
    # x is a list (or vector) of length 312
    return max(0, x[13])
def l168_14(x):
    # x is a list (or vector) of length 312
    return max(0, x[14])
def l168_15(x):
    # x is a list (or vector) of length 312
    return max(0, x[15])
def l168_16(x):
    # x is a list (or vector) of length 312
    return max(0, x[16])
def l168_17(x):
    # x is a list (or vector) of length 312
    return max(0, x[17])
def l168_18(x):
    # x is a list (or vector) of length 312
    return max(0, x[18])
def l168_19(x):
    # x is a list (or vector) of length 312
    return max(0, x[19])
def l168_20(x):
    # x is a list (or vector) of length 312
    return max(0, x[20])
def l168_21(x):
    # x is a list (or vector) of length 312
    return max(0, x[21])
def l168_22(x):
    # x is a list (or vector) of length 312
    return max(0, x[22])
def l168_23(x):
    # x is a list (or vector) of length 312
    return max(0, x[23])
def l168_24(x):
    # x is a list (or vector) of length 312
    return max(0, x[24])
def l168_25(x):
    # x is a list (or vector) of length 312
    return max(0, x[25])
def l168_26(x):
    # x is a list (or vector) of length 312
    return max(0, x[26])
def l168_27(x):
    # x is a list (or vector) of length 312
    return max(0, x[27])
def l168_28(x):
    # x is a list (or vector) of length 312
    return max(0, x[28])
def l168_29(x):
    # x is a list (or vector) of length 312
    return max(0, x[29])
def l168_30(x):
    # x is a list (or vector) of length 312
    return max(0, x[30])
def l168_31(x):
    # x is a list (or vector) of length 312
    return max(0, x[31])
def l168_32(x):
    # x is a list (or vector) of length 312
    return max(0, x[32])
def l168_33(x):
    # x is a list (or vector) of length 312
    return max(0, x[33])
def l168_34(x):
    # x is a list (or vector) of length 312
    return max(0, x[34])
def l168_35(x):
    # x is a list (or vector) of length 312
    return max(0, x[35])
def l168_36(x):
    # x is a list (or vector) of length 312
    return max(0, x[36])
def l168_37(x):
    # x is a list (or vector) of length 312
    return max(0, x[37])
def l168_38(x):
    # x is a list (or vector) of length 312
    return max(0, x[38])
def l168_39(x):
    # x is a list (or vector) of length 312
    return max(0, x[39])
def l168_40(x):
    # x is a list (or vector) of length 312
    return max(0, x[40])
def l168_41(x):
    # x is a list (or vector) of length 312
    return max(0, x[41])
def l168_42(x):
    # x is a list (or vector) of length 312
    return max(0, x[42])
def l168_43(x):
    # x is a list (or vector) of length 312
    return max(0, x[43])
def l168_44(x):
    # x is a list (or vector) of length 312
    return max(0, x[44])
def l168_45(x):
    # x is a list (or vector) of length 312
    return max(0, x[45])
def l168_46(x):
    # x is a list (or vector) of length 312
    return max(0, x[46])
def l168_47(x):
    # x is a list (or vector) of length 312
    return max(0, x[47])
def l168_48(x):
    # x is a list (or vector) of length 312
    return max(0, x[48])
def l168_49(x):
    # x is a list (or vector) of length 312
    return max(0, x[49])
def l168_50(x):
    # x is a list (or vector) of length 312
    return max(0, x[50])
def l168_51(x):
    # x is a list (or vector) of length 312
    return max(0, x[51])
def l168_52(x):
    # x is a list (or vector) of length 312
    return max(0, x[52])
def l168_53(x):
    # x is a list (or vector) of length 312
    return max(0, x[53])
def l168_54(x):
    # x is a list (or vector) of length 312
    return max(0, x[54])
def l168_55(x):
    # x is a list (or vector) of length 312
    return max(0, x[55])
def l168_56(x):
    # x is a list (or vector) of length 312
    return max(0, x[56])
def l168_57(x):
    # x is a list (or vector) of length 312
    return max(0, x[57])
def l168_58(x):
    # x is a list (or vector) of length 312
    return max(0, x[58])
def l168_59(x):
    # x is a list (or vector) of length 312
    return max(0, x[59])
def l168_60(x):
    # x is a list (or vector) of length 312
    return max(0, x[60])
def l168_61(x):
    # x is a list (or vector) of length 312
    return max(0, x[61])
def l168_62(x):
    # x is a list (or vector) of length 312
    return max(0, x[62])
def l168_63(x):
    # x is a list (or vector) of length 312
    return max(0, x[63])
def l168_64(x):
    # x is a list (or vector) of length 312
    return max(0, x[64])
def l168_65(x):
    # x is a list (or vector) of length 312
    return max(0, x[65])
def l168_66(x):
    # x is a list (or vector) of length 312
    return max(0, x[66])
def l168_67(x):
    # x is a list (or vector) of length 312
    return max(0, x[67])
def l168_68(x):
    # x is a list (or vector) of length 312
    return max(0, x[68])
def l168_69(x):
    # x is a list (or vector) of length 312
    return max(0, x[69])
def l168_70(x):
    # x is a list (or vector) of length 312
    return max(0, x[70])
def l168_71(x):
    # x is a list (or vector) of length 312
    return max(0, x[71])
def l168_72(x):
    # x is a list (or vector) of length 312
    return max(0, x[72])
def l168_73(x):
    # x is a list (or vector) of length 312
    return max(0, x[73])
def l168_74(x):
    # x is a list (or vector) of length 312
    return max(0, x[74])
def l168_75(x):
    # x is a list (or vector) of length 312
    return max(0, x[75])
def l168_76(x):
    # x is a list (or vector) of length 312
    return max(0, x[76])
def l168_77(x):
    # x is a list (or vector) of length 312
    return max(0, x[77])
def l168_78(x):
    # x is a list (or vector) of length 312
    return max(0, x[78])
def l168_79(x):
    # x is a list (or vector) of length 312
    return max(0, x[79])
def l168_80(x):
    # x is a list (or vector) of length 312
    return max(0, x[80])
def l168_81(x):
    # x is a list (or vector) of length 312
    return max(0, x[81])
def l168_82(x):
    # x is a list (or vector) of length 312
    return max(0, x[82])
def l168_83(x):
    # x is a list (or vector) of length 312
    return max(0, x[83])
def l168_84(x):
    # x is a list (or vector) of length 312
    return max(0, x[84])
def l168_85(x):
    # x is a list (or vector) of length 312
    return max(0, x[85])
def l168_86(x):
    # x is a list (or vector) of length 312
    return max(0, x[86])
def l168_87(x):
    # x is a list (or vector) of length 312
    return max(0, x[87])
def l168_88(x):
    # x is a list (or vector) of length 312
    return max(0, x[88])
def l168_89(x):
    # x is a list (or vector) of length 312
    return max(0, x[89])
def l168_90(x):
    # x is a list (or vector) of length 312
    return max(0, x[90])
def l168_91(x):
    # x is a list (or vector) of length 312
    return max(0, x[91])
def l168_92(x):
    # x is a list (or vector) of length 312
    return max(0, x[92])
def l168_93(x):
    # x is a list (or vector) of length 312
    return max(0, x[93])
def l168_94(x):
    # x is a list (or vector) of length 312
    return max(0, x[94])
def l168_95(x):
    # x is a list (or vector) of length 312
    return max(0, x[95])
def l168_96(x):
    # x is a list (or vector) of length 312
    return max(0, x[96])
def l168_97(x):
    # x is a list (or vector) of length 312
    return max(0, x[97])
def l168_98(x):
    # x is a list (or vector) of length 312
    return max(0, x[98])
def l168_99(x):
    # x is a list (or vector) of length 312
    return max(0, x[99])
def l168_100(x):
    # x is a list (or vector) of length 312
    return max(0, x[100])
def l168_101(x):
    # x is a list (or vector) of length 312
    return max(0, x[101])
def l168_102(x):
    # x is a list (or vector) of length 312
    return max(0, x[102])
def l168_103(x):
    # x is a list (or vector) of length 312
    return max(0, x[103])
def l168_104(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[104] + -1.0*x[128] + 1.0)
def l168_105(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[105] + -1.0*x[129] + 1.0)
def l168_106(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[106] + -1.0*x[130] + 1.0)
def l168_107(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[107] + -1.0*x[131] + 1.0)
def l168_108(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[108] + -1.0*x[132] + 1.0)
def l168_109(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[109] + -1.0*x[133] + 1.0)
def l168_110(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[110] + -1.0*x[134] + 1.0)
def l168_111(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[111] + -1.0*x[135] + 1.0)
def l168_112(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[112] + -1.0*x[136] + 1.0)
def l168_113(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[113] + -1.0*x[137] + 1.0)
def l168_114(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[114] + -1.0*x[138] + 1.0)
def l168_115(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[115] + -1.0*x[139] + 1.0)
def l168_116(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[116] + -1.0*x[140] + 1.0)
def l168_117(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[117] + -1.0*x[141] + 1.0)
def l168_118(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[118] + -1.0*x[142] + 1.0)
def l168_119(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[119] + -1.0*x[143] + 1.0)
def l168_120(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[120] + -1.0*x[144] + 1.0)
def l168_121(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[121] + -1.0*x[145] + 1.0)
def l168_122(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[122] + -1.0*x[146] + 1.0)
def l168_123(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[123] + -1.0*x[147] + 1.0)
def l168_124(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[124] + -1.0*x[148] + 1.0)
def l168_125(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[125] + -1.0*x[149] + 1.0)
def l168_126(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[126] + -1.0*x[150] + 1.0)
def l168_127(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[127] + -1.0*x[151] + 1.0)
def l168_128(x):
    # x is a list (or vector) of length 312
    return max(0, x[176])
def l168_129(x):
    # x is a list (or vector) of length 312
    return max(0, x[177])
def l168_130(x):
    # x is a list (or vector) of length 312
    return max(0, x[178])
def l168_131(x):
    # x is a list (or vector) of length 312
    return max(0, x[179])
def l168_132(x):
    # x is a list (or vector) of length 312
    return max(0, x[180])
def l168_133(x):
    # x is a list (or vector) of length 312
    return max(0, x[181])
def l168_134(x):
    # x is a list (or vector) of length 312
    return max(0, x[182])
def l168_135(x):
    # x is a list (or vector) of length 312
    return max(0, x[183])
def l168_136(x):
    # x is a list (or vector) of length 312
    return max(0, x[152])
def l168_137(x):
    # x is a list (or vector) of length 312
    return max(0, x[153])
def l168_138(x):
    # x is a list (or vector) of length 312
    return max(0, x[154])
def l168_139(x):
    # x is a list (or vector) of length 312
    return max(0, x[155])
def l168_140(x):
    # x is a list (or vector) of length 312
    return max(0, x[156])
def l168_141(x):
    # x is a list (or vector) of length 312
    return max(0, x[157])
def l168_142(x):
    # x is a list (or vector) of length 312
    return max(0, x[158])
def l168_143(x):
    # x is a list (or vector) of length 312
    return max(0, x[159])
def l168_144(x):
    # x is a list (or vector) of length 312
    return max(0, x[160])
def l168_145(x):
    # x is a list (or vector) of length 312
    return max(0, x[161])
def l168_146(x):
    # x is a list (or vector) of length 312
    return max(0, x[162])
def l168_147(x):
    # x is a list (or vector) of length 312
    return max(0, x[163])
def l168_148(x):
    # x is a list (or vector) of length 312
    return max(0, x[164])
def l168_149(x):
    # x is a list (or vector) of length 312
    return max(0, x[165])
def l168_150(x):
    # x is a list (or vector) of length 312
    return max(0, x[166])
def l168_151(x):
    # x is a list (or vector) of length 312
    return max(0, x[167])
def l168_152(x):
    # x is a list (or vector) of length 312
    return max(0, x[168])
def l168_153(x):
    # x is a list (or vector) of length 312
    return max(0, x[169])
def l168_154(x):
    # x is a list (or vector) of length 312
    return max(0, x[170])
def l168_155(x):
    # x is a list (or vector) of length 312
    return max(0, x[171])
def l168_156(x):
    # x is a list (or vector) of length 312
    return max(0, x[172])
def l168_157(x):
    # x is a list (or vector) of length 312
    return max(0, x[173])
def l168_158(x):
    # x is a list (or vector) of length 312
    return max(0, x[174])
def l168_159(x):
    # x is a list (or vector) of length 312
    return max(0, x[175])
def l168_160(x):
    # x is a list (or vector) of length 312
    return max(0, x[184])
def l168_161(x):
    # x is a list (or vector) of length 312
    return max(0, x[185])
def l168_162(x):
    # x is a list (or vector) of length 312
    return max(0, x[186])
def l168_163(x):
    # x is a list (or vector) of length 312
    return max(0, x[187])
def l168_164(x):
    # x is a list (or vector) of length 312
    return max(0, x[188])
def l168_165(x):
    # x is a list (or vector) of length 312
    return max(0, x[189])
def l168_166(x):
    # x is a list (or vector) of length 312
    return max(0, x[190])
def l168_167(x):
    # x is a list (or vector) of length 312
    return max(0, x[191])
def l168_168(x):
    # x is a list (or vector) of length 312
    return max(0, x[192])
def l168_169(x):
    # x is a list (or vector) of length 312
    return max(0, x[193])
def l168_170(x):
    # x is a list (or vector) of length 312
    return max(0, x[194])
def l168_171(x):
    # x is a list (or vector) of length 312
    return max(0, x[195])
def l168_172(x):
    # x is a list (or vector) of length 312
    return max(0, x[196])
def l168_173(x):
    # x is a list (or vector) of length 312
    return max(0, x[197])
def l168_174(x):
    # x is a list (or vector) of length 312
    return max(0, x[198])
def l168_175(x):
    # x is a list (or vector) of length 312
    return max(0, x[199])
def l168_176(x):
    # x is a list (or vector) of length 312
    return max(0, x[200])
def l168_177(x):
    # x is a list (or vector) of length 312
    return max(0, x[201])
def l168_178(x):
    # x is a list (or vector) of length 312
    return max(0, x[202])
def l168_179(x):
    # x is a list (or vector) of length 312
    return max(0, x[203])
def l168_180(x):
    # x is a list (or vector) of length 312
    return max(0, x[204])
def l168_181(x):
    # x is a list (or vector) of length 312
    return max(0, x[205])
def l168_182(x):
    # x is a list (or vector) of length 312
    return max(0, x[206])
def l168_183(x):
    # x is a list (or vector) of length 312
    return max(0, x[207])
def l168_184(x):
    # x is a list (or vector) of length 312
    return max(0, x[208])
def l168_185(x):
    # x is a list (or vector) of length 312
    return max(0, x[209])
def l168_186(x):
    # x is a list (or vector) of length 312
    return max(0, x[210])
def l168_187(x):
    # x is a list (or vector) of length 312
    return max(0, x[211])
def l168_188(x):
    # x is a list (or vector) of length 312
    return max(0, x[212])
def l168_189(x):
    # x is a list (or vector) of length 312
    return max(0, x[213])
def l168_190(x):
    # x is a list (or vector) of length 312
    return max(0, x[214])
def l168_191(x):
    # x is a list (or vector) of length 312
    return max(0, x[215])
def l168_192(x):
    # x is a list (or vector) of length 312
    return max(0, x[216])
def l168_193(x):
    # x is a list (or vector) of length 312
    return max(0, x[217])
def l168_194(x):
    # x is a list (or vector) of length 312
    return max(0, x[218])
def l168_195(x):
    # x is a list (or vector) of length 312
    return max(0, x[219])
def l168_196(x):
    # x is a list (or vector) of length 312
    return max(0, x[220])
def l168_197(x):
    # x is a list (or vector) of length 312
    return max(0, x[221])
def l168_198(x):
    # x is a list (or vector) of length 312
    return max(0, x[222])
def l168_199(x):
    # x is a list (or vector) of length 312
    return max(0, x[223])
def l168_200(x):
    # x is a list (or vector) of length 312
    return max(0, x[224])
def l168_201(x):
    # x is a list (or vector) of length 312
    return max(0, x[225])
def l168_202(x):
    # x is a list (or vector) of length 312
    return max(0, x[226])
def l168_203(x):
    # x is a list (or vector) of length 312
    return max(0, x[227])
def l168_204(x):
    # x is a list (or vector) of length 312
    return max(0, x[228])
def l168_205(x):
    # x is a list (or vector) of length 312
    return max(0, x[229])
def l168_206(x):
    # x is a list (or vector) of length 312
    return max(0, x[230])
def l168_207(x):
    # x is a list (or vector) of length 312
    return max(0, x[231])
def l168_208(x):
    # x is a list (or vector) of length 312
    return max(0, x[232])
def l168_209(x):
    # x is a list (or vector) of length 312
    return max(0, x[233])
def l168_210(x):
    # x is a list (or vector) of length 312
    return max(0, x[234])
def l168_211(x):
    # x is a list (or vector) of length 312
    return max(0, x[235])
def l168_212(x):
    # x is a list (or vector) of length 312
    return max(0, x[236])
def l168_213(x):
    # x is a list (or vector) of length 312
    return max(0, x[237])
def l168_214(x):
    # x is a list (or vector) of length 312
    return max(0, x[238])
def l168_215(x):
    # x is a list (or vector) of length 312
    return max(0, x[239])
def l168_216(x):
    # x is a list (or vector) of length 312
    return max(0, x[240])
def l168_217(x):
    # x is a list (or vector) of length 312
    return max(0, x[241])
def l168_218(x):
    # x is a list (or vector) of length 312
    return max(0, x[242])
def l168_219(x):
    # x is a list (or vector) of length 312
    return max(0, x[243])
def l168_220(x):
    # x is a list (or vector) of length 312
    return max(0, x[244])
def l168_221(x):
    # x is a list (or vector) of length 312
    return max(0, x[245])
def l168_222(x):
    # x is a list (or vector) of length 312
    return max(0, x[246])
def l168_223(x):
    # x is a list (or vector) of length 312
    return max(0, x[247])
def l168_224(x):
    # x is a list (or vector) of length 312
    return max(0, x[248])
def l168_225(x):
    # x is a list (or vector) of length 312
    return max(0, x[249])
def l168_226(x):
    # x is a list (or vector) of length 312
    return max(0, x[250])
def l168_227(x):
    # x is a list (or vector) of length 312
    return max(0, x[251])
def l168_228(x):
    # x is a list (or vector) of length 312
    return max(0, x[252])
def l168_229(x):
    # x is a list (or vector) of length 312
    return max(0, x[253])
def l168_230(x):
    # x is a list (or vector) of length 312
    return max(0, x[254])
def l168_231(x):
    # x is a list (or vector) of length 312
    return max(0, x[255])
def l168_232(x):
    # x is a list (or vector) of length 312
    return max(0, x[256])
def l168_233(x):
    # x is a list (or vector) of length 312
    return max(0, x[257])
def l168_234(x):
    # x is a list (or vector) of length 312
    return max(0, x[258])
def l168_235(x):
    # x is a list (or vector) of length 312
    return max(0, x[259])
def l168_236(x):
    # x is a list (or vector) of length 312
    return max(0, x[260])
def l168_237(x):
    # x is a list (or vector) of length 312
    return max(0, x[261])
def l168_238(x):
    # x is a list (or vector) of length 312
    return max(0, x[262])
def l168_239(x):
    # x is a list (or vector) of length 312
    return max(0, x[263])
def l168_240(x):
    # x is a list (or vector) of length 312
    return max(0, x[264])
def l168_241(x):
    # x is a list (or vector) of length 312
    return max(0, x[265])
def l168_242(x):
    # x is a list (or vector) of length 312
    return max(0, x[266])
def l168_243(x):
    # x is a list (or vector) of length 312
    return max(0, x[267])
def l168_244(x):
    # x is a list (or vector) of length 312
    return max(0, x[268])
def l168_245(x):
    # x is a list (or vector) of length 312
    return max(0, x[269])
def l168_246(x):
    # x is a list (or vector) of length 312
    return max(0, x[270])
def l168_247(x):
    # x is a list (or vector) of length 312
    return max(0, x[271])
def l168_248(x):
    # x is a list (or vector) of length 312
    return max(0, x[272])
def l168_249(x):
    # x is a list (or vector) of length 312
    return max(0, x[273])
def l168_250(x):
    # x is a list (or vector) of length 312
    return max(0, x[274])
def l168_251(x):
    # x is a list (or vector) of length 312
    return max(0, x[275])
def l168_252(x):
    # x is a list (or vector) of length 312
    return max(0, x[276])
def l168_253(x):
    # x is a list (or vector) of length 312
    return max(0, x[277])
def l168_254(x):
    # x is a list (or vector) of length 312
    return max(0, x[278])
def l168_255(x):
    # x is a list (or vector) of length 312
    return max(0, x[279])
def l168_256(x):
    # x is a list (or vector) of length 312
    return max(0, x[280])
def l168_257(x):
    # x is a list (or vector) of length 312
    return max(0, x[281])
def l168_258(x):
    # x is a list (or vector) of length 312
    return max(0, x[282])
def l168_259(x):
    # x is a list (or vector) of length 312
    return max(0, x[283])
def l168_260(x):
    # x is a list (or vector) of length 312
    return max(0, x[284])
def l168_261(x):
    # x is a list (or vector) of length 312
    return max(0, x[285])
def l168_262(x):
    # x is a list (or vector) of length 312
    return max(0, x[286])
def l168_263(x):
    # x is a list (or vector) of length 312
    return max(0, x[287])
def l168_264(x):
    # x is a list (or vector) of length 312
    return max(0, x[288])
def l168_265(x):
    # x is a list (or vector) of length 312
    return max(0, x[289])
def l168_266(x):
    # x is a list (or vector) of length 312
    return max(0, x[290])
def l168_267(x):
    # x is a list (or vector) of length 312
    return max(0, x[291])
def l168_268(x):
    # x is a list (or vector) of length 312
    return max(0, x[292])
def l168_269(x):
    # x is a list (or vector) of length 312
    return max(0, x[293])
def l168_270(x):
    # x is a list (or vector) of length 312
    return max(0, x[294])
def l168_271(x):
    # x is a list (or vector) of length 312
    return max(0, x[295])
def l168_272(x):
    # x is a list (or vector) of length 312
    return max(0, x[296])
def l168_273(x):
    # x is a list (or vector) of length 312
    return max(0, x[297])
def l168_274(x):
    # x is a list (or vector) of length 312
    return max(0, x[298])
def l168_275(x):
    # x is a list (or vector) of length 312
    return max(0, x[299])
def l168_276(x):
    # x is a list (or vector) of length 312
    return max(0, x[300])
def l168_277(x):
    # x is a list (or vector) of length 312
    return max(0, x[301])
def l168_278(x):
    # x is a list (or vector) of length 312
    return max(0, x[302])
def l168_279(x):
    # x is a list (or vector) of length 312
    return max(0, x[303])
def l168_280(x):
    # x is a list (or vector) of length 312
    return max(0, x[304])
def l168_281(x):
    # x is a list (or vector) of length 312
    return max(0, x[305])
def l168_282(x):
    # x is a list (or vector) of length 312
    return max(0, x[306])
def l168_283(x):
    # x is a list (or vector) of length 312
    return max(0, x[307])
def l168_284(x):
    # x is a list (or vector) of length 312
    return max(0, x[308])
def l168_285(x):
    # x is a list (or vector) of length 312
    return max(0, x[309])
def l168_286(x):
    # x is a list (or vector) of length 312
    return max(0, x[310])
def l168_287(x):
    # x is a list (or vector) of length 312
    return max(0, x[311])
def l168_(x):
    # x is a list (or vector) of length 312
    return [
        l168_0(x),
        l168_1(x),
        l168_2(x),
        l168_3(x),
        l168_4(x),
        l168_5(x),
        l168_6(x),
        l168_7(x),
        l168_8(x),
        l168_9(x),
        l168_10(x),
        l168_11(x),
        l168_12(x),
        l168_13(x),
        l168_14(x),
        l168_15(x),
        l168_16(x),
        l168_17(x),
        l168_18(x),
        l168_19(x),
        l168_20(x),
        l168_21(x),
        l168_22(x),
        l168_23(x),
        l168_24(x),
        l168_25(x),
        l168_26(x),
        l168_27(x),
        l168_28(x),
        l168_29(x),
        l168_30(x),
        l168_31(x),
        l168_32(x),
        l168_33(x),
        l168_34(x),
        l168_35(x),
        l168_36(x),
        l168_37(x),
        l168_38(x),
        l168_39(x),
        l168_40(x),
        l168_41(x),
        l168_42(x),
        l168_43(x),
        l168_44(x),
        l168_45(x),
        l168_46(x),
        l168_47(x),
        l168_48(x),
        l168_49(x),
        l168_50(x),
        l168_51(x),
        l168_52(x),
        l168_53(x),
        l168_54(x),
        l168_55(x),
        l168_56(x),
        l168_57(x),
        l168_58(x),
        l168_59(x),
        l168_60(x),
        l168_61(x),
        l168_62(x),
        l168_63(x),
        l168_64(x),
        l168_65(x),
        l168_66(x),
        l168_67(x),
        l168_68(x),
        l168_69(x),
        l168_70(x),
        l168_71(x),
        l168_72(x),
        l168_73(x),
        l168_74(x),
        l168_75(x),
        l168_76(x),
        l168_77(x),
        l168_78(x),
        l168_79(x),
        l168_80(x),
        l168_81(x),
        l168_82(x),
        l168_83(x),
        l168_84(x),
        l168_85(x),
        l168_86(x),
        l168_87(x),
        l168_88(x),
        l168_89(x),
        l168_90(x),
        l168_91(x),
        l168_92(x),
        l168_93(x),
        l168_94(x),
        l168_95(x),
        l168_96(x),
        l168_97(x),
        l168_98(x),
        l168_99(x),
        l168_100(x),
        l168_101(x),
        l168_102(x),
        l168_103(x),
        l168_104(x),
        l168_105(x),
        l168_106(x),
        l168_107(x),
        l168_108(x),
        l168_109(x),
        l168_110(x),
        l168_111(x),
        l168_112(x),
        l168_113(x),
        l168_114(x),
        l168_115(x),
        l168_116(x),
        l168_117(x),
        l168_118(x),
        l168_119(x),
        l168_120(x),
        l168_121(x),
        l168_122(x),
        l168_123(x),
        l168_124(x),
        l168_125(x),
        l168_126(x),
        l168_127(x),
        l168_128(x),
        l168_129(x),
        l168_130(x),
        l168_131(x),
        l168_132(x),
        l168_133(x),
        l168_134(x),
        l168_135(x),
        l168_136(x),
        l168_137(x),
        l168_138(x),
        l168_139(x),
        l168_140(x),
        l168_141(x),
        l168_142(x),
        l168_143(x),
        l168_144(x),
        l168_145(x),
        l168_146(x),
        l168_147(x),
        l168_148(x),
        l168_149(x),
        l168_150(x),
        l168_151(x),
        l168_152(x),
        l168_153(x),
        l168_154(x),
        l168_155(x),
        l168_156(x),
        l168_157(x),
        l168_158(x),
        l168_159(x),
        l168_160(x),
        l168_161(x),
        l168_162(x),
        l168_163(x),
        l168_164(x),
        l168_165(x),
        l168_166(x),
        l168_167(x),
        l168_168(x),
        l168_169(x),
        l168_170(x),
        l168_171(x),
        l168_172(x),
        l168_173(x),
        l168_174(x),
        l168_175(x),
        l168_176(x),
        l168_177(x),
        l168_178(x),
        l168_179(x),
        l168_180(x),
        l168_181(x),
        l168_182(x),
        l168_183(x),
        l168_184(x),
        l168_185(x),
        l168_186(x),
        l168_187(x),
        l168_188(x),
        l168_189(x),
        l168_190(x),
        l168_191(x),
        l168_192(x),
        l168_193(x),
        l168_194(x),
        l168_195(x),
        l168_196(x),
        l168_197(x),
        l168_198(x),
        l168_199(x),
        l168_200(x),
        l168_201(x),
        l168_202(x),
        l168_203(x),
        l168_204(x),
        l168_205(x),
        l168_206(x),
        l168_207(x),
        l168_208(x),
        l168_209(x),
        l168_210(x),
        l168_211(x),
        l168_212(x),
        l168_213(x),
        l168_214(x),
        l168_215(x),
        l168_216(x),
        l168_217(x),
        l168_218(x),
        l168_219(x),
        l168_220(x),
        l168_221(x),
        l168_222(x),
        l168_223(x),
        l168_224(x),
        l168_225(x),
        l168_226(x),
        l168_227(x),
        l168_228(x),
        l168_229(x),
        l168_230(x),
        l168_231(x),
        l168_232(x),
        l168_233(x),
        l168_234(x),
        l168_235(x),
        l168_236(x),
        l168_237(x),
        l168_238(x),
        l168_239(x),
        l168_240(x),
        l168_241(x),
        l168_242(x),
        l168_243(x),
        l168_244(x),
        l168_245(x),
        l168_246(x),
        l168_247(x),
        l168_248(x),
        l168_249(x),
        l168_250(x),
        l168_251(x),
        l168_252(x),
        l168_253(x),
        l168_254(x),
        l168_255(x),
        l168_256(x),
        l168_257(x),
        l168_258(x),
        l168_259(x),
        l168_260(x),
        l168_261(x),
        l168_262(x),
        l168_263(x),
        l168_264(x),
        l168_265(x),
        l168_266(x),
        l168_267(x),
        l168_268(x),
        l168_269(x),
        l168_270(x),
        l168_271(x),
        l168_272(x),
        l168_273(x),
        l168_274(x),
        l168_275(x),
        l168_276(x),
        l168_277(x),
        l168_278(x),
        l168_279(x),
        l168_280(x),
        l168_281(x),
        l168_282(x),
        l168_283(x),
        l168_284(x),
        l168_285(x),
        l168_286(x),
        l168_287(x),
    ]