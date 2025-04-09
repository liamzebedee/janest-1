import numpy as np




# Generated from reverse engineering
def l532_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 304
    out = np.empty(304, dtype=np.float32)
    
    # for i in range(0, 40):
    for i in range(0, 40):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xff (len=8)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(40, 48):
    for i in range(0, 8):
        s = -1 * x[40 + i]
        s += biases[i]
        out[40 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(48, 56):
    for i in range(0, 8):
        s = x[32 + i] + x[80 + i]
        s += biases[i]
        out[48 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(56, 64):
    for i in range(0, 8):
        s = x[88 + i] + -1 * x[40 + i]
        out[56 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffff (len=16)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(64, 80):
    for i in range(0, 16):
        s = -1 * x[48 + i]
        s += biases[i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(80, 96):
    for i in range(0, 16):
        s = x[64 + i] + x[80 + i]
        s += biases[i]
        out[80 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 112):
    for i in range(0, 16):
        s = x[64 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(112, 304):
    for i in range(0, 192):
        s = x[96 + i]
        out[112 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l532_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l532_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l532_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l532_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l532_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l532_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l532_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l532_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l532_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l532_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l532_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l532_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l532_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l532_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l532_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l532_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l532_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l532_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l532_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l532_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l532_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l532_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l532_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l532_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l532_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l532_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l532_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l532_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l532_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l532_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l532_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l532_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l532_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l532_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l532_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l532_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l532_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l532_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l532_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l532_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l532_40(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + 1.0)
def l532_41(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + 1.0)
def l532_42(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + 1.0)
def l532_43(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + 1.0)
def l532_44(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + 1.0)
def l532_45(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + 1.0)
def l532_46(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + 1.0)
def l532_47(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + 1.0)
def l532_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[32] + x[80] + -1.0)
def l532_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[33] + x[81] + -1.0)
def l532_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[34] + x[82] + -1.0)
def l532_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[35] + x[83] + -1.0)
def l532_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[36] + x[84] + -1.0)
def l532_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[37] + x[85] + -1.0)
def l532_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[38] + x[86] + -1.0)
def l532_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[39] + x[87] + -1.0)
def l532_56(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + x[88])
def l532_57(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + x[89])
def l532_58(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + x[90])
def l532_59(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + x[91])
def l532_60(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + x[92])
def l532_61(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + x[93])
def l532_62(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + x[94])
def l532_63(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + x[95])
def l532_64(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + 1.0)
def l532_65(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + 1.0)
def l532_66(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + 1.0)
def l532_67(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + 1.0)
def l532_68(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + 1.0)
def l532_69(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + 1.0)
def l532_70(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + 1.0)
def l532_71(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + 1.0)
def l532_72(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + 1.0)
def l532_73(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + 1.0)
def l532_74(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + 1.0)
def l532_75(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + 1.0)
def l532_76(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + 1.0)
def l532_77(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + 1.0)
def l532_78(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[62] + 1.0)
def l532_79(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[63] + 1.0)
def l532_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[64] + x[80] + -1.0)
def l532_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[65] + x[81] + -1.0)
def l532_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[66] + x[82] + -1.0)
def l532_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[67] + x[83] + -1.0)
def l532_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[68] + x[84] + -1.0)
def l532_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[69] + x[85] + -1.0)
def l532_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[70] + x[86] + -1.0)
def l532_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[71] + x[87] + -1.0)
def l532_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[72] + x[88] + -1.0)
def l532_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[73] + x[89] + -1.0)
def l532_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[74] + x[90] + -1.0)
def l532_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[75] + x[91] + -1.0)
def l532_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[76] + x[92] + -1.0)
def l532_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[77] + x[93] + -1.0)
def l532_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[78] + x[94] + -1.0)
def l532_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[79] + x[95] + -1.0)
def l532_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l532_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l532_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l532_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l532_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l532_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l532_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l532_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l532_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l532_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l532_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l532_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l532_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l532_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l532_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l532_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l532_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l532_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l532_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l532_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l532_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[100])
def l532_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[101])
def l532_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[102])
def l532_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[103])
def l532_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[104])
def l532_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[105])
def l532_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[106])
def l532_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[107])
def l532_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[108])
def l532_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[109])
def l532_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[110])
def l532_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[111])
def l532_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[112])
def l532_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[113])
def l532_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[114])
def l532_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[115])
def l532_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[116])
def l532_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[117])
def l532_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[118])
def l532_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[119])
def l532_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[120])
def l532_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[121])
def l532_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[122])
def l532_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[123])
def l532_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[124])
def l532_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[125])
def l532_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[126])
def l532_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[127])
def l532_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l532_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l532_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l532_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l532_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l532_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l532_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l532_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l532_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l532_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l532_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l532_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l532_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l532_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l532_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l532_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l532_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[144])
def l532_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[145])
def l532_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[146])
def l532_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[147])
def l532_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[148])
def l532_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[149])
def l532_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[150])
def l532_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[151])
def l532_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[152])
def l532_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[153])
def l532_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[154])
def l532_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[155])
def l532_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[156])
def l532_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[157])
def l532_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[158])
def l532_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[159])
def l532_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l532_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l532_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l532_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l532_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l532_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l532_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l532_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l532_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l532_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l532_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l532_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l532_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l532_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l532_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l532_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l532_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l532_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l532_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l532_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l532_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l532_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l532_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l532_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l532_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l532_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l532_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l532_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l532_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l532_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l532_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l532_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l532_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l532_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l532_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l532_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l532_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l532_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l532_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l532_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l532_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l532_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l532_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l532_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l532_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l532_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l532_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l532_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l532_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l532_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l532_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l532_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l532_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l532_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l532_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l532_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l532_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l532_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l532_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l532_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l532_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l532_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l532_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l532_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l532_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l532_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l532_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l532_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l532_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l532_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l532_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l532_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l532_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l532_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l532_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l532_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l532_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l532_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l532_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l532_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l532_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l532_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l532_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l532_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l532_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l532_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l532_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l532_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l532_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l532_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l532_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l532_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l532_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l532_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l532_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l532_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l532_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l532_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l532_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l532_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l532_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l532_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l532_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l532_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l532_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l532_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l532_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l532_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l532_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l532_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l532_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l532_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l532_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l532_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l532_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l532_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l532_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l532_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l532_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l532_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l532_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l532_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l532_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l532_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l532_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l532_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l532_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l532_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l532_(x):
    # x is a list (or vector) of length 288
    return [
        l532_0(x),
        l532_1(x),
        l532_2(x),
        l532_3(x),
        l532_4(x),
        l532_5(x),
        l532_6(x),
        l532_7(x),
        l532_8(x),
        l532_9(x),
        l532_10(x),
        l532_11(x),
        l532_12(x),
        l532_13(x),
        l532_14(x),
        l532_15(x),
        l532_16(x),
        l532_17(x),
        l532_18(x),
        l532_19(x),
        l532_20(x),
        l532_21(x),
        l532_22(x),
        l532_23(x),
        l532_24(x),
        l532_25(x),
        l532_26(x),
        l532_27(x),
        l532_28(x),
        l532_29(x),
        l532_30(x),
        l532_31(x),
        l532_32(x),
        l532_33(x),
        l532_34(x),
        l532_35(x),
        l532_36(x),
        l532_37(x),
        l532_38(x),
        l532_39(x),
        l532_40(x),
        l532_41(x),
        l532_42(x),
        l532_43(x),
        l532_44(x),
        l532_45(x),
        l532_46(x),
        l532_47(x),
        l532_48(x),
        l532_49(x),
        l532_50(x),
        l532_51(x),
        l532_52(x),
        l532_53(x),
        l532_54(x),
        l532_55(x),
        l532_56(x),
        l532_57(x),
        l532_58(x),
        l532_59(x),
        l532_60(x),
        l532_61(x),
        l532_62(x),
        l532_63(x),
        l532_64(x),
        l532_65(x),
        l532_66(x),
        l532_67(x),
        l532_68(x),
        l532_69(x),
        l532_70(x),
        l532_71(x),
        l532_72(x),
        l532_73(x),
        l532_74(x),
        l532_75(x),
        l532_76(x),
        l532_77(x),
        l532_78(x),
        l532_79(x),
        l532_80(x),
        l532_81(x),
        l532_82(x),
        l532_83(x),
        l532_84(x),
        l532_85(x),
        l532_86(x),
        l532_87(x),
        l532_88(x),
        l532_89(x),
        l532_90(x),
        l532_91(x),
        l532_92(x),
        l532_93(x),
        l532_94(x),
        l532_95(x),
        l532_96(x),
        l532_97(x),
        l532_98(x),
        l532_99(x),
        l532_100(x),
        l532_101(x),
        l532_102(x),
        l532_103(x),
        l532_104(x),
        l532_105(x),
        l532_106(x),
        l532_107(x),
        l532_108(x),
        l532_109(x),
        l532_110(x),
        l532_111(x),
        l532_112(x),
        l532_113(x),
        l532_114(x),
        l532_115(x),
        l532_116(x),
        l532_117(x),
        l532_118(x),
        l532_119(x),
        l532_120(x),
        l532_121(x),
        l532_122(x),
        l532_123(x),
        l532_124(x),
        l532_125(x),
        l532_126(x),
        l532_127(x),
        l532_128(x),
        l532_129(x),
        l532_130(x),
        l532_131(x),
        l532_132(x),
        l532_133(x),
        l532_134(x),
        l532_135(x),
        l532_136(x),
        l532_137(x),
        l532_138(x),
        l532_139(x),
        l532_140(x),
        l532_141(x),
        l532_142(x),
        l532_143(x),
        l532_144(x),
        l532_145(x),
        l532_146(x),
        l532_147(x),
        l532_148(x),
        l532_149(x),
        l532_150(x),
        l532_151(x),
        l532_152(x),
        l532_153(x),
        l532_154(x),
        l532_155(x),
        l532_156(x),
        l532_157(x),
        l532_158(x),
        l532_159(x),
        l532_160(x),
        l532_161(x),
        l532_162(x),
        l532_163(x),
        l532_164(x),
        l532_165(x),
        l532_166(x),
        l532_167(x),
        l532_168(x),
        l532_169(x),
        l532_170(x),
        l532_171(x),
        l532_172(x),
        l532_173(x),
        l532_174(x),
        l532_175(x),
        l532_176(x),
        l532_177(x),
        l532_178(x),
        l532_179(x),
        l532_180(x),
        l532_181(x),
        l532_182(x),
        l532_183(x),
        l532_184(x),
        l532_185(x),
        l532_186(x),
        l532_187(x),
        l532_188(x),
        l532_189(x),
        l532_190(x),
        l532_191(x),
        l532_192(x),
        l532_193(x),
        l532_194(x),
        l532_195(x),
        l532_196(x),
        l532_197(x),
        l532_198(x),
        l532_199(x),
        l532_200(x),
        l532_201(x),
        l532_202(x),
        l532_203(x),
        l532_204(x),
        l532_205(x),
        l532_206(x),
        l532_207(x),
        l532_208(x),
        l532_209(x),
        l532_210(x),
        l532_211(x),
        l532_212(x),
        l532_213(x),
        l532_214(x),
        l532_215(x),
        l532_216(x),
        l532_217(x),
        l532_218(x),
        l532_219(x),
        l532_220(x),
        l532_221(x),
        l532_222(x),
        l532_223(x),
        l532_224(x),
        l532_225(x),
        l532_226(x),
        l532_227(x),
        l532_228(x),
        l532_229(x),
        l532_230(x),
        l532_231(x),
        l532_232(x),
        l532_233(x),
        l532_234(x),
        l532_235(x),
        l532_236(x),
        l532_237(x),
        l532_238(x),
        l532_239(x),
        l532_240(x),
        l532_241(x),
        l532_242(x),
        l532_243(x),
        l532_244(x),
        l532_245(x),
        l532_246(x),
        l532_247(x),
        l532_248(x),
        l532_249(x),
        l532_250(x),
        l532_251(x),
        l532_252(x),
        l532_253(x),
        l532_254(x),
        l532_255(x),
        l532_256(x),
        l532_257(x),
        l532_258(x),
        l532_259(x),
        l532_260(x),
        l532_261(x),
        l532_262(x),
        l532_263(x),
        l532_264(x),
        l532_265(x),
        l532_266(x),
        l532_267(x),
        l532_268(x),
        l532_269(x),
        l532_270(x),
        l532_271(x),
        l532_272(x),
        l532_273(x),
        l532_274(x),
        l532_275(x),
        l532_276(x),
        l532_277(x),
        l532_278(x),
        l532_279(x),
        l532_280(x),
        l532_281(x),
        l532_282(x),
        l532_283(x),
        l532_284(x),
        l532_285(x),
        l532_286(x),
        l532_287(x),
        l532_288(x),
        l532_289(x),
        l532_290(x),
        l532_291(x),
        l532_292(x),
        l532_293(x),
        l532_294(x),
        l532_295(x),
        l532_296(x),
        l532_297(x),
        l532_298(x),
        l532_299(x),
        l532_300(x),
        l532_301(x),
        l532_302(x),
        l532_303(x),
    ]