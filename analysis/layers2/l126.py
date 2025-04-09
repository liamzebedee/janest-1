import numpy as np




# Generated from reverse engineering
def l126_g(x: np.ndarray) -> np.ndarray:
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




def l126_0(x):
    # x is a list (or vector) of length 332
    return max(0, x[0])
def l126_1(x):
    # x is a list (or vector) of length 332
    return max(0, x[1])
def l126_2(x):
    # x is a list (or vector) of length 332
    return max(0, x[2])
def l126_3(x):
    # x is a list (or vector) of length 332
    return max(0, x[3])
def l126_4(x):
    # x is a list (or vector) of length 332
    return max(0, x[4])
def l126_5(x):
    # x is a list (or vector) of length 332
    return max(0, x[5])
def l126_6(x):
    # x is a list (or vector) of length 332
    return max(0, x[6])
def l126_7(x):
    # x is a list (or vector) of length 332
    return max(0, x[7])
def l126_8(x):
    # x is a list (or vector) of length 332
    return max(0, x[8])
def l126_9(x):
    # x is a list (or vector) of length 332
    return max(0, x[9])
def l126_10(x):
    # x is a list (or vector) of length 332
    return max(0, x[10])
def l126_11(x):
    # x is a list (or vector) of length 332
    return max(0, x[11])
def l126_12(x):
    # x is a list (or vector) of length 332
    return max(0, x[12])
def l126_13(x):
    # x is a list (or vector) of length 332
    return max(0, x[13])
def l126_14(x):
    # x is a list (or vector) of length 332
    return max(0, x[14])
def l126_15(x):
    # x is a list (or vector) of length 332
    return max(0, x[15])
def l126_16(x):
    # x is a list (or vector) of length 332
    return max(0, x[16])
def l126_17(x):
    # x is a list (or vector) of length 332
    return max(0, x[17])
def l126_18(x):
    # x is a list (or vector) of length 332
    return max(0, x[18])
def l126_19(x):
    # x is a list (or vector) of length 332
    return max(0, x[19])
def l126_20(x):
    # x is a list (or vector) of length 332
    return max(0, x[20])
def l126_21(x):
    # x is a list (or vector) of length 332
    return max(0, x[21])
def l126_22(x):
    # x is a list (or vector) of length 332
    return max(0, x[22])
def l126_23(x):
    # x is a list (or vector) of length 332
    return max(0, x[23])
def l126_24(x):
    # x is a list (or vector) of length 332
    return max(0, x[24])
def l126_25(x):
    # x is a list (or vector) of length 332
    return max(0, x[25])
def l126_26(x):
    # x is a list (or vector) of length 332
    return max(0, x[26])
def l126_27(x):
    # x is a list (or vector) of length 332
    return max(0, x[27])
def l126_28(x):
    # x is a list (or vector) of length 332
    return max(0, x[28])
def l126_29(x):
    # x is a list (or vector) of length 332
    return max(0, x[29])
def l126_30(x):
    # x is a list (or vector) of length 332
    return max(0, x[30])
def l126_31(x):
    # x is a list (or vector) of length 332
    return max(0, x[31])
def l126_32(x):
    # x is a list (or vector) of length 332
    return max(0, x[32])
def l126_33(x):
    # x is a list (or vector) of length 332
    return max(0, x[33])
def l126_34(x):
    # x is a list (or vector) of length 332
    return max(0, x[34])
def l126_35(x):
    # x is a list (or vector) of length 332
    return max(0, x[35])
def l126_36(x):
    # x is a list (or vector) of length 332
    return max(0, x[36])
def l126_37(x):
    # x is a list (or vector) of length 332
    return max(0, x[37])
def l126_38(x):
    # x is a list (or vector) of length 332
    return max(0, x[38])
def l126_39(x):
    # x is a list (or vector) of length 332
    return max(0, x[39])
def l126_40(x):
    # x is a list (or vector) of length 332
    return max(0, x[40])
def l126_41(x):
    # x is a list (or vector) of length 332
    return max(0, x[41])
def l126_42(x):
    # x is a list (or vector) of length 332
    return max(0, x[42])
def l126_43(x):
    # x is a list (or vector) of length 332
    return max(0, x[43])
def l126_44(x):
    # x is a list (or vector) of length 332
    return max(0, x[44])
def l126_45(x):
    # x is a list (or vector) of length 332
    return max(0, x[45])
def l126_46(x):
    # x is a list (or vector) of length 332
    return max(0, x[46])
def l126_47(x):
    # x is a list (or vector) of length 332
    return max(0, x[47])
def l126_48(x):
    # x is a list (or vector) of length 332
    return max(0, x[48])
def l126_49(x):
    # x is a list (or vector) of length 332
    return max(0, x[49])
def l126_50(x):
    # x is a list (or vector) of length 332
    return max(0, x[50])
def l126_51(x):
    # x is a list (or vector) of length 332
    return max(0, x[51])
def l126_52(x):
    # x is a list (or vector) of length 332
    return max(0, x[52])
def l126_53(x):
    # x is a list (or vector) of length 332
    return max(0, x[53])
def l126_54(x):
    # x is a list (or vector) of length 332
    return max(0, x[54])
def l126_55(x):
    # x is a list (or vector) of length 332
    return max(0, x[55])
def l126_56(x):
    # x is a list (or vector) of length 332
    return max(0, x[56])
def l126_57(x):
    # x is a list (or vector) of length 332
    return max(0, x[57])
def l126_58(x):
    # x is a list (or vector) of length 332
    return max(0, x[58])
def l126_59(x):
    # x is a list (or vector) of length 332
    return max(0, x[59])
def l126_60(x):
    # x is a list (or vector) of length 332
    return max(0, x[60])
def l126_61(x):
    # x is a list (or vector) of length 332
    return max(0, x[61])
def l126_62(x):
    # x is a list (or vector) of length 332
    return max(0, x[62])
def l126_63(x):
    # x is a list (or vector) of length 332
    return max(0, x[63])
def l126_64(x):
    # x is a list (or vector) of length 332
    return max(0, x[64])
def l126_65(x):
    # x is a list (or vector) of length 332
    return max(0, x[65])
def l126_66(x):
    # x is a list (or vector) of length 332
    return max(0, x[66])
def l126_67(x):
    # x is a list (or vector) of length 332
    return max(0, x[67])
def l126_68(x):
    # x is a list (or vector) of length 332
    return max(0, x[68])
def l126_69(x):
    # x is a list (or vector) of length 332
    return max(0, x[69])
def l126_70(x):
    # x is a list (or vector) of length 332
    return max(0, x[70])
def l126_71(x):
    # x is a list (or vector) of length 332
    return max(0, x[71])
def l126_72(x):
    # x is a list (or vector) of length 332
    return max(0, x[72])
def l126_73(x):
    # x is a list (or vector) of length 332
    return max(0, x[73])
def l126_74(x):
    # x is a list (or vector) of length 332
    return max(0, x[74])
def l126_75(x):
    # x is a list (or vector) of length 332
    return max(0, x[75])
def l126_76(x):
    # x is a list (or vector) of length 332
    return max(0, x[76])
def l126_77(x):
    # x is a list (or vector) of length 332
    return max(0, x[77])
def l126_78(x):
    # x is a list (or vector) of length 332
    return max(0, x[78])
def l126_79(x):
    # x is a list (or vector) of length 332
    return max(0, x[79])
def l126_80(x):
    # x is a list (or vector) of length 332
    return max(0, x[80])
def l126_81(x):
    # x is a list (or vector) of length 332
    return max(0, x[81])
def l126_82(x):
    # x is a list (or vector) of length 332
    return max(0, x[82])
def l126_83(x):
    # x is a list (or vector) of length 332
    return max(0, x[83])
def l126_84(x):
    # x is a list (or vector) of length 332
    return max(0, x[84])
def l126_85(x):
    # x is a list (or vector) of length 332
    return max(0, x[85])
def l126_86(x):
    # x is a list (or vector) of length 332
    return max(0, x[86])
def l126_87(x):
    # x is a list (or vector) of length 332
    return max(0, x[87])
def l126_88(x):
    # x is a list (or vector) of length 332
    return max(0, x[88])
def l126_89(x):
    # x is a list (or vector) of length 332
    return max(0, x[89])
def l126_90(x):
    # x is a list (or vector) of length 332
    return max(0, x[90])
def l126_91(x):
    # x is a list (or vector) of length 332
    return max(0, x[91])
def l126_92(x):
    # x is a list (or vector) of length 332
    return max(0, x[92])
def l126_93(x):
    # x is a list (or vector) of length 332
    return max(0, x[93])
def l126_94(x):
    # x is a list (or vector) of length 332
    return max(0, x[94])
def l126_95(x):
    # x is a list (or vector) of length 332
    return max(0, x[95])
def l126_96(x):
    # x is a list (or vector) of length 332
    return max(0, x[96])
def l126_97(x):
    # x is a list (or vector) of length 332
    return max(0, x[97])
def l126_98(x):
    # x is a list (or vector) of length 332
    return max(0, x[98])
def l126_99(x):
    # x is a list (or vector) of length 332
    return max(0, x[99])
def l126_100(x):
    # x is a list (or vector) of length 332
    return max(0, x[100])
def l126_101(x):
    # x is a list (or vector) of length 332
    return max(0, x[101])
def l126_102(x):
    # x is a list (or vector) of length 332
    return max(0, x[102])
def l126_103(x):
    # x is a list (or vector) of length 332
    return max(0, x[103])
def l126_104(x):
    # x is a list (or vector) of length 332
    return max(0, x[104])
def l126_105(x):
    # x is a list (or vector) of length 332
    return max(0, x[105])
def l126_106(x):
    # x is a list (or vector) of length 332
    return max(0, x[106])
def l126_107(x):
    # x is a list (or vector) of length 332
    return max(0, x[107])
def l126_108(x):
    # x is a list (or vector) of length 332
    return max(0, x[108])
def l126_109(x):
    # x is a list (or vector) of length 332
    return max(0, x[109])
def l126_110(x):
    # x is a list (or vector) of length 332
    return max(0, x[110])
def l126_111(x):
    # x is a list (or vector) of length 332
    return max(0, x[111])
def l126_112(x):
    # x is a list (or vector) of length 332
    return max(0, x[112])
def l126_113(x):
    # x is a list (or vector) of length 332
    return max(0, x[113])
def l126_114(x):
    # x is a list (or vector) of length 332
    return max(0, x[114])
def l126_115(x):
    # x is a list (or vector) of length 332
    return max(0, x[115])
def l126_116(x):
    # x is a list (or vector) of length 332
    return max(0, x[116])
def l126_117(x):
    # x is a list (or vector) of length 332
    return max(0, x[117])
def l126_118(x):
    # x is a list (or vector) of length 332
    return max(0, x[118])
def l126_119(x):
    # x is a list (or vector) of length 332
    return max(0, x[119])
def l126_120(x):
    # x is a list (or vector) of length 332
    return max(0, x[120])
def l126_121(x):
    # x is a list (or vector) of length 332
    return max(0, x[121])
def l126_122(x):
    # x is a list (or vector) of length 332
    return max(0, x[122])
def l126_123(x):
    # x is a list (or vector) of length 332
    return max(0, x[123])
def l126_124(x):
    # x is a list (or vector) of length 332
    return max(0, x[124])
def l126_125(x):
    # x is a list (or vector) of length 332
    return max(0, x[125])
def l126_126(x):
    # x is a list (or vector) of length 332
    return max(0, x[126])
def l126_127(x):
    # x is a list (or vector) of length 332
    return max(0, x[127])
def l126_128(x):
    # x is a list (or vector) of length 332
    return max(0, x[128] + -2.0*x[160])
def l126_129(x):
    # x is a list (or vector) of length 332
    return max(0, x[129] + -2.0*x[161])
def l126_130(x):
    # x is a list (or vector) of length 332
    return max(0, x[130] + -2.0*x[162])
def l126_131(x):
    # x is a list (or vector) of length 332
    return max(0, x[131] + -2.0*x[163])
def l126_132(x):
    # x is a list (or vector) of length 332
    return max(0, x[132] + -2.0*x[164])
def l126_133(x):
    # x is a list (or vector) of length 332
    return max(0, x[133] + -2.0*x[165])
def l126_134(x):
    # x is a list (or vector) of length 332
    return max(0, x[134] + -2.0*x[166])
def l126_135(x):
    # x is a list (or vector) of length 332
    return max(0, x[135] + -2.0*x[167])
def l126_136(x):
    # x is a list (or vector) of length 332
    return max(0, x[136] + -2.0*x[168])
def l126_137(x):
    # x is a list (or vector) of length 332
    return max(0, x[137] + -2.0*x[169])
def l126_138(x):
    # x is a list (or vector) of length 332
    return max(0, x[138] + -2.0*x[170])
def l126_139(x):
    # x is a list (or vector) of length 332
    return max(0, x[139] + -2.0*x[171])
def l126_140(x):
    # x is a list (or vector) of length 332
    return max(0, x[140] + -2.0*x[172])
def l126_141(x):
    # x is a list (or vector) of length 332
    return max(0, x[141] + -2.0*x[173])
def l126_142(x):
    # x is a list (or vector) of length 332
    return max(0, x[142] + -2.0*x[174])
def l126_143(x):
    # x is a list (or vector) of length 332
    return max(0, x[143] + -2.0*x[175])
def l126_144(x):
    # x is a list (or vector) of length 332
    return max(0, x[144] + -2.0*x[176])
def l126_145(x):
    # x is a list (or vector) of length 332
    return max(0, x[145] + -2.0*x[177])
def l126_146(x):
    # x is a list (or vector) of length 332
    return max(0, x[146] + -2.0*x[178])
def l126_147(x):
    # x is a list (or vector) of length 332
    return max(0, x[147] + -2.0*x[179])
def l126_148(x):
    # x is a list (or vector) of length 332
    return max(0, x[148] + -2.0*x[180])
def l126_149(x):
    # x is a list (or vector) of length 332
    return max(0, x[149] + -2.0*x[181])
def l126_150(x):
    # x is a list (or vector) of length 332
    return max(0, x[150] + -2.0*x[182])
def l126_151(x):
    # x is a list (or vector) of length 332
    return max(0, x[151] + -2.0*x[183])
def l126_152(x):
    # x is a list (or vector) of length 332
    return max(0, x[152] + -2.0*x[184])
def l126_153(x):
    # x is a list (or vector) of length 332
    return max(0, x[153] + -2.0*x[185])
def l126_154(x):
    # x is a list (or vector) of length 332
    return max(0, x[154] + -2.0*x[186])
def l126_155(x):
    # x is a list (or vector) of length 332
    return max(0, x[155] + -2.0*x[187])
def l126_156(x):
    # x is a list (or vector) of length 332
    return max(0, x[156] + -2.0*x[188])
def l126_157(x):
    # x is a list (or vector) of length 332
    return max(0, x[157] + -2.0*x[189])
def l126_158(x):
    # x is a list (or vector) of length 332
    return max(0, x[158] + -2.0*x[190])
def l126_159(x):
    # x is a list (or vector) of length 332
    return max(0, x[159] + -2.0*x[191])
def l126_160(x):
    # x is a list (or vector) of length 332
    return max(0, x[192])
def l126_161(x):
    # x is a list (or vector) of length 332
    return max(0, x[192] + x[225] + -1.0)
def l126_162(x):
    # x is a list (or vector) of length 332
    return max(0, x[193] + x[226] + -1.0)
def l126_163(x):
    # x is a list (or vector) of length 332
    return max(0, x[194] + x[227] + -1.0)
def l126_164(x):
    # x is a list (or vector) of length 332
    return max(0, x[195] + x[228] + -1.0)
def l126_165(x):
    # x is a list (or vector) of length 332
    return max(0, x[196] + x[229] + -1.0)
def l126_166(x):
    # x is a list (or vector) of length 332
    return max(0, x[197] + x[230] + -1.0)
def l126_167(x):
    # x is a list (or vector) of length 332
    return max(0, x[198] + x[231] + -1.0)
def l126_168(x):
    # x is a list (or vector) of length 332
    return max(0, x[199] + x[232] + -1.0)
def l126_169(x):
    # x is a list (or vector) of length 332
    return max(0, x[200] + x[233] + -1.0)
def l126_170(x):
    # x is a list (or vector) of length 332
    return max(0, x[201] + x[234] + -1.0)
def l126_171(x):
    # x is a list (or vector) of length 332
    return max(0, x[202] + x[235] + -1.0)
def l126_172(x):
    # x is a list (or vector) of length 332
    return max(0, x[203] + x[236] + -1.0)
def l126_173(x):
    # x is a list (or vector) of length 332
    return max(0, x[204] + x[237] + -1.0)
def l126_174(x):
    # x is a list (or vector) of length 332
    return max(0, x[205] + x[238] + -1.0)
def l126_175(x):
    # x is a list (or vector) of length 332
    return max(0, x[206] + x[239] + -1.0)
def l126_176(x):
    # x is a list (or vector) of length 332
    return max(0, x[207] + x[240] + -1.0)
def l126_177(x):
    # x is a list (or vector) of length 332
    return max(0, x[208] + x[241] + -1.0)
def l126_178(x):
    # x is a list (or vector) of length 332
    return max(0, x[209] + x[242] + -1.0)
def l126_179(x):
    # x is a list (or vector) of length 332
    return max(0, x[210] + x[243] + -1.0)
def l126_180(x):
    # x is a list (or vector) of length 332
    return max(0, x[211] + x[244] + -1.0)
def l126_181(x):
    # x is a list (or vector) of length 332
    return max(0, x[212] + x[245] + -1.0)
def l126_182(x):
    # x is a list (or vector) of length 332
    return max(0, x[213] + x[246] + -1.0)
def l126_183(x):
    # x is a list (or vector) of length 332
    return max(0, x[214] + x[247] + -1.0)
def l126_184(x):
    # x is a list (or vector) of length 332
    return max(0, x[215] + x[248] + -1.0)
def l126_185(x):
    # x is a list (or vector) of length 332
    return max(0, x[216] + x[249] + -1.0)
def l126_186(x):
    # x is a list (or vector) of length 332
    return max(0, x[217] + x[250] + -1.0)
def l126_187(x):
    # x is a list (or vector) of length 332
    return max(0, x[218] + x[251] + -1.0)
def l126_188(x):
    # x is a list (or vector) of length 332
    return max(0, x[219] + x[252] + -1.0)
def l126_189(x):
    # x is a list (or vector) of length 332
    return max(0, x[220] + x[253] + -1.0)
def l126_190(x):
    # x is a list (or vector) of length 332
    return max(0, x[221] + x[254] + -1.0)
def l126_191(x):
    # x is a list (or vector) of length 332
    return max(0, x[222] + x[255] + -1.0)
def l126_192(x):
    # x is a list (or vector) of length 332
    return max(0, x[193])
def l126_193(x):
    # x is a list (or vector) of length 332
    return max(0, x[194])
def l126_194(x):
    # x is a list (or vector) of length 332
    return max(0, x[195])
def l126_195(x):
    # x is a list (or vector) of length 332
    return max(0, x[196])
def l126_196(x):
    # x is a list (or vector) of length 332
    return max(0, x[197])
def l126_197(x):
    # x is a list (or vector) of length 332
    return max(0, x[198])
def l126_198(x):
    # x is a list (or vector) of length 332
    return max(0, x[199])
def l126_199(x):
    # x is a list (or vector) of length 332
    return max(0, x[200])
def l126_200(x):
    # x is a list (or vector) of length 332
    return max(0, x[201])
def l126_201(x):
    # x is a list (or vector) of length 332
    return max(0, x[202])
def l126_202(x):
    # x is a list (or vector) of length 332
    return max(0, x[203])
def l126_203(x):
    # x is a list (or vector) of length 332
    return max(0, x[204])
def l126_204(x):
    # x is a list (or vector) of length 332
    return max(0, x[205])
def l126_205(x):
    # x is a list (or vector) of length 332
    return max(0, x[206])
def l126_206(x):
    # x is a list (or vector) of length 332
    return max(0, x[207])
def l126_207(x):
    # x is a list (or vector) of length 332
    return max(0, x[208])
def l126_208(x):
    # x is a list (or vector) of length 332
    return max(0, x[209])
def l126_209(x):
    # x is a list (or vector) of length 332
    return max(0, x[210])
def l126_210(x):
    # x is a list (or vector) of length 332
    return max(0, x[211])
def l126_211(x):
    # x is a list (or vector) of length 332
    return max(0, x[212])
def l126_212(x):
    # x is a list (or vector) of length 332
    return max(0, x[213])
def l126_213(x):
    # x is a list (or vector) of length 332
    return max(0, x[214])
def l126_214(x):
    # x is a list (or vector) of length 332
    return max(0, x[215])
def l126_215(x):
    # x is a list (or vector) of length 332
    return max(0, x[216])
def l126_216(x):
    # x is a list (or vector) of length 332
    return max(0, x[217])
def l126_217(x):
    # x is a list (or vector) of length 332
    return max(0, x[218])
def l126_218(x):
    # x is a list (or vector) of length 332
    return max(0, x[219])
def l126_219(x):
    # x is a list (or vector) of length 332
    return max(0, x[220])
def l126_220(x):
    # x is a list (or vector) of length 332
    return max(0, x[221])
def l126_221(x):
    # x is a list (or vector) of length 332
    return max(0, x[222])
def l126_222(x):
    # x is a list (or vector) of length 332
    return max(0, x[223])
def l126_223(x):
    # x is a list (or vector) of length 332
    return max(0, x[224] + x[225] + -1.0)
def l126_224(x):
    # x is a list (or vector) of length 332
    return max(0, x[225] + x[226] + -1.0)
def l126_225(x):
    # x is a list (or vector) of length 332
    return max(0, x[226] + x[227] + -1.0)
def l126_226(x):
    # x is a list (or vector) of length 332
    return max(0, x[227] + x[228] + -1.0)
def l126_227(x):
    # x is a list (or vector) of length 332
    return max(0, x[228] + x[229] + -1.0)
def l126_228(x):
    # x is a list (or vector) of length 332
    return max(0, x[229] + x[230] + -1.0)
def l126_229(x):
    # x is a list (or vector) of length 332
    return max(0, x[230] + x[231] + -1.0)
def l126_230(x):
    # x is a list (or vector) of length 332
    return max(0, x[231] + x[232] + -1.0)
def l126_231(x):
    # x is a list (or vector) of length 332
    return max(0, x[232] + x[233] + -1.0)
def l126_232(x):
    # x is a list (or vector) of length 332
    return max(0, x[233] + x[234] + -1.0)
def l126_233(x):
    # x is a list (or vector) of length 332
    return max(0, x[234] + x[235] + -1.0)
def l126_234(x):
    # x is a list (or vector) of length 332
    return max(0, x[235] + x[236] + -1.0)
def l126_235(x):
    # x is a list (or vector) of length 332
    return max(0, x[236] + x[237] + -1.0)
def l126_236(x):
    # x is a list (or vector) of length 332
    return max(0, x[237] + x[238] + -1.0)
def l126_237(x):
    # x is a list (or vector) of length 332
    return max(0, x[238] + x[239] + -1.0)
def l126_238(x):
    # x is a list (or vector) of length 332
    return max(0, x[239] + x[240] + -1.0)
def l126_239(x):
    # x is a list (or vector) of length 332
    return max(0, x[240] + x[241] + -1.0)
def l126_240(x):
    # x is a list (or vector) of length 332
    return max(0, x[241] + x[242] + -1.0)
def l126_241(x):
    # x is a list (or vector) of length 332
    return max(0, x[242] + x[243] + -1.0)
def l126_242(x):
    # x is a list (or vector) of length 332
    return max(0, x[243] + x[244] + -1.0)
def l126_243(x):
    # x is a list (or vector) of length 332
    return max(0, x[244] + x[245] + -1.0)
def l126_244(x):
    # x is a list (or vector) of length 332
    return max(0, x[245] + x[246] + -1.0)
def l126_245(x):
    # x is a list (or vector) of length 332
    return max(0, x[246] + x[247] + -1.0)
def l126_246(x):
    # x is a list (or vector) of length 332
    return max(0, x[247] + x[248] + -1.0)
def l126_247(x):
    # x is a list (or vector) of length 332
    return max(0, x[248] + x[249] + -1.0)
def l126_248(x):
    # x is a list (or vector) of length 332
    return max(0, x[249] + x[250] + -1.0)
def l126_249(x):
    # x is a list (or vector) of length 332
    return max(0, x[250] + x[251] + -1.0)
def l126_250(x):
    # x is a list (or vector) of length 332
    return max(0, x[251] + x[252] + -1.0)
def l126_251(x):
    # x is a list (or vector) of length 332
    return max(0, x[252] + x[253] + -1.0)
def l126_252(x):
    # x is a list (or vector) of length 332
    return max(0, x[253] + x[254] + -1.0)
def l126_253(x):
    # x is a list (or vector) of length 332
    return max(0, x[254] + x[255] + -1.0)
def l126_254(x):
    # x is a list (or vector) of length 332
    return max(0, x[224])
def l126_255(x):
    # x is a list (or vector) of length 332
    return max(0, x[224])
def l126_256(x):
    # x is a list (or vector) of length 332
    return max(0, x[225])
def l126_257(x):
    # x is a list (or vector) of length 332
    return max(0, x[226])
def l126_258(x):
    # x is a list (or vector) of length 332
    return max(0, x[227])
def l126_259(x):
    # x is a list (or vector) of length 332
    return max(0, x[228])
def l126_260(x):
    # x is a list (or vector) of length 332
    return max(0, x[229])
def l126_261(x):
    # x is a list (or vector) of length 332
    return max(0, x[230])
def l126_262(x):
    # x is a list (or vector) of length 332
    return max(0, x[231])
def l126_263(x):
    # x is a list (or vector) of length 332
    return max(0, x[232])
def l126_264(x):
    # x is a list (or vector) of length 332
    return max(0, x[233])
def l126_265(x):
    # x is a list (or vector) of length 332
    return max(0, x[234])
def l126_266(x):
    # x is a list (or vector) of length 332
    return max(0, x[235])
def l126_267(x):
    # x is a list (or vector) of length 332
    return max(0, x[236])
def l126_268(x):
    # x is a list (or vector) of length 332
    return max(0, x[237])
def l126_269(x):
    # x is a list (or vector) of length 332
    return max(0, x[238])
def l126_270(x):
    # x is a list (or vector) of length 332
    return max(0, x[239])
def l126_271(x):
    # x is a list (or vector) of length 332
    return max(0, x[240])
def l126_272(x):
    # x is a list (or vector) of length 332
    return max(0, x[241])
def l126_273(x):
    # x is a list (or vector) of length 332
    return max(0, x[242])
def l126_274(x):
    # x is a list (or vector) of length 332
    return max(0, x[243])
def l126_275(x):
    # x is a list (or vector) of length 332
    return max(0, x[244])
def l126_276(x):
    # x is a list (or vector) of length 332
    return max(0, x[245])
def l126_277(x):
    # x is a list (or vector) of length 332
    return max(0, x[246])
def l126_278(x):
    # x is a list (or vector) of length 332
    return max(0, x[247])
def l126_279(x):
    # x is a list (or vector) of length 332
    return max(0, x[248])
def l126_280(x):
    # x is a list (or vector) of length 332
    return max(0, x[249])
def l126_281(x):
    # x is a list (or vector) of length 332
    return max(0, x[250])
def l126_282(x):
    # x is a list (or vector) of length 332
    return max(0, x[251])
def l126_283(x):
    # x is a list (or vector) of length 332
    return max(0, x[252])
def l126_284(x):
    # x is a list (or vector) of length 332
    return max(0, x[253])
def l126_285(x):
    # x is a list (or vector) of length 332
    return max(0, x[254])
def l126_286(x):
    # x is a list (or vector) of length 332
    return max(0, x[255])
def l126_287(x):
    # x is a list (or vector) of length 332
    return max(0, x[256])
def l126_288(x):
    # x is a list (or vector) of length 332
    return max(0, x[257])
def l126_289(x):
    # x is a list (or vector) of length 332
    return max(0, x[258])
def l126_290(x):
    # x is a list (or vector) of length 332
    return max(0, x[259])
def l126_291(x):
    # x is a list (or vector) of length 332
    return max(0, x[260])
def l126_292(x):
    # x is a list (or vector) of length 332
    return max(0, x[261])
def l126_293(x):
    # x is a list (or vector) of length 332
    return max(0, x[262])
def l126_294(x):
    # x is a list (or vector) of length 332
    return max(0, x[263])
def l126_295(x):
    # x is a list (or vector) of length 332
    return max(0, -1.0*x[264] + 32.0)
def l126_296(x):
    # x is a list (or vector) of length 332
    return max(0, -1.0*x[265] + 32.0)
def l126_297(x):
    # x is a list (or vector) of length 332
    return max(0, -1.0*x[266] + 32.0)
def l126_298(x):
    # x is a list (or vector) of length 332
    return max(0, -1.0*x[267] + 32.0)
def l126_299(x):
    # x is a list (or vector) of length 332
    return max(0, x[264])
def l126_300(x):
    # x is a list (or vector) of length 332
    return max(0, x[265])
def l126_301(x):
    # x is a list (or vector) of length 332
    return max(0, x[266])
def l126_302(x):
    # x is a list (or vector) of length 332
    return max(0, x[267])
def l126_303(x):
    # x is a list (or vector) of length 332
    return max(0, x[264] + -31.0)
def l126_304(x):
    # x is a list (or vector) of length 332
    return max(0, x[265] + -31.0)
def l126_305(x):
    # x is a list (or vector) of length 332
    return max(0, x[266] + -31.0)
def l126_306(x):
    # x is a list (or vector) of length 332
    return max(0, x[267] + -31.0)
def l126_307(x):
    # x is a list (or vector) of length 332
    return max(0, x[264] + -32.0)
def l126_308(x):
    # x is a list (or vector) of length 332
    return max(0, x[265] + -32.0)
def l126_309(x):
    # x is a list (or vector) of length 332
    return max(0, x[266] + -32.0)
def l126_310(x):
    # x is a list (or vector) of length 332
    return max(0, x[267] + -32.0)
def l126_311(x):
    # x is a list (or vector) of length 332
    return max(0, x[268])
def l126_312(x):
    # x is a list (or vector) of length 332
    return max(0, x[269])
def l126_313(x):
    # x is a list (or vector) of length 332
    return max(0, x[270])
def l126_314(x):
    # x is a list (or vector) of length 332
    return max(0, x[271])
def l126_315(x):
    # x is a list (or vector) of length 332
    return max(0, x[272])
def l126_316(x):
    # x is a list (or vector) of length 332
    return max(0, x[273])
def l126_317(x):
    # x is a list (or vector) of length 332
    return max(0, x[274])
def l126_318(x):
    # x is a list (or vector) of length 332
    return max(0, x[275])
def l126_319(x):
    # x is a list (or vector) of length 332
    return max(0, x[276])
def l126_320(x):
    # x is a list (or vector) of length 332
    return max(0, x[277])
def l126_321(x):
    # x is a list (or vector) of length 332
    return max(0, x[278])
def l126_322(x):
    # x is a list (or vector) of length 332
    return max(0, x[279])
def l126_323(x):
    # x is a list (or vector) of length 332
    return max(0, x[280])
def l126_324(x):
    # x is a list (or vector) of length 332
    return max(0, x[281])
def l126_325(x):
    # x is a list (or vector) of length 332
    return max(0, x[282])
def l126_326(x):
    # x is a list (or vector) of length 332
    return max(0, x[283])
def l126_327(x):
    # x is a list (or vector) of length 332
    return max(0, x[284])
def l126_328(x):
    # x is a list (or vector) of length 332
    return max(0, x[285])
def l126_329(x):
    # x is a list (or vector) of length 332
    return max(0, x[286])
def l126_330(x):
    # x is a list (or vector) of length 332
    return max(0, x[287])
def l126_331(x):
    # x is a list (or vector) of length 332
    return max(0, x[288])
def l126_332(x):
    # x is a list (or vector) of length 332
    return max(0, x[289])
def l126_333(x):
    # x is a list (or vector) of length 332
    return max(0, x[290])
def l126_334(x):
    # x is a list (or vector) of length 332
    return max(0, x[291])
def l126_335(x):
    # x is a list (or vector) of length 332
    return max(0, x[292])
def l126_336(x):
    # x is a list (or vector) of length 332
    return max(0, x[293])
def l126_337(x):
    # x is a list (or vector) of length 332
    return max(0, x[294])
def l126_338(x):
    # x is a list (or vector) of length 332
    return max(0, x[295])
def l126_339(x):
    # x is a list (or vector) of length 332
    return max(0, x[296])
def l126_340(x):
    # x is a list (or vector) of length 332
    return max(0, x[297])
def l126_341(x):
    # x is a list (or vector) of length 332
    return max(0, x[298])
def l126_342(x):
    # x is a list (or vector) of length 332
    return max(0, x[299])
def l126_343(x):
    # x is a list (or vector) of length 332
    return max(0, x[300])
def l126_344(x):
    # x is a list (or vector) of length 332
    return max(0, x[301])
def l126_345(x):
    # x is a list (or vector) of length 332
    return max(0, x[302])
def l126_346(x):
    # x is a list (or vector) of length 332
    return max(0, x[303])
def l126_347(x):
    # x is a list (or vector) of length 332
    return max(0, x[304])
def l126_348(x):
    # x is a list (or vector) of length 332
    return max(0, x[305])
def l126_349(x):
    # x is a list (or vector) of length 332
    return max(0, x[306])
def l126_350(x):
    # x is a list (or vector) of length 332
    return max(0, x[307])
def l126_351(x):
    # x is a list (or vector) of length 332
    return max(0, x[308])
def l126_352(x):
    # x is a list (or vector) of length 332
    return max(0, x[309])
def l126_353(x):
    # x is a list (or vector) of length 332
    return max(0, x[310])
def l126_354(x):
    # x is a list (or vector) of length 332
    return max(0, x[311])
def l126_355(x):
    # x is a list (or vector) of length 332
    return max(0, x[312])
def l126_356(x):
    # x is a list (or vector) of length 332
    return max(0, x[313])
def l126_357(x):
    # x is a list (or vector) of length 332
    return max(0, x[314])
def l126_358(x):
    # x is a list (or vector) of length 332
    return max(0, x[315])
def l126_359(x):
    # x is a list (or vector) of length 332
    return max(0, x[316])
def l126_360(x):
    # x is a list (or vector) of length 332
    return max(0, x[317])
def l126_361(x):
    # x is a list (or vector) of length 332
    return max(0, x[318])
def l126_362(x):
    # x is a list (or vector) of length 332
    return max(0, x[319])
def l126_363(x):
    # x is a list (or vector) of length 332
    return max(0, x[320])
def l126_364(x):
    # x is a list (or vector) of length 332
    return max(0, x[321])
def l126_365(x):
    # x is a list (or vector) of length 332
    return max(0, x[322])
def l126_366(x):
    # x is a list (or vector) of length 332
    return max(0, x[323])
def l126_367(x):
    # x is a list (or vector) of length 332
    return max(0, x[324])
def l126_368(x):
    # x is a list (or vector) of length 332
    return max(0, x[325])
def l126_369(x):
    # x is a list (or vector) of length 332
    return max(0, x[326])
def l126_370(x):
    # x is a list (or vector) of length 332
    return max(0, x[327])
def l126_371(x):
    # x is a list (or vector) of length 332
    return max(0, x[328])
def l126_372(x):
    # x is a list (or vector) of length 332
    return max(0, x[329])
def l126_373(x):
    # x is a list (or vector) of length 332
    return max(0, x[330])
def l126_374(x):
    # x is a list (or vector) of length 332
    return max(0, x[331])
def l126_(x):
    # x is a list (or vector) of length 332
    return [
        l126_0(x),
        l126_1(x),
        l126_2(x),
        l126_3(x),
        l126_4(x),
        l126_5(x),
        l126_6(x),
        l126_7(x),
        l126_8(x),
        l126_9(x),
        l126_10(x),
        l126_11(x),
        l126_12(x),
        l126_13(x),
        l126_14(x),
        l126_15(x),
        l126_16(x),
        l126_17(x),
        l126_18(x),
        l126_19(x),
        l126_20(x),
        l126_21(x),
        l126_22(x),
        l126_23(x),
        l126_24(x),
        l126_25(x),
        l126_26(x),
        l126_27(x),
        l126_28(x),
        l126_29(x),
        l126_30(x),
        l126_31(x),
        l126_32(x),
        l126_33(x),
        l126_34(x),
        l126_35(x),
        l126_36(x),
        l126_37(x),
        l126_38(x),
        l126_39(x),
        l126_40(x),
        l126_41(x),
        l126_42(x),
        l126_43(x),
        l126_44(x),
        l126_45(x),
        l126_46(x),
        l126_47(x),
        l126_48(x),
        l126_49(x),
        l126_50(x),
        l126_51(x),
        l126_52(x),
        l126_53(x),
        l126_54(x),
        l126_55(x),
        l126_56(x),
        l126_57(x),
        l126_58(x),
        l126_59(x),
        l126_60(x),
        l126_61(x),
        l126_62(x),
        l126_63(x),
        l126_64(x),
        l126_65(x),
        l126_66(x),
        l126_67(x),
        l126_68(x),
        l126_69(x),
        l126_70(x),
        l126_71(x),
        l126_72(x),
        l126_73(x),
        l126_74(x),
        l126_75(x),
        l126_76(x),
        l126_77(x),
        l126_78(x),
        l126_79(x),
        l126_80(x),
        l126_81(x),
        l126_82(x),
        l126_83(x),
        l126_84(x),
        l126_85(x),
        l126_86(x),
        l126_87(x),
        l126_88(x),
        l126_89(x),
        l126_90(x),
        l126_91(x),
        l126_92(x),
        l126_93(x),
        l126_94(x),
        l126_95(x),
        l126_96(x),
        l126_97(x),
        l126_98(x),
        l126_99(x),
        l126_100(x),
        l126_101(x),
        l126_102(x),
        l126_103(x),
        l126_104(x),
        l126_105(x),
        l126_106(x),
        l126_107(x),
        l126_108(x),
        l126_109(x),
        l126_110(x),
        l126_111(x),
        l126_112(x),
        l126_113(x),
        l126_114(x),
        l126_115(x),
        l126_116(x),
        l126_117(x),
        l126_118(x),
        l126_119(x),
        l126_120(x),
        l126_121(x),
        l126_122(x),
        l126_123(x),
        l126_124(x),
        l126_125(x),
        l126_126(x),
        l126_127(x),
        l126_128(x),
        l126_129(x),
        l126_130(x),
        l126_131(x),
        l126_132(x),
        l126_133(x),
        l126_134(x),
        l126_135(x),
        l126_136(x),
        l126_137(x),
        l126_138(x),
        l126_139(x),
        l126_140(x),
        l126_141(x),
        l126_142(x),
        l126_143(x),
        l126_144(x),
        l126_145(x),
        l126_146(x),
        l126_147(x),
        l126_148(x),
        l126_149(x),
        l126_150(x),
        l126_151(x),
        l126_152(x),
        l126_153(x),
        l126_154(x),
        l126_155(x),
        l126_156(x),
        l126_157(x),
        l126_158(x),
        l126_159(x),
        l126_160(x),
        l126_161(x),
        l126_162(x),
        l126_163(x),
        l126_164(x),
        l126_165(x),
        l126_166(x),
        l126_167(x),
        l126_168(x),
        l126_169(x),
        l126_170(x),
        l126_171(x),
        l126_172(x),
        l126_173(x),
        l126_174(x),
        l126_175(x),
        l126_176(x),
        l126_177(x),
        l126_178(x),
        l126_179(x),
        l126_180(x),
        l126_181(x),
        l126_182(x),
        l126_183(x),
        l126_184(x),
        l126_185(x),
        l126_186(x),
        l126_187(x),
        l126_188(x),
        l126_189(x),
        l126_190(x),
        l126_191(x),
        l126_192(x),
        l126_193(x),
        l126_194(x),
        l126_195(x),
        l126_196(x),
        l126_197(x),
        l126_198(x),
        l126_199(x),
        l126_200(x),
        l126_201(x),
        l126_202(x),
        l126_203(x),
        l126_204(x),
        l126_205(x),
        l126_206(x),
        l126_207(x),
        l126_208(x),
        l126_209(x),
        l126_210(x),
        l126_211(x),
        l126_212(x),
        l126_213(x),
        l126_214(x),
        l126_215(x),
        l126_216(x),
        l126_217(x),
        l126_218(x),
        l126_219(x),
        l126_220(x),
        l126_221(x),
        l126_222(x),
        l126_223(x),
        l126_224(x),
        l126_225(x),
        l126_226(x),
        l126_227(x),
        l126_228(x),
        l126_229(x),
        l126_230(x),
        l126_231(x),
        l126_232(x),
        l126_233(x),
        l126_234(x),
        l126_235(x),
        l126_236(x),
        l126_237(x),
        l126_238(x),
        l126_239(x),
        l126_240(x),
        l126_241(x),
        l126_242(x),
        l126_243(x),
        l126_244(x),
        l126_245(x),
        l126_246(x),
        l126_247(x),
        l126_248(x),
        l126_249(x),
        l126_250(x),
        l126_251(x),
        l126_252(x),
        l126_253(x),
        l126_254(x),
        l126_255(x),
        l126_256(x),
        l126_257(x),
        l126_258(x),
        l126_259(x),
        l126_260(x),
        l126_261(x),
        l126_262(x),
        l126_263(x),
        l126_264(x),
        l126_265(x),
        l126_266(x),
        l126_267(x),
        l126_268(x),
        l126_269(x),
        l126_270(x),
        l126_271(x),
        l126_272(x),
        l126_273(x),
        l126_274(x),
        l126_275(x),
        l126_276(x),
        l126_277(x),
        l126_278(x),
        l126_279(x),
        l126_280(x),
        l126_281(x),
        l126_282(x),
        l126_283(x),
        l126_284(x),
        l126_285(x),
        l126_286(x),
        l126_287(x),
        l126_288(x),
        l126_289(x),
        l126_290(x),
        l126_291(x),
        l126_292(x),
        l126_293(x),
        l126_294(x),
        l126_295(x),
        l126_296(x),
        l126_297(x),
        l126_298(x),
        l126_299(x),
        l126_300(x),
        l126_301(x),
        l126_302(x),
        l126_303(x),
        l126_304(x),
        l126_305(x),
        l126_306(x),
        l126_307(x),
        l126_308(x),
        l126_309(x),
        l126_310(x),
        l126_311(x),
        l126_312(x),
        l126_313(x),
        l126_314(x),
        l126_315(x),
        l126_316(x),
        l126_317(x),
        l126_318(x),
        l126_319(x),
        l126_320(x),
        l126_321(x),
        l126_322(x),
        l126_323(x),
        l126_324(x),
        l126_325(x),
        l126_326(x),
        l126_327(x),
        l126_328(x),
        l126_329(x),
        l126_330(x),
        l126_331(x),
        l126_332(x),
        l126_333(x),
        l126_334(x),
        l126_335(x),
        l126_336(x),
        l126_337(x),
        l126_338(x),
        l126_339(x),
        l126_340(x),
        l126_341(x),
        l126_342(x),
        l126_343(x),
        l126_344(x),
        l126_345(x),
        l126_346(x),
        l126_347(x),
        l126_348(x),
        l126_349(x),
        l126_350(x),
        l126_351(x),
        l126_352(x),
        l126_353(x),
        l126_354(x),
        l126_355(x),
        l126_356(x),
        l126_357(x),
        l126_358(x),
        l126_359(x),
        l126_360(x),
        l126_361(x),
        l126_362(x),
        l126_363(x),
        l126_364(x),
        l126_365(x),
        l126_366(x),
        l126_367(x),
        l126_368(x),
        l126_369(x),
        l126_370(x),
        l126_371(x),
        l126_372(x),
        l126_373(x),
        l126_374(x),
    ]