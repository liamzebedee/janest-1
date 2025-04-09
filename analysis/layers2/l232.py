import numpy as np




# Generated from reverse engineering
def l232_g(x: np.ndarray) -> np.ndarray:
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




def l232_0(x):
    # x is a list (or vector) of length 352
    return max(0, x[0])
def l232_1(x):
    # x is a list (or vector) of length 352
    return max(0, x[1])
def l232_2(x):
    # x is a list (or vector) of length 352
    return max(0, x[2])
def l232_3(x):
    # x is a list (or vector) of length 352
    return max(0, x[3])
def l232_4(x):
    # x is a list (or vector) of length 352
    return max(0, x[4])
def l232_5(x):
    # x is a list (or vector) of length 352
    return max(0, x[5])
def l232_6(x):
    # x is a list (or vector) of length 352
    return max(0, x[6])
def l232_7(x):
    # x is a list (or vector) of length 352
    return max(0, x[7])
def l232_8(x):
    # x is a list (or vector) of length 352
    return max(0, x[8])
def l232_9(x):
    # x is a list (or vector) of length 352
    return max(0, x[9])
def l232_10(x):
    # x is a list (or vector) of length 352
    return max(0, x[10])
def l232_11(x):
    # x is a list (or vector) of length 352
    return max(0, x[11])
def l232_12(x):
    # x is a list (or vector) of length 352
    return max(0, x[12])
def l232_13(x):
    # x is a list (or vector) of length 352
    return max(0, x[13])
def l232_14(x):
    # x is a list (or vector) of length 352
    return max(0, x[14])
def l232_15(x):
    # x is a list (or vector) of length 352
    return max(0, x[15])
def l232_16(x):
    # x is a list (or vector) of length 352
    return max(0, x[16])
def l232_17(x):
    # x is a list (or vector) of length 352
    return max(0, x[17])
def l232_18(x):
    # x is a list (or vector) of length 352
    return max(0, x[18])
def l232_19(x):
    # x is a list (or vector) of length 352
    return max(0, x[19])
def l232_20(x):
    # x is a list (or vector) of length 352
    return max(0, x[20])
def l232_21(x):
    # x is a list (or vector) of length 352
    return max(0, x[21])
def l232_22(x):
    # x is a list (or vector) of length 352
    return max(0, x[22])
def l232_23(x):
    # x is a list (or vector) of length 352
    return max(0, x[23])
def l232_24(x):
    # x is a list (or vector) of length 352
    return max(0, x[24])
def l232_25(x):
    # x is a list (or vector) of length 352
    return max(0, x[25])
def l232_26(x):
    # x is a list (or vector) of length 352
    return max(0, x[26])
def l232_27(x):
    # x is a list (or vector) of length 352
    return max(0, x[27])
def l232_28(x):
    # x is a list (or vector) of length 352
    return max(0, x[28])
def l232_29(x):
    # x is a list (or vector) of length 352
    return max(0, x[29])
def l232_30(x):
    # x is a list (or vector) of length 352
    return max(0, x[30])
def l232_31(x):
    # x is a list (or vector) of length 352
    return max(0, x[31])
def l232_32(x):
    # x is a list (or vector) of length 352
    return max(0, x[32])
def l232_33(x):
    # x is a list (or vector) of length 352
    return max(0, x[33])
def l232_34(x):
    # x is a list (or vector) of length 352
    return max(0, x[34])
def l232_35(x):
    # x is a list (or vector) of length 352
    return max(0, x[35])
def l232_36(x):
    # x is a list (or vector) of length 352
    return max(0, x[36])
def l232_37(x):
    # x is a list (or vector) of length 352
    return max(0, x[37])
def l232_38(x):
    # x is a list (or vector) of length 352
    return max(0, x[38])
def l232_39(x):
    # x is a list (or vector) of length 352
    return max(0, x[39])
def l232_40(x):
    # x is a list (or vector) of length 352
    return max(0, x[40])
def l232_41(x):
    # x is a list (or vector) of length 352
    return max(0, x[41])
def l232_42(x):
    # x is a list (or vector) of length 352
    return max(0, x[42])
def l232_43(x):
    # x is a list (or vector) of length 352
    return max(0, x[43])
def l232_44(x):
    # x is a list (or vector) of length 352
    return max(0, x[44])
def l232_45(x):
    # x is a list (or vector) of length 352
    return max(0, x[45])
def l232_46(x):
    # x is a list (or vector) of length 352
    return max(0, x[46])
def l232_47(x):
    # x is a list (or vector) of length 352
    return max(0, x[47])
def l232_48(x):
    # x is a list (or vector) of length 352
    return max(0, x[48])
def l232_49(x):
    # x is a list (or vector) of length 352
    return max(0, x[49])
def l232_50(x):
    # x is a list (or vector) of length 352
    return max(0, x[50])
def l232_51(x):
    # x is a list (or vector) of length 352
    return max(0, x[51])
def l232_52(x):
    # x is a list (or vector) of length 352
    return max(0, x[52])
def l232_53(x):
    # x is a list (or vector) of length 352
    return max(0, x[53])
def l232_54(x):
    # x is a list (or vector) of length 352
    return max(0, x[54])
def l232_55(x):
    # x is a list (or vector) of length 352
    return max(0, x[55])
def l232_56(x):
    # x is a list (or vector) of length 352
    return max(0, x[56])
def l232_57(x):
    # x is a list (or vector) of length 352
    return max(0, x[57])
def l232_58(x):
    # x is a list (or vector) of length 352
    return max(0, x[58])
def l232_59(x):
    # x is a list (or vector) of length 352
    return max(0, x[59])
def l232_60(x):
    # x is a list (or vector) of length 352
    return max(0, x[60])
def l232_61(x):
    # x is a list (or vector) of length 352
    return max(0, x[61])
def l232_62(x):
    # x is a list (or vector) of length 352
    return max(0, x[62])
def l232_63(x):
    # x is a list (or vector) of length 352
    return max(0, x[63])
def l232_64(x):
    # x is a list (or vector) of length 352
    return max(0, x[64])
def l232_65(x):
    # x is a list (or vector) of length 352
    return max(0, x[65])
def l232_66(x):
    # x is a list (or vector) of length 352
    return max(0, x[66])
def l232_67(x):
    # x is a list (or vector) of length 352
    return max(0, x[67])
def l232_68(x):
    # x is a list (or vector) of length 352
    return max(0, x[68])
def l232_69(x):
    # x is a list (or vector) of length 352
    return max(0, x[69])
def l232_70(x):
    # x is a list (or vector) of length 352
    return max(0, x[70])
def l232_71(x):
    # x is a list (or vector) of length 352
    return max(0, x[71])
def l232_72(x):
    # x is a list (or vector) of length 352
    return max(0, x[72])
def l232_73(x):
    # x is a list (or vector) of length 352
    return max(0, x[73])
def l232_74(x):
    # x is a list (or vector) of length 352
    return max(0, x[74])
def l232_75(x):
    # x is a list (or vector) of length 352
    return max(0, x[75])
def l232_76(x):
    # x is a list (or vector) of length 352
    return max(0, x[76])
def l232_77(x):
    # x is a list (or vector) of length 352
    return max(0, x[77])
def l232_78(x):
    # x is a list (or vector) of length 352
    return max(0, x[78])
def l232_79(x):
    # x is a list (or vector) of length 352
    return max(0, x[79])
def l232_80(x):
    # x is a list (or vector) of length 352
    return max(0, x[80])
def l232_81(x):
    # x is a list (or vector) of length 352
    return max(0, x[81])
def l232_82(x):
    # x is a list (or vector) of length 352
    return max(0, x[82])
def l232_83(x):
    # x is a list (or vector) of length 352
    return max(0, x[83])
def l232_84(x):
    # x is a list (or vector) of length 352
    return max(0, x[84])
def l232_85(x):
    # x is a list (or vector) of length 352
    return max(0, x[85])
def l232_86(x):
    # x is a list (or vector) of length 352
    return max(0, x[86])
def l232_87(x):
    # x is a list (or vector) of length 352
    return max(0, x[87])
def l232_88(x):
    # x is a list (or vector) of length 352
    return max(0, x[88])
def l232_89(x):
    # x is a list (or vector) of length 352
    return max(0, x[89])
def l232_90(x):
    # x is a list (or vector) of length 352
    return max(0, x[90])
def l232_91(x):
    # x is a list (or vector) of length 352
    return max(0, x[91])
def l232_92(x):
    # x is a list (or vector) of length 352
    return max(0, x[92])
def l232_93(x):
    # x is a list (or vector) of length 352
    return max(0, x[93])
def l232_94(x):
    # x is a list (or vector) of length 352
    return max(0, x[94])
def l232_95(x):
    # x is a list (or vector) of length 352
    return max(0, x[95])
def l232_96(x):
    # x is a list (or vector) of length 352
    return max(0, x[160])
def l232_97(x):
    # x is a list (or vector) of length 352
    return max(0, x[96] + x[161])
def l232_98(x):
    # x is a list (or vector) of length 352
    return max(0, x[97] + x[162])
def l232_99(x):
    # x is a list (or vector) of length 352
    return max(0, x[98] + x[163])
def l232_100(x):
    # x is a list (or vector) of length 352
    return max(0, x[99] + x[164])
def l232_101(x):
    # x is a list (or vector) of length 352
    return max(0, x[100] + x[165])
def l232_102(x):
    # x is a list (or vector) of length 352
    return max(0, x[101] + x[166])
def l232_103(x):
    # x is a list (or vector) of length 352
    return max(0, x[102] + x[167])
def l232_104(x):
    # x is a list (or vector) of length 352
    return max(0, x[103] + x[168])
def l232_105(x):
    # x is a list (or vector) of length 352
    return max(0, x[104] + x[169])
def l232_106(x):
    # x is a list (or vector) of length 352
    return max(0, x[105] + x[170])
def l232_107(x):
    # x is a list (or vector) of length 352
    return max(0, x[106] + x[171])
def l232_108(x):
    # x is a list (or vector) of length 352
    return max(0, x[107] + x[172])
def l232_109(x):
    # x is a list (or vector) of length 352
    return max(0, x[108] + x[173])
def l232_110(x):
    # x is a list (or vector) of length 352
    return max(0, x[109] + x[174])
def l232_111(x):
    # x is a list (or vector) of length 352
    return max(0, x[110] + x[175])
def l232_112(x):
    # x is a list (or vector) of length 352
    return max(0, x[111] + x[176])
def l232_113(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[112] + x[177] + 1.0)
def l232_114(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[113] + x[178] + 1.0)
def l232_115(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[114] + x[179] + 1.0)
def l232_116(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[115] + x[180] + 1.0)
def l232_117(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[116] + x[181] + 1.0)
def l232_118(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[117] + x[182] + 1.0)
def l232_119(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[118] + x[183] + 1.0)
def l232_120(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[119] + x[184] + 1.0)
def l232_121(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[120] + x[185] + 1.0)
def l232_122(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[121] + x[186] + 1.0)
def l232_123(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[122] + x[187] + 1.0)
def l232_124(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[123] + x[188] + 1.0)
def l232_125(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[124] + x[189] + 1.0)
def l232_126(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[125] + x[190] + 1.0)
def l232_127(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[126] + x[191] + 1.0)
def l232_128(x):
    # x is a list (or vector) of length 352
    return max(0, x[160] + -1.0)
def l232_129(x):
    # x is a list (or vector) of length 352
    return max(0, x[96] + x[161] + -1.0)
def l232_130(x):
    # x is a list (or vector) of length 352
    return max(0, x[97] + x[162] + -1.0)
def l232_131(x):
    # x is a list (or vector) of length 352
    return max(0, x[98] + x[163] + -1.0)
def l232_132(x):
    # x is a list (or vector) of length 352
    return max(0, x[99] + x[164] + -1.0)
def l232_133(x):
    # x is a list (or vector) of length 352
    return max(0, x[100] + x[165] + -1.0)
def l232_134(x):
    # x is a list (or vector) of length 352
    return max(0, x[101] + x[166] + -1.0)
def l232_135(x):
    # x is a list (or vector) of length 352
    return max(0, x[102] + x[167] + -1.0)
def l232_136(x):
    # x is a list (or vector) of length 352
    return max(0, x[103] + x[168] + -1.0)
def l232_137(x):
    # x is a list (or vector) of length 352
    return max(0, x[104] + x[169] + -1.0)
def l232_138(x):
    # x is a list (or vector) of length 352
    return max(0, x[105] + x[170] + -1.0)
def l232_139(x):
    # x is a list (or vector) of length 352
    return max(0, x[106] + x[171] + -1.0)
def l232_140(x):
    # x is a list (or vector) of length 352
    return max(0, x[107] + x[172] + -1.0)
def l232_141(x):
    # x is a list (or vector) of length 352
    return max(0, x[108] + x[173] + -1.0)
def l232_142(x):
    # x is a list (or vector) of length 352
    return max(0, x[109] + x[174] + -1.0)
def l232_143(x):
    # x is a list (or vector) of length 352
    return max(0, x[110] + x[175] + -1.0)
def l232_144(x):
    # x is a list (or vector) of length 352
    return max(0, x[111] + x[176] + -1.0)
def l232_145(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[112] + x[177])
def l232_146(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[113] + x[178])
def l232_147(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[114] + x[179])
def l232_148(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[115] + x[180])
def l232_149(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[116] + x[181])
def l232_150(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[117] + x[182])
def l232_151(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[118] + x[183])
def l232_152(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[119] + x[184])
def l232_153(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[120] + x[185])
def l232_154(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[121] + x[186])
def l232_155(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[122] + x[187])
def l232_156(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[123] + x[188])
def l232_157(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[124] + x[189])
def l232_158(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[125] + x[190])
def l232_159(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[126] + x[191])
def l232_160(x):
    # x is a list (or vector) of length 352
    return max(0, x[192] + -2.0*x[224])
def l232_161(x):
    # x is a list (or vector) of length 352
    return max(0, x[193] + -2.0*x[225])
def l232_162(x):
    # x is a list (or vector) of length 352
    return max(0, x[194] + -2.0*x[226])
def l232_163(x):
    # x is a list (or vector) of length 352
    return max(0, x[195] + -2.0*x[227])
def l232_164(x):
    # x is a list (or vector) of length 352
    return max(0, x[196] + -2.0*x[228])
def l232_165(x):
    # x is a list (or vector) of length 352
    return max(0, x[197] + -2.0*x[229])
def l232_166(x):
    # x is a list (or vector) of length 352
    return max(0, x[198] + -2.0*x[230])
def l232_167(x):
    # x is a list (or vector) of length 352
    return max(0, x[199] + -2.0*x[231])
def l232_168(x):
    # x is a list (or vector) of length 352
    return max(0, x[200] + -2.0*x[232])
def l232_169(x):
    # x is a list (or vector) of length 352
    return max(0, x[201] + -2.0*x[233])
def l232_170(x):
    # x is a list (or vector) of length 352
    return max(0, x[202] + -2.0*x[234])
def l232_171(x):
    # x is a list (or vector) of length 352
    return max(0, x[203] + -2.0*x[235])
def l232_172(x):
    # x is a list (or vector) of length 352
    return max(0, x[204] + -2.0*x[236])
def l232_173(x):
    # x is a list (or vector) of length 352
    return max(0, x[205] + -2.0*x[237])
def l232_174(x):
    # x is a list (or vector) of length 352
    return max(0, x[206] + -2.0*x[238])
def l232_175(x):
    # x is a list (or vector) of length 352
    return max(0, x[207] + -2.0*x[239])
def l232_176(x):
    # x is a list (or vector) of length 352
    return max(0, x[208] + -2.0*x[240])
def l232_177(x):
    # x is a list (or vector) of length 352
    return max(0, x[209] + -2.0*x[241])
def l232_178(x):
    # x is a list (or vector) of length 352
    return max(0, x[210] + -2.0*x[242])
def l232_179(x):
    # x is a list (or vector) of length 352
    return max(0, x[211] + -2.0*x[243])
def l232_180(x):
    # x is a list (or vector) of length 352
    return max(0, x[212] + -2.0*x[244])
def l232_181(x):
    # x is a list (or vector) of length 352
    return max(0, x[213] + -2.0*x[245])
def l232_182(x):
    # x is a list (or vector) of length 352
    return max(0, x[214] + -2.0*x[246])
def l232_183(x):
    # x is a list (or vector) of length 352
    return max(0, x[215] + -2.0*x[247])
def l232_184(x):
    # x is a list (or vector) of length 352
    return max(0, x[216] + -2.0*x[248])
def l232_185(x):
    # x is a list (or vector) of length 352
    return max(0, x[217] + -2.0*x[249])
def l232_186(x):
    # x is a list (or vector) of length 352
    return max(0, x[218] + -2.0*x[250])
def l232_187(x):
    # x is a list (or vector) of length 352
    return max(0, x[219] + -2.0*x[251])
def l232_188(x):
    # x is a list (or vector) of length 352
    return max(0, x[220] + -2.0*x[252])
def l232_189(x):
    # x is a list (or vector) of length 352
    return max(0, x[221] + -2.0*x[253])
def l232_190(x):
    # x is a list (or vector) of length 352
    return max(0, x[222] + -2.0*x[254])
def l232_191(x):
    # x is a list (or vector) of length 352
    return max(0, x[223] + -2.0*x[255])
def l232_192(x):
    # x is a list (or vector) of length 352
    return max(0, x[256])
def l232_193(x):
    # x is a list (or vector) of length 352
    return max(0, x[257])
def l232_194(x):
    # x is a list (or vector) of length 352
    return max(0, x[258])
def l232_195(x):
    # x is a list (or vector) of length 352
    return max(0, x[259])
def l232_196(x):
    # x is a list (or vector) of length 352
    return max(0, x[260])
def l232_197(x):
    # x is a list (or vector) of length 352
    return max(0, x[261])
def l232_198(x):
    # x is a list (or vector) of length 352
    return max(0, x[262])
def l232_199(x):
    # x is a list (or vector) of length 352
    return max(0, x[263])
def l232_200(x):
    # x is a list (or vector) of length 352
    return max(0, x[264])
def l232_201(x):
    # x is a list (or vector) of length 352
    return max(0, x[265])
def l232_202(x):
    # x is a list (or vector) of length 352
    return max(0, x[266])
def l232_203(x):
    # x is a list (or vector) of length 352
    return max(0, x[267])
def l232_204(x):
    # x is a list (or vector) of length 352
    return max(0, x[268])
def l232_205(x):
    # x is a list (or vector) of length 352
    return max(0, x[269])
def l232_206(x):
    # x is a list (or vector) of length 352
    return max(0, x[270])
def l232_207(x):
    # x is a list (or vector) of length 352
    return max(0, x[271])
def l232_208(x):
    # x is a list (or vector) of length 352
    return max(0, x[272])
def l232_209(x):
    # x is a list (or vector) of length 352
    return max(0, x[273])
def l232_210(x):
    # x is a list (or vector) of length 352
    return max(0, x[274])
def l232_211(x):
    # x is a list (or vector) of length 352
    return max(0, x[275])
def l232_212(x):
    # x is a list (or vector) of length 352
    return max(0, x[276])
def l232_213(x):
    # x is a list (or vector) of length 352
    return max(0, x[277])
def l232_214(x):
    # x is a list (or vector) of length 352
    return max(0, x[278])
def l232_215(x):
    # x is a list (or vector) of length 352
    return max(0, x[279])
def l232_216(x):
    # x is a list (or vector) of length 352
    return max(0, x[280])
def l232_217(x):
    # x is a list (or vector) of length 352
    return max(0, x[281])
def l232_218(x):
    # x is a list (or vector) of length 352
    return max(0, x[282])
def l232_219(x):
    # x is a list (or vector) of length 352
    return max(0, x[283])
def l232_220(x):
    # x is a list (or vector) of length 352
    return max(0, x[284])
def l232_221(x):
    # x is a list (or vector) of length 352
    return max(0, x[285])
def l232_222(x):
    # x is a list (or vector) of length 352
    return max(0, x[286])
def l232_223(x):
    # x is a list (or vector) of length 352
    return max(0, x[287])
def l232_224(x):
    # x is a list (or vector) of length 352
    return max(0, x[288])
def l232_225(x):
    # x is a list (or vector) of length 352
    return max(0, x[289])
def l232_226(x):
    # x is a list (or vector) of length 352
    return max(0, x[290])
def l232_227(x):
    # x is a list (or vector) of length 352
    return max(0, x[291])
def l232_228(x):
    # x is a list (or vector) of length 352
    return max(0, x[292])
def l232_229(x):
    # x is a list (or vector) of length 352
    return max(0, x[293])
def l232_230(x):
    # x is a list (or vector) of length 352
    return max(0, x[294])
def l232_231(x):
    # x is a list (or vector) of length 352
    return max(0, x[295])
def l232_232(x):
    # x is a list (or vector) of length 352
    return max(0, x[296])
def l232_233(x):
    # x is a list (or vector) of length 352
    return max(0, x[297])
def l232_234(x):
    # x is a list (or vector) of length 352
    return max(0, x[298])
def l232_235(x):
    # x is a list (or vector) of length 352
    return max(0, x[299])
def l232_236(x):
    # x is a list (or vector) of length 352
    return max(0, x[300])
def l232_237(x):
    # x is a list (or vector) of length 352
    return max(0, x[301])
def l232_238(x):
    # x is a list (or vector) of length 352
    return max(0, x[302])
def l232_239(x):
    # x is a list (or vector) of length 352
    return max(0, x[303])
def l232_240(x):
    # x is a list (or vector) of length 352
    return max(0, x[304])
def l232_241(x):
    # x is a list (or vector) of length 352
    return max(0, x[305])
def l232_242(x):
    # x is a list (or vector) of length 352
    return max(0, x[306])
def l232_243(x):
    # x is a list (or vector) of length 352
    return max(0, x[307])
def l232_244(x):
    # x is a list (or vector) of length 352
    return max(0, x[308])
def l232_245(x):
    # x is a list (or vector) of length 352
    return max(0, x[309])
def l232_246(x):
    # x is a list (or vector) of length 352
    return max(0, x[310])
def l232_247(x):
    # x is a list (or vector) of length 352
    return max(0, x[311])
def l232_248(x):
    # x is a list (or vector) of length 352
    return max(0, x[312])
def l232_249(x):
    # x is a list (or vector) of length 352
    return max(0, x[313])
def l232_250(x):
    # x is a list (or vector) of length 352
    return max(0, x[314])
def l232_251(x):
    # x is a list (or vector) of length 352
    return max(0, x[315])
def l232_252(x):
    # x is a list (or vector) of length 352
    return max(0, x[316])
def l232_253(x):
    # x is a list (or vector) of length 352
    return max(0, x[317])
def l232_254(x):
    # x is a list (or vector) of length 352
    return max(0, x[318])
def l232_255(x):
    # x is a list (or vector) of length 352
    return max(0, x[319])
def l232_256(x):
    # x is a list (or vector) of length 352
    return max(0, x[320])
def l232_257(x):
    # x is a list (or vector) of length 352
    return max(0, x[321])
def l232_258(x):
    # x is a list (or vector) of length 352
    return max(0, x[322])
def l232_259(x):
    # x is a list (or vector) of length 352
    return max(0, x[323])
def l232_260(x):
    # x is a list (or vector) of length 352
    return max(0, x[324])
def l232_261(x):
    # x is a list (or vector) of length 352
    return max(0, x[325])
def l232_262(x):
    # x is a list (or vector) of length 352
    return max(0, x[326])
def l232_263(x):
    # x is a list (or vector) of length 352
    return max(0, x[327])
def l232_264(x):
    # x is a list (or vector) of length 352
    return max(0, x[328])
def l232_265(x):
    # x is a list (or vector) of length 352
    return max(0, x[329])
def l232_266(x):
    # x is a list (or vector) of length 352
    return max(0, x[330])
def l232_267(x):
    # x is a list (or vector) of length 352
    return max(0, x[331])
def l232_268(x):
    # x is a list (or vector) of length 352
    return max(0, x[332])
def l232_269(x):
    # x is a list (or vector) of length 352
    return max(0, x[333])
def l232_270(x):
    # x is a list (or vector) of length 352
    return max(0, x[334])
def l232_271(x):
    # x is a list (or vector) of length 352
    return max(0, x[335])
def l232_272(x):
    # x is a list (or vector) of length 352
    return max(0, x[336])
def l232_273(x):
    # x is a list (or vector) of length 352
    return max(0, x[337])
def l232_274(x):
    # x is a list (or vector) of length 352
    return max(0, x[338])
def l232_275(x):
    # x is a list (or vector) of length 352
    return max(0, x[339])
def l232_276(x):
    # x is a list (or vector) of length 352
    return max(0, x[340])
def l232_277(x):
    # x is a list (or vector) of length 352
    return max(0, x[341])
def l232_278(x):
    # x is a list (or vector) of length 352
    return max(0, x[342])
def l232_279(x):
    # x is a list (or vector) of length 352
    return max(0, x[343])
def l232_280(x):
    # x is a list (or vector) of length 352
    return max(0, x[344])
def l232_281(x):
    # x is a list (or vector) of length 352
    return max(0, x[345])
def l232_282(x):
    # x is a list (or vector) of length 352
    return max(0, x[346])
def l232_283(x):
    # x is a list (or vector) of length 352
    return max(0, x[347])
def l232_284(x):
    # x is a list (or vector) of length 352
    return max(0, x[348])
def l232_285(x):
    # x is a list (or vector) of length 352
    return max(0, x[349])
def l232_286(x):
    # x is a list (or vector) of length 352
    return max(0, x[350])
def l232_287(x):
    # x is a list (or vector) of length 352
    return max(0, x[351])
def l232_(x):
    # x is a list (or vector) of length 352
    return [
        l232_0(x),
        l232_1(x),
        l232_2(x),
        l232_3(x),
        l232_4(x),
        l232_5(x),
        l232_6(x),
        l232_7(x),
        l232_8(x),
        l232_9(x),
        l232_10(x),
        l232_11(x),
        l232_12(x),
        l232_13(x),
        l232_14(x),
        l232_15(x),
        l232_16(x),
        l232_17(x),
        l232_18(x),
        l232_19(x),
        l232_20(x),
        l232_21(x),
        l232_22(x),
        l232_23(x),
        l232_24(x),
        l232_25(x),
        l232_26(x),
        l232_27(x),
        l232_28(x),
        l232_29(x),
        l232_30(x),
        l232_31(x),
        l232_32(x),
        l232_33(x),
        l232_34(x),
        l232_35(x),
        l232_36(x),
        l232_37(x),
        l232_38(x),
        l232_39(x),
        l232_40(x),
        l232_41(x),
        l232_42(x),
        l232_43(x),
        l232_44(x),
        l232_45(x),
        l232_46(x),
        l232_47(x),
        l232_48(x),
        l232_49(x),
        l232_50(x),
        l232_51(x),
        l232_52(x),
        l232_53(x),
        l232_54(x),
        l232_55(x),
        l232_56(x),
        l232_57(x),
        l232_58(x),
        l232_59(x),
        l232_60(x),
        l232_61(x),
        l232_62(x),
        l232_63(x),
        l232_64(x),
        l232_65(x),
        l232_66(x),
        l232_67(x),
        l232_68(x),
        l232_69(x),
        l232_70(x),
        l232_71(x),
        l232_72(x),
        l232_73(x),
        l232_74(x),
        l232_75(x),
        l232_76(x),
        l232_77(x),
        l232_78(x),
        l232_79(x),
        l232_80(x),
        l232_81(x),
        l232_82(x),
        l232_83(x),
        l232_84(x),
        l232_85(x),
        l232_86(x),
        l232_87(x),
        l232_88(x),
        l232_89(x),
        l232_90(x),
        l232_91(x),
        l232_92(x),
        l232_93(x),
        l232_94(x),
        l232_95(x),
        l232_96(x),
        l232_97(x),
        l232_98(x),
        l232_99(x),
        l232_100(x),
        l232_101(x),
        l232_102(x),
        l232_103(x),
        l232_104(x),
        l232_105(x),
        l232_106(x),
        l232_107(x),
        l232_108(x),
        l232_109(x),
        l232_110(x),
        l232_111(x),
        l232_112(x),
        l232_113(x),
        l232_114(x),
        l232_115(x),
        l232_116(x),
        l232_117(x),
        l232_118(x),
        l232_119(x),
        l232_120(x),
        l232_121(x),
        l232_122(x),
        l232_123(x),
        l232_124(x),
        l232_125(x),
        l232_126(x),
        l232_127(x),
        l232_128(x),
        l232_129(x),
        l232_130(x),
        l232_131(x),
        l232_132(x),
        l232_133(x),
        l232_134(x),
        l232_135(x),
        l232_136(x),
        l232_137(x),
        l232_138(x),
        l232_139(x),
        l232_140(x),
        l232_141(x),
        l232_142(x),
        l232_143(x),
        l232_144(x),
        l232_145(x),
        l232_146(x),
        l232_147(x),
        l232_148(x),
        l232_149(x),
        l232_150(x),
        l232_151(x),
        l232_152(x),
        l232_153(x),
        l232_154(x),
        l232_155(x),
        l232_156(x),
        l232_157(x),
        l232_158(x),
        l232_159(x),
        l232_160(x),
        l232_161(x),
        l232_162(x),
        l232_163(x),
        l232_164(x),
        l232_165(x),
        l232_166(x),
        l232_167(x),
        l232_168(x),
        l232_169(x),
        l232_170(x),
        l232_171(x),
        l232_172(x),
        l232_173(x),
        l232_174(x),
        l232_175(x),
        l232_176(x),
        l232_177(x),
        l232_178(x),
        l232_179(x),
        l232_180(x),
        l232_181(x),
        l232_182(x),
        l232_183(x),
        l232_184(x),
        l232_185(x),
        l232_186(x),
        l232_187(x),
        l232_188(x),
        l232_189(x),
        l232_190(x),
        l232_191(x),
        l232_192(x),
        l232_193(x),
        l232_194(x),
        l232_195(x),
        l232_196(x),
        l232_197(x),
        l232_198(x),
        l232_199(x),
        l232_200(x),
        l232_201(x),
        l232_202(x),
        l232_203(x),
        l232_204(x),
        l232_205(x),
        l232_206(x),
        l232_207(x),
        l232_208(x),
        l232_209(x),
        l232_210(x),
        l232_211(x),
        l232_212(x),
        l232_213(x),
        l232_214(x),
        l232_215(x),
        l232_216(x),
        l232_217(x),
        l232_218(x),
        l232_219(x),
        l232_220(x),
        l232_221(x),
        l232_222(x),
        l232_223(x),
        l232_224(x),
        l232_225(x),
        l232_226(x),
        l232_227(x),
        l232_228(x),
        l232_229(x),
        l232_230(x),
        l232_231(x),
        l232_232(x),
        l232_233(x),
        l232_234(x),
        l232_235(x),
        l232_236(x),
        l232_237(x),
        l232_238(x),
        l232_239(x),
        l232_240(x),
        l232_241(x),
        l232_242(x),
        l232_243(x),
        l232_244(x),
        l232_245(x),
        l232_246(x),
        l232_247(x),
        l232_248(x),
        l232_249(x),
        l232_250(x),
        l232_251(x),
        l232_252(x),
        l232_253(x),
        l232_254(x),
        l232_255(x),
        l232_256(x),
        l232_257(x),
        l232_258(x),
        l232_259(x),
        l232_260(x),
        l232_261(x),
        l232_262(x),
        l232_263(x),
        l232_264(x),
        l232_265(x),
        l232_266(x),
        l232_267(x),
        l232_268(x),
        l232_269(x),
        l232_270(x),
        l232_271(x),
        l232_272(x),
        l232_273(x),
        l232_274(x),
        l232_275(x),
        l232_276(x),
        l232_277(x),
        l232_278(x),
        l232_279(x),
        l232_280(x),
        l232_281(x),
        l232_282(x),
        l232_283(x),
        l232_284(x),
        l232_285(x),
        l232_286(x),
        l232_287(x),
    ]