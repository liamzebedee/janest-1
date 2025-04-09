import numpy as np




# Generated from reverse engineering
def l278_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 288
    out = np.empty(288, dtype=np.float32)
    
    # for i in range(0, 40):
    for i in range(0, 40):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffffff (len=24)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(40, 64):
    for i in range(0, 24):
        s = -1 * x[40 + i] + -1 * x[64 + i]
        s += biases[i]
        out[40 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 72):
    for i in range(0, 8):
        s = x[112 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(72, 96):
    for i in range(0, 24):
        s = x[88 + i]
        out[72 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 288):
    for i in range(0, 192):
        s = x[120 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l278_0(x):
    # x is a list (or vector) of length 312
    return max(0, x[0])
def l278_1(x):
    # x is a list (or vector) of length 312
    return max(0, x[1])
def l278_2(x):
    # x is a list (or vector) of length 312
    return max(0, x[2])
def l278_3(x):
    # x is a list (or vector) of length 312
    return max(0, x[3])
def l278_4(x):
    # x is a list (or vector) of length 312
    return max(0, x[4])
def l278_5(x):
    # x is a list (or vector) of length 312
    return max(0, x[5])
def l278_6(x):
    # x is a list (or vector) of length 312
    return max(0, x[6])
def l278_7(x):
    # x is a list (or vector) of length 312
    return max(0, x[7])
def l278_8(x):
    # x is a list (or vector) of length 312
    return max(0, x[8])
def l278_9(x):
    # x is a list (or vector) of length 312
    return max(0, x[9])
def l278_10(x):
    # x is a list (or vector) of length 312
    return max(0, x[10])
def l278_11(x):
    # x is a list (or vector) of length 312
    return max(0, x[11])
def l278_12(x):
    # x is a list (or vector) of length 312
    return max(0, x[12])
def l278_13(x):
    # x is a list (or vector) of length 312
    return max(0, x[13])
def l278_14(x):
    # x is a list (or vector) of length 312
    return max(0, x[14])
def l278_15(x):
    # x is a list (or vector) of length 312
    return max(0, x[15])
def l278_16(x):
    # x is a list (or vector) of length 312
    return max(0, x[16])
def l278_17(x):
    # x is a list (or vector) of length 312
    return max(0, x[17])
def l278_18(x):
    # x is a list (or vector) of length 312
    return max(0, x[18])
def l278_19(x):
    # x is a list (or vector) of length 312
    return max(0, x[19])
def l278_20(x):
    # x is a list (or vector) of length 312
    return max(0, x[20])
def l278_21(x):
    # x is a list (or vector) of length 312
    return max(0, x[21])
def l278_22(x):
    # x is a list (or vector) of length 312
    return max(0, x[22])
def l278_23(x):
    # x is a list (or vector) of length 312
    return max(0, x[23])
def l278_24(x):
    # x is a list (or vector) of length 312
    return max(0, x[24])
def l278_25(x):
    # x is a list (or vector) of length 312
    return max(0, x[25])
def l278_26(x):
    # x is a list (or vector) of length 312
    return max(0, x[26])
def l278_27(x):
    # x is a list (or vector) of length 312
    return max(0, x[27])
def l278_28(x):
    # x is a list (or vector) of length 312
    return max(0, x[28])
def l278_29(x):
    # x is a list (or vector) of length 312
    return max(0, x[29])
def l278_30(x):
    # x is a list (or vector) of length 312
    return max(0, x[30])
def l278_31(x):
    # x is a list (or vector) of length 312
    return max(0, x[31])
def l278_32(x):
    # x is a list (or vector) of length 312
    return max(0, x[32])
def l278_33(x):
    # x is a list (or vector) of length 312
    return max(0, x[33])
def l278_34(x):
    # x is a list (or vector) of length 312
    return max(0, x[34])
def l278_35(x):
    # x is a list (or vector) of length 312
    return max(0, x[35])
def l278_36(x):
    # x is a list (or vector) of length 312
    return max(0, x[36])
def l278_37(x):
    # x is a list (or vector) of length 312
    return max(0, x[37])
def l278_38(x):
    # x is a list (or vector) of length 312
    return max(0, x[38])
def l278_39(x):
    # x is a list (or vector) of length 312
    return max(0, x[39])
def l278_40(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[40] + -1.0*x[64] + 1.0)
def l278_41(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[41] + -1.0*x[65] + 1.0)
def l278_42(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[42] + -1.0*x[66] + 1.0)
def l278_43(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[43] + -1.0*x[67] + 1.0)
def l278_44(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[44] + -1.0*x[68] + 1.0)
def l278_45(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[45] + -1.0*x[69] + 1.0)
def l278_46(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[46] + -1.0*x[70] + 1.0)
def l278_47(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[47] + -1.0*x[71] + 1.0)
def l278_48(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[48] + -1.0*x[72] + 1.0)
def l278_49(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[49] + -1.0*x[73] + 1.0)
def l278_50(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[50] + -1.0*x[74] + 1.0)
def l278_51(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[51] + -1.0*x[75] + 1.0)
def l278_52(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[52] + -1.0*x[76] + 1.0)
def l278_53(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[53] + -1.0*x[77] + 1.0)
def l278_54(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[54] + -1.0*x[78] + 1.0)
def l278_55(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[55] + -1.0*x[79] + 1.0)
def l278_56(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[56] + -1.0*x[80] + 1.0)
def l278_57(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[57] + -1.0*x[81] + 1.0)
def l278_58(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[58] + -1.0*x[82] + 1.0)
def l278_59(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[59] + -1.0*x[83] + 1.0)
def l278_60(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[60] + -1.0*x[84] + 1.0)
def l278_61(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[61] + -1.0*x[85] + 1.0)
def l278_62(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[62] + -1.0*x[86] + 1.0)
def l278_63(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[63] + -1.0*x[87] + 1.0)
def l278_64(x):
    # x is a list (or vector) of length 312
    return max(0, x[112])
def l278_65(x):
    # x is a list (or vector) of length 312
    return max(0, x[113])
def l278_66(x):
    # x is a list (or vector) of length 312
    return max(0, x[114])
def l278_67(x):
    # x is a list (or vector) of length 312
    return max(0, x[115])
def l278_68(x):
    # x is a list (or vector) of length 312
    return max(0, x[116])
def l278_69(x):
    # x is a list (or vector) of length 312
    return max(0, x[117])
def l278_70(x):
    # x is a list (or vector) of length 312
    return max(0, x[118])
def l278_71(x):
    # x is a list (or vector) of length 312
    return max(0, x[119])
def l278_72(x):
    # x is a list (or vector) of length 312
    return max(0, x[88])
def l278_73(x):
    # x is a list (or vector) of length 312
    return max(0, x[89])
def l278_74(x):
    # x is a list (or vector) of length 312
    return max(0, x[90])
def l278_75(x):
    # x is a list (or vector) of length 312
    return max(0, x[91])
def l278_76(x):
    # x is a list (or vector) of length 312
    return max(0, x[92])
def l278_77(x):
    # x is a list (or vector) of length 312
    return max(0, x[93])
def l278_78(x):
    # x is a list (or vector) of length 312
    return max(0, x[94])
def l278_79(x):
    # x is a list (or vector) of length 312
    return max(0, x[95])
def l278_80(x):
    # x is a list (or vector) of length 312
    return max(0, x[96])
def l278_81(x):
    # x is a list (or vector) of length 312
    return max(0, x[97])
def l278_82(x):
    # x is a list (or vector) of length 312
    return max(0, x[98])
def l278_83(x):
    # x is a list (or vector) of length 312
    return max(0, x[99])
def l278_84(x):
    # x is a list (or vector) of length 312
    return max(0, x[100])
def l278_85(x):
    # x is a list (or vector) of length 312
    return max(0, x[101])
def l278_86(x):
    # x is a list (or vector) of length 312
    return max(0, x[102])
def l278_87(x):
    # x is a list (or vector) of length 312
    return max(0, x[103])
def l278_88(x):
    # x is a list (or vector) of length 312
    return max(0, x[104])
def l278_89(x):
    # x is a list (or vector) of length 312
    return max(0, x[105])
def l278_90(x):
    # x is a list (or vector) of length 312
    return max(0, x[106])
def l278_91(x):
    # x is a list (or vector) of length 312
    return max(0, x[107])
def l278_92(x):
    # x is a list (or vector) of length 312
    return max(0, x[108])
def l278_93(x):
    # x is a list (or vector) of length 312
    return max(0, x[109])
def l278_94(x):
    # x is a list (or vector) of length 312
    return max(0, x[110])
def l278_95(x):
    # x is a list (or vector) of length 312
    return max(0, x[111])
def l278_96(x):
    # x is a list (or vector) of length 312
    return max(0, x[120])
def l278_97(x):
    # x is a list (or vector) of length 312
    return max(0, x[121])
def l278_98(x):
    # x is a list (or vector) of length 312
    return max(0, x[122])
def l278_99(x):
    # x is a list (or vector) of length 312
    return max(0, x[123])
def l278_100(x):
    # x is a list (or vector) of length 312
    return max(0, x[124])
def l278_101(x):
    # x is a list (or vector) of length 312
    return max(0, x[125])
def l278_102(x):
    # x is a list (or vector) of length 312
    return max(0, x[126])
def l278_103(x):
    # x is a list (or vector) of length 312
    return max(0, x[127])
def l278_104(x):
    # x is a list (or vector) of length 312
    return max(0, x[128])
def l278_105(x):
    # x is a list (or vector) of length 312
    return max(0, x[129])
def l278_106(x):
    # x is a list (or vector) of length 312
    return max(0, x[130])
def l278_107(x):
    # x is a list (or vector) of length 312
    return max(0, x[131])
def l278_108(x):
    # x is a list (or vector) of length 312
    return max(0, x[132])
def l278_109(x):
    # x is a list (or vector) of length 312
    return max(0, x[133])
def l278_110(x):
    # x is a list (or vector) of length 312
    return max(0, x[134])
def l278_111(x):
    # x is a list (or vector) of length 312
    return max(0, x[135])
def l278_112(x):
    # x is a list (or vector) of length 312
    return max(0, x[136])
def l278_113(x):
    # x is a list (or vector) of length 312
    return max(0, x[137])
def l278_114(x):
    # x is a list (or vector) of length 312
    return max(0, x[138])
def l278_115(x):
    # x is a list (or vector) of length 312
    return max(0, x[139])
def l278_116(x):
    # x is a list (or vector) of length 312
    return max(0, x[140])
def l278_117(x):
    # x is a list (or vector) of length 312
    return max(0, x[141])
def l278_118(x):
    # x is a list (or vector) of length 312
    return max(0, x[142])
def l278_119(x):
    # x is a list (or vector) of length 312
    return max(0, x[143])
def l278_120(x):
    # x is a list (or vector) of length 312
    return max(0, x[144])
def l278_121(x):
    # x is a list (or vector) of length 312
    return max(0, x[145])
def l278_122(x):
    # x is a list (or vector) of length 312
    return max(0, x[146])
def l278_123(x):
    # x is a list (or vector) of length 312
    return max(0, x[147])
def l278_124(x):
    # x is a list (or vector) of length 312
    return max(0, x[148])
def l278_125(x):
    # x is a list (or vector) of length 312
    return max(0, x[149])
def l278_126(x):
    # x is a list (or vector) of length 312
    return max(0, x[150])
def l278_127(x):
    # x is a list (or vector) of length 312
    return max(0, x[151])
def l278_128(x):
    # x is a list (or vector) of length 312
    return max(0, x[152])
def l278_129(x):
    # x is a list (or vector) of length 312
    return max(0, x[153])
def l278_130(x):
    # x is a list (or vector) of length 312
    return max(0, x[154])
def l278_131(x):
    # x is a list (or vector) of length 312
    return max(0, x[155])
def l278_132(x):
    # x is a list (or vector) of length 312
    return max(0, x[156])
def l278_133(x):
    # x is a list (or vector) of length 312
    return max(0, x[157])
def l278_134(x):
    # x is a list (or vector) of length 312
    return max(0, x[158])
def l278_135(x):
    # x is a list (or vector) of length 312
    return max(0, x[159])
def l278_136(x):
    # x is a list (or vector) of length 312
    return max(0, x[160])
def l278_137(x):
    # x is a list (or vector) of length 312
    return max(0, x[161])
def l278_138(x):
    # x is a list (or vector) of length 312
    return max(0, x[162])
def l278_139(x):
    # x is a list (or vector) of length 312
    return max(0, x[163])
def l278_140(x):
    # x is a list (or vector) of length 312
    return max(0, x[164])
def l278_141(x):
    # x is a list (or vector) of length 312
    return max(0, x[165])
def l278_142(x):
    # x is a list (or vector) of length 312
    return max(0, x[166])
def l278_143(x):
    # x is a list (or vector) of length 312
    return max(0, x[167])
def l278_144(x):
    # x is a list (or vector) of length 312
    return max(0, x[168])
def l278_145(x):
    # x is a list (or vector) of length 312
    return max(0, x[169])
def l278_146(x):
    # x is a list (or vector) of length 312
    return max(0, x[170])
def l278_147(x):
    # x is a list (or vector) of length 312
    return max(0, x[171])
def l278_148(x):
    # x is a list (or vector) of length 312
    return max(0, x[172])
def l278_149(x):
    # x is a list (or vector) of length 312
    return max(0, x[173])
def l278_150(x):
    # x is a list (or vector) of length 312
    return max(0, x[174])
def l278_151(x):
    # x is a list (or vector) of length 312
    return max(0, x[175])
def l278_152(x):
    # x is a list (or vector) of length 312
    return max(0, x[176])
def l278_153(x):
    # x is a list (or vector) of length 312
    return max(0, x[177])
def l278_154(x):
    # x is a list (or vector) of length 312
    return max(0, x[178])
def l278_155(x):
    # x is a list (or vector) of length 312
    return max(0, x[179])
def l278_156(x):
    # x is a list (or vector) of length 312
    return max(0, x[180])
def l278_157(x):
    # x is a list (or vector) of length 312
    return max(0, x[181])
def l278_158(x):
    # x is a list (or vector) of length 312
    return max(0, x[182])
def l278_159(x):
    # x is a list (or vector) of length 312
    return max(0, x[183])
def l278_160(x):
    # x is a list (or vector) of length 312
    return max(0, x[184])
def l278_161(x):
    # x is a list (or vector) of length 312
    return max(0, x[185])
def l278_162(x):
    # x is a list (or vector) of length 312
    return max(0, x[186])
def l278_163(x):
    # x is a list (or vector) of length 312
    return max(0, x[187])
def l278_164(x):
    # x is a list (or vector) of length 312
    return max(0, x[188])
def l278_165(x):
    # x is a list (or vector) of length 312
    return max(0, x[189])
def l278_166(x):
    # x is a list (or vector) of length 312
    return max(0, x[190])
def l278_167(x):
    # x is a list (or vector) of length 312
    return max(0, x[191])
def l278_168(x):
    # x is a list (or vector) of length 312
    return max(0, x[192])
def l278_169(x):
    # x is a list (or vector) of length 312
    return max(0, x[193])
def l278_170(x):
    # x is a list (or vector) of length 312
    return max(0, x[194])
def l278_171(x):
    # x is a list (or vector) of length 312
    return max(0, x[195])
def l278_172(x):
    # x is a list (or vector) of length 312
    return max(0, x[196])
def l278_173(x):
    # x is a list (or vector) of length 312
    return max(0, x[197])
def l278_174(x):
    # x is a list (or vector) of length 312
    return max(0, x[198])
def l278_175(x):
    # x is a list (or vector) of length 312
    return max(0, x[199])
def l278_176(x):
    # x is a list (or vector) of length 312
    return max(0, x[200])
def l278_177(x):
    # x is a list (or vector) of length 312
    return max(0, x[201])
def l278_178(x):
    # x is a list (or vector) of length 312
    return max(0, x[202])
def l278_179(x):
    # x is a list (or vector) of length 312
    return max(0, x[203])
def l278_180(x):
    # x is a list (or vector) of length 312
    return max(0, x[204])
def l278_181(x):
    # x is a list (or vector) of length 312
    return max(0, x[205])
def l278_182(x):
    # x is a list (or vector) of length 312
    return max(0, x[206])
def l278_183(x):
    # x is a list (or vector) of length 312
    return max(0, x[207])
def l278_184(x):
    # x is a list (or vector) of length 312
    return max(0, x[208])
def l278_185(x):
    # x is a list (or vector) of length 312
    return max(0, x[209])
def l278_186(x):
    # x is a list (or vector) of length 312
    return max(0, x[210])
def l278_187(x):
    # x is a list (or vector) of length 312
    return max(0, x[211])
def l278_188(x):
    # x is a list (or vector) of length 312
    return max(0, x[212])
def l278_189(x):
    # x is a list (or vector) of length 312
    return max(0, x[213])
def l278_190(x):
    # x is a list (or vector) of length 312
    return max(0, x[214])
def l278_191(x):
    # x is a list (or vector) of length 312
    return max(0, x[215])
def l278_192(x):
    # x is a list (or vector) of length 312
    return max(0, x[216])
def l278_193(x):
    # x is a list (or vector) of length 312
    return max(0, x[217])
def l278_194(x):
    # x is a list (or vector) of length 312
    return max(0, x[218])
def l278_195(x):
    # x is a list (or vector) of length 312
    return max(0, x[219])
def l278_196(x):
    # x is a list (or vector) of length 312
    return max(0, x[220])
def l278_197(x):
    # x is a list (or vector) of length 312
    return max(0, x[221])
def l278_198(x):
    # x is a list (or vector) of length 312
    return max(0, x[222])
def l278_199(x):
    # x is a list (or vector) of length 312
    return max(0, x[223])
def l278_200(x):
    # x is a list (or vector) of length 312
    return max(0, x[224])
def l278_201(x):
    # x is a list (or vector) of length 312
    return max(0, x[225])
def l278_202(x):
    # x is a list (or vector) of length 312
    return max(0, x[226])
def l278_203(x):
    # x is a list (or vector) of length 312
    return max(0, x[227])
def l278_204(x):
    # x is a list (or vector) of length 312
    return max(0, x[228])
def l278_205(x):
    # x is a list (or vector) of length 312
    return max(0, x[229])
def l278_206(x):
    # x is a list (or vector) of length 312
    return max(0, x[230])
def l278_207(x):
    # x is a list (or vector) of length 312
    return max(0, x[231])
def l278_208(x):
    # x is a list (or vector) of length 312
    return max(0, x[232])
def l278_209(x):
    # x is a list (or vector) of length 312
    return max(0, x[233])
def l278_210(x):
    # x is a list (or vector) of length 312
    return max(0, x[234])
def l278_211(x):
    # x is a list (or vector) of length 312
    return max(0, x[235])
def l278_212(x):
    # x is a list (or vector) of length 312
    return max(0, x[236])
def l278_213(x):
    # x is a list (or vector) of length 312
    return max(0, x[237])
def l278_214(x):
    # x is a list (or vector) of length 312
    return max(0, x[238])
def l278_215(x):
    # x is a list (or vector) of length 312
    return max(0, x[239])
def l278_216(x):
    # x is a list (or vector) of length 312
    return max(0, x[240])
def l278_217(x):
    # x is a list (or vector) of length 312
    return max(0, x[241])
def l278_218(x):
    # x is a list (or vector) of length 312
    return max(0, x[242])
def l278_219(x):
    # x is a list (or vector) of length 312
    return max(0, x[243])
def l278_220(x):
    # x is a list (or vector) of length 312
    return max(0, x[244])
def l278_221(x):
    # x is a list (or vector) of length 312
    return max(0, x[245])
def l278_222(x):
    # x is a list (or vector) of length 312
    return max(0, x[246])
def l278_223(x):
    # x is a list (or vector) of length 312
    return max(0, x[247])
def l278_224(x):
    # x is a list (or vector) of length 312
    return max(0, x[248])
def l278_225(x):
    # x is a list (or vector) of length 312
    return max(0, x[249])
def l278_226(x):
    # x is a list (or vector) of length 312
    return max(0, x[250])
def l278_227(x):
    # x is a list (or vector) of length 312
    return max(0, x[251])
def l278_228(x):
    # x is a list (or vector) of length 312
    return max(0, x[252])
def l278_229(x):
    # x is a list (or vector) of length 312
    return max(0, x[253])
def l278_230(x):
    # x is a list (or vector) of length 312
    return max(0, x[254])
def l278_231(x):
    # x is a list (or vector) of length 312
    return max(0, x[255])
def l278_232(x):
    # x is a list (or vector) of length 312
    return max(0, x[256])
def l278_233(x):
    # x is a list (or vector) of length 312
    return max(0, x[257])
def l278_234(x):
    # x is a list (or vector) of length 312
    return max(0, x[258])
def l278_235(x):
    # x is a list (or vector) of length 312
    return max(0, x[259])
def l278_236(x):
    # x is a list (or vector) of length 312
    return max(0, x[260])
def l278_237(x):
    # x is a list (or vector) of length 312
    return max(0, x[261])
def l278_238(x):
    # x is a list (or vector) of length 312
    return max(0, x[262])
def l278_239(x):
    # x is a list (or vector) of length 312
    return max(0, x[263])
def l278_240(x):
    # x is a list (or vector) of length 312
    return max(0, x[264])
def l278_241(x):
    # x is a list (or vector) of length 312
    return max(0, x[265])
def l278_242(x):
    # x is a list (or vector) of length 312
    return max(0, x[266])
def l278_243(x):
    # x is a list (or vector) of length 312
    return max(0, x[267])
def l278_244(x):
    # x is a list (or vector) of length 312
    return max(0, x[268])
def l278_245(x):
    # x is a list (or vector) of length 312
    return max(0, x[269])
def l278_246(x):
    # x is a list (or vector) of length 312
    return max(0, x[270])
def l278_247(x):
    # x is a list (or vector) of length 312
    return max(0, x[271])
def l278_248(x):
    # x is a list (or vector) of length 312
    return max(0, x[272])
def l278_249(x):
    # x is a list (or vector) of length 312
    return max(0, x[273])
def l278_250(x):
    # x is a list (or vector) of length 312
    return max(0, x[274])
def l278_251(x):
    # x is a list (or vector) of length 312
    return max(0, x[275])
def l278_252(x):
    # x is a list (or vector) of length 312
    return max(0, x[276])
def l278_253(x):
    # x is a list (or vector) of length 312
    return max(0, x[277])
def l278_254(x):
    # x is a list (or vector) of length 312
    return max(0, x[278])
def l278_255(x):
    # x is a list (or vector) of length 312
    return max(0, x[279])
def l278_256(x):
    # x is a list (or vector) of length 312
    return max(0, x[280])
def l278_257(x):
    # x is a list (or vector) of length 312
    return max(0, x[281])
def l278_258(x):
    # x is a list (or vector) of length 312
    return max(0, x[282])
def l278_259(x):
    # x is a list (or vector) of length 312
    return max(0, x[283])
def l278_260(x):
    # x is a list (or vector) of length 312
    return max(0, x[284])
def l278_261(x):
    # x is a list (or vector) of length 312
    return max(0, x[285])
def l278_262(x):
    # x is a list (or vector) of length 312
    return max(0, x[286])
def l278_263(x):
    # x is a list (or vector) of length 312
    return max(0, x[287])
def l278_264(x):
    # x is a list (or vector) of length 312
    return max(0, x[288])
def l278_265(x):
    # x is a list (or vector) of length 312
    return max(0, x[289])
def l278_266(x):
    # x is a list (or vector) of length 312
    return max(0, x[290])
def l278_267(x):
    # x is a list (or vector) of length 312
    return max(0, x[291])
def l278_268(x):
    # x is a list (or vector) of length 312
    return max(0, x[292])
def l278_269(x):
    # x is a list (or vector) of length 312
    return max(0, x[293])
def l278_270(x):
    # x is a list (or vector) of length 312
    return max(0, x[294])
def l278_271(x):
    # x is a list (or vector) of length 312
    return max(0, x[295])
def l278_272(x):
    # x is a list (or vector) of length 312
    return max(0, x[296])
def l278_273(x):
    # x is a list (or vector) of length 312
    return max(0, x[297])
def l278_274(x):
    # x is a list (or vector) of length 312
    return max(0, x[298])
def l278_275(x):
    # x is a list (or vector) of length 312
    return max(0, x[299])
def l278_276(x):
    # x is a list (or vector) of length 312
    return max(0, x[300])
def l278_277(x):
    # x is a list (or vector) of length 312
    return max(0, x[301])
def l278_278(x):
    # x is a list (or vector) of length 312
    return max(0, x[302])
def l278_279(x):
    # x is a list (or vector) of length 312
    return max(0, x[303])
def l278_280(x):
    # x is a list (or vector) of length 312
    return max(0, x[304])
def l278_281(x):
    # x is a list (or vector) of length 312
    return max(0, x[305])
def l278_282(x):
    # x is a list (or vector) of length 312
    return max(0, x[306])
def l278_283(x):
    # x is a list (or vector) of length 312
    return max(0, x[307])
def l278_284(x):
    # x is a list (or vector) of length 312
    return max(0, x[308])
def l278_285(x):
    # x is a list (or vector) of length 312
    return max(0, x[309])
def l278_286(x):
    # x is a list (or vector) of length 312
    return max(0, x[310])
def l278_287(x):
    # x is a list (or vector) of length 312
    return max(0, x[311])
def l278_(x):
    # x is a list (or vector) of length 312
    return [
        l278_0(x),
        l278_1(x),
        l278_2(x),
        l278_3(x),
        l278_4(x),
        l278_5(x),
        l278_6(x),
        l278_7(x),
        l278_8(x),
        l278_9(x),
        l278_10(x),
        l278_11(x),
        l278_12(x),
        l278_13(x),
        l278_14(x),
        l278_15(x),
        l278_16(x),
        l278_17(x),
        l278_18(x),
        l278_19(x),
        l278_20(x),
        l278_21(x),
        l278_22(x),
        l278_23(x),
        l278_24(x),
        l278_25(x),
        l278_26(x),
        l278_27(x),
        l278_28(x),
        l278_29(x),
        l278_30(x),
        l278_31(x),
        l278_32(x),
        l278_33(x),
        l278_34(x),
        l278_35(x),
        l278_36(x),
        l278_37(x),
        l278_38(x),
        l278_39(x),
        l278_40(x),
        l278_41(x),
        l278_42(x),
        l278_43(x),
        l278_44(x),
        l278_45(x),
        l278_46(x),
        l278_47(x),
        l278_48(x),
        l278_49(x),
        l278_50(x),
        l278_51(x),
        l278_52(x),
        l278_53(x),
        l278_54(x),
        l278_55(x),
        l278_56(x),
        l278_57(x),
        l278_58(x),
        l278_59(x),
        l278_60(x),
        l278_61(x),
        l278_62(x),
        l278_63(x),
        l278_64(x),
        l278_65(x),
        l278_66(x),
        l278_67(x),
        l278_68(x),
        l278_69(x),
        l278_70(x),
        l278_71(x),
        l278_72(x),
        l278_73(x),
        l278_74(x),
        l278_75(x),
        l278_76(x),
        l278_77(x),
        l278_78(x),
        l278_79(x),
        l278_80(x),
        l278_81(x),
        l278_82(x),
        l278_83(x),
        l278_84(x),
        l278_85(x),
        l278_86(x),
        l278_87(x),
        l278_88(x),
        l278_89(x),
        l278_90(x),
        l278_91(x),
        l278_92(x),
        l278_93(x),
        l278_94(x),
        l278_95(x),
        l278_96(x),
        l278_97(x),
        l278_98(x),
        l278_99(x),
        l278_100(x),
        l278_101(x),
        l278_102(x),
        l278_103(x),
        l278_104(x),
        l278_105(x),
        l278_106(x),
        l278_107(x),
        l278_108(x),
        l278_109(x),
        l278_110(x),
        l278_111(x),
        l278_112(x),
        l278_113(x),
        l278_114(x),
        l278_115(x),
        l278_116(x),
        l278_117(x),
        l278_118(x),
        l278_119(x),
        l278_120(x),
        l278_121(x),
        l278_122(x),
        l278_123(x),
        l278_124(x),
        l278_125(x),
        l278_126(x),
        l278_127(x),
        l278_128(x),
        l278_129(x),
        l278_130(x),
        l278_131(x),
        l278_132(x),
        l278_133(x),
        l278_134(x),
        l278_135(x),
        l278_136(x),
        l278_137(x),
        l278_138(x),
        l278_139(x),
        l278_140(x),
        l278_141(x),
        l278_142(x),
        l278_143(x),
        l278_144(x),
        l278_145(x),
        l278_146(x),
        l278_147(x),
        l278_148(x),
        l278_149(x),
        l278_150(x),
        l278_151(x),
        l278_152(x),
        l278_153(x),
        l278_154(x),
        l278_155(x),
        l278_156(x),
        l278_157(x),
        l278_158(x),
        l278_159(x),
        l278_160(x),
        l278_161(x),
        l278_162(x),
        l278_163(x),
        l278_164(x),
        l278_165(x),
        l278_166(x),
        l278_167(x),
        l278_168(x),
        l278_169(x),
        l278_170(x),
        l278_171(x),
        l278_172(x),
        l278_173(x),
        l278_174(x),
        l278_175(x),
        l278_176(x),
        l278_177(x),
        l278_178(x),
        l278_179(x),
        l278_180(x),
        l278_181(x),
        l278_182(x),
        l278_183(x),
        l278_184(x),
        l278_185(x),
        l278_186(x),
        l278_187(x),
        l278_188(x),
        l278_189(x),
        l278_190(x),
        l278_191(x),
        l278_192(x),
        l278_193(x),
        l278_194(x),
        l278_195(x),
        l278_196(x),
        l278_197(x),
        l278_198(x),
        l278_199(x),
        l278_200(x),
        l278_201(x),
        l278_202(x),
        l278_203(x),
        l278_204(x),
        l278_205(x),
        l278_206(x),
        l278_207(x),
        l278_208(x),
        l278_209(x),
        l278_210(x),
        l278_211(x),
        l278_212(x),
        l278_213(x),
        l278_214(x),
        l278_215(x),
        l278_216(x),
        l278_217(x),
        l278_218(x),
        l278_219(x),
        l278_220(x),
        l278_221(x),
        l278_222(x),
        l278_223(x),
        l278_224(x),
        l278_225(x),
        l278_226(x),
        l278_227(x),
        l278_228(x),
        l278_229(x),
        l278_230(x),
        l278_231(x),
        l278_232(x),
        l278_233(x),
        l278_234(x),
        l278_235(x),
        l278_236(x),
        l278_237(x),
        l278_238(x),
        l278_239(x),
        l278_240(x),
        l278_241(x),
        l278_242(x),
        l278_243(x),
        l278_244(x),
        l278_245(x),
        l278_246(x),
        l278_247(x),
        l278_248(x),
        l278_249(x),
        l278_250(x),
        l278_251(x),
        l278_252(x),
        l278_253(x),
        l278_254(x),
        l278_255(x),
        l278_256(x),
        l278_257(x),
        l278_258(x),
        l278_259(x),
        l278_260(x),
        l278_261(x),
        l278_262(x),
        l278_263(x),
        l278_264(x),
        l278_265(x),
        l278_266(x),
        l278_267(x),
        l278_268(x),
        l278_269(x),
        l278_270(x),
        l278_271(x),
        l278_272(x),
        l278_273(x),
        l278_274(x),
        l278_275(x),
        l278_276(x),
        l278_277(x),
        l278_278(x),
        l278_279(x),
        l278_280(x),
        l278_281(x),
        l278_282(x),
        l278_283(x),
        l278_284(x),
        l278_285(x),
        l278_286(x),
        l278_287(x),
    ]