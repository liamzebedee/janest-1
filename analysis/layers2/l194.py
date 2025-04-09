import numpy as np




# Generated from reverse engineering
def l194_g(x: np.ndarray) -> np.ndarray:
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




def l194_0(x):
    # x is a list (or vector) of length 312
    return max(0, x[0])
def l194_1(x):
    # x is a list (or vector) of length 312
    return max(0, x[1])
def l194_2(x):
    # x is a list (or vector) of length 312
    return max(0, x[2])
def l194_3(x):
    # x is a list (or vector) of length 312
    return max(0, x[3])
def l194_4(x):
    # x is a list (or vector) of length 312
    return max(0, x[4])
def l194_5(x):
    # x is a list (or vector) of length 312
    return max(0, x[5])
def l194_6(x):
    # x is a list (or vector) of length 312
    return max(0, x[6])
def l194_7(x):
    # x is a list (or vector) of length 312
    return max(0, x[7])
def l194_8(x):
    # x is a list (or vector) of length 312
    return max(0, x[8])
def l194_9(x):
    # x is a list (or vector) of length 312
    return max(0, x[9])
def l194_10(x):
    # x is a list (or vector) of length 312
    return max(0, x[10])
def l194_11(x):
    # x is a list (or vector) of length 312
    return max(0, x[11])
def l194_12(x):
    # x is a list (or vector) of length 312
    return max(0, x[12])
def l194_13(x):
    # x is a list (or vector) of length 312
    return max(0, x[13])
def l194_14(x):
    # x is a list (or vector) of length 312
    return max(0, x[14])
def l194_15(x):
    # x is a list (or vector) of length 312
    return max(0, x[15])
def l194_16(x):
    # x is a list (or vector) of length 312
    return max(0, x[16])
def l194_17(x):
    # x is a list (or vector) of length 312
    return max(0, x[17])
def l194_18(x):
    # x is a list (or vector) of length 312
    return max(0, x[18])
def l194_19(x):
    # x is a list (or vector) of length 312
    return max(0, x[19])
def l194_20(x):
    # x is a list (or vector) of length 312
    return max(0, x[20])
def l194_21(x):
    # x is a list (or vector) of length 312
    return max(0, x[21])
def l194_22(x):
    # x is a list (or vector) of length 312
    return max(0, x[22])
def l194_23(x):
    # x is a list (or vector) of length 312
    return max(0, x[23])
def l194_24(x):
    # x is a list (or vector) of length 312
    return max(0, x[24])
def l194_25(x):
    # x is a list (or vector) of length 312
    return max(0, x[25])
def l194_26(x):
    # x is a list (or vector) of length 312
    return max(0, x[26])
def l194_27(x):
    # x is a list (or vector) of length 312
    return max(0, x[27])
def l194_28(x):
    # x is a list (or vector) of length 312
    return max(0, x[28])
def l194_29(x):
    # x is a list (or vector) of length 312
    return max(0, x[29])
def l194_30(x):
    # x is a list (or vector) of length 312
    return max(0, x[30])
def l194_31(x):
    # x is a list (or vector) of length 312
    return max(0, x[31])
def l194_32(x):
    # x is a list (or vector) of length 312
    return max(0, x[32])
def l194_33(x):
    # x is a list (or vector) of length 312
    return max(0, x[33])
def l194_34(x):
    # x is a list (or vector) of length 312
    return max(0, x[34])
def l194_35(x):
    # x is a list (or vector) of length 312
    return max(0, x[35])
def l194_36(x):
    # x is a list (or vector) of length 312
    return max(0, x[36])
def l194_37(x):
    # x is a list (or vector) of length 312
    return max(0, x[37])
def l194_38(x):
    # x is a list (or vector) of length 312
    return max(0, x[38])
def l194_39(x):
    # x is a list (or vector) of length 312
    return max(0, x[39])
def l194_40(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[40] + -1.0*x[64] + 1.0)
def l194_41(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[41] + -1.0*x[65] + 1.0)
def l194_42(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[42] + -1.0*x[66] + 1.0)
def l194_43(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[43] + -1.0*x[67] + 1.0)
def l194_44(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[44] + -1.0*x[68] + 1.0)
def l194_45(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[45] + -1.0*x[69] + 1.0)
def l194_46(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[46] + -1.0*x[70] + 1.0)
def l194_47(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[47] + -1.0*x[71] + 1.0)
def l194_48(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[48] + -1.0*x[72] + 1.0)
def l194_49(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[49] + -1.0*x[73] + 1.0)
def l194_50(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[50] + -1.0*x[74] + 1.0)
def l194_51(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[51] + -1.0*x[75] + 1.0)
def l194_52(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[52] + -1.0*x[76] + 1.0)
def l194_53(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[53] + -1.0*x[77] + 1.0)
def l194_54(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[54] + -1.0*x[78] + 1.0)
def l194_55(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[55] + -1.0*x[79] + 1.0)
def l194_56(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[56] + -1.0*x[80] + 1.0)
def l194_57(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[57] + -1.0*x[81] + 1.0)
def l194_58(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[58] + -1.0*x[82] + 1.0)
def l194_59(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[59] + -1.0*x[83] + 1.0)
def l194_60(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[60] + -1.0*x[84] + 1.0)
def l194_61(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[61] + -1.0*x[85] + 1.0)
def l194_62(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[62] + -1.0*x[86] + 1.0)
def l194_63(x):
    # x is a list (or vector) of length 312
    return max(0, -1.0*x[63] + -1.0*x[87] + 1.0)
def l194_64(x):
    # x is a list (or vector) of length 312
    return max(0, x[112])
def l194_65(x):
    # x is a list (or vector) of length 312
    return max(0, x[113])
def l194_66(x):
    # x is a list (or vector) of length 312
    return max(0, x[114])
def l194_67(x):
    # x is a list (or vector) of length 312
    return max(0, x[115])
def l194_68(x):
    # x is a list (or vector) of length 312
    return max(0, x[116])
def l194_69(x):
    # x is a list (or vector) of length 312
    return max(0, x[117])
def l194_70(x):
    # x is a list (or vector) of length 312
    return max(0, x[118])
def l194_71(x):
    # x is a list (or vector) of length 312
    return max(0, x[119])
def l194_72(x):
    # x is a list (or vector) of length 312
    return max(0, x[88])
def l194_73(x):
    # x is a list (or vector) of length 312
    return max(0, x[89])
def l194_74(x):
    # x is a list (or vector) of length 312
    return max(0, x[90])
def l194_75(x):
    # x is a list (or vector) of length 312
    return max(0, x[91])
def l194_76(x):
    # x is a list (or vector) of length 312
    return max(0, x[92])
def l194_77(x):
    # x is a list (or vector) of length 312
    return max(0, x[93])
def l194_78(x):
    # x is a list (or vector) of length 312
    return max(0, x[94])
def l194_79(x):
    # x is a list (or vector) of length 312
    return max(0, x[95])
def l194_80(x):
    # x is a list (or vector) of length 312
    return max(0, x[96])
def l194_81(x):
    # x is a list (or vector) of length 312
    return max(0, x[97])
def l194_82(x):
    # x is a list (or vector) of length 312
    return max(0, x[98])
def l194_83(x):
    # x is a list (or vector) of length 312
    return max(0, x[99])
def l194_84(x):
    # x is a list (or vector) of length 312
    return max(0, x[100])
def l194_85(x):
    # x is a list (or vector) of length 312
    return max(0, x[101])
def l194_86(x):
    # x is a list (or vector) of length 312
    return max(0, x[102])
def l194_87(x):
    # x is a list (or vector) of length 312
    return max(0, x[103])
def l194_88(x):
    # x is a list (or vector) of length 312
    return max(0, x[104])
def l194_89(x):
    # x is a list (or vector) of length 312
    return max(0, x[105])
def l194_90(x):
    # x is a list (or vector) of length 312
    return max(0, x[106])
def l194_91(x):
    # x is a list (or vector) of length 312
    return max(0, x[107])
def l194_92(x):
    # x is a list (or vector) of length 312
    return max(0, x[108])
def l194_93(x):
    # x is a list (or vector) of length 312
    return max(0, x[109])
def l194_94(x):
    # x is a list (or vector) of length 312
    return max(0, x[110])
def l194_95(x):
    # x is a list (or vector) of length 312
    return max(0, x[111])
def l194_96(x):
    # x is a list (or vector) of length 312
    return max(0, x[120])
def l194_97(x):
    # x is a list (or vector) of length 312
    return max(0, x[121])
def l194_98(x):
    # x is a list (or vector) of length 312
    return max(0, x[122])
def l194_99(x):
    # x is a list (or vector) of length 312
    return max(0, x[123])
def l194_100(x):
    # x is a list (or vector) of length 312
    return max(0, x[124])
def l194_101(x):
    # x is a list (or vector) of length 312
    return max(0, x[125])
def l194_102(x):
    # x is a list (or vector) of length 312
    return max(0, x[126])
def l194_103(x):
    # x is a list (or vector) of length 312
    return max(0, x[127])
def l194_104(x):
    # x is a list (or vector) of length 312
    return max(0, x[128])
def l194_105(x):
    # x is a list (or vector) of length 312
    return max(0, x[129])
def l194_106(x):
    # x is a list (or vector) of length 312
    return max(0, x[130])
def l194_107(x):
    # x is a list (or vector) of length 312
    return max(0, x[131])
def l194_108(x):
    # x is a list (or vector) of length 312
    return max(0, x[132])
def l194_109(x):
    # x is a list (or vector) of length 312
    return max(0, x[133])
def l194_110(x):
    # x is a list (or vector) of length 312
    return max(0, x[134])
def l194_111(x):
    # x is a list (or vector) of length 312
    return max(0, x[135])
def l194_112(x):
    # x is a list (or vector) of length 312
    return max(0, x[136])
def l194_113(x):
    # x is a list (or vector) of length 312
    return max(0, x[137])
def l194_114(x):
    # x is a list (or vector) of length 312
    return max(0, x[138])
def l194_115(x):
    # x is a list (or vector) of length 312
    return max(0, x[139])
def l194_116(x):
    # x is a list (or vector) of length 312
    return max(0, x[140])
def l194_117(x):
    # x is a list (or vector) of length 312
    return max(0, x[141])
def l194_118(x):
    # x is a list (or vector) of length 312
    return max(0, x[142])
def l194_119(x):
    # x is a list (or vector) of length 312
    return max(0, x[143])
def l194_120(x):
    # x is a list (or vector) of length 312
    return max(0, x[144])
def l194_121(x):
    # x is a list (or vector) of length 312
    return max(0, x[145])
def l194_122(x):
    # x is a list (or vector) of length 312
    return max(0, x[146])
def l194_123(x):
    # x is a list (or vector) of length 312
    return max(0, x[147])
def l194_124(x):
    # x is a list (or vector) of length 312
    return max(0, x[148])
def l194_125(x):
    # x is a list (or vector) of length 312
    return max(0, x[149])
def l194_126(x):
    # x is a list (or vector) of length 312
    return max(0, x[150])
def l194_127(x):
    # x is a list (or vector) of length 312
    return max(0, x[151])
def l194_128(x):
    # x is a list (or vector) of length 312
    return max(0, x[152])
def l194_129(x):
    # x is a list (or vector) of length 312
    return max(0, x[153])
def l194_130(x):
    # x is a list (or vector) of length 312
    return max(0, x[154])
def l194_131(x):
    # x is a list (or vector) of length 312
    return max(0, x[155])
def l194_132(x):
    # x is a list (or vector) of length 312
    return max(0, x[156])
def l194_133(x):
    # x is a list (or vector) of length 312
    return max(0, x[157])
def l194_134(x):
    # x is a list (or vector) of length 312
    return max(0, x[158])
def l194_135(x):
    # x is a list (or vector) of length 312
    return max(0, x[159])
def l194_136(x):
    # x is a list (or vector) of length 312
    return max(0, x[160])
def l194_137(x):
    # x is a list (or vector) of length 312
    return max(0, x[161])
def l194_138(x):
    # x is a list (or vector) of length 312
    return max(0, x[162])
def l194_139(x):
    # x is a list (or vector) of length 312
    return max(0, x[163])
def l194_140(x):
    # x is a list (or vector) of length 312
    return max(0, x[164])
def l194_141(x):
    # x is a list (or vector) of length 312
    return max(0, x[165])
def l194_142(x):
    # x is a list (or vector) of length 312
    return max(0, x[166])
def l194_143(x):
    # x is a list (or vector) of length 312
    return max(0, x[167])
def l194_144(x):
    # x is a list (or vector) of length 312
    return max(0, x[168])
def l194_145(x):
    # x is a list (or vector) of length 312
    return max(0, x[169])
def l194_146(x):
    # x is a list (or vector) of length 312
    return max(0, x[170])
def l194_147(x):
    # x is a list (or vector) of length 312
    return max(0, x[171])
def l194_148(x):
    # x is a list (or vector) of length 312
    return max(0, x[172])
def l194_149(x):
    # x is a list (or vector) of length 312
    return max(0, x[173])
def l194_150(x):
    # x is a list (or vector) of length 312
    return max(0, x[174])
def l194_151(x):
    # x is a list (or vector) of length 312
    return max(0, x[175])
def l194_152(x):
    # x is a list (or vector) of length 312
    return max(0, x[176])
def l194_153(x):
    # x is a list (or vector) of length 312
    return max(0, x[177])
def l194_154(x):
    # x is a list (or vector) of length 312
    return max(0, x[178])
def l194_155(x):
    # x is a list (or vector) of length 312
    return max(0, x[179])
def l194_156(x):
    # x is a list (or vector) of length 312
    return max(0, x[180])
def l194_157(x):
    # x is a list (or vector) of length 312
    return max(0, x[181])
def l194_158(x):
    # x is a list (or vector) of length 312
    return max(0, x[182])
def l194_159(x):
    # x is a list (or vector) of length 312
    return max(0, x[183])
def l194_160(x):
    # x is a list (or vector) of length 312
    return max(0, x[184])
def l194_161(x):
    # x is a list (or vector) of length 312
    return max(0, x[185])
def l194_162(x):
    # x is a list (or vector) of length 312
    return max(0, x[186])
def l194_163(x):
    # x is a list (or vector) of length 312
    return max(0, x[187])
def l194_164(x):
    # x is a list (or vector) of length 312
    return max(0, x[188])
def l194_165(x):
    # x is a list (or vector) of length 312
    return max(0, x[189])
def l194_166(x):
    # x is a list (or vector) of length 312
    return max(0, x[190])
def l194_167(x):
    # x is a list (or vector) of length 312
    return max(0, x[191])
def l194_168(x):
    # x is a list (or vector) of length 312
    return max(0, x[192])
def l194_169(x):
    # x is a list (or vector) of length 312
    return max(0, x[193])
def l194_170(x):
    # x is a list (or vector) of length 312
    return max(0, x[194])
def l194_171(x):
    # x is a list (or vector) of length 312
    return max(0, x[195])
def l194_172(x):
    # x is a list (or vector) of length 312
    return max(0, x[196])
def l194_173(x):
    # x is a list (or vector) of length 312
    return max(0, x[197])
def l194_174(x):
    # x is a list (or vector) of length 312
    return max(0, x[198])
def l194_175(x):
    # x is a list (or vector) of length 312
    return max(0, x[199])
def l194_176(x):
    # x is a list (or vector) of length 312
    return max(0, x[200])
def l194_177(x):
    # x is a list (or vector) of length 312
    return max(0, x[201])
def l194_178(x):
    # x is a list (or vector) of length 312
    return max(0, x[202])
def l194_179(x):
    # x is a list (or vector) of length 312
    return max(0, x[203])
def l194_180(x):
    # x is a list (or vector) of length 312
    return max(0, x[204])
def l194_181(x):
    # x is a list (or vector) of length 312
    return max(0, x[205])
def l194_182(x):
    # x is a list (or vector) of length 312
    return max(0, x[206])
def l194_183(x):
    # x is a list (or vector) of length 312
    return max(0, x[207])
def l194_184(x):
    # x is a list (or vector) of length 312
    return max(0, x[208])
def l194_185(x):
    # x is a list (or vector) of length 312
    return max(0, x[209])
def l194_186(x):
    # x is a list (or vector) of length 312
    return max(0, x[210])
def l194_187(x):
    # x is a list (or vector) of length 312
    return max(0, x[211])
def l194_188(x):
    # x is a list (or vector) of length 312
    return max(0, x[212])
def l194_189(x):
    # x is a list (or vector) of length 312
    return max(0, x[213])
def l194_190(x):
    # x is a list (or vector) of length 312
    return max(0, x[214])
def l194_191(x):
    # x is a list (or vector) of length 312
    return max(0, x[215])
def l194_192(x):
    # x is a list (or vector) of length 312
    return max(0, x[216])
def l194_193(x):
    # x is a list (or vector) of length 312
    return max(0, x[217])
def l194_194(x):
    # x is a list (or vector) of length 312
    return max(0, x[218])
def l194_195(x):
    # x is a list (or vector) of length 312
    return max(0, x[219])
def l194_196(x):
    # x is a list (or vector) of length 312
    return max(0, x[220])
def l194_197(x):
    # x is a list (or vector) of length 312
    return max(0, x[221])
def l194_198(x):
    # x is a list (or vector) of length 312
    return max(0, x[222])
def l194_199(x):
    # x is a list (or vector) of length 312
    return max(0, x[223])
def l194_200(x):
    # x is a list (or vector) of length 312
    return max(0, x[224])
def l194_201(x):
    # x is a list (or vector) of length 312
    return max(0, x[225])
def l194_202(x):
    # x is a list (or vector) of length 312
    return max(0, x[226])
def l194_203(x):
    # x is a list (or vector) of length 312
    return max(0, x[227])
def l194_204(x):
    # x is a list (or vector) of length 312
    return max(0, x[228])
def l194_205(x):
    # x is a list (or vector) of length 312
    return max(0, x[229])
def l194_206(x):
    # x is a list (or vector) of length 312
    return max(0, x[230])
def l194_207(x):
    # x is a list (or vector) of length 312
    return max(0, x[231])
def l194_208(x):
    # x is a list (or vector) of length 312
    return max(0, x[232])
def l194_209(x):
    # x is a list (or vector) of length 312
    return max(0, x[233])
def l194_210(x):
    # x is a list (or vector) of length 312
    return max(0, x[234])
def l194_211(x):
    # x is a list (or vector) of length 312
    return max(0, x[235])
def l194_212(x):
    # x is a list (or vector) of length 312
    return max(0, x[236])
def l194_213(x):
    # x is a list (or vector) of length 312
    return max(0, x[237])
def l194_214(x):
    # x is a list (or vector) of length 312
    return max(0, x[238])
def l194_215(x):
    # x is a list (or vector) of length 312
    return max(0, x[239])
def l194_216(x):
    # x is a list (or vector) of length 312
    return max(0, x[240])
def l194_217(x):
    # x is a list (or vector) of length 312
    return max(0, x[241])
def l194_218(x):
    # x is a list (or vector) of length 312
    return max(0, x[242])
def l194_219(x):
    # x is a list (or vector) of length 312
    return max(0, x[243])
def l194_220(x):
    # x is a list (or vector) of length 312
    return max(0, x[244])
def l194_221(x):
    # x is a list (or vector) of length 312
    return max(0, x[245])
def l194_222(x):
    # x is a list (or vector) of length 312
    return max(0, x[246])
def l194_223(x):
    # x is a list (or vector) of length 312
    return max(0, x[247])
def l194_224(x):
    # x is a list (or vector) of length 312
    return max(0, x[248])
def l194_225(x):
    # x is a list (or vector) of length 312
    return max(0, x[249])
def l194_226(x):
    # x is a list (or vector) of length 312
    return max(0, x[250])
def l194_227(x):
    # x is a list (or vector) of length 312
    return max(0, x[251])
def l194_228(x):
    # x is a list (or vector) of length 312
    return max(0, x[252])
def l194_229(x):
    # x is a list (or vector) of length 312
    return max(0, x[253])
def l194_230(x):
    # x is a list (or vector) of length 312
    return max(0, x[254])
def l194_231(x):
    # x is a list (or vector) of length 312
    return max(0, x[255])
def l194_232(x):
    # x is a list (or vector) of length 312
    return max(0, x[256])
def l194_233(x):
    # x is a list (or vector) of length 312
    return max(0, x[257])
def l194_234(x):
    # x is a list (or vector) of length 312
    return max(0, x[258])
def l194_235(x):
    # x is a list (or vector) of length 312
    return max(0, x[259])
def l194_236(x):
    # x is a list (or vector) of length 312
    return max(0, x[260])
def l194_237(x):
    # x is a list (or vector) of length 312
    return max(0, x[261])
def l194_238(x):
    # x is a list (or vector) of length 312
    return max(0, x[262])
def l194_239(x):
    # x is a list (or vector) of length 312
    return max(0, x[263])
def l194_240(x):
    # x is a list (or vector) of length 312
    return max(0, x[264])
def l194_241(x):
    # x is a list (or vector) of length 312
    return max(0, x[265])
def l194_242(x):
    # x is a list (or vector) of length 312
    return max(0, x[266])
def l194_243(x):
    # x is a list (or vector) of length 312
    return max(0, x[267])
def l194_244(x):
    # x is a list (or vector) of length 312
    return max(0, x[268])
def l194_245(x):
    # x is a list (or vector) of length 312
    return max(0, x[269])
def l194_246(x):
    # x is a list (or vector) of length 312
    return max(0, x[270])
def l194_247(x):
    # x is a list (or vector) of length 312
    return max(0, x[271])
def l194_248(x):
    # x is a list (or vector) of length 312
    return max(0, x[272])
def l194_249(x):
    # x is a list (or vector) of length 312
    return max(0, x[273])
def l194_250(x):
    # x is a list (or vector) of length 312
    return max(0, x[274])
def l194_251(x):
    # x is a list (or vector) of length 312
    return max(0, x[275])
def l194_252(x):
    # x is a list (or vector) of length 312
    return max(0, x[276])
def l194_253(x):
    # x is a list (or vector) of length 312
    return max(0, x[277])
def l194_254(x):
    # x is a list (or vector) of length 312
    return max(0, x[278])
def l194_255(x):
    # x is a list (or vector) of length 312
    return max(0, x[279])
def l194_256(x):
    # x is a list (or vector) of length 312
    return max(0, x[280])
def l194_257(x):
    # x is a list (or vector) of length 312
    return max(0, x[281])
def l194_258(x):
    # x is a list (or vector) of length 312
    return max(0, x[282])
def l194_259(x):
    # x is a list (or vector) of length 312
    return max(0, x[283])
def l194_260(x):
    # x is a list (or vector) of length 312
    return max(0, x[284])
def l194_261(x):
    # x is a list (or vector) of length 312
    return max(0, x[285])
def l194_262(x):
    # x is a list (or vector) of length 312
    return max(0, x[286])
def l194_263(x):
    # x is a list (or vector) of length 312
    return max(0, x[287])
def l194_264(x):
    # x is a list (or vector) of length 312
    return max(0, x[288])
def l194_265(x):
    # x is a list (or vector) of length 312
    return max(0, x[289])
def l194_266(x):
    # x is a list (or vector) of length 312
    return max(0, x[290])
def l194_267(x):
    # x is a list (or vector) of length 312
    return max(0, x[291])
def l194_268(x):
    # x is a list (or vector) of length 312
    return max(0, x[292])
def l194_269(x):
    # x is a list (or vector) of length 312
    return max(0, x[293])
def l194_270(x):
    # x is a list (or vector) of length 312
    return max(0, x[294])
def l194_271(x):
    # x is a list (or vector) of length 312
    return max(0, x[295])
def l194_272(x):
    # x is a list (or vector) of length 312
    return max(0, x[296])
def l194_273(x):
    # x is a list (or vector) of length 312
    return max(0, x[297])
def l194_274(x):
    # x is a list (or vector) of length 312
    return max(0, x[298])
def l194_275(x):
    # x is a list (or vector) of length 312
    return max(0, x[299])
def l194_276(x):
    # x is a list (or vector) of length 312
    return max(0, x[300])
def l194_277(x):
    # x is a list (or vector) of length 312
    return max(0, x[301])
def l194_278(x):
    # x is a list (or vector) of length 312
    return max(0, x[302])
def l194_279(x):
    # x is a list (or vector) of length 312
    return max(0, x[303])
def l194_280(x):
    # x is a list (or vector) of length 312
    return max(0, x[304])
def l194_281(x):
    # x is a list (or vector) of length 312
    return max(0, x[305])
def l194_282(x):
    # x is a list (or vector) of length 312
    return max(0, x[306])
def l194_283(x):
    # x is a list (or vector) of length 312
    return max(0, x[307])
def l194_284(x):
    # x is a list (or vector) of length 312
    return max(0, x[308])
def l194_285(x):
    # x is a list (or vector) of length 312
    return max(0, x[309])
def l194_286(x):
    # x is a list (or vector) of length 312
    return max(0, x[310])
def l194_287(x):
    # x is a list (or vector) of length 312
    return max(0, x[311])
def l194_(x):
    # x is a list (or vector) of length 312
    return [
        l194_0(x),
        l194_1(x),
        l194_2(x),
        l194_3(x),
        l194_4(x),
        l194_5(x),
        l194_6(x),
        l194_7(x),
        l194_8(x),
        l194_9(x),
        l194_10(x),
        l194_11(x),
        l194_12(x),
        l194_13(x),
        l194_14(x),
        l194_15(x),
        l194_16(x),
        l194_17(x),
        l194_18(x),
        l194_19(x),
        l194_20(x),
        l194_21(x),
        l194_22(x),
        l194_23(x),
        l194_24(x),
        l194_25(x),
        l194_26(x),
        l194_27(x),
        l194_28(x),
        l194_29(x),
        l194_30(x),
        l194_31(x),
        l194_32(x),
        l194_33(x),
        l194_34(x),
        l194_35(x),
        l194_36(x),
        l194_37(x),
        l194_38(x),
        l194_39(x),
        l194_40(x),
        l194_41(x),
        l194_42(x),
        l194_43(x),
        l194_44(x),
        l194_45(x),
        l194_46(x),
        l194_47(x),
        l194_48(x),
        l194_49(x),
        l194_50(x),
        l194_51(x),
        l194_52(x),
        l194_53(x),
        l194_54(x),
        l194_55(x),
        l194_56(x),
        l194_57(x),
        l194_58(x),
        l194_59(x),
        l194_60(x),
        l194_61(x),
        l194_62(x),
        l194_63(x),
        l194_64(x),
        l194_65(x),
        l194_66(x),
        l194_67(x),
        l194_68(x),
        l194_69(x),
        l194_70(x),
        l194_71(x),
        l194_72(x),
        l194_73(x),
        l194_74(x),
        l194_75(x),
        l194_76(x),
        l194_77(x),
        l194_78(x),
        l194_79(x),
        l194_80(x),
        l194_81(x),
        l194_82(x),
        l194_83(x),
        l194_84(x),
        l194_85(x),
        l194_86(x),
        l194_87(x),
        l194_88(x),
        l194_89(x),
        l194_90(x),
        l194_91(x),
        l194_92(x),
        l194_93(x),
        l194_94(x),
        l194_95(x),
        l194_96(x),
        l194_97(x),
        l194_98(x),
        l194_99(x),
        l194_100(x),
        l194_101(x),
        l194_102(x),
        l194_103(x),
        l194_104(x),
        l194_105(x),
        l194_106(x),
        l194_107(x),
        l194_108(x),
        l194_109(x),
        l194_110(x),
        l194_111(x),
        l194_112(x),
        l194_113(x),
        l194_114(x),
        l194_115(x),
        l194_116(x),
        l194_117(x),
        l194_118(x),
        l194_119(x),
        l194_120(x),
        l194_121(x),
        l194_122(x),
        l194_123(x),
        l194_124(x),
        l194_125(x),
        l194_126(x),
        l194_127(x),
        l194_128(x),
        l194_129(x),
        l194_130(x),
        l194_131(x),
        l194_132(x),
        l194_133(x),
        l194_134(x),
        l194_135(x),
        l194_136(x),
        l194_137(x),
        l194_138(x),
        l194_139(x),
        l194_140(x),
        l194_141(x),
        l194_142(x),
        l194_143(x),
        l194_144(x),
        l194_145(x),
        l194_146(x),
        l194_147(x),
        l194_148(x),
        l194_149(x),
        l194_150(x),
        l194_151(x),
        l194_152(x),
        l194_153(x),
        l194_154(x),
        l194_155(x),
        l194_156(x),
        l194_157(x),
        l194_158(x),
        l194_159(x),
        l194_160(x),
        l194_161(x),
        l194_162(x),
        l194_163(x),
        l194_164(x),
        l194_165(x),
        l194_166(x),
        l194_167(x),
        l194_168(x),
        l194_169(x),
        l194_170(x),
        l194_171(x),
        l194_172(x),
        l194_173(x),
        l194_174(x),
        l194_175(x),
        l194_176(x),
        l194_177(x),
        l194_178(x),
        l194_179(x),
        l194_180(x),
        l194_181(x),
        l194_182(x),
        l194_183(x),
        l194_184(x),
        l194_185(x),
        l194_186(x),
        l194_187(x),
        l194_188(x),
        l194_189(x),
        l194_190(x),
        l194_191(x),
        l194_192(x),
        l194_193(x),
        l194_194(x),
        l194_195(x),
        l194_196(x),
        l194_197(x),
        l194_198(x),
        l194_199(x),
        l194_200(x),
        l194_201(x),
        l194_202(x),
        l194_203(x),
        l194_204(x),
        l194_205(x),
        l194_206(x),
        l194_207(x),
        l194_208(x),
        l194_209(x),
        l194_210(x),
        l194_211(x),
        l194_212(x),
        l194_213(x),
        l194_214(x),
        l194_215(x),
        l194_216(x),
        l194_217(x),
        l194_218(x),
        l194_219(x),
        l194_220(x),
        l194_221(x),
        l194_222(x),
        l194_223(x),
        l194_224(x),
        l194_225(x),
        l194_226(x),
        l194_227(x),
        l194_228(x),
        l194_229(x),
        l194_230(x),
        l194_231(x),
        l194_232(x),
        l194_233(x),
        l194_234(x),
        l194_235(x),
        l194_236(x),
        l194_237(x),
        l194_238(x),
        l194_239(x),
        l194_240(x),
        l194_241(x),
        l194_242(x),
        l194_243(x),
        l194_244(x),
        l194_245(x),
        l194_246(x),
        l194_247(x),
        l194_248(x),
        l194_249(x),
        l194_250(x),
        l194_251(x),
        l194_252(x),
        l194_253(x),
        l194_254(x),
        l194_255(x),
        l194_256(x),
        l194_257(x),
        l194_258(x),
        l194_259(x),
        l194_260(x),
        l194_261(x),
        l194_262(x),
        l194_263(x),
        l194_264(x),
        l194_265(x),
        l194_266(x),
        l194_267(x),
        l194_268(x),
        l194_269(x),
        l194_270(x),
        l194_271(x),
        l194_272(x),
        l194_273(x),
        l194_274(x),
        l194_275(x),
        l194_276(x),
        l194_277(x),
        l194_278(x),
        l194_279(x),
        l194_280(x),
        l194_281(x),
        l194_282(x),
        l194_283(x),
        l194_284(x),
        l194_285(x),
        l194_286(x),
        l194_287(x),
    ]