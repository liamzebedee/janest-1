import numpy as np




# Generated from reverse engineering
def l258_g(x: np.ndarray) -> np.ndarray:
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




def l258_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l258_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l258_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l258_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l258_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l258_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l258_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l258_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l258_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l258_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l258_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l258_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l258_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l258_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l258_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l258_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l258_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l258_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l258_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l258_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l258_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l258_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l258_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l258_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l258_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l258_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l258_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l258_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l258_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l258_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l258_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l258_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l258_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l258_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l258_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l258_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l258_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l258_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l258_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l258_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l258_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l258_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l258_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l258_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l258_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l258_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l258_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l258_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l258_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l258_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l258_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l258_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l258_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l258_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l258_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l258_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l258_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l258_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l258_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l258_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l258_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l258_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l258_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l258_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l258_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l258_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l258_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l258_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l258_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l258_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l258_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l258_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l258_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l258_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l258_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l258_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l258_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l258_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l258_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l258_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l258_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l258_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l258_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l258_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l258_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l258_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l258_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l258_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l258_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l258_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l258_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l258_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l258_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l258_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l258_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l258_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l258_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l258_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + x[161])
def l258_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + x[162])
def l258_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + x[163])
def l258_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + x[164])
def l258_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + x[165])
def l258_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + x[166])
def l258_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + x[167])
def l258_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + x[168])
def l258_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + x[169])
def l258_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + x[170])
def l258_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + x[171])
def l258_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + x[172])
def l258_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + x[173])
def l258_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + x[174])
def l258_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + x[175])
def l258_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + x[176])
def l258_113(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + x[177] + 1.0)
def l258_114(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + x[178] + 1.0)
def l258_115(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + x[179] + 1.0)
def l258_116(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + x[180] + 1.0)
def l258_117(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + x[181] + 1.0)
def l258_118(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + x[182] + 1.0)
def l258_119(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + x[183] + 1.0)
def l258_120(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + x[184] + 1.0)
def l258_121(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + x[185] + 1.0)
def l258_122(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + x[186] + 1.0)
def l258_123(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + x[187] + 1.0)
def l258_124(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + x[188] + 1.0)
def l258_125(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + x[189] + 1.0)
def l258_126(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + x[190] + 1.0)
def l258_127(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[126] + x[191] + 1.0)
def l258_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[160] + -1.0)
def l258_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + x[161] + -1.0)
def l258_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + x[162] + -1.0)
def l258_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + x[163] + -1.0)
def l258_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + x[164] + -1.0)
def l258_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + x[165] + -1.0)
def l258_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + x[166] + -1.0)
def l258_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + x[167] + -1.0)
def l258_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + x[168] + -1.0)
def l258_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + x[169] + -1.0)
def l258_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + x[170] + -1.0)
def l258_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + x[171] + -1.0)
def l258_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + x[172] + -1.0)
def l258_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + x[173] + -1.0)
def l258_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + x[174] + -1.0)
def l258_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + x[175] + -1.0)
def l258_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + x[176] + -1.0)
def l258_145(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + x[177])
def l258_146(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + x[178])
def l258_147(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + x[179])
def l258_148(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + x[180])
def l258_149(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + x[181])
def l258_150(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + x[182])
def l258_151(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + x[183])
def l258_152(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + x[184])
def l258_153(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + x[185])
def l258_154(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + x[186])
def l258_155(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + x[187])
def l258_156(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + x[188])
def l258_157(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + x[189])
def l258_158(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + x[190])
def l258_159(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[126] + x[191])
def l258_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l258_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l258_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l258_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l258_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l258_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l258_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l258_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l258_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l258_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l258_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l258_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l258_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l258_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l258_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l258_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l258_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l258_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l258_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l258_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l258_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l258_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l258_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l258_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l258_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l258_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l258_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l258_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l258_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l258_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l258_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l258_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l258_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l258_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l258_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l258_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l258_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l258_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l258_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l258_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l258_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l258_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l258_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l258_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l258_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l258_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l258_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l258_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l258_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l258_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l258_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l258_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l258_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l258_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l258_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l258_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l258_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l258_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l258_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l258_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l258_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l258_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l258_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l258_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l258_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l258_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l258_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l258_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l258_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l258_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l258_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l258_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l258_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l258_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l258_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l258_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l258_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l258_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l258_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l258_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l258_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l258_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l258_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l258_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l258_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l258_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l258_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l258_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l258_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l258_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l258_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l258_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l258_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l258_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l258_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l258_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l258_(x):
    # x is a list (or vector) of length 288
    return [
        l258_0(x),
        l258_1(x),
        l258_2(x),
        l258_3(x),
        l258_4(x),
        l258_5(x),
        l258_6(x),
        l258_7(x),
        l258_8(x),
        l258_9(x),
        l258_10(x),
        l258_11(x),
        l258_12(x),
        l258_13(x),
        l258_14(x),
        l258_15(x),
        l258_16(x),
        l258_17(x),
        l258_18(x),
        l258_19(x),
        l258_20(x),
        l258_21(x),
        l258_22(x),
        l258_23(x),
        l258_24(x),
        l258_25(x),
        l258_26(x),
        l258_27(x),
        l258_28(x),
        l258_29(x),
        l258_30(x),
        l258_31(x),
        l258_32(x),
        l258_33(x),
        l258_34(x),
        l258_35(x),
        l258_36(x),
        l258_37(x),
        l258_38(x),
        l258_39(x),
        l258_40(x),
        l258_41(x),
        l258_42(x),
        l258_43(x),
        l258_44(x),
        l258_45(x),
        l258_46(x),
        l258_47(x),
        l258_48(x),
        l258_49(x),
        l258_50(x),
        l258_51(x),
        l258_52(x),
        l258_53(x),
        l258_54(x),
        l258_55(x),
        l258_56(x),
        l258_57(x),
        l258_58(x),
        l258_59(x),
        l258_60(x),
        l258_61(x),
        l258_62(x),
        l258_63(x),
        l258_64(x),
        l258_65(x),
        l258_66(x),
        l258_67(x),
        l258_68(x),
        l258_69(x),
        l258_70(x),
        l258_71(x),
        l258_72(x),
        l258_73(x),
        l258_74(x),
        l258_75(x),
        l258_76(x),
        l258_77(x),
        l258_78(x),
        l258_79(x),
        l258_80(x),
        l258_81(x),
        l258_82(x),
        l258_83(x),
        l258_84(x),
        l258_85(x),
        l258_86(x),
        l258_87(x),
        l258_88(x),
        l258_89(x),
        l258_90(x),
        l258_91(x),
        l258_92(x),
        l258_93(x),
        l258_94(x),
        l258_95(x),
        l258_96(x),
        l258_97(x),
        l258_98(x),
        l258_99(x),
        l258_100(x),
        l258_101(x),
        l258_102(x),
        l258_103(x),
        l258_104(x),
        l258_105(x),
        l258_106(x),
        l258_107(x),
        l258_108(x),
        l258_109(x),
        l258_110(x),
        l258_111(x),
        l258_112(x),
        l258_113(x),
        l258_114(x),
        l258_115(x),
        l258_116(x),
        l258_117(x),
        l258_118(x),
        l258_119(x),
        l258_120(x),
        l258_121(x),
        l258_122(x),
        l258_123(x),
        l258_124(x),
        l258_125(x),
        l258_126(x),
        l258_127(x),
        l258_128(x),
        l258_129(x),
        l258_130(x),
        l258_131(x),
        l258_132(x),
        l258_133(x),
        l258_134(x),
        l258_135(x),
        l258_136(x),
        l258_137(x),
        l258_138(x),
        l258_139(x),
        l258_140(x),
        l258_141(x),
        l258_142(x),
        l258_143(x),
        l258_144(x),
        l258_145(x),
        l258_146(x),
        l258_147(x),
        l258_148(x),
        l258_149(x),
        l258_150(x),
        l258_151(x),
        l258_152(x),
        l258_153(x),
        l258_154(x),
        l258_155(x),
        l258_156(x),
        l258_157(x),
        l258_158(x),
        l258_159(x),
        l258_160(x),
        l258_161(x),
        l258_162(x),
        l258_163(x),
        l258_164(x),
        l258_165(x),
        l258_166(x),
        l258_167(x),
        l258_168(x),
        l258_169(x),
        l258_170(x),
        l258_171(x),
        l258_172(x),
        l258_173(x),
        l258_174(x),
        l258_175(x),
        l258_176(x),
        l258_177(x),
        l258_178(x),
        l258_179(x),
        l258_180(x),
        l258_181(x),
        l258_182(x),
        l258_183(x),
        l258_184(x),
        l258_185(x),
        l258_186(x),
        l258_187(x),
        l258_188(x),
        l258_189(x),
        l258_190(x),
        l258_191(x),
        l258_192(x),
        l258_193(x),
        l258_194(x),
        l258_195(x),
        l258_196(x),
        l258_197(x),
        l258_198(x),
        l258_199(x),
        l258_200(x),
        l258_201(x),
        l258_202(x),
        l258_203(x),
        l258_204(x),
        l258_205(x),
        l258_206(x),
        l258_207(x),
        l258_208(x),
        l258_209(x),
        l258_210(x),
        l258_211(x),
        l258_212(x),
        l258_213(x),
        l258_214(x),
        l258_215(x),
        l258_216(x),
        l258_217(x),
        l258_218(x),
        l258_219(x),
        l258_220(x),
        l258_221(x),
        l258_222(x),
        l258_223(x),
        l258_224(x),
        l258_225(x),
        l258_226(x),
        l258_227(x),
        l258_228(x),
        l258_229(x),
        l258_230(x),
        l258_231(x),
        l258_232(x),
        l258_233(x),
        l258_234(x),
        l258_235(x),
        l258_236(x),
        l258_237(x),
        l258_238(x),
        l258_239(x),
        l258_240(x),
        l258_241(x),
        l258_242(x),
        l258_243(x),
        l258_244(x),
        l258_245(x),
        l258_246(x),
        l258_247(x),
        l258_248(x),
        l258_249(x),
        l258_250(x),
        l258_251(x),
        l258_252(x),
        l258_253(x),
        l258_254(x),
        l258_255(x),
    ]