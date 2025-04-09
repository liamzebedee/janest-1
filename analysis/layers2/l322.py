import numpy as np




# Generated from reverse engineering
def l322_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 319
    out = np.empty(319, dtype=np.float32)
    
    # for i in range(0, 97):
    for i in range(0, 97):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(97, 128):
    for i in range(0, 31):
        s = x[96 + i] + x[129 + i]
        s += biases[i]
        out[97 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 159):
    for i in range(0, 31):
        s = x[97 + i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(159, 190):
    for i in range(0, 31):
        s = x[128 + i] + x[129 + i]
        s += biases[i]
        out[159 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(190, 191):
    for i in range(0, 1):
        s = x[128 + i]
        out[190 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(191, 319):
    for i in range(0, 128):
        s = x[128 + i]
        out[191 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l322_0(x):
    # x is a list (or vector) of length 256
    return max(0, x[0])
def l322_1(x):
    # x is a list (or vector) of length 256
    return max(0, x[1])
def l322_2(x):
    # x is a list (or vector) of length 256
    return max(0, x[2])
def l322_3(x):
    # x is a list (or vector) of length 256
    return max(0, x[3])
def l322_4(x):
    # x is a list (or vector) of length 256
    return max(0, x[4])
def l322_5(x):
    # x is a list (or vector) of length 256
    return max(0, x[5])
def l322_6(x):
    # x is a list (or vector) of length 256
    return max(0, x[6])
def l322_7(x):
    # x is a list (or vector) of length 256
    return max(0, x[7])
def l322_8(x):
    # x is a list (or vector) of length 256
    return max(0, x[8])
def l322_9(x):
    # x is a list (or vector) of length 256
    return max(0, x[9])
def l322_10(x):
    # x is a list (or vector) of length 256
    return max(0, x[10])
def l322_11(x):
    # x is a list (or vector) of length 256
    return max(0, x[11])
def l322_12(x):
    # x is a list (or vector) of length 256
    return max(0, x[12])
def l322_13(x):
    # x is a list (or vector) of length 256
    return max(0, x[13])
def l322_14(x):
    # x is a list (or vector) of length 256
    return max(0, x[14])
def l322_15(x):
    # x is a list (or vector) of length 256
    return max(0, x[15])
def l322_16(x):
    # x is a list (or vector) of length 256
    return max(0, x[16])
def l322_17(x):
    # x is a list (or vector) of length 256
    return max(0, x[17])
def l322_18(x):
    # x is a list (or vector) of length 256
    return max(0, x[18])
def l322_19(x):
    # x is a list (or vector) of length 256
    return max(0, x[19])
def l322_20(x):
    # x is a list (or vector) of length 256
    return max(0, x[20])
def l322_21(x):
    # x is a list (or vector) of length 256
    return max(0, x[21])
def l322_22(x):
    # x is a list (or vector) of length 256
    return max(0, x[22])
def l322_23(x):
    # x is a list (or vector) of length 256
    return max(0, x[23])
def l322_24(x):
    # x is a list (or vector) of length 256
    return max(0, x[24])
def l322_25(x):
    # x is a list (or vector) of length 256
    return max(0, x[25])
def l322_26(x):
    # x is a list (or vector) of length 256
    return max(0, x[26])
def l322_27(x):
    # x is a list (or vector) of length 256
    return max(0, x[27])
def l322_28(x):
    # x is a list (or vector) of length 256
    return max(0, x[28])
def l322_29(x):
    # x is a list (or vector) of length 256
    return max(0, x[29])
def l322_30(x):
    # x is a list (or vector) of length 256
    return max(0, x[30])
def l322_31(x):
    # x is a list (or vector) of length 256
    return max(0, x[31])
def l322_32(x):
    # x is a list (or vector) of length 256
    return max(0, x[32])
def l322_33(x):
    # x is a list (or vector) of length 256
    return max(0, x[33])
def l322_34(x):
    # x is a list (or vector) of length 256
    return max(0, x[34])
def l322_35(x):
    # x is a list (or vector) of length 256
    return max(0, x[35])
def l322_36(x):
    # x is a list (or vector) of length 256
    return max(0, x[36])
def l322_37(x):
    # x is a list (or vector) of length 256
    return max(0, x[37])
def l322_38(x):
    # x is a list (or vector) of length 256
    return max(0, x[38])
def l322_39(x):
    # x is a list (or vector) of length 256
    return max(0, x[39])
def l322_40(x):
    # x is a list (or vector) of length 256
    return max(0, x[40])
def l322_41(x):
    # x is a list (or vector) of length 256
    return max(0, x[41])
def l322_42(x):
    # x is a list (or vector) of length 256
    return max(0, x[42])
def l322_43(x):
    # x is a list (or vector) of length 256
    return max(0, x[43])
def l322_44(x):
    # x is a list (or vector) of length 256
    return max(0, x[44])
def l322_45(x):
    # x is a list (or vector) of length 256
    return max(0, x[45])
def l322_46(x):
    # x is a list (or vector) of length 256
    return max(0, x[46])
def l322_47(x):
    # x is a list (or vector) of length 256
    return max(0, x[47])
def l322_48(x):
    # x is a list (or vector) of length 256
    return max(0, x[48])
def l322_49(x):
    # x is a list (or vector) of length 256
    return max(0, x[49])
def l322_50(x):
    # x is a list (or vector) of length 256
    return max(0, x[50])
def l322_51(x):
    # x is a list (or vector) of length 256
    return max(0, x[51])
def l322_52(x):
    # x is a list (or vector) of length 256
    return max(0, x[52])
def l322_53(x):
    # x is a list (or vector) of length 256
    return max(0, x[53])
def l322_54(x):
    # x is a list (or vector) of length 256
    return max(0, x[54])
def l322_55(x):
    # x is a list (or vector) of length 256
    return max(0, x[55])
def l322_56(x):
    # x is a list (or vector) of length 256
    return max(0, x[56])
def l322_57(x):
    # x is a list (or vector) of length 256
    return max(0, x[57])
def l322_58(x):
    # x is a list (or vector) of length 256
    return max(0, x[58])
def l322_59(x):
    # x is a list (or vector) of length 256
    return max(0, x[59])
def l322_60(x):
    # x is a list (or vector) of length 256
    return max(0, x[60])
def l322_61(x):
    # x is a list (or vector) of length 256
    return max(0, x[61])
def l322_62(x):
    # x is a list (or vector) of length 256
    return max(0, x[62])
def l322_63(x):
    # x is a list (or vector) of length 256
    return max(0, x[63])
def l322_64(x):
    # x is a list (or vector) of length 256
    return max(0, x[64])
def l322_65(x):
    # x is a list (or vector) of length 256
    return max(0, x[65])
def l322_66(x):
    # x is a list (or vector) of length 256
    return max(0, x[66])
def l322_67(x):
    # x is a list (or vector) of length 256
    return max(0, x[67])
def l322_68(x):
    # x is a list (or vector) of length 256
    return max(0, x[68])
def l322_69(x):
    # x is a list (or vector) of length 256
    return max(0, x[69])
def l322_70(x):
    # x is a list (or vector) of length 256
    return max(0, x[70])
def l322_71(x):
    # x is a list (or vector) of length 256
    return max(0, x[71])
def l322_72(x):
    # x is a list (or vector) of length 256
    return max(0, x[72])
def l322_73(x):
    # x is a list (or vector) of length 256
    return max(0, x[73])
def l322_74(x):
    # x is a list (or vector) of length 256
    return max(0, x[74])
def l322_75(x):
    # x is a list (or vector) of length 256
    return max(0, x[75])
def l322_76(x):
    # x is a list (or vector) of length 256
    return max(0, x[76])
def l322_77(x):
    # x is a list (or vector) of length 256
    return max(0, x[77])
def l322_78(x):
    # x is a list (or vector) of length 256
    return max(0, x[78])
def l322_79(x):
    # x is a list (or vector) of length 256
    return max(0, x[79])
def l322_80(x):
    # x is a list (or vector) of length 256
    return max(0, x[80])
def l322_81(x):
    # x is a list (or vector) of length 256
    return max(0, x[81])
def l322_82(x):
    # x is a list (or vector) of length 256
    return max(0, x[82])
def l322_83(x):
    # x is a list (or vector) of length 256
    return max(0, x[83])
def l322_84(x):
    # x is a list (or vector) of length 256
    return max(0, x[84])
def l322_85(x):
    # x is a list (or vector) of length 256
    return max(0, x[85])
def l322_86(x):
    # x is a list (or vector) of length 256
    return max(0, x[86])
def l322_87(x):
    # x is a list (or vector) of length 256
    return max(0, x[87])
def l322_88(x):
    # x is a list (or vector) of length 256
    return max(0, x[88])
def l322_89(x):
    # x is a list (or vector) of length 256
    return max(0, x[89])
def l322_90(x):
    # x is a list (or vector) of length 256
    return max(0, x[90])
def l322_91(x):
    # x is a list (or vector) of length 256
    return max(0, x[91])
def l322_92(x):
    # x is a list (or vector) of length 256
    return max(0, x[92])
def l322_93(x):
    # x is a list (or vector) of length 256
    return max(0, x[93])
def l322_94(x):
    # x is a list (or vector) of length 256
    return max(0, x[94])
def l322_95(x):
    # x is a list (or vector) of length 256
    return max(0, x[95])
def l322_96(x):
    # x is a list (or vector) of length 256
    return max(0, x[96])
def l322_97(x):
    # x is a list (or vector) of length 256
    return max(0, x[96] + x[129] + -1.0)
def l322_98(x):
    # x is a list (or vector) of length 256
    return max(0, x[97] + x[130] + -1.0)
def l322_99(x):
    # x is a list (or vector) of length 256
    return max(0, x[98] + x[131] + -1.0)
def l322_100(x):
    # x is a list (or vector) of length 256
    return max(0, x[99] + x[132] + -1.0)
def l322_101(x):
    # x is a list (or vector) of length 256
    return max(0, x[100] + x[133] + -1.0)
def l322_102(x):
    # x is a list (or vector) of length 256
    return max(0, x[101] + x[134] + -1.0)
def l322_103(x):
    # x is a list (or vector) of length 256
    return max(0, x[102] + x[135] + -1.0)
def l322_104(x):
    # x is a list (or vector) of length 256
    return max(0, x[103] + x[136] + -1.0)
def l322_105(x):
    # x is a list (or vector) of length 256
    return max(0, x[104] + x[137] + -1.0)
def l322_106(x):
    # x is a list (or vector) of length 256
    return max(0, x[105] + x[138] + -1.0)
def l322_107(x):
    # x is a list (or vector) of length 256
    return max(0, x[106] + x[139] + -1.0)
def l322_108(x):
    # x is a list (or vector) of length 256
    return max(0, x[107] + x[140] + -1.0)
def l322_109(x):
    # x is a list (or vector) of length 256
    return max(0, x[108] + x[141] + -1.0)
def l322_110(x):
    # x is a list (or vector) of length 256
    return max(0, x[109] + x[142] + -1.0)
def l322_111(x):
    # x is a list (or vector) of length 256
    return max(0, x[110] + x[143] + -1.0)
def l322_112(x):
    # x is a list (or vector) of length 256
    return max(0, x[111] + x[144] + -1.0)
def l322_113(x):
    # x is a list (or vector) of length 256
    return max(0, x[112] + x[145] + -1.0)
def l322_114(x):
    # x is a list (or vector) of length 256
    return max(0, x[113] + x[146] + -1.0)
def l322_115(x):
    # x is a list (or vector) of length 256
    return max(0, x[114] + x[147] + -1.0)
def l322_116(x):
    # x is a list (or vector) of length 256
    return max(0, x[115] + x[148] + -1.0)
def l322_117(x):
    # x is a list (or vector) of length 256
    return max(0, x[116] + x[149] + -1.0)
def l322_118(x):
    # x is a list (or vector) of length 256
    return max(0, x[117] + x[150] + -1.0)
def l322_119(x):
    # x is a list (or vector) of length 256
    return max(0, x[118] + x[151] + -1.0)
def l322_120(x):
    # x is a list (or vector) of length 256
    return max(0, x[119] + x[152] + -1.0)
def l322_121(x):
    # x is a list (or vector) of length 256
    return max(0, x[120] + x[153] + -1.0)
def l322_122(x):
    # x is a list (or vector) of length 256
    return max(0, x[121] + x[154] + -1.0)
def l322_123(x):
    # x is a list (or vector) of length 256
    return max(0, x[122] + x[155] + -1.0)
def l322_124(x):
    # x is a list (or vector) of length 256
    return max(0, x[123] + x[156] + -1.0)
def l322_125(x):
    # x is a list (or vector) of length 256
    return max(0, x[124] + x[157] + -1.0)
def l322_126(x):
    # x is a list (or vector) of length 256
    return max(0, x[125] + x[158] + -1.0)
def l322_127(x):
    # x is a list (or vector) of length 256
    return max(0, x[126] + x[159] + -1.0)
def l322_128(x):
    # x is a list (or vector) of length 256
    return max(0, x[97])
def l322_129(x):
    # x is a list (or vector) of length 256
    return max(0, x[98])
def l322_130(x):
    # x is a list (or vector) of length 256
    return max(0, x[99])
def l322_131(x):
    # x is a list (or vector) of length 256
    return max(0, x[100])
def l322_132(x):
    # x is a list (or vector) of length 256
    return max(0, x[101])
def l322_133(x):
    # x is a list (or vector) of length 256
    return max(0, x[102])
def l322_134(x):
    # x is a list (or vector) of length 256
    return max(0, x[103])
def l322_135(x):
    # x is a list (or vector) of length 256
    return max(0, x[104])
def l322_136(x):
    # x is a list (or vector) of length 256
    return max(0, x[105])
def l322_137(x):
    # x is a list (or vector) of length 256
    return max(0, x[106])
def l322_138(x):
    # x is a list (or vector) of length 256
    return max(0, x[107])
def l322_139(x):
    # x is a list (or vector) of length 256
    return max(0, x[108])
def l322_140(x):
    # x is a list (or vector) of length 256
    return max(0, x[109])
def l322_141(x):
    # x is a list (or vector) of length 256
    return max(0, x[110])
def l322_142(x):
    # x is a list (or vector) of length 256
    return max(0, x[111])
def l322_143(x):
    # x is a list (or vector) of length 256
    return max(0, x[112])
def l322_144(x):
    # x is a list (or vector) of length 256
    return max(0, x[113])
def l322_145(x):
    # x is a list (or vector) of length 256
    return max(0, x[114])
def l322_146(x):
    # x is a list (or vector) of length 256
    return max(0, x[115])
def l322_147(x):
    # x is a list (or vector) of length 256
    return max(0, x[116])
def l322_148(x):
    # x is a list (or vector) of length 256
    return max(0, x[117])
def l322_149(x):
    # x is a list (or vector) of length 256
    return max(0, x[118])
def l322_150(x):
    # x is a list (or vector) of length 256
    return max(0, x[119])
def l322_151(x):
    # x is a list (or vector) of length 256
    return max(0, x[120])
def l322_152(x):
    # x is a list (or vector) of length 256
    return max(0, x[121])
def l322_153(x):
    # x is a list (or vector) of length 256
    return max(0, x[122])
def l322_154(x):
    # x is a list (or vector) of length 256
    return max(0, x[123])
def l322_155(x):
    # x is a list (or vector) of length 256
    return max(0, x[124])
def l322_156(x):
    # x is a list (or vector) of length 256
    return max(0, x[125])
def l322_157(x):
    # x is a list (or vector) of length 256
    return max(0, x[126])
def l322_158(x):
    # x is a list (or vector) of length 256
    return max(0, x[127])
def l322_159(x):
    # x is a list (or vector) of length 256
    return max(0, x[128] + x[129] + -1.0)
def l322_160(x):
    # x is a list (or vector) of length 256
    return max(0, x[129] + x[130] + -1.0)
def l322_161(x):
    # x is a list (or vector) of length 256
    return max(0, x[130] + x[131] + -1.0)
def l322_162(x):
    # x is a list (or vector) of length 256
    return max(0, x[131] + x[132] + -1.0)
def l322_163(x):
    # x is a list (or vector) of length 256
    return max(0, x[132] + x[133] + -1.0)
def l322_164(x):
    # x is a list (or vector) of length 256
    return max(0, x[133] + x[134] + -1.0)
def l322_165(x):
    # x is a list (or vector) of length 256
    return max(0, x[134] + x[135] + -1.0)
def l322_166(x):
    # x is a list (or vector) of length 256
    return max(0, x[135] + x[136] + -1.0)
def l322_167(x):
    # x is a list (or vector) of length 256
    return max(0, x[136] + x[137] + -1.0)
def l322_168(x):
    # x is a list (or vector) of length 256
    return max(0, x[137] + x[138] + -1.0)
def l322_169(x):
    # x is a list (or vector) of length 256
    return max(0, x[138] + x[139] + -1.0)
def l322_170(x):
    # x is a list (or vector) of length 256
    return max(0, x[139] + x[140] + -1.0)
def l322_171(x):
    # x is a list (or vector) of length 256
    return max(0, x[140] + x[141] + -1.0)
def l322_172(x):
    # x is a list (or vector) of length 256
    return max(0, x[141] + x[142] + -1.0)
def l322_173(x):
    # x is a list (or vector) of length 256
    return max(0, x[142] + x[143] + -1.0)
def l322_174(x):
    # x is a list (or vector) of length 256
    return max(0, x[143] + x[144] + -1.0)
def l322_175(x):
    # x is a list (or vector) of length 256
    return max(0, x[144] + x[145] + -1.0)
def l322_176(x):
    # x is a list (or vector) of length 256
    return max(0, x[145] + x[146] + -1.0)
def l322_177(x):
    # x is a list (or vector) of length 256
    return max(0, x[146] + x[147] + -1.0)
def l322_178(x):
    # x is a list (or vector) of length 256
    return max(0, x[147] + x[148] + -1.0)
def l322_179(x):
    # x is a list (or vector) of length 256
    return max(0, x[148] + x[149] + -1.0)
def l322_180(x):
    # x is a list (or vector) of length 256
    return max(0, x[149] + x[150] + -1.0)
def l322_181(x):
    # x is a list (or vector) of length 256
    return max(0, x[150] + x[151] + -1.0)
def l322_182(x):
    # x is a list (or vector) of length 256
    return max(0, x[151] + x[152] + -1.0)
def l322_183(x):
    # x is a list (or vector) of length 256
    return max(0, x[152] + x[153] + -1.0)
def l322_184(x):
    # x is a list (or vector) of length 256
    return max(0, x[153] + x[154] + -1.0)
def l322_185(x):
    # x is a list (or vector) of length 256
    return max(0, x[154] + x[155] + -1.0)
def l322_186(x):
    # x is a list (or vector) of length 256
    return max(0, x[155] + x[156] + -1.0)
def l322_187(x):
    # x is a list (or vector) of length 256
    return max(0, x[156] + x[157] + -1.0)
def l322_188(x):
    # x is a list (or vector) of length 256
    return max(0, x[157] + x[158] + -1.0)
def l322_189(x):
    # x is a list (or vector) of length 256
    return max(0, x[158] + x[159] + -1.0)
def l322_190(x):
    # x is a list (or vector) of length 256
    return max(0, x[128])
def l322_191(x):
    # x is a list (or vector) of length 256
    return max(0, x[128])
def l322_192(x):
    # x is a list (or vector) of length 256
    return max(0, x[129])
def l322_193(x):
    # x is a list (or vector) of length 256
    return max(0, x[130])
def l322_194(x):
    # x is a list (or vector) of length 256
    return max(0, x[131])
def l322_195(x):
    # x is a list (or vector) of length 256
    return max(0, x[132])
def l322_196(x):
    # x is a list (or vector) of length 256
    return max(0, x[133])
def l322_197(x):
    # x is a list (or vector) of length 256
    return max(0, x[134])
def l322_198(x):
    # x is a list (or vector) of length 256
    return max(0, x[135])
def l322_199(x):
    # x is a list (or vector) of length 256
    return max(0, x[136])
def l322_200(x):
    # x is a list (or vector) of length 256
    return max(0, x[137])
def l322_201(x):
    # x is a list (or vector) of length 256
    return max(0, x[138])
def l322_202(x):
    # x is a list (or vector) of length 256
    return max(0, x[139])
def l322_203(x):
    # x is a list (or vector) of length 256
    return max(0, x[140])
def l322_204(x):
    # x is a list (or vector) of length 256
    return max(0, x[141])
def l322_205(x):
    # x is a list (or vector) of length 256
    return max(0, x[142])
def l322_206(x):
    # x is a list (or vector) of length 256
    return max(0, x[143])
def l322_207(x):
    # x is a list (or vector) of length 256
    return max(0, x[144])
def l322_208(x):
    # x is a list (or vector) of length 256
    return max(0, x[145])
def l322_209(x):
    # x is a list (or vector) of length 256
    return max(0, x[146])
def l322_210(x):
    # x is a list (or vector) of length 256
    return max(0, x[147])
def l322_211(x):
    # x is a list (or vector) of length 256
    return max(0, x[148])
def l322_212(x):
    # x is a list (or vector) of length 256
    return max(0, x[149])
def l322_213(x):
    # x is a list (or vector) of length 256
    return max(0, x[150])
def l322_214(x):
    # x is a list (or vector) of length 256
    return max(0, x[151])
def l322_215(x):
    # x is a list (or vector) of length 256
    return max(0, x[152])
def l322_216(x):
    # x is a list (or vector) of length 256
    return max(0, x[153])
def l322_217(x):
    # x is a list (or vector) of length 256
    return max(0, x[154])
def l322_218(x):
    # x is a list (or vector) of length 256
    return max(0, x[155])
def l322_219(x):
    # x is a list (or vector) of length 256
    return max(0, x[156])
def l322_220(x):
    # x is a list (or vector) of length 256
    return max(0, x[157])
def l322_221(x):
    # x is a list (or vector) of length 256
    return max(0, x[158])
def l322_222(x):
    # x is a list (or vector) of length 256
    return max(0, x[159])
def l322_223(x):
    # x is a list (or vector) of length 256
    return max(0, x[160])
def l322_224(x):
    # x is a list (or vector) of length 256
    return max(0, x[161])
def l322_225(x):
    # x is a list (or vector) of length 256
    return max(0, x[162])
def l322_226(x):
    # x is a list (or vector) of length 256
    return max(0, x[163])
def l322_227(x):
    # x is a list (or vector) of length 256
    return max(0, x[164])
def l322_228(x):
    # x is a list (or vector) of length 256
    return max(0, x[165])
def l322_229(x):
    # x is a list (or vector) of length 256
    return max(0, x[166])
def l322_230(x):
    # x is a list (or vector) of length 256
    return max(0, x[167])
def l322_231(x):
    # x is a list (or vector) of length 256
    return max(0, x[168])
def l322_232(x):
    # x is a list (or vector) of length 256
    return max(0, x[169])
def l322_233(x):
    # x is a list (or vector) of length 256
    return max(0, x[170])
def l322_234(x):
    # x is a list (or vector) of length 256
    return max(0, x[171])
def l322_235(x):
    # x is a list (or vector) of length 256
    return max(0, x[172])
def l322_236(x):
    # x is a list (or vector) of length 256
    return max(0, x[173])
def l322_237(x):
    # x is a list (or vector) of length 256
    return max(0, x[174])
def l322_238(x):
    # x is a list (or vector) of length 256
    return max(0, x[175])
def l322_239(x):
    # x is a list (or vector) of length 256
    return max(0, x[176])
def l322_240(x):
    # x is a list (or vector) of length 256
    return max(0, x[177])
def l322_241(x):
    # x is a list (or vector) of length 256
    return max(0, x[178])
def l322_242(x):
    # x is a list (or vector) of length 256
    return max(0, x[179])
def l322_243(x):
    # x is a list (or vector) of length 256
    return max(0, x[180])
def l322_244(x):
    # x is a list (or vector) of length 256
    return max(0, x[181])
def l322_245(x):
    # x is a list (or vector) of length 256
    return max(0, x[182])
def l322_246(x):
    # x is a list (or vector) of length 256
    return max(0, x[183])
def l322_247(x):
    # x is a list (or vector) of length 256
    return max(0, x[184])
def l322_248(x):
    # x is a list (or vector) of length 256
    return max(0, x[185])
def l322_249(x):
    # x is a list (or vector) of length 256
    return max(0, x[186])
def l322_250(x):
    # x is a list (or vector) of length 256
    return max(0, x[187])
def l322_251(x):
    # x is a list (or vector) of length 256
    return max(0, x[188])
def l322_252(x):
    # x is a list (or vector) of length 256
    return max(0, x[189])
def l322_253(x):
    # x is a list (or vector) of length 256
    return max(0, x[190])
def l322_254(x):
    # x is a list (or vector) of length 256
    return max(0, x[191])
def l322_255(x):
    # x is a list (or vector) of length 256
    return max(0, x[192])
def l322_256(x):
    # x is a list (or vector) of length 256
    return max(0, x[193])
def l322_257(x):
    # x is a list (or vector) of length 256
    return max(0, x[194])
def l322_258(x):
    # x is a list (or vector) of length 256
    return max(0, x[195])
def l322_259(x):
    # x is a list (or vector) of length 256
    return max(0, x[196])
def l322_260(x):
    # x is a list (or vector) of length 256
    return max(0, x[197])
def l322_261(x):
    # x is a list (or vector) of length 256
    return max(0, x[198])
def l322_262(x):
    # x is a list (or vector) of length 256
    return max(0, x[199])
def l322_263(x):
    # x is a list (or vector) of length 256
    return max(0, x[200])
def l322_264(x):
    # x is a list (or vector) of length 256
    return max(0, x[201])
def l322_265(x):
    # x is a list (or vector) of length 256
    return max(0, x[202])
def l322_266(x):
    # x is a list (or vector) of length 256
    return max(0, x[203])
def l322_267(x):
    # x is a list (or vector) of length 256
    return max(0, x[204])
def l322_268(x):
    # x is a list (or vector) of length 256
    return max(0, x[205])
def l322_269(x):
    # x is a list (or vector) of length 256
    return max(0, x[206])
def l322_270(x):
    # x is a list (or vector) of length 256
    return max(0, x[207])
def l322_271(x):
    # x is a list (or vector) of length 256
    return max(0, x[208])
def l322_272(x):
    # x is a list (or vector) of length 256
    return max(0, x[209])
def l322_273(x):
    # x is a list (or vector) of length 256
    return max(0, x[210])
def l322_274(x):
    # x is a list (or vector) of length 256
    return max(0, x[211])
def l322_275(x):
    # x is a list (or vector) of length 256
    return max(0, x[212])
def l322_276(x):
    # x is a list (or vector) of length 256
    return max(0, x[213])
def l322_277(x):
    # x is a list (or vector) of length 256
    return max(0, x[214])
def l322_278(x):
    # x is a list (or vector) of length 256
    return max(0, x[215])
def l322_279(x):
    # x is a list (or vector) of length 256
    return max(0, x[216])
def l322_280(x):
    # x is a list (or vector) of length 256
    return max(0, x[217])
def l322_281(x):
    # x is a list (or vector) of length 256
    return max(0, x[218])
def l322_282(x):
    # x is a list (or vector) of length 256
    return max(0, x[219])
def l322_283(x):
    # x is a list (or vector) of length 256
    return max(0, x[220])
def l322_284(x):
    # x is a list (or vector) of length 256
    return max(0, x[221])
def l322_285(x):
    # x is a list (or vector) of length 256
    return max(0, x[222])
def l322_286(x):
    # x is a list (or vector) of length 256
    return max(0, x[223])
def l322_287(x):
    # x is a list (or vector) of length 256
    return max(0, x[224])
def l322_288(x):
    # x is a list (or vector) of length 256
    return max(0, x[225])
def l322_289(x):
    # x is a list (or vector) of length 256
    return max(0, x[226])
def l322_290(x):
    # x is a list (or vector) of length 256
    return max(0, x[227])
def l322_291(x):
    # x is a list (or vector) of length 256
    return max(0, x[228])
def l322_292(x):
    # x is a list (or vector) of length 256
    return max(0, x[229])
def l322_293(x):
    # x is a list (or vector) of length 256
    return max(0, x[230])
def l322_294(x):
    # x is a list (or vector) of length 256
    return max(0, x[231])
def l322_295(x):
    # x is a list (or vector) of length 256
    return max(0, x[232])
def l322_296(x):
    # x is a list (or vector) of length 256
    return max(0, x[233])
def l322_297(x):
    # x is a list (or vector) of length 256
    return max(0, x[234])
def l322_298(x):
    # x is a list (or vector) of length 256
    return max(0, x[235])
def l322_299(x):
    # x is a list (or vector) of length 256
    return max(0, x[236])
def l322_300(x):
    # x is a list (or vector) of length 256
    return max(0, x[237])
def l322_301(x):
    # x is a list (or vector) of length 256
    return max(0, x[238])
def l322_302(x):
    # x is a list (or vector) of length 256
    return max(0, x[239])
def l322_303(x):
    # x is a list (or vector) of length 256
    return max(0, x[240])
def l322_304(x):
    # x is a list (or vector) of length 256
    return max(0, x[241])
def l322_305(x):
    # x is a list (or vector) of length 256
    return max(0, x[242])
def l322_306(x):
    # x is a list (or vector) of length 256
    return max(0, x[243])
def l322_307(x):
    # x is a list (or vector) of length 256
    return max(0, x[244])
def l322_308(x):
    # x is a list (or vector) of length 256
    return max(0, x[245])
def l322_309(x):
    # x is a list (or vector) of length 256
    return max(0, x[246])
def l322_310(x):
    # x is a list (or vector) of length 256
    return max(0, x[247])
def l322_311(x):
    # x is a list (or vector) of length 256
    return max(0, x[248])
def l322_312(x):
    # x is a list (or vector) of length 256
    return max(0, x[249])
def l322_313(x):
    # x is a list (or vector) of length 256
    return max(0, x[250])
def l322_314(x):
    # x is a list (or vector) of length 256
    return max(0, x[251])
def l322_315(x):
    # x is a list (or vector) of length 256
    return max(0, x[252])
def l322_316(x):
    # x is a list (or vector) of length 256
    return max(0, x[253])
def l322_317(x):
    # x is a list (or vector) of length 256
    return max(0, x[254])
def l322_318(x):
    # x is a list (or vector) of length 256
    return max(0, x[255])
def l322_(x):
    # x is a list (or vector) of length 256
    return [
        l322_0(x),
        l322_1(x),
        l322_2(x),
        l322_3(x),
        l322_4(x),
        l322_5(x),
        l322_6(x),
        l322_7(x),
        l322_8(x),
        l322_9(x),
        l322_10(x),
        l322_11(x),
        l322_12(x),
        l322_13(x),
        l322_14(x),
        l322_15(x),
        l322_16(x),
        l322_17(x),
        l322_18(x),
        l322_19(x),
        l322_20(x),
        l322_21(x),
        l322_22(x),
        l322_23(x),
        l322_24(x),
        l322_25(x),
        l322_26(x),
        l322_27(x),
        l322_28(x),
        l322_29(x),
        l322_30(x),
        l322_31(x),
        l322_32(x),
        l322_33(x),
        l322_34(x),
        l322_35(x),
        l322_36(x),
        l322_37(x),
        l322_38(x),
        l322_39(x),
        l322_40(x),
        l322_41(x),
        l322_42(x),
        l322_43(x),
        l322_44(x),
        l322_45(x),
        l322_46(x),
        l322_47(x),
        l322_48(x),
        l322_49(x),
        l322_50(x),
        l322_51(x),
        l322_52(x),
        l322_53(x),
        l322_54(x),
        l322_55(x),
        l322_56(x),
        l322_57(x),
        l322_58(x),
        l322_59(x),
        l322_60(x),
        l322_61(x),
        l322_62(x),
        l322_63(x),
        l322_64(x),
        l322_65(x),
        l322_66(x),
        l322_67(x),
        l322_68(x),
        l322_69(x),
        l322_70(x),
        l322_71(x),
        l322_72(x),
        l322_73(x),
        l322_74(x),
        l322_75(x),
        l322_76(x),
        l322_77(x),
        l322_78(x),
        l322_79(x),
        l322_80(x),
        l322_81(x),
        l322_82(x),
        l322_83(x),
        l322_84(x),
        l322_85(x),
        l322_86(x),
        l322_87(x),
        l322_88(x),
        l322_89(x),
        l322_90(x),
        l322_91(x),
        l322_92(x),
        l322_93(x),
        l322_94(x),
        l322_95(x),
        l322_96(x),
        l322_97(x),
        l322_98(x),
        l322_99(x),
        l322_100(x),
        l322_101(x),
        l322_102(x),
        l322_103(x),
        l322_104(x),
        l322_105(x),
        l322_106(x),
        l322_107(x),
        l322_108(x),
        l322_109(x),
        l322_110(x),
        l322_111(x),
        l322_112(x),
        l322_113(x),
        l322_114(x),
        l322_115(x),
        l322_116(x),
        l322_117(x),
        l322_118(x),
        l322_119(x),
        l322_120(x),
        l322_121(x),
        l322_122(x),
        l322_123(x),
        l322_124(x),
        l322_125(x),
        l322_126(x),
        l322_127(x),
        l322_128(x),
        l322_129(x),
        l322_130(x),
        l322_131(x),
        l322_132(x),
        l322_133(x),
        l322_134(x),
        l322_135(x),
        l322_136(x),
        l322_137(x),
        l322_138(x),
        l322_139(x),
        l322_140(x),
        l322_141(x),
        l322_142(x),
        l322_143(x),
        l322_144(x),
        l322_145(x),
        l322_146(x),
        l322_147(x),
        l322_148(x),
        l322_149(x),
        l322_150(x),
        l322_151(x),
        l322_152(x),
        l322_153(x),
        l322_154(x),
        l322_155(x),
        l322_156(x),
        l322_157(x),
        l322_158(x),
        l322_159(x),
        l322_160(x),
        l322_161(x),
        l322_162(x),
        l322_163(x),
        l322_164(x),
        l322_165(x),
        l322_166(x),
        l322_167(x),
        l322_168(x),
        l322_169(x),
        l322_170(x),
        l322_171(x),
        l322_172(x),
        l322_173(x),
        l322_174(x),
        l322_175(x),
        l322_176(x),
        l322_177(x),
        l322_178(x),
        l322_179(x),
        l322_180(x),
        l322_181(x),
        l322_182(x),
        l322_183(x),
        l322_184(x),
        l322_185(x),
        l322_186(x),
        l322_187(x),
        l322_188(x),
        l322_189(x),
        l322_190(x),
        l322_191(x),
        l322_192(x),
        l322_193(x),
        l322_194(x),
        l322_195(x),
        l322_196(x),
        l322_197(x),
        l322_198(x),
        l322_199(x),
        l322_200(x),
        l322_201(x),
        l322_202(x),
        l322_203(x),
        l322_204(x),
        l322_205(x),
        l322_206(x),
        l322_207(x),
        l322_208(x),
        l322_209(x),
        l322_210(x),
        l322_211(x),
        l322_212(x),
        l322_213(x),
        l322_214(x),
        l322_215(x),
        l322_216(x),
        l322_217(x),
        l322_218(x),
        l322_219(x),
        l322_220(x),
        l322_221(x),
        l322_222(x),
        l322_223(x),
        l322_224(x),
        l322_225(x),
        l322_226(x),
        l322_227(x),
        l322_228(x),
        l322_229(x),
        l322_230(x),
        l322_231(x),
        l322_232(x),
        l322_233(x),
        l322_234(x),
        l322_235(x),
        l322_236(x),
        l322_237(x),
        l322_238(x),
        l322_239(x),
        l322_240(x),
        l322_241(x),
        l322_242(x),
        l322_243(x),
        l322_244(x),
        l322_245(x),
        l322_246(x),
        l322_247(x),
        l322_248(x),
        l322_249(x),
        l322_250(x),
        l322_251(x),
        l322_252(x),
        l322_253(x),
        l322_254(x),
        l322_255(x),
        l322_256(x),
        l322_257(x),
        l322_258(x),
        l322_259(x),
        l322_260(x),
        l322_261(x),
        l322_262(x),
        l322_263(x),
        l322_264(x),
        l322_265(x),
        l322_266(x),
        l322_267(x),
        l322_268(x),
        l322_269(x),
        l322_270(x),
        l322_271(x),
        l322_272(x),
        l322_273(x),
        l322_274(x),
        l322_275(x),
        l322_276(x),
        l322_277(x),
        l322_278(x),
        l322_279(x),
        l322_280(x),
        l322_281(x),
        l322_282(x),
        l322_283(x),
        l322_284(x),
        l322_285(x),
        l322_286(x),
        l322_287(x),
        l322_288(x),
        l322_289(x),
        l322_290(x),
        l322_291(x),
        l322_292(x),
        l322_293(x),
        l322_294(x),
        l322_295(x),
        l322_296(x),
        l322_297(x),
        l322_298(x),
        l322_299(x),
        l322_300(x),
        l322_301(x),
        l322_302(x),
        l322_303(x),
        l322_304(x),
        l322_305(x),
        l322_306(x),
        l322_307(x),
        l322_308(x),
        l322_309(x),
        l322_310(x),
        l322_311(x),
        l322_312(x),
        l322_313(x),
        l322_314(x),
        l322_315(x),
        l322_316(x),
        l322_317(x),
        l322_318(x),
    ]