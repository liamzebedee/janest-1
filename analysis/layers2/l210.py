import numpy as np




# Generated from reverse engineering
def l210_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 375
    out = np.empty(375, dtype=np.float32)
    
    # for i in range(0, 128):
    for i in range(0, 128):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 160):
    for i in range(0, 32):
        s = x[128 + i] + -2.0 * x[i + 160]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 161):
    for i in range(0, 1):
        s = x[192 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(161, 192):
    for i in range(0, 31):
        s = x[192 + i] + x[225 + i]
        s += biases[i]
        out[161 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(192, 223):
    for i in range(0, 31):
        s = x[193 + i]
        out[192 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(223, 254):
    for i in range(0, 31):
        s = x[224 + i] + x[225 + i]
        s += biases[i]
        out[223 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(254, 255):
    for i in range(0, 1):
        s = x[224 + i]
        out[254 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(255, 295):
    for i in range(0, 40):
        s = x[224 + i]
        out[255 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [32.0, 32.0, 32.0, 32.0]
    # for i in range(295, 299):
    for i in range(0, 4):
        s = -1 * x[264 + i]
        s += biases[i]
        out[295 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(299, 303):
    for i in range(0, 4):
        s = x[264 + i]
        out[299 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-31.0, -31.0, -31.0, -31.0]
    # for i in range(303, 307):
    for i in range(0, 4):
        s = x[264 + i]
        s += biases[i]
        out[303 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-32.0, -32.0, -32.0, -32.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    # for i in range(307, 375):
    for i in range(0, 68):
        s = x[264 + i]
        s += biases[i]
        out[307 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l210_0(x):
    # x is a list (or vector) of length 332
    return max(0, x[0])
def l210_1(x):
    # x is a list (or vector) of length 332
    return max(0, x[1])
def l210_2(x):
    # x is a list (or vector) of length 332
    return max(0, x[2])
def l210_3(x):
    # x is a list (or vector) of length 332
    return max(0, x[3])
def l210_4(x):
    # x is a list (or vector) of length 332
    return max(0, x[4])
def l210_5(x):
    # x is a list (or vector) of length 332
    return max(0, x[5])
def l210_6(x):
    # x is a list (or vector) of length 332
    return max(0, x[6])
def l210_7(x):
    # x is a list (or vector) of length 332
    return max(0, x[7])
def l210_8(x):
    # x is a list (or vector) of length 332
    return max(0, x[8])
def l210_9(x):
    # x is a list (or vector) of length 332
    return max(0, x[9])
def l210_10(x):
    # x is a list (or vector) of length 332
    return max(0, x[10])
def l210_11(x):
    # x is a list (or vector) of length 332
    return max(0, x[11])
def l210_12(x):
    # x is a list (or vector) of length 332
    return max(0, x[12])
def l210_13(x):
    # x is a list (or vector) of length 332
    return max(0, x[13])
def l210_14(x):
    # x is a list (or vector) of length 332
    return max(0, x[14])
def l210_15(x):
    # x is a list (or vector) of length 332
    return max(0, x[15])
def l210_16(x):
    # x is a list (or vector) of length 332
    return max(0, x[16])
def l210_17(x):
    # x is a list (or vector) of length 332
    return max(0, x[17])
def l210_18(x):
    # x is a list (or vector) of length 332
    return max(0, x[18])
def l210_19(x):
    # x is a list (or vector) of length 332
    return max(0, x[19])
def l210_20(x):
    # x is a list (or vector) of length 332
    return max(0, x[20])
def l210_21(x):
    # x is a list (or vector) of length 332
    return max(0, x[21])
def l210_22(x):
    # x is a list (or vector) of length 332
    return max(0, x[22])
def l210_23(x):
    # x is a list (or vector) of length 332
    return max(0, x[23])
def l210_24(x):
    # x is a list (or vector) of length 332
    return max(0, x[24])
def l210_25(x):
    # x is a list (or vector) of length 332
    return max(0, x[25])
def l210_26(x):
    # x is a list (or vector) of length 332
    return max(0, x[26])
def l210_27(x):
    # x is a list (or vector) of length 332
    return max(0, x[27])
def l210_28(x):
    # x is a list (or vector) of length 332
    return max(0, x[28])
def l210_29(x):
    # x is a list (or vector) of length 332
    return max(0, x[29])
def l210_30(x):
    # x is a list (or vector) of length 332
    return max(0, x[30])
def l210_31(x):
    # x is a list (or vector) of length 332
    return max(0, x[31])
def l210_32(x):
    # x is a list (or vector) of length 332
    return max(0, x[32])
def l210_33(x):
    # x is a list (or vector) of length 332
    return max(0, x[33])
def l210_34(x):
    # x is a list (or vector) of length 332
    return max(0, x[34])
def l210_35(x):
    # x is a list (or vector) of length 332
    return max(0, x[35])
def l210_36(x):
    # x is a list (or vector) of length 332
    return max(0, x[36])
def l210_37(x):
    # x is a list (or vector) of length 332
    return max(0, x[37])
def l210_38(x):
    # x is a list (or vector) of length 332
    return max(0, x[38])
def l210_39(x):
    # x is a list (or vector) of length 332
    return max(0, x[39])
def l210_40(x):
    # x is a list (or vector) of length 332
    return max(0, x[40])
def l210_41(x):
    # x is a list (or vector) of length 332
    return max(0, x[41])
def l210_42(x):
    # x is a list (or vector) of length 332
    return max(0, x[42])
def l210_43(x):
    # x is a list (or vector) of length 332
    return max(0, x[43])
def l210_44(x):
    # x is a list (or vector) of length 332
    return max(0, x[44])
def l210_45(x):
    # x is a list (or vector) of length 332
    return max(0, x[45])
def l210_46(x):
    # x is a list (or vector) of length 332
    return max(0, x[46])
def l210_47(x):
    # x is a list (or vector) of length 332
    return max(0, x[47])
def l210_48(x):
    # x is a list (or vector) of length 332
    return max(0, x[48])
def l210_49(x):
    # x is a list (or vector) of length 332
    return max(0, x[49])
def l210_50(x):
    # x is a list (or vector) of length 332
    return max(0, x[50])
def l210_51(x):
    # x is a list (or vector) of length 332
    return max(0, x[51])
def l210_52(x):
    # x is a list (or vector) of length 332
    return max(0, x[52])
def l210_53(x):
    # x is a list (or vector) of length 332
    return max(0, x[53])
def l210_54(x):
    # x is a list (or vector) of length 332
    return max(0, x[54])
def l210_55(x):
    # x is a list (or vector) of length 332
    return max(0, x[55])
def l210_56(x):
    # x is a list (or vector) of length 332
    return max(0, x[56])
def l210_57(x):
    # x is a list (or vector) of length 332
    return max(0, x[57])
def l210_58(x):
    # x is a list (or vector) of length 332
    return max(0, x[58])
def l210_59(x):
    # x is a list (or vector) of length 332
    return max(0, x[59])
def l210_60(x):
    # x is a list (or vector) of length 332
    return max(0, x[60])
def l210_61(x):
    # x is a list (or vector) of length 332
    return max(0, x[61])
def l210_62(x):
    # x is a list (or vector) of length 332
    return max(0, x[62])
def l210_63(x):
    # x is a list (or vector) of length 332
    return max(0, x[63])
def l210_64(x):
    # x is a list (or vector) of length 332
    return max(0, x[64])
def l210_65(x):
    # x is a list (or vector) of length 332
    return max(0, x[65])
def l210_66(x):
    # x is a list (or vector) of length 332
    return max(0, x[66])
def l210_67(x):
    # x is a list (or vector) of length 332
    return max(0, x[67])
def l210_68(x):
    # x is a list (or vector) of length 332
    return max(0, x[68])
def l210_69(x):
    # x is a list (or vector) of length 332
    return max(0, x[69])
def l210_70(x):
    # x is a list (or vector) of length 332
    return max(0, x[70])
def l210_71(x):
    # x is a list (or vector) of length 332
    return max(0, x[71])
def l210_72(x):
    # x is a list (or vector) of length 332
    return max(0, x[72])
def l210_73(x):
    # x is a list (or vector) of length 332
    return max(0, x[73])
def l210_74(x):
    # x is a list (or vector) of length 332
    return max(0, x[74])
def l210_75(x):
    # x is a list (or vector) of length 332
    return max(0, x[75])
def l210_76(x):
    # x is a list (or vector) of length 332
    return max(0, x[76])
def l210_77(x):
    # x is a list (or vector) of length 332
    return max(0, x[77])
def l210_78(x):
    # x is a list (or vector) of length 332
    return max(0, x[78])
def l210_79(x):
    # x is a list (or vector) of length 332
    return max(0, x[79])
def l210_80(x):
    # x is a list (or vector) of length 332
    return max(0, x[80])
def l210_81(x):
    # x is a list (or vector) of length 332
    return max(0, x[81])
def l210_82(x):
    # x is a list (or vector) of length 332
    return max(0, x[82])
def l210_83(x):
    # x is a list (or vector) of length 332
    return max(0, x[83])
def l210_84(x):
    # x is a list (or vector) of length 332
    return max(0, x[84])
def l210_85(x):
    # x is a list (or vector) of length 332
    return max(0, x[85])
def l210_86(x):
    # x is a list (or vector) of length 332
    return max(0, x[86])
def l210_87(x):
    # x is a list (or vector) of length 332
    return max(0, x[87])
def l210_88(x):
    # x is a list (or vector) of length 332
    return max(0, x[88])
def l210_89(x):
    # x is a list (or vector) of length 332
    return max(0, x[89])
def l210_90(x):
    # x is a list (or vector) of length 332
    return max(0, x[90])
def l210_91(x):
    # x is a list (or vector) of length 332
    return max(0, x[91])
def l210_92(x):
    # x is a list (or vector) of length 332
    return max(0, x[92])
def l210_93(x):
    # x is a list (or vector) of length 332
    return max(0, x[93])
def l210_94(x):
    # x is a list (or vector) of length 332
    return max(0, x[94])
def l210_95(x):
    # x is a list (or vector) of length 332
    return max(0, x[95])
def l210_96(x):
    # x is a list (or vector) of length 332
    return max(0, x[96])
def l210_97(x):
    # x is a list (or vector) of length 332
    return max(0, x[97])
def l210_98(x):
    # x is a list (or vector) of length 332
    return max(0, x[98])
def l210_99(x):
    # x is a list (or vector) of length 332
    return max(0, x[99])
def l210_100(x):
    # x is a list (or vector) of length 332
    return max(0, x[100])
def l210_101(x):
    # x is a list (or vector) of length 332
    return max(0, x[101])
def l210_102(x):
    # x is a list (or vector) of length 332
    return max(0, x[102])
def l210_103(x):
    # x is a list (or vector) of length 332
    return max(0, x[103])
def l210_104(x):
    # x is a list (or vector) of length 332
    return max(0, x[104])
def l210_105(x):
    # x is a list (or vector) of length 332
    return max(0, x[105])
def l210_106(x):
    # x is a list (or vector) of length 332
    return max(0, x[106])
def l210_107(x):
    # x is a list (or vector) of length 332
    return max(0, x[107])
def l210_108(x):
    # x is a list (or vector) of length 332
    return max(0, x[108])
def l210_109(x):
    # x is a list (or vector) of length 332
    return max(0, x[109])
def l210_110(x):
    # x is a list (or vector) of length 332
    return max(0, x[110])
def l210_111(x):
    # x is a list (or vector) of length 332
    return max(0, x[111])
def l210_112(x):
    # x is a list (or vector) of length 332
    return max(0, x[112])
def l210_113(x):
    # x is a list (or vector) of length 332
    return max(0, x[113])
def l210_114(x):
    # x is a list (or vector) of length 332
    return max(0, x[114])
def l210_115(x):
    # x is a list (or vector) of length 332
    return max(0, x[115])
def l210_116(x):
    # x is a list (or vector) of length 332
    return max(0, x[116])
def l210_117(x):
    # x is a list (or vector) of length 332
    return max(0, x[117])
def l210_118(x):
    # x is a list (or vector) of length 332
    return max(0, x[118])
def l210_119(x):
    # x is a list (or vector) of length 332
    return max(0, x[119])
def l210_120(x):
    # x is a list (or vector) of length 332
    return max(0, x[120])
def l210_121(x):
    # x is a list (or vector) of length 332
    return max(0, x[121])
def l210_122(x):
    # x is a list (or vector) of length 332
    return max(0, x[122])
def l210_123(x):
    # x is a list (or vector) of length 332
    return max(0, x[123])
def l210_124(x):
    # x is a list (or vector) of length 332
    return max(0, x[124])
def l210_125(x):
    # x is a list (or vector) of length 332
    return max(0, x[125])
def l210_126(x):
    # x is a list (or vector) of length 332
    return max(0, x[126])
def l210_127(x):
    # x is a list (or vector) of length 332
    return max(0, x[127])
def l210_128(x):
    # x is a list (or vector) of length 332
    return max(0, x[128] + -2.0*x[160])
def l210_129(x):
    # x is a list (or vector) of length 332
    return max(0, x[129] + -2.0*x[161])
def l210_130(x):
    # x is a list (or vector) of length 332
    return max(0, x[130] + -2.0*x[162])
def l210_131(x):
    # x is a list (or vector) of length 332
    return max(0, x[131] + -2.0*x[163])
def l210_132(x):
    # x is a list (or vector) of length 332
    return max(0, x[132] + -2.0*x[164])
def l210_133(x):
    # x is a list (or vector) of length 332
    return max(0, x[133] + -2.0*x[165])
def l210_134(x):
    # x is a list (or vector) of length 332
    return max(0, x[134] + -2.0*x[166])
def l210_135(x):
    # x is a list (or vector) of length 332
    return max(0, x[135] + -2.0*x[167])
def l210_136(x):
    # x is a list (or vector) of length 332
    return max(0, x[136] + -2.0*x[168])
def l210_137(x):
    # x is a list (or vector) of length 332
    return max(0, x[137] + -2.0*x[169])
def l210_138(x):
    # x is a list (or vector) of length 332
    return max(0, x[138] + -2.0*x[170])
def l210_139(x):
    # x is a list (or vector) of length 332
    return max(0, x[139] + -2.0*x[171])
def l210_140(x):
    # x is a list (or vector) of length 332
    return max(0, x[140] + -2.0*x[172])
def l210_141(x):
    # x is a list (or vector) of length 332
    return max(0, x[141] + -2.0*x[173])
def l210_142(x):
    # x is a list (or vector) of length 332
    return max(0, x[142] + -2.0*x[174])
def l210_143(x):
    # x is a list (or vector) of length 332
    return max(0, x[143] + -2.0*x[175])
def l210_144(x):
    # x is a list (or vector) of length 332
    return max(0, x[144] + -2.0*x[176])
def l210_145(x):
    # x is a list (or vector) of length 332
    return max(0, x[145] + -2.0*x[177])
def l210_146(x):
    # x is a list (or vector) of length 332
    return max(0, x[146] + -2.0*x[178])
def l210_147(x):
    # x is a list (or vector) of length 332
    return max(0, x[147] + -2.0*x[179])
def l210_148(x):
    # x is a list (or vector) of length 332
    return max(0, x[148] + -2.0*x[180])
def l210_149(x):
    # x is a list (or vector) of length 332
    return max(0, x[149] + -2.0*x[181])
def l210_150(x):
    # x is a list (or vector) of length 332
    return max(0, x[150] + -2.0*x[182])
def l210_151(x):
    # x is a list (or vector) of length 332
    return max(0, x[151] + -2.0*x[183])
def l210_152(x):
    # x is a list (or vector) of length 332
    return max(0, x[152] + -2.0*x[184])
def l210_153(x):
    # x is a list (or vector) of length 332
    return max(0, x[153] + -2.0*x[185])
def l210_154(x):
    # x is a list (or vector) of length 332
    return max(0, x[154] + -2.0*x[186])
def l210_155(x):
    # x is a list (or vector) of length 332
    return max(0, x[155] + -2.0*x[187])
def l210_156(x):
    # x is a list (or vector) of length 332
    return max(0, x[156] + -2.0*x[188])
def l210_157(x):
    # x is a list (or vector) of length 332
    return max(0, x[157] + -2.0*x[189])
def l210_158(x):
    # x is a list (or vector) of length 332
    return max(0, x[158] + -2.0*x[190])
def l210_159(x):
    # x is a list (or vector) of length 332
    return max(0, x[159] + -2.0*x[191])
def l210_160(x):
    # x is a list (or vector) of length 332
    return max(0, x[192])
def l210_161(x):
    # x is a list (or vector) of length 332
    return max(0, x[192] + x[225] + -1.0)
def l210_162(x):
    # x is a list (or vector) of length 332
    return max(0, x[193] + x[226] + -1.0)
def l210_163(x):
    # x is a list (or vector) of length 332
    return max(0, x[194] + x[227] + -1.0)
def l210_164(x):
    # x is a list (or vector) of length 332
    return max(0, x[195] + x[228] + -1.0)
def l210_165(x):
    # x is a list (or vector) of length 332
    return max(0, x[196] + x[229] + -1.0)
def l210_166(x):
    # x is a list (or vector) of length 332
    return max(0, x[197] + x[230] + -1.0)
def l210_167(x):
    # x is a list (or vector) of length 332
    return max(0, x[198] + x[231] + -1.0)
def l210_168(x):
    # x is a list (or vector) of length 332
    return max(0, x[199] + x[232] + -1.0)
def l210_169(x):
    # x is a list (or vector) of length 332
    return max(0, x[200] + x[233] + -1.0)
def l210_170(x):
    # x is a list (or vector) of length 332
    return max(0, x[201] + x[234] + -1.0)
def l210_171(x):
    # x is a list (or vector) of length 332
    return max(0, x[202] + x[235] + -1.0)
def l210_172(x):
    # x is a list (or vector) of length 332
    return max(0, x[203] + x[236] + -1.0)
def l210_173(x):
    # x is a list (or vector) of length 332
    return max(0, x[204] + x[237] + -1.0)
def l210_174(x):
    # x is a list (or vector) of length 332
    return max(0, x[205] + x[238] + -1.0)
def l210_175(x):
    # x is a list (or vector) of length 332
    return max(0, x[206] + x[239] + -1.0)
def l210_176(x):
    # x is a list (or vector) of length 332
    return max(0, x[207] + x[240] + -1.0)
def l210_177(x):
    # x is a list (or vector) of length 332
    return max(0, x[208] + x[241] + -1.0)
def l210_178(x):
    # x is a list (or vector) of length 332
    return max(0, x[209] + x[242] + -1.0)
def l210_179(x):
    # x is a list (or vector) of length 332
    return max(0, x[210] + x[243] + -1.0)
def l210_180(x):
    # x is a list (or vector) of length 332
    return max(0, x[211] + x[244] + -1.0)
def l210_181(x):
    # x is a list (or vector) of length 332
    return max(0, x[212] + x[245] + -1.0)
def l210_182(x):
    # x is a list (or vector) of length 332
    return max(0, x[213] + x[246] + -1.0)
def l210_183(x):
    # x is a list (or vector) of length 332
    return max(0, x[214] + x[247] + -1.0)
def l210_184(x):
    # x is a list (or vector) of length 332
    return max(0, x[215] + x[248] + -1.0)
def l210_185(x):
    # x is a list (or vector) of length 332
    return max(0, x[216] + x[249] + -1.0)
def l210_186(x):
    # x is a list (or vector) of length 332
    return max(0, x[217] + x[250] + -1.0)
def l210_187(x):
    # x is a list (or vector) of length 332
    return max(0, x[218] + x[251] + -1.0)
def l210_188(x):
    # x is a list (or vector) of length 332
    return max(0, x[219] + x[252] + -1.0)
def l210_189(x):
    # x is a list (or vector) of length 332
    return max(0, x[220] + x[253] + -1.0)
def l210_190(x):
    # x is a list (or vector) of length 332
    return max(0, x[221] + x[254] + -1.0)
def l210_191(x):
    # x is a list (or vector) of length 332
    return max(0, x[222] + x[255] + -1.0)
def l210_192(x):
    # x is a list (or vector) of length 332
    return max(0, x[193])
def l210_193(x):
    # x is a list (or vector) of length 332
    return max(0, x[194])
def l210_194(x):
    # x is a list (or vector) of length 332
    return max(0, x[195])
def l210_195(x):
    # x is a list (or vector) of length 332
    return max(0, x[196])
def l210_196(x):
    # x is a list (or vector) of length 332
    return max(0, x[197])
def l210_197(x):
    # x is a list (or vector) of length 332
    return max(0, x[198])
def l210_198(x):
    # x is a list (or vector) of length 332
    return max(0, x[199])
def l210_199(x):
    # x is a list (or vector) of length 332
    return max(0, x[200])
def l210_200(x):
    # x is a list (or vector) of length 332
    return max(0, x[201])
def l210_201(x):
    # x is a list (or vector) of length 332
    return max(0, x[202])
def l210_202(x):
    # x is a list (or vector) of length 332
    return max(0, x[203])
def l210_203(x):
    # x is a list (or vector) of length 332
    return max(0, x[204])
def l210_204(x):
    # x is a list (or vector) of length 332
    return max(0, x[205])
def l210_205(x):
    # x is a list (or vector) of length 332
    return max(0, x[206])
def l210_206(x):
    # x is a list (or vector) of length 332
    return max(0, x[207])
def l210_207(x):
    # x is a list (or vector) of length 332
    return max(0, x[208])
def l210_208(x):
    # x is a list (or vector) of length 332
    return max(0, x[209])
def l210_209(x):
    # x is a list (or vector) of length 332
    return max(0, x[210])
def l210_210(x):
    # x is a list (or vector) of length 332
    return max(0, x[211])
def l210_211(x):
    # x is a list (or vector) of length 332
    return max(0, x[212])
def l210_212(x):
    # x is a list (or vector) of length 332
    return max(0, x[213])
def l210_213(x):
    # x is a list (or vector) of length 332
    return max(0, x[214])
def l210_214(x):
    # x is a list (or vector) of length 332
    return max(0, x[215])
def l210_215(x):
    # x is a list (or vector) of length 332
    return max(0, x[216])
def l210_216(x):
    # x is a list (or vector) of length 332
    return max(0, x[217])
def l210_217(x):
    # x is a list (or vector) of length 332
    return max(0, x[218])
def l210_218(x):
    # x is a list (or vector) of length 332
    return max(0, x[219])
def l210_219(x):
    # x is a list (or vector) of length 332
    return max(0, x[220])
def l210_220(x):
    # x is a list (or vector) of length 332
    return max(0, x[221])
def l210_221(x):
    # x is a list (or vector) of length 332
    return max(0, x[222])
def l210_222(x):
    # x is a list (or vector) of length 332
    return max(0, x[223])
def l210_223(x):
    # x is a list (or vector) of length 332
    return max(0, x[224] + x[225] + -1.0)
def l210_224(x):
    # x is a list (or vector) of length 332
    return max(0, x[225] + x[226] + -1.0)
def l210_225(x):
    # x is a list (or vector) of length 332
    return max(0, x[226] + x[227] + -1.0)
def l210_226(x):
    # x is a list (or vector) of length 332
    return max(0, x[227] + x[228] + -1.0)
def l210_227(x):
    # x is a list (or vector) of length 332
    return max(0, x[228] + x[229] + -1.0)
def l210_228(x):
    # x is a list (or vector) of length 332
    return max(0, x[229] + x[230] + -1.0)
def l210_229(x):
    # x is a list (or vector) of length 332
    return max(0, x[230] + x[231] + -1.0)
def l210_230(x):
    # x is a list (or vector) of length 332
    return max(0, x[231] + x[232] + -1.0)
def l210_231(x):
    # x is a list (or vector) of length 332
    return max(0, x[232] + x[233] + -1.0)
def l210_232(x):
    # x is a list (or vector) of length 332
    return max(0, x[233] + x[234] + -1.0)
def l210_233(x):
    # x is a list (or vector) of length 332
    return max(0, x[234] + x[235] + -1.0)
def l210_234(x):
    # x is a list (or vector) of length 332
    return max(0, x[235] + x[236] + -1.0)
def l210_235(x):
    # x is a list (or vector) of length 332
    return max(0, x[236] + x[237] + -1.0)
def l210_236(x):
    # x is a list (or vector) of length 332
    return max(0, x[237] + x[238] + -1.0)
def l210_237(x):
    # x is a list (or vector) of length 332
    return max(0, x[238] + x[239] + -1.0)
def l210_238(x):
    # x is a list (or vector) of length 332
    return max(0, x[239] + x[240] + -1.0)
def l210_239(x):
    # x is a list (or vector) of length 332
    return max(0, x[240] + x[241] + -1.0)
def l210_240(x):
    # x is a list (or vector) of length 332
    return max(0, x[241] + x[242] + -1.0)
def l210_241(x):
    # x is a list (or vector) of length 332
    return max(0, x[242] + x[243] + -1.0)
def l210_242(x):
    # x is a list (or vector) of length 332
    return max(0, x[243] + x[244] + -1.0)
def l210_243(x):
    # x is a list (or vector) of length 332
    return max(0, x[244] + x[245] + -1.0)
def l210_244(x):
    # x is a list (or vector) of length 332
    return max(0, x[245] + x[246] + -1.0)
def l210_245(x):
    # x is a list (or vector) of length 332
    return max(0, x[246] + x[247] + -1.0)
def l210_246(x):
    # x is a list (or vector) of length 332
    return max(0, x[247] + x[248] + -1.0)
def l210_247(x):
    # x is a list (or vector) of length 332
    return max(0, x[248] + x[249] + -1.0)
def l210_248(x):
    # x is a list (or vector) of length 332
    return max(0, x[249] + x[250] + -1.0)
def l210_249(x):
    # x is a list (or vector) of length 332
    return max(0, x[250] + x[251] + -1.0)
def l210_250(x):
    # x is a list (or vector) of length 332
    return max(0, x[251] + x[252] + -1.0)
def l210_251(x):
    # x is a list (or vector) of length 332
    return max(0, x[252] + x[253] + -1.0)
def l210_252(x):
    # x is a list (or vector) of length 332
    return max(0, x[253] + x[254] + -1.0)
def l210_253(x):
    # x is a list (or vector) of length 332
    return max(0, x[254] + x[255] + -1.0)
def l210_254(x):
    # x is a list (or vector) of length 332
    return max(0, x[224])
def l210_255(x):
    # x is a list (or vector) of length 332
    return max(0, x[224])
def l210_256(x):
    # x is a list (or vector) of length 332
    return max(0, x[225])
def l210_257(x):
    # x is a list (or vector) of length 332
    return max(0, x[226])
def l210_258(x):
    # x is a list (or vector) of length 332
    return max(0, x[227])
def l210_259(x):
    # x is a list (or vector) of length 332
    return max(0, x[228])
def l210_260(x):
    # x is a list (or vector) of length 332
    return max(0, x[229])
def l210_261(x):
    # x is a list (or vector) of length 332
    return max(0, x[230])
def l210_262(x):
    # x is a list (or vector) of length 332
    return max(0, x[231])
def l210_263(x):
    # x is a list (or vector) of length 332
    return max(0, x[232])
def l210_264(x):
    # x is a list (or vector) of length 332
    return max(0, x[233])
def l210_265(x):
    # x is a list (or vector) of length 332
    return max(0, x[234])
def l210_266(x):
    # x is a list (or vector) of length 332
    return max(0, x[235])
def l210_267(x):
    # x is a list (or vector) of length 332
    return max(0, x[236])
def l210_268(x):
    # x is a list (or vector) of length 332
    return max(0, x[237])
def l210_269(x):
    # x is a list (or vector) of length 332
    return max(0, x[238])
def l210_270(x):
    # x is a list (or vector) of length 332
    return max(0, x[239])
def l210_271(x):
    # x is a list (or vector) of length 332
    return max(0, x[240])
def l210_272(x):
    # x is a list (or vector) of length 332
    return max(0, x[241])
def l210_273(x):
    # x is a list (or vector) of length 332
    return max(0, x[242])
def l210_274(x):
    # x is a list (or vector) of length 332
    return max(0, x[243])
def l210_275(x):
    # x is a list (or vector) of length 332
    return max(0, x[244])
def l210_276(x):
    # x is a list (or vector) of length 332
    return max(0, x[245])
def l210_277(x):
    # x is a list (or vector) of length 332
    return max(0, x[246])
def l210_278(x):
    # x is a list (or vector) of length 332
    return max(0, x[247])
def l210_279(x):
    # x is a list (or vector) of length 332
    return max(0, x[248])
def l210_280(x):
    # x is a list (or vector) of length 332
    return max(0, x[249])
def l210_281(x):
    # x is a list (or vector) of length 332
    return max(0, x[250])
def l210_282(x):
    # x is a list (or vector) of length 332
    return max(0, x[251])
def l210_283(x):
    # x is a list (or vector) of length 332
    return max(0, x[252])
def l210_284(x):
    # x is a list (or vector) of length 332
    return max(0, x[253])
def l210_285(x):
    # x is a list (or vector) of length 332
    return max(0, x[254])
def l210_286(x):
    # x is a list (or vector) of length 332
    return max(0, x[255])
def l210_287(x):
    # x is a list (or vector) of length 332
    return max(0, x[256])
def l210_288(x):
    # x is a list (or vector) of length 332
    return max(0, x[257])
def l210_289(x):
    # x is a list (or vector) of length 332
    return max(0, x[258])
def l210_290(x):
    # x is a list (or vector) of length 332
    return max(0, x[259])
def l210_291(x):
    # x is a list (or vector) of length 332
    return max(0, x[260])
def l210_292(x):
    # x is a list (or vector) of length 332
    return max(0, x[261])
def l210_293(x):
    # x is a list (or vector) of length 332
    return max(0, x[262])
def l210_294(x):
    # x is a list (or vector) of length 332
    return max(0, x[263])
def l210_295(x):
    # x is a list (or vector) of length 332
    return max(0, -1.0*x[264] + 32.0)
def l210_296(x):
    # x is a list (or vector) of length 332
    return max(0, -1.0*x[265] + 32.0)
def l210_297(x):
    # x is a list (or vector) of length 332
    return max(0, -1.0*x[266] + 32.0)
def l210_298(x):
    # x is a list (or vector) of length 332
    return max(0, -1.0*x[267] + 32.0)
def l210_299(x):
    # x is a list (or vector) of length 332
    return max(0, x[264])
def l210_300(x):
    # x is a list (or vector) of length 332
    return max(0, x[265])
def l210_301(x):
    # x is a list (or vector) of length 332
    return max(0, x[266])
def l210_302(x):
    # x is a list (or vector) of length 332
    return max(0, x[267])
def l210_303(x):
    # x is a list (or vector) of length 332
    return max(0, x[264] + -31.0)
def l210_304(x):
    # x is a list (or vector) of length 332
    return max(0, x[265] + -31.0)
def l210_305(x):
    # x is a list (or vector) of length 332
    return max(0, x[266] + -31.0)
def l210_306(x):
    # x is a list (or vector) of length 332
    return max(0, x[267] + -31.0)
def l210_307(x):
    # x is a list (or vector) of length 332
    return max(0, x[264] + -32.0)
def l210_308(x):
    # x is a list (or vector) of length 332
    return max(0, x[265] + -32.0)
def l210_309(x):
    # x is a list (or vector) of length 332
    return max(0, x[266] + -32.0)
def l210_310(x):
    # x is a list (or vector) of length 332
    return max(0, x[267] + -32.0)
def l210_311(x):
    # x is a list (or vector) of length 332
    return max(0, x[268])
def l210_312(x):
    # x is a list (or vector) of length 332
    return max(0, x[269])
def l210_313(x):
    # x is a list (or vector) of length 332
    return max(0, x[270])
def l210_314(x):
    # x is a list (or vector) of length 332
    return max(0, x[271])
def l210_315(x):
    # x is a list (or vector) of length 332
    return max(0, x[272])
def l210_316(x):
    # x is a list (or vector) of length 332
    return max(0, x[273])
def l210_317(x):
    # x is a list (or vector) of length 332
    return max(0, x[274])
def l210_318(x):
    # x is a list (or vector) of length 332
    return max(0, x[275])
def l210_319(x):
    # x is a list (or vector) of length 332
    return max(0, x[276])
def l210_320(x):
    # x is a list (or vector) of length 332
    return max(0, x[277])
def l210_321(x):
    # x is a list (or vector) of length 332
    return max(0, x[278])
def l210_322(x):
    # x is a list (or vector) of length 332
    return max(0, x[279])
def l210_323(x):
    # x is a list (or vector) of length 332
    return max(0, x[280])
def l210_324(x):
    # x is a list (or vector) of length 332
    return max(0, x[281])
def l210_325(x):
    # x is a list (or vector) of length 332
    return max(0, x[282])
def l210_326(x):
    # x is a list (or vector) of length 332
    return max(0, x[283])
def l210_327(x):
    # x is a list (or vector) of length 332
    return max(0, x[284])
def l210_328(x):
    # x is a list (or vector) of length 332
    return max(0, x[285])
def l210_329(x):
    # x is a list (or vector) of length 332
    return max(0, x[286])
def l210_330(x):
    # x is a list (or vector) of length 332
    return max(0, x[287])
def l210_331(x):
    # x is a list (or vector) of length 332
    return max(0, x[288])
def l210_332(x):
    # x is a list (or vector) of length 332
    return max(0, x[289])
def l210_333(x):
    # x is a list (or vector) of length 332
    return max(0, x[290])
def l210_334(x):
    # x is a list (or vector) of length 332
    return max(0, x[291])
def l210_335(x):
    # x is a list (or vector) of length 332
    return max(0, x[292])
def l210_336(x):
    # x is a list (or vector) of length 332
    return max(0, x[293])
def l210_337(x):
    # x is a list (or vector) of length 332
    return max(0, x[294])
def l210_338(x):
    # x is a list (or vector) of length 332
    return max(0, x[295])
def l210_339(x):
    # x is a list (or vector) of length 332
    return max(0, x[296])
def l210_340(x):
    # x is a list (or vector) of length 332
    return max(0, x[297])
def l210_341(x):
    # x is a list (or vector) of length 332
    return max(0, x[298])
def l210_342(x):
    # x is a list (or vector) of length 332
    return max(0, x[299])
def l210_343(x):
    # x is a list (or vector) of length 332
    return max(0, x[300])
def l210_344(x):
    # x is a list (or vector) of length 332
    return max(0, x[301])
def l210_345(x):
    # x is a list (or vector) of length 332
    return max(0, x[302])
def l210_346(x):
    # x is a list (or vector) of length 332
    return max(0, x[303])
def l210_347(x):
    # x is a list (or vector) of length 332
    return max(0, x[304])
def l210_348(x):
    # x is a list (or vector) of length 332
    return max(0, x[305])
def l210_349(x):
    # x is a list (or vector) of length 332
    return max(0, x[306])
def l210_350(x):
    # x is a list (or vector) of length 332
    return max(0, x[307])
def l210_351(x):
    # x is a list (or vector) of length 332
    return max(0, x[308])
def l210_352(x):
    # x is a list (or vector) of length 332
    return max(0, x[309])
def l210_353(x):
    # x is a list (or vector) of length 332
    return max(0, x[310])
def l210_354(x):
    # x is a list (or vector) of length 332
    return max(0, x[311])
def l210_355(x):
    # x is a list (or vector) of length 332
    return max(0, x[312])
def l210_356(x):
    # x is a list (or vector) of length 332
    return max(0, x[313])
def l210_357(x):
    # x is a list (or vector) of length 332
    return max(0, x[314])
def l210_358(x):
    # x is a list (or vector) of length 332
    return max(0, x[315])
def l210_359(x):
    # x is a list (or vector) of length 332
    return max(0, x[316])
def l210_360(x):
    # x is a list (or vector) of length 332
    return max(0, x[317])
def l210_361(x):
    # x is a list (or vector) of length 332
    return max(0, x[318])
def l210_362(x):
    # x is a list (or vector) of length 332
    return max(0, x[319])
def l210_363(x):
    # x is a list (or vector) of length 332
    return max(0, x[320])
def l210_364(x):
    # x is a list (or vector) of length 332
    return max(0, x[321])
def l210_365(x):
    # x is a list (or vector) of length 332
    return max(0, x[322])
def l210_366(x):
    # x is a list (or vector) of length 332
    return max(0, x[323])
def l210_367(x):
    # x is a list (or vector) of length 332
    return max(0, x[324])
def l210_368(x):
    # x is a list (or vector) of length 332
    return max(0, x[325])
def l210_369(x):
    # x is a list (or vector) of length 332
    return max(0, x[326])
def l210_370(x):
    # x is a list (or vector) of length 332
    return max(0, x[327])
def l210_371(x):
    # x is a list (or vector) of length 332
    return max(0, x[328])
def l210_372(x):
    # x is a list (or vector) of length 332
    return max(0, x[329])
def l210_373(x):
    # x is a list (or vector) of length 332
    return max(0, x[330])
def l210_374(x):
    # x is a list (or vector) of length 332
    return max(0, x[331])
def l210_(x):
    # x is a list (or vector) of length 332
    return [
        l210_0(x),
        l210_1(x),
        l210_2(x),
        l210_3(x),
        l210_4(x),
        l210_5(x),
        l210_6(x),
        l210_7(x),
        l210_8(x),
        l210_9(x),
        l210_10(x),
        l210_11(x),
        l210_12(x),
        l210_13(x),
        l210_14(x),
        l210_15(x),
        l210_16(x),
        l210_17(x),
        l210_18(x),
        l210_19(x),
        l210_20(x),
        l210_21(x),
        l210_22(x),
        l210_23(x),
        l210_24(x),
        l210_25(x),
        l210_26(x),
        l210_27(x),
        l210_28(x),
        l210_29(x),
        l210_30(x),
        l210_31(x),
        l210_32(x),
        l210_33(x),
        l210_34(x),
        l210_35(x),
        l210_36(x),
        l210_37(x),
        l210_38(x),
        l210_39(x),
        l210_40(x),
        l210_41(x),
        l210_42(x),
        l210_43(x),
        l210_44(x),
        l210_45(x),
        l210_46(x),
        l210_47(x),
        l210_48(x),
        l210_49(x),
        l210_50(x),
        l210_51(x),
        l210_52(x),
        l210_53(x),
        l210_54(x),
        l210_55(x),
        l210_56(x),
        l210_57(x),
        l210_58(x),
        l210_59(x),
        l210_60(x),
        l210_61(x),
        l210_62(x),
        l210_63(x),
        l210_64(x),
        l210_65(x),
        l210_66(x),
        l210_67(x),
        l210_68(x),
        l210_69(x),
        l210_70(x),
        l210_71(x),
        l210_72(x),
        l210_73(x),
        l210_74(x),
        l210_75(x),
        l210_76(x),
        l210_77(x),
        l210_78(x),
        l210_79(x),
        l210_80(x),
        l210_81(x),
        l210_82(x),
        l210_83(x),
        l210_84(x),
        l210_85(x),
        l210_86(x),
        l210_87(x),
        l210_88(x),
        l210_89(x),
        l210_90(x),
        l210_91(x),
        l210_92(x),
        l210_93(x),
        l210_94(x),
        l210_95(x),
        l210_96(x),
        l210_97(x),
        l210_98(x),
        l210_99(x),
        l210_100(x),
        l210_101(x),
        l210_102(x),
        l210_103(x),
        l210_104(x),
        l210_105(x),
        l210_106(x),
        l210_107(x),
        l210_108(x),
        l210_109(x),
        l210_110(x),
        l210_111(x),
        l210_112(x),
        l210_113(x),
        l210_114(x),
        l210_115(x),
        l210_116(x),
        l210_117(x),
        l210_118(x),
        l210_119(x),
        l210_120(x),
        l210_121(x),
        l210_122(x),
        l210_123(x),
        l210_124(x),
        l210_125(x),
        l210_126(x),
        l210_127(x),
        l210_128(x),
        l210_129(x),
        l210_130(x),
        l210_131(x),
        l210_132(x),
        l210_133(x),
        l210_134(x),
        l210_135(x),
        l210_136(x),
        l210_137(x),
        l210_138(x),
        l210_139(x),
        l210_140(x),
        l210_141(x),
        l210_142(x),
        l210_143(x),
        l210_144(x),
        l210_145(x),
        l210_146(x),
        l210_147(x),
        l210_148(x),
        l210_149(x),
        l210_150(x),
        l210_151(x),
        l210_152(x),
        l210_153(x),
        l210_154(x),
        l210_155(x),
        l210_156(x),
        l210_157(x),
        l210_158(x),
        l210_159(x),
        l210_160(x),
        l210_161(x),
        l210_162(x),
        l210_163(x),
        l210_164(x),
        l210_165(x),
        l210_166(x),
        l210_167(x),
        l210_168(x),
        l210_169(x),
        l210_170(x),
        l210_171(x),
        l210_172(x),
        l210_173(x),
        l210_174(x),
        l210_175(x),
        l210_176(x),
        l210_177(x),
        l210_178(x),
        l210_179(x),
        l210_180(x),
        l210_181(x),
        l210_182(x),
        l210_183(x),
        l210_184(x),
        l210_185(x),
        l210_186(x),
        l210_187(x),
        l210_188(x),
        l210_189(x),
        l210_190(x),
        l210_191(x),
        l210_192(x),
        l210_193(x),
        l210_194(x),
        l210_195(x),
        l210_196(x),
        l210_197(x),
        l210_198(x),
        l210_199(x),
        l210_200(x),
        l210_201(x),
        l210_202(x),
        l210_203(x),
        l210_204(x),
        l210_205(x),
        l210_206(x),
        l210_207(x),
        l210_208(x),
        l210_209(x),
        l210_210(x),
        l210_211(x),
        l210_212(x),
        l210_213(x),
        l210_214(x),
        l210_215(x),
        l210_216(x),
        l210_217(x),
        l210_218(x),
        l210_219(x),
        l210_220(x),
        l210_221(x),
        l210_222(x),
        l210_223(x),
        l210_224(x),
        l210_225(x),
        l210_226(x),
        l210_227(x),
        l210_228(x),
        l210_229(x),
        l210_230(x),
        l210_231(x),
        l210_232(x),
        l210_233(x),
        l210_234(x),
        l210_235(x),
        l210_236(x),
        l210_237(x),
        l210_238(x),
        l210_239(x),
        l210_240(x),
        l210_241(x),
        l210_242(x),
        l210_243(x),
        l210_244(x),
        l210_245(x),
        l210_246(x),
        l210_247(x),
        l210_248(x),
        l210_249(x),
        l210_250(x),
        l210_251(x),
        l210_252(x),
        l210_253(x),
        l210_254(x),
        l210_255(x),
        l210_256(x),
        l210_257(x),
        l210_258(x),
        l210_259(x),
        l210_260(x),
        l210_261(x),
        l210_262(x),
        l210_263(x),
        l210_264(x),
        l210_265(x),
        l210_266(x),
        l210_267(x),
        l210_268(x),
        l210_269(x),
        l210_270(x),
        l210_271(x),
        l210_272(x),
        l210_273(x),
        l210_274(x),
        l210_275(x),
        l210_276(x),
        l210_277(x),
        l210_278(x),
        l210_279(x),
        l210_280(x),
        l210_281(x),
        l210_282(x),
        l210_283(x),
        l210_284(x),
        l210_285(x),
        l210_286(x),
        l210_287(x),
        l210_288(x),
        l210_289(x),
        l210_290(x),
        l210_291(x),
        l210_292(x),
        l210_293(x),
        l210_294(x),
        l210_295(x),
        l210_296(x),
        l210_297(x),
        l210_298(x),
        l210_299(x),
        l210_300(x),
        l210_301(x),
        l210_302(x),
        l210_303(x),
        l210_304(x),
        l210_305(x),
        l210_306(x),
        l210_307(x),
        l210_308(x),
        l210_309(x),
        l210_310(x),
        l210_311(x),
        l210_312(x),
        l210_313(x),
        l210_314(x),
        l210_315(x),
        l210_316(x),
        l210_317(x),
        l210_318(x),
        l210_319(x),
        l210_320(x),
        l210_321(x),
        l210_322(x),
        l210_323(x),
        l210_324(x),
        l210_325(x),
        l210_326(x),
        l210_327(x),
        l210_328(x),
        l210_329(x),
        l210_330(x),
        l210_331(x),
        l210_332(x),
        l210_333(x),
        l210_334(x),
        l210_335(x),
        l210_336(x),
        l210_337(x),
        l210_338(x),
        l210_339(x),
        l210_340(x),
        l210_341(x),
        l210_342(x),
        l210_343(x),
        l210_344(x),
        l210_345(x),
        l210_346(x),
        l210_347(x),
        l210_348(x),
        l210_349(x),
        l210_350(x),
        l210_351(x),
        l210_352(x),
        l210_353(x),
        l210_354(x),
        l210_355(x),
        l210_356(x),
        l210_357(x),
        l210_358(x),
        l210_359(x),
        l210_360(x),
        l210_361(x),
        l210_362(x),
        l210_363(x),
        l210_364(x),
        l210_365(x),
        l210_366(x),
        l210_367(x),
        l210_368(x),
        l210_369(x),
        l210_370(x),
        l210_371(x),
        l210_372(x),
        l210_373(x),
        l210_374(x),
    ]