import numpy as np




# Generated from reverse engineering
def l174_g(x: np.ndarray) -> np.ndarray:
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




def l174_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l174_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l174_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l174_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l174_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l174_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l174_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l174_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l174_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l174_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l174_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l174_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l174_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l174_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l174_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l174_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l174_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l174_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l174_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l174_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l174_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l174_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l174_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l174_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l174_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l174_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l174_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l174_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l174_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l174_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l174_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l174_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l174_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l174_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l174_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l174_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l174_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l174_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l174_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l174_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l174_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l174_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l174_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l174_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l174_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l174_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l174_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l174_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l174_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l174_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l174_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l174_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l174_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l174_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l174_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l174_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l174_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l174_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l174_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l174_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l174_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l174_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l174_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l174_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l174_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l174_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l174_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l174_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l174_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l174_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l174_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l174_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l174_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l174_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l174_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l174_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l174_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l174_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l174_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l174_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l174_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l174_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l174_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l174_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l174_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l174_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l174_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l174_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l174_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l174_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l174_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l174_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l174_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l174_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l174_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l174_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l174_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l174_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + x[161])
def l174_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + x[162])
def l174_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + x[163])
def l174_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + x[164])
def l174_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + x[165])
def l174_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + x[166])
def l174_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + x[167])
def l174_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + x[168])
def l174_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + x[169])
def l174_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + x[170])
def l174_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + x[171])
def l174_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + x[172])
def l174_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + x[173])
def l174_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + x[174])
def l174_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + x[175])
def l174_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + x[176])
def l174_113(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + x[177] + 1.0)
def l174_114(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + x[178] + 1.0)
def l174_115(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + x[179] + 1.0)
def l174_116(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + x[180] + 1.0)
def l174_117(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + x[181] + 1.0)
def l174_118(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + x[182] + 1.0)
def l174_119(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + x[183] + 1.0)
def l174_120(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + x[184] + 1.0)
def l174_121(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + x[185] + 1.0)
def l174_122(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + x[186] + 1.0)
def l174_123(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + x[187] + 1.0)
def l174_124(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + x[188] + 1.0)
def l174_125(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + x[189] + 1.0)
def l174_126(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + x[190] + 1.0)
def l174_127(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[126] + x[191] + 1.0)
def l174_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[160] + -1.0)
def l174_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + x[161] + -1.0)
def l174_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + x[162] + -1.0)
def l174_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + x[163] + -1.0)
def l174_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + x[164] + -1.0)
def l174_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + x[165] + -1.0)
def l174_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + x[166] + -1.0)
def l174_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + x[167] + -1.0)
def l174_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + x[168] + -1.0)
def l174_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + x[169] + -1.0)
def l174_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + x[170] + -1.0)
def l174_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + x[171] + -1.0)
def l174_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + x[172] + -1.0)
def l174_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + x[173] + -1.0)
def l174_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + x[174] + -1.0)
def l174_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + x[175] + -1.0)
def l174_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + x[176] + -1.0)
def l174_145(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + x[177])
def l174_146(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + x[178])
def l174_147(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + x[179])
def l174_148(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + x[180])
def l174_149(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + x[181])
def l174_150(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + x[182])
def l174_151(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + x[183])
def l174_152(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + x[184])
def l174_153(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + x[185])
def l174_154(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + x[186])
def l174_155(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + x[187])
def l174_156(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + x[188])
def l174_157(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + x[189])
def l174_158(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + x[190])
def l174_159(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[126] + x[191])
def l174_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l174_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l174_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l174_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l174_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l174_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l174_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l174_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l174_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l174_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l174_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l174_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l174_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l174_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l174_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l174_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l174_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l174_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l174_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l174_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l174_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l174_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l174_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l174_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l174_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l174_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l174_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l174_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l174_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l174_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l174_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l174_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l174_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l174_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l174_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l174_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l174_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l174_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l174_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l174_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l174_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l174_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l174_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l174_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l174_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l174_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l174_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l174_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l174_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l174_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l174_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l174_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l174_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l174_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l174_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l174_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l174_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l174_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l174_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l174_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l174_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l174_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l174_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l174_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l174_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l174_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l174_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l174_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l174_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l174_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l174_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l174_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l174_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l174_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l174_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l174_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l174_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l174_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l174_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l174_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l174_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l174_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l174_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l174_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l174_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l174_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l174_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l174_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l174_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l174_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l174_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l174_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l174_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l174_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l174_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l174_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l174_(x):
    # x is a list (or vector) of length 288
    return [
        l174_0(x),
        l174_1(x),
        l174_2(x),
        l174_3(x),
        l174_4(x),
        l174_5(x),
        l174_6(x),
        l174_7(x),
        l174_8(x),
        l174_9(x),
        l174_10(x),
        l174_11(x),
        l174_12(x),
        l174_13(x),
        l174_14(x),
        l174_15(x),
        l174_16(x),
        l174_17(x),
        l174_18(x),
        l174_19(x),
        l174_20(x),
        l174_21(x),
        l174_22(x),
        l174_23(x),
        l174_24(x),
        l174_25(x),
        l174_26(x),
        l174_27(x),
        l174_28(x),
        l174_29(x),
        l174_30(x),
        l174_31(x),
        l174_32(x),
        l174_33(x),
        l174_34(x),
        l174_35(x),
        l174_36(x),
        l174_37(x),
        l174_38(x),
        l174_39(x),
        l174_40(x),
        l174_41(x),
        l174_42(x),
        l174_43(x),
        l174_44(x),
        l174_45(x),
        l174_46(x),
        l174_47(x),
        l174_48(x),
        l174_49(x),
        l174_50(x),
        l174_51(x),
        l174_52(x),
        l174_53(x),
        l174_54(x),
        l174_55(x),
        l174_56(x),
        l174_57(x),
        l174_58(x),
        l174_59(x),
        l174_60(x),
        l174_61(x),
        l174_62(x),
        l174_63(x),
        l174_64(x),
        l174_65(x),
        l174_66(x),
        l174_67(x),
        l174_68(x),
        l174_69(x),
        l174_70(x),
        l174_71(x),
        l174_72(x),
        l174_73(x),
        l174_74(x),
        l174_75(x),
        l174_76(x),
        l174_77(x),
        l174_78(x),
        l174_79(x),
        l174_80(x),
        l174_81(x),
        l174_82(x),
        l174_83(x),
        l174_84(x),
        l174_85(x),
        l174_86(x),
        l174_87(x),
        l174_88(x),
        l174_89(x),
        l174_90(x),
        l174_91(x),
        l174_92(x),
        l174_93(x),
        l174_94(x),
        l174_95(x),
        l174_96(x),
        l174_97(x),
        l174_98(x),
        l174_99(x),
        l174_100(x),
        l174_101(x),
        l174_102(x),
        l174_103(x),
        l174_104(x),
        l174_105(x),
        l174_106(x),
        l174_107(x),
        l174_108(x),
        l174_109(x),
        l174_110(x),
        l174_111(x),
        l174_112(x),
        l174_113(x),
        l174_114(x),
        l174_115(x),
        l174_116(x),
        l174_117(x),
        l174_118(x),
        l174_119(x),
        l174_120(x),
        l174_121(x),
        l174_122(x),
        l174_123(x),
        l174_124(x),
        l174_125(x),
        l174_126(x),
        l174_127(x),
        l174_128(x),
        l174_129(x),
        l174_130(x),
        l174_131(x),
        l174_132(x),
        l174_133(x),
        l174_134(x),
        l174_135(x),
        l174_136(x),
        l174_137(x),
        l174_138(x),
        l174_139(x),
        l174_140(x),
        l174_141(x),
        l174_142(x),
        l174_143(x),
        l174_144(x),
        l174_145(x),
        l174_146(x),
        l174_147(x),
        l174_148(x),
        l174_149(x),
        l174_150(x),
        l174_151(x),
        l174_152(x),
        l174_153(x),
        l174_154(x),
        l174_155(x),
        l174_156(x),
        l174_157(x),
        l174_158(x),
        l174_159(x),
        l174_160(x),
        l174_161(x),
        l174_162(x),
        l174_163(x),
        l174_164(x),
        l174_165(x),
        l174_166(x),
        l174_167(x),
        l174_168(x),
        l174_169(x),
        l174_170(x),
        l174_171(x),
        l174_172(x),
        l174_173(x),
        l174_174(x),
        l174_175(x),
        l174_176(x),
        l174_177(x),
        l174_178(x),
        l174_179(x),
        l174_180(x),
        l174_181(x),
        l174_182(x),
        l174_183(x),
        l174_184(x),
        l174_185(x),
        l174_186(x),
        l174_187(x),
        l174_188(x),
        l174_189(x),
        l174_190(x),
        l174_191(x),
        l174_192(x),
        l174_193(x),
        l174_194(x),
        l174_195(x),
        l174_196(x),
        l174_197(x),
        l174_198(x),
        l174_199(x),
        l174_200(x),
        l174_201(x),
        l174_202(x),
        l174_203(x),
        l174_204(x),
        l174_205(x),
        l174_206(x),
        l174_207(x),
        l174_208(x),
        l174_209(x),
        l174_210(x),
        l174_211(x),
        l174_212(x),
        l174_213(x),
        l174_214(x),
        l174_215(x),
        l174_216(x),
        l174_217(x),
        l174_218(x),
        l174_219(x),
        l174_220(x),
        l174_221(x),
        l174_222(x),
        l174_223(x),
        l174_224(x),
        l174_225(x),
        l174_226(x),
        l174_227(x),
        l174_228(x),
        l174_229(x),
        l174_230(x),
        l174_231(x),
        l174_232(x),
        l174_233(x),
        l174_234(x),
        l174_235(x),
        l174_236(x),
        l174_237(x),
        l174_238(x),
        l174_239(x),
        l174_240(x),
        l174_241(x),
        l174_242(x),
        l174_243(x),
        l174_244(x),
        l174_245(x),
        l174_246(x),
        l174_247(x),
        l174_248(x),
        l174_249(x),
        l174_250(x),
        l174_251(x),
        l174_252(x),
        l174_253(x),
        l174_254(x),
        l174_255(x),
    ]