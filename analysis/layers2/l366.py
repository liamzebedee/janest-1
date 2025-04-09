import numpy as np




# Generated from reverse engineering
def l366_g(x: np.ndarray) -> np.ndarray:
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




def l366_0(x):
    # x is a list (or vector) of length 304
    return max(0, x[0])
def l366_1(x):
    # x is a list (or vector) of length 304
    return max(0, x[1])
def l366_2(x):
    # x is a list (or vector) of length 304
    return max(0, x[2])
def l366_3(x):
    # x is a list (or vector) of length 304
    return max(0, x[3])
def l366_4(x):
    # x is a list (or vector) of length 304
    return max(0, x[4])
def l366_5(x):
    # x is a list (or vector) of length 304
    return max(0, x[5])
def l366_6(x):
    # x is a list (or vector) of length 304
    return max(0, x[6])
def l366_7(x):
    # x is a list (or vector) of length 304
    return max(0, x[7])
def l366_8(x):
    # x is a list (or vector) of length 304
    return max(0, x[8])
def l366_9(x):
    # x is a list (or vector) of length 304
    return max(0, x[9])
def l366_10(x):
    # x is a list (or vector) of length 304
    return max(0, x[10])
def l366_11(x):
    # x is a list (or vector) of length 304
    return max(0, x[11])
def l366_12(x):
    # x is a list (or vector) of length 304
    return max(0, x[12])
def l366_13(x):
    # x is a list (or vector) of length 304
    return max(0, x[13])
def l366_14(x):
    # x is a list (or vector) of length 304
    return max(0, x[14])
def l366_15(x):
    # x is a list (or vector) of length 304
    return max(0, x[15])
def l366_16(x):
    # x is a list (or vector) of length 304
    return max(0, x[16])
def l366_17(x):
    # x is a list (or vector) of length 304
    return max(0, x[17])
def l366_18(x):
    # x is a list (or vector) of length 304
    return max(0, x[18])
def l366_19(x):
    # x is a list (or vector) of length 304
    return max(0, x[19])
def l366_20(x):
    # x is a list (or vector) of length 304
    return max(0, x[20])
def l366_21(x):
    # x is a list (or vector) of length 304
    return max(0, x[21])
def l366_22(x):
    # x is a list (or vector) of length 304
    return max(0, x[22])
def l366_23(x):
    # x is a list (or vector) of length 304
    return max(0, x[23])
def l366_24(x):
    # x is a list (or vector) of length 304
    return max(0, x[24])
def l366_25(x):
    # x is a list (or vector) of length 304
    return max(0, x[25])
def l366_26(x):
    # x is a list (or vector) of length 304
    return max(0, x[26])
def l366_27(x):
    # x is a list (or vector) of length 304
    return max(0, x[27])
def l366_28(x):
    # x is a list (or vector) of length 304
    return max(0, x[28])
def l366_29(x):
    # x is a list (or vector) of length 304
    return max(0, x[29])
def l366_30(x):
    # x is a list (or vector) of length 304
    return max(0, x[30])
def l366_31(x):
    # x is a list (or vector) of length 304
    return max(0, x[31])
def l366_32(x):
    # x is a list (or vector) of length 304
    return max(0, x[32])
def l366_33(x):
    # x is a list (or vector) of length 304
    return max(0, x[33])
def l366_34(x):
    # x is a list (or vector) of length 304
    return max(0, x[34])
def l366_35(x):
    # x is a list (or vector) of length 304
    return max(0, x[35])
def l366_36(x):
    # x is a list (or vector) of length 304
    return max(0, x[36])
def l366_37(x):
    # x is a list (or vector) of length 304
    return max(0, x[37])
def l366_38(x):
    # x is a list (or vector) of length 304
    return max(0, x[38])
def l366_39(x):
    # x is a list (or vector) of length 304
    return max(0, x[39])
def l366_40(x):
    # x is a list (or vector) of length 304
    return max(0, x[40])
def l366_41(x):
    # x is a list (or vector) of length 304
    return max(0, x[41])
def l366_42(x):
    # x is a list (or vector) of length 304
    return max(0, x[42])
def l366_43(x):
    # x is a list (or vector) of length 304
    return max(0, x[43])
def l366_44(x):
    # x is a list (or vector) of length 304
    return max(0, x[44])
def l366_45(x):
    # x is a list (or vector) of length 304
    return max(0, x[45])
def l366_46(x):
    # x is a list (or vector) of length 304
    return max(0, x[46])
def l366_47(x):
    # x is a list (or vector) of length 304
    return max(0, x[47])
def l366_48(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[48] + -1.0*x[64] + 1.0)
def l366_49(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[49] + -1.0*x[65] + 1.0)
def l366_50(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[50] + -1.0*x[66] + 1.0)
def l366_51(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[51] + -1.0*x[67] + 1.0)
def l366_52(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[52] + -1.0*x[68] + 1.0)
def l366_53(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[53] + -1.0*x[69] + 1.0)
def l366_54(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[54] + -1.0*x[70] + 1.0)
def l366_55(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[55] + -1.0*x[71] + 1.0)
def l366_56(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[56] + -1.0*x[72] + 1.0)
def l366_57(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[57] + -1.0*x[73] + 1.0)
def l366_58(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[58] + -1.0*x[74] + 1.0)
def l366_59(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[59] + -1.0*x[75] + 1.0)
def l366_60(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[60] + -1.0*x[76] + 1.0)
def l366_61(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[61] + -1.0*x[77] + 1.0)
def l366_62(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[62] + -1.0*x[78] + 1.0)
def l366_63(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[63] + -1.0*x[79] + 1.0)
def l366_64(x):
    # x is a list (or vector) of length 304
    return max(0, x[96])
def l366_65(x):
    # x is a list (or vector) of length 304
    return max(0, x[97])
def l366_66(x):
    # x is a list (or vector) of length 304
    return max(0, x[98])
def l366_67(x):
    # x is a list (or vector) of length 304
    return max(0, x[99])
def l366_68(x):
    # x is a list (or vector) of length 304
    return max(0, x[100])
def l366_69(x):
    # x is a list (or vector) of length 304
    return max(0, x[101])
def l366_70(x):
    # x is a list (or vector) of length 304
    return max(0, x[102])
def l366_71(x):
    # x is a list (or vector) of length 304
    return max(0, x[103])
def l366_72(x):
    # x is a list (or vector) of length 304
    return max(0, x[104])
def l366_73(x):
    # x is a list (or vector) of length 304
    return max(0, x[105])
def l366_74(x):
    # x is a list (or vector) of length 304
    return max(0, x[106])
def l366_75(x):
    # x is a list (or vector) of length 304
    return max(0, x[107])
def l366_76(x):
    # x is a list (or vector) of length 304
    return max(0, x[108])
def l366_77(x):
    # x is a list (or vector) of length 304
    return max(0, x[109])
def l366_78(x):
    # x is a list (or vector) of length 304
    return max(0, x[110])
def l366_79(x):
    # x is a list (or vector) of length 304
    return max(0, x[111])
def l366_80(x):
    # x is a list (or vector) of length 304
    return max(0, x[80])
def l366_81(x):
    # x is a list (or vector) of length 304
    return max(0, x[81])
def l366_82(x):
    # x is a list (or vector) of length 304
    return max(0, x[82])
def l366_83(x):
    # x is a list (or vector) of length 304
    return max(0, x[83])
def l366_84(x):
    # x is a list (or vector) of length 304
    return max(0, x[84])
def l366_85(x):
    # x is a list (or vector) of length 304
    return max(0, x[85])
def l366_86(x):
    # x is a list (or vector) of length 304
    return max(0, x[86])
def l366_87(x):
    # x is a list (or vector) of length 304
    return max(0, x[87])
def l366_88(x):
    # x is a list (or vector) of length 304
    return max(0, x[88])
def l366_89(x):
    # x is a list (or vector) of length 304
    return max(0, x[89])
def l366_90(x):
    # x is a list (or vector) of length 304
    return max(0, x[90])
def l366_91(x):
    # x is a list (or vector) of length 304
    return max(0, x[91])
def l366_92(x):
    # x is a list (or vector) of length 304
    return max(0, x[92])
def l366_93(x):
    # x is a list (or vector) of length 304
    return max(0, x[93])
def l366_94(x):
    # x is a list (or vector) of length 304
    return max(0, x[94])
def l366_95(x):
    # x is a list (or vector) of length 304
    return max(0, x[95])
def l366_96(x):
    # x is a list (or vector) of length 304
    return max(0, x[112])
def l366_97(x):
    # x is a list (or vector) of length 304
    return max(0, x[113])
def l366_98(x):
    # x is a list (or vector) of length 304
    return max(0, x[114])
def l366_99(x):
    # x is a list (or vector) of length 304
    return max(0, x[115])
def l366_100(x):
    # x is a list (or vector) of length 304
    return max(0, x[116])
def l366_101(x):
    # x is a list (or vector) of length 304
    return max(0, x[117])
def l366_102(x):
    # x is a list (or vector) of length 304
    return max(0, x[118])
def l366_103(x):
    # x is a list (or vector) of length 304
    return max(0, x[119])
def l366_104(x):
    # x is a list (or vector) of length 304
    return max(0, x[120])
def l366_105(x):
    # x is a list (or vector) of length 304
    return max(0, x[121])
def l366_106(x):
    # x is a list (or vector) of length 304
    return max(0, x[122])
def l366_107(x):
    # x is a list (or vector) of length 304
    return max(0, x[123])
def l366_108(x):
    # x is a list (or vector) of length 304
    return max(0, x[124])
def l366_109(x):
    # x is a list (or vector) of length 304
    return max(0, x[125])
def l366_110(x):
    # x is a list (or vector) of length 304
    return max(0, x[126])
def l366_111(x):
    # x is a list (or vector) of length 304
    return max(0, x[127])
def l366_112(x):
    # x is a list (or vector) of length 304
    return max(0, x[128])
def l366_113(x):
    # x is a list (or vector) of length 304
    return max(0, x[129])
def l366_114(x):
    # x is a list (or vector) of length 304
    return max(0, x[130])
def l366_115(x):
    # x is a list (or vector) of length 304
    return max(0, x[131])
def l366_116(x):
    # x is a list (or vector) of length 304
    return max(0, x[132])
def l366_117(x):
    # x is a list (or vector) of length 304
    return max(0, x[133])
def l366_118(x):
    # x is a list (or vector) of length 304
    return max(0, x[134])
def l366_119(x):
    # x is a list (or vector) of length 304
    return max(0, x[135])
def l366_120(x):
    # x is a list (or vector) of length 304
    return max(0, x[136])
def l366_121(x):
    # x is a list (or vector) of length 304
    return max(0, x[137])
def l366_122(x):
    # x is a list (or vector) of length 304
    return max(0, x[138])
def l366_123(x):
    # x is a list (or vector) of length 304
    return max(0, x[139])
def l366_124(x):
    # x is a list (or vector) of length 304
    return max(0, x[140])
def l366_125(x):
    # x is a list (or vector) of length 304
    return max(0, x[141])
def l366_126(x):
    # x is a list (or vector) of length 304
    return max(0, x[142])
def l366_127(x):
    # x is a list (or vector) of length 304
    return max(0, x[143])
def l366_128(x):
    # x is a list (or vector) of length 304
    return max(0, x[144])
def l366_129(x):
    # x is a list (or vector) of length 304
    return max(0, x[145])
def l366_130(x):
    # x is a list (or vector) of length 304
    return max(0, x[146])
def l366_131(x):
    # x is a list (or vector) of length 304
    return max(0, x[147])
def l366_132(x):
    # x is a list (or vector) of length 304
    return max(0, x[148])
def l366_133(x):
    # x is a list (or vector) of length 304
    return max(0, x[149])
def l366_134(x):
    # x is a list (or vector) of length 304
    return max(0, x[150])
def l366_135(x):
    # x is a list (or vector) of length 304
    return max(0, x[151])
def l366_136(x):
    # x is a list (or vector) of length 304
    return max(0, x[152])
def l366_137(x):
    # x is a list (or vector) of length 304
    return max(0, x[153])
def l366_138(x):
    # x is a list (or vector) of length 304
    return max(0, x[154])
def l366_139(x):
    # x is a list (or vector) of length 304
    return max(0, x[155])
def l366_140(x):
    # x is a list (or vector) of length 304
    return max(0, x[156])
def l366_141(x):
    # x is a list (or vector) of length 304
    return max(0, x[157])
def l366_142(x):
    # x is a list (or vector) of length 304
    return max(0, x[158])
def l366_143(x):
    # x is a list (or vector) of length 304
    return max(0, x[159])
def l366_144(x):
    # x is a list (or vector) of length 304
    return max(0, x[160])
def l366_145(x):
    # x is a list (or vector) of length 304
    return max(0, x[161])
def l366_146(x):
    # x is a list (or vector) of length 304
    return max(0, x[162])
def l366_147(x):
    # x is a list (or vector) of length 304
    return max(0, x[163])
def l366_148(x):
    # x is a list (or vector) of length 304
    return max(0, x[164])
def l366_149(x):
    # x is a list (or vector) of length 304
    return max(0, x[165])
def l366_150(x):
    # x is a list (or vector) of length 304
    return max(0, x[166])
def l366_151(x):
    # x is a list (or vector) of length 304
    return max(0, x[167])
def l366_152(x):
    # x is a list (or vector) of length 304
    return max(0, x[168])
def l366_153(x):
    # x is a list (or vector) of length 304
    return max(0, x[169])
def l366_154(x):
    # x is a list (or vector) of length 304
    return max(0, x[170])
def l366_155(x):
    # x is a list (or vector) of length 304
    return max(0, x[171])
def l366_156(x):
    # x is a list (or vector) of length 304
    return max(0, x[172])
def l366_157(x):
    # x is a list (or vector) of length 304
    return max(0, x[173])
def l366_158(x):
    # x is a list (or vector) of length 304
    return max(0, x[174])
def l366_159(x):
    # x is a list (or vector) of length 304
    return max(0, x[175])
def l366_160(x):
    # x is a list (or vector) of length 304
    return max(0, x[176])
def l366_161(x):
    # x is a list (or vector) of length 304
    return max(0, x[177])
def l366_162(x):
    # x is a list (or vector) of length 304
    return max(0, x[178])
def l366_163(x):
    # x is a list (or vector) of length 304
    return max(0, x[179])
def l366_164(x):
    # x is a list (or vector) of length 304
    return max(0, x[180])
def l366_165(x):
    # x is a list (or vector) of length 304
    return max(0, x[181])
def l366_166(x):
    # x is a list (or vector) of length 304
    return max(0, x[182])
def l366_167(x):
    # x is a list (or vector) of length 304
    return max(0, x[183])
def l366_168(x):
    # x is a list (or vector) of length 304
    return max(0, x[184])
def l366_169(x):
    # x is a list (or vector) of length 304
    return max(0, x[185])
def l366_170(x):
    # x is a list (or vector) of length 304
    return max(0, x[186])
def l366_171(x):
    # x is a list (or vector) of length 304
    return max(0, x[187])
def l366_172(x):
    # x is a list (or vector) of length 304
    return max(0, x[188])
def l366_173(x):
    # x is a list (or vector) of length 304
    return max(0, x[189])
def l366_174(x):
    # x is a list (or vector) of length 304
    return max(0, x[190])
def l366_175(x):
    # x is a list (or vector) of length 304
    return max(0, x[191])
def l366_176(x):
    # x is a list (or vector) of length 304
    return max(0, x[192])
def l366_177(x):
    # x is a list (or vector) of length 304
    return max(0, x[193])
def l366_178(x):
    # x is a list (or vector) of length 304
    return max(0, x[194])
def l366_179(x):
    # x is a list (or vector) of length 304
    return max(0, x[195])
def l366_180(x):
    # x is a list (or vector) of length 304
    return max(0, x[196])
def l366_181(x):
    # x is a list (or vector) of length 304
    return max(0, x[197])
def l366_182(x):
    # x is a list (or vector) of length 304
    return max(0, x[198])
def l366_183(x):
    # x is a list (or vector) of length 304
    return max(0, x[199])
def l366_184(x):
    # x is a list (or vector) of length 304
    return max(0, x[200])
def l366_185(x):
    # x is a list (or vector) of length 304
    return max(0, x[201])
def l366_186(x):
    # x is a list (or vector) of length 304
    return max(0, x[202])
def l366_187(x):
    # x is a list (or vector) of length 304
    return max(0, x[203])
def l366_188(x):
    # x is a list (or vector) of length 304
    return max(0, x[204])
def l366_189(x):
    # x is a list (or vector) of length 304
    return max(0, x[205])
def l366_190(x):
    # x is a list (or vector) of length 304
    return max(0, x[206])
def l366_191(x):
    # x is a list (or vector) of length 304
    return max(0, x[207])
def l366_192(x):
    # x is a list (or vector) of length 304
    return max(0, x[208])
def l366_193(x):
    # x is a list (or vector) of length 304
    return max(0, x[209])
def l366_194(x):
    # x is a list (or vector) of length 304
    return max(0, x[210])
def l366_195(x):
    # x is a list (or vector) of length 304
    return max(0, x[211])
def l366_196(x):
    # x is a list (or vector) of length 304
    return max(0, x[212])
def l366_197(x):
    # x is a list (or vector) of length 304
    return max(0, x[213])
def l366_198(x):
    # x is a list (or vector) of length 304
    return max(0, x[214])
def l366_199(x):
    # x is a list (or vector) of length 304
    return max(0, x[215])
def l366_200(x):
    # x is a list (or vector) of length 304
    return max(0, x[216])
def l366_201(x):
    # x is a list (or vector) of length 304
    return max(0, x[217])
def l366_202(x):
    # x is a list (or vector) of length 304
    return max(0, x[218])
def l366_203(x):
    # x is a list (or vector) of length 304
    return max(0, x[219])
def l366_204(x):
    # x is a list (or vector) of length 304
    return max(0, x[220])
def l366_205(x):
    # x is a list (or vector) of length 304
    return max(0, x[221])
def l366_206(x):
    # x is a list (or vector) of length 304
    return max(0, x[222])
def l366_207(x):
    # x is a list (or vector) of length 304
    return max(0, x[223])
def l366_208(x):
    # x is a list (or vector) of length 304
    return max(0, x[224])
def l366_209(x):
    # x is a list (or vector) of length 304
    return max(0, x[225])
def l366_210(x):
    # x is a list (or vector) of length 304
    return max(0, x[226])
def l366_211(x):
    # x is a list (or vector) of length 304
    return max(0, x[227])
def l366_212(x):
    # x is a list (or vector) of length 304
    return max(0, x[228])
def l366_213(x):
    # x is a list (or vector) of length 304
    return max(0, x[229])
def l366_214(x):
    # x is a list (or vector) of length 304
    return max(0, x[230])
def l366_215(x):
    # x is a list (or vector) of length 304
    return max(0, x[231])
def l366_216(x):
    # x is a list (or vector) of length 304
    return max(0, x[232])
def l366_217(x):
    # x is a list (or vector) of length 304
    return max(0, x[233])
def l366_218(x):
    # x is a list (or vector) of length 304
    return max(0, x[234])
def l366_219(x):
    # x is a list (or vector) of length 304
    return max(0, x[235])
def l366_220(x):
    # x is a list (or vector) of length 304
    return max(0, x[236])
def l366_221(x):
    # x is a list (or vector) of length 304
    return max(0, x[237])
def l366_222(x):
    # x is a list (or vector) of length 304
    return max(0, x[238])
def l366_223(x):
    # x is a list (or vector) of length 304
    return max(0, x[239])
def l366_224(x):
    # x is a list (or vector) of length 304
    return max(0, x[240])
def l366_225(x):
    # x is a list (or vector) of length 304
    return max(0, x[241])
def l366_226(x):
    # x is a list (or vector) of length 304
    return max(0, x[242])
def l366_227(x):
    # x is a list (or vector) of length 304
    return max(0, x[243])
def l366_228(x):
    # x is a list (or vector) of length 304
    return max(0, x[244])
def l366_229(x):
    # x is a list (or vector) of length 304
    return max(0, x[245])
def l366_230(x):
    # x is a list (or vector) of length 304
    return max(0, x[246])
def l366_231(x):
    # x is a list (or vector) of length 304
    return max(0, x[247])
def l366_232(x):
    # x is a list (or vector) of length 304
    return max(0, x[248])
def l366_233(x):
    # x is a list (or vector) of length 304
    return max(0, x[249])
def l366_234(x):
    # x is a list (or vector) of length 304
    return max(0, x[250])
def l366_235(x):
    # x is a list (or vector) of length 304
    return max(0, x[251])
def l366_236(x):
    # x is a list (or vector) of length 304
    return max(0, x[252])
def l366_237(x):
    # x is a list (or vector) of length 304
    return max(0, x[253])
def l366_238(x):
    # x is a list (or vector) of length 304
    return max(0, x[254])
def l366_239(x):
    # x is a list (or vector) of length 304
    return max(0, x[255])
def l366_240(x):
    # x is a list (or vector) of length 304
    return max(0, x[256])
def l366_241(x):
    # x is a list (or vector) of length 304
    return max(0, x[257])
def l366_242(x):
    # x is a list (or vector) of length 304
    return max(0, x[258])
def l366_243(x):
    # x is a list (or vector) of length 304
    return max(0, x[259])
def l366_244(x):
    # x is a list (or vector) of length 304
    return max(0, x[260])
def l366_245(x):
    # x is a list (or vector) of length 304
    return max(0, x[261])
def l366_246(x):
    # x is a list (or vector) of length 304
    return max(0, x[262])
def l366_247(x):
    # x is a list (or vector) of length 304
    return max(0, x[263])
def l366_248(x):
    # x is a list (or vector) of length 304
    return max(0, x[264])
def l366_249(x):
    # x is a list (or vector) of length 304
    return max(0, x[265])
def l366_250(x):
    # x is a list (or vector) of length 304
    return max(0, x[266])
def l366_251(x):
    # x is a list (or vector) of length 304
    return max(0, x[267])
def l366_252(x):
    # x is a list (or vector) of length 304
    return max(0, x[268])
def l366_253(x):
    # x is a list (or vector) of length 304
    return max(0, x[269])
def l366_254(x):
    # x is a list (or vector) of length 304
    return max(0, x[270])
def l366_255(x):
    # x is a list (or vector) of length 304
    return max(0, x[271])
def l366_256(x):
    # x is a list (or vector) of length 304
    return max(0, x[272])
def l366_257(x):
    # x is a list (or vector) of length 304
    return max(0, x[273])
def l366_258(x):
    # x is a list (or vector) of length 304
    return max(0, x[274])
def l366_259(x):
    # x is a list (or vector) of length 304
    return max(0, x[275])
def l366_260(x):
    # x is a list (or vector) of length 304
    return max(0, x[276])
def l366_261(x):
    # x is a list (or vector) of length 304
    return max(0, x[277])
def l366_262(x):
    # x is a list (or vector) of length 304
    return max(0, x[278])
def l366_263(x):
    # x is a list (or vector) of length 304
    return max(0, x[279])
def l366_264(x):
    # x is a list (or vector) of length 304
    return max(0, x[280])
def l366_265(x):
    # x is a list (or vector) of length 304
    return max(0, x[281])
def l366_266(x):
    # x is a list (or vector) of length 304
    return max(0, x[282])
def l366_267(x):
    # x is a list (or vector) of length 304
    return max(0, x[283])
def l366_268(x):
    # x is a list (or vector) of length 304
    return max(0, x[284])
def l366_269(x):
    # x is a list (or vector) of length 304
    return max(0, x[285])
def l366_270(x):
    # x is a list (or vector) of length 304
    return max(0, x[286])
def l366_271(x):
    # x is a list (or vector) of length 304
    return max(0, x[287])
def l366_272(x):
    # x is a list (or vector) of length 304
    return max(0, x[288])
def l366_273(x):
    # x is a list (or vector) of length 304
    return max(0, x[289])
def l366_274(x):
    # x is a list (or vector) of length 304
    return max(0, x[290])
def l366_275(x):
    # x is a list (or vector) of length 304
    return max(0, x[291])
def l366_276(x):
    # x is a list (or vector) of length 304
    return max(0, x[292])
def l366_277(x):
    # x is a list (or vector) of length 304
    return max(0, x[293])
def l366_278(x):
    # x is a list (or vector) of length 304
    return max(0, x[294])
def l366_279(x):
    # x is a list (or vector) of length 304
    return max(0, x[295])
def l366_280(x):
    # x is a list (or vector) of length 304
    return max(0, x[296])
def l366_281(x):
    # x is a list (or vector) of length 304
    return max(0, x[297])
def l366_282(x):
    # x is a list (or vector) of length 304
    return max(0, x[298])
def l366_283(x):
    # x is a list (or vector) of length 304
    return max(0, x[299])
def l366_284(x):
    # x is a list (or vector) of length 304
    return max(0, x[300])
def l366_285(x):
    # x is a list (or vector) of length 304
    return max(0, x[301])
def l366_286(x):
    # x is a list (or vector) of length 304
    return max(0, x[302])
def l366_287(x):
    # x is a list (or vector) of length 304
    return max(0, x[303])
def l366_(x):
    # x is a list (or vector) of length 304
    return [
        l366_0(x),
        l366_1(x),
        l366_2(x),
        l366_3(x),
        l366_4(x),
        l366_5(x),
        l366_6(x),
        l366_7(x),
        l366_8(x),
        l366_9(x),
        l366_10(x),
        l366_11(x),
        l366_12(x),
        l366_13(x),
        l366_14(x),
        l366_15(x),
        l366_16(x),
        l366_17(x),
        l366_18(x),
        l366_19(x),
        l366_20(x),
        l366_21(x),
        l366_22(x),
        l366_23(x),
        l366_24(x),
        l366_25(x),
        l366_26(x),
        l366_27(x),
        l366_28(x),
        l366_29(x),
        l366_30(x),
        l366_31(x),
        l366_32(x),
        l366_33(x),
        l366_34(x),
        l366_35(x),
        l366_36(x),
        l366_37(x),
        l366_38(x),
        l366_39(x),
        l366_40(x),
        l366_41(x),
        l366_42(x),
        l366_43(x),
        l366_44(x),
        l366_45(x),
        l366_46(x),
        l366_47(x),
        l366_48(x),
        l366_49(x),
        l366_50(x),
        l366_51(x),
        l366_52(x),
        l366_53(x),
        l366_54(x),
        l366_55(x),
        l366_56(x),
        l366_57(x),
        l366_58(x),
        l366_59(x),
        l366_60(x),
        l366_61(x),
        l366_62(x),
        l366_63(x),
        l366_64(x),
        l366_65(x),
        l366_66(x),
        l366_67(x),
        l366_68(x),
        l366_69(x),
        l366_70(x),
        l366_71(x),
        l366_72(x),
        l366_73(x),
        l366_74(x),
        l366_75(x),
        l366_76(x),
        l366_77(x),
        l366_78(x),
        l366_79(x),
        l366_80(x),
        l366_81(x),
        l366_82(x),
        l366_83(x),
        l366_84(x),
        l366_85(x),
        l366_86(x),
        l366_87(x),
        l366_88(x),
        l366_89(x),
        l366_90(x),
        l366_91(x),
        l366_92(x),
        l366_93(x),
        l366_94(x),
        l366_95(x),
        l366_96(x),
        l366_97(x),
        l366_98(x),
        l366_99(x),
        l366_100(x),
        l366_101(x),
        l366_102(x),
        l366_103(x),
        l366_104(x),
        l366_105(x),
        l366_106(x),
        l366_107(x),
        l366_108(x),
        l366_109(x),
        l366_110(x),
        l366_111(x),
        l366_112(x),
        l366_113(x),
        l366_114(x),
        l366_115(x),
        l366_116(x),
        l366_117(x),
        l366_118(x),
        l366_119(x),
        l366_120(x),
        l366_121(x),
        l366_122(x),
        l366_123(x),
        l366_124(x),
        l366_125(x),
        l366_126(x),
        l366_127(x),
        l366_128(x),
        l366_129(x),
        l366_130(x),
        l366_131(x),
        l366_132(x),
        l366_133(x),
        l366_134(x),
        l366_135(x),
        l366_136(x),
        l366_137(x),
        l366_138(x),
        l366_139(x),
        l366_140(x),
        l366_141(x),
        l366_142(x),
        l366_143(x),
        l366_144(x),
        l366_145(x),
        l366_146(x),
        l366_147(x),
        l366_148(x),
        l366_149(x),
        l366_150(x),
        l366_151(x),
        l366_152(x),
        l366_153(x),
        l366_154(x),
        l366_155(x),
        l366_156(x),
        l366_157(x),
        l366_158(x),
        l366_159(x),
        l366_160(x),
        l366_161(x),
        l366_162(x),
        l366_163(x),
        l366_164(x),
        l366_165(x),
        l366_166(x),
        l366_167(x),
        l366_168(x),
        l366_169(x),
        l366_170(x),
        l366_171(x),
        l366_172(x),
        l366_173(x),
        l366_174(x),
        l366_175(x),
        l366_176(x),
        l366_177(x),
        l366_178(x),
        l366_179(x),
        l366_180(x),
        l366_181(x),
        l366_182(x),
        l366_183(x),
        l366_184(x),
        l366_185(x),
        l366_186(x),
        l366_187(x),
        l366_188(x),
        l366_189(x),
        l366_190(x),
        l366_191(x),
        l366_192(x),
        l366_193(x),
        l366_194(x),
        l366_195(x),
        l366_196(x),
        l366_197(x),
        l366_198(x),
        l366_199(x),
        l366_200(x),
        l366_201(x),
        l366_202(x),
        l366_203(x),
        l366_204(x),
        l366_205(x),
        l366_206(x),
        l366_207(x),
        l366_208(x),
        l366_209(x),
        l366_210(x),
        l366_211(x),
        l366_212(x),
        l366_213(x),
        l366_214(x),
        l366_215(x),
        l366_216(x),
        l366_217(x),
        l366_218(x),
        l366_219(x),
        l366_220(x),
        l366_221(x),
        l366_222(x),
        l366_223(x),
        l366_224(x),
        l366_225(x),
        l366_226(x),
        l366_227(x),
        l366_228(x),
        l366_229(x),
        l366_230(x),
        l366_231(x),
        l366_232(x),
        l366_233(x),
        l366_234(x),
        l366_235(x),
        l366_236(x),
        l366_237(x),
        l366_238(x),
        l366_239(x),
        l366_240(x),
        l366_241(x),
        l366_242(x),
        l366_243(x),
        l366_244(x),
        l366_245(x),
        l366_246(x),
        l366_247(x),
        l366_248(x),
        l366_249(x),
        l366_250(x),
        l366_251(x),
        l366_252(x),
        l366_253(x),
        l366_254(x),
        l366_255(x),
        l366_256(x),
        l366_257(x),
        l366_258(x),
        l366_259(x),
        l366_260(x),
        l366_261(x),
        l366_262(x),
        l366_263(x),
        l366_264(x),
        l366_265(x),
        l366_266(x),
        l366_267(x),
        l366_268(x),
        l366_269(x),
        l366_270(x),
        l366_271(x),
        l366_272(x),
        l366_273(x),
        l366_274(x),
        l366_275(x),
        l366_276(x),
        l366_277(x),
        l366_278(x),
        l366_279(x),
        l366_280(x),
        l366_281(x),
        l366_282(x),
        l366_283(x),
        l366_284(x),
        l366_285(x),
        l366_286(x),
        l366_287(x),
    ]