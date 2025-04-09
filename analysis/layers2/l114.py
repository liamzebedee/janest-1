import numpy as np




# Generated from reverse engineering
def l114_g(x: np.ndarray) -> np.ndarray:
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




def l114_0(x):
    # x is a list (or vector) of length 304
    return max(0, x[0])
def l114_1(x):
    # x is a list (or vector) of length 304
    return max(0, x[1])
def l114_2(x):
    # x is a list (or vector) of length 304
    return max(0, x[2])
def l114_3(x):
    # x is a list (or vector) of length 304
    return max(0, x[3])
def l114_4(x):
    # x is a list (or vector) of length 304
    return max(0, x[4])
def l114_5(x):
    # x is a list (or vector) of length 304
    return max(0, x[5])
def l114_6(x):
    # x is a list (or vector) of length 304
    return max(0, x[6])
def l114_7(x):
    # x is a list (or vector) of length 304
    return max(0, x[7])
def l114_8(x):
    # x is a list (or vector) of length 304
    return max(0, x[8])
def l114_9(x):
    # x is a list (or vector) of length 304
    return max(0, x[9])
def l114_10(x):
    # x is a list (or vector) of length 304
    return max(0, x[10])
def l114_11(x):
    # x is a list (or vector) of length 304
    return max(0, x[11])
def l114_12(x):
    # x is a list (or vector) of length 304
    return max(0, x[12])
def l114_13(x):
    # x is a list (or vector) of length 304
    return max(0, x[13])
def l114_14(x):
    # x is a list (or vector) of length 304
    return max(0, x[14])
def l114_15(x):
    # x is a list (or vector) of length 304
    return max(0, x[15])
def l114_16(x):
    # x is a list (or vector) of length 304
    return max(0, x[16])
def l114_17(x):
    # x is a list (or vector) of length 304
    return max(0, x[17])
def l114_18(x):
    # x is a list (or vector) of length 304
    return max(0, x[18])
def l114_19(x):
    # x is a list (or vector) of length 304
    return max(0, x[19])
def l114_20(x):
    # x is a list (or vector) of length 304
    return max(0, x[20])
def l114_21(x):
    # x is a list (or vector) of length 304
    return max(0, x[21])
def l114_22(x):
    # x is a list (or vector) of length 304
    return max(0, x[22])
def l114_23(x):
    # x is a list (or vector) of length 304
    return max(0, x[23])
def l114_24(x):
    # x is a list (or vector) of length 304
    return max(0, x[24])
def l114_25(x):
    # x is a list (or vector) of length 304
    return max(0, x[25])
def l114_26(x):
    # x is a list (or vector) of length 304
    return max(0, x[26])
def l114_27(x):
    # x is a list (or vector) of length 304
    return max(0, x[27])
def l114_28(x):
    # x is a list (or vector) of length 304
    return max(0, x[28])
def l114_29(x):
    # x is a list (or vector) of length 304
    return max(0, x[29])
def l114_30(x):
    # x is a list (or vector) of length 304
    return max(0, x[30])
def l114_31(x):
    # x is a list (or vector) of length 304
    return max(0, x[31])
def l114_32(x):
    # x is a list (or vector) of length 304
    return max(0, x[32])
def l114_33(x):
    # x is a list (or vector) of length 304
    return max(0, x[33])
def l114_34(x):
    # x is a list (or vector) of length 304
    return max(0, x[34])
def l114_35(x):
    # x is a list (or vector) of length 304
    return max(0, x[35])
def l114_36(x):
    # x is a list (or vector) of length 304
    return max(0, x[36])
def l114_37(x):
    # x is a list (or vector) of length 304
    return max(0, x[37])
def l114_38(x):
    # x is a list (or vector) of length 304
    return max(0, x[38])
def l114_39(x):
    # x is a list (or vector) of length 304
    return max(0, x[39])
def l114_40(x):
    # x is a list (or vector) of length 304
    return max(0, x[40])
def l114_41(x):
    # x is a list (or vector) of length 304
    return max(0, x[41])
def l114_42(x):
    # x is a list (or vector) of length 304
    return max(0, x[42])
def l114_43(x):
    # x is a list (or vector) of length 304
    return max(0, x[43])
def l114_44(x):
    # x is a list (or vector) of length 304
    return max(0, x[44])
def l114_45(x):
    # x is a list (or vector) of length 304
    return max(0, x[45])
def l114_46(x):
    # x is a list (or vector) of length 304
    return max(0, x[46])
def l114_47(x):
    # x is a list (or vector) of length 304
    return max(0, x[47])
def l114_48(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[48] + -1.0*x[64] + 1.0)
def l114_49(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[49] + -1.0*x[65] + 1.0)
def l114_50(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[50] + -1.0*x[66] + 1.0)
def l114_51(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[51] + -1.0*x[67] + 1.0)
def l114_52(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[52] + -1.0*x[68] + 1.0)
def l114_53(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[53] + -1.0*x[69] + 1.0)
def l114_54(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[54] + -1.0*x[70] + 1.0)
def l114_55(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[55] + -1.0*x[71] + 1.0)
def l114_56(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[56] + -1.0*x[72] + 1.0)
def l114_57(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[57] + -1.0*x[73] + 1.0)
def l114_58(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[58] + -1.0*x[74] + 1.0)
def l114_59(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[59] + -1.0*x[75] + 1.0)
def l114_60(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[60] + -1.0*x[76] + 1.0)
def l114_61(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[61] + -1.0*x[77] + 1.0)
def l114_62(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[62] + -1.0*x[78] + 1.0)
def l114_63(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[63] + -1.0*x[79] + 1.0)
def l114_64(x):
    # x is a list (or vector) of length 304
    return max(0, x[96])
def l114_65(x):
    # x is a list (or vector) of length 304
    return max(0, x[97])
def l114_66(x):
    # x is a list (or vector) of length 304
    return max(0, x[98])
def l114_67(x):
    # x is a list (or vector) of length 304
    return max(0, x[99])
def l114_68(x):
    # x is a list (or vector) of length 304
    return max(0, x[100])
def l114_69(x):
    # x is a list (or vector) of length 304
    return max(0, x[101])
def l114_70(x):
    # x is a list (or vector) of length 304
    return max(0, x[102])
def l114_71(x):
    # x is a list (or vector) of length 304
    return max(0, x[103])
def l114_72(x):
    # x is a list (or vector) of length 304
    return max(0, x[104])
def l114_73(x):
    # x is a list (or vector) of length 304
    return max(0, x[105])
def l114_74(x):
    # x is a list (or vector) of length 304
    return max(0, x[106])
def l114_75(x):
    # x is a list (or vector) of length 304
    return max(0, x[107])
def l114_76(x):
    # x is a list (or vector) of length 304
    return max(0, x[108])
def l114_77(x):
    # x is a list (or vector) of length 304
    return max(0, x[109])
def l114_78(x):
    # x is a list (or vector) of length 304
    return max(0, x[110])
def l114_79(x):
    # x is a list (or vector) of length 304
    return max(0, x[111])
def l114_80(x):
    # x is a list (or vector) of length 304
    return max(0, x[80])
def l114_81(x):
    # x is a list (or vector) of length 304
    return max(0, x[81])
def l114_82(x):
    # x is a list (or vector) of length 304
    return max(0, x[82])
def l114_83(x):
    # x is a list (or vector) of length 304
    return max(0, x[83])
def l114_84(x):
    # x is a list (or vector) of length 304
    return max(0, x[84])
def l114_85(x):
    # x is a list (or vector) of length 304
    return max(0, x[85])
def l114_86(x):
    # x is a list (or vector) of length 304
    return max(0, x[86])
def l114_87(x):
    # x is a list (or vector) of length 304
    return max(0, x[87])
def l114_88(x):
    # x is a list (or vector) of length 304
    return max(0, x[88])
def l114_89(x):
    # x is a list (or vector) of length 304
    return max(0, x[89])
def l114_90(x):
    # x is a list (or vector) of length 304
    return max(0, x[90])
def l114_91(x):
    # x is a list (or vector) of length 304
    return max(0, x[91])
def l114_92(x):
    # x is a list (or vector) of length 304
    return max(0, x[92])
def l114_93(x):
    # x is a list (or vector) of length 304
    return max(0, x[93])
def l114_94(x):
    # x is a list (or vector) of length 304
    return max(0, x[94])
def l114_95(x):
    # x is a list (or vector) of length 304
    return max(0, x[95])
def l114_96(x):
    # x is a list (or vector) of length 304
    return max(0, x[112])
def l114_97(x):
    # x is a list (or vector) of length 304
    return max(0, x[113])
def l114_98(x):
    # x is a list (or vector) of length 304
    return max(0, x[114])
def l114_99(x):
    # x is a list (or vector) of length 304
    return max(0, x[115])
def l114_100(x):
    # x is a list (or vector) of length 304
    return max(0, x[116])
def l114_101(x):
    # x is a list (or vector) of length 304
    return max(0, x[117])
def l114_102(x):
    # x is a list (or vector) of length 304
    return max(0, x[118])
def l114_103(x):
    # x is a list (or vector) of length 304
    return max(0, x[119])
def l114_104(x):
    # x is a list (or vector) of length 304
    return max(0, x[120])
def l114_105(x):
    # x is a list (or vector) of length 304
    return max(0, x[121])
def l114_106(x):
    # x is a list (or vector) of length 304
    return max(0, x[122])
def l114_107(x):
    # x is a list (or vector) of length 304
    return max(0, x[123])
def l114_108(x):
    # x is a list (or vector) of length 304
    return max(0, x[124])
def l114_109(x):
    # x is a list (or vector) of length 304
    return max(0, x[125])
def l114_110(x):
    # x is a list (or vector) of length 304
    return max(0, x[126])
def l114_111(x):
    # x is a list (or vector) of length 304
    return max(0, x[127])
def l114_112(x):
    # x is a list (or vector) of length 304
    return max(0, x[128])
def l114_113(x):
    # x is a list (or vector) of length 304
    return max(0, x[129])
def l114_114(x):
    # x is a list (or vector) of length 304
    return max(0, x[130])
def l114_115(x):
    # x is a list (or vector) of length 304
    return max(0, x[131])
def l114_116(x):
    # x is a list (or vector) of length 304
    return max(0, x[132])
def l114_117(x):
    # x is a list (or vector) of length 304
    return max(0, x[133])
def l114_118(x):
    # x is a list (or vector) of length 304
    return max(0, x[134])
def l114_119(x):
    # x is a list (or vector) of length 304
    return max(0, x[135])
def l114_120(x):
    # x is a list (or vector) of length 304
    return max(0, x[136])
def l114_121(x):
    # x is a list (or vector) of length 304
    return max(0, x[137])
def l114_122(x):
    # x is a list (or vector) of length 304
    return max(0, x[138])
def l114_123(x):
    # x is a list (or vector) of length 304
    return max(0, x[139])
def l114_124(x):
    # x is a list (or vector) of length 304
    return max(0, x[140])
def l114_125(x):
    # x is a list (or vector) of length 304
    return max(0, x[141])
def l114_126(x):
    # x is a list (or vector) of length 304
    return max(0, x[142])
def l114_127(x):
    # x is a list (or vector) of length 304
    return max(0, x[143])
def l114_128(x):
    # x is a list (or vector) of length 304
    return max(0, x[144])
def l114_129(x):
    # x is a list (or vector) of length 304
    return max(0, x[145])
def l114_130(x):
    # x is a list (or vector) of length 304
    return max(0, x[146])
def l114_131(x):
    # x is a list (or vector) of length 304
    return max(0, x[147])
def l114_132(x):
    # x is a list (or vector) of length 304
    return max(0, x[148])
def l114_133(x):
    # x is a list (or vector) of length 304
    return max(0, x[149])
def l114_134(x):
    # x is a list (or vector) of length 304
    return max(0, x[150])
def l114_135(x):
    # x is a list (or vector) of length 304
    return max(0, x[151])
def l114_136(x):
    # x is a list (or vector) of length 304
    return max(0, x[152])
def l114_137(x):
    # x is a list (or vector) of length 304
    return max(0, x[153])
def l114_138(x):
    # x is a list (or vector) of length 304
    return max(0, x[154])
def l114_139(x):
    # x is a list (or vector) of length 304
    return max(0, x[155])
def l114_140(x):
    # x is a list (or vector) of length 304
    return max(0, x[156])
def l114_141(x):
    # x is a list (or vector) of length 304
    return max(0, x[157])
def l114_142(x):
    # x is a list (or vector) of length 304
    return max(0, x[158])
def l114_143(x):
    # x is a list (or vector) of length 304
    return max(0, x[159])
def l114_144(x):
    # x is a list (or vector) of length 304
    return max(0, x[160])
def l114_145(x):
    # x is a list (or vector) of length 304
    return max(0, x[161])
def l114_146(x):
    # x is a list (or vector) of length 304
    return max(0, x[162])
def l114_147(x):
    # x is a list (or vector) of length 304
    return max(0, x[163])
def l114_148(x):
    # x is a list (or vector) of length 304
    return max(0, x[164])
def l114_149(x):
    # x is a list (or vector) of length 304
    return max(0, x[165])
def l114_150(x):
    # x is a list (or vector) of length 304
    return max(0, x[166])
def l114_151(x):
    # x is a list (or vector) of length 304
    return max(0, x[167])
def l114_152(x):
    # x is a list (or vector) of length 304
    return max(0, x[168])
def l114_153(x):
    # x is a list (or vector) of length 304
    return max(0, x[169])
def l114_154(x):
    # x is a list (or vector) of length 304
    return max(0, x[170])
def l114_155(x):
    # x is a list (or vector) of length 304
    return max(0, x[171])
def l114_156(x):
    # x is a list (or vector) of length 304
    return max(0, x[172])
def l114_157(x):
    # x is a list (or vector) of length 304
    return max(0, x[173])
def l114_158(x):
    # x is a list (or vector) of length 304
    return max(0, x[174])
def l114_159(x):
    # x is a list (or vector) of length 304
    return max(0, x[175])
def l114_160(x):
    # x is a list (or vector) of length 304
    return max(0, x[176])
def l114_161(x):
    # x is a list (or vector) of length 304
    return max(0, x[177])
def l114_162(x):
    # x is a list (or vector) of length 304
    return max(0, x[178])
def l114_163(x):
    # x is a list (or vector) of length 304
    return max(0, x[179])
def l114_164(x):
    # x is a list (or vector) of length 304
    return max(0, x[180])
def l114_165(x):
    # x is a list (or vector) of length 304
    return max(0, x[181])
def l114_166(x):
    # x is a list (or vector) of length 304
    return max(0, x[182])
def l114_167(x):
    # x is a list (or vector) of length 304
    return max(0, x[183])
def l114_168(x):
    # x is a list (or vector) of length 304
    return max(0, x[184])
def l114_169(x):
    # x is a list (or vector) of length 304
    return max(0, x[185])
def l114_170(x):
    # x is a list (or vector) of length 304
    return max(0, x[186])
def l114_171(x):
    # x is a list (or vector) of length 304
    return max(0, x[187])
def l114_172(x):
    # x is a list (or vector) of length 304
    return max(0, x[188])
def l114_173(x):
    # x is a list (or vector) of length 304
    return max(0, x[189])
def l114_174(x):
    # x is a list (or vector) of length 304
    return max(0, x[190])
def l114_175(x):
    # x is a list (or vector) of length 304
    return max(0, x[191])
def l114_176(x):
    # x is a list (or vector) of length 304
    return max(0, x[192])
def l114_177(x):
    # x is a list (or vector) of length 304
    return max(0, x[193])
def l114_178(x):
    # x is a list (or vector) of length 304
    return max(0, x[194])
def l114_179(x):
    # x is a list (or vector) of length 304
    return max(0, x[195])
def l114_180(x):
    # x is a list (or vector) of length 304
    return max(0, x[196])
def l114_181(x):
    # x is a list (or vector) of length 304
    return max(0, x[197])
def l114_182(x):
    # x is a list (or vector) of length 304
    return max(0, x[198])
def l114_183(x):
    # x is a list (or vector) of length 304
    return max(0, x[199])
def l114_184(x):
    # x is a list (or vector) of length 304
    return max(0, x[200])
def l114_185(x):
    # x is a list (or vector) of length 304
    return max(0, x[201])
def l114_186(x):
    # x is a list (or vector) of length 304
    return max(0, x[202])
def l114_187(x):
    # x is a list (or vector) of length 304
    return max(0, x[203])
def l114_188(x):
    # x is a list (or vector) of length 304
    return max(0, x[204])
def l114_189(x):
    # x is a list (or vector) of length 304
    return max(0, x[205])
def l114_190(x):
    # x is a list (or vector) of length 304
    return max(0, x[206])
def l114_191(x):
    # x is a list (or vector) of length 304
    return max(0, x[207])
def l114_192(x):
    # x is a list (or vector) of length 304
    return max(0, x[208])
def l114_193(x):
    # x is a list (or vector) of length 304
    return max(0, x[209])
def l114_194(x):
    # x is a list (or vector) of length 304
    return max(0, x[210])
def l114_195(x):
    # x is a list (or vector) of length 304
    return max(0, x[211])
def l114_196(x):
    # x is a list (or vector) of length 304
    return max(0, x[212])
def l114_197(x):
    # x is a list (or vector) of length 304
    return max(0, x[213])
def l114_198(x):
    # x is a list (or vector) of length 304
    return max(0, x[214])
def l114_199(x):
    # x is a list (or vector) of length 304
    return max(0, x[215])
def l114_200(x):
    # x is a list (or vector) of length 304
    return max(0, x[216])
def l114_201(x):
    # x is a list (or vector) of length 304
    return max(0, x[217])
def l114_202(x):
    # x is a list (or vector) of length 304
    return max(0, x[218])
def l114_203(x):
    # x is a list (or vector) of length 304
    return max(0, x[219])
def l114_204(x):
    # x is a list (or vector) of length 304
    return max(0, x[220])
def l114_205(x):
    # x is a list (or vector) of length 304
    return max(0, x[221])
def l114_206(x):
    # x is a list (or vector) of length 304
    return max(0, x[222])
def l114_207(x):
    # x is a list (or vector) of length 304
    return max(0, x[223])
def l114_208(x):
    # x is a list (or vector) of length 304
    return max(0, x[224])
def l114_209(x):
    # x is a list (or vector) of length 304
    return max(0, x[225])
def l114_210(x):
    # x is a list (or vector) of length 304
    return max(0, x[226])
def l114_211(x):
    # x is a list (or vector) of length 304
    return max(0, x[227])
def l114_212(x):
    # x is a list (or vector) of length 304
    return max(0, x[228])
def l114_213(x):
    # x is a list (or vector) of length 304
    return max(0, x[229])
def l114_214(x):
    # x is a list (or vector) of length 304
    return max(0, x[230])
def l114_215(x):
    # x is a list (or vector) of length 304
    return max(0, x[231])
def l114_216(x):
    # x is a list (or vector) of length 304
    return max(0, x[232])
def l114_217(x):
    # x is a list (or vector) of length 304
    return max(0, x[233])
def l114_218(x):
    # x is a list (or vector) of length 304
    return max(0, x[234])
def l114_219(x):
    # x is a list (or vector) of length 304
    return max(0, x[235])
def l114_220(x):
    # x is a list (or vector) of length 304
    return max(0, x[236])
def l114_221(x):
    # x is a list (or vector) of length 304
    return max(0, x[237])
def l114_222(x):
    # x is a list (or vector) of length 304
    return max(0, x[238])
def l114_223(x):
    # x is a list (or vector) of length 304
    return max(0, x[239])
def l114_224(x):
    # x is a list (or vector) of length 304
    return max(0, x[240])
def l114_225(x):
    # x is a list (or vector) of length 304
    return max(0, x[241])
def l114_226(x):
    # x is a list (or vector) of length 304
    return max(0, x[242])
def l114_227(x):
    # x is a list (or vector) of length 304
    return max(0, x[243])
def l114_228(x):
    # x is a list (or vector) of length 304
    return max(0, x[244])
def l114_229(x):
    # x is a list (or vector) of length 304
    return max(0, x[245])
def l114_230(x):
    # x is a list (or vector) of length 304
    return max(0, x[246])
def l114_231(x):
    # x is a list (or vector) of length 304
    return max(0, x[247])
def l114_232(x):
    # x is a list (or vector) of length 304
    return max(0, x[248])
def l114_233(x):
    # x is a list (or vector) of length 304
    return max(0, x[249])
def l114_234(x):
    # x is a list (or vector) of length 304
    return max(0, x[250])
def l114_235(x):
    # x is a list (or vector) of length 304
    return max(0, x[251])
def l114_236(x):
    # x is a list (or vector) of length 304
    return max(0, x[252])
def l114_237(x):
    # x is a list (or vector) of length 304
    return max(0, x[253])
def l114_238(x):
    # x is a list (or vector) of length 304
    return max(0, x[254])
def l114_239(x):
    # x is a list (or vector) of length 304
    return max(0, x[255])
def l114_240(x):
    # x is a list (or vector) of length 304
    return max(0, x[256])
def l114_241(x):
    # x is a list (or vector) of length 304
    return max(0, x[257])
def l114_242(x):
    # x is a list (or vector) of length 304
    return max(0, x[258])
def l114_243(x):
    # x is a list (or vector) of length 304
    return max(0, x[259])
def l114_244(x):
    # x is a list (or vector) of length 304
    return max(0, x[260])
def l114_245(x):
    # x is a list (or vector) of length 304
    return max(0, x[261])
def l114_246(x):
    # x is a list (or vector) of length 304
    return max(0, x[262])
def l114_247(x):
    # x is a list (or vector) of length 304
    return max(0, x[263])
def l114_248(x):
    # x is a list (or vector) of length 304
    return max(0, x[264])
def l114_249(x):
    # x is a list (or vector) of length 304
    return max(0, x[265])
def l114_250(x):
    # x is a list (or vector) of length 304
    return max(0, x[266])
def l114_251(x):
    # x is a list (or vector) of length 304
    return max(0, x[267])
def l114_252(x):
    # x is a list (or vector) of length 304
    return max(0, x[268])
def l114_253(x):
    # x is a list (or vector) of length 304
    return max(0, x[269])
def l114_254(x):
    # x is a list (or vector) of length 304
    return max(0, x[270])
def l114_255(x):
    # x is a list (or vector) of length 304
    return max(0, x[271])
def l114_256(x):
    # x is a list (or vector) of length 304
    return max(0, x[272])
def l114_257(x):
    # x is a list (or vector) of length 304
    return max(0, x[273])
def l114_258(x):
    # x is a list (or vector) of length 304
    return max(0, x[274])
def l114_259(x):
    # x is a list (or vector) of length 304
    return max(0, x[275])
def l114_260(x):
    # x is a list (or vector) of length 304
    return max(0, x[276])
def l114_261(x):
    # x is a list (or vector) of length 304
    return max(0, x[277])
def l114_262(x):
    # x is a list (or vector) of length 304
    return max(0, x[278])
def l114_263(x):
    # x is a list (or vector) of length 304
    return max(0, x[279])
def l114_264(x):
    # x is a list (or vector) of length 304
    return max(0, x[280])
def l114_265(x):
    # x is a list (or vector) of length 304
    return max(0, x[281])
def l114_266(x):
    # x is a list (or vector) of length 304
    return max(0, x[282])
def l114_267(x):
    # x is a list (or vector) of length 304
    return max(0, x[283])
def l114_268(x):
    # x is a list (or vector) of length 304
    return max(0, x[284])
def l114_269(x):
    # x is a list (or vector) of length 304
    return max(0, x[285])
def l114_270(x):
    # x is a list (or vector) of length 304
    return max(0, x[286])
def l114_271(x):
    # x is a list (or vector) of length 304
    return max(0, x[287])
def l114_272(x):
    # x is a list (or vector) of length 304
    return max(0, x[288])
def l114_273(x):
    # x is a list (or vector) of length 304
    return max(0, x[289])
def l114_274(x):
    # x is a list (or vector) of length 304
    return max(0, x[290])
def l114_275(x):
    # x is a list (or vector) of length 304
    return max(0, x[291])
def l114_276(x):
    # x is a list (or vector) of length 304
    return max(0, x[292])
def l114_277(x):
    # x is a list (or vector) of length 304
    return max(0, x[293])
def l114_278(x):
    # x is a list (or vector) of length 304
    return max(0, x[294])
def l114_279(x):
    # x is a list (or vector) of length 304
    return max(0, x[295])
def l114_280(x):
    # x is a list (or vector) of length 304
    return max(0, x[296])
def l114_281(x):
    # x is a list (or vector) of length 304
    return max(0, x[297])
def l114_282(x):
    # x is a list (or vector) of length 304
    return max(0, x[298])
def l114_283(x):
    # x is a list (or vector) of length 304
    return max(0, x[299])
def l114_284(x):
    # x is a list (or vector) of length 304
    return max(0, x[300])
def l114_285(x):
    # x is a list (or vector) of length 304
    return max(0, x[301])
def l114_286(x):
    # x is a list (or vector) of length 304
    return max(0, x[302])
def l114_287(x):
    # x is a list (or vector) of length 304
    return max(0, x[303])
def l114_(x):
    # x is a list (or vector) of length 304
    return [
        l114_0(x),
        l114_1(x),
        l114_2(x),
        l114_3(x),
        l114_4(x),
        l114_5(x),
        l114_6(x),
        l114_7(x),
        l114_8(x),
        l114_9(x),
        l114_10(x),
        l114_11(x),
        l114_12(x),
        l114_13(x),
        l114_14(x),
        l114_15(x),
        l114_16(x),
        l114_17(x),
        l114_18(x),
        l114_19(x),
        l114_20(x),
        l114_21(x),
        l114_22(x),
        l114_23(x),
        l114_24(x),
        l114_25(x),
        l114_26(x),
        l114_27(x),
        l114_28(x),
        l114_29(x),
        l114_30(x),
        l114_31(x),
        l114_32(x),
        l114_33(x),
        l114_34(x),
        l114_35(x),
        l114_36(x),
        l114_37(x),
        l114_38(x),
        l114_39(x),
        l114_40(x),
        l114_41(x),
        l114_42(x),
        l114_43(x),
        l114_44(x),
        l114_45(x),
        l114_46(x),
        l114_47(x),
        l114_48(x),
        l114_49(x),
        l114_50(x),
        l114_51(x),
        l114_52(x),
        l114_53(x),
        l114_54(x),
        l114_55(x),
        l114_56(x),
        l114_57(x),
        l114_58(x),
        l114_59(x),
        l114_60(x),
        l114_61(x),
        l114_62(x),
        l114_63(x),
        l114_64(x),
        l114_65(x),
        l114_66(x),
        l114_67(x),
        l114_68(x),
        l114_69(x),
        l114_70(x),
        l114_71(x),
        l114_72(x),
        l114_73(x),
        l114_74(x),
        l114_75(x),
        l114_76(x),
        l114_77(x),
        l114_78(x),
        l114_79(x),
        l114_80(x),
        l114_81(x),
        l114_82(x),
        l114_83(x),
        l114_84(x),
        l114_85(x),
        l114_86(x),
        l114_87(x),
        l114_88(x),
        l114_89(x),
        l114_90(x),
        l114_91(x),
        l114_92(x),
        l114_93(x),
        l114_94(x),
        l114_95(x),
        l114_96(x),
        l114_97(x),
        l114_98(x),
        l114_99(x),
        l114_100(x),
        l114_101(x),
        l114_102(x),
        l114_103(x),
        l114_104(x),
        l114_105(x),
        l114_106(x),
        l114_107(x),
        l114_108(x),
        l114_109(x),
        l114_110(x),
        l114_111(x),
        l114_112(x),
        l114_113(x),
        l114_114(x),
        l114_115(x),
        l114_116(x),
        l114_117(x),
        l114_118(x),
        l114_119(x),
        l114_120(x),
        l114_121(x),
        l114_122(x),
        l114_123(x),
        l114_124(x),
        l114_125(x),
        l114_126(x),
        l114_127(x),
        l114_128(x),
        l114_129(x),
        l114_130(x),
        l114_131(x),
        l114_132(x),
        l114_133(x),
        l114_134(x),
        l114_135(x),
        l114_136(x),
        l114_137(x),
        l114_138(x),
        l114_139(x),
        l114_140(x),
        l114_141(x),
        l114_142(x),
        l114_143(x),
        l114_144(x),
        l114_145(x),
        l114_146(x),
        l114_147(x),
        l114_148(x),
        l114_149(x),
        l114_150(x),
        l114_151(x),
        l114_152(x),
        l114_153(x),
        l114_154(x),
        l114_155(x),
        l114_156(x),
        l114_157(x),
        l114_158(x),
        l114_159(x),
        l114_160(x),
        l114_161(x),
        l114_162(x),
        l114_163(x),
        l114_164(x),
        l114_165(x),
        l114_166(x),
        l114_167(x),
        l114_168(x),
        l114_169(x),
        l114_170(x),
        l114_171(x),
        l114_172(x),
        l114_173(x),
        l114_174(x),
        l114_175(x),
        l114_176(x),
        l114_177(x),
        l114_178(x),
        l114_179(x),
        l114_180(x),
        l114_181(x),
        l114_182(x),
        l114_183(x),
        l114_184(x),
        l114_185(x),
        l114_186(x),
        l114_187(x),
        l114_188(x),
        l114_189(x),
        l114_190(x),
        l114_191(x),
        l114_192(x),
        l114_193(x),
        l114_194(x),
        l114_195(x),
        l114_196(x),
        l114_197(x),
        l114_198(x),
        l114_199(x),
        l114_200(x),
        l114_201(x),
        l114_202(x),
        l114_203(x),
        l114_204(x),
        l114_205(x),
        l114_206(x),
        l114_207(x),
        l114_208(x),
        l114_209(x),
        l114_210(x),
        l114_211(x),
        l114_212(x),
        l114_213(x),
        l114_214(x),
        l114_215(x),
        l114_216(x),
        l114_217(x),
        l114_218(x),
        l114_219(x),
        l114_220(x),
        l114_221(x),
        l114_222(x),
        l114_223(x),
        l114_224(x),
        l114_225(x),
        l114_226(x),
        l114_227(x),
        l114_228(x),
        l114_229(x),
        l114_230(x),
        l114_231(x),
        l114_232(x),
        l114_233(x),
        l114_234(x),
        l114_235(x),
        l114_236(x),
        l114_237(x),
        l114_238(x),
        l114_239(x),
        l114_240(x),
        l114_241(x),
        l114_242(x),
        l114_243(x),
        l114_244(x),
        l114_245(x),
        l114_246(x),
        l114_247(x),
        l114_248(x),
        l114_249(x),
        l114_250(x),
        l114_251(x),
        l114_252(x),
        l114_253(x),
        l114_254(x),
        l114_255(x),
        l114_256(x),
        l114_257(x),
        l114_258(x),
        l114_259(x),
        l114_260(x),
        l114_261(x),
        l114_262(x),
        l114_263(x),
        l114_264(x),
        l114_265(x),
        l114_266(x),
        l114_267(x),
        l114_268(x),
        l114_269(x),
        l114_270(x),
        l114_271(x),
        l114_272(x),
        l114_273(x),
        l114_274(x),
        l114_275(x),
        l114_276(x),
        l114_277(x),
        l114_278(x),
        l114_279(x),
        l114_280(x),
        l114_281(x),
        l114_282(x),
        l114_283(x),
        l114_284(x),
        l114_285(x),
        l114_286(x),
        l114_287(x),
    ]