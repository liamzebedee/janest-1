import numpy as np




# Generated from reverse engineering
def l450_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 288
    out = np.empty(288, dtype=np.float32)
    
    # for i in range(0, 48):
    for i in range(0, 48):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffff (len=16)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(48, 64):
    for i in range(0, 16):
        s = -1 * x[48 + i] + -1 * x[64 + i]
        s += biases[i]
        out[48 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 80):
    for i in range(0, 16):
        s = x[96 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(80, 96):
    for i in range(0, 16):
        s = x[80 + i]
        out[80 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 288):
    for i in range(0, 192):
        s = x[112 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l450_0(x):
    # x is a list (or vector) of length 304
    return max(0, x[0])
def l450_1(x):
    # x is a list (or vector) of length 304
    return max(0, x[1])
def l450_2(x):
    # x is a list (or vector) of length 304
    return max(0, x[2])
def l450_3(x):
    # x is a list (or vector) of length 304
    return max(0, x[3])
def l450_4(x):
    # x is a list (or vector) of length 304
    return max(0, x[4])
def l450_5(x):
    # x is a list (or vector) of length 304
    return max(0, x[5])
def l450_6(x):
    # x is a list (or vector) of length 304
    return max(0, x[6])
def l450_7(x):
    # x is a list (or vector) of length 304
    return max(0, x[7])
def l450_8(x):
    # x is a list (or vector) of length 304
    return max(0, x[8])
def l450_9(x):
    # x is a list (or vector) of length 304
    return max(0, x[9])
def l450_10(x):
    # x is a list (or vector) of length 304
    return max(0, x[10])
def l450_11(x):
    # x is a list (or vector) of length 304
    return max(0, x[11])
def l450_12(x):
    # x is a list (or vector) of length 304
    return max(0, x[12])
def l450_13(x):
    # x is a list (or vector) of length 304
    return max(0, x[13])
def l450_14(x):
    # x is a list (or vector) of length 304
    return max(0, x[14])
def l450_15(x):
    # x is a list (or vector) of length 304
    return max(0, x[15])
def l450_16(x):
    # x is a list (or vector) of length 304
    return max(0, x[16])
def l450_17(x):
    # x is a list (or vector) of length 304
    return max(0, x[17])
def l450_18(x):
    # x is a list (or vector) of length 304
    return max(0, x[18])
def l450_19(x):
    # x is a list (or vector) of length 304
    return max(0, x[19])
def l450_20(x):
    # x is a list (or vector) of length 304
    return max(0, x[20])
def l450_21(x):
    # x is a list (or vector) of length 304
    return max(0, x[21])
def l450_22(x):
    # x is a list (or vector) of length 304
    return max(0, x[22])
def l450_23(x):
    # x is a list (or vector) of length 304
    return max(0, x[23])
def l450_24(x):
    # x is a list (or vector) of length 304
    return max(0, x[24])
def l450_25(x):
    # x is a list (or vector) of length 304
    return max(0, x[25])
def l450_26(x):
    # x is a list (or vector) of length 304
    return max(0, x[26])
def l450_27(x):
    # x is a list (or vector) of length 304
    return max(0, x[27])
def l450_28(x):
    # x is a list (or vector) of length 304
    return max(0, x[28])
def l450_29(x):
    # x is a list (or vector) of length 304
    return max(0, x[29])
def l450_30(x):
    # x is a list (or vector) of length 304
    return max(0, x[30])
def l450_31(x):
    # x is a list (or vector) of length 304
    return max(0, x[31])
def l450_32(x):
    # x is a list (or vector) of length 304
    return max(0, x[32])
def l450_33(x):
    # x is a list (or vector) of length 304
    return max(0, x[33])
def l450_34(x):
    # x is a list (or vector) of length 304
    return max(0, x[34])
def l450_35(x):
    # x is a list (or vector) of length 304
    return max(0, x[35])
def l450_36(x):
    # x is a list (or vector) of length 304
    return max(0, x[36])
def l450_37(x):
    # x is a list (or vector) of length 304
    return max(0, x[37])
def l450_38(x):
    # x is a list (or vector) of length 304
    return max(0, x[38])
def l450_39(x):
    # x is a list (or vector) of length 304
    return max(0, x[39])
def l450_40(x):
    # x is a list (or vector) of length 304
    return max(0, x[40])
def l450_41(x):
    # x is a list (or vector) of length 304
    return max(0, x[41])
def l450_42(x):
    # x is a list (or vector) of length 304
    return max(0, x[42])
def l450_43(x):
    # x is a list (or vector) of length 304
    return max(0, x[43])
def l450_44(x):
    # x is a list (or vector) of length 304
    return max(0, x[44])
def l450_45(x):
    # x is a list (or vector) of length 304
    return max(0, x[45])
def l450_46(x):
    # x is a list (or vector) of length 304
    return max(0, x[46])
def l450_47(x):
    # x is a list (or vector) of length 304
    return max(0, x[47])
def l450_48(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[48] + -1.0*x[64] + 1.0)
def l450_49(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[49] + -1.0*x[65] + 1.0)
def l450_50(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[50] + -1.0*x[66] + 1.0)
def l450_51(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[51] + -1.0*x[67] + 1.0)
def l450_52(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[52] + -1.0*x[68] + 1.0)
def l450_53(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[53] + -1.0*x[69] + 1.0)
def l450_54(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[54] + -1.0*x[70] + 1.0)
def l450_55(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[55] + -1.0*x[71] + 1.0)
def l450_56(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[56] + -1.0*x[72] + 1.0)
def l450_57(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[57] + -1.0*x[73] + 1.0)
def l450_58(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[58] + -1.0*x[74] + 1.0)
def l450_59(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[59] + -1.0*x[75] + 1.0)
def l450_60(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[60] + -1.0*x[76] + 1.0)
def l450_61(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[61] + -1.0*x[77] + 1.0)
def l450_62(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[62] + -1.0*x[78] + 1.0)
def l450_63(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[63] + -1.0*x[79] + 1.0)
def l450_64(x):
    # x is a list (or vector) of length 304
    return max(0, x[96])
def l450_65(x):
    # x is a list (or vector) of length 304
    return max(0, x[97])
def l450_66(x):
    # x is a list (or vector) of length 304
    return max(0, x[98])
def l450_67(x):
    # x is a list (or vector) of length 304
    return max(0, x[99])
def l450_68(x):
    # x is a list (or vector) of length 304
    return max(0, x[100])
def l450_69(x):
    # x is a list (or vector) of length 304
    return max(0, x[101])
def l450_70(x):
    # x is a list (or vector) of length 304
    return max(0, x[102])
def l450_71(x):
    # x is a list (or vector) of length 304
    return max(0, x[103])
def l450_72(x):
    # x is a list (or vector) of length 304
    return max(0, x[104])
def l450_73(x):
    # x is a list (or vector) of length 304
    return max(0, x[105])
def l450_74(x):
    # x is a list (or vector) of length 304
    return max(0, x[106])
def l450_75(x):
    # x is a list (or vector) of length 304
    return max(0, x[107])
def l450_76(x):
    # x is a list (or vector) of length 304
    return max(0, x[108])
def l450_77(x):
    # x is a list (or vector) of length 304
    return max(0, x[109])
def l450_78(x):
    # x is a list (or vector) of length 304
    return max(0, x[110])
def l450_79(x):
    # x is a list (or vector) of length 304
    return max(0, x[111])
def l450_80(x):
    # x is a list (or vector) of length 304
    return max(0, x[80])
def l450_81(x):
    # x is a list (or vector) of length 304
    return max(0, x[81])
def l450_82(x):
    # x is a list (or vector) of length 304
    return max(0, x[82])
def l450_83(x):
    # x is a list (or vector) of length 304
    return max(0, x[83])
def l450_84(x):
    # x is a list (or vector) of length 304
    return max(0, x[84])
def l450_85(x):
    # x is a list (or vector) of length 304
    return max(0, x[85])
def l450_86(x):
    # x is a list (or vector) of length 304
    return max(0, x[86])
def l450_87(x):
    # x is a list (or vector) of length 304
    return max(0, x[87])
def l450_88(x):
    # x is a list (or vector) of length 304
    return max(0, x[88])
def l450_89(x):
    # x is a list (or vector) of length 304
    return max(0, x[89])
def l450_90(x):
    # x is a list (or vector) of length 304
    return max(0, x[90])
def l450_91(x):
    # x is a list (or vector) of length 304
    return max(0, x[91])
def l450_92(x):
    # x is a list (or vector) of length 304
    return max(0, x[92])
def l450_93(x):
    # x is a list (or vector) of length 304
    return max(0, x[93])
def l450_94(x):
    # x is a list (or vector) of length 304
    return max(0, x[94])
def l450_95(x):
    # x is a list (or vector) of length 304
    return max(0, x[95])
def l450_96(x):
    # x is a list (or vector) of length 304
    return max(0, x[112])
def l450_97(x):
    # x is a list (or vector) of length 304
    return max(0, x[113])
def l450_98(x):
    # x is a list (or vector) of length 304
    return max(0, x[114])
def l450_99(x):
    # x is a list (or vector) of length 304
    return max(0, x[115])
def l450_100(x):
    # x is a list (or vector) of length 304
    return max(0, x[116])
def l450_101(x):
    # x is a list (or vector) of length 304
    return max(0, x[117])
def l450_102(x):
    # x is a list (or vector) of length 304
    return max(0, x[118])
def l450_103(x):
    # x is a list (or vector) of length 304
    return max(0, x[119])
def l450_104(x):
    # x is a list (or vector) of length 304
    return max(0, x[120])
def l450_105(x):
    # x is a list (or vector) of length 304
    return max(0, x[121])
def l450_106(x):
    # x is a list (or vector) of length 304
    return max(0, x[122])
def l450_107(x):
    # x is a list (or vector) of length 304
    return max(0, x[123])
def l450_108(x):
    # x is a list (or vector) of length 304
    return max(0, x[124])
def l450_109(x):
    # x is a list (or vector) of length 304
    return max(0, x[125])
def l450_110(x):
    # x is a list (or vector) of length 304
    return max(0, x[126])
def l450_111(x):
    # x is a list (or vector) of length 304
    return max(0, x[127])
def l450_112(x):
    # x is a list (or vector) of length 304
    return max(0, x[128])
def l450_113(x):
    # x is a list (or vector) of length 304
    return max(0, x[129])
def l450_114(x):
    # x is a list (or vector) of length 304
    return max(0, x[130])
def l450_115(x):
    # x is a list (or vector) of length 304
    return max(0, x[131])
def l450_116(x):
    # x is a list (or vector) of length 304
    return max(0, x[132])
def l450_117(x):
    # x is a list (or vector) of length 304
    return max(0, x[133])
def l450_118(x):
    # x is a list (or vector) of length 304
    return max(0, x[134])
def l450_119(x):
    # x is a list (or vector) of length 304
    return max(0, x[135])
def l450_120(x):
    # x is a list (or vector) of length 304
    return max(0, x[136])
def l450_121(x):
    # x is a list (or vector) of length 304
    return max(0, x[137])
def l450_122(x):
    # x is a list (or vector) of length 304
    return max(0, x[138])
def l450_123(x):
    # x is a list (or vector) of length 304
    return max(0, x[139])
def l450_124(x):
    # x is a list (or vector) of length 304
    return max(0, x[140])
def l450_125(x):
    # x is a list (or vector) of length 304
    return max(0, x[141])
def l450_126(x):
    # x is a list (or vector) of length 304
    return max(0, x[142])
def l450_127(x):
    # x is a list (or vector) of length 304
    return max(0, x[143])
def l450_128(x):
    # x is a list (or vector) of length 304
    return max(0, x[144])
def l450_129(x):
    # x is a list (or vector) of length 304
    return max(0, x[145])
def l450_130(x):
    # x is a list (or vector) of length 304
    return max(0, x[146])
def l450_131(x):
    # x is a list (or vector) of length 304
    return max(0, x[147])
def l450_132(x):
    # x is a list (or vector) of length 304
    return max(0, x[148])
def l450_133(x):
    # x is a list (or vector) of length 304
    return max(0, x[149])
def l450_134(x):
    # x is a list (or vector) of length 304
    return max(0, x[150])
def l450_135(x):
    # x is a list (or vector) of length 304
    return max(0, x[151])
def l450_136(x):
    # x is a list (or vector) of length 304
    return max(0, x[152])
def l450_137(x):
    # x is a list (or vector) of length 304
    return max(0, x[153])
def l450_138(x):
    # x is a list (or vector) of length 304
    return max(0, x[154])
def l450_139(x):
    # x is a list (or vector) of length 304
    return max(0, x[155])
def l450_140(x):
    # x is a list (or vector) of length 304
    return max(0, x[156])
def l450_141(x):
    # x is a list (or vector) of length 304
    return max(0, x[157])
def l450_142(x):
    # x is a list (or vector) of length 304
    return max(0, x[158])
def l450_143(x):
    # x is a list (or vector) of length 304
    return max(0, x[159])
def l450_144(x):
    # x is a list (or vector) of length 304
    return max(0, x[160])
def l450_145(x):
    # x is a list (or vector) of length 304
    return max(0, x[161])
def l450_146(x):
    # x is a list (or vector) of length 304
    return max(0, x[162])
def l450_147(x):
    # x is a list (or vector) of length 304
    return max(0, x[163])
def l450_148(x):
    # x is a list (or vector) of length 304
    return max(0, x[164])
def l450_149(x):
    # x is a list (or vector) of length 304
    return max(0, x[165])
def l450_150(x):
    # x is a list (or vector) of length 304
    return max(0, x[166])
def l450_151(x):
    # x is a list (or vector) of length 304
    return max(0, x[167])
def l450_152(x):
    # x is a list (or vector) of length 304
    return max(0, x[168])
def l450_153(x):
    # x is a list (or vector) of length 304
    return max(0, x[169])
def l450_154(x):
    # x is a list (or vector) of length 304
    return max(0, x[170])
def l450_155(x):
    # x is a list (or vector) of length 304
    return max(0, x[171])
def l450_156(x):
    # x is a list (or vector) of length 304
    return max(0, x[172])
def l450_157(x):
    # x is a list (or vector) of length 304
    return max(0, x[173])
def l450_158(x):
    # x is a list (or vector) of length 304
    return max(0, x[174])
def l450_159(x):
    # x is a list (or vector) of length 304
    return max(0, x[175])
def l450_160(x):
    # x is a list (or vector) of length 304
    return max(0, x[176])
def l450_161(x):
    # x is a list (or vector) of length 304
    return max(0, x[177])
def l450_162(x):
    # x is a list (or vector) of length 304
    return max(0, x[178])
def l450_163(x):
    # x is a list (or vector) of length 304
    return max(0, x[179])
def l450_164(x):
    # x is a list (or vector) of length 304
    return max(0, x[180])
def l450_165(x):
    # x is a list (or vector) of length 304
    return max(0, x[181])
def l450_166(x):
    # x is a list (or vector) of length 304
    return max(0, x[182])
def l450_167(x):
    # x is a list (or vector) of length 304
    return max(0, x[183])
def l450_168(x):
    # x is a list (or vector) of length 304
    return max(0, x[184])
def l450_169(x):
    # x is a list (or vector) of length 304
    return max(0, x[185])
def l450_170(x):
    # x is a list (or vector) of length 304
    return max(0, x[186])
def l450_171(x):
    # x is a list (or vector) of length 304
    return max(0, x[187])
def l450_172(x):
    # x is a list (or vector) of length 304
    return max(0, x[188])
def l450_173(x):
    # x is a list (or vector) of length 304
    return max(0, x[189])
def l450_174(x):
    # x is a list (or vector) of length 304
    return max(0, x[190])
def l450_175(x):
    # x is a list (or vector) of length 304
    return max(0, x[191])
def l450_176(x):
    # x is a list (or vector) of length 304
    return max(0, x[192])
def l450_177(x):
    # x is a list (or vector) of length 304
    return max(0, x[193])
def l450_178(x):
    # x is a list (or vector) of length 304
    return max(0, x[194])
def l450_179(x):
    # x is a list (or vector) of length 304
    return max(0, x[195])
def l450_180(x):
    # x is a list (or vector) of length 304
    return max(0, x[196])
def l450_181(x):
    # x is a list (or vector) of length 304
    return max(0, x[197])
def l450_182(x):
    # x is a list (or vector) of length 304
    return max(0, x[198])
def l450_183(x):
    # x is a list (or vector) of length 304
    return max(0, x[199])
def l450_184(x):
    # x is a list (or vector) of length 304
    return max(0, x[200])
def l450_185(x):
    # x is a list (or vector) of length 304
    return max(0, x[201])
def l450_186(x):
    # x is a list (or vector) of length 304
    return max(0, x[202])
def l450_187(x):
    # x is a list (or vector) of length 304
    return max(0, x[203])
def l450_188(x):
    # x is a list (or vector) of length 304
    return max(0, x[204])
def l450_189(x):
    # x is a list (or vector) of length 304
    return max(0, x[205])
def l450_190(x):
    # x is a list (or vector) of length 304
    return max(0, x[206])
def l450_191(x):
    # x is a list (or vector) of length 304
    return max(0, x[207])
def l450_192(x):
    # x is a list (or vector) of length 304
    return max(0, x[208])
def l450_193(x):
    # x is a list (or vector) of length 304
    return max(0, x[209])
def l450_194(x):
    # x is a list (or vector) of length 304
    return max(0, x[210])
def l450_195(x):
    # x is a list (or vector) of length 304
    return max(0, x[211])
def l450_196(x):
    # x is a list (or vector) of length 304
    return max(0, x[212])
def l450_197(x):
    # x is a list (or vector) of length 304
    return max(0, x[213])
def l450_198(x):
    # x is a list (or vector) of length 304
    return max(0, x[214])
def l450_199(x):
    # x is a list (or vector) of length 304
    return max(0, x[215])
def l450_200(x):
    # x is a list (or vector) of length 304
    return max(0, x[216])
def l450_201(x):
    # x is a list (or vector) of length 304
    return max(0, x[217])
def l450_202(x):
    # x is a list (or vector) of length 304
    return max(0, x[218])
def l450_203(x):
    # x is a list (or vector) of length 304
    return max(0, x[219])
def l450_204(x):
    # x is a list (or vector) of length 304
    return max(0, x[220])
def l450_205(x):
    # x is a list (or vector) of length 304
    return max(0, x[221])
def l450_206(x):
    # x is a list (or vector) of length 304
    return max(0, x[222])
def l450_207(x):
    # x is a list (or vector) of length 304
    return max(0, x[223])
def l450_208(x):
    # x is a list (or vector) of length 304
    return max(0, x[224])
def l450_209(x):
    # x is a list (or vector) of length 304
    return max(0, x[225])
def l450_210(x):
    # x is a list (or vector) of length 304
    return max(0, x[226])
def l450_211(x):
    # x is a list (or vector) of length 304
    return max(0, x[227])
def l450_212(x):
    # x is a list (or vector) of length 304
    return max(0, x[228])
def l450_213(x):
    # x is a list (or vector) of length 304
    return max(0, x[229])
def l450_214(x):
    # x is a list (or vector) of length 304
    return max(0, x[230])
def l450_215(x):
    # x is a list (or vector) of length 304
    return max(0, x[231])
def l450_216(x):
    # x is a list (or vector) of length 304
    return max(0, x[232])
def l450_217(x):
    # x is a list (or vector) of length 304
    return max(0, x[233])
def l450_218(x):
    # x is a list (or vector) of length 304
    return max(0, x[234])
def l450_219(x):
    # x is a list (or vector) of length 304
    return max(0, x[235])
def l450_220(x):
    # x is a list (or vector) of length 304
    return max(0, x[236])
def l450_221(x):
    # x is a list (or vector) of length 304
    return max(0, x[237])
def l450_222(x):
    # x is a list (or vector) of length 304
    return max(0, x[238])
def l450_223(x):
    # x is a list (or vector) of length 304
    return max(0, x[239])
def l450_224(x):
    # x is a list (or vector) of length 304
    return max(0, x[240])
def l450_225(x):
    # x is a list (or vector) of length 304
    return max(0, x[241])
def l450_226(x):
    # x is a list (or vector) of length 304
    return max(0, x[242])
def l450_227(x):
    # x is a list (or vector) of length 304
    return max(0, x[243])
def l450_228(x):
    # x is a list (or vector) of length 304
    return max(0, x[244])
def l450_229(x):
    # x is a list (or vector) of length 304
    return max(0, x[245])
def l450_230(x):
    # x is a list (or vector) of length 304
    return max(0, x[246])
def l450_231(x):
    # x is a list (or vector) of length 304
    return max(0, x[247])
def l450_232(x):
    # x is a list (or vector) of length 304
    return max(0, x[248])
def l450_233(x):
    # x is a list (or vector) of length 304
    return max(0, x[249])
def l450_234(x):
    # x is a list (or vector) of length 304
    return max(0, x[250])
def l450_235(x):
    # x is a list (or vector) of length 304
    return max(0, x[251])
def l450_236(x):
    # x is a list (or vector) of length 304
    return max(0, x[252])
def l450_237(x):
    # x is a list (or vector) of length 304
    return max(0, x[253])
def l450_238(x):
    # x is a list (or vector) of length 304
    return max(0, x[254])
def l450_239(x):
    # x is a list (or vector) of length 304
    return max(0, x[255])
def l450_240(x):
    # x is a list (or vector) of length 304
    return max(0, x[256])
def l450_241(x):
    # x is a list (or vector) of length 304
    return max(0, x[257])
def l450_242(x):
    # x is a list (or vector) of length 304
    return max(0, x[258])
def l450_243(x):
    # x is a list (or vector) of length 304
    return max(0, x[259])
def l450_244(x):
    # x is a list (or vector) of length 304
    return max(0, x[260])
def l450_245(x):
    # x is a list (or vector) of length 304
    return max(0, x[261])
def l450_246(x):
    # x is a list (or vector) of length 304
    return max(0, x[262])
def l450_247(x):
    # x is a list (or vector) of length 304
    return max(0, x[263])
def l450_248(x):
    # x is a list (or vector) of length 304
    return max(0, x[264])
def l450_249(x):
    # x is a list (or vector) of length 304
    return max(0, x[265])
def l450_250(x):
    # x is a list (or vector) of length 304
    return max(0, x[266])
def l450_251(x):
    # x is a list (or vector) of length 304
    return max(0, x[267])
def l450_252(x):
    # x is a list (or vector) of length 304
    return max(0, x[268])
def l450_253(x):
    # x is a list (or vector) of length 304
    return max(0, x[269])
def l450_254(x):
    # x is a list (or vector) of length 304
    return max(0, x[270])
def l450_255(x):
    # x is a list (or vector) of length 304
    return max(0, x[271])
def l450_256(x):
    # x is a list (or vector) of length 304
    return max(0, x[272])
def l450_257(x):
    # x is a list (or vector) of length 304
    return max(0, x[273])
def l450_258(x):
    # x is a list (or vector) of length 304
    return max(0, x[274])
def l450_259(x):
    # x is a list (or vector) of length 304
    return max(0, x[275])
def l450_260(x):
    # x is a list (or vector) of length 304
    return max(0, x[276])
def l450_261(x):
    # x is a list (or vector) of length 304
    return max(0, x[277])
def l450_262(x):
    # x is a list (or vector) of length 304
    return max(0, x[278])
def l450_263(x):
    # x is a list (or vector) of length 304
    return max(0, x[279])
def l450_264(x):
    # x is a list (or vector) of length 304
    return max(0, x[280])
def l450_265(x):
    # x is a list (or vector) of length 304
    return max(0, x[281])
def l450_266(x):
    # x is a list (or vector) of length 304
    return max(0, x[282])
def l450_267(x):
    # x is a list (or vector) of length 304
    return max(0, x[283])
def l450_268(x):
    # x is a list (or vector) of length 304
    return max(0, x[284])
def l450_269(x):
    # x is a list (or vector) of length 304
    return max(0, x[285])
def l450_270(x):
    # x is a list (or vector) of length 304
    return max(0, x[286])
def l450_271(x):
    # x is a list (or vector) of length 304
    return max(0, x[287])
def l450_272(x):
    # x is a list (or vector) of length 304
    return max(0, x[288])
def l450_273(x):
    # x is a list (or vector) of length 304
    return max(0, x[289])
def l450_274(x):
    # x is a list (or vector) of length 304
    return max(0, x[290])
def l450_275(x):
    # x is a list (or vector) of length 304
    return max(0, x[291])
def l450_276(x):
    # x is a list (or vector) of length 304
    return max(0, x[292])
def l450_277(x):
    # x is a list (or vector) of length 304
    return max(0, x[293])
def l450_278(x):
    # x is a list (or vector) of length 304
    return max(0, x[294])
def l450_279(x):
    # x is a list (or vector) of length 304
    return max(0, x[295])
def l450_280(x):
    # x is a list (or vector) of length 304
    return max(0, x[296])
def l450_281(x):
    # x is a list (or vector) of length 304
    return max(0, x[297])
def l450_282(x):
    # x is a list (or vector) of length 304
    return max(0, x[298])
def l450_283(x):
    # x is a list (or vector) of length 304
    return max(0, x[299])
def l450_284(x):
    # x is a list (or vector) of length 304
    return max(0, x[300])
def l450_285(x):
    # x is a list (or vector) of length 304
    return max(0, x[301])
def l450_286(x):
    # x is a list (or vector) of length 304
    return max(0, x[302])
def l450_287(x):
    # x is a list (or vector) of length 304
    return max(0, x[303])
def l450_(x):
    # x is a list (or vector) of length 304
    return [
        l450_0(x),
        l450_1(x),
        l450_2(x),
        l450_3(x),
        l450_4(x),
        l450_5(x),
        l450_6(x),
        l450_7(x),
        l450_8(x),
        l450_9(x),
        l450_10(x),
        l450_11(x),
        l450_12(x),
        l450_13(x),
        l450_14(x),
        l450_15(x),
        l450_16(x),
        l450_17(x),
        l450_18(x),
        l450_19(x),
        l450_20(x),
        l450_21(x),
        l450_22(x),
        l450_23(x),
        l450_24(x),
        l450_25(x),
        l450_26(x),
        l450_27(x),
        l450_28(x),
        l450_29(x),
        l450_30(x),
        l450_31(x),
        l450_32(x),
        l450_33(x),
        l450_34(x),
        l450_35(x),
        l450_36(x),
        l450_37(x),
        l450_38(x),
        l450_39(x),
        l450_40(x),
        l450_41(x),
        l450_42(x),
        l450_43(x),
        l450_44(x),
        l450_45(x),
        l450_46(x),
        l450_47(x),
        l450_48(x),
        l450_49(x),
        l450_50(x),
        l450_51(x),
        l450_52(x),
        l450_53(x),
        l450_54(x),
        l450_55(x),
        l450_56(x),
        l450_57(x),
        l450_58(x),
        l450_59(x),
        l450_60(x),
        l450_61(x),
        l450_62(x),
        l450_63(x),
        l450_64(x),
        l450_65(x),
        l450_66(x),
        l450_67(x),
        l450_68(x),
        l450_69(x),
        l450_70(x),
        l450_71(x),
        l450_72(x),
        l450_73(x),
        l450_74(x),
        l450_75(x),
        l450_76(x),
        l450_77(x),
        l450_78(x),
        l450_79(x),
        l450_80(x),
        l450_81(x),
        l450_82(x),
        l450_83(x),
        l450_84(x),
        l450_85(x),
        l450_86(x),
        l450_87(x),
        l450_88(x),
        l450_89(x),
        l450_90(x),
        l450_91(x),
        l450_92(x),
        l450_93(x),
        l450_94(x),
        l450_95(x),
        l450_96(x),
        l450_97(x),
        l450_98(x),
        l450_99(x),
        l450_100(x),
        l450_101(x),
        l450_102(x),
        l450_103(x),
        l450_104(x),
        l450_105(x),
        l450_106(x),
        l450_107(x),
        l450_108(x),
        l450_109(x),
        l450_110(x),
        l450_111(x),
        l450_112(x),
        l450_113(x),
        l450_114(x),
        l450_115(x),
        l450_116(x),
        l450_117(x),
        l450_118(x),
        l450_119(x),
        l450_120(x),
        l450_121(x),
        l450_122(x),
        l450_123(x),
        l450_124(x),
        l450_125(x),
        l450_126(x),
        l450_127(x),
        l450_128(x),
        l450_129(x),
        l450_130(x),
        l450_131(x),
        l450_132(x),
        l450_133(x),
        l450_134(x),
        l450_135(x),
        l450_136(x),
        l450_137(x),
        l450_138(x),
        l450_139(x),
        l450_140(x),
        l450_141(x),
        l450_142(x),
        l450_143(x),
        l450_144(x),
        l450_145(x),
        l450_146(x),
        l450_147(x),
        l450_148(x),
        l450_149(x),
        l450_150(x),
        l450_151(x),
        l450_152(x),
        l450_153(x),
        l450_154(x),
        l450_155(x),
        l450_156(x),
        l450_157(x),
        l450_158(x),
        l450_159(x),
        l450_160(x),
        l450_161(x),
        l450_162(x),
        l450_163(x),
        l450_164(x),
        l450_165(x),
        l450_166(x),
        l450_167(x),
        l450_168(x),
        l450_169(x),
        l450_170(x),
        l450_171(x),
        l450_172(x),
        l450_173(x),
        l450_174(x),
        l450_175(x),
        l450_176(x),
        l450_177(x),
        l450_178(x),
        l450_179(x),
        l450_180(x),
        l450_181(x),
        l450_182(x),
        l450_183(x),
        l450_184(x),
        l450_185(x),
        l450_186(x),
        l450_187(x),
        l450_188(x),
        l450_189(x),
        l450_190(x),
        l450_191(x),
        l450_192(x),
        l450_193(x),
        l450_194(x),
        l450_195(x),
        l450_196(x),
        l450_197(x),
        l450_198(x),
        l450_199(x),
        l450_200(x),
        l450_201(x),
        l450_202(x),
        l450_203(x),
        l450_204(x),
        l450_205(x),
        l450_206(x),
        l450_207(x),
        l450_208(x),
        l450_209(x),
        l450_210(x),
        l450_211(x),
        l450_212(x),
        l450_213(x),
        l450_214(x),
        l450_215(x),
        l450_216(x),
        l450_217(x),
        l450_218(x),
        l450_219(x),
        l450_220(x),
        l450_221(x),
        l450_222(x),
        l450_223(x),
        l450_224(x),
        l450_225(x),
        l450_226(x),
        l450_227(x),
        l450_228(x),
        l450_229(x),
        l450_230(x),
        l450_231(x),
        l450_232(x),
        l450_233(x),
        l450_234(x),
        l450_235(x),
        l450_236(x),
        l450_237(x),
        l450_238(x),
        l450_239(x),
        l450_240(x),
        l450_241(x),
        l450_242(x),
        l450_243(x),
        l450_244(x),
        l450_245(x),
        l450_246(x),
        l450_247(x),
        l450_248(x),
        l450_249(x),
        l450_250(x),
        l450_251(x),
        l450_252(x),
        l450_253(x),
        l450_254(x),
        l450_255(x),
        l450_256(x),
        l450_257(x),
        l450_258(x),
        l450_259(x),
        l450_260(x),
        l450_261(x),
        l450_262(x),
        l450_263(x),
        l450_264(x),
        l450_265(x),
        l450_266(x),
        l450_267(x),
        l450_268(x),
        l450_269(x),
        l450_270(x),
        l450_271(x),
        l450_272(x),
        l450_273(x),
        l450_274(x),
        l450_275(x),
        l450_276(x),
        l450_277(x),
        l450_278(x),
        l450_279(x),
        l450_280(x),
        l450_281(x),
        l450_282(x),
        l450_283(x),
        l450_284(x),
        l450_285(x),
        l450_286(x),
        l450_287(x),
    ]