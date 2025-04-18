import numpy as np




# Generated from reverse engineering
def l42_g(x: np.ndarray) -> np.ndarray:
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




def l42_0(x):
    # x is a list (or vector) of length 332
    return max(0, x[0])
def l42_1(x):
    # x is a list (or vector) of length 332
    return max(0, x[1])
def l42_2(x):
    # x is a list (or vector) of length 332
    return max(0, x[2])
def l42_3(x):
    # x is a list (or vector) of length 332
    return max(0, x[3])
def l42_4(x):
    # x is a list (or vector) of length 332
    return max(0, x[4])
def l42_5(x):
    # x is a list (or vector) of length 332
    return max(0, x[5])
def l42_6(x):
    # x is a list (or vector) of length 332
    return max(0, x[6])
def l42_7(x):
    # x is a list (or vector) of length 332
    return max(0, x[7])
def l42_8(x):
    # x is a list (or vector) of length 332
    return max(0, x[8])
def l42_9(x):
    # x is a list (or vector) of length 332
    return max(0, x[9])
def l42_10(x):
    # x is a list (or vector) of length 332
    return max(0, x[10])
def l42_11(x):
    # x is a list (or vector) of length 332
    return max(0, x[11])
def l42_12(x):
    # x is a list (or vector) of length 332
    return max(0, x[12])
def l42_13(x):
    # x is a list (or vector) of length 332
    return max(0, x[13])
def l42_14(x):
    # x is a list (or vector) of length 332
    return max(0, x[14])
def l42_15(x):
    # x is a list (or vector) of length 332
    return max(0, x[15])
def l42_16(x):
    # x is a list (or vector) of length 332
    return max(0, x[16])
def l42_17(x):
    # x is a list (or vector) of length 332
    return max(0, x[17])
def l42_18(x):
    # x is a list (or vector) of length 332
    return max(0, x[18])
def l42_19(x):
    # x is a list (or vector) of length 332
    return max(0, x[19])
def l42_20(x):
    # x is a list (or vector) of length 332
    return max(0, x[20])
def l42_21(x):
    # x is a list (or vector) of length 332
    return max(0, x[21])
def l42_22(x):
    # x is a list (or vector) of length 332
    return max(0, x[22])
def l42_23(x):
    # x is a list (or vector) of length 332
    return max(0, x[23])
def l42_24(x):
    # x is a list (or vector) of length 332
    return max(0, x[24])
def l42_25(x):
    # x is a list (or vector) of length 332
    return max(0, x[25])
def l42_26(x):
    # x is a list (or vector) of length 332
    return max(0, x[26])
def l42_27(x):
    # x is a list (or vector) of length 332
    return max(0, x[27])
def l42_28(x):
    # x is a list (or vector) of length 332
    return max(0, x[28])
def l42_29(x):
    # x is a list (or vector) of length 332
    return max(0, x[29])
def l42_30(x):
    # x is a list (or vector) of length 332
    return max(0, x[30])
def l42_31(x):
    # x is a list (or vector) of length 332
    return max(0, x[31])
def l42_32(x):
    # x is a list (or vector) of length 332
    return max(0, x[32])
def l42_33(x):
    # x is a list (or vector) of length 332
    return max(0, x[33])
def l42_34(x):
    # x is a list (or vector) of length 332
    return max(0, x[34])
def l42_35(x):
    # x is a list (or vector) of length 332
    return max(0, x[35])
def l42_36(x):
    # x is a list (or vector) of length 332
    return max(0, x[36])
def l42_37(x):
    # x is a list (or vector) of length 332
    return max(0, x[37])
def l42_38(x):
    # x is a list (or vector) of length 332
    return max(0, x[38])
def l42_39(x):
    # x is a list (or vector) of length 332
    return max(0, x[39])
def l42_40(x):
    # x is a list (or vector) of length 332
    return max(0, x[40])
def l42_41(x):
    # x is a list (or vector) of length 332
    return max(0, x[41])
def l42_42(x):
    # x is a list (or vector) of length 332
    return max(0, x[42])
def l42_43(x):
    # x is a list (or vector) of length 332
    return max(0, x[43])
def l42_44(x):
    # x is a list (or vector) of length 332
    return max(0, x[44])
def l42_45(x):
    # x is a list (or vector) of length 332
    return max(0, x[45])
def l42_46(x):
    # x is a list (or vector) of length 332
    return max(0, x[46])
def l42_47(x):
    # x is a list (or vector) of length 332
    return max(0, x[47])
def l42_48(x):
    # x is a list (or vector) of length 332
    return max(0, x[48])
def l42_49(x):
    # x is a list (or vector) of length 332
    return max(0, x[49])
def l42_50(x):
    # x is a list (or vector) of length 332
    return max(0, x[50])
def l42_51(x):
    # x is a list (or vector) of length 332
    return max(0, x[51])
def l42_52(x):
    # x is a list (or vector) of length 332
    return max(0, x[52])
def l42_53(x):
    # x is a list (or vector) of length 332
    return max(0, x[53])
def l42_54(x):
    # x is a list (or vector) of length 332
    return max(0, x[54])
def l42_55(x):
    # x is a list (or vector) of length 332
    return max(0, x[55])
def l42_56(x):
    # x is a list (or vector) of length 332
    return max(0, x[56])
def l42_57(x):
    # x is a list (or vector) of length 332
    return max(0, x[57])
def l42_58(x):
    # x is a list (or vector) of length 332
    return max(0, x[58])
def l42_59(x):
    # x is a list (or vector) of length 332
    return max(0, x[59])
def l42_60(x):
    # x is a list (or vector) of length 332
    return max(0, x[60])
def l42_61(x):
    # x is a list (or vector) of length 332
    return max(0, x[61])
def l42_62(x):
    # x is a list (or vector) of length 332
    return max(0, x[62])
def l42_63(x):
    # x is a list (or vector) of length 332
    return max(0, x[63])
def l42_64(x):
    # x is a list (or vector) of length 332
    return max(0, x[64])
def l42_65(x):
    # x is a list (or vector) of length 332
    return max(0, x[65])
def l42_66(x):
    # x is a list (or vector) of length 332
    return max(0, x[66])
def l42_67(x):
    # x is a list (or vector) of length 332
    return max(0, x[67])
def l42_68(x):
    # x is a list (or vector) of length 332
    return max(0, x[68])
def l42_69(x):
    # x is a list (or vector) of length 332
    return max(0, x[69])
def l42_70(x):
    # x is a list (or vector) of length 332
    return max(0, x[70])
def l42_71(x):
    # x is a list (or vector) of length 332
    return max(0, x[71])
def l42_72(x):
    # x is a list (or vector) of length 332
    return max(0, x[72])
def l42_73(x):
    # x is a list (or vector) of length 332
    return max(0, x[73])
def l42_74(x):
    # x is a list (or vector) of length 332
    return max(0, x[74])
def l42_75(x):
    # x is a list (or vector) of length 332
    return max(0, x[75])
def l42_76(x):
    # x is a list (or vector) of length 332
    return max(0, x[76])
def l42_77(x):
    # x is a list (or vector) of length 332
    return max(0, x[77])
def l42_78(x):
    # x is a list (or vector) of length 332
    return max(0, x[78])
def l42_79(x):
    # x is a list (or vector) of length 332
    return max(0, x[79])
def l42_80(x):
    # x is a list (or vector) of length 332
    return max(0, x[80])
def l42_81(x):
    # x is a list (or vector) of length 332
    return max(0, x[81])
def l42_82(x):
    # x is a list (or vector) of length 332
    return max(0, x[82])
def l42_83(x):
    # x is a list (or vector) of length 332
    return max(0, x[83])
def l42_84(x):
    # x is a list (or vector) of length 332
    return max(0, x[84])
def l42_85(x):
    # x is a list (or vector) of length 332
    return max(0, x[85])
def l42_86(x):
    # x is a list (or vector) of length 332
    return max(0, x[86])
def l42_87(x):
    # x is a list (or vector) of length 332
    return max(0, x[87])
def l42_88(x):
    # x is a list (or vector) of length 332
    return max(0, x[88])
def l42_89(x):
    # x is a list (or vector) of length 332
    return max(0, x[89])
def l42_90(x):
    # x is a list (or vector) of length 332
    return max(0, x[90])
def l42_91(x):
    # x is a list (or vector) of length 332
    return max(0, x[91])
def l42_92(x):
    # x is a list (or vector) of length 332
    return max(0, x[92])
def l42_93(x):
    # x is a list (or vector) of length 332
    return max(0, x[93])
def l42_94(x):
    # x is a list (or vector) of length 332
    return max(0, x[94])
def l42_95(x):
    # x is a list (or vector) of length 332
    return max(0, x[95])
def l42_96(x):
    # x is a list (or vector) of length 332
    return max(0, x[96])
def l42_97(x):
    # x is a list (or vector) of length 332
    return max(0, x[97])
def l42_98(x):
    # x is a list (or vector) of length 332
    return max(0, x[98])
def l42_99(x):
    # x is a list (or vector) of length 332
    return max(0, x[99])
def l42_100(x):
    # x is a list (or vector) of length 332
    return max(0, x[100])
def l42_101(x):
    # x is a list (or vector) of length 332
    return max(0, x[101])
def l42_102(x):
    # x is a list (or vector) of length 332
    return max(0, x[102])
def l42_103(x):
    # x is a list (or vector) of length 332
    return max(0, x[103])
def l42_104(x):
    # x is a list (or vector) of length 332
    return max(0, x[104])
def l42_105(x):
    # x is a list (or vector) of length 332
    return max(0, x[105])
def l42_106(x):
    # x is a list (or vector) of length 332
    return max(0, x[106])
def l42_107(x):
    # x is a list (or vector) of length 332
    return max(0, x[107])
def l42_108(x):
    # x is a list (or vector) of length 332
    return max(0, x[108])
def l42_109(x):
    # x is a list (or vector) of length 332
    return max(0, x[109])
def l42_110(x):
    # x is a list (or vector) of length 332
    return max(0, x[110])
def l42_111(x):
    # x is a list (or vector) of length 332
    return max(0, x[111])
def l42_112(x):
    # x is a list (or vector) of length 332
    return max(0, x[112])
def l42_113(x):
    # x is a list (or vector) of length 332
    return max(0, x[113])
def l42_114(x):
    # x is a list (or vector) of length 332
    return max(0, x[114])
def l42_115(x):
    # x is a list (or vector) of length 332
    return max(0, x[115])
def l42_116(x):
    # x is a list (or vector) of length 332
    return max(0, x[116])
def l42_117(x):
    # x is a list (or vector) of length 332
    return max(0, x[117])
def l42_118(x):
    # x is a list (or vector) of length 332
    return max(0, x[118])
def l42_119(x):
    # x is a list (or vector) of length 332
    return max(0, x[119])
def l42_120(x):
    # x is a list (or vector) of length 332
    return max(0, x[120])
def l42_121(x):
    # x is a list (or vector) of length 332
    return max(0, x[121])
def l42_122(x):
    # x is a list (or vector) of length 332
    return max(0, x[122])
def l42_123(x):
    # x is a list (or vector) of length 332
    return max(0, x[123])
def l42_124(x):
    # x is a list (or vector) of length 332
    return max(0, x[124])
def l42_125(x):
    # x is a list (or vector) of length 332
    return max(0, x[125])
def l42_126(x):
    # x is a list (or vector) of length 332
    return max(0, x[126])
def l42_127(x):
    # x is a list (or vector) of length 332
    return max(0, x[127])
def l42_128(x):
    # x is a list (or vector) of length 332
    return max(0, x[128] + -2.0*x[160])
def l42_129(x):
    # x is a list (or vector) of length 332
    return max(0, x[129] + -2.0*x[161])
def l42_130(x):
    # x is a list (or vector) of length 332
    return max(0, x[130] + -2.0*x[162])
def l42_131(x):
    # x is a list (or vector) of length 332
    return max(0, x[131] + -2.0*x[163])
def l42_132(x):
    # x is a list (or vector) of length 332
    return max(0, x[132] + -2.0*x[164])
def l42_133(x):
    # x is a list (or vector) of length 332
    return max(0, x[133] + -2.0*x[165])
def l42_134(x):
    # x is a list (or vector) of length 332
    return max(0, x[134] + -2.0*x[166])
def l42_135(x):
    # x is a list (or vector) of length 332
    return max(0, x[135] + -2.0*x[167])
def l42_136(x):
    # x is a list (or vector) of length 332
    return max(0, x[136] + -2.0*x[168])
def l42_137(x):
    # x is a list (or vector) of length 332
    return max(0, x[137] + -2.0*x[169])
def l42_138(x):
    # x is a list (or vector) of length 332
    return max(0, x[138] + -2.0*x[170])
def l42_139(x):
    # x is a list (or vector) of length 332
    return max(0, x[139] + -2.0*x[171])
def l42_140(x):
    # x is a list (or vector) of length 332
    return max(0, x[140] + -2.0*x[172])
def l42_141(x):
    # x is a list (or vector) of length 332
    return max(0, x[141] + -2.0*x[173])
def l42_142(x):
    # x is a list (or vector) of length 332
    return max(0, x[142] + -2.0*x[174])
def l42_143(x):
    # x is a list (or vector) of length 332
    return max(0, x[143] + -2.0*x[175])
def l42_144(x):
    # x is a list (or vector) of length 332
    return max(0, x[144] + -2.0*x[176])
def l42_145(x):
    # x is a list (or vector) of length 332
    return max(0, x[145] + -2.0*x[177])
def l42_146(x):
    # x is a list (or vector) of length 332
    return max(0, x[146] + -2.0*x[178])
def l42_147(x):
    # x is a list (or vector) of length 332
    return max(0, x[147] + -2.0*x[179])
def l42_148(x):
    # x is a list (or vector) of length 332
    return max(0, x[148] + -2.0*x[180])
def l42_149(x):
    # x is a list (or vector) of length 332
    return max(0, x[149] + -2.0*x[181])
def l42_150(x):
    # x is a list (or vector) of length 332
    return max(0, x[150] + -2.0*x[182])
def l42_151(x):
    # x is a list (or vector) of length 332
    return max(0, x[151] + -2.0*x[183])
def l42_152(x):
    # x is a list (or vector) of length 332
    return max(0, x[152] + -2.0*x[184])
def l42_153(x):
    # x is a list (or vector) of length 332
    return max(0, x[153] + -2.0*x[185])
def l42_154(x):
    # x is a list (or vector) of length 332
    return max(0, x[154] + -2.0*x[186])
def l42_155(x):
    # x is a list (or vector) of length 332
    return max(0, x[155] + -2.0*x[187])
def l42_156(x):
    # x is a list (or vector) of length 332
    return max(0, x[156] + -2.0*x[188])
def l42_157(x):
    # x is a list (or vector) of length 332
    return max(0, x[157] + -2.0*x[189])
def l42_158(x):
    # x is a list (or vector) of length 332
    return max(0, x[158] + -2.0*x[190])
def l42_159(x):
    # x is a list (or vector) of length 332
    return max(0, x[159] + -2.0*x[191])
def l42_160(x):
    # x is a list (or vector) of length 332
    return max(0, x[192])
def l42_161(x):
    # x is a list (or vector) of length 332
    return max(0, x[192] + x[225] + -1.0)
def l42_162(x):
    # x is a list (or vector) of length 332
    return max(0, x[193] + x[226] + -1.0)
def l42_163(x):
    # x is a list (or vector) of length 332
    return max(0, x[194] + x[227] + -1.0)
def l42_164(x):
    # x is a list (or vector) of length 332
    return max(0, x[195] + x[228] + -1.0)
def l42_165(x):
    # x is a list (or vector) of length 332
    return max(0, x[196] + x[229] + -1.0)
def l42_166(x):
    # x is a list (or vector) of length 332
    return max(0, x[197] + x[230] + -1.0)
def l42_167(x):
    # x is a list (or vector) of length 332
    return max(0, x[198] + x[231] + -1.0)
def l42_168(x):
    # x is a list (or vector) of length 332
    return max(0, x[199] + x[232] + -1.0)
def l42_169(x):
    # x is a list (or vector) of length 332
    return max(0, x[200] + x[233] + -1.0)
def l42_170(x):
    # x is a list (or vector) of length 332
    return max(0, x[201] + x[234] + -1.0)
def l42_171(x):
    # x is a list (or vector) of length 332
    return max(0, x[202] + x[235] + -1.0)
def l42_172(x):
    # x is a list (or vector) of length 332
    return max(0, x[203] + x[236] + -1.0)
def l42_173(x):
    # x is a list (or vector) of length 332
    return max(0, x[204] + x[237] + -1.0)
def l42_174(x):
    # x is a list (or vector) of length 332
    return max(0, x[205] + x[238] + -1.0)
def l42_175(x):
    # x is a list (or vector) of length 332
    return max(0, x[206] + x[239] + -1.0)
def l42_176(x):
    # x is a list (or vector) of length 332
    return max(0, x[207] + x[240] + -1.0)
def l42_177(x):
    # x is a list (or vector) of length 332
    return max(0, x[208] + x[241] + -1.0)
def l42_178(x):
    # x is a list (or vector) of length 332
    return max(0, x[209] + x[242] + -1.0)
def l42_179(x):
    # x is a list (or vector) of length 332
    return max(0, x[210] + x[243] + -1.0)
def l42_180(x):
    # x is a list (or vector) of length 332
    return max(0, x[211] + x[244] + -1.0)
def l42_181(x):
    # x is a list (or vector) of length 332
    return max(0, x[212] + x[245] + -1.0)
def l42_182(x):
    # x is a list (or vector) of length 332
    return max(0, x[213] + x[246] + -1.0)
def l42_183(x):
    # x is a list (or vector) of length 332
    return max(0, x[214] + x[247] + -1.0)
def l42_184(x):
    # x is a list (or vector) of length 332
    return max(0, x[215] + x[248] + -1.0)
def l42_185(x):
    # x is a list (or vector) of length 332
    return max(0, x[216] + x[249] + -1.0)
def l42_186(x):
    # x is a list (or vector) of length 332
    return max(0, x[217] + x[250] + -1.0)
def l42_187(x):
    # x is a list (or vector) of length 332
    return max(0, x[218] + x[251] + -1.0)
def l42_188(x):
    # x is a list (or vector) of length 332
    return max(0, x[219] + x[252] + -1.0)
def l42_189(x):
    # x is a list (or vector) of length 332
    return max(0, x[220] + x[253] + -1.0)
def l42_190(x):
    # x is a list (or vector) of length 332
    return max(0, x[221] + x[254] + -1.0)
def l42_191(x):
    # x is a list (or vector) of length 332
    return max(0, x[222] + x[255] + -1.0)
def l42_192(x):
    # x is a list (or vector) of length 332
    return max(0, x[193])
def l42_193(x):
    # x is a list (or vector) of length 332
    return max(0, x[194])
def l42_194(x):
    # x is a list (or vector) of length 332
    return max(0, x[195])
def l42_195(x):
    # x is a list (or vector) of length 332
    return max(0, x[196])
def l42_196(x):
    # x is a list (or vector) of length 332
    return max(0, x[197])
def l42_197(x):
    # x is a list (or vector) of length 332
    return max(0, x[198])
def l42_198(x):
    # x is a list (or vector) of length 332
    return max(0, x[199])
def l42_199(x):
    # x is a list (or vector) of length 332
    return max(0, x[200])
def l42_200(x):
    # x is a list (or vector) of length 332
    return max(0, x[201])
def l42_201(x):
    # x is a list (or vector) of length 332
    return max(0, x[202])
def l42_202(x):
    # x is a list (or vector) of length 332
    return max(0, x[203])
def l42_203(x):
    # x is a list (or vector) of length 332
    return max(0, x[204])
def l42_204(x):
    # x is a list (or vector) of length 332
    return max(0, x[205])
def l42_205(x):
    # x is a list (or vector) of length 332
    return max(0, x[206])
def l42_206(x):
    # x is a list (or vector) of length 332
    return max(0, x[207])
def l42_207(x):
    # x is a list (or vector) of length 332
    return max(0, x[208])
def l42_208(x):
    # x is a list (or vector) of length 332
    return max(0, x[209])
def l42_209(x):
    # x is a list (or vector) of length 332
    return max(0, x[210])
def l42_210(x):
    # x is a list (or vector) of length 332
    return max(0, x[211])
def l42_211(x):
    # x is a list (or vector) of length 332
    return max(0, x[212])
def l42_212(x):
    # x is a list (or vector) of length 332
    return max(0, x[213])
def l42_213(x):
    # x is a list (or vector) of length 332
    return max(0, x[214])
def l42_214(x):
    # x is a list (or vector) of length 332
    return max(0, x[215])
def l42_215(x):
    # x is a list (or vector) of length 332
    return max(0, x[216])
def l42_216(x):
    # x is a list (or vector) of length 332
    return max(0, x[217])
def l42_217(x):
    # x is a list (or vector) of length 332
    return max(0, x[218])
def l42_218(x):
    # x is a list (or vector) of length 332
    return max(0, x[219])
def l42_219(x):
    # x is a list (or vector) of length 332
    return max(0, x[220])
def l42_220(x):
    # x is a list (or vector) of length 332
    return max(0, x[221])
def l42_221(x):
    # x is a list (or vector) of length 332
    return max(0, x[222])
def l42_222(x):
    # x is a list (or vector) of length 332
    return max(0, x[223])
def l42_223(x):
    # x is a list (or vector) of length 332
    return max(0, x[224] + x[225] + -1.0)
def l42_224(x):
    # x is a list (or vector) of length 332
    return max(0, x[225] + x[226] + -1.0)
def l42_225(x):
    # x is a list (or vector) of length 332
    return max(0, x[226] + x[227] + -1.0)
def l42_226(x):
    # x is a list (or vector) of length 332
    return max(0, x[227] + x[228] + -1.0)
def l42_227(x):
    # x is a list (or vector) of length 332
    return max(0, x[228] + x[229] + -1.0)
def l42_228(x):
    # x is a list (or vector) of length 332
    return max(0, x[229] + x[230] + -1.0)
def l42_229(x):
    # x is a list (or vector) of length 332
    return max(0, x[230] + x[231] + -1.0)
def l42_230(x):
    # x is a list (or vector) of length 332
    return max(0, x[231] + x[232] + -1.0)
def l42_231(x):
    # x is a list (or vector) of length 332
    return max(0, x[232] + x[233] + -1.0)
def l42_232(x):
    # x is a list (or vector) of length 332
    return max(0, x[233] + x[234] + -1.0)
def l42_233(x):
    # x is a list (or vector) of length 332
    return max(0, x[234] + x[235] + -1.0)
def l42_234(x):
    # x is a list (or vector) of length 332
    return max(0, x[235] + x[236] + -1.0)
def l42_235(x):
    # x is a list (or vector) of length 332
    return max(0, x[236] + x[237] + -1.0)
def l42_236(x):
    # x is a list (or vector) of length 332
    return max(0, x[237] + x[238] + -1.0)
def l42_237(x):
    # x is a list (or vector) of length 332
    return max(0, x[238] + x[239] + -1.0)
def l42_238(x):
    # x is a list (or vector) of length 332
    return max(0, x[239] + x[240] + -1.0)
def l42_239(x):
    # x is a list (or vector) of length 332
    return max(0, x[240] + x[241] + -1.0)
def l42_240(x):
    # x is a list (or vector) of length 332
    return max(0, x[241] + x[242] + -1.0)
def l42_241(x):
    # x is a list (or vector) of length 332
    return max(0, x[242] + x[243] + -1.0)
def l42_242(x):
    # x is a list (or vector) of length 332
    return max(0, x[243] + x[244] + -1.0)
def l42_243(x):
    # x is a list (or vector) of length 332
    return max(0, x[244] + x[245] + -1.0)
def l42_244(x):
    # x is a list (or vector) of length 332
    return max(0, x[245] + x[246] + -1.0)
def l42_245(x):
    # x is a list (or vector) of length 332
    return max(0, x[246] + x[247] + -1.0)
def l42_246(x):
    # x is a list (or vector) of length 332
    return max(0, x[247] + x[248] + -1.0)
def l42_247(x):
    # x is a list (or vector) of length 332
    return max(0, x[248] + x[249] + -1.0)
def l42_248(x):
    # x is a list (or vector) of length 332
    return max(0, x[249] + x[250] + -1.0)
def l42_249(x):
    # x is a list (or vector) of length 332
    return max(0, x[250] + x[251] + -1.0)
def l42_250(x):
    # x is a list (or vector) of length 332
    return max(0, x[251] + x[252] + -1.0)
def l42_251(x):
    # x is a list (or vector) of length 332
    return max(0, x[252] + x[253] + -1.0)
def l42_252(x):
    # x is a list (or vector) of length 332
    return max(0, x[253] + x[254] + -1.0)
def l42_253(x):
    # x is a list (or vector) of length 332
    return max(0, x[254] + x[255] + -1.0)
def l42_254(x):
    # x is a list (or vector) of length 332
    return max(0, x[224])
def l42_255(x):
    # x is a list (or vector) of length 332
    return max(0, x[224])
def l42_256(x):
    # x is a list (or vector) of length 332
    return max(0, x[225])
def l42_257(x):
    # x is a list (or vector) of length 332
    return max(0, x[226])
def l42_258(x):
    # x is a list (or vector) of length 332
    return max(0, x[227])
def l42_259(x):
    # x is a list (or vector) of length 332
    return max(0, x[228])
def l42_260(x):
    # x is a list (or vector) of length 332
    return max(0, x[229])
def l42_261(x):
    # x is a list (or vector) of length 332
    return max(0, x[230])
def l42_262(x):
    # x is a list (or vector) of length 332
    return max(0, x[231])
def l42_263(x):
    # x is a list (or vector) of length 332
    return max(0, x[232])
def l42_264(x):
    # x is a list (or vector) of length 332
    return max(0, x[233])
def l42_265(x):
    # x is a list (or vector) of length 332
    return max(0, x[234])
def l42_266(x):
    # x is a list (or vector) of length 332
    return max(0, x[235])
def l42_267(x):
    # x is a list (or vector) of length 332
    return max(0, x[236])
def l42_268(x):
    # x is a list (or vector) of length 332
    return max(0, x[237])
def l42_269(x):
    # x is a list (or vector) of length 332
    return max(0, x[238])
def l42_270(x):
    # x is a list (or vector) of length 332
    return max(0, x[239])
def l42_271(x):
    # x is a list (or vector) of length 332
    return max(0, x[240])
def l42_272(x):
    # x is a list (or vector) of length 332
    return max(0, x[241])
def l42_273(x):
    # x is a list (or vector) of length 332
    return max(0, x[242])
def l42_274(x):
    # x is a list (or vector) of length 332
    return max(0, x[243])
def l42_275(x):
    # x is a list (or vector) of length 332
    return max(0, x[244])
def l42_276(x):
    # x is a list (or vector) of length 332
    return max(0, x[245])
def l42_277(x):
    # x is a list (or vector) of length 332
    return max(0, x[246])
def l42_278(x):
    # x is a list (or vector) of length 332
    return max(0, x[247])
def l42_279(x):
    # x is a list (or vector) of length 332
    return max(0, x[248])
def l42_280(x):
    # x is a list (or vector) of length 332
    return max(0, x[249])
def l42_281(x):
    # x is a list (or vector) of length 332
    return max(0, x[250])
def l42_282(x):
    # x is a list (or vector) of length 332
    return max(0, x[251])
def l42_283(x):
    # x is a list (or vector) of length 332
    return max(0, x[252])
def l42_284(x):
    # x is a list (or vector) of length 332
    return max(0, x[253])
def l42_285(x):
    # x is a list (or vector) of length 332
    return max(0, x[254])
def l42_286(x):
    # x is a list (or vector) of length 332
    return max(0, x[255])
def l42_287(x):
    # x is a list (or vector) of length 332
    return max(0, x[256])
def l42_288(x):
    # x is a list (or vector) of length 332
    return max(0, x[257])
def l42_289(x):
    # x is a list (or vector) of length 332
    return max(0, x[258])
def l42_290(x):
    # x is a list (or vector) of length 332
    return max(0, x[259])
def l42_291(x):
    # x is a list (or vector) of length 332
    return max(0, x[260])
def l42_292(x):
    # x is a list (or vector) of length 332
    return max(0, x[261])
def l42_293(x):
    # x is a list (or vector) of length 332
    return max(0, x[262])
def l42_294(x):
    # x is a list (or vector) of length 332
    return max(0, x[263])
def l42_295(x):
    # x is a list (or vector) of length 332
    return max(0, -1.0*x[264] + 32.0)
def l42_296(x):
    # x is a list (or vector) of length 332
    return max(0, -1.0*x[265] + 32.0)
def l42_297(x):
    # x is a list (or vector) of length 332
    return max(0, -1.0*x[266] + 32.0)
def l42_298(x):
    # x is a list (or vector) of length 332
    return max(0, -1.0*x[267] + 32.0)
def l42_299(x):
    # x is a list (or vector) of length 332
    return max(0, x[264])
def l42_300(x):
    # x is a list (or vector) of length 332
    return max(0, x[265])
def l42_301(x):
    # x is a list (or vector) of length 332
    return max(0, x[266])
def l42_302(x):
    # x is a list (or vector) of length 332
    return max(0, x[267])
def l42_303(x):
    # x is a list (or vector) of length 332
    return max(0, x[264] + -31.0)
def l42_304(x):
    # x is a list (or vector) of length 332
    return max(0, x[265] + -31.0)
def l42_305(x):
    # x is a list (or vector) of length 332
    return max(0, x[266] + -31.0)
def l42_306(x):
    # x is a list (or vector) of length 332
    return max(0, x[267] + -31.0)
def l42_307(x):
    # x is a list (or vector) of length 332
    return max(0, x[264] + -32.0)
def l42_308(x):
    # x is a list (or vector) of length 332
    return max(0, x[265] + -32.0)
def l42_309(x):
    # x is a list (or vector) of length 332
    return max(0, x[266] + -32.0)
def l42_310(x):
    # x is a list (or vector) of length 332
    return max(0, x[267] + -32.0)
def l42_311(x):
    # x is a list (or vector) of length 332
    return max(0, x[268])
def l42_312(x):
    # x is a list (or vector) of length 332
    return max(0, x[269])
def l42_313(x):
    # x is a list (or vector) of length 332
    return max(0, x[270])
def l42_314(x):
    # x is a list (or vector) of length 332
    return max(0, x[271])
def l42_315(x):
    # x is a list (or vector) of length 332
    return max(0, x[272])
def l42_316(x):
    # x is a list (or vector) of length 332
    return max(0, x[273])
def l42_317(x):
    # x is a list (or vector) of length 332
    return max(0, x[274])
def l42_318(x):
    # x is a list (or vector) of length 332
    return max(0, x[275])
def l42_319(x):
    # x is a list (or vector) of length 332
    return max(0, x[276])
def l42_320(x):
    # x is a list (or vector) of length 332
    return max(0, x[277])
def l42_321(x):
    # x is a list (or vector) of length 332
    return max(0, x[278])
def l42_322(x):
    # x is a list (or vector) of length 332
    return max(0, x[279])
def l42_323(x):
    # x is a list (or vector) of length 332
    return max(0, x[280])
def l42_324(x):
    # x is a list (or vector) of length 332
    return max(0, x[281])
def l42_325(x):
    # x is a list (or vector) of length 332
    return max(0, x[282])
def l42_326(x):
    # x is a list (or vector) of length 332
    return max(0, x[283])
def l42_327(x):
    # x is a list (or vector) of length 332
    return max(0, x[284])
def l42_328(x):
    # x is a list (or vector) of length 332
    return max(0, x[285])
def l42_329(x):
    # x is a list (or vector) of length 332
    return max(0, x[286])
def l42_330(x):
    # x is a list (or vector) of length 332
    return max(0, x[287])
def l42_331(x):
    # x is a list (or vector) of length 332
    return max(0, x[288])
def l42_332(x):
    # x is a list (or vector) of length 332
    return max(0, x[289])
def l42_333(x):
    # x is a list (or vector) of length 332
    return max(0, x[290])
def l42_334(x):
    # x is a list (or vector) of length 332
    return max(0, x[291])
def l42_335(x):
    # x is a list (or vector) of length 332
    return max(0, x[292])
def l42_336(x):
    # x is a list (or vector) of length 332
    return max(0, x[293])
def l42_337(x):
    # x is a list (or vector) of length 332
    return max(0, x[294])
def l42_338(x):
    # x is a list (or vector) of length 332
    return max(0, x[295])
def l42_339(x):
    # x is a list (or vector) of length 332
    return max(0, x[296])
def l42_340(x):
    # x is a list (or vector) of length 332
    return max(0, x[297])
def l42_341(x):
    # x is a list (or vector) of length 332
    return max(0, x[298])
def l42_342(x):
    # x is a list (or vector) of length 332
    return max(0, x[299])
def l42_343(x):
    # x is a list (or vector) of length 332
    return max(0, x[300])
def l42_344(x):
    # x is a list (or vector) of length 332
    return max(0, x[301])
def l42_345(x):
    # x is a list (or vector) of length 332
    return max(0, x[302])
def l42_346(x):
    # x is a list (or vector) of length 332
    return max(0, x[303])
def l42_347(x):
    # x is a list (or vector) of length 332
    return max(0, x[304])
def l42_348(x):
    # x is a list (or vector) of length 332
    return max(0, x[305])
def l42_349(x):
    # x is a list (or vector) of length 332
    return max(0, x[306])
def l42_350(x):
    # x is a list (or vector) of length 332
    return max(0, x[307])
def l42_351(x):
    # x is a list (or vector) of length 332
    return max(0, x[308])
def l42_352(x):
    # x is a list (or vector) of length 332
    return max(0, x[309])
def l42_353(x):
    # x is a list (or vector) of length 332
    return max(0, x[310])
def l42_354(x):
    # x is a list (or vector) of length 332
    return max(0, x[311])
def l42_355(x):
    # x is a list (or vector) of length 332
    return max(0, x[312])
def l42_356(x):
    # x is a list (or vector) of length 332
    return max(0, x[313])
def l42_357(x):
    # x is a list (or vector) of length 332
    return max(0, x[314])
def l42_358(x):
    # x is a list (or vector) of length 332
    return max(0, x[315])
def l42_359(x):
    # x is a list (or vector) of length 332
    return max(0, x[316])
def l42_360(x):
    # x is a list (or vector) of length 332
    return max(0, x[317])
def l42_361(x):
    # x is a list (or vector) of length 332
    return max(0, x[318])
def l42_362(x):
    # x is a list (or vector) of length 332
    return max(0, x[319])
def l42_363(x):
    # x is a list (or vector) of length 332
    return max(0, x[320])
def l42_364(x):
    # x is a list (or vector) of length 332
    return max(0, x[321])
def l42_365(x):
    # x is a list (or vector) of length 332
    return max(0, x[322])
def l42_366(x):
    # x is a list (or vector) of length 332
    return max(0, x[323])
def l42_367(x):
    # x is a list (or vector) of length 332
    return max(0, x[324])
def l42_368(x):
    # x is a list (or vector) of length 332
    return max(0, x[325])
def l42_369(x):
    # x is a list (or vector) of length 332
    return max(0, x[326])
def l42_370(x):
    # x is a list (or vector) of length 332
    return max(0, x[327])
def l42_371(x):
    # x is a list (or vector) of length 332
    return max(0, x[328])
def l42_372(x):
    # x is a list (or vector) of length 332
    return max(0, x[329])
def l42_373(x):
    # x is a list (or vector) of length 332
    return max(0, x[330])
def l42_374(x):
    # x is a list (or vector) of length 332
    return max(0, x[331])
def l42_(x):
    # x is a list (or vector) of length 332
    return [
        l42_0(x),
        l42_1(x),
        l42_2(x),
        l42_3(x),
        l42_4(x),
        l42_5(x),
        l42_6(x),
        l42_7(x),
        l42_8(x),
        l42_9(x),
        l42_10(x),
        l42_11(x),
        l42_12(x),
        l42_13(x),
        l42_14(x),
        l42_15(x),
        l42_16(x),
        l42_17(x),
        l42_18(x),
        l42_19(x),
        l42_20(x),
        l42_21(x),
        l42_22(x),
        l42_23(x),
        l42_24(x),
        l42_25(x),
        l42_26(x),
        l42_27(x),
        l42_28(x),
        l42_29(x),
        l42_30(x),
        l42_31(x),
        l42_32(x),
        l42_33(x),
        l42_34(x),
        l42_35(x),
        l42_36(x),
        l42_37(x),
        l42_38(x),
        l42_39(x),
        l42_40(x),
        l42_41(x),
        l42_42(x),
        l42_43(x),
        l42_44(x),
        l42_45(x),
        l42_46(x),
        l42_47(x),
        l42_48(x),
        l42_49(x),
        l42_50(x),
        l42_51(x),
        l42_52(x),
        l42_53(x),
        l42_54(x),
        l42_55(x),
        l42_56(x),
        l42_57(x),
        l42_58(x),
        l42_59(x),
        l42_60(x),
        l42_61(x),
        l42_62(x),
        l42_63(x),
        l42_64(x),
        l42_65(x),
        l42_66(x),
        l42_67(x),
        l42_68(x),
        l42_69(x),
        l42_70(x),
        l42_71(x),
        l42_72(x),
        l42_73(x),
        l42_74(x),
        l42_75(x),
        l42_76(x),
        l42_77(x),
        l42_78(x),
        l42_79(x),
        l42_80(x),
        l42_81(x),
        l42_82(x),
        l42_83(x),
        l42_84(x),
        l42_85(x),
        l42_86(x),
        l42_87(x),
        l42_88(x),
        l42_89(x),
        l42_90(x),
        l42_91(x),
        l42_92(x),
        l42_93(x),
        l42_94(x),
        l42_95(x),
        l42_96(x),
        l42_97(x),
        l42_98(x),
        l42_99(x),
        l42_100(x),
        l42_101(x),
        l42_102(x),
        l42_103(x),
        l42_104(x),
        l42_105(x),
        l42_106(x),
        l42_107(x),
        l42_108(x),
        l42_109(x),
        l42_110(x),
        l42_111(x),
        l42_112(x),
        l42_113(x),
        l42_114(x),
        l42_115(x),
        l42_116(x),
        l42_117(x),
        l42_118(x),
        l42_119(x),
        l42_120(x),
        l42_121(x),
        l42_122(x),
        l42_123(x),
        l42_124(x),
        l42_125(x),
        l42_126(x),
        l42_127(x),
        l42_128(x),
        l42_129(x),
        l42_130(x),
        l42_131(x),
        l42_132(x),
        l42_133(x),
        l42_134(x),
        l42_135(x),
        l42_136(x),
        l42_137(x),
        l42_138(x),
        l42_139(x),
        l42_140(x),
        l42_141(x),
        l42_142(x),
        l42_143(x),
        l42_144(x),
        l42_145(x),
        l42_146(x),
        l42_147(x),
        l42_148(x),
        l42_149(x),
        l42_150(x),
        l42_151(x),
        l42_152(x),
        l42_153(x),
        l42_154(x),
        l42_155(x),
        l42_156(x),
        l42_157(x),
        l42_158(x),
        l42_159(x),
        l42_160(x),
        l42_161(x),
        l42_162(x),
        l42_163(x),
        l42_164(x),
        l42_165(x),
        l42_166(x),
        l42_167(x),
        l42_168(x),
        l42_169(x),
        l42_170(x),
        l42_171(x),
        l42_172(x),
        l42_173(x),
        l42_174(x),
        l42_175(x),
        l42_176(x),
        l42_177(x),
        l42_178(x),
        l42_179(x),
        l42_180(x),
        l42_181(x),
        l42_182(x),
        l42_183(x),
        l42_184(x),
        l42_185(x),
        l42_186(x),
        l42_187(x),
        l42_188(x),
        l42_189(x),
        l42_190(x),
        l42_191(x),
        l42_192(x),
        l42_193(x),
        l42_194(x),
        l42_195(x),
        l42_196(x),
        l42_197(x),
        l42_198(x),
        l42_199(x),
        l42_200(x),
        l42_201(x),
        l42_202(x),
        l42_203(x),
        l42_204(x),
        l42_205(x),
        l42_206(x),
        l42_207(x),
        l42_208(x),
        l42_209(x),
        l42_210(x),
        l42_211(x),
        l42_212(x),
        l42_213(x),
        l42_214(x),
        l42_215(x),
        l42_216(x),
        l42_217(x),
        l42_218(x),
        l42_219(x),
        l42_220(x),
        l42_221(x),
        l42_222(x),
        l42_223(x),
        l42_224(x),
        l42_225(x),
        l42_226(x),
        l42_227(x),
        l42_228(x),
        l42_229(x),
        l42_230(x),
        l42_231(x),
        l42_232(x),
        l42_233(x),
        l42_234(x),
        l42_235(x),
        l42_236(x),
        l42_237(x),
        l42_238(x),
        l42_239(x),
        l42_240(x),
        l42_241(x),
        l42_242(x),
        l42_243(x),
        l42_244(x),
        l42_245(x),
        l42_246(x),
        l42_247(x),
        l42_248(x),
        l42_249(x),
        l42_250(x),
        l42_251(x),
        l42_252(x),
        l42_253(x),
        l42_254(x),
        l42_255(x),
        l42_256(x),
        l42_257(x),
        l42_258(x),
        l42_259(x),
        l42_260(x),
        l42_261(x),
        l42_262(x),
        l42_263(x),
        l42_264(x),
        l42_265(x),
        l42_266(x),
        l42_267(x),
        l42_268(x),
        l42_269(x),
        l42_270(x),
        l42_271(x),
        l42_272(x),
        l42_273(x),
        l42_274(x),
        l42_275(x),
        l42_276(x),
        l42_277(x),
        l42_278(x),
        l42_279(x),
        l42_280(x),
        l42_281(x),
        l42_282(x),
        l42_283(x),
        l42_284(x),
        l42_285(x),
        l42_286(x),
        l42_287(x),
        l42_288(x),
        l42_289(x),
        l42_290(x),
        l42_291(x),
        l42_292(x),
        l42_293(x),
        l42_294(x),
        l42_295(x),
        l42_296(x),
        l42_297(x),
        l42_298(x),
        l42_299(x),
        l42_300(x),
        l42_301(x),
        l42_302(x),
        l42_303(x),
        l42_304(x),
        l42_305(x),
        l42_306(x),
        l42_307(x),
        l42_308(x),
        l42_309(x),
        l42_310(x),
        l42_311(x),
        l42_312(x),
        l42_313(x),
        l42_314(x),
        l42_315(x),
        l42_316(x),
        l42_317(x),
        l42_318(x),
        l42_319(x),
        l42_320(x),
        l42_321(x),
        l42_322(x),
        l42_323(x),
        l42_324(x),
        l42_325(x),
        l42_326(x),
        l42_327(x),
        l42_328(x),
        l42_329(x),
        l42_330(x),
        l42_331(x),
        l42_332(x),
        l42_333(x),
        l42_334(x),
        l42_335(x),
        l42_336(x),
        l42_337(x),
        l42_338(x),
        l42_339(x),
        l42_340(x),
        l42_341(x),
        l42_342(x),
        l42_343(x),
        l42_344(x),
        l42_345(x),
        l42_346(x),
        l42_347(x),
        l42_348(x),
        l42_349(x),
        l42_350(x),
        l42_351(x),
        l42_352(x),
        l42_353(x),
        l42_354(x),
        l42_355(x),
        l42_356(x),
        l42_357(x),
        l42_358(x),
        l42_359(x),
        l42_360(x),
        l42_361(x),
        l42_362(x),
        l42_363(x),
        l42_364(x),
        l42_365(x),
        l42_366(x),
        l42_367(x),
        l42_368(x),
        l42_369(x),
        l42_370(x),
        l42_371(x),
        l42_372(x),
        l42_373(x),
        l42_374(x),
    ]