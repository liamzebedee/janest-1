import numpy as np




# Generated from reverse engineering
def l406_g(x: np.ndarray) -> np.ndarray:
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




def l406_0(x):
    # x is a list (or vector) of length 256
    return max(0, x[0])
def l406_1(x):
    # x is a list (or vector) of length 256
    return max(0, x[1])
def l406_2(x):
    # x is a list (or vector) of length 256
    return max(0, x[2])
def l406_3(x):
    # x is a list (or vector) of length 256
    return max(0, x[3])
def l406_4(x):
    # x is a list (or vector) of length 256
    return max(0, x[4])
def l406_5(x):
    # x is a list (or vector) of length 256
    return max(0, x[5])
def l406_6(x):
    # x is a list (or vector) of length 256
    return max(0, x[6])
def l406_7(x):
    # x is a list (or vector) of length 256
    return max(0, x[7])
def l406_8(x):
    # x is a list (or vector) of length 256
    return max(0, x[8])
def l406_9(x):
    # x is a list (or vector) of length 256
    return max(0, x[9])
def l406_10(x):
    # x is a list (or vector) of length 256
    return max(0, x[10])
def l406_11(x):
    # x is a list (or vector) of length 256
    return max(0, x[11])
def l406_12(x):
    # x is a list (or vector) of length 256
    return max(0, x[12])
def l406_13(x):
    # x is a list (or vector) of length 256
    return max(0, x[13])
def l406_14(x):
    # x is a list (or vector) of length 256
    return max(0, x[14])
def l406_15(x):
    # x is a list (or vector) of length 256
    return max(0, x[15])
def l406_16(x):
    # x is a list (or vector) of length 256
    return max(0, x[16])
def l406_17(x):
    # x is a list (or vector) of length 256
    return max(0, x[17])
def l406_18(x):
    # x is a list (or vector) of length 256
    return max(0, x[18])
def l406_19(x):
    # x is a list (or vector) of length 256
    return max(0, x[19])
def l406_20(x):
    # x is a list (or vector) of length 256
    return max(0, x[20])
def l406_21(x):
    # x is a list (or vector) of length 256
    return max(0, x[21])
def l406_22(x):
    # x is a list (or vector) of length 256
    return max(0, x[22])
def l406_23(x):
    # x is a list (or vector) of length 256
    return max(0, x[23])
def l406_24(x):
    # x is a list (or vector) of length 256
    return max(0, x[24])
def l406_25(x):
    # x is a list (or vector) of length 256
    return max(0, x[25])
def l406_26(x):
    # x is a list (or vector) of length 256
    return max(0, x[26])
def l406_27(x):
    # x is a list (or vector) of length 256
    return max(0, x[27])
def l406_28(x):
    # x is a list (or vector) of length 256
    return max(0, x[28])
def l406_29(x):
    # x is a list (or vector) of length 256
    return max(0, x[29])
def l406_30(x):
    # x is a list (or vector) of length 256
    return max(0, x[30])
def l406_31(x):
    # x is a list (or vector) of length 256
    return max(0, x[31])
def l406_32(x):
    # x is a list (or vector) of length 256
    return max(0, x[32])
def l406_33(x):
    # x is a list (or vector) of length 256
    return max(0, x[33])
def l406_34(x):
    # x is a list (or vector) of length 256
    return max(0, x[34])
def l406_35(x):
    # x is a list (or vector) of length 256
    return max(0, x[35])
def l406_36(x):
    # x is a list (or vector) of length 256
    return max(0, x[36])
def l406_37(x):
    # x is a list (or vector) of length 256
    return max(0, x[37])
def l406_38(x):
    # x is a list (or vector) of length 256
    return max(0, x[38])
def l406_39(x):
    # x is a list (or vector) of length 256
    return max(0, x[39])
def l406_40(x):
    # x is a list (or vector) of length 256
    return max(0, x[40])
def l406_41(x):
    # x is a list (or vector) of length 256
    return max(0, x[41])
def l406_42(x):
    # x is a list (or vector) of length 256
    return max(0, x[42])
def l406_43(x):
    # x is a list (or vector) of length 256
    return max(0, x[43])
def l406_44(x):
    # x is a list (or vector) of length 256
    return max(0, x[44])
def l406_45(x):
    # x is a list (or vector) of length 256
    return max(0, x[45])
def l406_46(x):
    # x is a list (or vector) of length 256
    return max(0, x[46])
def l406_47(x):
    # x is a list (or vector) of length 256
    return max(0, x[47])
def l406_48(x):
    # x is a list (or vector) of length 256
    return max(0, x[48])
def l406_49(x):
    # x is a list (or vector) of length 256
    return max(0, x[49])
def l406_50(x):
    # x is a list (or vector) of length 256
    return max(0, x[50])
def l406_51(x):
    # x is a list (or vector) of length 256
    return max(0, x[51])
def l406_52(x):
    # x is a list (or vector) of length 256
    return max(0, x[52])
def l406_53(x):
    # x is a list (or vector) of length 256
    return max(0, x[53])
def l406_54(x):
    # x is a list (or vector) of length 256
    return max(0, x[54])
def l406_55(x):
    # x is a list (or vector) of length 256
    return max(0, x[55])
def l406_56(x):
    # x is a list (or vector) of length 256
    return max(0, x[56])
def l406_57(x):
    # x is a list (or vector) of length 256
    return max(0, x[57])
def l406_58(x):
    # x is a list (or vector) of length 256
    return max(0, x[58])
def l406_59(x):
    # x is a list (or vector) of length 256
    return max(0, x[59])
def l406_60(x):
    # x is a list (or vector) of length 256
    return max(0, x[60])
def l406_61(x):
    # x is a list (or vector) of length 256
    return max(0, x[61])
def l406_62(x):
    # x is a list (or vector) of length 256
    return max(0, x[62])
def l406_63(x):
    # x is a list (or vector) of length 256
    return max(0, x[63])
def l406_64(x):
    # x is a list (or vector) of length 256
    return max(0, x[64])
def l406_65(x):
    # x is a list (or vector) of length 256
    return max(0, x[65])
def l406_66(x):
    # x is a list (or vector) of length 256
    return max(0, x[66])
def l406_67(x):
    # x is a list (or vector) of length 256
    return max(0, x[67])
def l406_68(x):
    # x is a list (or vector) of length 256
    return max(0, x[68])
def l406_69(x):
    # x is a list (or vector) of length 256
    return max(0, x[69])
def l406_70(x):
    # x is a list (or vector) of length 256
    return max(0, x[70])
def l406_71(x):
    # x is a list (or vector) of length 256
    return max(0, x[71])
def l406_72(x):
    # x is a list (or vector) of length 256
    return max(0, x[72])
def l406_73(x):
    # x is a list (or vector) of length 256
    return max(0, x[73])
def l406_74(x):
    # x is a list (or vector) of length 256
    return max(0, x[74])
def l406_75(x):
    # x is a list (or vector) of length 256
    return max(0, x[75])
def l406_76(x):
    # x is a list (or vector) of length 256
    return max(0, x[76])
def l406_77(x):
    # x is a list (or vector) of length 256
    return max(0, x[77])
def l406_78(x):
    # x is a list (or vector) of length 256
    return max(0, x[78])
def l406_79(x):
    # x is a list (or vector) of length 256
    return max(0, x[79])
def l406_80(x):
    # x is a list (or vector) of length 256
    return max(0, x[80])
def l406_81(x):
    # x is a list (or vector) of length 256
    return max(0, x[81])
def l406_82(x):
    # x is a list (or vector) of length 256
    return max(0, x[82])
def l406_83(x):
    # x is a list (or vector) of length 256
    return max(0, x[83])
def l406_84(x):
    # x is a list (or vector) of length 256
    return max(0, x[84])
def l406_85(x):
    # x is a list (or vector) of length 256
    return max(0, x[85])
def l406_86(x):
    # x is a list (or vector) of length 256
    return max(0, x[86])
def l406_87(x):
    # x is a list (or vector) of length 256
    return max(0, x[87])
def l406_88(x):
    # x is a list (or vector) of length 256
    return max(0, x[88])
def l406_89(x):
    # x is a list (or vector) of length 256
    return max(0, x[89])
def l406_90(x):
    # x is a list (or vector) of length 256
    return max(0, x[90])
def l406_91(x):
    # x is a list (or vector) of length 256
    return max(0, x[91])
def l406_92(x):
    # x is a list (or vector) of length 256
    return max(0, x[92])
def l406_93(x):
    # x is a list (or vector) of length 256
    return max(0, x[93])
def l406_94(x):
    # x is a list (or vector) of length 256
    return max(0, x[94])
def l406_95(x):
    # x is a list (or vector) of length 256
    return max(0, x[95])
def l406_96(x):
    # x is a list (or vector) of length 256
    return max(0, x[96])
def l406_97(x):
    # x is a list (or vector) of length 256
    return max(0, x[96] + x[129] + -1.0)
def l406_98(x):
    # x is a list (or vector) of length 256
    return max(0, x[97] + x[130] + -1.0)
def l406_99(x):
    # x is a list (or vector) of length 256
    return max(0, x[98] + x[131] + -1.0)
def l406_100(x):
    # x is a list (or vector) of length 256
    return max(0, x[99] + x[132] + -1.0)
def l406_101(x):
    # x is a list (or vector) of length 256
    return max(0, x[100] + x[133] + -1.0)
def l406_102(x):
    # x is a list (or vector) of length 256
    return max(0, x[101] + x[134] + -1.0)
def l406_103(x):
    # x is a list (or vector) of length 256
    return max(0, x[102] + x[135] + -1.0)
def l406_104(x):
    # x is a list (or vector) of length 256
    return max(0, x[103] + x[136] + -1.0)
def l406_105(x):
    # x is a list (or vector) of length 256
    return max(0, x[104] + x[137] + -1.0)
def l406_106(x):
    # x is a list (or vector) of length 256
    return max(0, x[105] + x[138] + -1.0)
def l406_107(x):
    # x is a list (or vector) of length 256
    return max(0, x[106] + x[139] + -1.0)
def l406_108(x):
    # x is a list (or vector) of length 256
    return max(0, x[107] + x[140] + -1.0)
def l406_109(x):
    # x is a list (or vector) of length 256
    return max(0, x[108] + x[141] + -1.0)
def l406_110(x):
    # x is a list (or vector) of length 256
    return max(0, x[109] + x[142] + -1.0)
def l406_111(x):
    # x is a list (or vector) of length 256
    return max(0, x[110] + x[143] + -1.0)
def l406_112(x):
    # x is a list (or vector) of length 256
    return max(0, x[111] + x[144] + -1.0)
def l406_113(x):
    # x is a list (or vector) of length 256
    return max(0, x[112] + x[145] + -1.0)
def l406_114(x):
    # x is a list (or vector) of length 256
    return max(0, x[113] + x[146] + -1.0)
def l406_115(x):
    # x is a list (or vector) of length 256
    return max(0, x[114] + x[147] + -1.0)
def l406_116(x):
    # x is a list (or vector) of length 256
    return max(0, x[115] + x[148] + -1.0)
def l406_117(x):
    # x is a list (or vector) of length 256
    return max(0, x[116] + x[149] + -1.0)
def l406_118(x):
    # x is a list (or vector) of length 256
    return max(0, x[117] + x[150] + -1.0)
def l406_119(x):
    # x is a list (or vector) of length 256
    return max(0, x[118] + x[151] + -1.0)
def l406_120(x):
    # x is a list (or vector) of length 256
    return max(0, x[119] + x[152] + -1.0)
def l406_121(x):
    # x is a list (or vector) of length 256
    return max(0, x[120] + x[153] + -1.0)
def l406_122(x):
    # x is a list (or vector) of length 256
    return max(0, x[121] + x[154] + -1.0)
def l406_123(x):
    # x is a list (or vector) of length 256
    return max(0, x[122] + x[155] + -1.0)
def l406_124(x):
    # x is a list (or vector) of length 256
    return max(0, x[123] + x[156] + -1.0)
def l406_125(x):
    # x is a list (or vector) of length 256
    return max(0, x[124] + x[157] + -1.0)
def l406_126(x):
    # x is a list (or vector) of length 256
    return max(0, x[125] + x[158] + -1.0)
def l406_127(x):
    # x is a list (or vector) of length 256
    return max(0, x[126] + x[159] + -1.0)
def l406_128(x):
    # x is a list (or vector) of length 256
    return max(0, x[97])
def l406_129(x):
    # x is a list (or vector) of length 256
    return max(0, x[98])
def l406_130(x):
    # x is a list (or vector) of length 256
    return max(0, x[99])
def l406_131(x):
    # x is a list (or vector) of length 256
    return max(0, x[100])
def l406_132(x):
    # x is a list (or vector) of length 256
    return max(0, x[101])
def l406_133(x):
    # x is a list (or vector) of length 256
    return max(0, x[102])
def l406_134(x):
    # x is a list (or vector) of length 256
    return max(0, x[103])
def l406_135(x):
    # x is a list (or vector) of length 256
    return max(0, x[104])
def l406_136(x):
    # x is a list (or vector) of length 256
    return max(0, x[105])
def l406_137(x):
    # x is a list (or vector) of length 256
    return max(0, x[106])
def l406_138(x):
    # x is a list (or vector) of length 256
    return max(0, x[107])
def l406_139(x):
    # x is a list (or vector) of length 256
    return max(0, x[108])
def l406_140(x):
    # x is a list (or vector) of length 256
    return max(0, x[109])
def l406_141(x):
    # x is a list (or vector) of length 256
    return max(0, x[110])
def l406_142(x):
    # x is a list (or vector) of length 256
    return max(0, x[111])
def l406_143(x):
    # x is a list (or vector) of length 256
    return max(0, x[112])
def l406_144(x):
    # x is a list (or vector) of length 256
    return max(0, x[113])
def l406_145(x):
    # x is a list (or vector) of length 256
    return max(0, x[114])
def l406_146(x):
    # x is a list (or vector) of length 256
    return max(0, x[115])
def l406_147(x):
    # x is a list (or vector) of length 256
    return max(0, x[116])
def l406_148(x):
    # x is a list (or vector) of length 256
    return max(0, x[117])
def l406_149(x):
    # x is a list (or vector) of length 256
    return max(0, x[118])
def l406_150(x):
    # x is a list (or vector) of length 256
    return max(0, x[119])
def l406_151(x):
    # x is a list (or vector) of length 256
    return max(0, x[120])
def l406_152(x):
    # x is a list (or vector) of length 256
    return max(0, x[121])
def l406_153(x):
    # x is a list (or vector) of length 256
    return max(0, x[122])
def l406_154(x):
    # x is a list (or vector) of length 256
    return max(0, x[123])
def l406_155(x):
    # x is a list (or vector) of length 256
    return max(0, x[124])
def l406_156(x):
    # x is a list (or vector) of length 256
    return max(0, x[125])
def l406_157(x):
    # x is a list (or vector) of length 256
    return max(0, x[126])
def l406_158(x):
    # x is a list (or vector) of length 256
    return max(0, x[127])
def l406_159(x):
    # x is a list (or vector) of length 256
    return max(0, x[128] + x[129] + -1.0)
def l406_160(x):
    # x is a list (or vector) of length 256
    return max(0, x[129] + x[130] + -1.0)
def l406_161(x):
    # x is a list (or vector) of length 256
    return max(0, x[130] + x[131] + -1.0)
def l406_162(x):
    # x is a list (or vector) of length 256
    return max(0, x[131] + x[132] + -1.0)
def l406_163(x):
    # x is a list (or vector) of length 256
    return max(0, x[132] + x[133] + -1.0)
def l406_164(x):
    # x is a list (or vector) of length 256
    return max(0, x[133] + x[134] + -1.0)
def l406_165(x):
    # x is a list (or vector) of length 256
    return max(0, x[134] + x[135] + -1.0)
def l406_166(x):
    # x is a list (or vector) of length 256
    return max(0, x[135] + x[136] + -1.0)
def l406_167(x):
    # x is a list (or vector) of length 256
    return max(0, x[136] + x[137] + -1.0)
def l406_168(x):
    # x is a list (or vector) of length 256
    return max(0, x[137] + x[138] + -1.0)
def l406_169(x):
    # x is a list (or vector) of length 256
    return max(0, x[138] + x[139] + -1.0)
def l406_170(x):
    # x is a list (or vector) of length 256
    return max(0, x[139] + x[140] + -1.0)
def l406_171(x):
    # x is a list (or vector) of length 256
    return max(0, x[140] + x[141] + -1.0)
def l406_172(x):
    # x is a list (or vector) of length 256
    return max(0, x[141] + x[142] + -1.0)
def l406_173(x):
    # x is a list (or vector) of length 256
    return max(0, x[142] + x[143] + -1.0)
def l406_174(x):
    # x is a list (or vector) of length 256
    return max(0, x[143] + x[144] + -1.0)
def l406_175(x):
    # x is a list (or vector) of length 256
    return max(0, x[144] + x[145] + -1.0)
def l406_176(x):
    # x is a list (or vector) of length 256
    return max(0, x[145] + x[146] + -1.0)
def l406_177(x):
    # x is a list (or vector) of length 256
    return max(0, x[146] + x[147] + -1.0)
def l406_178(x):
    # x is a list (or vector) of length 256
    return max(0, x[147] + x[148] + -1.0)
def l406_179(x):
    # x is a list (or vector) of length 256
    return max(0, x[148] + x[149] + -1.0)
def l406_180(x):
    # x is a list (or vector) of length 256
    return max(0, x[149] + x[150] + -1.0)
def l406_181(x):
    # x is a list (or vector) of length 256
    return max(0, x[150] + x[151] + -1.0)
def l406_182(x):
    # x is a list (or vector) of length 256
    return max(0, x[151] + x[152] + -1.0)
def l406_183(x):
    # x is a list (or vector) of length 256
    return max(0, x[152] + x[153] + -1.0)
def l406_184(x):
    # x is a list (or vector) of length 256
    return max(0, x[153] + x[154] + -1.0)
def l406_185(x):
    # x is a list (or vector) of length 256
    return max(0, x[154] + x[155] + -1.0)
def l406_186(x):
    # x is a list (or vector) of length 256
    return max(0, x[155] + x[156] + -1.0)
def l406_187(x):
    # x is a list (or vector) of length 256
    return max(0, x[156] + x[157] + -1.0)
def l406_188(x):
    # x is a list (or vector) of length 256
    return max(0, x[157] + x[158] + -1.0)
def l406_189(x):
    # x is a list (or vector) of length 256
    return max(0, x[158] + x[159] + -1.0)
def l406_190(x):
    # x is a list (or vector) of length 256
    return max(0, x[128])
def l406_191(x):
    # x is a list (or vector) of length 256
    return max(0, x[128])
def l406_192(x):
    # x is a list (or vector) of length 256
    return max(0, x[129])
def l406_193(x):
    # x is a list (or vector) of length 256
    return max(0, x[130])
def l406_194(x):
    # x is a list (or vector) of length 256
    return max(0, x[131])
def l406_195(x):
    # x is a list (or vector) of length 256
    return max(0, x[132])
def l406_196(x):
    # x is a list (or vector) of length 256
    return max(0, x[133])
def l406_197(x):
    # x is a list (or vector) of length 256
    return max(0, x[134])
def l406_198(x):
    # x is a list (or vector) of length 256
    return max(0, x[135])
def l406_199(x):
    # x is a list (or vector) of length 256
    return max(0, x[136])
def l406_200(x):
    # x is a list (or vector) of length 256
    return max(0, x[137])
def l406_201(x):
    # x is a list (or vector) of length 256
    return max(0, x[138])
def l406_202(x):
    # x is a list (or vector) of length 256
    return max(0, x[139])
def l406_203(x):
    # x is a list (or vector) of length 256
    return max(0, x[140])
def l406_204(x):
    # x is a list (or vector) of length 256
    return max(0, x[141])
def l406_205(x):
    # x is a list (or vector) of length 256
    return max(0, x[142])
def l406_206(x):
    # x is a list (or vector) of length 256
    return max(0, x[143])
def l406_207(x):
    # x is a list (or vector) of length 256
    return max(0, x[144])
def l406_208(x):
    # x is a list (or vector) of length 256
    return max(0, x[145])
def l406_209(x):
    # x is a list (or vector) of length 256
    return max(0, x[146])
def l406_210(x):
    # x is a list (or vector) of length 256
    return max(0, x[147])
def l406_211(x):
    # x is a list (or vector) of length 256
    return max(0, x[148])
def l406_212(x):
    # x is a list (or vector) of length 256
    return max(0, x[149])
def l406_213(x):
    # x is a list (or vector) of length 256
    return max(0, x[150])
def l406_214(x):
    # x is a list (or vector) of length 256
    return max(0, x[151])
def l406_215(x):
    # x is a list (or vector) of length 256
    return max(0, x[152])
def l406_216(x):
    # x is a list (or vector) of length 256
    return max(0, x[153])
def l406_217(x):
    # x is a list (or vector) of length 256
    return max(0, x[154])
def l406_218(x):
    # x is a list (or vector) of length 256
    return max(0, x[155])
def l406_219(x):
    # x is a list (or vector) of length 256
    return max(0, x[156])
def l406_220(x):
    # x is a list (or vector) of length 256
    return max(0, x[157])
def l406_221(x):
    # x is a list (or vector) of length 256
    return max(0, x[158])
def l406_222(x):
    # x is a list (or vector) of length 256
    return max(0, x[159])
def l406_223(x):
    # x is a list (or vector) of length 256
    return max(0, x[160])
def l406_224(x):
    # x is a list (or vector) of length 256
    return max(0, x[161])
def l406_225(x):
    # x is a list (or vector) of length 256
    return max(0, x[162])
def l406_226(x):
    # x is a list (or vector) of length 256
    return max(0, x[163])
def l406_227(x):
    # x is a list (or vector) of length 256
    return max(0, x[164])
def l406_228(x):
    # x is a list (or vector) of length 256
    return max(0, x[165])
def l406_229(x):
    # x is a list (or vector) of length 256
    return max(0, x[166])
def l406_230(x):
    # x is a list (or vector) of length 256
    return max(0, x[167])
def l406_231(x):
    # x is a list (or vector) of length 256
    return max(0, x[168])
def l406_232(x):
    # x is a list (or vector) of length 256
    return max(0, x[169])
def l406_233(x):
    # x is a list (or vector) of length 256
    return max(0, x[170])
def l406_234(x):
    # x is a list (or vector) of length 256
    return max(0, x[171])
def l406_235(x):
    # x is a list (or vector) of length 256
    return max(0, x[172])
def l406_236(x):
    # x is a list (or vector) of length 256
    return max(0, x[173])
def l406_237(x):
    # x is a list (or vector) of length 256
    return max(0, x[174])
def l406_238(x):
    # x is a list (or vector) of length 256
    return max(0, x[175])
def l406_239(x):
    # x is a list (or vector) of length 256
    return max(0, x[176])
def l406_240(x):
    # x is a list (or vector) of length 256
    return max(0, x[177])
def l406_241(x):
    # x is a list (or vector) of length 256
    return max(0, x[178])
def l406_242(x):
    # x is a list (or vector) of length 256
    return max(0, x[179])
def l406_243(x):
    # x is a list (or vector) of length 256
    return max(0, x[180])
def l406_244(x):
    # x is a list (or vector) of length 256
    return max(0, x[181])
def l406_245(x):
    # x is a list (or vector) of length 256
    return max(0, x[182])
def l406_246(x):
    # x is a list (or vector) of length 256
    return max(0, x[183])
def l406_247(x):
    # x is a list (or vector) of length 256
    return max(0, x[184])
def l406_248(x):
    # x is a list (or vector) of length 256
    return max(0, x[185])
def l406_249(x):
    # x is a list (or vector) of length 256
    return max(0, x[186])
def l406_250(x):
    # x is a list (or vector) of length 256
    return max(0, x[187])
def l406_251(x):
    # x is a list (or vector) of length 256
    return max(0, x[188])
def l406_252(x):
    # x is a list (or vector) of length 256
    return max(0, x[189])
def l406_253(x):
    # x is a list (or vector) of length 256
    return max(0, x[190])
def l406_254(x):
    # x is a list (or vector) of length 256
    return max(0, x[191])
def l406_255(x):
    # x is a list (or vector) of length 256
    return max(0, x[192])
def l406_256(x):
    # x is a list (or vector) of length 256
    return max(0, x[193])
def l406_257(x):
    # x is a list (or vector) of length 256
    return max(0, x[194])
def l406_258(x):
    # x is a list (or vector) of length 256
    return max(0, x[195])
def l406_259(x):
    # x is a list (or vector) of length 256
    return max(0, x[196])
def l406_260(x):
    # x is a list (or vector) of length 256
    return max(0, x[197])
def l406_261(x):
    # x is a list (or vector) of length 256
    return max(0, x[198])
def l406_262(x):
    # x is a list (or vector) of length 256
    return max(0, x[199])
def l406_263(x):
    # x is a list (or vector) of length 256
    return max(0, x[200])
def l406_264(x):
    # x is a list (or vector) of length 256
    return max(0, x[201])
def l406_265(x):
    # x is a list (or vector) of length 256
    return max(0, x[202])
def l406_266(x):
    # x is a list (or vector) of length 256
    return max(0, x[203])
def l406_267(x):
    # x is a list (or vector) of length 256
    return max(0, x[204])
def l406_268(x):
    # x is a list (or vector) of length 256
    return max(0, x[205])
def l406_269(x):
    # x is a list (or vector) of length 256
    return max(0, x[206])
def l406_270(x):
    # x is a list (or vector) of length 256
    return max(0, x[207])
def l406_271(x):
    # x is a list (or vector) of length 256
    return max(0, x[208])
def l406_272(x):
    # x is a list (or vector) of length 256
    return max(0, x[209])
def l406_273(x):
    # x is a list (or vector) of length 256
    return max(0, x[210])
def l406_274(x):
    # x is a list (or vector) of length 256
    return max(0, x[211])
def l406_275(x):
    # x is a list (or vector) of length 256
    return max(0, x[212])
def l406_276(x):
    # x is a list (or vector) of length 256
    return max(0, x[213])
def l406_277(x):
    # x is a list (or vector) of length 256
    return max(0, x[214])
def l406_278(x):
    # x is a list (or vector) of length 256
    return max(0, x[215])
def l406_279(x):
    # x is a list (or vector) of length 256
    return max(0, x[216])
def l406_280(x):
    # x is a list (or vector) of length 256
    return max(0, x[217])
def l406_281(x):
    # x is a list (or vector) of length 256
    return max(0, x[218])
def l406_282(x):
    # x is a list (or vector) of length 256
    return max(0, x[219])
def l406_283(x):
    # x is a list (or vector) of length 256
    return max(0, x[220])
def l406_284(x):
    # x is a list (or vector) of length 256
    return max(0, x[221])
def l406_285(x):
    # x is a list (or vector) of length 256
    return max(0, x[222])
def l406_286(x):
    # x is a list (or vector) of length 256
    return max(0, x[223])
def l406_287(x):
    # x is a list (or vector) of length 256
    return max(0, x[224])
def l406_288(x):
    # x is a list (or vector) of length 256
    return max(0, x[225])
def l406_289(x):
    # x is a list (or vector) of length 256
    return max(0, x[226])
def l406_290(x):
    # x is a list (or vector) of length 256
    return max(0, x[227])
def l406_291(x):
    # x is a list (or vector) of length 256
    return max(0, x[228])
def l406_292(x):
    # x is a list (or vector) of length 256
    return max(0, x[229])
def l406_293(x):
    # x is a list (or vector) of length 256
    return max(0, x[230])
def l406_294(x):
    # x is a list (or vector) of length 256
    return max(0, x[231])
def l406_295(x):
    # x is a list (or vector) of length 256
    return max(0, x[232])
def l406_296(x):
    # x is a list (or vector) of length 256
    return max(0, x[233])
def l406_297(x):
    # x is a list (or vector) of length 256
    return max(0, x[234])
def l406_298(x):
    # x is a list (or vector) of length 256
    return max(0, x[235])
def l406_299(x):
    # x is a list (or vector) of length 256
    return max(0, x[236])
def l406_300(x):
    # x is a list (or vector) of length 256
    return max(0, x[237])
def l406_301(x):
    # x is a list (or vector) of length 256
    return max(0, x[238])
def l406_302(x):
    # x is a list (or vector) of length 256
    return max(0, x[239])
def l406_303(x):
    # x is a list (or vector) of length 256
    return max(0, x[240])
def l406_304(x):
    # x is a list (or vector) of length 256
    return max(0, x[241])
def l406_305(x):
    # x is a list (or vector) of length 256
    return max(0, x[242])
def l406_306(x):
    # x is a list (or vector) of length 256
    return max(0, x[243])
def l406_307(x):
    # x is a list (or vector) of length 256
    return max(0, x[244])
def l406_308(x):
    # x is a list (or vector) of length 256
    return max(0, x[245])
def l406_309(x):
    # x is a list (or vector) of length 256
    return max(0, x[246])
def l406_310(x):
    # x is a list (or vector) of length 256
    return max(0, x[247])
def l406_311(x):
    # x is a list (or vector) of length 256
    return max(0, x[248])
def l406_312(x):
    # x is a list (or vector) of length 256
    return max(0, x[249])
def l406_313(x):
    # x is a list (or vector) of length 256
    return max(0, x[250])
def l406_314(x):
    # x is a list (or vector) of length 256
    return max(0, x[251])
def l406_315(x):
    # x is a list (or vector) of length 256
    return max(0, x[252])
def l406_316(x):
    # x is a list (or vector) of length 256
    return max(0, x[253])
def l406_317(x):
    # x is a list (or vector) of length 256
    return max(0, x[254])
def l406_318(x):
    # x is a list (or vector) of length 256
    return max(0, x[255])
def l406_(x):
    # x is a list (or vector) of length 256
    return [
        l406_0(x),
        l406_1(x),
        l406_2(x),
        l406_3(x),
        l406_4(x),
        l406_5(x),
        l406_6(x),
        l406_7(x),
        l406_8(x),
        l406_9(x),
        l406_10(x),
        l406_11(x),
        l406_12(x),
        l406_13(x),
        l406_14(x),
        l406_15(x),
        l406_16(x),
        l406_17(x),
        l406_18(x),
        l406_19(x),
        l406_20(x),
        l406_21(x),
        l406_22(x),
        l406_23(x),
        l406_24(x),
        l406_25(x),
        l406_26(x),
        l406_27(x),
        l406_28(x),
        l406_29(x),
        l406_30(x),
        l406_31(x),
        l406_32(x),
        l406_33(x),
        l406_34(x),
        l406_35(x),
        l406_36(x),
        l406_37(x),
        l406_38(x),
        l406_39(x),
        l406_40(x),
        l406_41(x),
        l406_42(x),
        l406_43(x),
        l406_44(x),
        l406_45(x),
        l406_46(x),
        l406_47(x),
        l406_48(x),
        l406_49(x),
        l406_50(x),
        l406_51(x),
        l406_52(x),
        l406_53(x),
        l406_54(x),
        l406_55(x),
        l406_56(x),
        l406_57(x),
        l406_58(x),
        l406_59(x),
        l406_60(x),
        l406_61(x),
        l406_62(x),
        l406_63(x),
        l406_64(x),
        l406_65(x),
        l406_66(x),
        l406_67(x),
        l406_68(x),
        l406_69(x),
        l406_70(x),
        l406_71(x),
        l406_72(x),
        l406_73(x),
        l406_74(x),
        l406_75(x),
        l406_76(x),
        l406_77(x),
        l406_78(x),
        l406_79(x),
        l406_80(x),
        l406_81(x),
        l406_82(x),
        l406_83(x),
        l406_84(x),
        l406_85(x),
        l406_86(x),
        l406_87(x),
        l406_88(x),
        l406_89(x),
        l406_90(x),
        l406_91(x),
        l406_92(x),
        l406_93(x),
        l406_94(x),
        l406_95(x),
        l406_96(x),
        l406_97(x),
        l406_98(x),
        l406_99(x),
        l406_100(x),
        l406_101(x),
        l406_102(x),
        l406_103(x),
        l406_104(x),
        l406_105(x),
        l406_106(x),
        l406_107(x),
        l406_108(x),
        l406_109(x),
        l406_110(x),
        l406_111(x),
        l406_112(x),
        l406_113(x),
        l406_114(x),
        l406_115(x),
        l406_116(x),
        l406_117(x),
        l406_118(x),
        l406_119(x),
        l406_120(x),
        l406_121(x),
        l406_122(x),
        l406_123(x),
        l406_124(x),
        l406_125(x),
        l406_126(x),
        l406_127(x),
        l406_128(x),
        l406_129(x),
        l406_130(x),
        l406_131(x),
        l406_132(x),
        l406_133(x),
        l406_134(x),
        l406_135(x),
        l406_136(x),
        l406_137(x),
        l406_138(x),
        l406_139(x),
        l406_140(x),
        l406_141(x),
        l406_142(x),
        l406_143(x),
        l406_144(x),
        l406_145(x),
        l406_146(x),
        l406_147(x),
        l406_148(x),
        l406_149(x),
        l406_150(x),
        l406_151(x),
        l406_152(x),
        l406_153(x),
        l406_154(x),
        l406_155(x),
        l406_156(x),
        l406_157(x),
        l406_158(x),
        l406_159(x),
        l406_160(x),
        l406_161(x),
        l406_162(x),
        l406_163(x),
        l406_164(x),
        l406_165(x),
        l406_166(x),
        l406_167(x),
        l406_168(x),
        l406_169(x),
        l406_170(x),
        l406_171(x),
        l406_172(x),
        l406_173(x),
        l406_174(x),
        l406_175(x),
        l406_176(x),
        l406_177(x),
        l406_178(x),
        l406_179(x),
        l406_180(x),
        l406_181(x),
        l406_182(x),
        l406_183(x),
        l406_184(x),
        l406_185(x),
        l406_186(x),
        l406_187(x),
        l406_188(x),
        l406_189(x),
        l406_190(x),
        l406_191(x),
        l406_192(x),
        l406_193(x),
        l406_194(x),
        l406_195(x),
        l406_196(x),
        l406_197(x),
        l406_198(x),
        l406_199(x),
        l406_200(x),
        l406_201(x),
        l406_202(x),
        l406_203(x),
        l406_204(x),
        l406_205(x),
        l406_206(x),
        l406_207(x),
        l406_208(x),
        l406_209(x),
        l406_210(x),
        l406_211(x),
        l406_212(x),
        l406_213(x),
        l406_214(x),
        l406_215(x),
        l406_216(x),
        l406_217(x),
        l406_218(x),
        l406_219(x),
        l406_220(x),
        l406_221(x),
        l406_222(x),
        l406_223(x),
        l406_224(x),
        l406_225(x),
        l406_226(x),
        l406_227(x),
        l406_228(x),
        l406_229(x),
        l406_230(x),
        l406_231(x),
        l406_232(x),
        l406_233(x),
        l406_234(x),
        l406_235(x),
        l406_236(x),
        l406_237(x),
        l406_238(x),
        l406_239(x),
        l406_240(x),
        l406_241(x),
        l406_242(x),
        l406_243(x),
        l406_244(x),
        l406_245(x),
        l406_246(x),
        l406_247(x),
        l406_248(x),
        l406_249(x),
        l406_250(x),
        l406_251(x),
        l406_252(x),
        l406_253(x),
        l406_254(x),
        l406_255(x),
        l406_256(x),
        l406_257(x),
        l406_258(x),
        l406_259(x),
        l406_260(x),
        l406_261(x),
        l406_262(x),
        l406_263(x),
        l406_264(x),
        l406_265(x),
        l406_266(x),
        l406_267(x),
        l406_268(x),
        l406_269(x),
        l406_270(x),
        l406_271(x),
        l406_272(x),
        l406_273(x),
        l406_274(x),
        l406_275(x),
        l406_276(x),
        l406_277(x),
        l406_278(x),
        l406_279(x),
        l406_280(x),
        l406_281(x),
        l406_282(x),
        l406_283(x),
        l406_284(x),
        l406_285(x),
        l406_286(x),
        l406_287(x),
        l406_288(x),
        l406_289(x),
        l406_290(x),
        l406_291(x),
        l406_292(x),
        l406_293(x),
        l406_294(x),
        l406_295(x),
        l406_296(x),
        l406_297(x),
        l406_298(x),
        l406_299(x),
        l406_300(x),
        l406_301(x),
        l406_302(x),
        l406_303(x),
        l406_304(x),
        l406_305(x),
        l406_306(x),
        l406_307(x),
        l406_308(x),
        l406_309(x),
        l406_310(x),
        l406_311(x),
        l406_312(x),
        l406_313(x),
        l406_314(x),
        l406_315(x),
        l406_316(x),
        l406_317(x),
        l406_318(x),
    ]