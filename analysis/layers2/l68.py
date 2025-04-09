import numpy as np




# Generated from reverse engineering
def l68_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 256
    out = np.empty(256, dtype=np.float32)
    
    # for i in range(0, 128):
    for i in range(0, 128):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 160):
    for i in range(0, 32):
        s = x[128 + i] + -2.0 * x[i + 160]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 256):
    for i in range(0, 96):
        s = x[192 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l68_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l68_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l68_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l68_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l68_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l68_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l68_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l68_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l68_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l68_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l68_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l68_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l68_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l68_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l68_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l68_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l68_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l68_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l68_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l68_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l68_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l68_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l68_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l68_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l68_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l68_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l68_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l68_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l68_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l68_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l68_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l68_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l68_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l68_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l68_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l68_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l68_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l68_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l68_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l68_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l68_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l68_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l68_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l68_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l68_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l68_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l68_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l68_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l68_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l68_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l68_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l68_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l68_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l68_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l68_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l68_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l68_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l68_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l68_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l68_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l68_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l68_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l68_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l68_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l68_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l68_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l68_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l68_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l68_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l68_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l68_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l68_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l68_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l68_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l68_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l68_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l68_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l68_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l68_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l68_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l68_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l68_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l68_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l68_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l68_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l68_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l68_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l68_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l68_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l68_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l68_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l68_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l68_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l68_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l68_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l68_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l68_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l68_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l68_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l68_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l68_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[100])
def l68_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[101])
def l68_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[102])
def l68_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[103])
def l68_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[104])
def l68_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[105])
def l68_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[106])
def l68_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[107])
def l68_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[108])
def l68_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[109])
def l68_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[110])
def l68_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[111])
def l68_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[112])
def l68_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[113])
def l68_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[114])
def l68_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[115])
def l68_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[116])
def l68_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[117])
def l68_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[118])
def l68_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[119])
def l68_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[120])
def l68_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[121])
def l68_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[122])
def l68_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[123])
def l68_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[124])
def l68_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[125])
def l68_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[126])
def l68_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[127])
def l68_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[128] + -2.0*x[160])
def l68_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[129] + -2.0*x[161])
def l68_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[130] + -2.0*x[162])
def l68_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[131] + -2.0*x[163])
def l68_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[132] + -2.0*x[164])
def l68_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[133] + -2.0*x[165])
def l68_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[134] + -2.0*x[166])
def l68_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[135] + -2.0*x[167])
def l68_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[136] + -2.0*x[168])
def l68_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[137] + -2.0*x[169])
def l68_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[138] + -2.0*x[170])
def l68_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[139] + -2.0*x[171])
def l68_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[140] + -2.0*x[172])
def l68_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[141] + -2.0*x[173])
def l68_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[142] + -2.0*x[174])
def l68_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[143] + -2.0*x[175])
def l68_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[144] + -2.0*x[176])
def l68_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[145] + -2.0*x[177])
def l68_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[146] + -2.0*x[178])
def l68_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[147] + -2.0*x[179])
def l68_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[148] + -2.0*x[180])
def l68_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[149] + -2.0*x[181])
def l68_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[150] + -2.0*x[182])
def l68_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[151] + -2.0*x[183])
def l68_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[152] + -2.0*x[184])
def l68_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[153] + -2.0*x[185])
def l68_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[154] + -2.0*x[186])
def l68_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[155] + -2.0*x[187])
def l68_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[156] + -2.0*x[188])
def l68_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[157] + -2.0*x[189])
def l68_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[158] + -2.0*x[190])
def l68_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[159] + -2.0*x[191])
def l68_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l68_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l68_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l68_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l68_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l68_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l68_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l68_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l68_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l68_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l68_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l68_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l68_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l68_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l68_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l68_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l68_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l68_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l68_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l68_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l68_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l68_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l68_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l68_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l68_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l68_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l68_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l68_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l68_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l68_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l68_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l68_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l68_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l68_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l68_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l68_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l68_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l68_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l68_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l68_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l68_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l68_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l68_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l68_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l68_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l68_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l68_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l68_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l68_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l68_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l68_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l68_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l68_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l68_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l68_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l68_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l68_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l68_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l68_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l68_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l68_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l68_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l68_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l68_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l68_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l68_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l68_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l68_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l68_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l68_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l68_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l68_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l68_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l68_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l68_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l68_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l68_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l68_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l68_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l68_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l68_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l68_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l68_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l68_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l68_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l68_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l68_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l68_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l68_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l68_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l68_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l68_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l68_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l68_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l68_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l68_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l68_(x):
    # x is a list (or vector) of length 288
    return [
        l68_0(x),
        l68_1(x),
        l68_2(x),
        l68_3(x),
        l68_4(x),
        l68_5(x),
        l68_6(x),
        l68_7(x),
        l68_8(x),
        l68_9(x),
        l68_10(x),
        l68_11(x),
        l68_12(x),
        l68_13(x),
        l68_14(x),
        l68_15(x),
        l68_16(x),
        l68_17(x),
        l68_18(x),
        l68_19(x),
        l68_20(x),
        l68_21(x),
        l68_22(x),
        l68_23(x),
        l68_24(x),
        l68_25(x),
        l68_26(x),
        l68_27(x),
        l68_28(x),
        l68_29(x),
        l68_30(x),
        l68_31(x),
        l68_32(x),
        l68_33(x),
        l68_34(x),
        l68_35(x),
        l68_36(x),
        l68_37(x),
        l68_38(x),
        l68_39(x),
        l68_40(x),
        l68_41(x),
        l68_42(x),
        l68_43(x),
        l68_44(x),
        l68_45(x),
        l68_46(x),
        l68_47(x),
        l68_48(x),
        l68_49(x),
        l68_50(x),
        l68_51(x),
        l68_52(x),
        l68_53(x),
        l68_54(x),
        l68_55(x),
        l68_56(x),
        l68_57(x),
        l68_58(x),
        l68_59(x),
        l68_60(x),
        l68_61(x),
        l68_62(x),
        l68_63(x),
        l68_64(x),
        l68_65(x),
        l68_66(x),
        l68_67(x),
        l68_68(x),
        l68_69(x),
        l68_70(x),
        l68_71(x),
        l68_72(x),
        l68_73(x),
        l68_74(x),
        l68_75(x),
        l68_76(x),
        l68_77(x),
        l68_78(x),
        l68_79(x),
        l68_80(x),
        l68_81(x),
        l68_82(x),
        l68_83(x),
        l68_84(x),
        l68_85(x),
        l68_86(x),
        l68_87(x),
        l68_88(x),
        l68_89(x),
        l68_90(x),
        l68_91(x),
        l68_92(x),
        l68_93(x),
        l68_94(x),
        l68_95(x),
        l68_96(x),
        l68_97(x),
        l68_98(x),
        l68_99(x),
        l68_100(x),
        l68_101(x),
        l68_102(x),
        l68_103(x),
        l68_104(x),
        l68_105(x),
        l68_106(x),
        l68_107(x),
        l68_108(x),
        l68_109(x),
        l68_110(x),
        l68_111(x),
        l68_112(x),
        l68_113(x),
        l68_114(x),
        l68_115(x),
        l68_116(x),
        l68_117(x),
        l68_118(x),
        l68_119(x),
        l68_120(x),
        l68_121(x),
        l68_122(x),
        l68_123(x),
        l68_124(x),
        l68_125(x),
        l68_126(x),
        l68_127(x),
        l68_128(x),
        l68_129(x),
        l68_130(x),
        l68_131(x),
        l68_132(x),
        l68_133(x),
        l68_134(x),
        l68_135(x),
        l68_136(x),
        l68_137(x),
        l68_138(x),
        l68_139(x),
        l68_140(x),
        l68_141(x),
        l68_142(x),
        l68_143(x),
        l68_144(x),
        l68_145(x),
        l68_146(x),
        l68_147(x),
        l68_148(x),
        l68_149(x),
        l68_150(x),
        l68_151(x),
        l68_152(x),
        l68_153(x),
        l68_154(x),
        l68_155(x),
        l68_156(x),
        l68_157(x),
        l68_158(x),
        l68_159(x),
        l68_160(x),
        l68_161(x),
        l68_162(x),
        l68_163(x),
        l68_164(x),
        l68_165(x),
        l68_166(x),
        l68_167(x),
        l68_168(x),
        l68_169(x),
        l68_170(x),
        l68_171(x),
        l68_172(x),
        l68_173(x),
        l68_174(x),
        l68_175(x),
        l68_176(x),
        l68_177(x),
        l68_178(x),
        l68_179(x),
        l68_180(x),
        l68_181(x),
        l68_182(x),
        l68_183(x),
        l68_184(x),
        l68_185(x),
        l68_186(x),
        l68_187(x),
        l68_188(x),
        l68_189(x),
        l68_190(x),
        l68_191(x),
        l68_192(x),
        l68_193(x),
        l68_194(x),
        l68_195(x),
        l68_196(x),
        l68_197(x),
        l68_198(x),
        l68_199(x),
        l68_200(x),
        l68_201(x),
        l68_202(x),
        l68_203(x),
        l68_204(x),
        l68_205(x),
        l68_206(x),
        l68_207(x),
        l68_208(x),
        l68_209(x),
        l68_210(x),
        l68_211(x),
        l68_212(x),
        l68_213(x),
        l68_214(x),
        l68_215(x),
        l68_216(x),
        l68_217(x),
        l68_218(x),
        l68_219(x),
        l68_220(x),
        l68_221(x),
        l68_222(x),
        l68_223(x),
        l68_224(x),
        l68_225(x),
        l68_226(x),
        l68_227(x),
        l68_228(x),
        l68_229(x),
        l68_230(x),
        l68_231(x),
        l68_232(x),
        l68_233(x),
        l68_234(x),
        l68_235(x),
        l68_236(x),
        l68_237(x),
        l68_238(x),
        l68_239(x),
        l68_240(x),
        l68_241(x),
        l68_242(x),
        l68_243(x),
        l68_244(x),
        l68_245(x),
        l68_246(x),
        l68_247(x),
        l68_248(x),
        l68_249(x),
        l68_250(x),
        l68_251(x),
        l68_252(x),
        l68_253(x),
        l68_254(x),
        l68_255(x),
    ]