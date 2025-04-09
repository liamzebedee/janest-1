import numpy as np




# Generated from reverse engineering
def l152_g(x: np.ndarray) -> np.ndarray:
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




def l152_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l152_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l152_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l152_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l152_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l152_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l152_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l152_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l152_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l152_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l152_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l152_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l152_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l152_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l152_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l152_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l152_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l152_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l152_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l152_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l152_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l152_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l152_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l152_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l152_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l152_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l152_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l152_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l152_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l152_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l152_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l152_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l152_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l152_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l152_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l152_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l152_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l152_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l152_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l152_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l152_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l152_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l152_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l152_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l152_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l152_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l152_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l152_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l152_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l152_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l152_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l152_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l152_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l152_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l152_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l152_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l152_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l152_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l152_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l152_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l152_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l152_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l152_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l152_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l152_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l152_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l152_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l152_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l152_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l152_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l152_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l152_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l152_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l152_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l152_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l152_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l152_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l152_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l152_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l152_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l152_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l152_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l152_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l152_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l152_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l152_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l152_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l152_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l152_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l152_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l152_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l152_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l152_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l152_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l152_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l152_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l152_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l152_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l152_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l152_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l152_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[100])
def l152_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[101])
def l152_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[102])
def l152_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[103])
def l152_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[104])
def l152_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[105])
def l152_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[106])
def l152_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[107])
def l152_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[108])
def l152_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[109])
def l152_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[110])
def l152_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[111])
def l152_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[112])
def l152_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[113])
def l152_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[114])
def l152_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[115])
def l152_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[116])
def l152_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[117])
def l152_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[118])
def l152_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[119])
def l152_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[120])
def l152_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[121])
def l152_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[122])
def l152_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[123])
def l152_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[124])
def l152_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[125])
def l152_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[126])
def l152_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[127])
def l152_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[128] + -2.0*x[160])
def l152_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[129] + -2.0*x[161])
def l152_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[130] + -2.0*x[162])
def l152_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[131] + -2.0*x[163])
def l152_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[132] + -2.0*x[164])
def l152_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[133] + -2.0*x[165])
def l152_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[134] + -2.0*x[166])
def l152_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[135] + -2.0*x[167])
def l152_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[136] + -2.0*x[168])
def l152_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[137] + -2.0*x[169])
def l152_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[138] + -2.0*x[170])
def l152_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[139] + -2.0*x[171])
def l152_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[140] + -2.0*x[172])
def l152_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[141] + -2.0*x[173])
def l152_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[142] + -2.0*x[174])
def l152_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[143] + -2.0*x[175])
def l152_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[144] + -2.0*x[176])
def l152_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[145] + -2.0*x[177])
def l152_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[146] + -2.0*x[178])
def l152_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[147] + -2.0*x[179])
def l152_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[148] + -2.0*x[180])
def l152_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[149] + -2.0*x[181])
def l152_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[150] + -2.0*x[182])
def l152_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[151] + -2.0*x[183])
def l152_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[152] + -2.0*x[184])
def l152_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[153] + -2.0*x[185])
def l152_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[154] + -2.0*x[186])
def l152_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[155] + -2.0*x[187])
def l152_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[156] + -2.0*x[188])
def l152_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[157] + -2.0*x[189])
def l152_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[158] + -2.0*x[190])
def l152_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[159] + -2.0*x[191])
def l152_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l152_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l152_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l152_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l152_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l152_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l152_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l152_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l152_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l152_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l152_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l152_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l152_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l152_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l152_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l152_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l152_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l152_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l152_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l152_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l152_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l152_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l152_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l152_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l152_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l152_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l152_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l152_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l152_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l152_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l152_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l152_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l152_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l152_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l152_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l152_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l152_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l152_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l152_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l152_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l152_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l152_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l152_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l152_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l152_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l152_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l152_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l152_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l152_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l152_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l152_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l152_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l152_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l152_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l152_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l152_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l152_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l152_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l152_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l152_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l152_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l152_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l152_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l152_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l152_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l152_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l152_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l152_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l152_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l152_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l152_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l152_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l152_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l152_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l152_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l152_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l152_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l152_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l152_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l152_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l152_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l152_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l152_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l152_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l152_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l152_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l152_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l152_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l152_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l152_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l152_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l152_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l152_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l152_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l152_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l152_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l152_(x):
    # x is a list (or vector) of length 288
    return [
        l152_0(x),
        l152_1(x),
        l152_2(x),
        l152_3(x),
        l152_4(x),
        l152_5(x),
        l152_6(x),
        l152_7(x),
        l152_8(x),
        l152_9(x),
        l152_10(x),
        l152_11(x),
        l152_12(x),
        l152_13(x),
        l152_14(x),
        l152_15(x),
        l152_16(x),
        l152_17(x),
        l152_18(x),
        l152_19(x),
        l152_20(x),
        l152_21(x),
        l152_22(x),
        l152_23(x),
        l152_24(x),
        l152_25(x),
        l152_26(x),
        l152_27(x),
        l152_28(x),
        l152_29(x),
        l152_30(x),
        l152_31(x),
        l152_32(x),
        l152_33(x),
        l152_34(x),
        l152_35(x),
        l152_36(x),
        l152_37(x),
        l152_38(x),
        l152_39(x),
        l152_40(x),
        l152_41(x),
        l152_42(x),
        l152_43(x),
        l152_44(x),
        l152_45(x),
        l152_46(x),
        l152_47(x),
        l152_48(x),
        l152_49(x),
        l152_50(x),
        l152_51(x),
        l152_52(x),
        l152_53(x),
        l152_54(x),
        l152_55(x),
        l152_56(x),
        l152_57(x),
        l152_58(x),
        l152_59(x),
        l152_60(x),
        l152_61(x),
        l152_62(x),
        l152_63(x),
        l152_64(x),
        l152_65(x),
        l152_66(x),
        l152_67(x),
        l152_68(x),
        l152_69(x),
        l152_70(x),
        l152_71(x),
        l152_72(x),
        l152_73(x),
        l152_74(x),
        l152_75(x),
        l152_76(x),
        l152_77(x),
        l152_78(x),
        l152_79(x),
        l152_80(x),
        l152_81(x),
        l152_82(x),
        l152_83(x),
        l152_84(x),
        l152_85(x),
        l152_86(x),
        l152_87(x),
        l152_88(x),
        l152_89(x),
        l152_90(x),
        l152_91(x),
        l152_92(x),
        l152_93(x),
        l152_94(x),
        l152_95(x),
        l152_96(x),
        l152_97(x),
        l152_98(x),
        l152_99(x),
        l152_100(x),
        l152_101(x),
        l152_102(x),
        l152_103(x),
        l152_104(x),
        l152_105(x),
        l152_106(x),
        l152_107(x),
        l152_108(x),
        l152_109(x),
        l152_110(x),
        l152_111(x),
        l152_112(x),
        l152_113(x),
        l152_114(x),
        l152_115(x),
        l152_116(x),
        l152_117(x),
        l152_118(x),
        l152_119(x),
        l152_120(x),
        l152_121(x),
        l152_122(x),
        l152_123(x),
        l152_124(x),
        l152_125(x),
        l152_126(x),
        l152_127(x),
        l152_128(x),
        l152_129(x),
        l152_130(x),
        l152_131(x),
        l152_132(x),
        l152_133(x),
        l152_134(x),
        l152_135(x),
        l152_136(x),
        l152_137(x),
        l152_138(x),
        l152_139(x),
        l152_140(x),
        l152_141(x),
        l152_142(x),
        l152_143(x),
        l152_144(x),
        l152_145(x),
        l152_146(x),
        l152_147(x),
        l152_148(x),
        l152_149(x),
        l152_150(x),
        l152_151(x),
        l152_152(x),
        l152_153(x),
        l152_154(x),
        l152_155(x),
        l152_156(x),
        l152_157(x),
        l152_158(x),
        l152_159(x),
        l152_160(x),
        l152_161(x),
        l152_162(x),
        l152_163(x),
        l152_164(x),
        l152_165(x),
        l152_166(x),
        l152_167(x),
        l152_168(x),
        l152_169(x),
        l152_170(x),
        l152_171(x),
        l152_172(x),
        l152_173(x),
        l152_174(x),
        l152_175(x),
        l152_176(x),
        l152_177(x),
        l152_178(x),
        l152_179(x),
        l152_180(x),
        l152_181(x),
        l152_182(x),
        l152_183(x),
        l152_184(x),
        l152_185(x),
        l152_186(x),
        l152_187(x),
        l152_188(x),
        l152_189(x),
        l152_190(x),
        l152_191(x),
        l152_192(x),
        l152_193(x),
        l152_194(x),
        l152_195(x),
        l152_196(x),
        l152_197(x),
        l152_198(x),
        l152_199(x),
        l152_200(x),
        l152_201(x),
        l152_202(x),
        l152_203(x),
        l152_204(x),
        l152_205(x),
        l152_206(x),
        l152_207(x),
        l152_208(x),
        l152_209(x),
        l152_210(x),
        l152_211(x),
        l152_212(x),
        l152_213(x),
        l152_214(x),
        l152_215(x),
        l152_216(x),
        l152_217(x),
        l152_218(x),
        l152_219(x),
        l152_220(x),
        l152_221(x),
        l152_222(x),
        l152_223(x),
        l152_224(x),
        l152_225(x),
        l152_226(x),
        l152_227(x),
        l152_228(x),
        l152_229(x),
        l152_230(x),
        l152_231(x),
        l152_232(x),
        l152_233(x),
        l152_234(x),
        l152_235(x),
        l152_236(x),
        l152_237(x),
        l152_238(x),
        l152_239(x),
        l152_240(x),
        l152_241(x),
        l152_242(x),
        l152_243(x),
        l152_244(x),
        l152_245(x),
        l152_246(x),
        l152_247(x),
        l152_248(x),
        l152_249(x),
        l152_250(x),
        l152_251(x),
        l152_252(x),
        l152_253(x),
        l152_254(x),
        l152_255(x),
    ]