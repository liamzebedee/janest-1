import numpy as np




# Generated from reverse engineering
def l316_g(x: np.ndarray) -> np.ndarray:
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




def l316_0(x):
    # x is a list (or vector) of length 352
    return max(0, x[0])
def l316_1(x):
    # x is a list (or vector) of length 352
    return max(0, x[1])
def l316_2(x):
    # x is a list (or vector) of length 352
    return max(0, x[2])
def l316_3(x):
    # x is a list (or vector) of length 352
    return max(0, x[3])
def l316_4(x):
    # x is a list (or vector) of length 352
    return max(0, x[4])
def l316_5(x):
    # x is a list (or vector) of length 352
    return max(0, x[5])
def l316_6(x):
    # x is a list (or vector) of length 352
    return max(0, x[6])
def l316_7(x):
    # x is a list (or vector) of length 352
    return max(0, x[7])
def l316_8(x):
    # x is a list (or vector) of length 352
    return max(0, x[8])
def l316_9(x):
    # x is a list (or vector) of length 352
    return max(0, x[9])
def l316_10(x):
    # x is a list (or vector) of length 352
    return max(0, x[10])
def l316_11(x):
    # x is a list (or vector) of length 352
    return max(0, x[11])
def l316_12(x):
    # x is a list (or vector) of length 352
    return max(0, x[12])
def l316_13(x):
    # x is a list (or vector) of length 352
    return max(0, x[13])
def l316_14(x):
    # x is a list (or vector) of length 352
    return max(0, x[14])
def l316_15(x):
    # x is a list (or vector) of length 352
    return max(0, x[15])
def l316_16(x):
    # x is a list (or vector) of length 352
    return max(0, x[16])
def l316_17(x):
    # x is a list (or vector) of length 352
    return max(0, x[17])
def l316_18(x):
    # x is a list (or vector) of length 352
    return max(0, x[18])
def l316_19(x):
    # x is a list (or vector) of length 352
    return max(0, x[19])
def l316_20(x):
    # x is a list (or vector) of length 352
    return max(0, x[20])
def l316_21(x):
    # x is a list (or vector) of length 352
    return max(0, x[21])
def l316_22(x):
    # x is a list (or vector) of length 352
    return max(0, x[22])
def l316_23(x):
    # x is a list (or vector) of length 352
    return max(0, x[23])
def l316_24(x):
    # x is a list (or vector) of length 352
    return max(0, x[24])
def l316_25(x):
    # x is a list (or vector) of length 352
    return max(0, x[25])
def l316_26(x):
    # x is a list (or vector) of length 352
    return max(0, x[26])
def l316_27(x):
    # x is a list (or vector) of length 352
    return max(0, x[27])
def l316_28(x):
    # x is a list (or vector) of length 352
    return max(0, x[28])
def l316_29(x):
    # x is a list (or vector) of length 352
    return max(0, x[29])
def l316_30(x):
    # x is a list (or vector) of length 352
    return max(0, x[30])
def l316_31(x):
    # x is a list (or vector) of length 352
    return max(0, x[31])
def l316_32(x):
    # x is a list (or vector) of length 352
    return max(0, x[32])
def l316_33(x):
    # x is a list (or vector) of length 352
    return max(0, x[33])
def l316_34(x):
    # x is a list (or vector) of length 352
    return max(0, x[34])
def l316_35(x):
    # x is a list (or vector) of length 352
    return max(0, x[35])
def l316_36(x):
    # x is a list (or vector) of length 352
    return max(0, x[36])
def l316_37(x):
    # x is a list (or vector) of length 352
    return max(0, x[37])
def l316_38(x):
    # x is a list (or vector) of length 352
    return max(0, x[38])
def l316_39(x):
    # x is a list (or vector) of length 352
    return max(0, x[39])
def l316_40(x):
    # x is a list (or vector) of length 352
    return max(0, x[40])
def l316_41(x):
    # x is a list (or vector) of length 352
    return max(0, x[41])
def l316_42(x):
    # x is a list (or vector) of length 352
    return max(0, x[42])
def l316_43(x):
    # x is a list (or vector) of length 352
    return max(0, x[43])
def l316_44(x):
    # x is a list (or vector) of length 352
    return max(0, x[44])
def l316_45(x):
    # x is a list (or vector) of length 352
    return max(0, x[45])
def l316_46(x):
    # x is a list (or vector) of length 352
    return max(0, x[46])
def l316_47(x):
    # x is a list (or vector) of length 352
    return max(0, x[47])
def l316_48(x):
    # x is a list (or vector) of length 352
    return max(0, x[48])
def l316_49(x):
    # x is a list (or vector) of length 352
    return max(0, x[49])
def l316_50(x):
    # x is a list (or vector) of length 352
    return max(0, x[50])
def l316_51(x):
    # x is a list (or vector) of length 352
    return max(0, x[51])
def l316_52(x):
    # x is a list (or vector) of length 352
    return max(0, x[52])
def l316_53(x):
    # x is a list (or vector) of length 352
    return max(0, x[53])
def l316_54(x):
    # x is a list (or vector) of length 352
    return max(0, x[54])
def l316_55(x):
    # x is a list (or vector) of length 352
    return max(0, x[55])
def l316_56(x):
    # x is a list (or vector) of length 352
    return max(0, x[56])
def l316_57(x):
    # x is a list (or vector) of length 352
    return max(0, x[57])
def l316_58(x):
    # x is a list (or vector) of length 352
    return max(0, x[58])
def l316_59(x):
    # x is a list (or vector) of length 352
    return max(0, x[59])
def l316_60(x):
    # x is a list (or vector) of length 352
    return max(0, x[60])
def l316_61(x):
    # x is a list (or vector) of length 352
    return max(0, x[61])
def l316_62(x):
    # x is a list (or vector) of length 352
    return max(0, x[62])
def l316_63(x):
    # x is a list (or vector) of length 352
    return max(0, x[63])
def l316_64(x):
    # x is a list (or vector) of length 352
    return max(0, x[64])
def l316_65(x):
    # x is a list (or vector) of length 352
    return max(0, x[65])
def l316_66(x):
    # x is a list (or vector) of length 352
    return max(0, x[66])
def l316_67(x):
    # x is a list (or vector) of length 352
    return max(0, x[67])
def l316_68(x):
    # x is a list (or vector) of length 352
    return max(0, x[68])
def l316_69(x):
    # x is a list (or vector) of length 352
    return max(0, x[69])
def l316_70(x):
    # x is a list (or vector) of length 352
    return max(0, x[70])
def l316_71(x):
    # x is a list (or vector) of length 352
    return max(0, x[71])
def l316_72(x):
    # x is a list (or vector) of length 352
    return max(0, x[72])
def l316_73(x):
    # x is a list (or vector) of length 352
    return max(0, x[73])
def l316_74(x):
    # x is a list (or vector) of length 352
    return max(0, x[74])
def l316_75(x):
    # x is a list (or vector) of length 352
    return max(0, x[75])
def l316_76(x):
    # x is a list (or vector) of length 352
    return max(0, x[76])
def l316_77(x):
    # x is a list (or vector) of length 352
    return max(0, x[77])
def l316_78(x):
    # x is a list (or vector) of length 352
    return max(0, x[78])
def l316_79(x):
    # x is a list (or vector) of length 352
    return max(0, x[79])
def l316_80(x):
    # x is a list (or vector) of length 352
    return max(0, x[80])
def l316_81(x):
    # x is a list (or vector) of length 352
    return max(0, x[81])
def l316_82(x):
    # x is a list (or vector) of length 352
    return max(0, x[82])
def l316_83(x):
    # x is a list (or vector) of length 352
    return max(0, x[83])
def l316_84(x):
    # x is a list (or vector) of length 352
    return max(0, x[84])
def l316_85(x):
    # x is a list (or vector) of length 352
    return max(0, x[85])
def l316_86(x):
    # x is a list (or vector) of length 352
    return max(0, x[86])
def l316_87(x):
    # x is a list (or vector) of length 352
    return max(0, x[87])
def l316_88(x):
    # x is a list (or vector) of length 352
    return max(0, x[88])
def l316_89(x):
    # x is a list (or vector) of length 352
    return max(0, x[89])
def l316_90(x):
    # x is a list (or vector) of length 352
    return max(0, x[90])
def l316_91(x):
    # x is a list (or vector) of length 352
    return max(0, x[91])
def l316_92(x):
    # x is a list (or vector) of length 352
    return max(0, x[92])
def l316_93(x):
    # x is a list (or vector) of length 352
    return max(0, x[93])
def l316_94(x):
    # x is a list (or vector) of length 352
    return max(0, x[94])
def l316_95(x):
    # x is a list (or vector) of length 352
    return max(0, x[95])
def l316_96(x):
    # x is a list (or vector) of length 352
    return max(0, x[160])
def l316_97(x):
    # x is a list (or vector) of length 352
    return max(0, x[96] + x[161])
def l316_98(x):
    # x is a list (or vector) of length 352
    return max(0, x[97] + x[162])
def l316_99(x):
    # x is a list (or vector) of length 352
    return max(0, x[98] + x[163])
def l316_100(x):
    # x is a list (or vector) of length 352
    return max(0, x[99] + x[164])
def l316_101(x):
    # x is a list (or vector) of length 352
    return max(0, x[100] + x[165])
def l316_102(x):
    # x is a list (or vector) of length 352
    return max(0, x[101] + x[166])
def l316_103(x):
    # x is a list (or vector) of length 352
    return max(0, x[102] + x[167])
def l316_104(x):
    # x is a list (or vector) of length 352
    return max(0, x[103] + x[168])
def l316_105(x):
    # x is a list (or vector) of length 352
    return max(0, x[104] + x[169])
def l316_106(x):
    # x is a list (or vector) of length 352
    return max(0, x[105] + x[170])
def l316_107(x):
    # x is a list (or vector) of length 352
    return max(0, x[106] + x[171])
def l316_108(x):
    # x is a list (or vector) of length 352
    return max(0, x[107] + x[172])
def l316_109(x):
    # x is a list (or vector) of length 352
    return max(0, x[108] + x[173])
def l316_110(x):
    # x is a list (or vector) of length 352
    return max(0, x[109] + x[174])
def l316_111(x):
    # x is a list (or vector) of length 352
    return max(0, x[110] + x[175])
def l316_112(x):
    # x is a list (or vector) of length 352
    return max(0, x[111] + x[176])
def l316_113(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[112] + x[177] + 1.0)
def l316_114(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[113] + x[178] + 1.0)
def l316_115(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[114] + x[179] + 1.0)
def l316_116(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[115] + x[180] + 1.0)
def l316_117(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[116] + x[181] + 1.0)
def l316_118(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[117] + x[182] + 1.0)
def l316_119(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[118] + x[183] + 1.0)
def l316_120(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[119] + x[184] + 1.0)
def l316_121(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[120] + x[185] + 1.0)
def l316_122(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[121] + x[186] + 1.0)
def l316_123(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[122] + x[187] + 1.0)
def l316_124(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[123] + x[188] + 1.0)
def l316_125(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[124] + x[189] + 1.0)
def l316_126(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[125] + x[190] + 1.0)
def l316_127(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[126] + x[191] + 1.0)
def l316_128(x):
    # x is a list (or vector) of length 352
    return max(0, x[160] + -1.0)
def l316_129(x):
    # x is a list (or vector) of length 352
    return max(0, x[96] + x[161] + -1.0)
def l316_130(x):
    # x is a list (or vector) of length 352
    return max(0, x[97] + x[162] + -1.0)
def l316_131(x):
    # x is a list (or vector) of length 352
    return max(0, x[98] + x[163] + -1.0)
def l316_132(x):
    # x is a list (or vector) of length 352
    return max(0, x[99] + x[164] + -1.0)
def l316_133(x):
    # x is a list (or vector) of length 352
    return max(0, x[100] + x[165] + -1.0)
def l316_134(x):
    # x is a list (or vector) of length 352
    return max(0, x[101] + x[166] + -1.0)
def l316_135(x):
    # x is a list (or vector) of length 352
    return max(0, x[102] + x[167] + -1.0)
def l316_136(x):
    # x is a list (or vector) of length 352
    return max(0, x[103] + x[168] + -1.0)
def l316_137(x):
    # x is a list (or vector) of length 352
    return max(0, x[104] + x[169] + -1.0)
def l316_138(x):
    # x is a list (or vector) of length 352
    return max(0, x[105] + x[170] + -1.0)
def l316_139(x):
    # x is a list (or vector) of length 352
    return max(0, x[106] + x[171] + -1.0)
def l316_140(x):
    # x is a list (or vector) of length 352
    return max(0, x[107] + x[172] + -1.0)
def l316_141(x):
    # x is a list (or vector) of length 352
    return max(0, x[108] + x[173] + -1.0)
def l316_142(x):
    # x is a list (or vector) of length 352
    return max(0, x[109] + x[174] + -1.0)
def l316_143(x):
    # x is a list (or vector) of length 352
    return max(0, x[110] + x[175] + -1.0)
def l316_144(x):
    # x is a list (or vector) of length 352
    return max(0, x[111] + x[176] + -1.0)
def l316_145(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[112] + x[177])
def l316_146(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[113] + x[178])
def l316_147(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[114] + x[179])
def l316_148(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[115] + x[180])
def l316_149(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[116] + x[181])
def l316_150(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[117] + x[182])
def l316_151(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[118] + x[183])
def l316_152(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[119] + x[184])
def l316_153(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[120] + x[185])
def l316_154(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[121] + x[186])
def l316_155(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[122] + x[187])
def l316_156(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[123] + x[188])
def l316_157(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[124] + x[189])
def l316_158(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[125] + x[190])
def l316_159(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[126] + x[191])
def l316_160(x):
    # x is a list (or vector) of length 352
    return max(0, x[192] + -2.0*x[224])
def l316_161(x):
    # x is a list (or vector) of length 352
    return max(0, x[193] + -2.0*x[225])
def l316_162(x):
    # x is a list (or vector) of length 352
    return max(0, x[194] + -2.0*x[226])
def l316_163(x):
    # x is a list (or vector) of length 352
    return max(0, x[195] + -2.0*x[227])
def l316_164(x):
    # x is a list (or vector) of length 352
    return max(0, x[196] + -2.0*x[228])
def l316_165(x):
    # x is a list (or vector) of length 352
    return max(0, x[197] + -2.0*x[229])
def l316_166(x):
    # x is a list (or vector) of length 352
    return max(0, x[198] + -2.0*x[230])
def l316_167(x):
    # x is a list (or vector) of length 352
    return max(0, x[199] + -2.0*x[231])
def l316_168(x):
    # x is a list (or vector) of length 352
    return max(0, x[200] + -2.0*x[232])
def l316_169(x):
    # x is a list (or vector) of length 352
    return max(0, x[201] + -2.0*x[233])
def l316_170(x):
    # x is a list (or vector) of length 352
    return max(0, x[202] + -2.0*x[234])
def l316_171(x):
    # x is a list (or vector) of length 352
    return max(0, x[203] + -2.0*x[235])
def l316_172(x):
    # x is a list (or vector) of length 352
    return max(0, x[204] + -2.0*x[236])
def l316_173(x):
    # x is a list (or vector) of length 352
    return max(0, x[205] + -2.0*x[237])
def l316_174(x):
    # x is a list (or vector) of length 352
    return max(0, x[206] + -2.0*x[238])
def l316_175(x):
    # x is a list (or vector) of length 352
    return max(0, x[207] + -2.0*x[239])
def l316_176(x):
    # x is a list (or vector) of length 352
    return max(0, x[208] + -2.0*x[240])
def l316_177(x):
    # x is a list (or vector) of length 352
    return max(0, x[209] + -2.0*x[241])
def l316_178(x):
    # x is a list (or vector) of length 352
    return max(0, x[210] + -2.0*x[242])
def l316_179(x):
    # x is a list (or vector) of length 352
    return max(0, x[211] + -2.0*x[243])
def l316_180(x):
    # x is a list (or vector) of length 352
    return max(0, x[212] + -2.0*x[244])
def l316_181(x):
    # x is a list (or vector) of length 352
    return max(0, x[213] + -2.0*x[245])
def l316_182(x):
    # x is a list (or vector) of length 352
    return max(0, x[214] + -2.0*x[246])
def l316_183(x):
    # x is a list (or vector) of length 352
    return max(0, x[215] + -2.0*x[247])
def l316_184(x):
    # x is a list (or vector) of length 352
    return max(0, x[216] + -2.0*x[248])
def l316_185(x):
    # x is a list (or vector) of length 352
    return max(0, x[217] + -2.0*x[249])
def l316_186(x):
    # x is a list (or vector) of length 352
    return max(0, x[218] + -2.0*x[250])
def l316_187(x):
    # x is a list (or vector) of length 352
    return max(0, x[219] + -2.0*x[251])
def l316_188(x):
    # x is a list (or vector) of length 352
    return max(0, x[220] + -2.0*x[252])
def l316_189(x):
    # x is a list (or vector) of length 352
    return max(0, x[221] + -2.0*x[253])
def l316_190(x):
    # x is a list (or vector) of length 352
    return max(0, x[222] + -2.0*x[254])
def l316_191(x):
    # x is a list (or vector) of length 352
    return max(0, x[223] + -2.0*x[255])
def l316_192(x):
    # x is a list (or vector) of length 352
    return max(0, x[256])
def l316_193(x):
    # x is a list (or vector) of length 352
    return max(0, x[257])
def l316_194(x):
    # x is a list (or vector) of length 352
    return max(0, x[258])
def l316_195(x):
    # x is a list (or vector) of length 352
    return max(0, x[259])
def l316_196(x):
    # x is a list (or vector) of length 352
    return max(0, x[260])
def l316_197(x):
    # x is a list (or vector) of length 352
    return max(0, x[261])
def l316_198(x):
    # x is a list (or vector) of length 352
    return max(0, x[262])
def l316_199(x):
    # x is a list (or vector) of length 352
    return max(0, x[263])
def l316_200(x):
    # x is a list (or vector) of length 352
    return max(0, x[264])
def l316_201(x):
    # x is a list (or vector) of length 352
    return max(0, x[265])
def l316_202(x):
    # x is a list (or vector) of length 352
    return max(0, x[266])
def l316_203(x):
    # x is a list (or vector) of length 352
    return max(0, x[267])
def l316_204(x):
    # x is a list (or vector) of length 352
    return max(0, x[268])
def l316_205(x):
    # x is a list (or vector) of length 352
    return max(0, x[269])
def l316_206(x):
    # x is a list (or vector) of length 352
    return max(0, x[270])
def l316_207(x):
    # x is a list (or vector) of length 352
    return max(0, x[271])
def l316_208(x):
    # x is a list (or vector) of length 352
    return max(0, x[272])
def l316_209(x):
    # x is a list (or vector) of length 352
    return max(0, x[273])
def l316_210(x):
    # x is a list (or vector) of length 352
    return max(0, x[274])
def l316_211(x):
    # x is a list (or vector) of length 352
    return max(0, x[275])
def l316_212(x):
    # x is a list (or vector) of length 352
    return max(0, x[276])
def l316_213(x):
    # x is a list (or vector) of length 352
    return max(0, x[277])
def l316_214(x):
    # x is a list (or vector) of length 352
    return max(0, x[278])
def l316_215(x):
    # x is a list (or vector) of length 352
    return max(0, x[279])
def l316_216(x):
    # x is a list (or vector) of length 352
    return max(0, x[280])
def l316_217(x):
    # x is a list (or vector) of length 352
    return max(0, x[281])
def l316_218(x):
    # x is a list (or vector) of length 352
    return max(0, x[282])
def l316_219(x):
    # x is a list (or vector) of length 352
    return max(0, x[283])
def l316_220(x):
    # x is a list (or vector) of length 352
    return max(0, x[284])
def l316_221(x):
    # x is a list (or vector) of length 352
    return max(0, x[285])
def l316_222(x):
    # x is a list (or vector) of length 352
    return max(0, x[286])
def l316_223(x):
    # x is a list (or vector) of length 352
    return max(0, x[287])
def l316_224(x):
    # x is a list (or vector) of length 352
    return max(0, x[288])
def l316_225(x):
    # x is a list (or vector) of length 352
    return max(0, x[289])
def l316_226(x):
    # x is a list (or vector) of length 352
    return max(0, x[290])
def l316_227(x):
    # x is a list (or vector) of length 352
    return max(0, x[291])
def l316_228(x):
    # x is a list (or vector) of length 352
    return max(0, x[292])
def l316_229(x):
    # x is a list (or vector) of length 352
    return max(0, x[293])
def l316_230(x):
    # x is a list (or vector) of length 352
    return max(0, x[294])
def l316_231(x):
    # x is a list (or vector) of length 352
    return max(0, x[295])
def l316_232(x):
    # x is a list (or vector) of length 352
    return max(0, x[296])
def l316_233(x):
    # x is a list (or vector) of length 352
    return max(0, x[297])
def l316_234(x):
    # x is a list (or vector) of length 352
    return max(0, x[298])
def l316_235(x):
    # x is a list (or vector) of length 352
    return max(0, x[299])
def l316_236(x):
    # x is a list (or vector) of length 352
    return max(0, x[300])
def l316_237(x):
    # x is a list (or vector) of length 352
    return max(0, x[301])
def l316_238(x):
    # x is a list (or vector) of length 352
    return max(0, x[302])
def l316_239(x):
    # x is a list (or vector) of length 352
    return max(0, x[303])
def l316_240(x):
    # x is a list (or vector) of length 352
    return max(0, x[304])
def l316_241(x):
    # x is a list (or vector) of length 352
    return max(0, x[305])
def l316_242(x):
    # x is a list (or vector) of length 352
    return max(0, x[306])
def l316_243(x):
    # x is a list (or vector) of length 352
    return max(0, x[307])
def l316_244(x):
    # x is a list (or vector) of length 352
    return max(0, x[308])
def l316_245(x):
    # x is a list (or vector) of length 352
    return max(0, x[309])
def l316_246(x):
    # x is a list (or vector) of length 352
    return max(0, x[310])
def l316_247(x):
    # x is a list (or vector) of length 352
    return max(0, x[311])
def l316_248(x):
    # x is a list (or vector) of length 352
    return max(0, x[312])
def l316_249(x):
    # x is a list (or vector) of length 352
    return max(0, x[313])
def l316_250(x):
    # x is a list (or vector) of length 352
    return max(0, x[314])
def l316_251(x):
    # x is a list (or vector) of length 352
    return max(0, x[315])
def l316_252(x):
    # x is a list (or vector) of length 352
    return max(0, x[316])
def l316_253(x):
    # x is a list (or vector) of length 352
    return max(0, x[317])
def l316_254(x):
    # x is a list (or vector) of length 352
    return max(0, x[318])
def l316_255(x):
    # x is a list (or vector) of length 352
    return max(0, x[319])
def l316_256(x):
    # x is a list (or vector) of length 352
    return max(0, x[320])
def l316_257(x):
    # x is a list (or vector) of length 352
    return max(0, x[321])
def l316_258(x):
    # x is a list (or vector) of length 352
    return max(0, x[322])
def l316_259(x):
    # x is a list (or vector) of length 352
    return max(0, x[323])
def l316_260(x):
    # x is a list (or vector) of length 352
    return max(0, x[324])
def l316_261(x):
    # x is a list (or vector) of length 352
    return max(0, x[325])
def l316_262(x):
    # x is a list (or vector) of length 352
    return max(0, x[326])
def l316_263(x):
    # x is a list (or vector) of length 352
    return max(0, x[327])
def l316_264(x):
    # x is a list (or vector) of length 352
    return max(0, x[328])
def l316_265(x):
    # x is a list (or vector) of length 352
    return max(0, x[329])
def l316_266(x):
    # x is a list (or vector) of length 352
    return max(0, x[330])
def l316_267(x):
    # x is a list (or vector) of length 352
    return max(0, x[331])
def l316_268(x):
    # x is a list (or vector) of length 352
    return max(0, x[332])
def l316_269(x):
    # x is a list (or vector) of length 352
    return max(0, x[333])
def l316_270(x):
    # x is a list (or vector) of length 352
    return max(0, x[334])
def l316_271(x):
    # x is a list (or vector) of length 352
    return max(0, x[335])
def l316_272(x):
    # x is a list (or vector) of length 352
    return max(0, x[336])
def l316_273(x):
    # x is a list (or vector) of length 352
    return max(0, x[337])
def l316_274(x):
    # x is a list (or vector) of length 352
    return max(0, x[338])
def l316_275(x):
    # x is a list (or vector) of length 352
    return max(0, x[339])
def l316_276(x):
    # x is a list (or vector) of length 352
    return max(0, x[340])
def l316_277(x):
    # x is a list (or vector) of length 352
    return max(0, x[341])
def l316_278(x):
    # x is a list (or vector) of length 352
    return max(0, x[342])
def l316_279(x):
    # x is a list (or vector) of length 352
    return max(0, x[343])
def l316_280(x):
    # x is a list (or vector) of length 352
    return max(0, x[344])
def l316_281(x):
    # x is a list (or vector) of length 352
    return max(0, x[345])
def l316_282(x):
    # x is a list (or vector) of length 352
    return max(0, x[346])
def l316_283(x):
    # x is a list (or vector) of length 352
    return max(0, x[347])
def l316_284(x):
    # x is a list (or vector) of length 352
    return max(0, x[348])
def l316_285(x):
    # x is a list (or vector) of length 352
    return max(0, x[349])
def l316_286(x):
    # x is a list (or vector) of length 352
    return max(0, x[350])
def l316_287(x):
    # x is a list (or vector) of length 352
    return max(0, x[351])
def l316_(x):
    # x is a list (or vector) of length 352
    return [
        l316_0(x),
        l316_1(x),
        l316_2(x),
        l316_3(x),
        l316_4(x),
        l316_5(x),
        l316_6(x),
        l316_7(x),
        l316_8(x),
        l316_9(x),
        l316_10(x),
        l316_11(x),
        l316_12(x),
        l316_13(x),
        l316_14(x),
        l316_15(x),
        l316_16(x),
        l316_17(x),
        l316_18(x),
        l316_19(x),
        l316_20(x),
        l316_21(x),
        l316_22(x),
        l316_23(x),
        l316_24(x),
        l316_25(x),
        l316_26(x),
        l316_27(x),
        l316_28(x),
        l316_29(x),
        l316_30(x),
        l316_31(x),
        l316_32(x),
        l316_33(x),
        l316_34(x),
        l316_35(x),
        l316_36(x),
        l316_37(x),
        l316_38(x),
        l316_39(x),
        l316_40(x),
        l316_41(x),
        l316_42(x),
        l316_43(x),
        l316_44(x),
        l316_45(x),
        l316_46(x),
        l316_47(x),
        l316_48(x),
        l316_49(x),
        l316_50(x),
        l316_51(x),
        l316_52(x),
        l316_53(x),
        l316_54(x),
        l316_55(x),
        l316_56(x),
        l316_57(x),
        l316_58(x),
        l316_59(x),
        l316_60(x),
        l316_61(x),
        l316_62(x),
        l316_63(x),
        l316_64(x),
        l316_65(x),
        l316_66(x),
        l316_67(x),
        l316_68(x),
        l316_69(x),
        l316_70(x),
        l316_71(x),
        l316_72(x),
        l316_73(x),
        l316_74(x),
        l316_75(x),
        l316_76(x),
        l316_77(x),
        l316_78(x),
        l316_79(x),
        l316_80(x),
        l316_81(x),
        l316_82(x),
        l316_83(x),
        l316_84(x),
        l316_85(x),
        l316_86(x),
        l316_87(x),
        l316_88(x),
        l316_89(x),
        l316_90(x),
        l316_91(x),
        l316_92(x),
        l316_93(x),
        l316_94(x),
        l316_95(x),
        l316_96(x),
        l316_97(x),
        l316_98(x),
        l316_99(x),
        l316_100(x),
        l316_101(x),
        l316_102(x),
        l316_103(x),
        l316_104(x),
        l316_105(x),
        l316_106(x),
        l316_107(x),
        l316_108(x),
        l316_109(x),
        l316_110(x),
        l316_111(x),
        l316_112(x),
        l316_113(x),
        l316_114(x),
        l316_115(x),
        l316_116(x),
        l316_117(x),
        l316_118(x),
        l316_119(x),
        l316_120(x),
        l316_121(x),
        l316_122(x),
        l316_123(x),
        l316_124(x),
        l316_125(x),
        l316_126(x),
        l316_127(x),
        l316_128(x),
        l316_129(x),
        l316_130(x),
        l316_131(x),
        l316_132(x),
        l316_133(x),
        l316_134(x),
        l316_135(x),
        l316_136(x),
        l316_137(x),
        l316_138(x),
        l316_139(x),
        l316_140(x),
        l316_141(x),
        l316_142(x),
        l316_143(x),
        l316_144(x),
        l316_145(x),
        l316_146(x),
        l316_147(x),
        l316_148(x),
        l316_149(x),
        l316_150(x),
        l316_151(x),
        l316_152(x),
        l316_153(x),
        l316_154(x),
        l316_155(x),
        l316_156(x),
        l316_157(x),
        l316_158(x),
        l316_159(x),
        l316_160(x),
        l316_161(x),
        l316_162(x),
        l316_163(x),
        l316_164(x),
        l316_165(x),
        l316_166(x),
        l316_167(x),
        l316_168(x),
        l316_169(x),
        l316_170(x),
        l316_171(x),
        l316_172(x),
        l316_173(x),
        l316_174(x),
        l316_175(x),
        l316_176(x),
        l316_177(x),
        l316_178(x),
        l316_179(x),
        l316_180(x),
        l316_181(x),
        l316_182(x),
        l316_183(x),
        l316_184(x),
        l316_185(x),
        l316_186(x),
        l316_187(x),
        l316_188(x),
        l316_189(x),
        l316_190(x),
        l316_191(x),
        l316_192(x),
        l316_193(x),
        l316_194(x),
        l316_195(x),
        l316_196(x),
        l316_197(x),
        l316_198(x),
        l316_199(x),
        l316_200(x),
        l316_201(x),
        l316_202(x),
        l316_203(x),
        l316_204(x),
        l316_205(x),
        l316_206(x),
        l316_207(x),
        l316_208(x),
        l316_209(x),
        l316_210(x),
        l316_211(x),
        l316_212(x),
        l316_213(x),
        l316_214(x),
        l316_215(x),
        l316_216(x),
        l316_217(x),
        l316_218(x),
        l316_219(x),
        l316_220(x),
        l316_221(x),
        l316_222(x),
        l316_223(x),
        l316_224(x),
        l316_225(x),
        l316_226(x),
        l316_227(x),
        l316_228(x),
        l316_229(x),
        l316_230(x),
        l316_231(x),
        l316_232(x),
        l316_233(x),
        l316_234(x),
        l316_235(x),
        l316_236(x),
        l316_237(x),
        l316_238(x),
        l316_239(x),
        l316_240(x),
        l316_241(x),
        l316_242(x),
        l316_243(x),
        l316_244(x),
        l316_245(x),
        l316_246(x),
        l316_247(x),
        l316_248(x),
        l316_249(x),
        l316_250(x),
        l316_251(x),
        l316_252(x),
        l316_253(x),
        l316_254(x),
        l316_255(x),
        l316_256(x),
        l316_257(x),
        l316_258(x),
        l316_259(x),
        l316_260(x),
        l316_261(x),
        l316_262(x),
        l316_263(x),
        l316_264(x),
        l316_265(x),
        l316_266(x),
        l316_267(x),
        l316_268(x),
        l316_269(x),
        l316_270(x),
        l316_271(x),
        l316_272(x),
        l316_273(x),
        l316_274(x),
        l316_275(x),
        l316_276(x),
        l316_277(x),
        l316_278(x),
        l316_279(x),
        l316_280(x),
        l316_281(x),
        l316_282(x),
        l316_283(x),
        l316_284(x),
        l316_285(x),
        l316_286(x),
        l316_287(x),
    ]