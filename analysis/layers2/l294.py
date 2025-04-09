import numpy as np




# Generated from reverse engineering
def l294_g(x: np.ndarray) -> np.ndarray:
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




def l294_0(x):
    # x is a list (or vector) of length 332
    return max(0, x[0])
def l294_1(x):
    # x is a list (or vector) of length 332
    return max(0, x[1])
def l294_2(x):
    # x is a list (or vector) of length 332
    return max(0, x[2])
def l294_3(x):
    # x is a list (or vector) of length 332
    return max(0, x[3])
def l294_4(x):
    # x is a list (or vector) of length 332
    return max(0, x[4])
def l294_5(x):
    # x is a list (or vector) of length 332
    return max(0, x[5])
def l294_6(x):
    # x is a list (or vector) of length 332
    return max(0, x[6])
def l294_7(x):
    # x is a list (or vector) of length 332
    return max(0, x[7])
def l294_8(x):
    # x is a list (or vector) of length 332
    return max(0, x[8])
def l294_9(x):
    # x is a list (or vector) of length 332
    return max(0, x[9])
def l294_10(x):
    # x is a list (or vector) of length 332
    return max(0, x[10])
def l294_11(x):
    # x is a list (or vector) of length 332
    return max(0, x[11])
def l294_12(x):
    # x is a list (or vector) of length 332
    return max(0, x[12])
def l294_13(x):
    # x is a list (or vector) of length 332
    return max(0, x[13])
def l294_14(x):
    # x is a list (or vector) of length 332
    return max(0, x[14])
def l294_15(x):
    # x is a list (or vector) of length 332
    return max(0, x[15])
def l294_16(x):
    # x is a list (or vector) of length 332
    return max(0, x[16])
def l294_17(x):
    # x is a list (or vector) of length 332
    return max(0, x[17])
def l294_18(x):
    # x is a list (or vector) of length 332
    return max(0, x[18])
def l294_19(x):
    # x is a list (or vector) of length 332
    return max(0, x[19])
def l294_20(x):
    # x is a list (or vector) of length 332
    return max(0, x[20])
def l294_21(x):
    # x is a list (or vector) of length 332
    return max(0, x[21])
def l294_22(x):
    # x is a list (or vector) of length 332
    return max(0, x[22])
def l294_23(x):
    # x is a list (or vector) of length 332
    return max(0, x[23])
def l294_24(x):
    # x is a list (or vector) of length 332
    return max(0, x[24])
def l294_25(x):
    # x is a list (or vector) of length 332
    return max(0, x[25])
def l294_26(x):
    # x is a list (or vector) of length 332
    return max(0, x[26])
def l294_27(x):
    # x is a list (or vector) of length 332
    return max(0, x[27])
def l294_28(x):
    # x is a list (or vector) of length 332
    return max(0, x[28])
def l294_29(x):
    # x is a list (or vector) of length 332
    return max(0, x[29])
def l294_30(x):
    # x is a list (or vector) of length 332
    return max(0, x[30])
def l294_31(x):
    # x is a list (or vector) of length 332
    return max(0, x[31])
def l294_32(x):
    # x is a list (or vector) of length 332
    return max(0, x[32])
def l294_33(x):
    # x is a list (or vector) of length 332
    return max(0, x[33])
def l294_34(x):
    # x is a list (or vector) of length 332
    return max(0, x[34])
def l294_35(x):
    # x is a list (or vector) of length 332
    return max(0, x[35])
def l294_36(x):
    # x is a list (or vector) of length 332
    return max(0, x[36])
def l294_37(x):
    # x is a list (or vector) of length 332
    return max(0, x[37])
def l294_38(x):
    # x is a list (or vector) of length 332
    return max(0, x[38])
def l294_39(x):
    # x is a list (or vector) of length 332
    return max(0, x[39])
def l294_40(x):
    # x is a list (or vector) of length 332
    return max(0, x[40])
def l294_41(x):
    # x is a list (or vector) of length 332
    return max(0, x[41])
def l294_42(x):
    # x is a list (or vector) of length 332
    return max(0, x[42])
def l294_43(x):
    # x is a list (or vector) of length 332
    return max(0, x[43])
def l294_44(x):
    # x is a list (or vector) of length 332
    return max(0, x[44])
def l294_45(x):
    # x is a list (or vector) of length 332
    return max(0, x[45])
def l294_46(x):
    # x is a list (or vector) of length 332
    return max(0, x[46])
def l294_47(x):
    # x is a list (or vector) of length 332
    return max(0, x[47])
def l294_48(x):
    # x is a list (or vector) of length 332
    return max(0, x[48])
def l294_49(x):
    # x is a list (or vector) of length 332
    return max(0, x[49])
def l294_50(x):
    # x is a list (or vector) of length 332
    return max(0, x[50])
def l294_51(x):
    # x is a list (or vector) of length 332
    return max(0, x[51])
def l294_52(x):
    # x is a list (or vector) of length 332
    return max(0, x[52])
def l294_53(x):
    # x is a list (or vector) of length 332
    return max(0, x[53])
def l294_54(x):
    # x is a list (or vector) of length 332
    return max(0, x[54])
def l294_55(x):
    # x is a list (or vector) of length 332
    return max(0, x[55])
def l294_56(x):
    # x is a list (or vector) of length 332
    return max(0, x[56])
def l294_57(x):
    # x is a list (or vector) of length 332
    return max(0, x[57])
def l294_58(x):
    # x is a list (or vector) of length 332
    return max(0, x[58])
def l294_59(x):
    # x is a list (or vector) of length 332
    return max(0, x[59])
def l294_60(x):
    # x is a list (or vector) of length 332
    return max(0, x[60])
def l294_61(x):
    # x is a list (or vector) of length 332
    return max(0, x[61])
def l294_62(x):
    # x is a list (or vector) of length 332
    return max(0, x[62])
def l294_63(x):
    # x is a list (or vector) of length 332
    return max(0, x[63])
def l294_64(x):
    # x is a list (or vector) of length 332
    return max(0, x[64])
def l294_65(x):
    # x is a list (or vector) of length 332
    return max(0, x[65])
def l294_66(x):
    # x is a list (or vector) of length 332
    return max(0, x[66])
def l294_67(x):
    # x is a list (or vector) of length 332
    return max(0, x[67])
def l294_68(x):
    # x is a list (or vector) of length 332
    return max(0, x[68])
def l294_69(x):
    # x is a list (or vector) of length 332
    return max(0, x[69])
def l294_70(x):
    # x is a list (or vector) of length 332
    return max(0, x[70])
def l294_71(x):
    # x is a list (or vector) of length 332
    return max(0, x[71])
def l294_72(x):
    # x is a list (or vector) of length 332
    return max(0, x[72])
def l294_73(x):
    # x is a list (or vector) of length 332
    return max(0, x[73])
def l294_74(x):
    # x is a list (or vector) of length 332
    return max(0, x[74])
def l294_75(x):
    # x is a list (or vector) of length 332
    return max(0, x[75])
def l294_76(x):
    # x is a list (or vector) of length 332
    return max(0, x[76])
def l294_77(x):
    # x is a list (or vector) of length 332
    return max(0, x[77])
def l294_78(x):
    # x is a list (or vector) of length 332
    return max(0, x[78])
def l294_79(x):
    # x is a list (or vector) of length 332
    return max(0, x[79])
def l294_80(x):
    # x is a list (or vector) of length 332
    return max(0, x[80])
def l294_81(x):
    # x is a list (or vector) of length 332
    return max(0, x[81])
def l294_82(x):
    # x is a list (or vector) of length 332
    return max(0, x[82])
def l294_83(x):
    # x is a list (or vector) of length 332
    return max(0, x[83])
def l294_84(x):
    # x is a list (or vector) of length 332
    return max(0, x[84])
def l294_85(x):
    # x is a list (or vector) of length 332
    return max(0, x[85])
def l294_86(x):
    # x is a list (or vector) of length 332
    return max(0, x[86])
def l294_87(x):
    # x is a list (or vector) of length 332
    return max(0, x[87])
def l294_88(x):
    # x is a list (or vector) of length 332
    return max(0, x[88])
def l294_89(x):
    # x is a list (or vector) of length 332
    return max(0, x[89])
def l294_90(x):
    # x is a list (or vector) of length 332
    return max(0, x[90])
def l294_91(x):
    # x is a list (or vector) of length 332
    return max(0, x[91])
def l294_92(x):
    # x is a list (or vector) of length 332
    return max(0, x[92])
def l294_93(x):
    # x is a list (or vector) of length 332
    return max(0, x[93])
def l294_94(x):
    # x is a list (or vector) of length 332
    return max(0, x[94])
def l294_95(x):
    # x is a list (or vector) of length 332
    return max(0, x[95])
def l294_96(x):
    # x is a list (or vector) of length 332
    return max(0, x[96])
def l294_97(x):
    # x is a list (or vector) of length 332
    return max(0, x[97])
def l294_98(x):
    # x is a list (or vector) of length 332
    return max(0, x[98])
def l294_99(x):
    # x is a list (or vector) of length 332
    return max(0, x[99])
def l294_100(x):
    # x is a list (or vector) of length 332
    return max(0, x[100])
def l294_101(x):
    # x is a list (or vector) of length 332
    return max(0, x[101])
def l294_102(x):
    # x is a list (or vector) of length 332
    return max(0, x[102])
def l294_103(x):
    # x is a list (or vector) of length 332
    return max(0, x[103])
def l294_104(x):
    # x is a list (or vector) of length 332
    return max(0, x[104])
def l294_105(x):
    # x is a list (or vector) of length 332
    return max(0, x[105])
def l294_106(x):
    # x is a list (or vector) of length 332
    return max(0, x[106])
def l294_107(x):
    # x is a list (or vector) of length 332
    return max(0, x[107])
def l294_108(x):
    # x is a list (or vector) of length 332
    return max(0, x[108])
def l294_109(x):
    # x is a list (or vector) of length 332
    return max(0, x[109])
def l294_110(x):
    # x is a list (or vector) of length 332
    return max(0, x[110])
def l294_111(x):
    # x is a list (or vector) of length 332
    return max(0, x[111])
def l294_112(x):
    # x is a list (or vector) of length 332
    return max(0, x[112])
def l294_113(x):
    # x is a list (or vector) of length 332
    return max(0, x[113])
def l294_114(x):
    # x is a list (or vector) of length 332
    return max(0, x[114])
def l294_115(x):
    # x is a list (or vector) of length 332
    return max(0, x[115])
def l294_116(x):
    # x is a list (or vector) of length 332
    return max(0, x[116])
def l294_117(x):
    # x is a list (or vector) of length 332
    return max(0, x[117])
def l294_118(x):
    # x is a list (or vector) of length 332
    return max(0, x[118])
def l294_119(x):
    # x is a list (or vector) of length 332
    return max(0, x[119])
def l294_120(x):
    # x is a list (or vector) of length 332
    return max(0, x[120])
def l294_121(x):
    # x is a list (or vector) of length 332
    return max(0, x[121])
def l294_122(x):
    # x is a list (or vector) of length 332
    return max(0, x[122])
def l294_123(x):
    # x is a list (or vector) of length 332
    return max(0, x[123])
def l294_124(x):
    # x is a list (or vector) of length 332
    return max(0, x[124])
def l294_125(x):
    # x is a list (or vector) of length 332
    return max(0, x[125])
def l294_126(x):
    # x is a list (or vector) of length 332
    return max(0, x[126])
def l294_127(x):
    # x is a list (or vector) of length 332
    return max(0, x[127])
def l294_128(x):
    # x is a list (or vector) of length 332
    return max(0, x[128] + -2.0*x[160])
def l294_129(x):
    # x is a list (or vector) of length 332
    return max(0, x[129] + -2.0*x[161])
def l294_130(x):
    # x is a list (or vector) of length 332
    return max(0, x[130] + -2.0*x[162])
def l294_131(x):
    # x is a list (or vector) of length 332
    return max(0, x[131] + -2.0*x[163])
def l294_132(x):
    # x is a list (or vector) of length 332
    return max(0, x[132] + -2.0*x[164])
def l294_133(x):
    # x is a list (or vector) of length 332
    return max(0, x[133] + -2.0*x[165])
def l294_134(x):
    # x is a list (or vector) of length 332
    return max(0, x[134] + -2.0*x[166])
def l294_135(x):
    # x is a list (or vector) of length 332
    return max(0, x[135] + -2.0*x[167])
def l294_136(x):
    # x is a list (or vector) of length 332
    return max(0, x[136] + -2.0*x[168])
def l294_137(x):
    # x is a list (or vector) of length 332
    return max(0, x[137] + -2.0*x[169])
def l294_138(x):
    # x is a list (or vector) of length 332
    return max(0, x[138] + -2.0*x[170])
def l294_139(x):
    # x is a list (or vector) of length 332
    return max(0, x[139] + -2.0*x[171])
def l294_140(x):
    # x is a list (or vector) of length 332
    return max(0, x[140] + -2.0*x[172])
def l294_141(x):
    # x is a list (or vector) of length 332
    return max(0, x[141] + -2.0*x[173])
def l294_142(x):
    # x is a list (or vector) of length 332
    return max(0, x[142] + -2.0*x[174])
def l294_143(x):
    # x is a list (or vector) of length 332
    return max(0, x[143] + -2.0*x[175])
def l294_144(x):
    # x is a list (or vector) of length 332
    return max(0, x[144] + -2.0*x[176])
def l294_145(x):
    # x is a list (or vector) of length 332
    return max(0, x[145] + -2.0*x[177])
def l294_146(x):
    # x is a list (or vector) of length 332
    return max(0, x[146] + -2.0*x[178])
def l294_147(x):
    # x is a list (or vector) of length 332
    return max(0, x[147] + -2.0*x[179])
def l294_148(x):
    # x is a list (or vector) of length 332
    return max(0, x[148] + -2.0*x[180])
def l294_149(x):
    # x is a list (or vector) of length 332
    return max(0, x[149] + -2.0*x[181])
def l294_150(x):
    # x is a list (or vector) of length 332
    return max(0, x[150] + -2.0*x[182])
def l294_151(x):
    # x is a list (or vector) of length 332
    return max(0, x[151] + -2.0*x[183])
def l294_152(x):
    # x is a list (or vector) of length 332
    return max(0, x[152] + -2.0*x[184])
def l294_153(x):
    # x is a list (or vector) of length 332
    return max(0, x[153] + -2.0*x[185])
def l294_154(x):
    # x is a list (or vector) of length 332
    return max(0, x[154] + -2.0*x[186])
def l294_155(x):
    # x is a list (or vector) of length 332
    return max(0, x[155] + -2.0*x[187])
def l294_156(x):
    # x is a list (or vector) of length 332
    return max(0, x[156] + -2.0*x[188])
def l294_157(x):
    # x is a list (or vector) of length 332
    return max(0, x[157] + -2.0*x[189])
def l294_158(x):
    # x is a list (or vector) of length 332
    return max(0, x[158] + -2.0*x[190])
def l294_159(x):
    # x is a list (or vector) of length 332
    return max(0, x[159] + -2.0*x[191])
def l294_160(x):
    # x is a list (or vector) of length 332
    return max(0, x[192])
def l294_161(x):
    # x is a list (or vector) of length 332
    return max(0, x[192] + x[225] + -1.0)
def l294_162(x):
    # x is a list (or vector) of length 332
    return max(0, x[193] + x[226] + -1.0)
def l294_163(x):
    # x is a list (or vector) of length 332
    return max(0, x[194] + x[227] + -1.0)
def l294_164(x):
    # x is a list (or vector) of length 332
    return max(0, x[195] + x[228] + -1.0)
def l294_165(x):
    # x is a list (or vector) of length 332
    return max(0, x[196] + x[229] + -1.0)
def l294_166(x):
    # x is a list (or vector) of length 332
    return max(0, x[197] + x[230] + -1.0)
def l294_167(x):
    # x is a list (or vector) of length 332
    return max(0, x[198] + x[231] + -1.0)
def l294_168(x):
    # x is a list (or vector) of length 332
    return max(0, x[199] + x[232] + -1.0)
def l294_169(x):
    # x is a list (or vector) of length 332
    return max(0, x[200] + x[233] + -1.0)
def l294_170(x):
    # x is a list (or vector) of length 332
    return max(0, x[201] + x[234] + -1.0)
def l294_171(x):
    # x is a list (or vector) of length 332
    return max(0, x[202] + x[235] + -1.0)
def l294_172(x):
    # x is a list (or vector) of length 332
    return max(0, x[203] + x[236] + -1.0)
def l294_173(x):
    # x is a list (or vector) of length 332
    return max(0, x[204] + x[237] + -1.0)
def l294_174(x):
    # x is a list (or vector) of length 332
    return max(0, x[205] + x[238] + -1.0)
def l294_175(x):
    # x is a list (or vector) of length 332
    return max(0, x[206] + x[239] + -1.0)
def l294_176(x):
    # x is a list (or vector) of length 332
    return max(0, x[207] + x[240] + -1.0)
def l294_177(x):
    # x is a list (or vector) of length 332
    return max(0, x[208] + x[241] + -1.0)
def l294_178(x):
    # x is a list (or vector) of length 332
    return max(0, x[209] + x[242] + -1.0)
def l294_179(x):
    # x is a list (or vector) of length 332
    return max(0, x[210] + x[243] + -1.0)
def l294_180(x):
    # x is a list (or vector) of length 332
    return max(0, x[211] + x[244] + -1.0)
def l294_181(x):
    # x is a list (or vector) of length 332
    return max(0, x[212] + x[245] + -1.0)
def l294_182(x):
    # x is a list (or vector) of length 332
    return max(0, x[213] + x[246] + -1.0)
def l294_183(x):
    # x is a list (or vector) of length 332
    return max(0, x[214] + x[247] + -1.0)
def l294_184(x):
    # x is a list (or vector) of length 332
    return max(0, x[215] + x[248] + -1.0)
def l294_185(x):
    # x is a list (or vector) of length 332
    return max(0, x[216] + x[249] + -1.0)
def l294_186(x):
    # x is a list (or vector) of length 332
    return max(0, x[217] + x[250] + -1.0)
def l294_187(x):
    # x is a list (or vector) of length 332
    return max(0, x[218] + x[251] + -1.0)
def l294_188(x):
    # x is a list (or vector) of length 332
    return max(0, x[219] + x[252] + -1.0)
def l294_189(x):
    # x is a list (or vector) of length 332
    return max(0, x[220] + x[253] + -1.0)
def l294_190(x):
    # x is a list (or vector) of length 332
    return max(0, x[221] + x[254] + -1.0)
def l294_191(x):
    # x is a list (or vector) of length 332
    return max(0, x[222] + x[255] + -1.0)
def l294_192(x):
    # x is a list (or vector) of length 332
    return max(0, x[193])
def l294_193(x):
    # x is a list (or vector) of length 332
    return max(0, x[194])
def l294_194(x):
    # x is a list (or vector) of length 332
    return max(0, x[195])
def l294_195(x):
    # x is a list (or vector) of length 332
    return max(0, x[196])
def l294_196(x):
    # x is a list (or vector) of length 332
    return max(0, x[197])
def l294_197(x):
    # x is a list (or vector) of length 332
    return max(0, x[198])
def l294_198(x):
    # x is a list (or vector) of length 332
    return max(0, x[199])
def l294_199(x):
    # x is a list (or vector) of length 332
    return max(0, x[200])
def l294_200(x):
    # x is a list (or vector) of length 332
    return max(0, x[201])
def l294_201(x):
    # x is a list (or vector) of length 332
    return max(0, x[202])
def l294_202(x):
    # x is a list (or vector) of length 332
    return max(0, x[203])
def l294_203(x):
    # x is a list (or vector) of length 332
    return max(0, x[204])
def l294_204(x):
    # x is a list (or vector) of length 332
    return max(0, x[205])
def l294_205(x):
    # x is a list (or vector) of length 332
    return max(0, x[206])
def l294_206(x):
    # x is a list (or vector) of length 332
    return max(0, x[207])
def l294_207(x):
    # x is a list (or vector) of length 332
    return max(0, x[208])
def l294_208(x):
    # x is a list (or vector) of length 332
    return max(0, x[209])
def l294_209(x):
    # x is a list (or vector) of length 332
    return max(0, x[210])
def l294_210(x):
    # x is a list (or vector) of length 332
    return max(0, x[211])
def l294_211(x):
    # x is a list (or vector) of length 332
    return max(0, x[212])
def l294_212(x):
    # x is a list (or vector) of length 332
    return max(0, x[213])
def l294_213(x):
    # x is a list (or vector) of length 332
    return max(0, x[214])
def l294_214(x):
    # x is a list (or vector) of length 332
    return max(0, x[215])
def l294_215(x):
    # x is a list (or vector) of length 332
    return max(0, x[216])
def l294_216(x):
    # x is a list (or vector) of length 332
    return max(0, x[217])
def l294_217(x):
    # x is a list (or vector) of length 332
    return max(0, x[218])
def l294_218(x):
    # x is a list (or vector) of length 332
    return max(0, x[219])
def l294_219(x):
    # x is a list (or vector) of length 332
    return max(0, x[220])
def l294_220(x):
    # x is a list (or vector) of length 332
    return max(0, x[221])
def l294_221(x):
    # x is a list (or vector) of length 332
    return max(0, x[222])
def l294_222(x):
    # x is a list (or vector) of length 332
    return max(0, x[223])
def l294_223(x):
    # x is a list (or vector) of length 332
    return max(0, x[224] + x[225] + -1.0)
def l294_224(x):
    # x is a list (or vector) of length 332
    return max(0, x[225] + x[226] + -1.0)
def l294_225(x):
    # x is a list (or vector) of length 332
    return max(0, x[226] + x[227] + -1.0)
def l294_226(x):
    # x is a list (or vector) of length 332
    return max(0, x[227] + x[228] + -1.0)
def l294_227(x):
    # x is a list (or vector) of length 332
    return max(0, x[228] + x[229] + -1.0)
def l294_228(x):
    # x is a list (or vector) of length 332
    return max(0, x[229] + x[230] + -1.0)
def l294_229(x):
    # x is a list (or vector) of length 332
    return max(0, x[230] + x[231] + -1.0)
def l294_230(x):
    # x is a list (or vector) of length 332
    return max(0, x[231] + x[232] + -1.0)
def l294_231(x):
    # x is a list (or vector) of length 332
    return max(0, x[232] + x[233] + -1.0)
def l294_232(x):
    # x is a list (or vector) of length 332
    return max(0, x[233] + x[234] + -1.0)
def l294_233(x):
    # x is a list (or vector) of length 332
    return max(0, x[234] + x[235] + -1.0)
def l294_234(x):
    # x is a list (or vector) of length 332
    return max(0, x[235] + x[236] + -1.0)
def l294_235(x):
    # x is a list (or vector) of length 332
    return max(0, x[236] + x[237] + -1.0)
def l294_236(x):
    # x is a list (or vector) of length 332
    return max(0, x[237] + x[238] + -1.0)
def l294_237(x):
    # x is a list (or vector) of length 332
    return max(0, x[238] + x[239] + -1.0)
def l294_238(x):
    # x is a list (or vector) of length 332
    return max(0, x[239] + x[240] + -1.0)
def l294_239(x):
    # x is a list (or vector) of length 332
    return max(0, x[240] + x[241] + -1.0)
def l294_240(x):
    # x is a list (or vector) of length 332
    return max(0, x[241] + x[242] + -1.0)
def l294_241(x):
    # x is a list (or vector) of length 332
    return max(0, x[242] + x[243] + -1.0)
def l294_242(x):
    # x is a list (or vector) of length 332
    return max(0, x[243] + x[244] + -1.0)
def l294_243(x):
    # x is a list (or vector) of length 332
    return max(0, x[244] + x[245] + -1.0)
def l294_244(x):
    # x is a list (or vector) of length 332
    return max(0, x[245] + x[246] + -1.0)
def l294_245(x):
    # x is a list (or vector) of length 332
    return max(0, x[246] + x[247] + -1.0)
def l294_246(x):
    # x is a list (or vector) of length 332
    return max(0, x[247] + x[248] + -1.0)
def l294_247(x):
    # x is a list (or vector) of length 332
    return max(0, x[248] + x[249] + -1.0)
def l294_248(x):
    # x is a list (or vector) of length 332
    return max(0, x[249] + x[250] + -1.0)
def l294_249(x):
    # x is a list (or vector) of length 332
    return max(0, x[250] + x[251] + -1.0)
def l294_250(x):
    # x is a list (or vector) of length 332
    return max(0, x[251] + x[252] + -1.0)
def l294_251(x):
    # x is a list (or vector) of length 332
    return max(0, x[252] + x[253] + -1.0)
def l294_252(x):
    # x is a list (or vector) of length 332
    return max(0, x[253] + x[254] + -1.0)
def l294_253(x):
    # x is a list (or vector) of length 332
    return max(0, x[254] + x[255] + -1.0)
def l294_254(x):
    # x is a list (or vector) of length 332
    return max(0, x[224])
def l294_255(x):
    # x is a list (or vector) of length 332
    return max(0, x[224])
def l294_256(x):
    # x is a list (or vector) of length 332
    return max(0, x[225])
def l294_257(x):
    # x is a list (or vector) of length 332
    return max(0, x[226])
def l294_258(x):
    # x is a list (or vector) of length 332
    return max(0, x[227])
def l294_259(x):
    # x is a list (or vector) of length 332
    return max(0, x[228])
def l294_260(x):
    # x is a list (or vector) of length 332
    return max(0, x[229])
def l294_261(x):
    # x is a list (or vector) of length 332
    return max(0, x[230])
def l294_262(x):
    # x is a list (or vector) of length 332
    return max(0, x[231])
def l294_263(x):
    # x is a list (or vector) of length 332
    return max(0, x[232])
def l294_264(x):
    # x is a list (or vector) of length 332
    return max(0, x[233])
def l294_265(x):
    # x is a list (or vector) of length 332
    return max(0, x[234])
def l294_266(x):
    # x is a list (or vector) of length 332
    return max(0, x[235])
def l294_267(x):
    # x is a list (or vector) of length 332
    return max(0, x[236])
def l294_268(x):
    # x is a list (or vector) of length 332
    return max(0, x[237])
def l294_269(x):
    # x is a list (or vector) of length 332
    return max(0, x[238])
def l294_270(x):
    # x is a list (or vector) of length 332
    return max(0, x[239])
def l294_271(x):
    # x is a list (or vector) of length 332
    return max(0, x[240])
def l294_272(x):
    # x is a list (or vector) of length 332
    return max(0, x[241])
def l294_273(x):
    # x is a list (or vector) of length 332
    return max(0, x[242])
def l294_274(x):
    # x is a list (or vector) of length 332
    return max(0, x[243])
def l294_275(x):
    # x is a list (or vector) of length 332
    return max(0, x[244])
def l294_276(x):
    # x is a list (or vector) of length 332
    return max(0, x[245])
def l294_277(x):
    # x is a list (or vector) of length 332
    return max(0, x[246])
def l294_278(x):
    # x is a list (or vector) of length 332
    return max(0, x[247])
def l294_279(x):
    # x is a list (or vector) of length 332
    return max(0, x[248])
def l294_280(x):
    # x is a list (or vector) of length 332
    return max(0, x[249])
def l294_281(x):
    # x is a list (or vector) of length 332
    return max(0, x[250])
def l294_282(x):
    # x is a list (or vector) of length 332
    return max(0, x[251])
def l294_283(x):
    # x is a list (or vector) of length 332
    return max(0, x[252])
def l294_284(x):
    # x is a list (or vector) of length 332
    return max(0, x[253])
def l294_285(x):
    # x is a list (or vector) of length 332
    return max(0, x[254])
def l294_286(x):
    # x is a list (or vector) of length 332
    return max(0, x[255])
def l294_287(x):
    # x is a list (or vector) of length 332
    return max(0, x[256])
def l294_288(x):
    # x is a list (or vector) of length 332
    return max(0, x[257])
def l294_289(x):
    # x is a list (or vector) of length 332
    return max(0, x[258])
def l294_290(x):
    # x is a list (or vector) of length 332
    return max(0, x[259])
def l294_291(x):
    # x is a list (or vector) of length 332
    return max(0, x[260])
def l294_292(x):
    # x is a list (or vector) of length 332
    return max(0, x[261])
def l294_293(x):
    # x is a list (or vector) of length 332
    return max(0, x[262])
def l294_294(x):
    # x is a list (or vector) of length 332
    return max(0, x[263])
def l294_295(x):
    # x is a list (or vector) of length 332
    return max(0, -1.0*x[264] + 32.0)
def l294_296(x):
    # x is a list (or vector) of length 332
    return max(0, -1.0*x[265] + 32.0)
def l294_297(x):
    # x is a list (or vector) of length 332
    return max(0, -1.0*x[266] + 32.0)
def l294_298(x):
    # x is a list (or vector) of length 332
    return max(0, -1.0*x[267] + 32.0)
def l294_299(x):
    # x is a list (or vector) of length 332
    return max(0, x[264])
def l294_300(x):
    # x is a list (or vector) of length 332
    return max(0, x[265])
def l294_301(x):
    # x is a list (or vector) of length 332
    return max(0, x[266])
def l294_302(x):
    # x is a list (or vector) of length 332
    return max(0, x[267])
def l294_303(x):
    # x is a list (or vector) of length 332
    return max(0, x[264] + -31.0)
def l294_304(x):
    # x is a list (or vector) of length 332
    return max(0, x[265] + -31.0)
def l294_305(x):
    # x is a list (or vector) of length 332
    return max(0, x[266] + -31.0)
def l294_306(x):
    # x is a list (or vector) of length 332
    return max(0, x[267] + -31.0)
def l294_307(x):
    # x is a list (or vector) of length 332
    return max(0, x[264] + -32.0)
def l294_308(x):
    # x is a list (or vector) of length 332
    return max(0, x[265] + -32.0)
def l294_309(x):
    # x is a list (or vector) of length 332
    return max(0, x[266] + -32.0)
def l294_310(x):
    # x is a list (or vector) of length 332
    return max(0, x[267] + -32.0)
def l294_311(x):
    # x is a list (or vector) of length 332
    return max(0, x[268])
def l294_312(x):
    # x is a list (or vector) of length 332
    return max(0, x[269])
def l294_313(x):
    # x is a list (or vector) of length 332
    return max(0, x[270])
def l294_314(x):
    # x is a list (or vector) of length 332
    return max(0, x[271])
def l294_315(x):
    # x is a list (or vector) of length 332
    return max(0, x[272])
def l294_316(x):
    # x is a list (or vector) of length 332
    return max(0, x[273])
def l294_317(x):
    # x is a list (or vector) of length 332
    return max(0, x[274])
def l294_318(x):
    # x is a list (or vector) of length 332
    return max(0, x[275])
def l294_319(x):
    # x is a list (or vector) of length 332
    return max(0, x[276])
def l294_320(x):
    # x is a list (or vector) of length 332
    return max(0, x[277])
def l294_321(x):
    # x is a list (or vector) of length 332
    return max(0, x[278])
def l294_322(x):
    # x is a list (or vector) of length 332
    return max(0, x[279])
def l294_323(x):
    # x is a list (or vector) of length 332
    return max(0, x[280])
def l294_324(x):
    # x is a list (or vector) of length 332
    return max(0, x[281])
def l294_325(x):
    # x is a list (or vector) of length 332
    return max(0, x[282])
def l294_326(x):
    # x is a list (or vector) of length 332
    return max(0, x[283])
def l294_327(x):
    # x is a list (or vector) of length 332
    return max(0, x[284])
def l294_328(x):
    # x is a list (or vector) of length 332
    return max(0, x[285])
def l294_329(x):
    # x is a list (or vector) of length 332
    return max(0, x[286])
def l294_330(x):
    # x is a list (or vector) of length 332
    return max(0, x[287])
def l294_331(x):
    # x is a list (or vector) of length 332
    return max(0, x[288])
def l294_332(x):
    # x is a list (or vector) of length 332
    return max(0, x[289])
def l294_333(x):
    # x is a list (or vector) of length 332
    return max(0, x[290])
def l294_334(x):
    # x is a list (or vector) of length 332
    return max(0, x[291])
def l294_335(x):
    # x is a list (or vector) of length 332
    return max(0, x[292])
def l294_336(x):
    # x is a list (or vector) of length 332
    return max(0, x[293])
def l294_337(x):
    # x is a list (or vector) of length 332
    return max(0, x[294])
def l294_338(x):
    # x is a list (or vector) of length 332
    return max(0, x[295])
def l294_339(x):
    # x is a list (or vector) of length 332
    return max(0, x[296])
def l294_340(x):
    # x is a list (or vector) of length 332
    return max(0, x[297])
def l294_341(x):
    # x is a list (or vector) of length 332
    return max(0, x[298])
def l294_342(x):
    # x is a list (or vector) of length 332
    return max(0, x[299])
def l294_343(x):
    # x is a list (or vector) of length 332
    return max(0, x[300])
def l294_344(x):
    # x is a list (or vector) of length 332
    return max(0, x[301])
def l294_345(x):
    # x is a list (or vector) of length 332
    return max(0, x[302])
def l294_346(x):
    # x is a list (or vector) of length 332
    return max(0, x[303])
def l294_347(x):
    # x is a list (or vector) of length 332
    return max(0, x[304])
def l294_348(x):
    # x is a list (or vector) of length 332
    return max(0, x[305])
def l294_349(x):
    # x is a list (or vector) of length 332
    return max(0, x[306])
def l294_350(x):
    # x is a list (or vector) of length 332
    return max(0, x[307])
def l294_351(x):
    # x is a list (or vector) of length 332
    return max(0, x[308])
def l294_352(x):
    # x is a list (or vector) of length 332
    return max(0, x[309])
def l294_353(x):
    # x is a list (or vector) of length 332
    return max(0, x[310])
def l294_354(x):
    # x is a list (or vector) of length 332
    return max(0, x[311])
def l294_355(x):
    # x is a list (or vector) of length 332
    return max(0, x[312])
def l294_356(x):
    # x is a list (or vector) of length 332
    return max(0, x[313])
def l294_357(x):
    # x is a list (or vector) of length 332
    return max(0, x[314])
def l294_358(x):
    # x is a list (or vector) of length 332
    return max(0, x[315])
def l294_359(x):
    # x is a list (or vector) of length 332
    return max(0, x[316])
def l294_360(x):
    # x is a list (or vector) of length 332
    return max(0, x[317])
def l294_361(x):
    # x is a list (or vector) of length 332
    return max(0, x[318])
def l294_362(x):
    # x is a list (or vector) of length 332
    return max(0, x[319])
def l294_363(x):
    # x is a list (or vector) of length 332
    return max(0, x[320])
def l294_364(x):
    # x is a list (or vector) of length 332
    return max(0, x[321])
def l294_365(x):
    # x is a list (or vector) of length 332
    return max(0, x[322])
def l294_366(x):
    # x is a list (or vector) of length 332
    return max(0, x[323])
def l294_367(x):
    # x is a list (or vector) of length 332
    return max(0, x[324])
def l294_368(x):
    # x is a list (or vector) of length 332
    return max(0, x[325])
def l294_369(x):
    # x is a list (or vector) of length 332
    return max(0, x[326])
def l294_370(x):
    # x is a list (or vector) of length 332
    return max(0, x[327])
def l294_371(x):
    # x is a list (or vector) of length 332
    return max(0, x[328])
def l294_372(x):
    # x is a list (or vector) of length 332
    return max(0, x[329])
def l294_373(x):
    # x is a list (or vector) of length 332
    return max(0, x[330])
def l294_374(x):
    # x is a list (or vector) of length 332
    return max(0, x[331])
def l294_(x):
    # x is a list (or vector) of length 332
    return [
        l294_0(x),
        l294_1(x),
        l294_2(x),
        l294_3(x),
        l294_4(x),
        l294_5(x),
        l294_6(x),
        l294_7(x),
        l294_8(x),
        l294_9(x),
        l294_10(x),
        l294_11(x),
        l294_12(x),
        l294_13(x),
        l294_14(x),
        l294_15(x),
        l294_16(x),
        l294_17(x),
        l294_18(x),
        l294_19(x),
        l294_20(x),
        l294_21(x),
        l294_22(x),
        l294_23(x),
        l294_24(x),
        l294_25(x),
        l294_26(x),
        l294_27(x),
        l294_28(x),
        l294_29(x),
        l294_30(x),
        l294_31(x),
        l294_32(x),
        l294_33(x),
        l294_34(x),
        l294_35(x),
        l294_36(x),
        l294_37(x),
        l294_38(x),
        l294_39(x),
        l294_40(x),
        l294_41(x),
        l294_42(x),
        l294_43(x),
        l294_44(x),
        l294_45(x),
        l294_46(x),
        l294_47(x),
        l294_48(x),
        l294_49(x),
        l294_50(x),
        l294_51(x),
        l294_52(x),
        l294_53(x),
        l294_54(x),
        l294_55(x),
        l294_56(x),
        l294_57(x),
        l294_58(x),
        l294_59(x),
        l294_60(x),
        l294_61(x),
        l294_62(x),
        l294_63(x),
        l294_64(x),
        l294_65(x),
        l294_66(x),
        l294_67(x),
        l294_68(x),
        l294_69(x),
        l294_70(x),
        l294_71(x),
        l294_72(x),
        l294_73(x),
        l294_74(x),
        l294_75(x),
        l294_76(x),
        l294_77(x),
        l294_78(x),
        l294_79(x),
        l294_80(x),
        l294_81(x),
        l294_82(x),
        l294_83(x),
        l294_84(x),
        l294_85(x),
        l294_86(x),
        l294_87(x),
        l294_88(x),
        l294_89(x),
        l294_90(x),
        l294_91(x),
        l294_92(x),
        l294_93(x),
        l294_94(x),
        l294_95(x),
        l294_96(x),
        l294_97(x),
        l294_98(x),
        l294_99(x),
        l294_100(x),
        l294_101(x),
        l294_102(x),
        l294_103(x),
        l294_104(x),
        l294_105(x),
        l294_106(x),
        l294_107(x),
        l294_108(x),
        l294_109(x),
        l294_110(x),
        l294_111(x),
        l294_112(x),
        l294_113(x),
        l294_114(x),
        l294_115(x),
        l294_116(x),
        l294_117(x),
        l294_118(x),
        l294_119(x),
        l294_120(x),
        l294_121(x),
        l294_122(x),
        l294_123(x),
        l294_124(x),
        l294_125(x),
        l294_126(x),
        l294_127(x),
        l294_128(x),
        l294_129(x),
        l294_130(x),
        l294_131(x),
        l294_132(x),
        l294_133(x),
        l294_134(x),
        l294_135(x),
        l294_136(x),
        l294_137(x),
        l294_138(x),
        l294_139(x),
        l294_140(x),
        l294_141(x),
        l294_142(x),
        l294_143(x),
        l294_144(x),
        l294_145(x),
        l294_146(x),
        l294_147(x),
        l294_148(x),
        l294_149(x),
        l294_150(x),
        l294_151(x),
        l294_152(x),
        l294_153(x),
        l294_154(x),
        l294_155(x),
        l294_156(x),
        l294_157(x),
        l294_158(x),
        l294_159(x),
        l294_160(x),
        l294_161(x),
        l294_162(x),
        l294_163(x),
        l294_164(x),
        l294_165(x),
        l294_166(x),
        l294_167(x),
        l294_168(x),
        l294_169(x),
        l294_170(x),
        l294_171(x),
        l294_172(x),
        l294_173(x),
        l294_174(x),
        l294_175(x),
        l294_176(x),
        l294_177(x),
        l294_178(x),
        l294_179(x),
        l294_180(x),
        l294_181(x),
        l294_182(x),
        l294_183(x),
        l294_184(x),
        l294_185(x),
        l294_186(x),
        l294_187(x),
        l294_188(x),
        l294_189(x),
        l294_190(x),
        l294_191(x),
        l294_192(x),
        l294_193(x),
        l294_194(x),
        l294_195(x),
        l294_196(x),
        l294_197(x),
        l294_198(x),
        l294_199(x),
        l294_200(x),
        l294_201(x),
        l294_202(x),
        l294_203(x),
        l294_204(x),
        l294_205(x),
        l294_206(x),
        l294_207(x),
        l294_208(x),
        l294_209(x),
        l294_210(x),
        l294_211(x),
        l294_212(x),
        l294_213(x),
        l294_214(x),
        l294_215(x),
        l294_216(x),
        l294_217(x),
        l294_218(x),
        l294_219(x),
        l294_220(x),
        l294_221(x),
        l294_222(x),
        l294_223(x),
        l294_224(x),
        l294_225(x),
        l294_226(x),
        l294_227(x),
        l294_228(x),
        l294_229(x),
        l294_230(x),
        l294_231(x),
        l294_232(x),
        l294_233(x),
        l294_234(x),
        l294_235(x),
        l294_236(x),
        l294_237(x),
        l294_238(x),
        l294_239(x),
        l294_240(x),
        l294_241(x),
        l294_242(x),
        l294_243(x),
        l294_244(x),
        l294_245(x),
        l294_246(x),
        l294_247(x),
        l294_248(x),
        l294_249(x),
        l294_250(x),
        l294_251(x),
        l294_252(x),
        l294_253(x),
        l294_254(x),
        l294_255(x),
        l294_256(x),
        l294_257(x),
        l294_258(x),
        l294_259(x),
        l294_260(x),
        l294_261(x),
        l294_262(x),
        l294_263(x),
        l294_264(x),
        l294_265(x),
        l294_266(x),
        l294_267(x),
        l294_268(x),
        l294_269(x),
        l294_270(x),
        l294_271(x),
        l294_272(x),
        l294_273(x),
        l294_274(x),
        l294_275(x),
        l294_276(x),
        l294_277(x),
        l294_278(x),
        l294_279(x),
        l294_280(x),
        l294_281(x),
        l294_282(x),
        l294_283(x),
        l294_284(x),
        l294_285(x),
        l294_286(x),
        l294_287(x),
        l294_288(x),
        l294_289(x),
        l294_290(x),
        l294_291(x),
        l294_292(x),
        l294_293(x),
        l294_294(x),
        l294_295(x),
        l294_296(x),
        l294_297(x),
        l294_298(x),
        l294_299(x),
        l294_300(x),
        l294_301(x),
        l294_302(x),
        l294_303(x),
        l294_304(x),
        l294_305(x),
        l294_306(x),
        l294_307(x),
        l294_308(x),
        l294_309(x),
        l294_310(x),
        l294_311(x),
        l294_312(x),
        l294_313(x),
        l294_314(x),
        l294_315(x),
        l294_316(x),
        l294_317(x),
        l294_318(x),
        l294_319(x),
        l294_320(x),
        l294_321(x),
        l294_322(x),
        l294_323(x),
        l294_324(x),
        l294_325(x),
        l294_326(x),
        l294_327(x),
        l294_328(x),
        l294_329(x),
        l294_330(x),
        l294_331(x),
        l294_332(x),
        l294_333(x),
        l294_334(x),
        l294_335(x),
        l294_336(x),
        l294_337(x),
        l294_338(x),
        l294_339(x),
        l294_340(x),
        l294_341(x),
        l294_342(x),
        l294_343(x),
        l294_344(x),
        l294_345(x),
        l294_346(x),
        l294_347(x),
        l294_348(x),
        l294_349(x),
        l294_350(x),
        l294_351(x),
        l294_352(x),
        l294_353(x),
        l294_354(x),
        l294_355(x),
        l294_356(x),
        l294_357(x),
        l294_358(x),
        l294_359(x),
        l294_360(x),
        l294_361(x),
        l294_362(x),
        l294_363(x),
        l294_364(x),
        l294_365(x),
        l294_366(x),
        l294_367(x),
        l294_368(x),
        l294_369(x),
        l294_370(x),
        l294_371(x),
        l294_372(x),
        l294_373(x),
        l294_374(x),
    ]