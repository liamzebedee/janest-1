import numpy as np




# Generated from reverse engineering
def l400_g(x: np.ndarray) -> np.ndarray:
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




def l400_0(x):
    # x is a list (or vector) of length 352
    return max(0, x[0])
def l400_1(x):
    # x is a list (or vector) of length 352
    return max(0, x[1])
def l400_2(x):
    # x is a list (or vector) of length 352
    return max(0, x[2])
def l400_3(x):
    # x is a list (or vector) of length 352
    return max(0, x[3])
def l400_4(x):
    # x is a list (or vector) of length 352
    return max(0, x[4])
def l400_5(x):
    # x is a list (or vector) of length 352
    return max(0, x[5])
def l400_6(x):
    # x is a list (or vector) of length 352
    return max(0, x[6])
def l400_7(x):
    # x is a list (or vector) of length 352
    return max(0, x[7])
def l400_8(x):
    # x is a list (or vector) of length 352
    return max(0, x[8])
def l400_9(x):
    # x is a list (or vector) of length 352
    return max(0, x[9])
def l400_10(x):
    # x is a list (or vector) of length 352
    return max(0, x[10])
def l400_11(x):
    # x is a list (or vector) of length 352
    return max(0, x[11])
def l400_12(x):
    # x is a list (or vector) of length 352
    return max(0, x[12])
def l400_13(x):
    # x is a list (or vector) of length 352
    return max(0, x[13])
def l400_14(x):
    # x is a list (or vector) of length 352
    return max(0, x[14])
def l400_15(x):
    # x is a list (or vector) of length 352
    return max(0, x[15])
def l400_16(x):
    # x is a list (or vector) of length 352
    return max(0, x[16])
def l400_17(x):
    # x is a list (or vector) of length 352
    return max(0, x[17])
def l400_18(x):
    # x is a list (or vector) of length 352
    return max(0, x[18])
def l400_19(x):
    # x is a list (or vector) of length 352
    return max(0, x[19])
def l400_20(x):
    # x is a list (or vector) of length 352
    return max(0, x[20])
def l400_21(x):
    # x is a list (or vector) of length 352
    return max(0, x[21])
def l400_22(x):
    # x is a list (or vector) of length 352
    return max(0, x[22])
def l400_23(x):
    # x is a list (or vector) of length 352
    return max(0, x[23])
def l400_24(x):
    # x is a list (or vector) of length 352
    return max(0, x[24])
def l400_25(x):
    # x is a list (or vector) of length 352
    return max(0, x[25])
def l400_26(x):
    # x is a list (or vector) of length 352
    return max(0, x[26])
def l400_27(x):
    # x is a list (or vector) of length 352
    return max(0, x[27])
def l400_28(x):
    # x is a list (or vector) of length 352
    return max(0, x[28])
def l400_29(x):
    # x is a list (or vector) of length 352
    return max(0, x[29])
def l400_30(x):
    # x is a list (or vector) of length 352
    return max(0, x[30])
def l400_31(x):
    # x is a list (or vector) of length 352
    return max(0, x[31])
def l400_32(x):
    # x is a list (or vector) of length 352
    return max(0, x[32])
def l400_33(x):
    # x is a list (or vector) of length 352
    return max(0, x[33])
def l400_34(x):
    # x is a list (or vector) of length 352
    return max(0, x[34])
def l400_35(x):
    # x is a list (or vector) of length 352
    return max(0, x[35])
def l400_36(x):
    # x is a list (or vector) of length 352
    return max(0, x[36])
def l400_37(x):
    # x is a list (or vector) of length 352
    return max(0, x[37])
def l400_38(x):
    # x is a list (or vector) of length 352
    return max(0, x[38])
def l400_39(x):
    # x is a list (or vector) of length 352
    return max(0, x[39])
def l400_40(x):
    # x is a list (or vector) of length 352
    return max(0, x[40])
def l400_41(x):
    # x is a list (or vector) of length 352
    return max(0, x[41])
def l400_42(x):
    # x is a list (or vector) of length 352
    return max(0, x[42])
def l400_43(x):
    # x is a list (or vector) of length 352
    return max(0, x[43])
def l400_44(x):
    # x is a list (or vector) of length 352
    return max(0, x[44])
def l400_45(x):
    # x is a list (or vector) of length 352
    return max(0, x[45])
def l400_46(x):
    # x is a list (or vector) of length 352
    return max(0, x[46])
def l400_47(x):
    # x is a list (or vector) of length 352
    return max(0, x[47])
def l400_48(x):
    # x is a list (or vector) of length 352
    return max(0, x[48])
def l400_49(x):
    # x is a list (or vector) of length 352
    return max(0, x[49])
def l400_50(x):
    # x is a list (or vector) of length 352
    return max(0, x[50])
def l400_51(x):
    # x is a list (or vector) of length 352
    return max(0, x[51])
def l400_52(x):
    # x is a list (or vector) of length 352
    return max(0, x[52])
def l400_53(x):
    # x is a list (or vector) of length 352
    return max(0, x[53])
def l400_54(x):
    # x is a list (or vector) of length 352
    return max(0, x[54])
def l400_55(x):
    # x is a list (or vector) of length 352
    return max(0, x[55])
def l400_56(x):
    # x is a list (or vector) of length 352
    return max(0, x[56])
def l400_57(x):
    # x is a list (or vector) of length 352
    return max(0, x[57])
def l400_58(x):
    # x is a list (or vector) of length 352
    return max(0, x[58])
def l400_59(x):
    # x is a list (or vector) of length 352
    return max(0, x[59])
def l400_60(x):
    # x is a list (or vector) of length 352
    return max(0, x[60])
def l400_61(x):
    # x is a list (or vector) of length 352
    return max(0, x[61])
def l400_62(x):
    # x is a list (or vector) of length 352
    return max(0, x[62])
def l400_63(x):
    # x is a list (or vector) of length 352
    return max(0, x[63])
def l400_64(x):
    # x is a list (or vector) of length 352
    return max(0, x[64])
def l400_65(x):
    # x is a list (or vector) of length 352
    return max(0, x[65])
def l400_66(x):
    # x is a list (or vector) of length 352
    return max(0, x[66])
def l400_67(x):
    # x is a list (or vector) of length 352
    return max(0, x[67])
def l400_68(x):
    # x is a list (or vector) of length 352
    return max(0, x[68])
def l400_69(x):
    # x is a list (or vector) of length 352
    return max(0, x[69])
def l400_70(x):
    # x is a list (or vector) of length 352
    return max(0, x[70])
def l400_71(x):
    # x is a list (or vector) of length 352
    return max(0, x[71])
def l400_72(x):
    # x is a list (or vector) of length 352
    return max(0, x[72])
def l400_73(x):
    # x is a list (or vector) of length 352
    return max(0, x[73])
def l400_74(x):
    # x is a list (or vector) of length 352
    return max(0, x[74])
def l400_75(x):
    # x is a list (or vector) of length 352
    return max(0, x[75])
def l400_76(x):
    # x is a list (or vector) of length 352
    return max(0, x[76])
def l400_77(x):
    # x is a list (or vector) of length 352
    return max(0, x[77])
def l400_78(x):
    # x is a list (or vector) of length 352
    return max(0, x[78])
def l400_79(x):
    # x is a list (or vector) of length 352
    return max(0, x[79])
def l400_80(x):
    # x is a list (or vector) of length 352
    return max(0, x[80])
def l400_81(x):
    # x is a list (or vector) of length 352
    return max(0, x[81])
def l400_82(x):
    # x is a list (or vector) of length 352
    return max(0, x[82])
def l400_83(x):
    # x is a list (or vector) of length 352
    return max(0, x[83])
def l400_84(x):
    # x is a list (or vector) of length 352
    return max(0, x[84])
def l400_85(x):
    # x is a list (or vector) of length 352
    return max(0, x[85])
def l400_86(x):
    # x is a list (or vector) of length 352
    return max(0, x[86])
def l400_87(x):
    # x is a list (or vector) of length 352
    return max(0, x[87])
def l400_88(x):
    # x is a list (or vector) of length 352
    return max(0, x[88])
def l400_89(x):
    # x is a list (or vector) of length 352
    return max(0, x[89])
def l400_90(x):
    # x is a list (or vector) of length 352
    return max(0, x[90])
def l400_91(x):
    # x is a list (or vector) of length 352
    return max(0, x[91])
def l400_92(x):
    # x is a list (or vector) of length 352
    return max(0, x[92])
def l400_93(x):
    # x is a list (or vector) of length 352
    return max(0, x[93])
def l400_94(x):
    # x is a list (or vector) of length 352
    return max(0, x[94])
def l400_95(x):
    # x is a list (or vector) of length 352
    return max(0, x[95])
def l400_96(x):
    # x is a list (or vector) of length 352
    return max(0, x[160])
def l400_97(x):
    # x is a list (or vector) of length 352
    return max(0, x[96] + x[161])
def l400_98(x):
    # x is a list (or vector) of length 352
    return max(0, x[97] + x[162])
def l400_99(x):
    # x is a list (or vector) of length 352
    return max(0, x[98] + x[163])
def l400_100(x):
    # x is a list (or vector) of length 352
    return max(0, x[99] + x[164])
def l400_101(x):
    # x is a list (or vector) of length 352
    return max(0, x[100] + x[165])
def l400_102(x):
    # x is a list (or vector) of length 352
    return max(0, x[101] + x[166])
def l400_103(x):
    # x is a list (or vector) of length 352
    return max(0, x[102] + x[167])
def l400_104(x):
    # x is a list (or vector) of length 352
    return max(0, x[103] + x[168])
def l400_105(x):
    # x is a list (or vector) of length 352
    return max(0, x[104] + x[169])
def l400_106(x):
    # x is a list (or vector) of length 352
    return max(0, x[105] + x[170])
def l400_107(x):
    # x is a list (or vector) of length 352
    return max(0, x[106] + x[171])
def l400_108(x):
    # x is a list (or vector) of length 352
    return max(0, x[107] + x[172])
def l400_109(x):
    # x is a list (or vector) of length 352
    return max(0, x[108] + x[173])
def l400_110(x):
    # x is a list (or vector) of length 352
    return max(0, x[109] + x[174])
def l400_111(x):
    # x is a list (or vector) of length 352
    return max(0, x[110] + x[175])
def l400_112(x):
    # x is a list (or vector) of length 352
    return max(0, x[111] + x[176])
def l400_113(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[112] + x[177] + 1.0)
def l400_114(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[113] + x[178] + 1.0)
def l400_115(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[114] + x[179] + 1.0)
def l400_116(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[115] + x[180] + 1.0)
def l400_117(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[116] + x[181] + 1.0)
def l400_118(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[117] + x[182] + 1.0)
def l400_119(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[118] + x[183] + 1.0)
def l400_120(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[119] + x[184] + 1.0)
def l400_121(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[120] + x[185] + 1.0)
def l400_122(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[121] + x[186] + 1.0)
def l400_123(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[122] + x[187] + 1.0)
def l400_124(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[123] + x[188] + 1.0)
def l400_125(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[124] + x[189] + 1.0)
def l400_126(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[125] + x[190] + 1.0)
def l400_127(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[126] + x[191] + 1.0)
def l400_128(x):
    # x is a list (or vector) of length 352
    return max(0, x[160] + -1.0)
def l400_129(x):
    # x is a list (or vector) of length 352
    return max(0, x[96] + x[161] + -1.0)
def l400_130(x):
    # x is a list (or vector) of length 352
    return max(0, x[97] + x[162] + -1.0)
def l400_131(x):
    # x is a list (or vector) of length 352
    return max(0, x[98] + x[163] + -1.0)
def l400_132(x):
    # x is a list (or vector) of length 352
    return max(0, x[99] + x[164] + -1.0)
def l400_133(x):
    # x is a list (or vector) of length 352
    return max(0, x[100] + x[165] + -1.0)
def l400_134(x):
    # x is a list (or vector) of length 352
    return max(0, x[101] + x[166] + -1.0)
def l400_135(x):
    # x is a list (or vector) of length 352
    return max(0, x[102] + x[167] + -1.0)
def l400_136(x):
    # x is a list (or vector) of length 352
    return max(0, x[103] + x[168] + -1.0)
def l400_137(x):
    # x is a list (or vector) of length 352
    return max(0, x[104] + x[169] + -1.0)
def l400_138(x):
    # x is a list (or vector) of length 352
    return max(0, x[105] + x[170] + -1.0)
def l400_139(x):
    # x is a list (or vector) of length 352
    return max(0, x[106] + x[171] + -1.0)
def l400_140(x):
    # x is a list (or vector) of length 352
    return max(0, x[107] + x[172] + -1.0)
def l400_141(x):
    # x is a list (or vector) of length 352
    return max(0, x[108] + x[173] + -1.0)
def l400_142(x):
    # x is a list (or vector) of length 352
    return max(0, x[109] + x[174] + -1.0)
def l400_143(x):
    # x is a list (or vector) of length 352
    return max(0, x[110] + x[175] + -1.0)
def l400_144(x):
    # x is a list (or vector) of length 352
    return max(0, x[111] + x[176] + -1.0)
def l400_145(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[112] + x[177])
def l400_146(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[113] + x[178])
def l400_147(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[114] + x[179])
def l400_148(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[115] + x[180])
def l400_149(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[116] + x[181])
def l400_150(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[117] + x[182])
def l400_151(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[118] + x[183])
def l400_152(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[119] + x[184])
def l400_153(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[120] + x[185])
def l400_154(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[121] + x[186])
def l400_155(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[122] + x[187])
def l400_156(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[123] + x[188])
def l400_157(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[124] + x[189])
def l400_158(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[125] + x[190])
def l400_159(x):
    # x is a list (or vector) of length 352
    return max(0, -1.0*x[126] + x[191])
def l400_160(x):
    # x is a list (or vector) of length 352
    return max(0, x[192] + -2.0*x[224])
def l400_161(x):
    # x is a list (or vector) of length 352
    return max(0, x[193] + -2.0*x[225])
def l400_162(x):
    # x is a list (or vector) of length 352
    return max(0, x[194] + -2.0*x[226])
def l400_163(x):
    # x is a list (or vector) of length 352
    return max(0, x[195] + -2.0*x[227])
def l400_164(x):
    # x is a list (or vector) of length 352
    return max(0, x[196] + -2.0*x[228])
def l400_165(x):
    # x is a list (or vector) of length 352
    return max(0, x[197] + -2.0*x[229])
def l400_166(x):
    # x is a list (or vector) of length 352
    return max(0, x[198] + -2.0*x[230])
def l400_167(x):
    # x is a list (or vector) of length 352
    return max(0, x[199] + -2.0*x[231])
def l400_168(x):
    # x is a list (or vector) of length 352
    return max(0, x[200] + -2.0*x[232])
def l400_169(x):
    # x is a list (or vector) of length 352
    return max(0, x[201] + -2.0*x[233])
def l400_170(x):
    # x is a list (or vector) of length 352
    return max(0, x[202] + -2.0*x[234])
def l400_171(x):
    # x is a list (or vector) of length 352
    return max(0, x[203] + -2.0*x[235])
def l400_172(x):
    # x is a list (or vector) of length 352
    return max(0, x[204] + -2.0*x[236])
def l400_173(x):
    # x is a list (or vector) of length 352
    return max(0, x[205] + -2.0*x[237])
def l400_174(x):
    # x is a list (or vector) of length 352
    return max(0, x[206] + -2.0*x[238])
def l400_175(x):
    # x is a list (or vector) of length 352
    return max(0, x[207] + -2.0*x[239])
def l400_176(x):
    # x is a list (or vector) of length 352
    return max(0, x[208] + -2.0*x[240])
def l400_177(x):
    # x is a list (or vector) of length 352
    return max(0, x[209] + -2.0*x[241])
def l400_178(x):
    # x is a list (or vector) of length 352
    return max(0, x[210] + -2.0*x[242])
def l400_179(x):
    # x is a list (or vector) of length 352
    return max(0, x[211] + -2.0*x[243])
def l400_180(x):
    # x is a list (or vector) of length 352
    return max(0, x[212] + -2.0*x[244])
def l400_181(x):
    # x is a list (or vector) of length 352
    return max(0, x[213] + -2.0*x[245])
def l400_182(x):
    # x is a list (or vector) of length 352
    return max(0, x[214] + -2.0*x[246])
def l400_183(x):
    # x is a list (or vector) of length 352
    return max(0, x[215] + -2.0*x[247])
def l400_184(x):
    # x is a list (or vector) of length 352
    return max(0, x[216] + -2.0*x[248])
def l400_185(x):
    # x is a list (or vector) of length 352
    return max(0, x[217] + -2.0*x[249])
def l400_186(x):
    # x is a list (or vector) of length 352
    return max(0, x[218] + -2.0*x[250])
def l400_187(x):
    # x is a list (or vector) of length 352
    return max(0, x[219] + -2.0*x[251])
def l400_188(x):
    # x is a list (or vector) of length 352
    return max(0, x[220] + -2.0*x[252])
def l400_189(x):
    # x is a list (or vector) of length 352
    return max(0, x[221] + -2.0*x[253])
def l400_190(x):
    # x is a list (or vector) of length 352
    return max(0, x[222] + -2.0*x[254])
def l400_191(x):
    # x is a list (or vector) of length 352
    return max(0, x[223] + -2.0*x[255])
def l400_192(x):
    # x is a list (or vector) of length 352
    return max(0, x[256])
def l400_193(x):
    # x is a list (or vector) of length 352
    return max(0, x[257])
def l400_194(x):
    # x is a list (or vector) of length 352
    return max(0, x[258])
def l400_195(x):
    # x is a list (or vector) of length 352
    return max(0, x[259])
def l400_196(x):
    # x is a list (or vector) of length 352
    return max(0, x[260])
def l400_197(x):
    # x is a list (or vector) of length 352
    return max(0, x[261])
def l400_198(x):
    # x is a list (or vector) of length 352
    return max(0, x[262])
def l400_199(x):
    # x is a list (or vector) of length 352
    return max(0, x[263])
def l400_200(x):
    # x is a list (or vector) of length 352
    return max(0, x[264])
def l400_201(x):
    # x is a list (or vector) of length 352
    return max(0, x[265])
def l400_202(x):
    # x is a list (or vector) of length 352
    return max(0, x[266])
def l400_203(x):
    # x is a list (or vector) of length 352
    return max(0, x[267])
def l400_204(x):
    # x is a list (or vector) of length 352
    return max(0, x[268])
def l400_205(x):
    # x is a list (or vector) of length 352
    return max(0, x[269])
def l400_206(x):
    # x is a list (or vector) of length 352
    return max(0, x[270])
def l400_207(x):
    # x is a list (or vector) of length 352
    return max(0, x[271])
def l400_208(x):
    # x is a list (or vector) of length 352
    return max(0, x[272])
def l400_209(x):
    # x is a list (or vector) of length 352
    return max(0, x[273])
def l400_210(x):
    # x is a list (or vector) of length 352
    return max(0, x[274])
def l400_211(x):
    # x is a list (or vector) of length 352
    return max(0, x[275])
def l400_212(x):
    # x is a list (or vector) of length 352
    return max(0, x[276])
def l400_213(x):
    # x is a list (or vector) of length 352
    return max(0, x[277])
def l400_214(x):
    # x is a list (or vector) of length 352
    return max(0, x[278])
def l400_215(x):
    # x is a list (or vector) of length 352
    return max(0, x[279])
def l400_216(x):
    # x is a list (or vector) of length 352
    return max(0, x[280])
def l400_217(x):
    # x is a list (or vector) of length 352
    return max(0, x[281])
def l400_218(x):
    # x is a list (or vector) of length 352
    return max(0, x[282])
def l400_219(x):
    # x is a list (or vector) of length 352
    return max(0, x[283])
def l400_220(x):
    # x is a list (or vector) of length 352
    return max(0, x[284])
def l400_221(x):
    # x is a list (or vector) of length 352
    return max(0, x[285])
def l400_222(x):
    # x is a list (or vector) of length 352
    return max(0, x[286])
def l400_223(x):
    # x is a list (or vector) of length 352
    return max(0, x[287])
def l400_224(x):
    # x is a list (or vector) of length 352
    return max(0, x[288])
def l400_225(x):
    # x is a list (or vector) of length 352
    return max(0, x[289])
def l400_226(x):
    # x is a list (or vector) of length 352
    return max(0, x[290])
def l400_227(x):
    # x is a list (or vector) of length 352
    return max(0, x[291])
def l400_228(x):
    # x is a list (or vector) of length 352
    return max(0, x[292])
def l400_229(x):
    # x is a list (or vector) of length 352
    return max(0, x[293])
def l400_230(x):
    # x is a list (or vector) of length 352
    return max(0, x[294])
def l400_231(x):
    # x is a list (or vector) of length 352
    return max(0, x[295])
def l400_232(x):
    # x is a list (or vector) of length 352
    return max(0, x[296])
def l400_233(x):
    # x is a list (or vector) of length 352
    return max(0, x[297])
def l400_234(x):
    # x is a list (or vector) of length 352
    return max(0, x[298])
def l400_235(x):
    # x is a list (or vector) of length 352
    return max(0, x[299])
def l400_236(x):
    # x is a list (or vector) of length 352
    return max(0, x[300])
def l400_237(x):
    # x is a list (or vector) of length 352
    return max(0, x[301])
def l400_238(x):
    # x is a list (or vector) of length 352
    return max(0, x[302])
def l400_239(x):
    # x is a list (or vector) of length 352
    return max(0, x[303])
def l400_240(x):
    # x is a list (or vector) of length 352
    return max(0, x[304])
def l400_241(x):
    # x is a list (or vector) of length 352
    return max(0, x[305])
def l400_242(x):
    # x is a list (or vector) of length 352
    return max(0, x[306])
def l400_243(x):
    # x is a list (or vector) of length 352
    return max(0, x[307])
def l400_244(x):
    # x is a list (or vector) of length 352
    return max(0, x[308])
def l400_245(x):
    # x is a list (or vector) of length 352
    return max(0, x[309])
def l400_246(x):
    # x is a list (or vector) of length 352
    return max(0, x[310])
def l400_247(x):
    # x is a list (or vector) of length 352
    return max(0, x[311])
def l400_248(x):
    # x is a list (or vector) of length 352
    return max(0, x[312])
def l400_249(x):
    # x is a list (or vector) of length 352
    return max(0, x[313])
def l400_250(x):
    # x is a list (or vector) of length 352
    return max(0, x[314])
def l400_251(x):
    # x is a list (or vector) of length 352
    return max(0, x[315])
def l400_252(x):
    # x is a list (or vector) of length 352
    return max(0, x[316])
def l400_253(x):
    # x is a list (or vector) of length 352
    return max(0, x[317])
def l400_254(x):
    # x is a list (or vector) of length 352
    return max(0, x[318])
def l400_255(x):
    # x is a list (or vector) of length 352
    return max(0, x[319])
def l400_256(x):
    # x is a list (or vector) of length 352
    return max(0, x[320])
def l400_257(x):
    # x is a list (or vector) of length 352
    return max(0, x[321])
def l400_258(x):
    # x is a list (or vector) of length 352
    return max(0, x[322])
def l400_259(x):
    # x is a list (or vector) of length 352
    return max(0, x[323])
def l400_260(x):
    # x is a list (or vector) of length 352
    return max(0, x[324])
def l400_261(x):
    # x is a list (or vector) of length 352
    return max(0, x[325])
def l400_262(x):
    # x is a list (or vector) of length 352
    return max(0, x[326])
def l400_263(x):
    # x is a list (or vector) of length 352
    return max(0, x[327])
def l400_264(x):
    # x is a list (or vector) of length 352
    return max(0, x[328])
def l400_265(x):
    # x is a list (or vector) of length 352
    return max(0, x[329])
def l400_266(x):
    # x is a list (or vector) of length 352
    return max(0, x[330])
def l400_267(x):
    # x is a list (or vector) of length 352
    return max(0, x[331])
def l400_268(x):
    # x is a list (or vector) of length 352
    return max(0, x[332])
def l400_269(x):
    # x is a list (or vector) of length 352
    return max(0, x[333])
def l400_270(x):
    # x is a list (or vector) of length 352
    return max(0, x[334])
def l400_271(x):
    # x is a list (or vector) of length 352
    return max(0, x[335])
def l400_272(x):
    # x is a list (or vector) of length 352
    return max(0, x[336])
def l400_273(x):
    # x is a list (or vector) of length 352
    return max(0, x[337])
def l400_274(x):
    # x is a list (or vector) of length 352
    return max(0, x[338])
def l400_275(x):
    # x is a list (or vector) of length 352
    return max(0, x[339])
def l400_276(x):
    # x is a list (or vector) of length 352
    return max(0, x[340])
def l400_277(x):
    # x is a list (or vector) of length 352
    return max(0, x[341])
def l400_278(x):
    # x is a list (or vector) of length 352
    return max(0, x[342])
def l400_279(x):
    # x is a list (or vector) of length 352
    return max(0, x[343])
def l400_280(x):
    # x is a list (or vector) of length 352
    return max(0, x[344])
def l400_281(x):
    # x is a list (or vector) of length 352
    return max(0, x[345])
def l400_282(x):
    # x is a list (or vector) of length 352
    return max(0, x[346])
def l400_283(x):
    # x is a list (or vector) of length 352
    return max(0, x[347])
def l400_284(x):
    # x is a list (or vector) of length 352
    return max(0, x[348])
def l400_285(x):
    # x is a list (or vector) of length 352
    return max(0, x[349])
def l400_286(x):
    # x is a list (or vector) of length 352
    return max(0, x[350])
def l400_287(x):
    # x is a list (or vector) of length 352
    return max(0, x[351])
def l400_(x):
    # x is a list (or vector) of length 352
    return [
        l400_0(x),
        l400_1(x),
        l400_2(x),
        l400_3(x),
        l400_4(x),
        l400_5(x),
        l400_6(x),
        l400_7(x),
        l400_8(x),
        l400_9(x),
        l400_10(x),
        l400_11(x),
        l400_12(x),
        l400_13(x),
        l400_14(x),
        l400_15(x),
        l400_16(x),
        l400_17(x),
        l400_18(x),
        l400_19(x),
        l400_20(x),
        l400_21(x),
        l400_22(x),
        l400_23(x),
        l400_24(x),
        l400_25(x),
        l400_26(x),
        l400_27(x),
        l400_28(x),
        l400_29(x),
        l400_30(x),
        l400_31(x),
        l400_32(x),
        l400_33(x),
        l400_34(x),
        l400_35(x),
        l400_36(x),
        l400_37(x),
        l400_38(x),
        l400_39(x),
        l400_40(x),
        l400_41(x),
        l400_42(x),
        l400_43(x),
        l400_44(x),
        l400_45(x),
        l400_46(x),
        l400_47(x),
        l400_48(x),
        l400_49(x),
        l400_50(x),
        l400_51(x),
        l400_52(x),
        l400_53(x),
        l400_54(x),
        l400_55(x),
        l400_56(x),
        l400_57(x),
        l400_58(x),
        l400_59(x),
        l400_60(x),
        l400_61(x),
        l400_62(x),
        l400_63(x),
        l400_64(x),
        l400_65(x),
        l400_66(x),
        l400_67(x),
        l400_68(x),
        l400_69(x),
        l400_70(x),
        l400_71(x),
        l400_72(x),
        l400_73(x),
        l400_74(x),
        l400_75(x),
        l400_76(x),
        l400_77(x),
        l400_78(x),
        l400_79(x),
        l400_80(x),
        l400_81(x),
        l400_82(x),
        l400_83(x),
        l400_84(x),
        l400_85(x),
        l400_86(x),
        l400_87(x),
        l400_88(x),
        l400_89(x),
        l400_90(x),
        l400_91(x),
        l400_92(x),
        l400_93(x),
        l400_94(x),
        l400_95(x),
        l400_96(x),
        l400_97(x),
        l400_98(x),
        l400_99(x),
        l400_100(x),
        l400_101(x),
        l400_102(x),
        l400_103(x),
        l400_104(x),
        l400_105(x),
        l400_106(x),
        l400_107(x),
        l400_108(x),
        l400_109(x),
        l400_110(x),
        l400_111(x),
        l400_112(x),
        l400_113(x),
        l400_114(x),
        l400_115(x),
        l400_116(x),
        l400_117(x),
        l400_118(x),
        l400_119(x),
        l400_120(x),
        l400_121(x),
        l400_122(x),
        l400_123(x),
        l400_124(x),
        l400_125(x),
        l400_126(x),
        l400_127(x),
        l400_128(x),
        l400_129(x),
        l400_130(x),
        l400_131(x),
        l400_132(x),
        l400_133(x),
        l400_134(x),
        l400_135(x),
        l400_136(x),
        l400_137(x),
        l400_138(x),
        l400_139(x),
        l400_140(x),
        l400_141(x),
        l400_142(x),
        l400_143(x),
        l400_144(x),
        l400_145(x),
        l400_146(x),
        l400_147(x),
        l400_148(x),
        l400_149(x),
        l400_150(x),
        l400_151(x),
        l400_152(x),
        l400_153(x),
        l400_154(x),
        l400_155(x),
        l400_156(x),
        l400_157(x),
        l400_158(x),
        l400_159(x),
        l400_160(x),
        l400_161(x),
        l400_162(x),
        l400_163(x),
        l400_164(x),
        l400_165(x),
        l400_166(x),
        l400_167(x),
        l400_168(x),
        l400_169(x),
        l400_170(x),
        l400_171(x),
        l400_172(x),
        l400_173(x),
        l400_174(x),
        l400_175(x),
        l400_176(x),
        l400_177(x),
        l400_178(x),
        l400_179(x),
        l400_180(x),
        l400_181(x),
        l400_182(x),
        l400_183(x),
        l400_184(x),
        l400_185(x),
        l400_186(x),
        l400_187(x),
        l400_188(x),
        l400_189(x),
        l400_190(x),
        l400_191(x),
        l400_192(x),
        l400_193(x),
        l400_194(x),
        l400_195(x),
        l400_196(x),
        l400_197(x),
        l400_198(x),
        l400_199(x),
        l400_200(x),
        l400_201(x),
        l400_202(x),
        l400_203(x),
        l400_204(x),
        l400_205(x),
        l400_206(x),
        l400_207(x),
        l400_208(x),
        l400_209(x),
        l400_210(x),
        l400_211(x),
        l400_212(x),
        l400_213(x),
        l400_214(x),
        l400_215(x),
        l400_216(x),
        l400_217(x),
        l400_218(x),
        l400_219(x),
        l400_220(x),
        l400_221(x),
        l400_222(x),
        l400_223(x),
        l400_224(x),
        l400_225(x),
        l400_226(x),
        l400_227(x),
        l400_228(x),
        l400_229(x),
        l400_230(x),
        l400_231(x),
        l400_232(x),
        l400_233(x),
        l400_234(x),
        l400_235(x),
        l400_236(x),
        l400_237(x),
        l400_238(x),
        l400_239(x),
        l400_240(x),
        l400_241(x),
        l400_242(x),
        l400_243(x),
        l400_244(x),
        l400_245(x),
        l400_246(x),
        l400_247(x),
        l400_248(x),
        l400_249(x),
        l400_250(x),
        l400_251(x),
        l400_252(x),
        l400_253(x),
        l400_254(x),
        l400_255(x),
        l400_256(x),
        l400_257(x),
        l400_258(x),
        l400_259(x),
        l400_260(x),
        l400_261(x),
        l400_262(x),
        l400_263(x),
        l400_264(x),
        l400_265(x),
        l400_266(x),
        l400_267(x),
        l400_268(x),
        l400_269(x),
        l400_270(x),
        l400_271(x),
        l400_272(x),
        l400_273(x),
        l400_274(x),
        l400_275(x),
        l400_276(x),
        l400_277(x),
        l400_278(x),
        l400_279(x),
        l400_280(x),
        l400_281(x),
        l400_282(x),
        l400_283(x),
        l400_284(x),
        l400_285(x),
        l400_286(x),
        l400_287(x),
    ]