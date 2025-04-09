import numpy as np




# Generated from reverse engineering
def l154_g(x: np.ndarray) -> np.ndarray:
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




def l154_0(x):
    # x is a list (or vector) of length 256
    return max(0, x[0])
def l154_1(x):
    # x is a list (or vector) of length 256
    return max(0, x[1])
def l154_2(x):
    # x is a list (or vector) of length 256
    return max(0, x[2])
def l154_3(x):
    # x is a list (or vector) of length 256
    return max(0, x[3])
def l154_4(x):
    # x is a list (or vector) of length 256
    return max(0, x[4])
def l154_5(x):
    # x is a list (or vector) of length 256
    return max(0, x[5])
def l154_6(x):
    # x is a list (or vector) of length 256
    return max(0, x[6])
def l154_7(x):
    # x is a list (or vector) of length 256
    return max(0, x[7])
def l154_8(x):
    # x is a list (or vector) of length 256
    return max(0, x[8])
def l154_9(x):
    # x is a list (or vector) of length 256
    return max(0, x[9])
def l154_10(x):
    # x is a list (or vector) of length 256
    return max(0, x[10])
def l154_11(x):
    # x is a list (or vector) of length 256
    return max(0, x[11])
def l154_12(x):
    # x is a list (or vector) of length 256
    return max(0, x[12])
def l154_13(x):
    # x is a list (or vector) of length 256
    return max(0, x[13])
def l154_14(x):
    # x is a list (or vector) of length 256
    return max(0, x[14])
def l154_15(x):
    # x is a list (or vector) of length 256
    return max(0, x[15])
def l154_16(x):
    # x is a list (or vector) of length 256
    return max(0, x[16])
def l154_17(x):
    # x is a list (or vector) of length 256
    return max(0, x[17])
def l154_18(x):
    # x is a list (or vector) of length 256
    return max(0, x[18])
def l154_19(x):
    # x is a list (or vector) of length 256
    return max(0, x[19])
def l154_20(x):
    # x is a list (or vector) of length 256
    return max(0, x[20])
def l154_21(x):
    # x is a list (or vector) of length 256
    return max(0, x[21])
def l154_22(x):
    # x is a list (or vector) of length 256
    return max(0, x[22])
def l154_23(x):
    # x is a list (or vector) of length 256
    return max(0, x[23])
def l154_24(x):
    # x is a list (or vector) of length 256
    return max(0, x[24])
def l154_25(x):
    # x is a list (or vector) of length 256
    return max(0, x[25])
def l154_26(x):
    # x is a list (or vector) of length 256
    return max(0, x[26])
def l154_27(x):
    # x is a list (or vector) of length 256
    return max(0, x[27])
def l154_28(x):
    # x is a list (or vector) of length 256
    return max(0, x[28])
def l154_29(x):
    # x is a list (or vector) of length 256
    return max(0, x[29])
def l154_30(x):
    # x is a list (or vector) of length 256
    return max(0, x[30])
def l154_31(x):
    # x is a list (or vector) of length 256
    return max(0, x[31])
def l154_32(x):
    # x is a list (or vector) of length 256
    return max(0, x[32])
def l154_33(x):
    # x is a list (or vector) of length 256
    return max(0, x[33])
def l154_34(x):
    # x is a list (or vector) of length 256
    return max(0, x[34])
def l154_35(x):
    # x is a list (or vector) of length 256
    return max(0, x[35])
def l154_36(x):
    # x is a list (or vector) of length 256
    return max(0, x[36])
def l154_37(x):
    # x is a list (or vector) of length 256
    return max(0, x[37])
def l154_38(x):
    # x is a list (or vector) of length 256
    return max(0, x[38])
def l154_39(x):
    # x is a list (or vector) of length 256
    return max(0, x[39])
def l154_40(x):
    # x is a list (or vector) of length 256
    return max(0, x[40])
def l154_41(x):
    # x is a list (or vector) of length 256
    return max(0, x[41])
def l154_42(x):
    # x is a list (or vector) of length 256
    return max(0, x[42])
def l154_43(x):
    # x is a list (or vector) of length 256
    return max(0, x[43])
def l154_44(x):
    # x is a list (or vector) of length 256
    return max(0, x[44])
def l154_45(x):
    # x is a list (or vector) of length 256
    return max(0, x[45])
def l154_46(x):
    # x is a list (or vector) of length 256
    return max(0, x[46])
def l154_47(x):
    # x is a list (or vector) of length 256
    return max(0, x[47])
def l154_48(x):
    # x is a list (or vector) of length 256
    return max(0, x[48])
def l154_49(x):
    # x is a list (or vector) of length 256
    return max(0, x[49])
def l154_50(x):
    # x is a list (or vector) of length 256
    return max(0, x[50])
def l154_51(x):
    # x is a list (or vector) of length 256
    return max(0, x[51])
def l154_52(x):
    # x is a list (or vector) of length 256
    return max(0, x[52])
def l154_53(x):
    # x is a list (or vector) of length 256
    return max(0, x[53])
def l154_54(x):
    # x is a list (or vector) of length 256
    return max(0, x[54])
def l154_55(x):
    # x is a list (or vector) of length 256
    return max(0, x[55])
def l154_56(x):
    # x is a list (or vector) of length 256
    return max(0, x[56])
def l154_57(x):
    # x is a list (or vector) of length 256
    return max(0, x[57])
def l154_58(x):
    # x is a list (or vector) of length 256
    return max(0, x[58])
def l154_59(x):
    # x is a list (or vector) of length 256
    return max(0, x[59])
def l154_60(x):
    # x is a list (or vector) of length 256
    return max(0, x[60])
def l154_61(x):
    # x is a list (or vector) of length 256
    return max(0, x[61])
def l154_62(x):
    # x is a list (or vector) of length 256
    return max(0, x[62])
def l154_63(x):
    # x is a list (or vector) of length 256
    return max(0, x[63])
def l154_64(x):
    # x is a list (or vector) of length 256
    return max(0, x[64])
def l154_65(x):
    # x is a list (or vector) of length 256
    return max(0, x[65])
def l154_66(x):
    # x is a list (or vector) of length 256
    return max(0, x[66])
def l154_67(x):
    # x is a list (or vector) of length 256
    return max(0, x[67])
def l154_68(x):
    # x is a list (or vector) of length 256
    return max(0, x[68])
def l154_69(x):
    # x is a list (or vector) of length 256
    return max(0, x[69])
def l154_70(x):
    # x is a list (or vector) of length 256
    return max(0, x[70])
def l154_71(x):
    # x is a list (or vector) of length 256
    return max(0, x[71])
def l154_72(x):
    # x is a list (or vector) of length 256
    return max(0, x[72])
def l154_73(x):
    # x is a list (or vector) of length 256
    return max(0, x[73])
def l154_74(x):
    # x is a list (or vector) of length 256
    return max(0, x[74])
def l154_75(x):
    # x is a list (or vector) of length 256
    return max(0, x[75])
def l154_76(x):
    # x is a list (or vector) of length 256
    return max(0, x[76])
def l154_77(x):
    # x is a list (or vector) of length 256
    return max(0, x[77])
def l154_78(x):
    # x is a list (or vector) of length 256
    return max(0, x[78])
def l154_79(x):
    # x is a list (or vector) of length 256
    return max(0, x[79])
def l154_80(x):
    # x is a list (or vector) of length 256
    return max(0, x[80])
def l154_81(x):
    # x is a list (or vector) of length 256
    return max(0, x[81])
def l154_82(x):
    # x is a list (or vector) of length 256
    return max(0, x[82])
def l154_83(x):
    # x is a list (or vector) of length 256
    return max(0, x[83])
def l154_84(x):
    # x is a list (or vector) of length 256
    return max(0, x[84])
def l154_85(x):
    # x is a list (or vector) of length 256
    return max(0, x[85])
def l154_86(x):
    # x is a list (or vector) of length 256
    return max(0, x[86])
def l154_87(x):
    # x is a list (or vector) of length 256
    return max(0, x[87])
def l154_88(x):
    # x is a list (or vector) of length 256
    return max(0, x[88])
def l154_89(x):
    # x is a list (or vector) of length 256
    return max(0, x[89])
def l154_90(x):
    # x is a list (or vector) of length 256
    return max(0, x[90])
def l154_91(x):
    # x is a list (or vector) of length 256
    return max(0, x[91])
def l154_92(x):
    # x is a list (or vector) of length 256
    return max(0, x[92])
def l154_93(x):
    # x is a list (or vector) of length 256
    return max(0, x[93])
def l154_94(x):
    # x is a list (or vector) of length 256
    return max(0, x[94])
def l154_95(x):
    # x is a list (or vector) of length 256
    return max(0, x[95])
def l154_96(x):
    # x is a list (or vector) of length 256
    return max(0, x[96])
def l154_97(x):
    # x is a list (or vector) of length 256
    return max(0, x[96] + x[129] + -1.0)
def l154_98(x):
    # x is a list (or vector) of length 256
    return max(0, x[97] + x[130] + -1.0)
def l154_99(x):
    # x is a list (or vector) of length 256
    return max(0, x[98] + x[131] + -1.0)
def l154_100(x):
    # x is a list (or vector) of length 256
    return max(0, x[99] + x[132] + -1.0)
def l154_101(x):
    # x is a list (or vector) of length 256
    return max(0, x[100] + x[133] + -1.0)
def l154_102(x):
    # x is a list (or vector) of length 256
    return max(0, x[101] + x[134] + -1.0)
def l154_103(x):
    # x is a list (or vector) of length 256
    return max(0, x[102] + x[135] + -1.0)
def l154_104(x):
    # x is a list (or vector) of length 256
    return max(0, x[103] + x[136] + -1.0)
def l154_105(x):
    # x is a list (or vector) of length 256
    return max(0, x[104] + x[137] + -1.0)
def l154_106(x):
    # x is a list (or vector) of length 256
    return max(0, x[105] + x[138] + -1.0)
def l154_107(x):
    # x is a list (or vector) of length 256
    return max(0, x[106] + x[139] + -1.0)
def l154_108(x):
    # x is a list (or vector) of length 256
    return max(0, x[107] + x[140] + -1.0)
def l154_109(x):
    # x is a list (or vector) of length 256
    return max(0, x[108] + x[141] + -1.0)
def l154_110(x):
    # x is a list (or vector) of length 256
    return max(0, x[109] + x[142] + -1.0)
def l154_111(x):
    # x is a list (or vector) of length 256
    return max(0, x[110] + x[143] + -1.0)
def l154_112(x):
    # x is a list (or vector) of length 256
    return max(0, x[111] + x[144] + -1.0)
def l154_113(x):
    # x is a list (or vector) of length 256
    return max(0, x[112] + x[145] + -1.0)
def l154_114(x):
    # x is a list (or vector) of length 256
    return max(0, x[113] + x[146] + -1.0)
def l154_115(x):
    # x is a list (or vector) of length 256
    return max(0, x[114] + x[147] + -1.0)
def l154_116(x):
    # x is a list (or vector) of length 256
    return max(0, x[115] + x[148] + -1.0)
def l154_117(x):
    # x is a list (or vector) of length 256
    return max(0, x[116] + x[149] + -1.0)
def l154_118(x):
    # x is a list (or vector) of length 256
    return max(0, x[117] + x[150] + -1.0)
def l154_119(x):
    # x is a list (or vector) of length 256
    return max(0, x[118] + x[151] + -1.0)
def l154_120(x):
    # x is a list (or vector) of length 256
    return max(0, x[119] + x[152] + -1.0)
def l154_121(x):
    # x is a list (or vector) of length 256
    return max(0, x[120] + x[153] + -1.0)
def l154_122(x):
    # x is a list (or vector) of length 256
    return max(0, x[121] + x[154] + -1.0)
def l154_123(x):
    # x is a list (or vector) of length 256
    return max(0, x[122] + x[155] + -1.0)
def l154_124(x):
    # x is a list (or vector) of length 256
    return max(0, x[123] + x[156] + -1.0)
def l154_125(x):
    # x is a list (or vector) of length 256
    return max(0, x[124] + x[157] + -1.0)
def l154_126(x):
    # x is a list (or vector) of length 256
    return max(0, x[125] + x[158] + -1.0)
def l154_127(x):
    # x is a list (or vector) of length 256
    return max(0, x[126] + x[159] + -1.0)
def l154_128(x):
    # x is a list (or vector) of length 256
    return max(0, x[97])
def l154_129(x):
    # x is a list (or vector) of length 256
    return max(0, x[98])
def l154_130(x):
    # x is a list (or vector) of length 256
    return max(0, x[99])
def l154_131(x):
    # x is a list (or vector) of length 256
    return max(0, x[100])
def l154_132(x):
    # x is a list (or vector) of length 256
    return max(0, x[101])
def l154_133(x):
    # x is a list (or vector) of length 256
    return max(0, x[102])
def l154_134(x):
    # x is a list (or vector) of length 256
    return max(0, x[103])
def l154_135(x):
    # x is a list (or vector) of length 256
    return max(0, x[104])
def l154_136(x):
    # x is a list (or vector) of length 256
    return max(0, x[105])
def l154_137(x):
    # x is a list (or vector) of length 256
    return max(0, x[106])
def l154_138(x):
    # x is a list (or vector) of length 256
    return max(0, x[107])
def l154_139(x):
    # x is a list (or vector) of length 256
    return max(0, x[108])
def l154_140(x):
    # x is a list (or vector) of length 256
    return max(0, x[109])
def l154_141(x):
    # x is a list (or vector) of length 256
    return max(0, x[110])
def l154_142(x):
    # x is a list (or vector) of length 256
    return max(0, x[111])
def l154_143(x):
    # x is a list (or vector) of length 256
    return max(0, x[112])
def l154_144(x):
    # x is a list (or vector) of length 256
    return max(0, x[113])
def l154_145(x):
    # x is a list (or vector) of length 256
    return max(0, x[114])
def l154_146(x):
    # x is a list (or vector) of length 256
    return max(0, x[115])
def l154_147(x):
    # x is a list (or vector) of length 256
    return max(0, x[116])
def l154_148(x):
    # x is a list (or vector) of length 256
    return max(0, x[117])
def l154_149(x):
    # x is a list (or vector) of length 256
    return max(0, x[118])
def l154_150(x):
    # x is a list (or vector) of length 256
    return max(0, x[119])
def l154_151(x):
    # x is a list (or vector) of length 256
    return max(0, x[120])
def l154_152(x):
    # x is a list (or vector) of length 256
    return max(0, x[121])
def l154_153(x):
    # x is a list (or vector) of length 256
    return max(0, x[122])
def l154_154(x):
    # x is a list (or vector) of length 256
    return max(0, x[123])
def l154_155(x):
    # x is a list (or vector) of length 256
    return max(0, x[124])
def l154_156(x):
    # x is a list (or vector) of length 256
    return max(0, x[125])
def l154_157(x):
    # x is a list (or vector) of length 256
    return max(0, x[126])
def l154_158(x):
    # x is a list (or vector) of length 256
    return max(0, x[127])
def l154_159(x):
    # x is a list (or vector) of length 256
    return max(0, x[128] + x[129] + -1.0)
def l154_160(x):
    # x is a list (or vector) of length 256
    return max(0, x[129] + x[130] + -1.0)
def l154_161(x):
    # x is a list (or vector) of length 256
    return max(0, x[130] + x[131] + -1.0)
def l154_162(x):
    # x is a list (or vector) of length 256
    return max(0, x[131] + x[132] + -1.0)
def l154_163(x):
    # x is a list (or vector) of length 256
    return max(0, x[132] + x[133] + -1.0)
def l154_164(x):
    # x is a list (or vector) of length 256
    return max(0, x[133] + x[134] + -1.0)
def l154_165(x):
    # x is a list (or vector) of length 256
    return max(0, x[134] + x[135] + -1.0)
def l154_166(x):
    # x is a list (or vector) of length 256
    return max(0, x[135] + x[136] + -1.0)
def l154_167(x):
    # x is a list (or vector) of length 256
    return max(0, x[136] + x[137] + -1.0)
def l154_168(x):
    # x is a list (or vector) of length 256
    return max(0, x[137] + x[138] + -1.0)
def l154_169(x):
    # x is a list (or vector) of length 256
    return max(0, x[138] + x[139] + -1.0)
def l154_170(x):
    # x is a list (or vector) of length 256
    return max(0, x[139] + x[140] + -1.0)
def l154_171(x):
    # x is a list (or vector) of length 256
    return max(0, x[140] + x[141] + -1.0)
def l154_172(x):
    # x is a list (or vector) of length 256
    return max(0, x[141] + x[142] + -1.0)
def l154_173(x):
    # x is a list (or vector) of length 256
    return max(0, x[142] + x[143] + -1.0)
def l154_174(x):
    # x is a list (or vector) of length 256
    return max(0, x[143] + x[144] + -1.0)
def l154_175(x):
    # x is a list (or vector) of length 256
    return max(0, x[144] + x[145] + -1.0)
def l154_176(x):
    # x is a list (or vector) of length 256
    return max(0, x[145] + x[146] + -1.0)
def l154_177(x):
    # x is a list (or vector) of length 256
    return max(0, x[146] + x[147] + -1.0)
def l154_178(x):
    # x is a list (or vector) of length 256
    return max(0, x[147] + x[148] + -1.0)
def l154_179(x):
    # x is a list (or vector) of length 256
    return max(0, x[148] + x[149] + -1.0)
def l154_180(x):
    # x is a list (or vector) of length 256
    return max(0, x[149] + x[150] + -1.0)
def l154_181(x):
    # x is a list (or vector) of length 256
    return max(0, x[150] + x[151] + -1.0)
def l154_182(x):
    # x is a list (or vector) of length 256
    return max(0, x[151] + x[152] + -1.0)
def l154_183(x):
    # x is a list (or vector) of length 256
    return max(0, x[152] + x[153] + -1.0)
def l154_184(x):
    # x is a list (or vector) of length 256
    return max(0, x[153] + x[154] + -1.0)
def l154_185(x):
    # x is a list (or vector) of length 256
    return max(0, x[154] + x[155] + -1.0)
def l154_186(x):
    # x is a list (or vector) of length 256
    return max(0, x[155] + x[156] + -1.0)
def l154_187(x):
    # x is a list (or vector) of length 256
    return max(0, x[156] + x[157] + -1.0)
def l154_188(x):
    # x is a list (or vector) of length 256
    return max(0, x[157] + x[158] + -1.0)
def l154_189(x):
    # x is a list (or vector) of length 256
    return max(0, x[158] + x[159] + -1.0)
def l154_190(x):
    # x is a list (or vector) of length 256
    return max(0, x[128])
def l154_191(x):
    # x is a list (or vector) of length 256
    return max(0, x[128])
def l154_192(x):
    # x is a list (or vector) of length 256
    return max(0, x[129])
def l154_193(x):
    # x is a list (or vector) of length 256
    return max(0, x[130])
def l154_194(x):
    # x is a list (or vector) of length 256
    return max(0, x[131])
def l154_195(x):
    # x is a list (or vector) of length 256
    return max(0, x[132])
def l154_196(x):
    # x is a list (or vector) of length 256
    return max(0, x[133])
def l154_197(x):
    # x is a list (or vector) of length 256
    return max(0, x[134])
def l154_198(x):
    # x is a list (or vector) of length 256
    return max(0, x[135])
def l154_199(x):
    # x is a list (or vector) of length 256
    return max(0, x[136])
def l154_200(x):
    # x is a list (or vector) of length 256
    return max(0, x[137])
def l154_201(x):
    # x is a list (or vector) of length 256
    return max(0, x[138])
def l154_202(x):
    # x is a list (or vector) of length 256
    return max(0, x[139])
def l154_203(x):
    # x is a list (or vector) of length 256
    return max(0, x[140])
def l154_204(x):
    # x is a list (or vector) of length 256
    return max(0, x[141])
def l154_205(x):
    # x is a list (or vector) of length 256
    return max(0, x[142])
def l154_206(x):
    # x is a list (or vector) of length 256
    return max(0, x[143])
def l154_207(x):
    # x is a list (or vector) of length 256
    return max(0, x[144])
def l154_208(x):
    # x is a list (or vector) of length 256
    return max(0, x[145])
def l154_209(x):
    # x is a list (or vector) of length 256
    return max(0, x[146])
def l154_210(x):
    # x is a list (or vector) of length 256
    return max(0, x[147])
def l154_211(x):
    # x is a list (or vector) of length 256
    return max(0, x[148])
def l154_212(x):
    # x is a list (or vector) of length 256
    return max(0, x[149])
def l154_213(x):
    # x is a list (or vector) of length 256
    return max(0, x[150])
def l154_214(x):
    # x is a list (or vector) of length 256
    return max(0, x[151])
def l154_215(x):
    # x is a list (or vector) of length 256
    return max(0, x[152])
def l154_216(x):
    # x is a list (or vector) of length 256
    return max(0, x[153])
def l154_217(x):
    # x is a list (or vector) of length 256
    return max(0, x[154])
def l154_218(x):
    # x is a list (or vector) of length 256
    return max(0, x[155])
def l154_219(x):
    # x is a list (or vector) of length 256
    return max(0, x[156])
def l154_220(x):
    # x is a list (or vector) of length 256
    return max(0, x[157])
def l154_221(x):
    # x is a list (or vector) of length 256
    return max(0, x[158])
def l154_222(x):
    # x is a list (or vector) of length 256
    return max(0, x[159])
def l154_223(x):
    # x is a list (or vector) of length 256
    return max(0, x[160])
def l154_224(x):
    # x is a list (or vector) of length 256
    return max(0, x[161])
def l154_225(x):
    # x is a list (or vector) of length 256
    return max(0, x[162])
def l154_226(x):
    # x is a list (or vector) of length 256
    return max(0, x[163])
def l154_227(x):
    # x is a list (or vector) of length 256
    return max(0, x[164])
def l154_228(x):
    # x is a list (or vector) of length 256
    return max(0, x[165])
def l154_229(x):
    # x is a list (or vector) of length 256
    return max(0, x[166])
def l154_230(x):
    # x is a list (or vector) of length 256
    return max(0, x[167])
def l154_231(x):
    # x is a list (or vector) of length 256
    return max(0, x[168])
def l154_232(x):
    # x is a list (or vector) of length 256
    return max(0, x[169])
def l154_233(x):
    # x is a list (or vector) of length 256
    return max(0, x[170])
def l154_234(x):
    # x is a list (or vector) of length 256
    return max(0, x[171])
def l154_235(x):
    # x is a list (or vector) of length 256
    return max(0, x[172])
def l154_236(x):
    # x is a list (or vector) of length 256
    return max(0, x[173])
def l154_237(x):
    # x is a list (or vector) of length 256
    return max(0, x[174])
def l154_238(x):
    # x is a list (or vector) of length 256
    return max(0, x[175])
def l154_239(x):
    # x is a list (or vector) of length 256
    return max(0, x[176])
def l154_240(x):
    # x is a list (or vector) of length 256
    return max(0, x[177])
def l154_241(x):
    # x is a list (or vector) of length 256
    return max(0, x[178])
def l154_242(x):
    # x is a list (or vector) of length 256
    return max(0, x[179])
def l154_243(x):
    # x is a list (or vector) of length 256
    return max(0, x[180])
def l154_244(x):
    # x is a list (or vector) of length 256
    return max(0, x[181])
def l154_245(x):
    # x is a list (or vector) of length 256
    return max(0, x[182])
def l154_246(x):
    # x is a list (or vector) of length 256
    return max(0, x[183])
def l154_247(x):
    # x is a list (or vector) of length 256
    return max(0, x[184])
def l154_248(x):
    # x is a list (or vector) of length 256
    return max(0, x[185])
def l154_249(x):
    # x is a list (or vector) of length 256
    return max(0, x[186])
def l154_250(x):
    # x is a list (or vector) of length 256
    return max(0, x[187])
def l154_251(x):
    # x is a list (or vector) of length 256
    return max(0, x[188])
def l154_252(x):
    # x is a list (or vector) of length 256
    return max(0, x[189])
def l154_253(x):
    # x is a list (or vector) of length 256
    return max(0, x[190])
def l154_254(x):
    # x is a list (or vector) of length 256
    return max(0, x[191])
def l154_255(x):
    # x is a list (or vector) of length 256
    return max(0, x[192])
def l154_256(x):
    # x is a list (or vector) of length 256
    return max(0, x[193])
def l154_257(x):
    # x is a list (or vector) of length 256
    return max(0, x[194])
def l154_258(x):
    # x is a list (or vector) of length 256
    return max(0, x[195])
def l154_259(x):
    # x is a list (or vector) of length 256
    return max(0, x[196])
def l154_260(x):
    # x is a list (or vector) of length 256
    return max(0, x[197])
def l154_261(x):
    # x is a list (or vector) of length 256
    return max(0, x[198])
def l154_262(x):
    # x is a list (or vector) of length 256
    return max(0, x[199])
def l154_263(x):
    # x is a list (or vector) of length 256
    return max(0, x[200])
def l154_264(x):
    # x is a list (or vector) of length 256
    return max(0, x[201])
def l154_265(x):
    # x is a list (or vector) of length 256
    return max(0, x[202])
def l154_266(x):
    # x is a list (or vector) of length 256
    return max(0, x[203])
def l154_267(x):
    # x is a list (or vector) of length 256
    return max(0, x[204])
def l154_268(x):
    # x is a list (or vector) of length 256
    return max(0, x[205])
def l154_269(x):
    # x is a list (or vector) of length 256
    return max(0, x[206])
def l154_270(x):
    # x is a list (or vector) of length 256
    return max(0, x[207])
def l154_271(x):
    # x is a list (or vector) of length 256
    return max(0, x[208])
def l154_272(x):
    # x is a list (or vector) of length 256
    return max(0, x[209])
def l154_273(x):
    # x is a list (or vector) of length 256
    return max(0, x[210])
def l154_274(x):
    # x is a list (or vector) of length 256
    return max(0, x[211])
def l154_275(x):
    # x is a list (or vector) of length 256
    return max(0, x[212])
def l154_276(x):
    # x is a list (or vector) of length 256
    return max(0, x[213])
def l154_277(x):
    # x is a list (or vector) of length 256
    return max(0, x[214])
def l154_278(x):
    # x is a list (or vector) of length 256
    return max(0, x[215])
def l154_279(x):
    # x is a list (or vector) of length 256
    return max(0, x[216])
def l154_280(x):
    # x is a list (or vector) of length 256
    return max(0, x[217])
def l154_281(x):
    # x is a list (or vector) of length 256
    return max(0, x[218])
def l154_282(x):
    # x is a list (or vector) of length 256
    return max(0, x[219])
def l154_283(x):
    # x is a list (or vector) of length 256
    return max(0, x[220])
def l154_284(x):
    # x is a list (or vector) of length 256
    return max(0, x[221])
def l154_285(x):
    # x is a list (or vector) of length 256
    return max(0, x[222])
def l154_286(x):
    # x is a list (or vector) of length 256
    return max(0, x[223])
def l154_287(x):
    # x is a list (or vector) of length 256
    return max(0, x[224])
def l154_288(x):
    # x is a list (or vector) of length 256
    return max(0, x[225])
def l154_289(x):
    # x is a list (or vector) of length 256
    return max(0, x[226])
def l154_290(x):
    # x is a list (or vector) of length 256
    return max(0, x[227])
def l154_291(x):
    # x is a list (or vector) of length 256
    return max(0, x[228])
def l154_292(x):
    # x is a list (or vector) of length 256
    return max(0, x[229])
def l154_293(x):
    # x is a list (or vector) of length 256
    return max(0, x[230])
def l154_294(x):
    # x is a list (or vector) of length 256
    return max(0, x[231])
def l154_295(x):
    # x is a list (or vector) of length 256
    return max(0, x[232])
def l154_296(x):
    # x is a list (or vector) of length 256
    return max(0, x[233])
def l154_297(x):
    # x is a list (or vector) of length 256
    return max(0, x[234])
def l154_298(x):
    # x is a list (or vector) of length 256
    return max(0, x[235])
def l154_299(x):
    # x is a list (or vector) of length 256
    return max(0, x[236])
def l154_300(x):
    # x is a list (or vector) of length 256
    return max(0, x[237])
def l154_301(x):
    # x is a list (or vector) of length 256
    return max(0, x[238])
def l154_302(x):
    # x is a list (or vector) of length 256
    return max(0, x[239])
def l154_303(x):
    # x is a list (or vector) of length 256
    return max(0, x[240])
def l154_304(x):
    # x is a list (or vector) of length 256
    return max(0, x[241])
def l154_305(x):
    # x is a list (or vector) of length 256
    return max(0, x[242])
def l154_306(x):
    # x is a list (or vector) of length 256
    return max(0, x[243])
def l154_307(x):
    # x is a list (or vector) of length 256
    return max(0, x[244])
def l154_308(x):
    # x is a list (or vector) of length 256
    return max(0, x[245])
def l154_309(x):
    # x is a list (or vector) of length 256
    return max(0, x[246])
def l154_310(x):
    # x is a list (or vector) of length 256
    return max(0, x[247])
def l154_311(x):
    # x is a list (or vector) of length 256
    return max(0, x[248])
def l154_312(x):
    # x is a list (or vector) of length 256
    return max(0, x[249])
def l154_313(x):
    # x is a list (or vector) of length 256
    return max(0, x[250])
def l154_314(x):
    # x is a list (or vector) of length 256
    return max(0, x[251])
def l154_315(x):
    # x is a list (or vector) of length 256
    return max(0, x[252])
def l154_316(x):
    # x is a list (or vector) of length 256
    return max(0, x[253])
def l154_317(x):
    # x is a list (or vector) of length 256
    return max(0, x[254])
def l154_318(x):
    # x is a list (or vector) of length 256
    return max(0, x[255])
def l154_(x):
    # x is a list (or vector) of length 256
    return [
        l154_0(x),
        l154_1(x),
        l154_2(x),
        l154_3(x),
        l154_4(x),
        l154_5(x),
        l154_6(x),
        l154_7(x),
        l154_8(x),
        l154_9(x),
        l154_10(x),
        l154_11(x),
        l154_12(x),
        l154_13(x),
        l154_14(x),
        l154_15(x),
        l154_16(x),
        l154_17(x),
        l154_18(x),
        l154_19(x),
        l154_20(x),
        l154_21(x),
        l154_22(x),
        l154_23(x),
        l154_24(x),
        l154_25(x),
        l154_26(x),
        l154_27(x),
        l154_28(x),
        l154_29(x),
        l154_30(x),
        l154_31(x),
        l154_32(x),
        l154_33(x),
        l154_34(x),
        l154_35(x),
        l154_36(x),
        l154_37(x),
        l154_38(x),
        l154_39(x),
        l154_40(x),
        l154_41(x),
        l154_42(x),
        l154_43(x),
        l154_44(x),
        l154_45(x),
        l154_46(x),
        l154_47(x),
        l154_48(x),
        l154_49(x),
        l154_50(x),
        l154_51(x),
        l154_52(x),
        l154_53(x),
        l154_54(x),
        l154_55(x),
        l154_56(x),
        l154_57(x),
        l154_58(x),
        l154_59(x),
        l154_60(x),
        l154_61(x),
        l154_62(x),
        l154_63(x),
        l154_64(x),
        l154_65(x),
        l154_66(x),
        l154_67(x),
        l154_68(x),
        l154_69(x),
        l154_70(x),
        l154_71(x),
        l154_72(x),
        l154_73(x),
        l154_74(x),
        l154_75(x),
        l154_76(x),
        l154_77(x),
        l154_78(x),
        l154_79(x),
        l154_80(x),
        l154_81(x),
        l154_82(x),
        l154_83(x),
        l154_84(x),
        l154_85(x),
        l154_86(x),
        l154_87(x),
        l154_88(x),
        l154_89(x),
        l154_90(x),
        l154_91(x),
        l154_92(x),
        l154_93(x),
        l154_94(x),
        l154_95(x),
        l154_96(x),
        l154_97(x),
        l154_98(x),
        l154_99(x),
        l154_100(x),
        l154_101(x),
        l154_102(x),
        l154_103(x),
        l154_104(x),
        l154_105(x),
        l154_106(x),
        l154_107(x),
        l154_108(x),
        l154_109(x),
        l154_110(x),
        l154_111(x),
        l154_112(x),
        l154_113(x),
        l154_114(x),
        l154_115(x),
        l154_116(x),
        l154_117(x),
        l154_118(x),
        l154_119(x),
        l154_120(x),
        l154_121(x),
        l154_122(x),
        l154_123(x),
        l154_124(x),
        l154_125(x),
        l154_126(x),
        l154_127(x),
        l154_128(x),
        l154_129(x),
        l154_130(x),
        l154_131(x),
        l154_132(x),
        l154_133(x),
        l154_134(x),
        l154_135(x),
        l154_136(x),
        l154_137(x),
        l154_138(x),
        l154_139(x),
        l154_140(x),
        l154_141(x),
        l154_142(x),
        l154_143(x),
        l154_144(x),
        l154_145(x),
        l154_146(x),
        l154_147(x),
        l154_148(x),
        l154_149(x),
        l154_150(x),
        l154_151(x),
        l154_152(x),
        l154_153(x),
        l154_154(x),
        l154_155(x),
        l154_156(x),
        l154_157(x),
        l154_158(x),
        l154_159(x),
        l154_160(x),
        l154_161(x),
        l154_162(x),
        l154_163(x),
        l154_164(x),
        l154_165(x),
        l154_166(x),
        l154_167(x),
        l154_168(x),
        l154_169(x),
        l154_170(x),
        l154_171(x),
        l154_172(x),
        l154_173(x),
        l154_174(x),
        l154_175(x),
        l154_176(x),
        l154_177(x),
        l154_178(x),
        l154_179(x),
        l154_180(x),
        l154_181(x),
        l154_182(x),
        l154_183(x),
        l154_184(x),
        l154_185(x),
        l154_186(x),
        l154_187(x),
        l154_188(x),
        l154_189(x),
        l154_190(x),
        l154_191(x),
        l154_192(x),
        l154_193(x),
        l154_194(x),
        l154_195(x),
        l154_196(x),
        l154_197(x),
        l154_198(x),
        l154_199(x),
        l154_200(x),
        l154_201(x),
        l154_202(x),
        l154_203(x),
        l154_204(x),
        l154_205(x),
        l154_206(x),
        l154_207(x),
        l154_208(x),
        l154_209(x),
        l154_210(x),
        l154_211(x),
        l154_212(x),
        l154_213(x),
        l154_214(x),
        l154_215(x),
        l154_216(x),
        l154_217(x),
        l154_218(x),
        l154_219(x),
        l154_220(x),
        l154_221(x),
        l154_222(x),
        l154_223(x),
        l154_224(x),
        l154_225(x),
        l154_226(x),
        l154_227(x),
        l154_228(x),
        l154_229(x),
        l154_230(x),
        l154_231(x),
        l154_232(x),
        l154_233(x),
        l154_234(x),
        l154_235(x),
        l154_236(x),
        l154_237(x),
        l154_238(x),
        l154_239(x),
        l154_240(x),
        l154_241(x),
        l154_242(x),
        l154_243(x),
        l154_244(x),
        l154_245(x),
        l154_246(x),
        l154_247(x),
        l154_248(x),
        l154_249(x),
        l154_250(x),
        l154_251(x),
        l154_252(x),
        l154_253(x),
        l154_254(x),
        l154_255(x),
        l154_256(x),
        l154_257(x),
        l154_258(x),
        l154_259(x),
        l154_260(x),
        l154_261(x),
        l154_262(x),
        l154_263(x),
        l154_264(x),
        l154_265(x),
        l154_266(x),
        l154_267(x),
        l154_268(x),
        l154_269(x),
        l154_270(x),
        l154_271(x),
        l154_272(x),
        l154_273(x),
        l154_274(x),
        l154_275(x),
        l154_276(x),
        l154_277(x),
        l154_278(x),
        l154_279(x),
        l154_280(x),
        l154_281(x),
        l154_282(x),
        l154_283(x),
        l154_284(x),
        l154_285(x),
        l154_286(x),
        l154_287(x),
        l154_288(x),
        l154_289(x),
        l154_290(x),
        l154_291(x),
        l154_292(x),
        l154_293(x),
        l154_294(x),
        l154_295(x),
        l154_296(x),
        l154_297(x),
        l154_298(x),
        l154_299(x),
        l154_300(x),
        l154_301(x),
        l154_302(x),
        l154_303(x),
        l154_304(x),
        l154_305(x),
        l154_306(x),
        l154_307(x),
        l154_308(x),
        l154_309(x),
        l154_310(x),
        l154_311(x),
        l154_312(x),
        l154_313(x),
        l154_314(x),
        l154_315(x),
        l154_316(x),
        l154_317(x),
        l154_318(x),
    ]