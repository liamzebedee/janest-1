import numpy as np




# Generated from reverse engineering
def l198_g(x: np.ndarray) -> np.ndarray:
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




def l198_0(x):
    # x is a list (or vector) of length 304
    return max(0, x[0])
def l198_1(x):
    # x is a list (or vector) of length 304
    return max(0, x[1])
def l198_2(x):
    # x is a list (or vector) of length 304
    return max(0, x[2])
def l198_3(x):
    # x is a list (or vector) of length 304
    return max(0, x[3])
def l198_4(x):
    # x is a list (or vector) of length 304
    return max(0, x[4])
def l198_5(x):
    # x is a list (or vector) of length 304
    return max(0, x[5])
def l198_6(x):
    # x is a list (or vector) of length 304
    return max(0, x[6])
def l198_7(x):
    # x is a list (or vector) of length 304
    return max(0, x[7])
def l198_8(x):
    # x is a list (or vector) of length 304
    return max(0, x[8])
def l198_9(x):
    # x is a list (or vector) of length 304
    return max(0, x[9])
def l198_10(x):
    # x is a list (or vector) of length 304
    return max(0, x[10])
def l198_11(x):
    # x is a list (or vector) of length 304
    return max(0, x[11])
def l198_12(x):
    # x is a list (or vector) of length 304
    return max(0, x[12])
def l198_13(x):
    # x is a list (or vector) of length 304
    return max(0, x[13])
def l198_14(x):
    # x is a list (or vector) of length 304
    return max(0, x[14])
def l198_15(x):
    # x is a list (or vector) of length 304
    return max(0, x[15])
def l198_16(x):
    # x is a list (or vector) of length 304
    return max(0, x[16])
def l198_17(x):
    # x is a list (or vector) of length 304
    return max(0, x[17])
def l198_18(x):
    # x is a list (or vector) of length 304
    return max(0, x[18])
def l198_19(x):
    # x is a list (or vector) of length 304
    return max(0, x[19])
def l198_20(x):
    # x is a list (or vector) of length 304
    return max(0, x[20])
def l198_21(x):
    # x is a list (or vector) of length 304
    return max(0, x[21])
def l198_22(x):
    # x is a list (or vector) of length 304
    return max(0, x[22])
def l198_23(x):
    # x is a list (or vector) of length 304
    return max(0, x[23])
def l198_24(x):
    # x is a list (or vector) of length 304
    return max(0, x[24])
def l198_25(x):
    # x is a list (or vector) of length 304
    return max(0, x[25])
def l198_26(x):
    # x is a list (or vector) of length 304
    return max(0, x[26])
def l198_27(x):
    # x is a list (or vector) of length 304
    return max(0, x[27])
def l198_28(x):
    # x is a list (or vector) of length 304
    return max(0, x[28])
def l198_29(x):
    # x is a list (or vector) of length 304
    return max(0, x[29])
def l198_30(x):
    # x is a list (or vector) of length 304
    return max(0, x[30])
def l198_31(x):
    # x is a list (or vector) of length 304
    return max(0, x[31])
def l198_32(x):
    # x is a list (or vector) of length 304
    return max(0, x[32])
def l198_33(x):
    # x is a list (or vector) of length 304
    return max(0, x[33])
def l198_34(x):
    # x is a list (or vector) of length 304
    return max(0, x[34])
def l198_35(x):
    # x is a list (or vector) of length 304
    return max(0, x[35])
def l198_36(x):
    # x is a list (or vector) of length 304
    return max(0, x[36])
def l198_37(x):
    # x is a list (or vector) of length 304
    return max(0, x[37])
def l198_38(x):
    # x is a list (or vector) of length 304
    return max(0, x[38])
def l198_39(x):
    # x is a list (or vector) of length 304
    return max(0, x[39])
def l198_40(x):
    # x is a list (or vector) of length 304
    return max(0, x[40])
def l198_41(x):
    # x is a list (or vector) of length 304
    return max(0, x[41])
def l198_42(x):
    # x is a list (or vector) of length 304
    return max(0, x[42])
def l198_43(x):
    # x is a list (or vector) of length 304
    return max(0, x[43])
def l198_44(x):
    # x is a list (or vector) of length 304
    return max(0, x[44])
def l198_45(x):
    # x is a list (or vector) of length 304
    return max(0, x[45])
def l198_46(x):
    # x is a list (or vector) of length 304
    return max(0, x[46])
def l198_47(x):
    # x is a list (or vector) of length 304
    return max(0, x[47])
def l198_48(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[48] + -1.0*x[64] + 1.0)
def l198_49(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[49] + -1.0*x[65] + 1.0)
def l198_50(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[50] + -1.0*x[66] + 1.0)
def l198_51(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[51] + -1.0*x[67] + 1.0)
def l198_52(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[52] + -1.0*x[68] + 1.0)
def l198_53(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[53] + -1.0*x[69] + 1.0)
def l198_54(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[54] + -1.0*x[70] + 1.0)
def l198_55(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[55] + -1.0*x[71] + 1.0)
def l198_56(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[56] + -1.0*x[72] + 1.0)
def l198_57(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[57] + -1.0*x[73] + 1.0)
def l198_58(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[58] + -1.0*x[74] + 1.0)
def l198_59(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[59] + -1.0*x[75] + 1.0)
def l198_60(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[60] + -1.0*x[76] + 1.0)
def l198_61(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[61] + -1.0*x[77] + 1.0)
def l198_62(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[62] + -1.0*x[78] + 1.0)
def l198_63(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[63] + -1.0*x[79] + 1.0)
def l198_64(x):
    # x is a list (or vector) of length 304
    return max(0, x[96])
def l198_65(x):
    # x is a list (or vector) of length 304
    return max(0, x[97])
def l198_66(x):
    # x is a list (or vector) of length 304
    return max(0, x[98])
def l198_67(x):
    # x is a list (or vector) of length 304
    return max(0, x[99])
def l198_68(x):
    # x is a list (or vector) of length 304
    return max(0, x[100])
def l198_69(x):
    # x is a list (or vector) of length 304
    return max(0, x[101])
def l198_70(x):
    # x is a list (or vector) of length 304
    return max(0, x[102])
def l198_71(x):
    # x is a list (or vector) of length 304
    return max(0, x[103])
def l198_72(x):
    # x is a list (or vector) of length 304
    return max(0, x[104])
def l198_73(x):
    # x is a list (or vector) of length 304
    return max(0, x[105])
def l198_74(x):
    # x is a list (or vector) of length 304
    return max(0, x[106])
def l198_75(x):
    # x is a list (or vector) of length 304
    return max(0, x[107])
def l198_76(x):
    # x is a list (or vector) of length 304
    return max(0, x[108])
def l198_77(x):
    # x is a list (or vector) of length 304
    return max(0, x[109])
def l198_78(x):
    # x is a list (or vector) of length 304
    return max(0, x[110])
def l198_79(x):
    # x is a list (or vector) of length 304
    return max(0, x[111])
def l198_80(x):
    # x is a list (or vector) of length 304
    return max(0, x[80])
def l198_81(x):
    # x is a list (or vector) of length 304
    return max(0, x[81])
def l198_82(x):
    # x is a list (or vector) of length 304
    return max(0, x[82])
def l198_83(x):
    # x is a list (or vector) of length 304
    return max(0, x[83])
def l198_84(x):
    # x is a list (or vector) of length 304
    return max(0, x[84])
def l198_85(x):
    # x is a list (or vector) of length 304
    return max(0, x[85])
def l198_86(x):
    # x is a list (or vector) of length 304
    return max(0, x[86])
def l198_87(x):
    # x is a list (or vector) of length 304
    return max(0, x[87])
def l198_88(x):
    # x is a list (or vector) of length 304
    return max(0, x[88])
def l198_89(x):
    # x is a list (or vector) of length 304
    return max(0, x[89])
def l198_90(x):
    # x is a list (or vector) of length 304
    return max(0, x[90])
def l198_91(x):
    # x is a list (or vector) of length 304
    return max(0, x[91])
def l198_92(x):
    # x is a list (or vector) of length 304
    return max(0, x[92])
def l198_93(x):
    # x is a list (or vector) of length 304
    return max(0, x[93])
def l198_94(x):
    # x is a list (or vector) of length 304
    return max(0, x[94])
def l198_95(x):
    # x is a list (or vector) of length 304
    return max(0, x[95])
def l198_96(x):
    # x is a list (or vector) of length 304
    return max(0, x[112])
def l198_97(x):
    # x is a list (or vector) of length 304
    return max(0, x[113])
def l198_98(x):
    # x is a list (or vector) of length 304
    return max(0, x[114])
def l198_99(x):
    # x is a list (or vector) of length 304
    return max(0, x[115])
def l198_100(x):
    # x is a list (or vector) of length 304
    return max(0, x[116])
def l198_101(x):
    # x is a list (or vector) of length 304
    return max(0, x[117])
def l198_102(x):
    # x is a list (or vector) of length 304
    return max(0, x[118])
def l198_103(x):
    # x is a list (or vector) of length 304
    return max(0, x[119])
def l198_104(x):
    # x is a list (or vector) of length 304
    return max(0, x[120])
def l198_105(x):
    # x is a list (or vector) of length 304
    return max(0, x[121])
def l198_106(x):
    # x is a list (or vector) of length 304
    return max(0, x[122])
def l198_107(x):
    # x is a list (or vector) of length 304
    return max(0, x[123])
def l198_108(x):
    # x is a list (or vector) of length 304
    return max(0, x[124])
def l198_109(x):
    # x is a list (or vector) of length 304
    return max(0, x[125])
def l198_110(x):
    # x is a list (or vector) of length 304
    return max(0, x[126])
def l198_111(x):
    # x is a list (or vector) of length 304
    return max(0, x[127])
def l198_112(x):
    # x is a list (or vector) of length 304
    return max(0, x[128])
def l198_113(x):
    # x is a list (or vector) of length 304
    return max(0, x[129])
def l198_114(x):
    # x is a list (or vector) of length 304
    return max(0, x[130])
def l198_115(x):
    # x is a list (or vector) of length 304
    return max(0, x[131])
def l198_116(x):
    # x is a list (or vector) of length 304
    return max(0, x[132])
def l198_117(x):
    # x is a list (or vector) of length 304
    return max(0, x[133])
def l198_118(x):
    # x is a list (or vector) of length 304
    return max(0, x[134])
def l198_119(x):
    # x is a list (or vector) of length 304
    return max(0, x[135])
def l198_120(x):
    # x is a list (or vector) of length 304
    return max(0, x[136])
def l198_121(x):
    # x is a list (or vector) of length 304
    return max(0, x[137])
def l198_122(x):
    # x is a list (or vector) of length 304
    return max(0, x[138])
def l198_123(x):
    # x is a list (or vector) of length 304
    return max(0, x[139])
def l198_124(x):
    # x is a list (or vector) of length 304
    return max(0, x[140])
def l198_125(x):
    # x is a list (or vector) of length 304
    return max(0, x[141])
def l198_126(x):
    # x is a list (or vector) of length 304
    return max(0, x[142])
def l198_127(x):
    # x is a list (or vector) of length 304
    return max(0, x[143])
def l198_128(x):
    # x is a list (or vector) of length 304
    return max(0, x[144])
def l198_129(x):
    # x is a list (or vector) of length 304
    return max(0, x[145])
def l198_130(x):
    # x is a list (or vector) of length 304
    return max(0, x[146])
def l198_131(x):
    # x is a list (or vector) of length 304
    return max(0, x[147])
def l198_132(x):
    # x is a list (or vector) of length 304
    return max(0, x[148])
def l198_133(x):
    # x is a list (or vector) of length 304
    return max(0, x[149])
def l198_134(x):
    # x is a list (or vector) of length 304
    return max(0, x[150])
def l198_135(x):
    # x is a list (or vector) of length 304
    return max(0, x[151])
def l198_136(x):
    # x is a list (or vector) of length 304
    return max(0, x[152])
def l198_137(x):
    # x is a list (or vector) of length 304
    return max(0, x[153])
def l198_138(x):
    # x is a list (or vector) of length 304
    return max(0, x[154])
def l198_139(x):
    # x is a list (or vector) of length 304
    return max(0, x[155])
def l198_140(x):
    # x is a list (or vector) of length 304
    return max(0, x[156])
def l198_141(x):
    # x is a list (or vector) of length 304
    return max(0, x[157])
def l198_142(x):
    # x is a list (or vector) of length 304
    return max(0, x[158])
def l198_143(x):
    # x is a list (or vector) of length 304
    return max(0, x[159])
def l198_144(x):
    # x is a list (or vector) of length 304
    return max(0, x[160])
def l198_145(x):
    # x is a list (or vector) of length 304
    return max(0, x[161])
def l198_146(x):
    # x is a list (or vector) of length 304
    return max(0, x[162])
def l198_147(x):
    # x is a list (or vector) of length 304
    return max(0, x[163])
def l198_148(x):
    # x is a list (or vector) of length 304
    return max(0, x[164])
def l198_149(x):
    # x is a list (or vector) of length 304
    return max(0, x[165])
def l198_150(x):
    # x is a list (or vector) of length 304
    return max(0, x[166])
def l198_151(x):
    # x is a list (or vector) of length 304
    return max(0, x[167])
def l198_152(x):
    # x is a list (or vector) of length 304
    return max(0, x[168])
def l198_153(x):
    # x is a list (or vector) of length 304
    return max(0, x[169])
def l198_154(x):
    # x is a list (or vector) of length 304
    return max(0, x[170])
def l198_155(x):
    # x is a list (or vector) of length 304
    return max(0, x[171])
def l198_156(x):
    # x is a list (or vector) of length 304
    return max(0, x[172])
def l198_157(x):
    # x is a list (or vector) of length 304
    return max(0, x[173])
def l198_158(x):
    # x is a list (or vector) of length 304
    return max(0, x[174])
def l198_159(x):
    # x is a list (or vector) of length 304
    return max(0, x[175])
def l198_160(x):
    # x is a list (or vector) of length 304
    return max(0, x[176])
def l198_161(x):
    # x is a list (or vector) of length 304
    return max(0, x[177])
def l198_162(x):
    # x is a list (or vector) of length 304
    return max(0, x[178])
def l198_163(x):
    # x is a list (or vector) of length 304
    return max(0, x[179])
def l198_164(x):
    # x is a list (or vector) of length 304
    return max(0, x[180])
def l198_165(x):
    # x is a list (or vector) of length 304
    return max(0, x[181])
def l198_166(x):
    # x is a list (or vector) of length 304
    return max(0, x[182])
def l198_167(x):
    # x is a list (or vector) of length 304
    return max(0, x[183])
def l198_168(x):
    # x is a list (or vector) of length 304
    return max(0, x[184])
def l198_169(x):
    # x is a list (or vector) of length 304
    return max(0, x[185])
def l198_170(x):
    # x is a list (or vector) of length 304
    return max(0, x[186])
def l198_171(x):
    # x is a list (or vector) of length 304
    return max(0, x[187])
def l198_172(x):
    # x is a list (or vector) of length 304
    return max(0, x[188])
def l198_173(x):
    # x is a list (or vector) of length 304
    return max(0, x[189])
def l198_174(x):
    # x is a list (or vector) of length 304
    return max(0, x[190])
def l198_175(x):
    # x is a list (or vector) of length 304
    return max(0, x[191])
def l198_176(x):
    # x is a list (or vector) of length 304
    return max(0, x[192])
def l198_177(x):
    # x is a list (or vector) of length 304
    return max(0, x[193])
def l198_178(x):
    # x is a list (or vector) of length 304
    return max(0, x[194])
def l198_179(x):
    # x is a list (or vector) of length 304
    return max(0, x[195])
def l198_180(x):
    # x is a list (or vector) of length 304
    return max(0, x[196])
def l198_181(x):
    # x is a list (or vector) of length 304
    return max(0, x[197])
def l198_182(x):
    # x is a list (or vector) of length 304
    return max(0, x[198])
def l198_183(x):
    # x is a list (or vector) of length 304
    return max(0, x[199])
def l198_184(x):
    # x is a list (or vector) of length 304
    return max(0, x[200])
def l198_185(x):
    # x is a list (or vector) of length 304
    return max(0, x[201])
def l198_186(x):
    # x is a list (or vector) of length 304
    return max(0, x[202])
def l198_187(x):
    # x is a list (or vector) of length 304
    return max(0, x[203])
def l198_188(x):
    # x is a list (or vector) of length 304
    return max(0, x[204])
def l198_189(x):
    # x is a list (or vector) of length 304
    return max(0, x[205])
def l198_190(x):
    # x is a list (or vector) of length 304
    return max(0, x[206])
def l198_191(x):
    # x is a list (or vector) of length 304
    return max(0, x[207])
def l198_192(x):
    # x is a list (or vector) of length 304
    return max(0, x[208])
def l198_193(x):
    # x is a list (or vector) of length 304
    return max(0, x[209])
def l198_194(x):
    # x is a list (or vector) of length 304
    return max(0, x[210])
def l198_195(x):
    # x is a list (or vector) of length 304
    return max(0, x[211])
def l198_196(x):
    # x is a list (or vector) of length 304
    return max(0, x[212])
def l198_197(x):
    # x is a list (or vector) of length 304
    return max(0, x[213])
def l198_198(x):
    # x is a list (or vector) of length 304
    return max(0, x[214])
def l198_199(x):
    # x is a list (or vector) of length 304
    return max(0, x[215])
def l198_200(x):
    # x is a list (or vector) of length 304
    return max(0, x[216])
def l198_201(x):
    # x is a list (or vector) of length 304
    return max(0, x[217])
def l198_202(x):
    # x is a list (or vector) of length 304
    return max(0, x[218])
def l198_203(x):
    # x is a list (or vector) of length 304
    return max(0, x[219])
def l198_204(x):
    # x is a list (or vector) of length 304
    return max(0, x[220])
def l198_205(x):
    # x is a list (or vector) of length 304
    return max(0, x[221])
def l198_206(x):
    # x is a list (or vector) of length 304
    return max(0, x[222])
def l198_207(x):
    # x is a list (or vector) of length 304
    return max(0, x[223])
def l198_208(x):
    # x is a list (or vector) of length 304
    return max(0, x[224])
def l198_209(x):
    # x is a list (or vector) of length 304
    return max(0, x[225])
def l198_210(x):
    # x is a list (or vector) of length 304
    return max(0, x[226])
def l198_211(x):
    # x is a list (or vector) of length 304
    return max(0, x[227])
def l198_212(x):
    # x is a list (or vector) of length 304
    return max(0, x[228])
def l198_213(x):
    # x is a list (or vector) of length 304
    return max(0, x[229])
def l198_214(x):
    # x is a list (or vector) of length 304
    return max(0, x[230])
def l198_215(x):
    # x is a list (or vector) of length 304
    return max(0, x[231])
def l198_216(x):
    # x is a list (or vector) of length 304
    return max(0, x[232])
def l198_217(x):
    # x is a list (or vector) of length 304
    return max(0, x[233])
def l198_218(x):
    # x is a list (or vector) of length 304
    return max(0, x[234])
def l198_219(x):
    # x is a list (or vector) of length 304
    return max(0, x[235])
def l198_220(x):
    # x is a list (or vector) of length 304
    return max(0, x[236])
def l198_221(x):
    # x is a list (or vector) of length 304
    return max(0, x[237])
def l198_222(x):
    # x is a list (or vector) of length 304
    return max(0, x[238])
def l198_223(x):
    # x is a list (or vector) of length 304
    return max(0, x[239])
def l198_224(x):
    # x is a list (or vector) of length 304
    return max(0, x[240])
def l198_225(x):
    # x is a list (or vector) of length 304
    return max(0, x[241])
def l198_226(x):
    # x is a list (or vector) of length 304
    return max(0, x[242])
def l198_227(x):
    # x is a list (or vector) of length 304
    return max(0, x[243])
def l198_228(x):
    # x is a list (or vector) of length 304
    return max(0, x[244])
def l198_229(x):
    # x is a list (or vector) of length 304
    return max(0, x[245])
def l198_230(x):
    # x is a list (or vector) of length 304
    return max(0, x[246])
def l198_231(x):
    # x is a list (or vector) of length 304
    return max(0, x[247])
def l198_232(x):
    # x is a list (or vector) of length 304
    return max(0, x[248])
def l198_233(x):
    # x is a list (or vector) of length 304
    return max(0, x[249])
def l198_234(x):
    # x is a list (or vector) of length 304
    return max(0, x[250])
def l198_235(x):
    # x is a list (or vector) of length 304
    return max(0, x[251])
def l198_236(x):
    # x is a list (or vector) of length 304
    return max(0, x[252])
def l198_237(x):
    # x is a list (or vector) of length 304
    return max(0, x[253])
def l198_238(x):
    # x is a list (or vector) of length 304
    return max(0, x[254])
def l198_239(x):
    # x is a list (or vector) of length 304
    return max(0, x[255])
def l198_240(x):
    # x is a list (or vector) of length 304
    return max(0, x[256])
def l198_241(x):
    # x is a list (or vector) of length 304
    return max(0, x[257])
def l198_242(x):
    # x is a list (or vector) of length 304
    return max(0, x[258])
def l198_243(x):
    # x is a list (or vector) of length 304
    return max(0, x[259])
def l198_244(x):
    # x is a list (or vector) of length 304
    return max(0, x[260])
def l198_245(x):
    # x is a list (or vector) of length 304
    return max(0, x[261])
def l198_246(x):
    # x is a list (or vector) of length 304
    return max(0, x[262])
def l198_247(x):
    # x is a list (or vector) of length 304
    return max(0, x[263])
def l198_248(x):
    # x is a list (or vector) of length 304
    return max(0, x[264])
def l198_249(x):
    # x is a list (or vector) of length 304
    return max(0, x[265])
def l198_250(x):
    # x is a list (or vector) of length 304
    return max(0, x[266])
def l198_251(x):
    # x is a list (or vector) of length 304
    return max(0, x[267])
def l198_252(x):
    # x is a list (or vector) of length 304
    return max(0, x[268])
def l198_253(x):
    # x is a list (or vector) of length 304
    return max(0, x[269])
def l198_254(x):
    # x is a list (or vector) of length 304
    return max(0, x[270])
def l198_255(x):
    # x is a list (or vector) of length 304
    return max(0, x[271])
def l198_256(x):
    # x is a list (or vector) of length 304
    return max(0, x[272])
def l198_257(x):
    # x is a list (or vector) of length 304
    return max(0, x[273])
def l198_258(x):
    # x is a list (or vector) of length 304
    return max(0, x[274])
def l198_259(x):
    # x is a list (or vector) of length 304
    return max(0, x[275])
def l198_260(x):
    # x is a list (or vector) of length 304
    return max(0, x[276])
def l198_261(x):
    # x is a list (or vector) of length 304
    return max(0, x[277])
def l198_262(x):
    # x is a list (or vector) of length 304
    return max(0, x[278])
def l198_263(x):
    # x is a list (or vector) of length 304
    return max(0, x[279])
def l198_264(x):
    # x is a list (or vector) of length 304
    return max(0, x[280])
def l198_265(x):
    # x is a list (or vector) of length 304
    return max(0, x[281])
def l198_266(x):
    # x is a list (or vector) of length 304
    return max(0, x[282])
def l198_267(x):
    # x is a list (or vector) of length 304
    return max(0, x[283])
def l198_268(x):
    # x is a list (or vector) of length 304
    return max(0, x[284])
def l198_269(x):
    # x is a list (or vector) of length 304
    return max(0, x[285])
def l198_270(x):
    # x is a list (or vector) of length 304
    return max(0, x[286])
def l198_271(x):
    # x is a list (or vector) of length 304
    return max(0, x[287])
def l198_272(x):
    # x is a list (or vector) of length 304
    return max(0, x[288])
def l198_273(x):
    # x is a list (or vector) of length 304
    return max(0, x[289])
def l198_274(x):
    # x is a list (or vector) of length 304
    return max(0, x[290])
def l198_275(x):
    # x is a list (or vector) of length 304
    return max(0, x[291])
def l198_276(x):
    # x is a list (or vector) of length 304
    return max(0, x[292])
def l198_277(x):
    # x is a list (or vector) of length 304
    return max(0, x[293])
def l198_278(x):
    # x is a list (or vector) of length 304
    return max(0, x[294])
def l198_279(x):
    # x is a list (or vector) of length 304
    return max(0, x[295])
def l198_280(x):
    # x is a list (or vector) of length 304
    return max(0, x[296])
def l198_281(x):
    # x is a list (or vector) of length 304
    return max(0, x[297])
def l198_282(x):
    # x is a list (or vector) of length 304
    return max(0, x[298])
def l198_283(x):
    # x is a list (or vector) of length 304
    return max(0, x[299])
def l198_284(x):
    # x is a list (or vector) of length 304
    return max(0, x[300])
def l198_285(x):
    # x is a list (or vector) of length 304
    return max(0, x[301])
def l198_286(x):
    # x is a list (or vector) of length 304
    return max(0, x[302])
def l198_287(x):
    # x is a list (or vector) of length 304
    return max(0, x[303])
def l198_(x):
    # x is a list (or vector) of length 304
    return [
        l198_0(x),
        l198_1(x),
        l198_2(x),
        l198_3(x),
        l198_4(x),
        l198_5(x),
        l198_6(x),
        l198_7(x),
        l198_8(x),
        l198_9(x),
        l198_10(x),
        l198_11(x),
        l198_12(x),
        l198_13(x),
        l198_14(x),
        l198_15(x),
        l198_16(x),
        l198_17(x),
        l198_18(x),
        l198_19(x),
        l198_20(x),
        l198_21(x),
        l198_22(x),
        l198_23(x),
        l198_24(x),
        l198_25(x),
        l198_26(x),
        l198_27(x),
        l198_28(x),
        l198_29(x),
        l198_30(x),
        l198_31(x),
        l198_32(x),
        l198_33(x),
        l198_34(x),
        l198_35(x),
        l198_36(x),
        l198_37(x),
        l198_38(x),
        l198_39(x),
        l198_40(x),
        l198_41(x),
        l198_42(x),
        l198_43(x),
        l198_44(x),
        l198_45(x),
        l198_46(x),
        l198_47(x),
        l198_48(x),
        l198_49(x),
        l198_50(x),
        l198_51(x),
        l198_52(x),
        l198_53(x),
        l198_54(x),
        l198_55(x),
        l198_56(x),
        l198_57(x),
        l198_58(x),
        l198_59(x),
        l198_60(x),
        l198_61(x),
        l198_62(x),
        l198_63(x),
        l198_64(x),
        l198_65(x),
        l198_66(x),
        l198_67(x),
        l198_68(x),
        l198_69(x),
        l198_70(x),
        l198_71(x),
        l198_72(x),
        l198_73(x),
        l198_74(x),
        l198_75(x),
        l198_76(x),
        l198_77(x),
        l198_78(x),
        l198_79(x),
        l198_80(x),
        l198_81(x),
        l198_82(x),
        l198_83(x),
        l198_84(x),
        l198_85(x),
        l198_86(x),
        l198_87(x),
        l198_88(x),
        l198_89(x),
        l198_90(x),
        l198_91(x),
        l198_92(x),
        l198_93(x),
        l198_94(x),
        l198_95(x),
        l198_96(x),
        l198_97(x),
        l198_98(x),
        l198_99(x),
        l198_100(x),
        l198_101(x),
        l198_102(x),
        l198_103(x),
        l198_104(x),
        l198_105(x),
        l198_106(x),
        l198_107(x),
        l198_108(x),
        l198_109(x),
        l198_110(x),
        l198_111(x),
        l198_112(x),
        l198_113(x),
        l198_114(x),
        l198_115(x),
        l198_116(x),
        l198_117(x),
        l198_118(x),
        l198_119(x),
        l198_120(x),
        l198_121(x),
        l198_122(x),
        l198_123(x),
        l198_124(x),
        l198_125(x),
        l198_126(x),
        l198_127(x),
        l198_128(x),
        l198_129(x),
        l198_130(x),
        l198_131(x),
        l198_132(x),
        l198_133(x),
        l198_134(x),
        l198_135(x),
        l198_136(x),
        l198_137(x),
        l198_138(x),
        l198_139(x),
        l198_140(x),
        l198_141(x),
        l198_142(x),
        l198_143(x),
        l198_144(x),
        l198_145(x),
        l198_146(x),
        l198_147(x),
        l198_148(x),
        l198_149(x),
        l198_150(x),
        l198_151(x),
        l198_152(x),
        l198_153(x),
        l198_154(x),
        l198_155(x),
        l198_156(x),
        l198_157(x),
        l198_158(x),
        l198_159(x),
        l198_160(x),
        l198_161(x),
        l198_162(x),
        l198_163(x),
        l198_164(x),
        l198_165(x),
        l198_166(x),
        l198_167(x),
        l198_168(x),
        l198_169(x),
        l198_170(x),
        l198_171(x),
        l198_172(x),
        l198_173(x),
        l198_174(x),
        l198_175(x),
        l198_176(x),
        l198_177(x),
        l198_178(x),
        l198_179(x),
        l198_180(x),
        l198_181(x),
        l198_182(x),
        l198_183(x),
        l198_184(x),
        l198_185(x),
        l198_186(x),
        l198_187(x),
        l198_188(x),
        l198_189(x),
        l198_190(x),
        l198_191(x),
        l198_192(x),
        l198_193(x),
        l198_194(x),
        l198_195(x),
        l198_196(x),
        l198_197(x),
        l198_198(x),
        l198_199(x),
        l198_200(x),
        l198_201(x),
        l198_202(x),
        l198_203(x),
        l198_204(x),
        l198_205(x),
        l198_206(x),
        l198_207(x),
        l198_208(x),
        l198_209(x),
        l198_210(x),
        l198_211(x),
        l198_212(x),
        l198_213(x),
        l198_214(x),
        l198_215(x),
        l198_216(x),
        l198_217(x),
        l198_218(x),
        l198_219(x),
        l198_220(x),
        l198_221(x),
        l198_222(x),
        l198_223(x),
        l198_224(x),
        l198_225(x),
        l198_226(x),
        l198_227(x),
        l198_228(x),
        l198_229(x),
        l198_230(x),
        l198_231(x),
        l198_232(x),
        l198_233(x),
        l198_234(x),
        l198_235(x),
        l198_236(x),
        l198_237(x),
        l198_238(x),
        l198_239(x),
        l198_240(x),
        l198_241(x),
        l198_242(x),
        l198_243(x),
        l198_244(x),
        l198_245(x),
        l198_246(x),
        l198_247(x),
        l198_248(x),
        l198_249(x),
        l198_250(x),
        l198_251(x),
        l198_252(x),
        l198_253(x),
        l198_254(x),
        l198_255(x),
        l198_256(x),
        l198_257(x),
        l198_258(x),
        l198_259(x),
        l198_260(x),
        l198_261(x),
        l198_262(x),
        l198_263(x),
        l198_264(x),
        l198_265(x),
        l198_266(x),
        l198_267(x),
        l198_268(x),
        l198_269(x),
        l198_270(x),
        l198_271(x),
        l198_272(x),
        l198_273(x),
        l198_274(x),
        l198_275(x),
        l198_276(x),
        l198_277(x),
        l198_278(x),
        l198_279(x),
        l198_280(x),
        l198_281(x),
        l198_282(x),
        l198_283(x),
        l198_284(x),
        l198_285(x),
        l198_286(x),
        l198_287(x),
    ]