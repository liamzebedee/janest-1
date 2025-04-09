import numpy as np




# Generated from reverse engineering
def l206_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 340
    out = np.empty(340, dtype=np.float32)
    
    # for i in range(0, 96):
    for i in range(0, 96):
        s = x[32 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffffffff (len=32)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(96, 128):
    for i in range(0, 32):
        s = -1 * x[128 + i]
        s += biases[i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 160):
    for i in range(0, 32):
        s = x[0 + i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(160, 192):
    for i in range(0, 32):
        s = x[160 + i] + x[192 + i]
        s += biases[i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(192, 224):
    for i in range(0, 32):
        s = x[160 + i] + x[192 + i]
        out[192 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(224, 256):
    for i in range(0, 32):
        s = x[160 + i] + x[192 + i]
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(256, 260):
    for i in range(0, 4):
        s = x[224 + i]
        out[256 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [64.0, 64.0, 64.0, 64.0]
    # for i in range(260, 264):
    for i in range(0, 4):
        s = -1 * x[228 + i]
        s += biases[i]
        out[260 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(264, 268):
    for i in range(0, 4):
        s = x[228 + i]
        out[264 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-63.0, -63.0, -63.0, -63.0]
    # for i in range(268, 272):
    for i in range(0, 4):
        s = x[228 + i]
        s += biases[i]
        out[268 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-64.0, -64.0, -64.0, -64.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    # for i in range(272, 340):
    for i in range(0, 68):
        s = x[228 + i]
        s += biases[i]
        out[272 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l206_0(x):
    # x is a list (or vector) of length 296
    return max(0, x[32])
def l206_1(x):
    # x is a list (or vector) of length 296
    return max(0, x[33])
def l206_2(x):
    # x is a list (or vector) of length 296
    return max(0, x[34])
def l206_3(x):
    # x is a list (or vector) of length 296
    return max(0, x[35])
def l206_4(x):
    # x is a list (or vector) of length 296
    return max(0, x[36])
def l206_5(x):
    # x is a list (or vector) of length 296
    return max(0, x[37])
def l206_6(x):
    # x is a list (or vector) of length 296
    return max(0, x[38])
def l206_7(x):
    # x is a list (or vector) of length 296
    return max(0, x[39])
def l206_8(x):
    # x is a list (or vector) of length 296
    return max(0, x[40])
def l206_9(x):
    # x is a list (or vector) of length 296
    return max(0, x[41])
def l206_10(x):
    # x is a list (or vector) of length 296
    return max(0, x[42])
def l206_11(x):
    # x is a list (or vector) of length 296
    return max(0, x[43])
def l206_12(x):
    # x is a list (or vector) of length 296
    return max(0, x[44])
def l206_13(x):
    # x is a list (or vector) of length 296
    return max(0, x[45])
def l206_14(x):
    # x is a list (or vector) of length 296
    return max(0, x[46])
def l206_15(x):
    # x is a list (or vector) of length 296
    return max(0, x[47])
def l206_16(x):
    # x is a list (or vector) of length 296
    return max(0, x[48])
def l206_17(x):
    # x is a list (or vector) of length 296
    return max(0, x[49])
def l206_18(x):
    # x is a list (or vector) of length 296
    return max(0, x[50])
def l206_19(x):
    # x is a list (or vector) of length 296
    return max(0, x[51])
def l206_20(x):
    # x is a list (or vector) of length 296
    return max(0, x[52])
def l206_21(x):
    # x is a list (or vector) of length 296
    return max(0, x[53])
def l206_22(x):
    # x is a list (or vector) of length 296
    return max(0, x[54])
def l206_23(x):
    # x is a list (or vector) of length 296
    return max(0, x[55])
def l206_24(x):
    # x is a list (or vector) of length 296
    return max(0, x[56])
def l206_25(x):
    # x is a list (or vector) of length 296
    return max(0, x[57])
def l206_26(x):
    # x is a list (or vector) of length 296
    return max(0, x[58])
def l206_27(x):
    # x is a list (or vector) of length 296
    return max(0, x[59])
def l206_28(x):
    # x is a list (or vector) of length 296
    return max(0, x[60])
def l206_29(x):
    # x is a list (or vector) of length 296
    return max(0, x[61])
def l206_30(x):
    # x is a list (or vector) of length 296
    return max(0, x[62])
def l206_31(x):
    # x is a list (or vector) of length 296
    return max(0, x[63])
def l206_32(x):
    # x is a list (or vector) of length 296
    return max(0, x[64])
def l206_33(x):
    # x is a list (or vector) of length 296
    return max(0, x[65])
def l206_34(x):
    # x is a list (or vector) of length 296
    return max(0, x[66])
def l206_35(x):
    # x is a list (or vector) of length 296
    return max(0, x[67])
def l206_36(x):
    # x is a list (or vector) of length 296
    return max(0, x[68])
def l206_37(x):
    # x is a list (or vector) of length 296
    return max(0, x[69])
def l206_38(x):
    # x is a list (or vector) of length 296
    return max(0, x[70])
def l206_39(x):
    # x is a list (or vector) of length 296
    return max(0, x[71])
def l206_40(x):
    # x is a list (or vector) of length 296
    return max(0, x[72])
def l206_41(x):
    # x is a list (or vector) of length 296
    return max(0, x[73])
def l206_42(x):
    # x is a list (or vector) of length 296
    return max(0, x[74])
def l206_43(x):
    # x is a list (or vector) of length 296
    return max(0, x[75])
def l206_44(x):
    # x is a list (or vector) of length 296
    return max(0, x[76])
def l206_45(x):
    # x is a list (or vector) of length 296
    return max(0, x[77])
def l206_46(x):
    # x is a list (or vector) of length 296
    return max(0, x[78])
def l206_47(x):
    # x is a list (or vector) of length 296
    return max(0, x[79])
def l206_48(x):
    # x is a list (or vector) of length 296
    return max(0, x[80])
def l206_49(x):
    # x is a list (or vector) of length 296
    return max(0, x[81])
def l206_50(x):
    # x is a list (or vector) of length 296
    return max(0, x[82])
def l206_51(x):
    # x is a list (or vector) of length 296
    return max(0, x[83])
def l206_52(x):
    # x is a list (or vector) of length 296
    return max(0, x[84])
def l206_53(x):
    # x is a list (or vector) of length 296
    return max(0, x[85])
def l206_54(x):
    # x is a list (or vector) of length 296
    return max(0, x[86])
def l206_55(x):
    # x is a list (or vector) of length 296
    return max(0, x[87])
def l206_56(x):
    # x is a list (or vector) of length 296
    return max(0, x[88])
def l206_57(x):
    # x is a list (or vector) of length 296
    return max(0, x[89])
def l206_58(x):
    # x is a list (or vector) of length 296
    return max(0, x[90])
def l206_59(x):
    # x is a list (or vector) of length 296
    return max(0, x[91])
def l206_60(x):
    # x is a list (or vector) of length 296
    return max(0, x[92])
def l206_61(x):
    # x is a list (or vector) of length 296
    return max(0, x[93])
def l206_62(x):
    # x is a list (or vector) of length 296
    return max(0, x[94])
def l206_63(x):
    # x is a list (or vector) of length 296
    return max(0, x[95])
def l206_64(x):
    # x is a list (or vector) of length 296
    return max(0, x[96])
def l206_65(x):
    # x is a list (or vector) of length 296
    return max(0, x[97])
def l206_66(x):
    # x is a list (or vector) of length 296
    return max(0, x[98])
def l206_67(x):
    # x is a list (or vector) of length 296
    return max(0, x[99])
def l206_68(x):
    # x is a list (or vector) of length 296
    return max(0, x[100])
def l206_69(x):
    # x is a list (or vector) of length 296
    return max(0, x[101])
def l206_70(x):
    # x is a list (or vector) of length 296
    return max(0, x[102])
def l206_71(x):
    # x is a list (or vector) of length 296
    return max(0, x[103])
def l206_72(x):
    # x is a list (or vector) of length 296
    return max(0, x[104])
def l206_73(x):
    # x is a list (or vector) of length 296
    return max(0, x[105])
def l206_74(x):
    # x is a list (or vector) of length 296
    return max(0, x[106])
def l206_75(x):
    # x is a list (or vector) of length 296
    return max(0, x[107])
def l206_76(x):
    # x is a list (or vector) of length 296
    return max(0, x[108])
def l206_77(x):
    # x is a list (or vector) of length 296
    return max(0, x[109])
def l206_78(x):
    # x is a list (or vector) of length 296
    return max(0, x[110])
def l206_79(x):
    # x is a list (or vector) of length 296
    return max(0, x[111])
def l206_80(x):
    # x is a list (or vector) of length 296
    return max(0, x[112])
def l206_81(x):
    # x is a list (or vector) of length 296
    return max(0, x[113])
def l206_82(x):
    # x is a list (or vector) of length 296
    return max(0, x[114])
def l206_83(x):
    # x is a list (or vector) of length 296
    return max(0, x[115])
def l206_84(x):
    # x is a list (or vector) of length 296
    return max(0, x[116])
def l206_85(x):
    # x is a list (or vector) of length 296
    return max(0, x[117])
def l206_86(x):
    # x is a list (or vector) of length 296
    return max(0, x[118])
def l206_87(x):
    # x is a list (or vector) of length 296
    return max(0, x[119])
def l206_88(x):
    # x is a list (or vector) of length 296
    return max(0, x[120])
def l206_89(x):
    # x is a list (or vector) of length 296
    return max(0, x[121])
def l206_90(x):
    # x is a list (or vector) of length 296
    return max(0, x[122])
def l206_91(x):
    # x is a list (or vector) of length 296
    return max(0, x[123])
def l206_92(x):
    # x is a list (or vector) of length 296
    return max(0, x[124])
def l206_93(x):
    # x is a list (or vector) of length 296
    return max(0, x[125])
def l206_94(x):
    # x is a list (or vector) of length 296
    return max(0, x[126])
def l206_95(x):
    # x is a list (or vector) of length 296
    return max(0, x[127])
def l206_96(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[128] + 1.0)
def l206_97(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[129] + 1.0)
def l206_98(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[130] + 1.0)
def l206_99(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[131] + 1.0)
def l206_100(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[132] + 1.0)
def l206_101(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[133] + 1.0)
def l206_102(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[134] + 1.0)
def l206_103(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[135] + 1.0)
def l206_104(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[136] + 1.0)
def l206_105(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[137] + 1.0)
def l206_106(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[138] + 1.0)
def l206_107(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[139] + 1.0)
def l206_108(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[140] + 1.0)
def l206_109(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[141] + 1.0)
def l206_110(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[142] + 1.0)
def l206_111(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[143] + 1.0)
def l206_112(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[144] + 1.0)
def l206_113(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[145] + 1.0)
def l206_114(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[146] + 1.0)
def l206_115(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[147] + 1.0)
def l206_116(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[148] + 1.0)
def l206_117(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[149] + 1.0)
def l206_118(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[150] + 1.0)
def l206_119(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[151] + 1.0)
def l206_120(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[152] + 1.0)
def l206_121(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[153] + 1.0)
def l206_122(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[154] + 1.0)
def l206_123(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[155] + 1.0)
def l206_124(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[156] + 1.0)
def l206_125(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[157] + 1.0)
def l206_126(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[158] + 1.0)
def l206_127(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[159] + 1.0)
def l206_128(x):
    # x is a list (or vector) of length 296
    return max(0, x[0])
def l206_129(x):
    # x is a list (or vector) of length 296
    return max(0, x[1])
def l206_130(x):
    # x is a list (or vector) of length 296
    return max(0, x[2])
def l206_131(x):
    # x is a list (or vector) of length 296
    return max(0, x[3])
def l206_132(x):
    # x is a list (or vector) of length 296
    return max(0, x[4])
def l206_133(x):
    # x is a list (or vector) of length 296
    return max(0, x[5])
def l206_134(x):
    # x is a list (or vector) of length 296
    return max(0, x[6])
def l206_135(x):
    # x is a list (or vector) of length 296
    return max(0, x[7])
def l206_136(x):
    # x is a list (or vector) of length 296
    return max(0, x[8])
def l206_137(x):
    # x is a list (or vector) of length 296
    return max(0, x[9])
def l206_138(x):
    # x is a list (or vector) of length 296
    return max(0, x[10])
def l206_139(x):
    # x is a list (or vector) of length 296
    return max(0, x[11])
def l206_140(x):
    # x is a list (or vector) of length 296
    return max(0, x[12])
def l206_141(x):
    # x is a list (or vector) of length 296
    return max(0, x[13])
def l206_142(x):
    # x is a list (or vector) of length 296
    return max(0, x[14])
def l206_143(x):
    # x is a list (or vector) of length 296
    return max(0, x[15])
def l206_144(x):
    # x is a list (or vector) of length 296
    return max(0, x[16])
def l206_145(x):
    # x is a list (or vector) of length 296
    return max(0, x[17])
def l206_146(x):
    # x is a list (or vector) of length 296
    return max(0, x[18])
def l206_147(x):
    # x is a list (or vector) of length 296
    return max(0, x[19])
def l206_148(x):
    # x is a list (or vector) of length 296
    return max(0, x[20])
def l206_149(x):
    # x is a list (or vector) of length 296
    return max(0, x[21])
def l206_150(x):
    # x is a list (or vector) of length 296
    return max(0, x[22])
def l206_151(x):
    # x is a list (or vector) of length 296
    return max(0, x[23])
def l206_152(x):
    # x is a list (or vector) of length 296
    return max(0, x[24])
def l206_153(x):
    # x is a list (or vector) of length 296
    return max(0, x[25])
def l206_154(x):
    # x is a list (or vector) of length 296
    return max(0, x[26])
def l206_155(x):
    # x is a list (or vector) of length 296
    return max(0, x[27])
def l206_156(x):
    # x is a list (or vector) of length 296
    return max(0, x[28])
def l206_157(x):
    # x is a list (or vector) of length 296
    return max(0, x[29])
def l206_158(x):
    # x is a list (or vector) of length 296
    return max(0, x[30])
def l206_159(x):
    # x is a list (or vector) of length 296
    return max(0, x[31])
def l206_160(x):
    # x is a list (or vector) of length 296
    return max(0, x[160] + x[192] + -1.0)
def l206_161(x):
    # x is a list (or vector) of length 296
    return max(0, x[161] + x[193] + -1.0)
def l206_162(x):
    # x is a list (or vector) of length 296
    return max(0, x[162] + x[194] + -1.0)
def l206_163(x):
    # x is a list (or vector) of length 296
    return max(0, x[163] + x[195] + -1.0)
def l206_164(x):
    # x is a list (or vector) of length 296
    return max(0, x[164] + x[196] + -1.0)
def l206_165(x):
    # x is a list (or vector) of length 296
    return max(0, x[165] + x[197] + -1.0)
def l206_166(x):
    # x is a list (or vector) of length 296
    return max(0, x[166] + x[198] + -1.0)
def l206_167(x):
    # x is a list (or vector) of length 296
    return max(0, x[167] + x[199] + -1.0)
def l206_168(x):
    # x is a list (or vector) of length 296
    return max(0, x[168] + x[200] + -1.0)
def l206_169(x):
    # x is a list (or vector) of length 296
    return max(0, x[169] + x[201] + -1.0)
def l206_170(x):
    # x is a list (or vector) of length 296
    return max(0, x[170] + x[202] + -1.0)
def l206_171(x):
    # x is a list (or vector) of length 296
    return max(0, x[171] + x[203] + -1.0)
def l206_172(x):
    # x is a list (or vector) of length 296
    return max(0, x[172] + x[204] + -1.0)
def l206_173(x):
    # x is a list (or vector) of length 296
    return max(0, x[173] + x[205] + -1.0)
def l206_174(x):
    # x is a list (or vector) of length 296
    return max(0, x[174] + x[206] + -1.0)
def l206_175(x):
    # x is a list (or vector) of length 296
    return max(0, x[175] + x[207] + -1.0)
def l206_176(x):
    # x is a list (or vector) of length 296
    return max(0, x[176] + x[208] + -1.0)
def l206_177(x):
    # x is a list (or vector) of length 296
    return max(0, x[177] + x[209] + -1.0)
def l206_178(x):
    # x is a list (or vector) of length 296
    return max(0, x[178] + x[210] + -1.0)
def l206_179(x):
    # x is a list (or vector) of length 296
    return max(0, x[179] + x[211] + -1.0)
def l206_180(x):
    # x is a list (or vector) of length 296
    return max(0, x[180] + x[212] + -1.0)
def l206_181(x):
    # x is a list (or vector) of length 296
    return max(0, x[181] + x[213] + -1.0)
def l206_182(x):
    # x is a list (or vector) of length 296
    return max(0, x[182] + x[214] + -1.0)
def l206_183(x):
    # x is a list (or vector) of length 296
    return max(0, x[183] + x[215] + -1.0)
def l206_184(x):
    # x is a list (or vector) of length 296
    return max(0, x[184] + x[216] + -1.0)
def l206_185(x):
    # x is a list (or vector) of length 296
    return max(0, x[185] + x[217] + -1.0)
def l206_186(x):
    # x is a list (or vector) of length 296
    return max(0, x[186] + x[218] + -1.0)
def l206_187(x):
    # x is a list (or vector) of length 296
    return max(0, x[187] + x[219] + -1.0)
def l206_188(x):
    # x is a list (or vector) of length 296
    return max(0, x[188] + x[220] + -1.0)
def l206_189(x):
    # x is a list (or vector) of length 296
    return max(0, x[189] + x[221] + -1.0)
def l206_190(x):
    # x is a list (or vector) of length 296
    return max(0, x[190] + x[222] + -1.0)
def l206_191(x):
    # x is a list (or vector) of length 296
    return max(0, x[191] + x[223] + -1.0)
def l206_192(x):
    # x is a list (or vector) of length 296
    return max(0, x[160] + x[192])
def l206_193(x):
    # x is a list (or vector) of length 296
    return max(0, x[161] + x[193])
def l206_194(x):
    # x is a list (or vector) of length 296
    return max(0, x[162] + x[194])
def l206_195(x):
    # x is a list (or vector) of length 296
    return max(0, x[163] + x[195])
def l206_196(x):
    # x is a list (or vector) of length 296
    return max(0, x[164] + x[196])
def l206_197(x):
    # x is a list (or vector) of length 296
    return max(0, x[165] + x[197])
def l206_198(x):
    # x is a list (or vector) of length 296
    return max(0, x[166] + x[198])
def l206_199(x):
    # x is a list (or vector) of length 296
    return max(0, x[167] + x[199])
def l206_200(x):
    # x is a list (or vector) of length 296
    return max(0, x[168] + x[200])
def l206_201(x):
    # x is a list (or vector) of length 296
    return max(0, x[169] + x[201])
def l206_202(x):
    # x is a list (or vector) of length 296
    return max(0, x[170] + x[202])
def l206_203(x):
    # x is a list (or vector) of length 296
    return max(0, x[171] + x[203])
def l206_204(x):
    # x is a list (or vector) of length 296
    return max(0, x[172] + x[204])
def l206_205(x):
    # x is a list (or vector) of length 296
    return max(0, x[173] + x[205])
def l206_206(x):
    # x is a list (or vector) of length 296
    return max(0, x[174] + x[206])
def l206_207(x):
    # x is a list (or vector) of length 296
    return max(0, x[175] + x[207])
def l206_208(x):
    # x is a list (or vector) of length 296
    return max(0, x[176] + x[208])
def l206_209(x):
    # x is a list (or vector) of length 296
    return max(0, x[177] + x[209])
def l206_210(x):
    # x is a list (or vector) of length 296
    return max(0, x[178] + x[210])
def l206_211(x):
    # x is a list (or vector) of length 296
    return max(0, x[179] + x[211])
def l206_212(x):
    # x is a list (or vector) of length 296
    return max(0, x[180] + x[212])
def l206_213(x):
    # x is a list (or vector) of length 296
    return max(0, x[181] + x[213])
def l206_214(x):
    # x is a list (or vector) of length 296
    return max(0, x[182] + x[214])
def l206_215(x):
    # x is a list (or vector) of length 296
    return max(0, x[183] + x[215])
def l206_216(x):
    # x is a list (or vector) of length 296
    return max(0, x[184] + x[216])
def l206_217(x):
    # x is a list (or vector) of length 296
    return max(0, x[185] + x[217])
def l206_218(x):
    # x is a list (or vector) of length 296
    return max(0, x[186] + x[218])
def l206_219(x):
    # x is a list (or vector) of length 296
    return max(0, x[187] + x[219])
def l206_220(x):
    # x is a list (or vector) of length 296
    return max(0, x[188] + x[220])
def l206_221(x):
    # x is a list (or vector) of length 296
    return max(0, x[189] + x[221])
def l206_222(x):
    # x is a list (or vector) of length 296
    return max(0, x[190] + x[222])
def l206_223(x):
    # x is a list (or vector) of length 296
    return max(0, x[191] + x[223])
def l206_224(x):
    # x is a list (or vector) of length 296
    return max(0, x[160] + x[192] + -1.0)
def l206_225(x):
    # x is a list (or vector) of length 296
    return max(0, x[161] + x[193] + -1.0)
def l206_226(x):
    # x is a list (or vector) of length 296
    return max(0, x[162] + x[194] + -1.0)
def l206_227(x):
    # x is a list (or vector) of length 296
    return max(0, x[163] + x[195] + -1.0)
def l206_228(x):
    # x is a list (or vector) of length 296
    return max(0, x[164] + x[196] + -1.0)
def l206_229(x):
    # x is a list (or vector) of length 296
    return max(0, x[165] + x[197] + -1.0)
def l206_230(x):
    # x is a list (or vector) of length 296
    return max(0, x[166] + x[198] + -1.0)
def l206_231(x):
    # x is a list (or vector) of length 296
    return max(0, x[167] + x[199] + -1.0)
def l206_232(x):
    # x is a list (or vector) of length 296
    return max(0, x[168] + x[200] + -1.0)
def l206_233(x):
    # x is a list (or vector) of length 296
    return max(0, x[169] + x[201] + -1.0)
def l206_234(x):
    # x is a list (or vector) of length 296
    return max(0, x[170] + x[202] + -1.0)
def l206_235(x):
    # x is a list (or vector) of length 296
    return max(0, x[171] + x[203] + -1.0)
def l206_236(x):
    # x is a list (or vector) of length 296
    return max(0, x[172] + x[204] + -1.0)
def l206_237(x):
    # x is a list (or vector) of length 296
    return max(0, x[173] + x[205] + -1.0)
def l206_238(x):
    # x is a list (or vector) of length 296
    return max(0, x[174] + x[206] + -1.0)
def l206_239(x):
    # x is a list (or vector) of length 296
    return max(0, x[175] + x[207] + -1.0)
def l206_240(x):
    # x is a list (or vector) of length 296
    return max(0, x[176] + x[208] + -1.0)
def l206_241(x):
    # x is a list (or vector) of length 296
    return max(0, x[177] + x[209] + -1.0)
def l206_242(x):
    # x is a list (or vector) of length 296
    return max(0, x[178] + x[210] + -1.0)
def l206_243(x):
    # x is a list (or vector) of length 296
    return max(0, x[179] + x[211] + -1.0)
def l206_244(x):
    # x is a list (or vector) of length 296
    return max(0, x[180] + x[212] + -1.0)
def l206_245(x):
    # x is a list (or vector) of length 296
    return max(0, x[181] + x[213] + -1.0)
def l206_246(x):
    # x is a list (or vector) of length 296
    return max(0, x[182] + x[214] + -1.0)
def l206_247(x):
    # x is a list (or vector) of length 296
    return max(0, x[183] + x[215] + -1.0)
def l206_248(x):
    # x is a list (or vector) of length 296
    return max(0, x[184] + x[216] + -1.0)
def l206_249(x):
    # x is a list (or vector) of length 296
    return max(0, x[185] + x[217] + -1.0)
def l206_250(x):
    # x is a list (or vector) of length 296
    return max(0, x[186] + x[218] + -1.0)
def l206_251(x):
    # x is a list (or vector) of length 296
    return max(0, x[187] + x[219] + -1.0)
def l206_252(x):
    # x is a list (or vector) of length 296
    return max(0, x[188] + x[220] + -1.0)
def l206_253(x):
    # x is a list (or vector) of length 296
    return max(0, x[189] + x[221] + -1.0)
def l206_254(x):
    # x is a list (or vector) of length 296
    return max(0, x[190] + x[222] + -1.0)
def l206_255(x):
    # x is a list (or vector) of length 296
    return max(0, x[191] + x[223] + -1.0)
def l206_256(x):
    # x is a list (or vector) of length 296
    return max(0, x[224])
def l206_257(x):
    # x is a list (or vector) of length 296
    return max(0, x[225])
def l206_258(x):
    # x is a list (or vector) of length 296
    return max(0, x[226])
def l206_259(x):
    # x is a list (or vector) of length 296
    return max(0, x[227])
def l206_260(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[228] + 64.0)
def l206_261(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[229] + 64.0)
def l206_262(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[230] + 64.0)
def l206_263(x):
    # x is a list (or vector) of length 296
    return max(0, -1.0*x[231] + 64.0)
def l206_264(x):
    # x is a list (or vector) of length 296
    return max(0, x[228])
def l206_265(x):
    # x is a list (or vector) of length 296
    return max(0, x[229])
def l206_266(x):
    # x is a list (or vector) of length 296
    return max(0, x[230])
def l206_267(x):
    # x is a list (or vector) of length 296
    return max(0, x[231])
def l206_268(x):
    # x is a list (or vector) of length 296
    return max(0, x[228] + -63.0)
def l206_269(x):
    # x is a list (or vector) of length 296
    return max(0, x[229] + -63.0)
def l206_270(x):
    # x is a list (or vector) of length 296
    return max(0, x[230] + -63.0)
def l206_271(x):
    # x is a list (or vector) of length 296
    return max(0, x[231] + -63.0)
def l206_272(x):
    # x is a list (or vector) of length 296
    return max(0, x[228] + -64.0)
def l206_273(x):
    # x is a list (or vector) of length 296
    return max(0, x[229] + -64.0)
def l206_274(x):
    # x is a list (or vector) of length 296
    return max(0, x[230] + -64.0)
def l206_275(x):
    # x is a list (or vector) of length 296
    return max(0, x[231] + -64.0)
def l206_276(x):
    # x is a list (or vector) of length 296
    return max(0, x[232])
def l206_277(x):
    # x is a list (or vector) of length 296
    return max(0, x[233])
def l206_278(x):
    # x is a list (or vector) of length 296
    return max(0, x[234])
def l206_279(x):
    # x is a list (or vector) of length 296
    return max(0, x[235])
def l206_280(x):
    # x is a list (or vector) of length 296
    return max(0, x[236])
def l206_281(x):
    # x is a list (or vector) of length 296
    return max(0, x[237])
def l206_282(x):
    # x is a list (or vector) of length 296
    return max(0, x[238])
def l206_283(x):
    # x is a list (or vector) of length 296
    return max(0, x[239])
def l206_284(x):
    # x is a list (or vector) of length 296
    return max(0, x[240])
def l206_285(x):
    # x is a list (or vector) of length 296
    return max(0, x[241])
def l206_286(x):
    # x is a list (or vector) of length 296
    return max(0, x[242])
def l206_287(x):
    # x is a list (or vector) of length 296
    return max(0, x[243])
def l206_288(x):
    # x is a list (or vector) of length 296
    return max(0, x[244])
def l206_289(x):
    # x is a list (or vector) of length 296
    return max(0, x[245])
def l206_290(x):
    # x is a list (or vector) of length 296
    return max(0, x[246])
def l206_291(x):
    # x is a list (or vector) of length 296
    return max(0, x[247])
def l206_292(x):
    # x is a list (or vector) of length 296
    return max(0, x[248])
def l206_293(x):
    # x is a list (or vector) of length 296
    return max(0, x[249])
def l206_294(x):
    # x is a list (or vector) of length 296
    return max(0, x[250])
def l206_295(x):
    # x is a list (or vector) of length 296
    return max(0, x[251])
def l206_296(x):
    # x is a list (or vector) of length 296
    return max(0, x[252])
def l206_297(x):
    # x is a list (or vector) of length 296
    return max(0, x[253])
def l206_298(x):
    # x is a list (or vector) of length 296
    return max(0, x[254])
def l206_299(x):
    # x is a list (or vector) of length 296
    return max(0, x[255])
def l206_300(x):
    # x is a list (or vector) of length 296
    return max(0, x[256])
def l206_301(x):
    # x is a list (or vector) of length 296
    return max(0, x[257])
def l206_302(x):
    # x is a list (or vector) of length 296
    return max(0, x[258])
def l206_303(x):
    # x is a list (or vector) of length 296
    return max(0, x[259])
def l206_304(x):
    # x is a list (or vector) of length 296
    return max(0, x[260])
def l206_305(x):
    # x is a list (or vector) of length 296
    return max(0, x[261])
def l206_306(x):
    # x is a list (or vector) of length 296
    return max(0, x[262])
def l206_307(x):
    # x is a list (or vector) of length 296
    return max(0, x[263])
def l206_308(x):
    # x is a list (or vector) of length 296
    return max(0, x[264])
def l206_309(x):
    # x is a list (or vector) of length 296
    return max(0, x[265])
def l206_310(x):
    # x is a list (or vector) of length 296
    return max(0, x[266])
def l206_311(x):
    # x is a list (or vector) of length 296
    return max(0, x[267])
def l206_312(x):
    # x is a list (or vector) of length 296
    return max(0, x[268])
def l206_313(x):
    # x is a list (or vector) of length 296
    return max(0, x[269])
def l206_314(x):
    # x is a list (or vector) of length 296
    return max(0, x[270])
def l206_315(x):
    # x is a list (or vector) of length 296
    return max(0, x[271])
def l206_316(x):
    # x is a list (or vector) of length 296
    return max(0, x[272])
def l206_317(x):
    # x is a list (or vector) of length 296
    return max(0, x[273])
def l206_318(x):
    # x is a list (or vector) of length 296
    return max(0, x[274])
def l206_319(x):
    # x is a list (or vector) of length 296
    return max(0, x[275])
def l206_320(x):
    # x is a list (or vector) of length 296
    return max(0, x[276])
def l206_321(x):
    # x is a list (or vector) of length 296
    return max(0, x[277])
def l206_322(x):
    # x is a list (or vector) of length 296
    return max(0, x[278])
def l206_323(x):
    # x is a list (or vector) of length 296
    return max(0, x[279])
def l206_324(x):
    # x is a list (or vector) of length 296
    return max(0, x[280])
def l206_325(x):
    # x is a list (or vector) of length 296
    return max(0, x[281])
def l206_326(x):
    # x is a list (or vector) of length 296
    return max(0, x[282])
def l206_327(x):
    # x is a list (or vector) of length 296
    return max(0, x[283])
def l206_328(x):
    # x is a list (or vector) of length 296
    return max(0, x[284])
def l206_329(x):
    # x is a list (or vector) of length 296
    return max(0, x[285])
def l206_330(x):
    # x is a list (or vector) of length 296
    return max(0, x[286])
def l206_331(x):
    # x is a list (or vector) of length 296
    return max(0, x[287])
def l206_332(x):
    # x is a list (or vector) of length 296
    return max(0, x[288])
def l206_333(x):
    # x is a list (or vector) of length 296
    return max(0, x[289])
def l206_334(x):
    # x is a list (or vector) of length 296
    return max(0, x[290])
def l206_335(x):
    # x is a list (or vector) of length 296
    return max(0, x[291])
def l206_336(x):
    # x is a list (or vector) of length 296
    return max(0, x[292])
def l206_337(x):
    # x is a list (or vector) of length 296
    return max(0, x[293])
def l206_338(x):
    # x is a list (or vector) of length 296
    return max(0, x[294])
def l206_339(x):
    # x is a list (or vector) of length 296
    return max(0, x[295])
def l206_(x):
    # x is a list (or vector) of length 296
    return [
        l206_0(x),
        l206_1(x),
        l206_2(x),
        l206_3(x),
        l206_4(x),
        l206_5(x),
        l206_6(x),
        l206_7(x),
        l206_8(x),
        l206_9(x),
        l206_10(x),
        l206_11(x),
        l206_12(x),
        l206_13(x),
        l206_14(x),
        l206_15(x),
        l206_16(x),
        l206_17(x),
        l206_18(x),
        l206_19(x),
        l206_20(x),
        l206_21(x),
        l206_22(x),
        l206_23(x),
        l206_24(x),
        l206_25(x),
        l206_26(x),
        l206_27(x),
        l206_28(x),
        l206_29(x),
        l206_30(x),
        l206_31(x),
        l206_32(x),
        l206_33(x),
        l206_34(x),
        l206_35(x),
        l206_36(x),
        l206_37(x),
        l206_38(x),
        l206_39(x),
        l206_40(x),
        l206_41(x),
        l206_42(x),
        l206_43(x),
        l206_44(x),
        l206_45(x),
        l206_46(x),
        l206_47(x),
        l206_48(x),
        l206_49(x),
        l206_50(x),
        l206_51(x),
        l206_52(x),
        l206_53(x),
        l206_54(x),
        l206_55(x),
        l206_56(x),
        l206_57(x),
        l206_58(x),
        l206_59(x),
        l206_60(x),
        l206_61(x),
        l206_62(x),
        l206_63(x),
        l206_64(x),
        l206_65(x),
        l206_66(x),
        l206_67(x),
        l206_68(x),
        l206_69(x),
        l206_70(x),
        l206_71(x),
        l206_72(x),
        l206_73(x),
        l206_74(x),
        l206_75(x),
        l206_76(x),
        l206_77(x),
        l206_78(x),
        l206_79(x),
        l206_80(x),
        l206_81(x),
        l206_82(x),
        l206_83(x),
        l206_84(x),
        l206_85(x),
        l206_86(x),
        l206_87(x),
        l206_88(x),
        l206_89(x),
        l206_90(x),
        l206_91(x),
        l206_92(x),
        l206_93(x),
        l206_94(x),
        l206_95(x),
        l206_96(x),
        l206_97(x),
        l206_98(x),
        l206_99(x),
        l206_100(x),
        l206_101(x),
        l206_102(x),
        l206_103(x),
        l206_104(x),
        l206_105(x),
        l206_106(x),
        l206_107(x),
        l206_108(x),
        l206_109(x),
        l206_110(x),
        l206_111(x),
        l206_112(x),
        l206_113(x),
        l206_114(x),
        l206_115(x),
        l206_116(x),
        l206_117(x),
        l206_118(x),
        l206_119(x),
        l206_120(x),
        l206_121(x),
        l206_122(x),
        l206_123(x),
        l206_124(x),
        l206_125(x),
        l206_126(x),
        l206_127(x),
        l206_128(x),
        l206_129(x),
        l206_130(x),
        l206_131(x),
        l206_132(x),
        l206_133(x),
        l206_134(x),
        l206_135(x),
        l206_136(x),
        l206_137(x),
        l206_138(x),
        l206_139(x),
        l206_140(x),
        l206_141(x),
        l206_142(x),
        l206_143(x),
        l206_144(x),
        l206_145(x),
        l206_146(x),
        l206_147(x),
        l206_148(x),
        l206_149(x),
        l206_150(x),
        l206_151(x),
        l206_152(x),
        l206_153(x),
        l206_154(x),
        l206_155(x),
        l206_156(x),
        l206_157(x),
        l206_158(x),
        l206_159(x),
        l206_160(x),
        l206_161(x),
        l206_162(x),
        l206_163(x),
        l206_164(x),
        l206_165(x),
        l206_166(x),
        l206_167(x),
        l206_168(x),
        l206_169(x),
        l206_170(x),
        l206_171(x),
        l206_172(x),
        l206_173(x),
        l206_174(x),
        l206_175(x),
        l206_176(x),
        l206_177(x),
        l206_178(x),
        l206_179(x),
        l206_180(x),
        l206_181(x),
        l206_182(x),
        l206_183(x),
        l206_184(x),
        l206_185(x),
        l206_186(x),
        l206_187(x),
        l206_188(x),
        l206_189(x),
        l206_190(x),
        l206_191(x),
        l206_192(x),
        l206_193(x),
        l206_194(x),
        l206_195(x),
        l206_196(x),
        l206_197(x),
        l206_198(x),
        l206_199(x),
        l206_200(x),
        l206_201(x),
        l206_202(x),
        l206_203(x),
        l206_204(x),
        l206_205(x),
        l206_206(x),
        l206_207(x),
        l206_208(x),
        l206_209(x),
        l206_210(x),
        l206_211(x),
        l206_212(x),
        l206_213(x),
        l206_214(x),
        l206_215(x),
        l206_216(x),
        l206_217(x),
        l206_218(x),
        l206_219(x),
        l206_220(x),
        l206_221(x),
        l206_222(x),
        l206_223(x),
        l206_224(x),
        l206_225(x),
        l206_226(x),
        l206_227(x),
        l206_228(x),
        l206_229(x),
        l206_230(x),
        l206_231(x),
        l206_232(x),
        l206_233(x),
        l206_234(x),
        l206_235(x),
        l206_236(x),
        l206_237(x),
        l206_238(x),
        l206_239(x),
        l206_240(x),
        l206_241(x),
        l206_242(x),
        l206_243(x),
        l206_244(x),
        l206_245(x),
        l206_246(x),
        l206_247(x),
        l206_248(x),
        l206_249(x),
        l206_250(x),
        l206_251(x),
        l206_252(x),
        l206_253(x),
        l206_254(x),
        l206_255(x),
        l206_256(x),
        l206_257(x),
        l206_258(x),
        l206_259(x),
        l206_260(x),
        l206_261(x),
        l206_262(x),
        l206_263(x),
        l206_264(x),
        l206_265(x),
        l206_266(x),
        l206_267(x),
        l206_268(x),
        l206_269(x),
        l206_270(x),
        l206_271(x),
        l206_272(x),
        l206_273(x),
        l206_274(x),
        l206_275(x),
        l206_276(x),
        l206_277(x),
        l206_278(x),
        l206_279(x),
        l206_280(x),
        l206_281(x),
        l206_282(x),
        l206_283(x),
        l206_284(x),
        l206_285(x),
        l206_286(x),
        l206_287(x),
        l206_288(x),
        l206_289(x),
        l206_290(x),
        l206_291(x),
        l206_292(x),
        l206_293(x),
        l206_294(x),
        l206_295(x),
        l206_296(x),
        l206_297(x),
        l206_298(x),
        l206_299(x),
        l206_300(x),
        l206_301(x),
        l206_302(x),
        l206_303(x),
        l206_304(x),
        l206_305(x),
        l206_306(x),
        l206_307(x),
        l206_308(x),
        l206_309(x),
        l206_310(x),
        l206_311(x),
        l206_312(x),
        l206_313(x),
        l206_314(x),
        l206_315(x),
        l206_316(x),
        l206_317(x),
        l206_318(x),
        l206_319(x),
        l206_320(x),
        l206_321(x),
        l206_322(x),
        l206_323(x),
        l206_324(x),
        l206_325(x),
        l206_326(x),
        l206_327(x),
        l206_328(x),
        l206_329(x),
        l206_330(x),
        l206_331(x),
        l206_332(x),
        l206_333(x),
        l206_334(x),
        l206_335(x),
        l206_336(x),
        l206_337(x),
        l206_338(x),
        l206_339(x),
    ]