import numpy as np




# Generated from reverse engineering
def l534_g(x: np.ndarray) -> np.ndarray:
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




def l534_0(x):
    # x is a list (or vector) of length 304
    return max(0, x[0])
def l534_1(x):
    # x is a list (or vector) of length 304
    return max(0, x[1])
def l534_2(x):
    # x is a list (or vector) of length 304
    return max(0, x[2])
def l534_3(x):
    # x is a list (or vector) of length 304
    return max(0, x[3])
def l534_4(x):
    # x is a list (or vector) of length 304
    return max(0, x[4])
def l534_5(x):
    # x is a list (or vector) of length 304
    return max(0, x[5])
def l534_6(x):
    # x is a list (or vector) of length 304
    return max(0, x[6])
def l534_7(x):
    # x is a list (or vector) of length 304
    return max(0, x[7])
def l534_8(x):
    # x is a list (or vector) of length 304
    return max(0, x[8])
def l534_9(x):
    # x is a list (or vector) of length 304
    return max(0, x[9])
def l534_10(x):
    # x is a list (or vector) of length 304
    return max(0, x[10])
def l534_11(x):
    # x is a list (or vector) of length 304
    return max(0, x[11])
def l534_12(x):
    # x is a list (or vector) of length 304
    return max(0, x[12])
def l534_13(x):
    # x is a list (or vector) of length 304
    return max(0, x[13])
def l534_14(x):
    # x is a list (or vector) of length 304
    return max(0, x[14])
def l534_15(x):
    # x is a list (or vector) of length 304
    return max(0, x[15])
def l534_16(x):
    # x is a list (or vector) of length 304
    return max(0, x[16])
def l534_17(x):
    # x is a list (or vector) of length 304
    return max(0, x[17])
def l534_18(x):
    # x is a list (or vector) of length 304
    return max(0, x[18])
def l534_19(x):
    # x is a list (or vector) of length 304
    return max(0, x[19])
def l534_20(x):
    # x is a list (or vector) of length 304
    return max(0, x[20])
def l534_21(x):
    # x is a list (or vector) of length 304
    return max(0, x[21])
def l534_22(x):
    # x is a list (or vector) of length 304
    return max(0, x[22])
def l534_23(x):
    # x is a list (or vector) of length 304
    return max(0, x[23])
def l534_24(x):
    # x is a list (or vector) of length 304
    return max(0, x[24])
def l534_25(x):
    # x is a list (or vector) of length 304
    return max(0, x[25])
def l534_26(x):
    # x is a list (or vector) of length 304
    return max(0, x[26])
def l534_27(x):
    # x is a list (or vector) of length 304
    return max(0, x[27])
def l534_28(x):
    # x is a list (or vector) of length 304
    return max(0, x[28])
def l534_29(x):
    # x is a list (or vector) of length 304
    return max(0, x[29])
def l534_30(x):
    # x is a list (or vector) of length 304
    return max(0, x[30])
def l534_31(x):
    # x is a list (or vector) of length 304
    return max(0, x[31])
def l534_32(x):
    # x is a list (or vector) of length 304
    return max(0, x[32])
def l534_33(x):
    # x is a list (or vector) of length 304
    return max(0, x[33])
def l534_34(x):
    # x is a list (or vector) of length 304
    return max(0, x[34])
def l534_35(x):
    # x is a list (or vector) of length 304
    return max(0, x[35])
def l534_36(x):
    # x is a list (or vector) of length 304
    return max(0, x[36])
def l534_37(x):
    # x is a list (or vector) of length 304
    return max(0, x[37])
def l534_38(x):
    # x is a list (or vector) of length 304
    return max(0, x[38])
def l534_39(x):
    # x is a list (or vector) of length 304
    return max(0, x[39])
def l534_40(x):
    # x is a list (or vector) of length 304
    return max(0, x[40])
def l534_41(x):
    # x is a list (or vector) of length 304
    return max(0, x[41])
def l534_42(x):
    # x is a list (or vector) of length 304
    return max(0, x[42])
def l534_43(x):
    # x is a list (or vector) of length 304
    return max(0, x[43])
def l534_44(x):
    # x is a list (or vector) of length 304
    return max(0, x[44])
def l534_45(x):
    # x is a list (or vector) of length 304
    return max(0, x[45])
def l534_46(x):
    # x is a list (or vector) of length 304
    return max(0, x[46])
def l534_47(x):
    # x is a list (or vector) of length 304
    return max(0, x[47])
def l534_48(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[48] + -1.0*x[64] + 1.0)
def l534_49(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[49] + -1.0*x[65] + 1.0)
def l534_50(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[50] + -1.0*x[66] + 1.0)
def l534_51(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[51] + -1.0*x[67] + 1.0)
def l534_52(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[52] + -1.0*x[68] + 1.0)
def l534_53(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[53] + -1.0*x[69] + 1.0)
def l534_54(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[54] + -1.0*x[70] + 1.0)
def l534_55(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[55] + -1.0*x[71] + 1.0)
def l534_56(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[56] + -1.0*x[72] + 1.0)
def l534_57(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[57] + -1.0*x[73] + 1.0)
def l534_58(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[58] + -1.0*x[74] + 1.0)
def l534_59(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[59] + -1.0*x[75] + 1.0)
def l534_60(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[60] + -1.0*x[76] + 1.0)
def l534_61(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[61] + -1.0*x[77] + 1.0)
def l534_62(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[62] + -1.0*x[78] + 1.0)
def l534_63(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[63] + -1.0*x[79] + 1.0)
def l534_64(x):
    # x is a list (or vector) of length 304
    return max(0, x[96])
def l534_65(x):
    # x is a list (or vector) of length 304
    return max(0, x[97])
def l534_66(x):
    # x is a list (or vector) of length 304
    return max(0, x[98])
def l534_67(x):
    # x is a list (or vector) of length 304
    return max(0, x[99])
def l534_68(x):
    # x is a list (or vector) of length 304
    return max(0, x[100])
def l534_69(x):
    # x is a list (or vector) of length 304
    return max(0, x[101])
def l534_70(x):
    # x is a list (or vector) of length 304
    return max(0, x[102])
def l534_71(x):
    # x is a list (or vector) of length 304
    return max(0, x[103])
def l534_72(x):
    # x is a list (or vector) of length 304
    return max(0, x[104])
def l534_73(x):
    # x is a list (or vector) of length 304
    return max(0, x[105])
def l534_74(x):
    # x is a list (or vector) of length 304
    return max(0, x[106])
def l534_75(x):
    # x is a list (or vector) of length 304
    return max(0, x[107])
def l534_76(x):
    # x is a list (or vector) of length 304
    return max(0, x[108])
def l534_77(x):
    # x is a list (or vector) of length 304
    return max(0, x[109])
def l534_78(x):
    # x is a list (or vector) of length 304
    return max(0, x[110])
def l534_79(x):
    # x is a list (or vector) of length 304
    return max(0, x[111])
def l534_80(x):
    # x is a list (or vector) of length 304
    return max(0, x[80])
def l534_81(x):
    # x is a list (or vector) of length 304
    return max(0, x[81])
def l534_82(x):
    # x is a list (or vector) of length 304
    return max(0, x[82])
def l534_83(x):
    # x is a list (or vector) of length 304
    return max(0, x[83])
def l534_84(x):
    # x is a list (or vector) of length 304
    return max(0, x[84])
def l534_85(x):
    # x is a list (or vector) of length 304
    return max(0, x[85])
def l534_86(x):
    # x is a list (or vector) of length 304
    return max(0, x[86])
def l534_87(x):
    # x is a list (or vector) of length 304
    return max(0, x[87])
def l534_88(x):
    # x is a list (or vector) of length 304
    return max(0, x[88])
def l534_89(x):
    # x is a list (or vector) of length 304
    return max(0, x[89])
def l534_90(x):
    # x is a list (or vector) of length 304
    return max(0, x[90])
def l534_91(x):
    # x is a list (or vector) of length 304
    return max(0, x[91])
def l534_92(x):
    # x is a list (or vector) of length 304
    return max(0, x[92])
def l534_93(x):
    # x is a list (or vector) of length 304
    return max(0, x[93])
def l534_94(x):
    # x is a list (or vector) of length 304
    return max(0, x[94])
def l534_95(x):
    # x is a list (or vector) of length 304
    return max(0, x[95])
def l534_96(x):
    # x is a list (or vector) of length 304
    return max(0, x[112])
def l534_97(x):
    # x is a list (or vector) of length 304
    return max(0, x[113])
def l534_98(x):
    # x is a list (or vector) of length 304
    return max(0, x[114])
def l534_99(x):
    # x is a list (or vector) of length 304
    return max(0, x[115])
def l534_100(x):
    # x is a list (or vector) of length 304
    return max(0, x[116])
def l534_101(x):
    # x is a list (or vector) of length 304
    return max(0, x[117])
def l534_102(x):
    # x is a list (or vector) of length 304
    return max(0, x[118])
def l534_103(x):
    # x is a list (or vector) of length 304
    return max(0, x[119])
def l534_104(x):
    # x is a list (or vector) of length 304
    return max(0, x[120])
def l534_105(x):
    # x is a list (or vector) of length 304
    return max(0, x[121])
def l534_106(x):
    # x is a list (or vector) of length 304
    return max(0, x[122])
def l534_107(x):
    # x is a list (or vector) of length 304
    return max(0, x[123])
def l534_108(x):
    # x is a list (or vector) of length 304
    return max(0, x[124])
def l534_109(x):
    # x is a list (or vector) of length 304
    return max(0, x[125])
def l534_110(x):
    # x is a list (or vector) of length 304
    return max(0, x[126])
def l534_111(x):
    # x is a list (or vector) of length 304
    return max(0, x[127])
def l534_112(x):
    # x is a list (or vector) of length 304
    return max(0, x[128])
def l534_113(x):
    # x is a list (or vector) of length 304
    return max(0, x[129])
def l534_114(x):
    # x is a list (or vector) of length 304
    return max(0, x[130])
def l534_115(x):
    # x is a list (or vector) of length 304
    return max(0, x[131])
def l534_116(x):
    # x is a list (or vector) of length 304
    return max(0, x[132])
def l534_117(x):
    # x is a list (or vector) of length 304
    return max(0, x[133])
def l534_118(x):
    # x is a list (or vector) of length 304
    return max(0, x[134])
def l534_119(x):
    # x is a list (or vector) of length 304
    return max(0, x[135])
def l534_120(x):
    # x is a list (or vector) of length 304
    return max(0, x[136])
def l534_121(x):
    # x is a list (or vector) of length 304
    return max(0, x[137])
def l534_122(x):
    # x is a list (or vector) of length 304
    return max(0, x[138])
def l534_123(x):
    # x is a list (or vector) of length 304
    return max(0, x[139])
def l534_124(x):
    # x is a list (or vector) of length 304
    return max(0, x[140])
def l534_125(x):
    # x is a list (or vector) of length 304
    return max(0, x[141])
def l534_126(x):
    # x is a list (or vector) of length 304
    return max(0, x[142])
def l534_127(x):
    # x is a list (or vector) of length 304
    return max(0, x[143])
def l534_128(x):
    # x is a list (or vector) of length 304
    return max(0, x[144])
def l534_129(x):
    # x is a list (or vector) of length 304
    return max(0, x[145])
def l534_130(x):
    # x is a list (or vector) of length 304
    return max(0, x[146])
def l534_131(x):
    # x is a list (or vector) of length 304
    return max(0, x[147])
def l534_132(x):
    # x is a list (or vector) of length 304
    return max(0, x[148])
def l534_133(x):
    # x is a list (or vector) of length 304
    return max(0, x[149])
def l534_134(x):
    # x is a list (or vector) of length 304
    return max(0, x[150])
def l534_135(x):
    # x is a list (or vector) of length 304
    return max(0, x[151])
def l534_136(x):
    # x is a list (or vector) of length 304
    return max(0, x[152])
def l534_137(x):
    # x is a list (or vector) of length 304
    return max(0, x[153])
def l534_138(x):
    # x is a list (or vector) of length 304
    return max(0, x[154])
def l534_139(x):
    # x is a list (or vector) of length 304
    return max(0, x[155])
def l534_140(x):
    # x is a list (or vector) of length 304
    return max(0, x[156])
def l534_141(x):
    # x is a list (or vector) of length 304
    return max(0, x[157])
def l534_142(x):
    # x is a list (or vector) of length 304
    return max(0, x[158])
def l534_143(x):
    # x is a list (or vector) of length 304
    return max(0, x[159])
def l534_144(x):
    # x is a list (or vector) of length 304
    return max(0, x[160])
def l534_145(x):
    # x is a list (or vector) of length 304
    return max(0, x[161])
def l534_146(x):
    # x is a list (or vector) of length 304
    return max(0, x[162])
def l534_147(x):
    # x is a list (or vector) of length 304
    return max(0, x[163])
def l534_148(x):
    # x is a list (or vector) of length 304
    return max(0, x[164])
def l534_149(x):
    # x is a list (or vector) of length 304
    return max(0, x[165])
def l534_150(x):
    # x is a list (or vector) of length 304
    return max(0, x[166])
def l534_151(x):
    # x is a list (or vector) of length 304
    return max(0, x[167])
def l534_152(x):
    # x is a list (or vector) of length 304
    return max(0, x[168])
def l534_153(x):
    # x is a list (or vector) of length 304
    return max(0, x[169])
def l534_154(x):
    # x is a list (or vector) of length 304
    return max(0, x[170])
def l534_155(x):
    # x is a list (or vector) of length 304
    return max(0, x[171])
def l534_156(x):
    # x is a list (or vector) of length 304
    return max(0, x[172])
def l534_157(x):
    # x is a list (or vector) of length 304
    return max(0, x[173])
def l534_158(x):
    # x is a list (or vector) of length 304
    return max(0, x[174])
def l534_159(x):
    # x is a list (or vector) of length 304
    return max(0, x[175])
def l534_160(x):
    # x is a list (or vector) of length 304
    return max(0, x[176])
def l534_161(x):
    # x is a list (or vector) of length 304
    return max(0, x[177])
def l534_162(x):
    # x is a list (or vector) of length 304
    return max(0, x[178])
def l534_163(x):
    # x is a list (or vector) of length 304
    return max(0, x[179])
def l534_164(x):
    # x is a list (or vector) of length 304
    return max(0, x[180])
def l534_165(x):
    # x is a list (or vector) of length 304
    return max(0, x[181])
def l534_166(x):
    # x is a list (or vector) of length 304
    return max(0, x[182])
def l534_167(x):
    # x is a list (or vector) of length 304
    return max(0, x[183])
def l534_168(x):
    # x is a list (or vector) of length 304
    return max(0, x[184])
def l534_169(x):
    # x is a list (or vector) of length 304
    return max(0, x[185])
def l534_170(x):
    # x is a list (or vector) of length 304
    return max(0, x[186])
def l534_171(x):
    # x is a list (or vector) of length 304
    return max(0, x[187])
def l534_172(x):
    # x is a list (or vector) of length 304
    return max(0, x[188])
def l534_173(x):
    # x is a list (or vector) of length 304
    return max(0, x[189])
def l534_174(x):
    # x is a list (or vector) of length 304
    return max(0, x[190])
def l534_175(x):
    # x is a list (or vector) of length 304
    return max(0, x[191])
def l534_176(x):
    # x is a list (or vector) of length 304
    return max(0, x[192])
def l534_177(x):
    # x is a list (or vector) of length 304
    return max(0, x[193])
def l534_178(x):
    # x is a list (or vector) of length 304
    return max(0, x[194])
def l534_179(x):
    # x is a list (or vector) of length 304
    return max(0, x[195])
def l534_180(x):
    # x is a list (or vector) of length 304
    return max(0, x[196])
def l534_181(x):
    # x is a list (or vector) of length 304
    return max(0, x[197])
def l534_182(x):
    # x is a list (or vector) of length 304
    return max(0, x[198])
def l534_183(x):
    # x is a list (or vector) of length 304
    return max(0, x[199])
def l534_184(x):
    # x is a list (or vector) of length 304
    return max(0, x[200])
def l534_185(x):
    # x is a list (or vector) of length 304
    return max(0, x[201])
def l534_186(x):
    # x is a list (or vector) of length 304
    return max(0, x[202])
def l534_187(x):
    # x is a list (or vector) of length 304
    return max(0, x[203])
def l534_188(x):
    # x is a list (or vector) of length 304
    return max(0, x[204])
def l534_189(x):
    # x is a list (or vector) of length 304
    return max(0, x[205])
def l534_190(x):
    # x is a list (or vector) of length 304
    return max(0, x[206])
def l534_191(x):
    # x is a list (or vector) of length 304
    return max(0, x[207])
def l534_192(x):
    # x is a list (or vector) of length 304
    return max(0, x[208])
def l534_193(x):
    # x is a list (or vector) of length 304
    return max(0, x[209])
def l534_194(x):
    # x is a list (or vector) of length 304
    return max(0, x[210])
def l534_195(x):
    # x is a list (or vector) of length 304
    return max(0, x[211])
def l534_196(x):
    # x is a list (or vector) of length 304
    return max(0, x[212])
def l534_197(x):
    # x is a list (or vector) of length 304
    return max(0, x[213])
def l534_198(x):
    # x is a list (or vector) of length 304
    return max(0, x[214])
def l534_199(x):
    # x is a list (or vector) of length 304
    return max(0, x[215])
def l534_200(x):
    # x is a list (or vector) of length 304
    return max(0, x[216])
def l534_201(x):
    # x is a list (or vector) of length 304
    return max(0, x[217])
def l534_202(x):
    # x is a list (or vector) of length 304
    return max(0, x[218])
def l534_203(x):
    # x is a list (or vector) of length 304
    return max(0, x[219])
def l534_204(x):
    # x is a list (or vector) of length 304
    return max(0, x[220])
def l534_205(x):
    # x is a list (or vector) of length 304
    return max(0, x[221])
def l534_206(x):
    # x is a list (or vector) of length 304
    return max(0, x[222])
def l534_207(x):
    # x is a list (or vector) of length 304
    return max(0, x[223])
def l534_208(x):
    # x is a list (or vector) of length 304
    return max(0, x[224])
def l534_209(x):
    # x is a list (or vector) of length 304
    return max(0, x[225])
def l534_210(x):
    # x is a list (or vector) of length 304
    return max(0, x[226])
def l534_211(x):
    # x is a list (or vector) of length 304
    return max(0, x[227])
def l534_212(x):
    # x is a list (or vector) of length 304
    return max(0, x[228])
def l534_213(x):
    # x is a list (or vector) of length 304
    return max(0, x[229])
def l534_214(x):
    # x is a list (or vector) of length 304
    return max(0, x[230])
def l534_215(x):
    # x is a list (or vector) of length 304
    return max(0, x[231])
def l534_216(x):
    # x is a list (or vector) of length 304
    return max(0, x[232])
def l534_217(x):
    # x is a list (or vector) of length 304
    return max(0, x[233])
def l534_218(x):
    # x is a list (or vector) of length 304
    return max(0, x[234])
def l534_219(x):
    # x is a list (or vector) of length 304
    return max(0, x[235])
def l534_220(x):
    # x is a list (or vector) of length 304
    return max(0, x[236])
def l534_221(x):
    # x is a list (or vector) of length 304
    return max(0, x[237])
def l534_222(x):
    # x is a list (or vector) of length 304
    return max(0, x[238])
def l534_223(x):
    # x is a list (or vector) of length 304
    return max(0, x[239])
def l534_224(x):
    # x is a list (or vector) of length 304
    return max(0, x[240])
def l534_225(x):
    # x is a list (or vector) of length 304
    return max(0, x[241])
def l534_226(x):
    # x is a list (or vector) of length 304
    return max(0, x[242])
def l534_227(x):
    # x is a list (or vector) of length 304
    return max(0, x[243])
def l534_228(x):
    # x is a list (or vector) of length 304
    return max(0, x[244])
def l534_229(x):
    # x is a list (or vector) of length 304
    return max(0, x[245])
def l534_230(x):
    # x is a list (or vector) of length 304
    return max(0, x[246])
def l534_231(x):
    # x is a list (or vector) of length 304
    return max(0, x[247])
def l534_232(x):
    # x is a list (or vector) of length 304
    return max(0, x[248])
def l534_233(x):
    # x is a list (or vector) of length 304
    return max(0, x[249])
def l534_234(x):
    # x is a list (or vector) of length 304
    return max(0, x[250])
def l534_235(x):
    # x is a list (or vector) of length 304
    return max(0, x[251])
def l534_236(x):
    # x is a list (or vector) of length 304
    return max(0, x[252])
def l534_237(x):
    # x is a list (or vector) of length 304
    return max(0, x[253])
def l534_238(x):
    # x is a list (or vector) of length 304
    return max(0, x[254])
def l534_239(x):
    # x is a list (or vector) of length 304
    return max(0, x[255])
def l534_240(x):
    # x is a list (or vector) of length 304
    return max(0, x[256])
def l534_241(x):
    # x is a list (or vector) of length 304
    return max(0, x[257])
def l534_242(x):
    # x is a list (or vector) of length 304
    return max(0, x[258])
def l534_243(x):
    # x is a list (or vector) of length 304
    return max(0, x[259])
def l534_244(x):
    # x is a list (or vector) of length 304
    return max(0, x[260])
def l534_245(x):
    # x is a list (or vector) of length 304
    return max(0, x[261])
def l534_246(x):
    # x is a list (or vector) of length 304
    return max(0, x[262])
def l534_247(x):
    # x is a list (or vector) of length 304
    return max(0, x[263])
def l534_248(x):
    # x is a list (or vector) of length 304
    return max(0, x[264])
def l534_249(x):
    # x is a list (or vector) of length 304
    return max(0, x[265])
def l534_250(x):
    # x is a list (or vector) of length 304
    return max(0, x[266])
def l534_251(x):
    # x is a list (or vector) of length 304
    return max(0, x[267])
def l534_252(x):
    # x is a list (or vector) of length 304
    return max(0, x[268])
def l534_253(x):
    # x is a list (or vector) of length 304
    return max(0, x[269])
def l534_254(x):
    # x is a list (or vector) of length 304
    return max(0, x[270])
def l534_255(x):
    # x is a list (or vector) of length 304
    return max(0, x[271])
def l534_256(x):
    # x is a list (or vector) of length 304
    return max(0, x[272])
def l534_257(x):
    # x is a list (or vector) of length 304
    return max(0, x[273])
def l534_258(x):
    # x is a list (or vector) of length 304
    return max(0, x[274])
def l534_259(x):
    # x is a list (or vector) of length 304
    return max(0, x[275])
def l534_260(x):
    # x is a list (or vector) of length 304
    return max(0, x[276])
def l534_261(x):
    # x is a list (or vector) of length 304
    return max(0, x[277])
def l534_262(x):
    # x is a list (or vector) of length 304
    return max(0, x[278])
def l534_263(x):
    # x is a list (or vector) of length 304
    return max(0, x[279])
def l534_264(x):
    # x is a list (or vector) of length 304
    return max(0, x[280])
def l534_265(x):
    # x is a list (or vector) of length 304
    return max(0, x[281])
def l534_266(x):
    # x is a list (or vector) of length 304
    return max(0, x[282])
def l534_267(x):
    # x is a list (or vector) of length 304
    return max(0, x[283])
def l534_268(x):
    # x is a list (or vector) of length 304
    return max(0, x[284])
def l534_269(x):
    # x is a list (or vector) of length 304
    return max(0, x[285])
def l534_270(x):
    # x is a list (or vector) of length 304
    return max(0, x[286])
def l534_271(x):
    # x is a list (or vector) of length 304
    return max(0, x[287])
def l534_272(x):
    # x is a list (or vector) of length 304
    return max(0, x[288])
def l534_273(x):
    # x is a list (or vector) of length 304
    return max(0, x[289])
def l534_274(x):
    # x is a list (or vector) of length 304
    return max(0, x[290])
def l534_275(x):
    # x is a list (or vector) of length 304
    return max(0, x[291])
def l534_276(x):
    # x is a list (or vector) of length 304
    return max(0, x[292])
def l534_277(x):
    # x is a list (or vector) of length 304
    return max(0, x[293])
def l534_278(x):
    # x is a list (or vector) of length 304
    return max(0, x[294])
def l534_279(x):
    # x is a list (or vector) of length 304
    return max(0, x[295])
def l534_280(x):
    # x is a list (or vector) of length 304
    return max(0, x[296])
def l534_281(x):
    # x is a list (or vector) of length 304
    return max(0, x[297])
def l534_282(x):
    # x is a list (or vector) of length 304
    return max(0, x[298])
def l534_283(x):
    # x is a list (or vector) of length 304
    return max(0, x[299])
def l534_284(x):
    # x is a list (or vector) of length 304
    return max(0, x[300])
def l534_285(x):
    # x is a list (or vector) of length 304
    return max(0, x[301])
def l534_286(x):
    # x is a list (or vector) of length 304
    return max(0, x[302])
def l534_287(x):
    # x is a list (or vector) of length 304
    return max(0, x[303])
def l534_(x):
    # x is a list (or vector) of length 304
    return [
        l534_0(x),
        l534_1(x),
        l534_2(x),
        l534_3(x),
        l534_4(x),
        l534_5(x),
        l534_6(x),
        l534_7(x),
        l534_8(x),
        l534_9(x),
        l534_10(x),
        l534_11(x),
        l534_12(x),
        l534_13(x),
        l534_14(x),
        l534_15(x),
        l534_16(x),
        l534_17(x),
        l534_18(x),
        l534_19(x),
        l534_20(x),
        l534_21(x),
        l534_22(x),
        l534_23(x),
        l534_24(x),
        l534_25(x),
        l534_26(x),
        l534_27(x),
        l534_28(x),
        l534_29(x),
        l534_30(x),
        l534_31(x),
        l534_32(x),
        l534_33(x),
        l534_34(x),
        l534_35(x),
        l534_36(x),
        l534_37(x),
        l534_38(x),
        l534_39(x),
        l534_40(x),
        l534_41(x),
        l534_42(x),
        l534_43(x),
        l534_44(x),
        l534_45(x),
        l534_46(x),
        l534_47(x),
        l534_48(x),
        l534_49(x),
        l534_50(x),
        l534_51(x),
        l534_52(x),
        l534_53(x),
        l534_54(x),
        l534_55(x),
        l534_56(x),
        l534_57(x),
        l534_58(x),
        l534_59(x),
        l534_60(x),
        l534_61(x),
        l534_62(x),
        l534_63(x),
        l534_64(x),
        l534_65(x),
        l534_66(x),
        l534_67(x),
        l534_68(x),
        l534_69(x),
        l534_70(x),
        l534_71(x),
        l534_72(x),
        l534_73(x),
        l534_74(x),
        l534_75(x),
        l534_76(x),
        l534_77(x),
        l534_78(x),
        l534_79(x),
        l534_80(x),
        l534_81(x),
        l534_82(x),
        l534_83(x),
        l534_84(x),
        l534_85(x),
        l534_86(x),
        l534_87(x),
        l534_88(x),
        l534_89(x),
        l534_90(x),
        l534_91(x),
        l534_92(x),
        l534_93(x),
        l534_94(x),
        l534_95(x),
        l534_96(x),
        l534_97(x),
        l534_98(x),
        l534_99(x),
        l534_100(x),
        l534_101(x),
        l534_102(x),
        l534_103(x),
        l534_104(x),
        l534_105(x),
        l534_106(x),
        l534_107(x),
        l534_108(x),
        l534_109(x),
        l534_110(x),
        l534_111(x),
        l534_112(x),
        l534_113(x),
        l534_114(x),
        l534_115(x),
        l534_116(x),
        l534_117(x),
        l534_118(x),
        l534_119(x),
        l534_120(x),
        l534_121(x),
        l534_122(x),
        l534_123(x),
        l534_124(x),
        l534_125(x),
        l534_126(x),
        l534_127(x),
        l534_128(x),
        l534_129(x),
        l534_130(x),
        l534_131(x),
        l534_132(x),
        l534_133(x),
        l534_134(x),
        l534_135(x),
        l534_136(x),
        l534_137(x),
        l534_138(x),
        l534_139(x),
        l534_140(x),
        l534_141(x),
        l534_142(x),
        l534_143(x),
        l534_144(x),
        l534_145(x),
        l534_146(x),
        l534_147(x),
        l534_148(x),
        l534_149(x),
        l534_150(x),
        l534_151(x),
        l534_152(x),
        l534_153(x),
        l534_154(x),
        l534_155(x),
        l534_156(x),
        l534_157(x),
        l534_158(x),
        l534_159(x),
        l534_160(x),
        l534_161(x),
        l534_162(x),
        l534_163(x),
        l534_164(x),
        l534_165(x),
        l534_166(x),
        l534_167(x),
        l534_168(x),
        l534_169(x),
        l534_170(x),
        l534_171(x),
        l534_172(x),
        l534_173(x),
        l534_174(x),
        l534_175(x),
        l534_176(x),
        l534_177(x),
        l534_178(x),
        l534_179(x),
        l534_180(x),
        l534_181(x),
        l534_182(x),
        l534_183(x),
        l534_184(x),
        l534_185(x),
        l534_186(x),
        l534_187(x),
        l534_188(x),
        l534_189(x),
        l534_190(x),
        l534_191(x),
        l534_192(x),
        l534_193(x),
        l534_194(x),
        l534_195(x),
        l534_196(x),
        l534_197(x),
        l534_198(x),
        l534_199(x),
        l534_200(x),
        l534_201(x),
        l534_202(x),
        l534_203(x),
        l534_204(x),
        l534_205(x),
        l534_206(x),
        l534_207(x),
        l534_208(x),
        l534_209(x),
        l534_210(x),
        l534_211(x),
        l534_212(x),
        l534_213(x),
        l534_214(x),
        l534_215(x),
        l534_216(x),
        l534_217(x),
        l534_218(x),
        l534_219(x),
        l534_220(x),
        l534_221(x),
        l534_222(x),
        l534_223(x),
        l534_224(x),
        l534_225(x),
        l534_226(x),
        l534_227(x),
        l534_228(x),
        l534_229(x),
        l534_230(x),
        l534_231(x),
        l534_232(x),
        l534_233(x),
        l534_234(x),
        l534_235(x),
        l534_236(x),
        l534_237(x),
        l534_238(x),
        l534_239(x),
        l534_240(x),
        l534_241(x),
        l534_242(x),
        l534_243(x),
        l534_244(x),
        l534_245(x),
        l534_246(x),
        l534_247(x),
        l534_248(x),
        l534_249(x),
        l534_250(x),
        l534_251(x),
        l534_252(x),
        l534_253(x),
        l534_254(x),
        l534_255(x),
        l534_256(x),
        l534_257(x),
        l534_258(x),
        l534_259(x),
        l534_260(x),
        l534_261(x),
        l534_262(x),
        l534_263(x),
        l534_264(x),
        l534_265(x),
        l534_266(x),
        l534_267(x),
        l534_268(x),
        l534_269(x),
        l534_270(x),
        l534_271(x),
        l534_272(x),
        l534_273(x),
        l534_274(x),
        l534_275(x),
        l534_276(x),
        l534_277(x),
        l534_278(x),
        l534_279(x),
        l534_280(x),
        l534_281(x),
        l534_282(x),
        l534_283(x),
        l534_284(x),
        l534_285(x),
        l534_286(x),
        l534_287(x),
    ]