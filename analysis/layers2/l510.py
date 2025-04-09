import numpy as np




# Generated from reverse engineering
def l510_g(x: np.ndarray) -> np.ndarray:
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




def l510_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l510_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l510_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l510_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l510_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l510_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l510_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l510_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l510_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l510_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l510_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l510_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l510_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l510_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l510_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l510_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l510_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l510_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l510_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l510_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l510_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l510_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l510_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l510_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l510_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l510_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l510_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l510_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l510_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l510_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l510_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l510_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l510_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l510_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l510_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l510_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l510_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l510_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l510_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l510_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l510_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l510_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l510_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l510_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l510_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l510_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l510_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l510_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l510_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l510_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l510_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l510_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l510_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l510_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l510_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l510_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l510_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l510_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l510_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l510_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l510_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l510_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l510_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l510_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l510_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l510_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l510_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l510_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l510_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l510_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l510_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l510_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l510_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l510_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l510_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l510_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l510_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l510_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l510_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l510_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l510_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l510_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l510_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l510_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l510_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l510_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l510_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l510_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l510_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l510_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l510_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l510_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l510_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l510_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l510_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l510_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l510_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l510_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + x[161])
def l510_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + x[162])
def l510_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + x[163])
def l510_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + x[164])
def l510_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + x[165])
def l510_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + x[166])
def l510_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + x[167])
def l510_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + x[168])
def l510_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + x[169])
def l510_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + x[170])
def l510_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + x[171])
def l510_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + x[172])
def l510_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + x[173])
def l510_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + x[174])
def l510_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + x[175])
def l510_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + x[176])
def l510_113(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + x[177] + 1.0)
def l510_114(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + x[178] + 1.0)
def l510_115(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + x[179] + 1.0)
def l510_116(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + x[180] + 1.0)
def l510_117(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + x[181] + 1.0)
def l510_118(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + x[182] + 1.0)
def l510_119(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + x[183] + 1.0)
def l510_120(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + x[184] + 1.0)
def l510_121(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + x[185] + 1.0)
def l510_122(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + x[186] + 1.0)
def l510_123(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + x[187] + 1.0)
def l510_124(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + x[188] + 1.0)
def l510_125(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + x[189] + 1.0)
def l510_126(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + x[190] + 1.0)
def l510_127(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[126] + x[191] + 1.0)
def l510_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[160] + -1.0)
def l510_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + x[161] + -1.0)
def l510_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + x[162] + -1.0)
def l510_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + x[163] + -1.0)
def l510_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + x[164] + -1.0)
def l510_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + x[165] + -1.0)
def l510_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + x[166] + -1.0)
def l510_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + x[167] + -1.0)
def l510_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + x[168] + -1.0)
def l510_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + x[169] + -1.0)
def l510_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + x[170] + -1.0)
def l510_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + x[171] + -1.0)
def l510_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + x[172] + -1.0)
def l510_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + x[173] + -1.0)
def l510_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + x[174] + -1.0)
def l510_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + x[175] + -1.0)
def l510_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + x[176] + -1.0)
def l510_145(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + x[177])
def l510_146(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + x[178])
def l510_147(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + x[179])
def l510_148(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + x[180])
def l510_149(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + x[181])
def l510_150(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + x[182])
def l510_151(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + x[183])
def l510_152(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + x[184])
def l510_153(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + x[185])
def l510_154(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + x[186])
def l510_155(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + x[187])
def l510_156(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + x[188])
def l510_157(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + x[189])
def l510_158(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + x[190])
def l510_159(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[126] + x[191])
def l510_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l510_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l510_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l510_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l510_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l510_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l510_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l510_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l510_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l510_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l510_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l510_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l510_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l510_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l510_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l510_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l510_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l510_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l510_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l510_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l510_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l510_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l510_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l510_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l510_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l510_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l510_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l510_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l510_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l510_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l510_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l510_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l510_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l510_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l510_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l510_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l510_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l510_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l510_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l510_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l510_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l510_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l510_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l510_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l510_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l510_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l510_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l510_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l510_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l510_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l510_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l510_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l510_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l510_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l510_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l510_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l510_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l510_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l510_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l510_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l510_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l510_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l510_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l510_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l510_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l510_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l510_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l510_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l510_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l510_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l510_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l510_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l510_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l510_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l510_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l510_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l510_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l510_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l510_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l510_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l510_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l510_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l510_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l510_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l510_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l510_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l510_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l510_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l510_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l510_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l510_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l510_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l510_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l510_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l510_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l510_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l510_(x):
    # x is a list (or vector) of length 288
    return [
        l510_0(x),
        l510_1(x),
        l510_2(x),
        l510_3(x),
        l510_4(x),
        l510_5(x),
        l510_6(x),
        l510_7(x),
        l510_8(x),
        l510_9(x),
        l510_10(x),
        l510_11(x),
        l510_12(x),
        l510_13(x),
        l510_14(x),
        l510_15(x),
        l510_16(x),
        l510_17(x),
        l510_18(x),
        l510_19(x),
        l510_20(x),
        l510_21(x),
        l510_22(x),
        l510_23(x),
        l510_24(x),
        l510_25(x),
        l510_26(x),
        l510_27(x),
        l510_28(x),
        l510_29(x),
        l510_30(x),
        l510_31(x),
        l510_32(x),
        l510_33(x),
        l510_34(x),
        l510_35(x),
        l510_36(x),
        l510_37(x),
        l510_38(x),
        l510_39(x),
        l510_40(x),
        l510_41(x),
        l510_42(x),
        l510_43(x),
        l510_44(x),
        l510_45(x),
        l510_46(x),
        l510_47(x),
        l510_48(x),
        l510_49(x),
        l510_50(x),
        l510_51(x),
        l510_52(x),
        l510_53(x),
        l510_54(x),
        l510_55(x),
        l510_56(x),
        l510_57(x),
        l510_58(x),
        l510_59(x),
        l510_60(x),
        l510_61(x),
        l510_62(x),
        l510_63(x),
        l510_64(x),
        l510_65(x),
        l510_66(x),
        l510_67(x),
        l510_68(x),
        l510_69(x),
        l510_70(x),
        l510_71(x),
        l510_72(x),
        l510_73(x),
        l510_74(x),
        l510_75(x),
        l510_76(x),
        l510_77(x),
        l510_78(x),
        l510_79(x),
        l510_80(x),
        l510_81(x),
        l510_82(x),
        l510_83(x),
        l510_84(x),
        l510_85(x),
        l510_86(x),
        l510_87(x),
        l510_88(x),
        l510_89(x),
        l510_90(x),
        l510_91(x),
        l510_92(x),
        l510_93(x),
        l510_94(x),
        l510_95(x),
        l510_96(x),
        l510_97(x),
        l510_98(x),
        l510_99(x),
        l510_100(x),
        l510_101(x),
        l510_102(x),
        l510_103(x),
        l510_104(x),
        l510_105(x),
        l510_106(x),
        l510_107(x),
        l510_108(x),
        l510_109(x),
        l510_110(x),
        l510_111(x),
        l510_112(x),
        l510_113(x),
        l510_114(x),
        l510_115(x),
        l510_116(x),
        l510_117(x),
        l510_118(x),
        l510_119(x),
        l510_120(x),
        l510_121(x),
        l510_122(x),
        l510_123(x),
        l510_124(x),
        l510_125(x),
        l510_126(x),
        l510_127(x),
        l510_128(x),
        l510_129(x),
        l510_130(x),
        l510_131(x),
        l510_132(x),
        l510_133(x),
        l510_134(x),
        l510_135(x),
        l510_136(x),
        l510_137(x),
        l510_138(x),
        l510_139(x),
        l510_140(x),
        l510_141(x),
        l510_142(x),
        l510_143(x),
        l510_144(x),
        l510_145(x),
        l510_146(x),
        l510_147(x),
        l510_148(x),
        l510_149(x),
        l510_150(x),
        l510_151(x),
        l510_152(x),
        l510_153(x),
        l510_154(x),
        l510_155(x),
        l510_156(x),
        l510_157(x),
        l510_158(x),
        l510_159(x),
        l510_160(x),
        l510_161(x),
        l510_162(x),
        l510_163(x),
        l510_164(x),
        l510_165(x),
        l510_166(x),
        l510_167(x),
        l510_168(x),
        l510_169(x),
        l510_170(x),
        l510_171(x),
        l510_172(x),
        l510_173(x),
        l510_174(x),
        l510_175(x),
        l510_176(x),
        l510_177(x),
        l510_178(x),
        l510_179(x),
        l510_180(x),
        l510_181(x),
        l510_182(x),
        l510_183(x),
        l510_184(x),
        l510_185(x),
        l510_186(x),
        l510_187(x),
        l510_188(x),
        l510_189(x),
        l510_190(x),
        l510_191(x),
        l510_192(x),
        l510_193(x),
        l510_194(x),
        l510_195(x),
        l510_196(x),
        l510_197(x),
        l510_198(x),
        l510_199(x),
        l510_200(x),
        l510_201(x),
        l510_202(x),
        l510_203(x),
        l510_204(x),
        l510_205(x),
        l510_206(x),
        l510_207(x),
        l510_208(x),
        l510_209(x),
        l510_210(x),
        l510_211(x),
        l510_212(x),
        l510_213(x),
        l510_214(x),
        l510_215(x),
        l510_216(x),
        l510_217(x),
        l510_218(x),
        l510_219(x),
        l510_220(x),
        l510_221(x),
        l510_222(x),
        l510_223(x),
        l510_224(x),
        l510_225(x),
        l510_226(x),
        l510_227(x),
        l510_228(x),
        l510_229(x),
        l510_230(x),
        l510_231(x),
        l510_232(x),
        l510_233(x),
        l510_234(x),
        l510_235(x),
        l510_236(x),
        l510_237(x),
        l510_238(x),
        l510_239(x),
        l510_240(x),
        l510_241(x),
        l510_242(x),
        l510_243(x),
        l510_244(x),
        l510_245(x),
        l510_246(x),
        l510_247(x),
        l510_248(x),
        l510_249(x),
        l510_250(x),
        l510_251(x),
        l510_252(x),
        l510_253(x),
        l510_254(x),
        l510_255(x),
    ]