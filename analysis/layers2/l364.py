import numpy as np




# Generated from reverse engineering
def l364_g(x: np.ndarray) -> np.ndarray:
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




def l364_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l364_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l364_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l364_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l364_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l364_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l364_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l364_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l364_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l364_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l364_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l364_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l364_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l364_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l364_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l364_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l364_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l364_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l364_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l364_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l364_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l364_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l364_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l364_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l364_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l364_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l364_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l364_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l364_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l364_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l364_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l364_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l364_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l364_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l364_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l364_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l364_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l364_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l364_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l364_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l364_40(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + 1.0)
def l364_41(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + 1.0)
def l364_42(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + 1.0)
def l364_43(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + 1.0)
def l364_44(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + 1.0)
def l364_45(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + 1.0)
def l364_46(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + 1.0)
def l364_47(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + 1.0)
def l364_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[32] + x[80] + -1.0)
def l364_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[33] + x[81] + -1.0)
def l364_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[34] + x[82] + -1.0)
def l364_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[35] + x[83] + -1.0)
def l364_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[36] + x[84] + -1.0)
def l364_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[37] + x[85] + -1.0)
def l364_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[38] + x[86] + -1.0)
def l364_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[39] + x[87] + -1.0)
def l364_56(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[40] + x[88])
def l364_57(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[41] + x[89])
def l364_58(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[42] + x[90])
def l364_59(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[43] + x[91])
def l364_60(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[44] + x[92])
def l364_61(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[45] + x[93])
def l364_62(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[46] + x[94])
def l364_63(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[47] + x[95])
def l364_64(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + 1.0)
def l364_65(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + 1.0)
def l364_66(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + 1.0)
def l364_67(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + 1.0)
def l364_68(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + 1.0)
def l364_69(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + 1.0)
def l364_70(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + 1.0)
def l364_71(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + 1.0)
def l364_72(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + 1.0)
def l364_73(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + 1.0)
def l364_74(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + 1.0)
def l364_75(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + 1.0)
def l364_76(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + 1.0)
def l364_77(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + 1.0)
def l364_78(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[62] + 1.0)
def l364_79(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[63] + 1.0)
def l364_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[64] + x[80] + -1.0)
def l364_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[65] + x[81] + -1.0)
def l364_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[66] + x[82] + -1.0)
def l364_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[67] + x[83] + -1.0)
def l364_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[68] + x[84] + -1.0)
def l364_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[69] + x[85] + -1.0)
def l364_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[70] + x[86] + -1.0)
def l364_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[71] + x[87] + -1.0)
def l364_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[72] + x[88] + -1.0)
def l364_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[73] + x[89] + -1.0)
def l364_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[74] + x[90] + -1.0)
def l364_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[75] + x[91] + -1.0)
def l364_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[76] + x[92] + -1.0)
def l364_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[77] + x[93] + -1.0)
def l364_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[78] + x[94] + -1.0)
def l364_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[79] + x[95] + -1.0)
def l364_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l364_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l364_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l364_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l364_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l364_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l364_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l364_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l364_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l364_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l364_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l364_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l364_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l364_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l364_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l364_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l364_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l364_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l364_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l364_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l364_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[100])
def l364_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[101])
def l364_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[102])
def l364_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[103])
def l364_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[104])
def l364_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[105])
def l364_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[106])
def l364_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[107])
def l364_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[108])
def l364_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[109])
def l364_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[110])
def l364_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[111])
def l364_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[112])
def l364_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[113])
def l364_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[114])
def l364_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[115])
def l364_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[116])
def l364_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[117])
def l364_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[118])
def l364_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[119])
def l364_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[120])
def l364_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[121])
def l364_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[122])
def l364_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[123])
def l364_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[124])
def l364_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[125])
def l364_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[126])
def l364_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[127])
def l364_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l364_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l364_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l364_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l364_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l364_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l364_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l364_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l364_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l364_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l364_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l364_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l364_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l364_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l364_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l364_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l364_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[144])
def l364_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[145])
def l364_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[146])
def l364_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[147])
def l364_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[148])
def l364_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[149])
def l364_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[150])
def l364_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[151])
def l364_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[152])
def l364_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[153])
def l364_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[154])
def l364_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[155])
def l364_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[156])
def l364_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[157])
def l364_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[158])
def l364_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[159])
def l364_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l364_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l364_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l364_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l364_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l364_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l364_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l364_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l364_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l364_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l364_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l364_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l364_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l364_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l364_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l364_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l364_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l364_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l364_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l364_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l364_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l364_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l364_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l364_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l364_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l364_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l364_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l364_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l364_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l364_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l364_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l364_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l364_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l364_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l364_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l364_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l364_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l364_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l364_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l364_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l364_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l364_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l364_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l364_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l364_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l364_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l364_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l364_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l364_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l364_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l364_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l364_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l364_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l364_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l364_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l364_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l364_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l364_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l364_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l364_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l364_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l364_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l364_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l364_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l364_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l364_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l364_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l364_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l364_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l364_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l364_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l364_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l364_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l364_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l364_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l364_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l364_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l364_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l364_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l364_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l364_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l364_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l364_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l364_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l364_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l364_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l364_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l364_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l364_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l364_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l364_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l364_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l364_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l364_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l364_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l364_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l364_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l364_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l364_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l364_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l364_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l364_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l364_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l364_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l364_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l364_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l364_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l364_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l364_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l364_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l364_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l364_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l364_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l364_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l364_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l364_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l364_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l364_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l364_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l364_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l364_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l364_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l364_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l364_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l364_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l364_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l364_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l364_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l364_(x):
    # x is a list (or vector) of length 288
    return [
        l364_0(x),
        l364_1(x),
        l364_2(x),
        l364_3(x),
        l364_4(x),
        l364_5(x),
        l364_6(x),
        l364_7(x),
        l364_8(x),
        l364_9(x),
        l364_10(x),
        l364_11(x),
        l364_12(x),
        l364_13(x),
        l364_14(x),
        l364_15(x),
        l364_16(x),
        l364_17(x),
        l364_18(x),
        l364_19(x),
        l364_20(x),
        l364_21(x),
        l364_22(x),
        l364_23(x),
        l364_24(x),
        l364_25(x),
        l364_26(x),
        l364_27(x),
        l364_28(x),
        l364_29(x),
        l364_30(x),
        l364_31(x),
        l364_32(x),
        l364_33(x),
        l364_34(x),
        l364_35(x),
        l364_36(x),
        l364_37(x),
        l364_38(x),
        l364_39(x),
        l364_40(x),
        l364_41(x),
        l364_42(x),
        l364_43(x),
        l364_44(x),
        l364_45(x),
        l364_46(x),
        l364_47(x),
        l364_48(x),
        l364_49(x),
        l364_50(x),
        l364_51(x),
        l364_52(x),
        l364_53(x),
        l364_54(x),
        l364_55(x),
        l364_56(x),
        l364_57(x),
        l364_58(x),
        l364_59(x),
        l364_60(x),
        l364_61(x),
        l364_62(x),
        l364_63(x),
        l364_64(x),
        l364_65(x),
        l364_66(x),
        l364_67(x),
        l364_68(x),
        l364_69(x),
        l364_70(x),
        l364_71(x),
        l364_72(x),
        l364_73(x),
        l364_74(x),
        l364_75(x),
        l364_76(x),
        l364_77(x),
        l364_78(x),
        l364_79(x),
        l364_80(x),
        l364_81(x),
        l364_82(x),
        l364_83(x),
        l364_84(x),
        l364_85(x),
        l364_86(x),
        l364_87(x),
        l364_88(x),
        l364_89(x),
        l364_90(x),
        l364_91(x),
        l364_92(x),
        l364_93(x),
        l364_94(x),
        l364_95(x),
        l364_96(x),
        l364_97(x),
        l364_98(x),
        l364_99(x),
        l364_100(x),
        l364_101(x),
        l364_102(x),
        l364_103(x),
        l364_104(x),
        l364_105(x),
        l364_106(x),
        l364_107(x),
        l364_108(x),
        l364_109(x),
        l364_110(x),
        l364_111(x),
        l364_112(x),
        l364_113(x),
        l364_114(x),
        l364_115(x),
        l364_116(x),
        l364_117(x),
        l364_118(x),
        l364_119(x),
        l364_120(x),
        l364_121(x),
        l364_122(x),
        l364_123(x),
        l364_124(x),
        l364_125(x),
        l364_126(x),
        l364_127(x),
        l364_128(x),
        l364_129(x),
        l364_130(x),
        l364_131(x),
        l364_132(x),
        l364_133(x),
        l364_134(x),
        l364_135(x),
        l364_136(x),
        l364_137(x),
        l364_138(x),
        l364_139(x),
        l364_140(x),
        l364_141(x),
        l364_142(x),
        l364_143(x),
        l364_144(x),
        l364_145(x),
        l364_146(x),
        l364_147(x),
        l364_148(x),
        l364_149(x),
        l364_150(x),
        l364_151(x),
        l364_152(x),
        l364_153(x),
        l364_154(x),
        l364_155(x),
        l364_156(x),
        l364_157(x),
        l364_158(x),
        l364_159(x),
        l364_160(x),
        l364_161(x),
        l364_162(x),
        l364_163(x),
        l364_164(x),
        l364_165(x),
        l364_166(x),
        l364_167(x),
        l364_168(x),
        l364_169(x),
        l364_170(x),
        l364_171(x),
        l364_172(x),
        l364_173(x),
        l364_174(x),
        l364_175(x),
        l364_176(x),
        l364_177(x),
        l364_178(x),
        l364_179(x),
        l364_180(x),
        l364_181(x),
        l364_182(x),
        l364_183(x),
        l364_184(x),
        l364_185(x),
        l364_186(x),
        l364_187(x),
        l364_188(x),
        l364_189(x),
        l364_190(x),
        l364_191(x),
        l364_192(x),
        l364_193(x),
        l364_194(x),
        l364_195(x),
        l364_196(x),
        l364_197(x),
        l364_198(x),
        l364_199(x),
        l364_200(x),
        l364_201(x),
        l364_202(x),
        l364_203(x),
        l364_204(x),
        l364_205(x),
        l364_206(x),
        l364_207(x),
        l364_208(x),
        l364_209(x),
        l364_210(x),
        l364_211(x),
        l364_212(x),
        l364_213(x),
        l364_214(x),
        l364_215(x),
        l364_216(x),
        l364_217(x),
        l364_218(x),
        l364_219(x),
        l364_220(x),
        l364_221(x),
        l364_222(x),
        l364_223(x),
        l364_224(x),
        l364_225(x),
        l364_226(x),
        l364_227(x),
        l364_228(x),
        l364_229(x),
        l364_230(x),
        l364_231(x),
        l364_232(x),
        l364_233(x),
        l364_234(x),
        l364_235(x),
        l364_236(x),
        l364_237(x),
        l364_238(x),
        l364_239(x),
        l364_240(x),
        l364_241(x),
        l364_242(x),
        l364_243(x),
        l364_244(x),
        l364_245(x),
        l364_246(x),
        l364_247(x),
        l364_248(x),
        l364_249(x),
        l364_250(x),
        l364_251(x),
        l364_252(x),
        l364_253(x),
        l364_254(x),
        l364_255(x),
        l364_256(x),
        l364_257(x),
        l364_258(x),
        l364_259(x),
        l364_260(x),
        l364_261(x),
        l364_262(x),
        l364_263(x),
        l364_264(x),
        l364_265(x),
        l364_266(x),
        l364_267(x),
        l364_268(x),
        l364_269(x),
        l364_270(x),
        l364_271(x),
        l364_272(x),
        l364_273(x),
        l364_274(x),
        l364_275(x),
        l364_276(x),
        l364_277(x),
        l364_278(x),
        l364_279(x),
        l364_280(x),
        l364_281(x),
        l364_282(x),
        l364_283(x),
        l364_284(x),
        l364_285(x),
        l364_286(x),
        l364_287(x),
        l364_288(x),
        l364_289(x),
        l364_290(x),
        l364_291(x),
        l364_292(x),
        l364_293(x),
        l364_294(x),
        l364_295(x),
        l364_296(x),
        l364_297(x),
        l364_298(x),
        l364_299(x),
        l364_300(x),
        l364_301(x),
        l364_302(x),
        l364_303(x),
    ]