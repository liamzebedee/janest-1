import numpy as np




# Generated from reverse engineering
def l64_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 288
    out = np.empty(288, dtype=np.float32)
    
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
        
    # for i in range(160, 192):
    for i in range(0, 32):
        s = x[192 + i] + -2.0 * x[i + 224]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(192, 288):
    for i in range(0, 96):
        s = x[256 + i]
        out[192 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l64_0(x):
    # x is a list (or vector) of length 352
    return max(0, x[0])
def l64_1(x):
    # x is a list (or vector) of length 352
    return max(0, x[1])
def l64_2(x):
    # x is a list (or vector) of length 352
    return max(0, x[2])
def l64_3(x):
    # x is a list (or vector) of length 352
    return max(0, x[3])
def l64_4(x):
    # x is a list (or vector) of length 352
    return max(0, x[4])
def l64_5(x):
    # x is a list (or vector) of length 352
    return max(0, x[5])
def l64_6(x):
    # x is a list (or vector) of length 352
    return max(0, x[6])
def l64_7(x):
    # x is a list (or vector) of length 352
    return max(0, x[7])
def l64_8(x):
    # x is a list (or vector) of length 352
    return max(0, x[8])
def l64_9(x):
    # x is a list (or vector) of length 352
    return max(0, x[9])
def l64_10(x):
    # x is a list (or vector) of length 352
    return max(0, x[10])
def l64_11(x):
    # x is a list (or vector) of length 352
    return max(0, x[11])
def l64_12(x):
    # x is a list (or vector) of length 352
    return max(0, x[12])
def l64_13(x):
    # x is a list (or vector) of length 352
    return max(0, x[13])
def l64_14(x):
    # x is a list (or vector) of length 352
    return max(0, x[14])
def l64_15(x):
    # x is a list (or vector) of length 352
    return max(0, x[15])
def l64_16(x):
    # x is a list (or vector) of length 352
    return max(0, x[16])
def l64_17(x):
    # x is a list (or vector) of length 352
    return max(0, x[17])
def l64_18(x):
    # x is a list (or vector) of length 352
    return max(0, x[18])
def l64_19(x):
    # x is a list (or vector) of length 352
    return max(0, x[19])
def l64_20(x):
    # x is a list (or vector) of length 352
    return max(0, x[20])
def l64_21(x):
    # x is a list (or vector) of length 352
    return max(0, x[21])
def l64_22(x):
    # x is a list (or vector) of length 352
    return max(0, x[22])
def l64_23(x):
    # x is a list (or vector) of length 352
    return max(0, x[23])
def l64_24(x):
    # x is a list (or vector) of length 352
    return max(0, x[24])
def l64_25(x):
    # x is a list (or vector) of length 352
    return max(0, x[25])
def l64_26(x):
    # x is a list (or vector) of length 352
    return max(0, x[26])
def l64_27(x):
    # x is a list (or vector) of length 352
    return max(0, x[27])
def l64_28(x):
    # x is a list (or vector) of length 352
    return max(0, x[28])
def l64_29(x):
    # x is a list (or vector) of length 352
    return max(0, x[29])
def l64_30(x):
    # x is a list (or vector) of length 352
    return max(0, x[30])
def l64_31(x):
    # x is a list (or vector) of length 352
    return max(0, x[31])
def l64_32(x):
    # x is a list (or vector) of length 352
    return max(0, x[32])
def l64_33(x):
    # x is a list (or vector) of length 352
    return max(0, x[33])
def l64_34(x):
    # x is a list (or vector) of length 352
    return max(0, x[34])
def l64_35(x):
    # x is a list (or vector) of length 352
    return max(0, x[35])
def l64_36(x):
    # x is a list (or vector) of length 352
    return max(0, x[36])
def l64_37(x):
    # x is a list (or vector) of length 352
    return max(0, x[37])
def l64_38(x):
    # x is a list (or vector) of length 352
    return max(0, x[38])
def l64_39(x):
    # x is a list (or vector) of length 352
    return max(0, x[39])
def l64_40(x):
    # x is a list (or vector) of length 352
    return max(0, x[40])
def l64_41(x):
    # x is a list (or vector) of length 352
    return max(0, x[41])
def l64_42(x):
    # x is a list (or vector) of length 352
    return max(0, x[42])
def l64_43(x):
    # x is a list (or vector) of length 352
    return max(0, x[43])
def l64_44(x):
    # x is a list (or vector) of length 352
    return max(0, x[44])
def l64_45(x):
    # x is a list (or vector) of length 352
    return max(0, x[45])
def l64_46(x):
    # x is a list (or vector) of length 352
    return max(0, x[46])
def l64_47(x):
    # x is a list (or vector) of length 352
    return max(0, x[47])
def l64_48(x):
    # x is a list (or vector) of length 352
    return max(0, x[48])
def l64_49(x):
    # x is a list (or vector) of length 352
    return max(0, x[49])
def l64_50(x):
    # x is a list (or vector) of length 352
    return max(0, x[50])
def l64_51(x):
    # x is a list (or vector) of length 352
    return max(0, x[51])
def l64_52(x):
    # x is a list (or vector) of length 352
    return max(0, x[52])
def l64_53(x):
    # x is a list (or vector) of length 352
    return max(0, x[53])
def l64_54(x):
    # x is a list (or vector) of length 352
    return max(0, x[54])
def l64_55(x):
    # x is a list (or vector) of length 352
    return max(0, x[55])
def l64_56(x):
    # x is a list (or vector) of length 352
    return max(0, x[56])
def l64_57(x):
    # x is a list (or vector) of length 352
    return max(0, x[57])
def l64_58(x):
    # x is a list (or vector) of length 352
    return max(0, x[58])
def l64_59(x):
    # x is a list (or vector) of length 352
    return max(0, x[59])
def l64_60(x):
    # x is a list (or vector) of length 352
    return max(0, x[60])
def l64_61(x):
    # x is a list (or vector) of length 352
    return max(0, x[61])
def l64_62(x):
    # x is a list (or vector) of length 352
    return max(0, x[62])
def l64_63(x):
    # x is a list (or vector) of length 352
    return max(0, x[63])
def l64_64(x):
    # x is a list (or vector) of length 352
    return max(0, x[64])
def l64_65(x):
    # x is a list (or vector) of length 352
    return max(0, x[65])
def l64_66(x):
    # x is a list (or vector) of length 352
    return max(0, x[66])
def l64_67(x):
    # x is a list (or vector) of length 352
    return max(0, x[67])
def l64_68(x):
    # x is a list (or vector) of length 352
    return max(0, x[68])
def l64_69(x):
    # x is a list (or vector) of length 352
    return max(0, x[69])
def l64_70(x):
    # x is a list (or vector) of length 352
    return max(0, x[70])
def l64_71(x):
    # x is a list (or vector) of length 352
    return max(0, x[71])
def l64_72(x):
    # x is a list (or vector) of length 352
    return max(0, x[72])
def l64_73(x):
    # x is a list (or vector) of length 352
    return max(0, x[73])
def l64_74(x):
    # x is a list (or vector) of length 352
    return max(0, x[74])
def l64_75(x):
    # x is a list (or vector) of length 352
    return max(0, x[75])
def l64_76(x):
    # x is a list (or vector) of length 352
    return max(0, x[76])
def l64_77(x):
    # x is a list (or vector) of length 352
    return max(0, x[77])
def l64_78(x):
    # x is a list (or vector) of length 352
    return max(0, x[78])
def l64_79(x):
    # x is a list (or vector) of length 352
    return max(0, x[79])
def l64_80(x):
    # x is a list (or vector) of length 352
    return max(0, x[80])
def l64_81(x):
    # x is a list (or vector) of length 352
    return max(0, x[81])
def l64_82(x):
    # x is a list (or vector) of length 352
    return max(0, x[82])
def l64_83(x):
    # x is a list (or vector) of length 352
    return max(0, x[83])
def l64_84(x):
    # x is a list (or vector) of length 352
    return max(0, x[84])
def l64_85(x):
    # x is a list (or vector) of length 352
    return max(0, x[85])
def l64_86(x):
    # x is a list (or vector) of length 352
    return max(0, x[86])
def l64_87(x):
    # x is a list (or vector) of length 352
    return max(0, x[87])
def l64_88(x):
    # x is a list (or vector) of length 352
    return max(0, x[88])
def l64_89(x):
    # x is a list (or vector) of length 352
    return max(0, x[89])
def l64_90(x):
    # x is a list (or vector) of length 352
    return max(0, x[90])
def l64_91(x):
    # x is a list (or vector) of length 352
    return max(0, x[91])
def l64_92(x):
    # x is a list (or vector) of length 352
    return max(0, x[92])
def l64_93(x):
    # x is a list (or vector) of length 352
    return max(0, x[93])
def l64_94(x):
    # x is a list (or vector) of length 352
    return max(0, x[94])
def l64_95(x):
    # x is a list (or vector) of length 352
    return max(0, x[95])
def l64_96(x):
    # x is a list (or vector) of length 352
    return max(0, x[160])
def l64_97(x):
    # x is a list (or vector) of length 352
    return max(0, x[96] + x[161])
def l64_98(x):
    # x is a list (or vector) of length 352
    return max(0, x[97] + x[162])
def l64_99(x):
    # x is a list (or vector) of length 352
    return max(0, x[98] + x[163])
def l64_100(x):
    # x is a list (or vector) of length 352
    return max(0, x[99] + x[164])
def l64_101(x):
    # x is a list (or vector) of length 352
    return max(0, x[100] + x[165])
def l64_102(x):
    # x is a list (or vector) of length 352
    return max(0, x[101] + x[166])
def l64_103(x):
    # x is a list (or vector) of length 352
    return max(0, x[102] + x[167])
def l64_104(x):
    # x is a list (or vector) of length 352
    return max(0, x[103] + x[168])
def l64_105(x):
    # x is a list (or vector) of length 352
    return max(0, x[104] + x[169])
def l64_106(x):
    # x is a list (or vector) of length 352
    return max(0, x[105] + x[170])
def l64_107(x):
    # x is a list (or vector) of length 352
    return max(0, x[106] + x[171])
def l64_108(x):
    # x is a list (or vector) of length 352
    return max(0, x[107] + x[172])
def l64_109(x):
    # x is a list (or vector) of length 352
    return max(0, x[108] + x[173])
def l64_110(x):
    # x is a list (or vector) of length 352
    return max(0, x[109] + x[174])
def l64_111(x):
    # x is a list (or vector) of length 352
    return max(0, x[110] + x[175])
def l64_112(x):
    # x is a list (or vector) of length 352
    return max(0, x[111] + x[176])
def l64_113(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[112] + x[177] + 1.0)
def l64_114(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[113] + x[178] + 1.0)
def l64_115(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[114] + x[179] + 1.0)
def l64_116(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[115] + x[180] + 1.0)
def l64_117(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[116] + x[181] + 1.0)
def l64_118(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[117] + x[182] + 1.0)
def l64_119(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[118] + x[183] + 1.0)
def l64_120(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[119] + x[184] + 1.0)
def l64_121(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[120] + x[185] + 1.0)
def l64_122(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[121] + x[186] + 1.0)
def l64_123(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[122] + x[187] + 1.0)
def l64_124(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[123] + x[188] + 1.0)
def l64_125(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[124] + x[189] + 1.0)
def l64_126(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[125] + x[190] + 1.0)
def l64_127(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[126] + x[191] + 1.0)
def l64_128(x):
    # x is a list (or vector) of length 352
    return max(0, x[160] + -1.0)
def l64_129(x):
    # x is a list (or vector) of length 352
    return max(0, x[96] + x[161] + -1.0)
def l64_130(x):
    # x is a list (or vector) of length 352
    return max(0, x[97] + x[162] + -1.0)
def l64_131(x):
    # x is a list (or vector) of length 352
    return max(0, x[98] + x[163] + -1.0)
def l64_132(x):
    # x is a list (or vector) of length 352
    return max(0, x[99] + x[164] + -1.0)
def l64_133(x):
    # x is a list (or vector) of length 352
    return max(0, x[100] + x[165] + -1.0)
def l64_134(x):
    # x is a list (or vector) of length 352
    return max(0, x[101] + x[166] + -1.0)
def l64_135(x):
    # x is a list (or vector) of length 352
    return max(0, x[102] + x[167] + -1.0)
def l64_136(x):
    # x is a list (or vector) of length 352
    return max(0, x[103] + x[168] + -1.0)
def l64_137(x):
    # x is a list (or vector) of length 352
    return max(0, x[104] + x[169] + -1.0)
def l64_138(x):
    # x is a list (or vector) of length 352
    return max(0, x[105] + x[170] + -1.0)
def l64_139(x):
    # x is a list (or vector) of length 352
    return max(0, x[106] + x[171] + -1.0)
def l64_140(x):
    # x is a list (or vector) of length 352
    return max(0, x[107] + x[172] + -1.0)
def l64_141(x):
    # x is a list (or vector) of length 352
    return max(0, x[108] + x[173] + -1.0)
def l64_142(x):
    # x is a list (or vector) of length 352
    return max(0, x[109] + x[174] + -1.0)
def l64_143(x):
    # x is a list (or vector) of length 352
    return max(0, x[110] + x[175] + -1.0)
def l64_144(x):
    # x is a list (or vector) of length 352
    return max(0, x[111] + x[176] + -1.0)
def l64_145(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[112] + x[177])
def l64_146(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[113] + x[178])
def l64_147(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[114] + x[179])
def l64_148(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[115] + x[180])
def l64_149(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[116] + x[181])
def l64_150(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[117] + x[182])
def l64_151(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[118] + x[183])
def l64_152(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[119] + x[184])
def l64_153(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[120] + x[185])
def l64_154(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[121] + x[186])
def l64_155(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[122] + x[187])
def l64_156(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[123] + x[188])
def l64_157(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[124] + x[189])
def l64_158(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[125] + x[190])
def l64_159(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[126] + x[191])
def l64_160(x):
    # x is a list (or vector) of length 352
    return max(0, x[192] + -2.0*x[224])
def l64_161(x):
    # x is a list (or vector) of length 352
    return max(0, x[193] + -2.0*x[225])
def l64_162(x):
    # x is a list (or vector) of length 352
    return max(0, x[194] + -2.0*x[226])
def l64_163(x):
    # x is a list (or vector) of length 352
    return max(0, x[195] + -2.0*x[227])
def l64_164(x):
    # x is a list (or vector) of length 352
    return max(0, x[196] + -2.0*x[228])
def l64_165(x):
    # x is a list (or vector) of length 352
    return max(0, x[197] + -2.0*x[229])
def l64_166(x):
    # x is a list (or vector) of length 352
    return max(0, x[198] + -2.0*x[230])
def l64_167(x):
    # x is a list (or vector) of length 352
    return max(0, x[199] + -2.0*x[231])
def l64_168(x):
    # x is a list (or vector) of length 352
    return max(0, x[200] + -2.0*x[232])
def l64_169(x):
    # x is a list (or vector) of length 352
    return max(0, x[201] + -2.0*x[233])
def l64_170(x):
    # x is a list (or vector) of length 352
    return max(0, x[202] + -2.0*x[234])
def l64_171(x):
    # x is a list (or vector) of length 352
    return max(0, x[203] + -2.0*x[235])
def l64_172(x):
    # x is a list (or vector) of length 352
    return max(0, x[204] + -2.0*x[236])
def l64_173(x):
    # x is a list (or vector) of length 352
    return max(0, x[205] + -2.0*x[237])
def l64_174(x):
    # x is a list (or vector) of length 352
    return max(0, x[206] + -2.0*x[238])
def l64_175(x):
    # x is a list (or vector) of length 352
    return max(0, x[207] + -2.0*x[239])
def l64_176(x):
    # x is a list (or vector) of length 352
    return max(0, x[208] + -2.0*x[240])
def l64_177(x):
    # x is a list (or vector) of length 352
    return max(0, x[209] + -2.0*x[241])
def l64_178(x):
    # x is a list (or vector) of length 352
    return max(0, x[210] + -2.0*x[242])
def l64_179(x):
    # x is a list (or vector) of length 352
    return max(0, x[211] + -2.0*x[243])
def l64_180(x):
    # x is a list (or vector) of length 352
    return max(0, x[212] + -2.0*x[244])
def l64_181(x):
    # x is a list (or vector) of length 352
    return max(0, x[213] + -2.0*x[245])
def l64_182(x):
    # x is a list (or vector) of length 352
    return max(0, x[214] + -2.0*x[246])
def l64_183(x):
    # x is a list (or vector) of length 352
    return max(0, x[215] + -2.0*x[247])
def l64_184(x):
    # x is a list (or vector) of length 352
    return max(0, x[216] + -2.0*x[248])
def l64_185(x):
    # x is a list (or vector) of length 352
    return max(0, x[217] + -2.0*x[249])
def l64_186(x):
    # x is a list (or vector) of length 352
    return max(0, x[218] + -2.0*x[250])
def l64_187(x):
    # x is a list (or vector) of length 352
    return max(0, x[219] + -2.0*x[251])
def l64_188(x):
    # x is a list (or vector) of length 352
    return max(0, x[220] + -2.0*x[252])
def l64_189(x):
    # x is a list (or vector) of length 352
    return max(0, x[221] + -2.0*x[253])
def l64_190(x):
    # x is a list (or vector) of length 352
    return max(0, x[222] + -2.0*x[254])
def l64_191(x):
    # x is a list (or vector) of length 352
    return max(0, x[223] + -2.0*x[255])
def l64_192(x):
    # x is a list (or vector) of length 352
    return max(0, x[256])
def l64_193(x):
    # x is a list (or vector) of length 352
    return max(0, x[257])
def l64_194(x):
    # x is a list (or vector) of length 352
    return max(0, x[258])
def l64_195(x):
    # x is a list (or vector) of length 352
    return max(0, x[259])
def l64_196(x):
    # x is a list (or vector) of length 352
    return max(0, x[260])
def l64_197(x):
    # x is a list (or vector) of length 352
    return max(0, x[261])
def l64_198(x):
    # x is a list (or vector) of length 352
    return max(0, x[262])
def l64_199(x):
    # x is a list (or vector) of length 352
    return max(0, x[263])
def l64_200(x):
    # x is a list (or vector) of length 352
    return max(0, x[264])
def l64_201(x):
    # x is a list (or vector) of length 352
    return max(0, x[265])
def l64_202(x):
    # x is a list (or vector) of length 352
    return max(0, x[266])
def l64_203(x):
    # x is a list (or vector) of length 352
    return max(0, x[267])
def l64_204(x):
    # x is a list (or vector) of length 352
    return max(0, x[268])
def l64_205(x):
    # x is a list (or vector) of length 352
    return max(0, x[269])
def l64_206(x):
    # x is a list (or vector) of length 352
    return max(0, x[270])
def l64_207(x):
    # x is a list (or vector) of length 352
    return max(0, x[271])
def l64_208(x):
    # x is a list (or vector) of length 352
    return max(0, x[272])
def l64_209(x):
    # x is a list (or vector) of length 352
    return max(0, x[273])
def l64_210(x):
    # x is a list (or vector) of length 352
    return max(0, x[274])
def l64_211(x):
    # x is a list (or vector) of length 352
    return max(0, x[275])
def l64_212(x):
    # x is a list (or vector) of length 352
    return max(0, x[276])
def l64_213(x):
    # x is a list (or vector) of length 352
    return max(0, x[277])
def l64_214(x):
    # x is a list (or vector) of length 352
    return max(0, x[278])
def l64_215(x):
    # x is a list (or vector) of length 352
    return max(0, x[279])
def l64_216(x):
    # x is a list (or vector) of length 352
    return max(0, x[280])
def l64_217(x):
    # x is a list (or vector) of length 352
    return max(0, x[281])
def l64_218(x):
    # x is a list (or vector) of length 352
    return max(0, x[282])
def l64_219(x):
    # x is a list (or vector) of length 352
    return max(0, x[283])
def l64_220(x):
    # x is a list (or vector) of length 352
    return max(0, x[284])
def l64_221(x):
    # x is a list (or vector) of length 352
    return max(0, x[285])
def l64_222(x):
    # x is a list (or vector) of length 352
    return max(0, x[286])
def l64_223(x):
    # x is a list (or vector) of length 352
    return max(0, x[287])
def l64_224(x):
    # x is a list (or vector) of length 352
    return max(0, x[288])
def l64_225(x):
    # x is a list (or vector) of length 352
    return max(0, x[289])
def l64_226(x):
    # x is a list (or vector) of length 352
    return max(0, x[290])
def l64_227(x):
    # x is a list (or vector) of length 352
    return max(0, x[291])
def l64_228(x):
    # x is a list (or vector) of length 352
    return max(0, x[292])
def l64_229(x):
    # x is a list (or vector) of length 352
    return max(0, x[293])
def l64_230(x):
    # x is a list (or vector) of length 352
    return max(0, x[294])
def l64_231(x):
    # x is a list (or vector) of length 352
    return max(0, x[295])
def l64_232(x):
    # x is a list (or vector) of length 352
    return max(0, x[296])
def l64_233(x):
    # x is a list (or vector) of length 352
    return max(0, x[297])
def l64_234(x):
    # x is a list (or vector) of length 352
    return max(0, x[298])
def l64_235(x):
    # x is a list (or vector) of length 352
    return max(0, x[299])
def l64_236(x):
    # x is a list (or vector) of length 352
    return max(0, x[300])
def l64_237(x):
    # x is a list (or vector) of length 352
    return max(0, x[301])
def l64_238(x):
    # x is a list (or vector) of length 352
    return max(0, x[302])
def l64_239(x):
    # x is a list (or vector) of length 352
    return max(0, x[303])
def l64_240(x):
    # x is a list (or vector) of length 352
    return max(0, x[304])
def l64_241(x):
    # x is a list (or vector) of length 352
    return max(0, x[305])
def l64_242(x):
    # x is a list (or vector) of length 352
    return max(0, x[306])
def l64_243(x):
    # x is a list (or vector) of length 352
    return max(0, x[307])
def l64_244(x):
    # x is a list (or vector) of length 352
    return max(0, x[308])
def l64_245(x):
    # x is a list (or vector) of length 352
    return max(0, x[309])
def l64_246(x):
    # x is a list (or vector) of length 352
    return max(0, x[310])
def l64_247(x):
    # x is a list (or vector) of length 352
    return max(0, x[311])
def l64_248(x):
    # x is a list (or vector) of length 352
    return max(0, x[312])
def l64_249(x):
    # x is a list (or vector) of length 352
    return max(0, x[313])
def l64_250(x):
    # x is a list (or vector) of length 352
    return max(0, x[314])
def l64_251(x):
    # x is a list (or vector) of length 352
    return max(0, x[315])
def l64_252(x):
    # x is a list (or vector) of length 352
    return max(0, x[316])
def l64_253(x):
    # x is a list (or vector) of length 352
    return max(0, x[317])
def l64_254(x):
    # x is a list (or vector) of length 352
    return max(0, x[318])
def l64_255(x):
    # x is a list (or vector) of length 352
    return max(0, x[319])
def l64_256(x):
    # x is a list (or vector) of length 352
    return max(0, x[320])
def l64_257(x):
    # x is a list (or vector) of length 352
    return max(0, x[321])
def l64_258(x):
    # x is a list (or vector) of length 352
    return max(0, x[322])
def l64_259(x):
    # x is a list (or vector) of length 352
    return max(0, x[323])
def l64_260(x):
    # x is a list (or vector) of length 352
    return max(0, x[324])
def l64_261(x):
    # x is a list (or vector) of length 352
    return max(0, x[325])
def l64_262(x):
    # x is a list (or vector) of length 352
    return max(0, x[326])
def l64_263(x):
    # x is a list (or vector) of length 352
    return max(0, x[327])
def l64_264(x):
    # x is a list (or vector) of length 352
    return max(0, x[328])
def l64_265(x):
    # x is a list (or vector) of length 352
    return max(0, x[329])
def l64_266(x):
    # x is a list (or vector) of length 352
    return max(0, x[330])
def l64_267(x):
    # x is a list (or vector) of length 352
    return max(0, x[331])
def l64_268(x):
    # x is a list (or vector) of length 352
    return max(0, x[332])
def l64_269(x):
    # x is a list (or vector) of length 352
    return max(0, x[333])
def l64_270(x):
    # x is a list (or vector) of length 352
    return max(0, x[334])
def l64_271(x):
    # x is a list (or vector) of length 352
    return max(0, x[335])
def l64_272(x):
    # x is a list (or vector) of length 352
    return max(0, x[336])
def l64_273(x):
    # x is a list (or vector) of length 352
    return max(0, x[337])
def l64_274(x):
    # x is a list (or vector) of length 352
    return max(0, x[338])
def l64_275(x):
    # x is a list (or vector) of length 352
    return max(0, x[339])
def l64_276(x):
    # x is a list (or vector) of length 352
    return max(0, x[340])
def l64_277(x):
    # x is a list (or vector) of length 352
    return max(0, x[341])
def l64_278(x):
    # x is a list (or vector) of length 352
    return max(0, x[342])
def l64_279(x):
    # x is a list (or vector) of length 352
    return max(0, x[343])
def l64_280(x):
    # x is a list (or vector) of length 352
    return max(0, x[344])
def l64_281(x):
    # x is a list (or vector) of length 352
    return max(0, x[345])
def l64_282(x):
    # x is a list (or vector) of length 352
    return max(0, x[346])
def l64_283(x):
    # x is a list (or vector) of length 352
    return max(0, x[347])
def l64_284(x):
    # x is a list (or vector) of length 352
    return max(0, x[348])
def l64_285(x):
    # x is a list (or vector) of length 352
    return max(0, x[349])
def l64_286(x):
    # x is a list (or vector) of length 352
    return max(0, x[350])
def l64_287(x):
    # x is a list (or vector) of length 352
    return max(0, x[351])
def l64_(x):
    # x is a list (or vector) of length 352
    return [
        l64_0(x),
        l64_1(x),
        l64_2(x),
        l64_3(x),
        l64_4(x),
        l64_5(x),
        l64_6(x),
        l64_7(x),
        l64_8(x),
        l64_9(x),
        l64_10(x),
        l64_11(x),
        l64_12(x),
        l64_13(x),
        l64_14(x),
        l64_15(x),
        l64_16(x),
        l64_17(x),
        l64_18(x),
        l64_19(x),
        l64_20(x),
        l64_21(x),
        l64_22(x),
        l64_23(x),
        l64_24(x),
        l64_25(x),
        l64_26(x),
        l64_27(x),
        l64_28(x),
        l64_29(x),
        l64_30(x),
        l64_31(x),
        l64_32(x),
        l64_33(x),
        l64_34(x),
        l64_35(x),
        l64_36(x),
        l64_37(x),
        l64_38(x),
        l64_39(x),
        l64_40(x),
        l64_41(x),
        l64_42(x),
        l64_43(x),
        l64_44(x),
        l64_45(x),
        l64_46(x),
        l64_47(x),
        l64_48(x),
        l64_49(x),
        l64_50(x),
        l64_51(x),
        l64_52(x),
        l64_53(x),
        l64_54(x),
        l64_55(x),
        l64_56(x),
        l64_57(x),
        l64_58(x),
        l64_59(x),
        l64_60(x),
        l64_61(x),
        l64_62(x),
        l64_63(x),
        l64_64(x),
        l64_65(x),
        l64_66(x),
        l64_67(x),
        l64_68(x),
        l64_69(x),
        l64_70(x),
        l64_71(x),
        l64_72(x),
        l64_73(x),
        l64_74(x),
        l64_75(x),
        l64_76(x),
        l64_77(x),
        l64_78(x),
        l64_79(x),
        l64_80(x),
        l64_81(x),
        l64_82(x),
        l64_83(x),
        l64_84(x),
        l64_85(x),
        l64_86(x),
        l64_87(x),
        l64_88(x),
        l64_89(x),
        l64_90(x),
        l64_91(x),
        l64_92(x),
        l64_93(x),
        l64_94(x),
        l64_95(x),
        l64_96(x),
        l64_97(x),
        l64_98(x),
        l64_99(x),
        l64_100(x),
        l64_101(x),
        l64_102(x),
        l64_103(x),
        l64_104(x),
        l64_105(x),
        l64_106(x),
        l64_107(x),
        l64_108(x),
        l64_109(x),
        l64_110(x),
        l64_111(x),
        l64_112(x),
        l64_113(x),
        l64_114(x),
        l64_115(x),
        l64_116(x),
        l64_117(x),
        l64_118(x),
        l64_119(x),
        l64_120(x),
        l64_121(x),
        l64_122(x),
        l64_123(x),
        l64_124(x),
        l64_125(x),
        l64_126(x),
        l64_127(x),
        l64_128(x),
        l64_129(x),
        l64_130(x),
        l64_131(x),
        l64_132(x),
        l64_133(x),
        l64_134(x),
        l64_135(x),
        l64_136(x),
        l64_137(x),
        l64_138(x),
        l64_139(x),
        l64_140(x),
        l64_141(x),
        l64_142(x),
        l64_143(x),
        l64_144(x),
        l64_145(x),
        l64_146(x),
        l64_147(x),
        l64_148(x),
        l64_149(x),
        l64_150(x),
        l64_151(x),
        l64_152(x),
        l64_153(x),
        l64_154(x),
        l64_155(x),
        l64_156(x),
        l64_157(x),
        l64_158(x),
        l64_159(x),
        l64_160(x),
        l64_161(x),
        l64_162(x),
        l64_163(x),
        l64_164(x),
        l64_165(x),
        l64_166(x),
        l64_167(x),
        l64_168(x),
        l64_169(x),
        l64_170(x),
        l64_171(x),
        l64_172(x),
        l64_173(x),
        l64_174(x),
        l64_175(x),
        l64_176(x),
        l64_177(x),
        l64_178(x),
        l64_179(x),
        l64_180(x),
        l64_181(x),
        l64_182(x),
        l64_183(x),
        l64_184(x),
        l64_185(x),
        l64_186(x),
        l64_187(x),
        l64_188(x),
        l64_189(x),
        l64_190(x),
        l64_191(x),
        l64_192(x),
        l64_193(x),
        l64_194(x),
        l64_195(x),
        l64_196(x),
        l64_197(x),
        l64_198(x),
        l64_199(x),
        l64_200(x),
        l64_201(x),
        l64_202(x),
        l64_203(x),
        l64_204(x),
        l64_205(x),
        l64_206(x),
        l64_207(x),
        l64_208(x),
        l64_209(x),
        l64_210(x),
        l64_211(x),
        l64_212(x),
        l64_213(x),
        l64_214(x),
        l64_215(x),
        l64_216(x),
        l64_217(x),
        l64_218(x),
        l64_219(x),
        l64_220(x),
        l64_221(x),
        l64_222(x),
        l64_223(x),
        l64_224(x),
        l64_225(x),
        l64_226(x),
        l64_227(x),
        l64_228(x),
        l64_229(x),
        l64_230(x),
        l64_231(x),
        l64_232(x),
        l64_233(x),
        l64_234(x),
        l64_235(x),
        l64_236(x),
        l64_237(x),
        l64_238(x),
        l64_239(x),
        l64_240(x),
        l64_241(x),
        l64_242(x),
        l64_243(x),
        l64_244(x),
        l64_245(x),
        l64_246(x),
        l64_247(x),
        l64_248(x),
        l64_249(x),
        l64_250(x),
        l64_251(x),
        l64_252(x),
        l64_253(x),
        l64_254(x),
        l64_255(x),
        l64_256(x),
        l64_257(x),
        l64_258(x),
        l64_259(x),
        l64_260(x),
        l64_261(x),
        l64_262(x),
        l64_263(x),
        l64_264(x),
        l64_265(x),
        l64_266(x),
        l64_267(x),
        l64_268(x),
        l64_269(x),
        l64_270(x),
        l64_271(x),
        l64_272(x),
        l64_273(x),
        l64_274(x),
        l64_275(x),
        l64_276(x),
        l64_277(x),
        l64_278(x),
        l64_279(x),
        l64_280(x),
        l64_281(x),
        l64_282(x),
        l64_283(x),
        l64_284(x),
        l64_285(x),
        l64_286(x),
        l64_287(x),
    ]