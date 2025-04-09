import numpy as np




# Generated from reverse engineering
def l426_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 256
    out = np.empty(256, dtype=np.float32)
    
    # for i in range(0, 96):
    for i in range(0, 96):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 97):
    for i in range(0, 1):
        s = x[160 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(97, 113):
    for i in range(0, 16):
        s = x[96 + i] + x[161 + i]
        out[97 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x7fff (len=15)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(113, 128):
    for i in range(0, 15):
        s = x[177 + i] + -1 * x[112 + i]
        s += biases[i]
        out[113 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0]
    # for i in range(128, 129):
    for i in range(0, 1):
        s = x[160 + i]
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(129, 145):
    for i in range(0, 16):
        s = x[96 + i] + x[161 + i]
        s += biases[i]
        out[129 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(145, 160):
    for i in range(0, 15):
        s = x[177 + i] + -1 * x[112 + i]
        out[145 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 256):
    for i in range(0, 96):
        s = x[192 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l426_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l426_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l426_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l426_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l426_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l426_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l426_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l426_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l426_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l426_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l426_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l426_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l426_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l426_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l426_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l426_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l426_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l426_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l426_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l426_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l426_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l426_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l426_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l426_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l426_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l426_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l426_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l426_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l426_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l426_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l426_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l426_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l426_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l426_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l426_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l426_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l426_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l426_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l426_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l426_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l426_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l426_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l426_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l426_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l426_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l426_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l426_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l426_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l426_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l426_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l426_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l426_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l426_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l426_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l426_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l426_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l426_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l426_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l426_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l426_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l426_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l426_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l426_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l426_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l426_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l426_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l426_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l426_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l426_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l426_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l426_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l426_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l426_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l426_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l426_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l426_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l426_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l426_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l426_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l426_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l426_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l426_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l426_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l426_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l426_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l426_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l426_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l426_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l426_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l426_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l426_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l426_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l426_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l426_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l426_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l426_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l426_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l426_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + x[161])
def l426_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + x[162])
def l426_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + x[163])
def l426_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + x[164])
def l426_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + x[165])
def l426_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + x[166])
def l426_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + x[167])
def l426_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + x[168])
def l426_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + x[169])
def l426_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + x[170])
def l426_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + x[171])
def l426_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + x[172])
def l426_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + x[173])
def l426_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + x[174])
def l426_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + x[175])
def l426_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + x[176])
def l426_113(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + x[177] + 1.0)
def l426_114(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + x[178] + 1.0)
def l426_115(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + x[179] + 1.0)
def l426_116(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + x[180] + 1.0)
def l426_117(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + x[181] + 1.0)
def l426_118(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + x[182] + 1.0)
def l426_119(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + x[183] + 1.0)
def l426_120(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + x[184] + 1.0)
def l426_121(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + x[185] + 1.0)
def l426_122(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + x[186] + 1.0)
def l426_123(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + x[187] + 1.0)
def l426_124(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + x[188] + 1.0)
def l426_125(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + x[189] + 1.0)
def l426_126(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + x[190] + 1.0)
def l426_127(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[126] + x[191] + 1.0)
def l426_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[160] + -1.0)
def l426_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + x[161] + -1.0)
def l426_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + x[162] + -1.0)
def l426_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + x[163] + -1.0)
def l426_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + x[164] + -1.0)
def l426_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + x[165] + -1.0)
def l426_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + x[166] + -1.0)
def l426_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + x[167] + -1.0)
def l426_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + x[168] + -1.0)
def l426_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + x[169] + -1.0)
def l426_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + x[170] + -1.0)
def l426_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + x[171] + -1.0)
def l426_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + x[172] + -1.0)
def l426_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + x[173] + -1.0)
def l426_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + x[174] + -1.0)
def l426_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + x[175] + -1.0)
def l426_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + x[176] + -1.0)
def l426_145(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + x[177])
def l426_146(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + x[178])
def l426_147(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + x[179])
def l426_148(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + x[180])
def l426_149(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + x[181])
def l426_150(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + x[182])
def l426_151(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + x[183])
def l426_152(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + x[184])
def l426_153(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + x[185])
def l426_154(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + x[186])
def l426_155(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + x[187])
def l426_156(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + x[188])
def l426_157(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + x[189])
def l426_158(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + x[190])
def l426_159(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[126] + x[191])
def l426_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l426_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l426_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l426_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l426_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l426_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l426_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l426_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l426_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l426_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l426_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l426_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l426_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l426_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l426_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l426_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l426_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l426_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l426_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l426_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l426_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l426_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l426_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l426_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l426_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l426_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l426_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l426_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l426_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l426_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l426_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l426_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l426_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l426_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l426_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l426_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l426_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l426_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l426_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l426_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l426_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l426_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l426_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l426_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l426_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l426_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l426_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l426_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l426_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l426_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l426_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l426_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l426_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l426_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l426_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l426_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l426_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l426_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l426_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l426_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l426_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l426_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l426_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l426_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l426_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l426_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l426_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l426_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l426_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l426_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l426_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l426_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l426_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l426_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l426_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l426_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l426_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l426_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l426_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l426_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l426_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l426_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l426_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l426_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l426_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l426_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l426_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l426_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l426_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l426_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l426_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l426_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l426_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l426_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l426_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l426_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l426_(x):
    # x is a list (or vector) of length 288
    return [
        l426_0(x),
        l426_1(x),
        l426_2(x),
        l426_3(x),
        l426_4(x),
        l426_5(x),
        l426_6(x),
        l426_7(x),
        l426_8(x),
        l426_9(x),
        l426_10(x),
        l426_11(x),
        l426_12(x),
        l426_13(x),
        l426_14(x),
        l426_15(x),
        l426_16(x),
        l426_17(x),
        l426_18(x),
        l426_19(x),
        l426_20(x),
        l426_21(x),
        l426_22(x),
        l426_23(x),
        l426_24(x),
        l426_25(x),
        l426_26(x),
        l426_27(x),
        l426_28(x),
        l426_29(x),
        l426_30(x),
        l426_31(x),
        l426_32(x),
        l426_33(x),
        l426_34(x),
        l426_35(x),
        l426_36(x),
        l426_37(x),
        l426_38(x),
        l426_39(x),
        l426_40(x),
        l426_41(x),
        l426_42(x),
        l426_43(x),
        l426_44(x),
        l426_45(x),
        l426_46(x),
        l426_47(x),
        l426_48(x),
        l426_49(x),
        l426_50(x),
        l426_51(x),
        l426_52(x),
        l426_53(x),
        l426_54(x),
        l426_55(x),
        l426_56(x),
        l426_57(x),
        l426_58(x),
        l426_59(x),
        l426_60(x),
        l426_61(x),
        l426_62(x),
        l426_63(x),
        l426_64(x),
        l426_65(x),
        l426_66(x),
        l426_67(x),
        l426_68(x),
        l426_69(x),
        l426_70(x),
        l426_71(x),
        l426_72(x),
        l426_73(x),
        l426_74(x),
        l426_75(x),
        l426_76(x),
        l426_77(x),
        l426_78(x),
        l426_79(x),
        l426_80(x),
        l426_81(x),
        l426_82(x),
        l426_83(x),
        l426_84(x),
        l426_85(x),
        l426_86(x),
        l426_87(x),
        l426_88(x),
        l426_89(x),
        l426_90(x),
        l426_91(x),
        l426_92(x),
        l426_93(x),
        l426_94(x),
        l426_95(x),
        l426_96(x),
        l426_97(x),
        l426_98(x),
        l426_99(x),
        l426_100(x),
        l426_101(x),
        l426_102(x),
        l426_103(x),
        l426_104(x),
        l426_105(x),
        l426_106(x),
        l426_107(x),
        l426_108(x),
        l426_109(x),
        l426_110(x),
        l426_111(x),
        l426_112(x),
        l426_113(x),
        l426_114(x),
        l426_115(x),
        l426_116(x),
        l426_117(x),
        l426_118(x),
        l426_119(x),
        l426_120(x),
        l426_121(x),
        l426_122(x),
        l426_123(x),
        l426_124(x),
        l426_125(x),
        l426_126(x),
        l426_127(x),
        l426_128(x),
        l426_129(x),
        l426_130(x),
        l426_131(x),
        l426_132(x),
        l426_133(x),
        l426_134(x),
        l426_135(x),
        l426_136(x),
        l426_137(x),
        l426_138(x),
        l426_139(x),
        l426_140(x),
        l426_141(x),
        l426_142(x),
        l426_143(x),
        l426_144(x),
        l426_145(x),
        l426_146(x),
        l426_147(x),
        l426_148(x),
        l426_149(x),
        l426_150(x),
        l426_151(x),
        l426_152(x),
        l426_153(x),
        l426_154(x),
        l426_155(x),
        l426_156(x),
        l426_157(x),
        l426_158(x),
        l426_159(x),
        l426_160(x),
        l426_161(x),
        l426_162(x),
        l426_163(x),
        l426_164(x),
        l426_165(x),
        l426_166(x),
        l426_167(x),
        l426_168(x),
        l426_169(x),
        l426_170(x),
        l426_171(x),
        l426_172(x),
        l426_173(x),
        l426_174(x),
        l426_175(x),
        l426_176(x),
        l426_177(x),
        l426_178(x),
        l426_179(x),
        l426_180(x),
        l426_181(x),
        l426_182(x),
        l426_183(x),
        l426_184(x),
        l426_185(x),
        l426_186(x),
        l426_187(x),
        l426_188(x),
        l426_189(x),
        l426_190(x),
        l426_191(x),
        l426_192(x),
        l426_193(x),
        l426_194(x),
        l426_195(x),
        l426_196(x),
        l426_197(x),
        l426_198(x),
        l426_199(x),
        l426_200(x),
        l426_201(x),
        l426_202(x),
        l426_203(x),
        l426_204(x),
        l426_205(x),
        l426_206(x),
        l426_207(x),
        l426_208(x),
        l426_209(x),
        l426_210(x),
        l426_211(x),
        l426_212(x),
        l426_213(x),
        l426_214(x),
        l426_215(x),
        l426_216(x),
        l426_217(x),
        l426_218(x),
        l426_219(x),
        l426_220(x),
        l426_221(x),
        l426_222(x),
        l426_223(x),
        l426_224(x),
        l426_225(x),
        l426_226(x),
        l426_227(x),
        l426_228(x),
        l426_229(x),
        l426_230(x),
        l426_231(x),
        l426_232(x),
        l426_233(x),
        l426_234(x),
        l426_235(x),
        l426_236(x),
        l426_237(x),
        l426_238(x),
        l426_239(x),
        l426_240(x),
        l426_241(x),
        l426_242(x),
        l426_243(x),
        l426_244(x),
        l426_245(x),
        l426_246(x),
        l426_247(x),
        l426_248(x),
        l426_249(x),
        l426_250(x),
        l426_251(x),
        l426_252(x),
        l426_253(x),
        l426_254(x),
        l426_255(x),
    ]