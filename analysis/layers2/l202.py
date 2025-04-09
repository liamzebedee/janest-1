import numpy as np




# Generated from reverse engineering
def l202_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 336
    out = np.empty(336, dtype=np.float32)
    
    # for i in range(0, 32):
    for i in range(0, 32):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(32, 64):
    for i in range(0, 32):
        s = x[32 + i] + -2.0 * x[i + 64]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 128):
    for i in range(0, 64):
        s = x[96 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(128, 160):
    for i in range(0, 32):
        s = x[32 + i] + x[96 + i] + -2.0 * x[i + 64]
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 192):
    for i in range(0, 32):
        s = x[128 + i] + -1 * x[32 + i] + 2.0 * x[i + 64]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(192, 224):
    for i in range(0, 32):
        s = x[160 + i]
        out[192 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xdb0e0424 (len=32)
    biases = [1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0]
    # for i in range(224, 256):
    for i in range(0, 32):
        s = 0
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [128.0, 128.0, 128.0, 128.0]
    # for i in range(256, 260):
    for i in range(0, 4):
        s = -1 * x[204 + i]
        s += biases[i]
        out[256 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(260, 264):
    for i in range(0, 4):
        s = x[204 + i]
        out[260 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-127.0, -127.0, -127.0, -127.0]
    # for i in range(264, 268):
    for i in range(0, 4):
        s = x[204 + i]
        s += biases[i]
        out[264 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-128.0, -128.0, -128.0, -128.0]
    # for i in range(268, 272):
    for i in range(0, 4):
        s = x[204 + i]
        s += biases[i]
        out[268 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(272, 336):
    for i in range(0, 64):
        s = x[192 + i]
        out[272 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l202_0(x):
    # x is a list (or vector) of length 256
    return max(0, x[0])
def l202_1(x):
    # x is a list (or vector) of length 256
    return max(0, x[1])
def l202_2(x):
    # x is a list (or vector) of length 256
    return max(0, x[2])
def l202_3(x):
    # x is a list (or vector) of length 256
    return max(0, x[3])
def l202_4(x):
    # x is a list (or vector) of length 256
    return max(0, x[4])
def l202_5(x):
    # x is a list (or vector) of length 256
    return max(0, x[5])
def l202_6(x):
    # x is a list (or vector) of length 256
    return max(0, x[6])
def l202_7(x):
    # x is a list (or vector) of length 256
    return max(0, x[7])
def l202_8(x):
    # x is a list (or vector) of length 256
    return max(0, x[8])
def l202_9(x):
    # x is a list (or vector) of length 256
    return max(0, x[9])
def l202_10(x):
    # x is a list (or vector) of length 256
    return max(0, x[10])
def l202_11(x):
    # x is a list (or vector) of length 256
    return max(0, x[11])
def l202_12(x):
    # x is a list (or vector) of length 256
    return max(0, x[12])
def l202_13(x):
    # x is a list (or vector) of length 256
    return max(0, x[13])
def l202_14(x):
    # x is a list (or vector) of length 256
    return max(0, x[14])
def l202_15(x):
    # x is a list (or vector) of length 256
    return max(0, x[15])
def l202_16(x):
    # x is a list (or vector) of length 256
    return max(0, x[16])
def l202_17(x):
    # x is a list (or vector) of length 256
    return max(0, x[17])
def l202_18(x):
    # x is a list (or vector) of length 256
    return max(0, x[18])
def l202_19(x):
    # x is a list (or vector) of length 256
    return max(0, x[19])
def l202_20(x):
    # x is a list (or vector) of length 256
    return max(0, x[20])
def l202_21(x):
    # x is a list (or vector) of length 256
    return max(0, x[21])
def l202_22(x):
    # x is a list (or vector) of length 256
    return max(0, x[22])
def l202_23(x):
    # x is a list (or vector) of length 256
    return max(0, x[23])
def l202_24(x):
    # x is a list (or vector) of length 256
    return max(0, x[24])
def l202_25(x):
    # x is a list (or vector) of length 256
    return max(0, x[25])
def l202_26(x):
    # x is a list (or vector) of length 256
    return max(0, x[26])
def l202_27(x):
    # x is a list (or vector) of length 256
    return max(0, x[27])
def l202_28(x):
    # x is a list (or vector) of length 256
    return max(0, x[28])
def l202_29(x):
    # x is a list (or vector) of length 256
    return max(0, x[29])
def l202_30(x):
    # x is a list (or vector) of length 256
    return max(0, x[30])
def l202_31(x):
    # x is a list (or vector) of length 256
    return max(0, x[31])
def l202_32(x):
    # x is a list (or vector) of length 256
    return max(0, x[32] + -2.0*x[64])
def l202_33(x):
    # x is a list (or vector) of length 256
    return max(0, x[33] + -2.0*x[65])
def l202_34(x):
    # x is a list (or vector) of length 256
    return max(0, x[34] + -2.0*x[66])
def l202_35(x):
    # x is a list (or vector) of length 256
    return max(0, x[35] + -2.0*x[67])
def l202_36(x):
    # x is a list (or vector) of length 256
    return max(0, x[36] + -2.0*x[68])
def l202_37(x):
    # x is a list (or vector) of length 256
    return max(0, x[37] + -2.0*x[69])
def l202_38(x):
    # x is a list (or vector) of length 256
    return max(0, x[38] + -2.0*x[70])
def l202_39(x):
    # x is a list (or vector) of length 256
    return max(0, x[39] + -2.0*x[71])
def l202_40(x):
    # x is a list (or vector) of length 256
    return max(0, x[40] + -2.0*x[72])
def l202_41(x):
    # x is a list (or vector) of length 256
    return max(0, x[41] + -2.0*x[73])
def l202_42(x):
    # x is a list (or vector) of length 256
    return max(0, x[42] + -2.0*x[74])
def l202_43(x):
    # x is a list (or vector) of length 256
    return max(0, x[43] + -2.0*x[75])
def l202_44(x):
    # x is a list (or vector) of length 256
    return max(0, x[44] + -2.0*x[76])
def l202_45(x):
    # x is a list (or vector) of length 256
    return max(0, x[45] + -2.0*x[77])
def l202_46(x):
    # x is a list (or vector) of length 256
    return max(0, x[46] + -2.0*x[78])
def l202_47(x):
    # x is a list (or vector) of length 256
    return max(0, x[47] + -2.0*x[79])
def l202_48(x):
    # x is a list (or vector) of length 256
    return max(0, x[48] + -2.0*x[80])
def l202_49(x):
    # x is a list (or vector) of length 256
    return max(0, x[49] + -2.0*x[81])
def l202_50(x):
    # x is a list (or vector) of length 256
    return max(0, x[50] + -2.0*x[82])
def l202_51(x):
    # x is a list (or vector) of length 256
    return max(0, x[51] + -2.0*x[83])
def l202_52(x):
    # x is a list (or vector) of length 256
    return max(0, x[52] + -2.0*x[84])
def l202_53(x):
    # x is a list (or vector) of length 256
    return max(0, x[53] + -2.0*x[85])
def l202_54(x):
    # x is a list (or vector) of length 256
    return max(0, x[54] + -2.0*x[86])
def l202_55(x):
    # x is a list (or vector) of length 256
    return max(0, x[55] + -2.0*x[87])
def l202_56(x):
    # x is a list (or vector) of length 256
    return max(0, x[56] + -2.0*x[88])
def l202_57(x):
    # x is a list (or vector) of length 256
    return max(0, x[57] + -2.0*x[89])
def l202_58(x):
    # x is a list (or vector) of length 256
    return max(0, x[58] + -2.0*x[90])
def l202_59(x):
    # x is a list (or vector) of length 256
    return max(0, x[59] + -2.0*x[91])
def l202_60(x):
    # x is a list (or vector) of length 256
    return max(0, x[60] + -2.0*x[92])
def l202_61(x):
    # x is a list (or vector) of length 256
    return max(0, x[61] + -2.0*x[93])
def l202_62(x):
    # x is a list (or vector) of length 256
    return max(0, x[62] + -2.0*x[94])
def l202_63(x):
    # x is a list (or vector) of length 256
    return max(0, x[63] + -2.0*x[95])
def l202_64(x):
    # x is a list (or vector) of length 256
    return max(0, x[96])
def l202_65(x):
    # x is a list (or vector) of length 256
    return max(0, x[97])
def l202_66(x):
    # x is a list (or vector) of length 256
    return max(0, x[98])
def l202_67(x):
    # x is a list (or vector) of length 256
    return max(0, x[99])
def l202_68(x):
    # x is a list (or vector) of length 256
    return max(0, x[100])
def l202_69(x):
    # x is a list (or vector) of length 256
    return max(0, x[101])
def l202_70(x):
    # x is a list (or vector) of length 256
    return max(0, x[102])
def l202_71(x):
    # x is a list (or vector) of length 256
    return max(0, x[103])
def l202_72(x):
    # x is a list (or vector) of length 256
    return max(0, x[104])
def l202_73(x):
    # x is a list (or vector) of length 256
    return max(0, x[105])
def l202_74(x):
    # x is a list (or vector) of length 256
    return max(0, x[106])
def l202_75(x):
    # x is a list (or vector) of length 256
    return max(0, x[107])
def l202_76(x):
    # x is a list (or vector) of length 256
    return max(0, x[108])
def l202_77(x):
    # x is a list (or vector) of length 256
    return max(0, x[109])
def l202_78(x):
    # x is a list (or vector) of length 256
    return max(0, x[110])
def l202_79(x):
    # x is a list (or vector) of length 256
    return max(0, x[111])
def l202_80(x):
    # x is a list (or vector) of length 256
    return max(0, x[112])
def l202_81(x):
    # x is a list (or vector) of length 256
    return max(0, x[113])
def l202_82(x):
    # x is a list (or vector) of length 256
    return max(0, x[114])
def l202_83(x):
    # x is a list (or vector) of length 256
    return max(0, x[115])
def l202_84(x):
    # x is a list (or vector) of length 256
    return max(0, x[116])
def l202_85(x):
    # x is a list (or vector) of length 256
    return max(0, x[117])
def l202_86(x):
    # x is a list (or vector) of length 256
    return max(0, x[118])
def l202_87(x):
    # x is a list (or vector) of length 256
    return max(0, x[119])
def l202_88(x):
    # x is a list (or vector) of length 256
    return max(0, x[120])
def l202_89(x):
    # x is a list (or vector) of length 256
    return max(0, x[121])
def l202_90(x):
    # x is a list (or vector) of length 256
    return max(0, x[122])
def l202_91(x):
    # x is a list (or vector) of length 256
    return max(0, x[123])
def l202_92(x):
    # x is a list (or vector) of length 256
    return max(0, x[124])
def l202_93(x):
    # x is a list (or vector) of length 256
    return max(0, x[125])
def l202_94(x):
    # x is a list (or vector) of length 256
    return max(0, x[126])
def l202_95(x):
    # x is a list (or vector) of length 256
    return max(0, x[127])
def l202_96(x):
    # x is a list (or vector) of length 256
    return max(0, x[128])
def l202_97(x):
    # x is a list (or vector) of length 256
    return max(0, x[129])
def l202_98(x):
    # x is a list (or vector) of length 256
    return max(0, x[130])
def l202_99(x):
    # x is a list (or vector) of length 256
    return max(0, x[131])
def l202_100(x):
    # x is a list (or vector) of length 256
    return max(0, x[132])
def l202_101(x):
    # x is a list (or vector) of length 256
    return max(0, x[133])
def l202_102(x):
    # x is a list (or vector) of length 256
    return max(0, x[134])
def l202_103(x):
    # x is a list (or vector) of length 256
    return max(0, x[135])
def l202_104(x):
    # x is a list (or vector) of length 256
    return max(0, x[136])
def l202_105(x):
    # x is a list (or vector) of length 256
    return max(0, x[137])
def l202_106(x):
    # x is a list (or vector) of length 256
    return max(0, x[138])
def l202_107(x):
    # x is a list (or vector) of length 256
    return max(0, x[139])
def l202_108(x):
    # x is a list (or vector) of length 256
    return max(0, x[140])
def l202_109(x):
    # x is a list (or vector) of length 256
    return max(0, x[141])
def l202_110(x):
    # x is a list (or vector) of length 256
    return max(0, x[142])
def l202_111(x):
    # x is a list (or vector) of length 256
    return max(0, x[143])
def l202_112(x):
    # x is a list (or vector) of length 256
    return max(0, x[144])
def l202_113(x):
    # x is a list (or vector) of length 256
    return max(0, x[145])
def l202_114(x):
    # x is a list (or vector) of length 256
    return max(0, x[146])
def l202_115(x):
    # x is a list (or vector) of length 256
    return max(0, x[147])
def l202_116(x):
    # x is a list (or vector) of length 256
    return max(0, x[148])
def l202_117(x):
    # x is a list (or vector) of length 256
    return max(0, x[149])
def l202_118(x):
    # x is a list (or vector) of length 256
    return max(0, x[150])
def l202_119(x):
    # x is a list (or vector) of length 256
    return max(0, x[151])
def l202_120(x):
    # x is a list (or vector) of length 256
    return max(0, x[152])
def l202_121(x):
    # x is a list (or vector) of length 256
    return max(0, x[153])
def l202_122(x):
    # x is a list (or vector) of length 256
    return max(0, x[154])
def l202_123(x):
    # x is a list (or vector) of length 256
    return max(0, x[155])
def l202_124(x):
    # x is a list (or vector) of length 256
    return max(0, x[156])
def l202_125(x):
    # x is a list (or vector) of length 256
    return max(0, x[157])
def l202_126(x):
    # x is a list (or vector) of length 256
    return max(0, x[158])
def l202_127(x):
    # x is a list (or vector) of length 256
    return max(0, x[159])
def l202_128(x):
    # x is a list (or vector) of length 256
    return max(0, x[32] + -2.0*x[64] + x[96] + -1.0)
def l202_129(x):
    # x is a list (or vector) of length 256
    return max(0, x[33] + -2.0*x[65] + x[97] + -1.0)
def l202_130(x):
    # x is a list (or vector) of length 256
    return max(0, x[34] + -2.0*x[66] + x[98] + -1.0)
def l202_131(x):
    # x is a list (or vector) of length 256
    return max(0, x[35] + -2.0*x[67] + x[99] + -1.0)
def l202_132(x):
    # x is a list (or vector) of length 256
    return max(0, x[36] + -2.0*x[68] + x[100] + -1.0)
def l202_133(x):
    # x is a list (or vector) of length 256
    return max(0, x[37] + -2.0*x[69] + x[101] + -1.0)
def l202_134(x):
    # x is a list (or vector) of length 256
    return max(0, x[38] + -2.0*x[70] + x[102] + -1.0)
def l202_135(x):
    # x is a list (or vector) of length 256
    return max(0, x[39] + -2.0*x[71] + x[103] + -1.0)
def l202_136(x):
    # x is a list (or vector) of length 256
    return max(0, x[40] + -2.0*x[72] + x[104] + -1.0)
def l202_137(x):
    # x is a list (or vector) of length 256
    return max(0, x[41] + -2.0*x[73] + x[105] + -1.0)
def l202_138(x):
    # x is a list (or vector) of length 256
    return max(0, x[42] + -2.0*x[74] + x[106] + -1.0)
def l202_139(x):
    # x is a list (or vector) of length 256
    return max(0, x[43] + -2.0*x[75] + x[107] + -1.0)
def l202_140(x):
    # x is a list (or vector) of length 256
    return max(0, x[44] + -2.0*x[76] + x[108] + -1.0)
def l202_141(x):
    # x is a list (or vector) of length 256
    return max(0, x[45] + -2.0*x[77] + x[109] + -1.0)
def l202_142(x):
    # x is a list (or vector) of length 256
    return max(0, x[46] + -2.0*x[78] + x[110] + -1.0)
def l202_143(x):
    # x is a list (or vector) of length 256
    return max(0, x[47] + -2.0*x[79] + x[111] + -1.0)
def l202_144(x):
    # x is a list (or vector) of length 256
    return max(0, x[48] + -2.0*x[80] + x[112] + -1.0)
def l202_145(x):
    # x is a list (or vector) of length 256
    return max(0, x[49] + -2.0*x[81] + x[113] + -1.0)
def l202_146(x):
    # x is a list (or vector) of length 256
    return max(0, x[50] + -2.0*x[82] + x[114] + -1.0)
def l202_147(x):
    # x is a list (or vector) of length 256
    return max(0, x[51] + -2.0*x[83] + x[115] + -1.0)
def l202_148(x):
    # x is a list (or vector) of length 256
    return max(0, x[52] + -2.0*x[84] + x[116] + -1.0)
def l202_149(x):
    # x is a list (or vector) of length 256
    return max(0, x[53] + -2.0*x[85] + x[117] + -1.0)
def l202_150(x):
    # x is a list (or vector) of length 256
    return max(0, x[54] + -2.0*x[86] + x[118] + -1.0)
def l202_151(x):
    # x is a list (or vector) of length 256
    return max(0, x[55] + -2.0*x[87] + x[119] + -1.0)
def l202_152(x):
    # x is a list (or vector) of length 256
    return max(0, x[56] + -2.0*x[88] + x[120] + -1.0)
def l202_153(x):
    # x is a list (or vector) of length 256
    return max(0, x[57] + -2.0*x[89] + x[121] + -1.0)
def l202_154(x):
    # x is a list (or vector) of length 256
    return max(0, x[58] + -2.0*x[90] + x[122] + -1.0)
def l202_155(x):
    # x is a list (or vector) of length 256
    return max(0, x[59] + -2.0*x[91] + x[123] + -1.0)
def l202_156(x):
    # x is a list (or vector) of length 256
    return max(0, x[60] + -2.0*x[92] + x[124] + -1.0)
def l202_157(x):
    # x is a list (or vector) of length 256
    return max(0, x[61] + -2.0*x[93] + x[125] + -1.0)
def l202_158(x):
    # x is a list (or vector) of length 256
    return max(0, x[62] + -2.0*x[94] + x[126] + -1.0)
def l202_159(x):
    # x is a list (or vector) of length 256
    return max(0, x[63] + -2.0*x[95] + x[127] + -1.0)
def l202_160(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[32] + 2.0*x[64] + x[128])
def l202_161(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[33] + 2.0*x[65] + x[129])
def l202_162(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[34] + 2.0*x[66] + x[130])
def l202_163(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[35] + 2.0*x[67] + x[131])
def l202_164(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[36] + 2.0*x[68] + x[132])
def l202_165(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[37] + 2.0*x[69] + x[133])
def l202_166(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[38] + 2.0*x[70] + x[134])
def l202_167(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[39] + 2.0*x[71] + x[135])
def l202_168(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[40] + 2.0*x[72] + x[136])
def l202_169(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[41] + 2.0*x[73] + x[137])
def l202_170(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[42] + 2.0*x[74] + x[138])
def l202_171(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[43] + 2.0*x[75] + x[139])
def l202_172(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[44] + 2.0*x[76] + x[140])
def l202_173(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[45] + 2.0*x[77] + x[141])
def l202_174(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[46] + 2.0*x[78] + x[142])
def l202_175(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[47] + 2.0*x[79] + x[143])
def l202_176(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[48] + 2.0*x[80] + x[144])
def l202_177(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[49] + 2.0*x[81] + x[145])
def l202_178(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[50] + 2.0*x[82] + x[146])
def l202_179(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[51] + 2.0*x[83] + x[147])
def l202_180(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[52] + 2.0*x[84] + x[148])
def l202_181(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[53] + 2.0*x[85] + x[149])
def l202_182(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[54] + 2.0*x[86] + x[150])
def l202_183(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[55] + 2.0*x[87] + x[151])
def l202_184(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[56] + 2.0*x[88] + x[152])
def l202_185(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[57] + 2.0*x[89] + x[153])
def l202_186(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[58] + 2.0*x[90] + x[154])
def l202_187(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[59] + 2.0*x[91] + x[155])
def l202_188(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[60] + 2.0*x[92] + x[156])
def l202_189(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[61] + 2.0*x[93] + x[157])
def l202_190(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[62] + 2.0*x[94] + x[158])
def l202_191(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[63] + 2.0*x[95] + x[159])
def l202_192(x):
    # x is a list (or vector) of length 256
    return max(0, x[160])
def l202_193(x):
    # x is a list (or vector) of length 256
    return max(0, x[161])
def l202_194(x):
    # x is a list (or vector) of length 256
    return max(0, x[162])
def l202_195(x):
    # x is a list (or vector) of length 256
    return max(0, x[163])
def l202_196(x):
    # x is a list (or vector) of length 256
    return max(0, x[164])
def l202_197(x):
    # x is a list (or vector) of length 256
    return max(0, x[165])
def l202_198(x):
    # x is a list (or vector) of length 256
    return max(0, x[166])
def l202_199(x):
    # x is a list (or vector) of length 256
    return max(0, x[167])
def l202_200(x):
    # x is a list (or vector) of length 256
    return max(0, x[168])
def l202_201(x):
    # x is a list (or vector) of length 256
    return max(0, x[169])
def l202_202(x):
    # x is a list (or vector) of length 256
    return max(0, x[170])
def l202_203(x):
    # x is a list (or vector) of length 256
    return max(0, x[171])
def l202_204(x):
    # x is a list (or vector) of length 256
    return max(0, x[172])
def l202_205(x):
    # x is a list (or vector) of length 256
    return max(0, x[173])
def l202_206(x):
    # x is a list (or vector) of length 256
    return max(0, x[174])
def l202_207(x):
    # x is a list (or vector) of length 256
    return max(0, x[175])
def l202_208(x):
    # x is a list (or vector) of length 256
    return max(0, x[176])
def l202_209(x):
    # x is a list (or vector) of length 256
    return max(0, x[177])
def l202_210(x):
    # x is a list (or vector) of length 256
    return max(0, x[178])
def l202_211(x):
    # x is a list (or vector) of length 256
    return max(0, x[179])
def l202_212(x):
    # x is a list (or vector) of length 256
    return max(0, x[180])
def l202_213(x):
    # x is a list (or vector) of length 256
    return max(0, x[181])
def l202_214(x):
    # x is a list (or vector) of length 256
    return max(0, x[182])
def l202_215(x):
    # x is a list (or vector) of length 256
    return max(0, x[183])
def l202_216(x):
    # x is a list (or vector) of length 256
    return max(0, x[184])
def l202_217(x):
    # x is a list (or vector) of length 256
    return max(0, x[185])
def l202_218(x):
    # x is a list (or vector) of length 256
    return max(0, x[186])
def l202_219(x):
    # x is a list (or vector) of length 256
    return max(0, x[187])
def l202_220(x):
    # x is a list (or vector) of length 256
    return max(0, x[188])
def l202_221(x):
    # x is a list (or vector) of length 256
    return max(0, x[189])
def l202_222(x):
    # x is a list (or vector) of length 256
    return max(0, x[190])
def l202_223(x):
    # x is a list (or vector) of length 256
    return max(0, x[191])
def l202_224(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l202_225(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l202_226(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_227(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l202_228(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l202_229(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_230(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l202_231(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l202_232(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_233(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_234(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_235(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_236(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l202_237(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l202_238(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l202_239(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_240(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_241(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_242(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_243(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_244(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_245(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l202_246(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_247(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_248(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_249(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_250(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l202_251(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_252(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_253(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l202_254(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_255(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l202_256(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[204] + 128.0)
def l202_257(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[205] + 128.0)
def l202_258(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[206] + 128.0)
def l202_259(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[207] + 128.0)
def l202_260(x):
    # x is a list (or vector) of length 256
    return max(0, x[204])
def l202_261(x):
    # x is a list (or vector) of length 256
    return max(0, x[205])
def l202_262(x):
    # x is a list (or vector) of length 256
    return max(0, x[206])
def l202_263(x):
    # x is a list (or vector) of length 256
    return max(0, x[207])
def l202_264(x):
    # x is a list (or vector) of length 256
    return max(0, x[204] + -127.0)
def l202_265(x):
    # x is a list (or vector) of length 256
    return max(0, x[205] + -127.0)
def l202_266(x):
    # x is a list (or vector) of length 256
    return max(0, x[206] + -127.0)
def l202_267(x):
    # x is a list (or vector) of length 256
    return max(0, x[207] + -127.0)
def l202_268(x):
    # x is a list (or vector) of length 256
    return max(0, x[204] + -128.0)
def l202_269(x):
    # x is a list (or vector) of length 256
    return max(0, x[205] + -128.0)
def l202_270(x):
    # x is a list (or vector) of length 256
    return max(0, x[206] + -128.0)
def l202_271(x):
    # x is a list (or vector) of length 256
    return max(0, x[207] + -128.0)
def l202_272(x):
    # x is a list (or vector) of length 256
    return max(0, x[192])
def l202_273(x):
    # x is a list (or vector) of length 256
    return max(0, x[193])
def l202_274(x):
    # x is a list (or vector) of length 256
    return max(0, x[194])
def l202_275(x):
    # x is a list (or vector) of length 256
    return max(0, x[195])
def l202_276(x):
    # x is a list (or vector) of length 256
    return max(0, x[196])
def l202_277(x):
    # x is a list (or vector) of length 256
    return max(0, x[197])
def l202_278(x):
    # x is a list (or vector) of length 256
    return max(0, x[198])
def l202_279(x):
    # x is a list (or vector) of length 256
    return max(0, x[199])
def l202_280(x):
    # x is a list (or vector) of length 256
    return max(0, x[200])
def l202_281(x):
    # x is a list (or vector) of length 256
    return max(0, x[201])
def l202_282(x):
    # x is a list (or vector) of length 256
    return max(0, x[202])
def l202_283(x):
    # x is a list (or vector) of length 256
    return max(0, x[203])
def l202_284(x):
    # x is a list (or vector) of length 256
    return max(0, x[204])
def l202_285(x):
    # x is a list (or vector) of length 256
    return max(0, x[205])
def l202_286(x):
    # x is a list (or vector) of length 256
    return max(0, x[206])
def l202_287(x):
    # x is a list (or vector) of length 256
    return max(0, x[207])
def l202_288(x):
    # x is a list (or vector) of length 256
    return max(0, x[208])
def l202_289(x):
    # x is a list (or vector) of length 256
    return max(0, x[209])
def l202_290(x):
    # x is a list (or vector) of length 256
    return max(0, x[210])
def l202_291(x):
    # x is a list (or vector) of length 256
    return max(0, x[211])
def l202_292(x):
    # x is a list (or vector) of length 256
    return max(0, x[212])
def l202_293(x):
    # x is a list (or vector) of length 256
    return max(0, x[213])
def l202_294(x):
    # x is a list (or vector) of length 256
    return max(0, x[214])
def l202_295(x):
    # x is a list (or vector) of length 256
    return max(0, x[215])
def l202_296(x):
    # x is a list (or vector) of length 256
    return max(0, x[216])
def l202_297(x):
    # x is a list (or vector) of length 256
    return max(0, x[217])
def l202_298(x):
    # x is a list (or vector) of length 256
    return max(0, x[218])
def l202_299(x):
    # x is a list (or vector) of length 256
    return max(0, x[219])
def l202_300(x):
    # x is a list (or vector) of length 256
    return max(0, x[220])
def l202_301(x):
    # x is a list (or vector) of length 256
    return max(0, x[221])
def l202_302(x):
    # x is a list (or vector) of length 256
    return max(0, x[222])
def l202_303(x):
    # x is a list (or vector) of length 256
    return max(0, x[223])
def l202_304(x):
    # x is a list (or vector) of length 256
    return max(0, x[224])
def l202_305(x):
    # x is a list (or vector) of length 256
    return max(0, x[225])
def l202_306(x):
    # x is a list (or vector) of length 256
    return max(0, x[226])
def l202_307(x):
    # x is a list (or vector) of length 256
    return max(0, x[227])
def l202_308(x):
    # x is a list (or vector) of length 256
    return max(0, x[228])
def l202_309(x):
    # x is a list (or vector) of length 256
    return max(0, x[229])
def l202_310(x):
    # x is a list (or vector) of length 256
    return max(0, x[230])
def l202_311(x):
    # x is a list (or vector) of length 256
    return max(0, x[231])
def l202_312(x):
    # x is a list (or vector) of length 256
    return max(0, x[232])
def l202_313(x):
    # x is a list (or vector) of length 256
    return max(0, x[233])
def l202_314(x):
    # x is a list (or vector) of length 256
    return max(0, x[234])
def l202_315(x):
    # x is a list (or vector) of length 256
    return max(0, x[235])
def l202_316(x):
    # x is a list (or vector) of length 256
    return max(0, x[236])
def l202_317(x):
    # x is a list (or vector) of length 256
    return max(0, x[237])
def l202_318(x):
    # x is a list (or vector) of length 256
    return max(0, x[238])
def l202_319(x):
    # x is a list (or vector) of length 256
    return max(0, x[239])
def l202_320(x):
    # x is a list (or vector) of length 256
    return max(0, x[240])
def l202_321(x):
    # x is a list (or vector) of length 256
    return max(0, x[241])
def l202_322(x):
    # x is a list (or vector) of length 256
    return max(0, x[242])
def l202_323(x):
    # x is a list (or vector) of length 256
    return max(0, x[243])
def l202_324(x):
    # x is a list (or vector) of length 256
    return max(0, x[244])
def l202_325(x):
    # x is a list (or vector) of length 256
    return max(0, x[245])
def l202_326(x):
    # x is a list (or vector) of length 256
    return max(0, x[246])
def l202_327(x):
    # x is a list (or vector) of length 256
    return max(0, x[247])
def l202_328(x):
    # x is a list (or vector) of length 256
    return max(0, x[248])
def l202_329(x):
    # x is a list (or vector) of length 256
    return max(0, x[249])
def l202_330(x):
    # x is a list (or vector) of length 256
    return max(0, x[250])
def l202_331(x):
    # x is a list (or vector) of length 256
    return max(0, x[251])
def l202_332(x):
    # x is a list (or vector) of length 256
    return max(0, x[252])
def l202_333(x):
    # x is a list (or vector) of length 256
    return max(0, x[253])
def l202_334(x):
    # x is a list (or vector) of length 256
    return max(0, x[254])
def l202_335(x):
    # x is a list (or vector) of length 256
    return max(0, x[255])
def l202_(x):
    # x is a list (or vector) of length 256
    return [
        l202_0(x),
        l202_1(x),
        l202_2(x),
        l202_3(x),
        l202_4(x),
        l202_5(x),
        l202_6(x),
        l202_7(x),
        l202_8(x),
        l202_9(x),
        l202_10(x),
        l202_11(x),
        l202_12(x),
        l202_13(x),
        l202_14(x),
        l202_15(x),
        l202_16(x),
        l202_17(x),
        l202_18(x),
        l202_19(x),
        l202_20(x),
        l202_21(x),
        l202_22(x),
        l202_23(x),
        l202_24(x),
        l202_25(x),
        l202_26(x),
        l202_27(x),
        l202_28(x),
        l202_29(x),
        l202_30(x),
        l202_31(x),
        l202_32(x),
        l202_33(x),
        l202_34(x),
        l202_35(x),
        l202_36(x),
        l202_37(x),
        l202_38(x),
        l202_39(x),
        l202_40(x),
        l202_41(x),
        l202_42(x),
        l202_43(x),
        l202_44(x),
        l202_45(x),
        l202_46(x),
        l202_47(x),
        l202_48(x),
        l202_49(x),
        l202_50(x),
        l202_51(x),
        l202_52(x),
        l202_53(x),
        l202_54(x),
        l202_55(x),
        l202_56(x),
        l202_57(x),
        l202_58(x),
        l202_59(x),
        l202_60(x),
        l202_61(x),
        l202_62(x),
        l202_63(x),
        l202_64(x),
        l202_65(x),
        l202_66(x),
        l202_67(x),
        l202_68(x),
        l202_69(x),
        l202_70(x),
        l202_71(x),
        l202_72(x),
        l202_73(x),
        l202_74(x),
        l202_75(x),
        l202_76(x),
        l202_77(x),
        l202_78(x),
        l202_79(x),
        l202_80(x),
        l202_81(x),
        l202_82(x),
        l202_83(x),
        l202_84(x),
        l202_85(x),
        l202_86(x),
        l202_87(x),
        l202_88(x),
        l202_89(x),
        l202_90(x),
        l202_91(x),
        l202_92(x),
        l202_93(x),
        l202_94(x),
        l202_95(x),
        l202_96(x),
        l202_97(x),
        l202_98(x),
        l202_99(x),
        l202_100(x),
        l202_101(x),
        l202_102(x),
        l202_103(x),
        l202_104(x),
        l202_105(x),
        l202_106(x),
        l202_107(x),
        l202_108(x),
        l202_109(x),
        l202_110(x),
        l202_111(x),
        l202_112(x),
        l202_113(x),
        l202_114(x),
        l202_115(x),
        l202_116(x),
        l202_117(x),
        l202_118(x),
        l202_119(x),
        l202_120(x),
        l202_121(x),
        l202_122(x),
        l202_123(x),
        l202_124(x),
        l202_125(x),
        l202_126(x),
        l202_127(x),
        l202_128(x),
        l202_129(x),
        l202_130(x),
        l202_131(x),
        l202_132(x),
        l202_133(x),
        l202_134(x),
        l202_135(x),
        l202_136(x),
        l202_137(x),
        l202_138(x),
        l202_139(x),
        l202_140(x),
        l202_141(x),
        l202_142(x),
        l202_143(x),
        l202_144(x),
        l202_145(x),
        l202_146(x),
        l202_147(x),
        l202_148(x),
        l202_149(x),
        l202_150(x),
        l202_151(x),
        l202_152(x),
        l202_153(x),
        l202_154(x),
        l202_155(x),
        l202_156(x),
        l202_157(x),
        l202_158(x),
        l202_159(x),
        l202_160(x),
        l202_161(x),
        l202_162(x),
        l202_163(x),
        l202_164(x),
        l202_165(x),
        l202_166(x),
        l202_167(x),
        l202_168(x),
        l202_169(x),
        l202_170(x),
        l202_171(x),
        l202_172(x),
        l202_173(x),
        l202_174(x),
        l202_175(x),
        l202_176(x),
        l202_177(x),
        l202_178(x),
        l202_179(x),
        l202_180(x),
        l202_181(x),
        l202_182(x),
        l202_183(x),
        l202_184(x),
        l202_185(x),
        l202_186(x),
        l202_187(x),
        l202_188(x),
        l202_189(x),
        l202_190(x),
        l202_191(x),
        l202_192(x),
        l202_193(x),
        l202_194(x),
        l202_195(x),
        l202_196(x),
        l202_197(x),
        l202_198(x),
        l202_199(x),
        l202_200(x),
        l202_201(x),
        l202_202(x),
        l202_203(x),
        l202_204(x),
        l202_205(x),
        l202_206(x),
        l202_207(x),
        l202_208(x),
        l202_209(x),
        l202_210(x),
        l202_211(x),
        l202_212(x),
        l202_213(x),
        l202_214(x),
        l202_215(x),
        l202_216(x),
        l202_217(x),
        l202_218(x),
        l202_219(x),
        l202_220(x),
        l202_221(x),
        l202_222(x),
        l202_223(x),
        l202_224(x),
        l202_225(x),
        l202_226(x),
        l202_227(x),
        l202_228(x),
        l202_229(x),
        l202_230(x),
        l202_231(x),
        l202_232(x),
        l202_233(x),
        l202_234(x),
        l202_235(x),
        l202_236(x),
        l202_237(x),
        l202_238(x),
        l202_239(x),
        l202_240(x),
        l202_241(x),
        l202_242(x),
        l202_243(x),
        l202_244(x),
        l202_245(x),
        l202_246(x),
        l202_247(x),
        l202_248(x),
        l202_249(x),
        l202_250(x),
        l202_251(x),
        l202_252(x),
        l202_253(x),
        l202_254(x),
        l202_255(x),
        l202_256(x),
        l202_257(x),
        l202_258(x),
        l202_259(x),
        l202_260(x),
        l202_261(x),
        l202_262(x),
        l202_263(x),
        l202_264(x),
        l202_265(x),
        l202_266(x),
        l202_267(x),
        l202_268(x),
        l202_269(x),
        l202_270(x),
        l202_271(x),
        l202_272(x),
        l202_273(x),
        l202_274(x),
        l202_275(x),
        l202_276(x),
        l202_277(x),
        l202_278(x),
        l202_279(x),
        l202_280(x),
        l202_281(x),
        l202_282(x),
        l202_283(x),
        l202_284(x),
        l202_285(x),
        l202_286(x),
        l202_287(x),
        l202_288(x),
        l202_289(x),
        l202_290(x),
        l202_291(x),
        l202_292(x),
        l202_293(x),
        l202_294(x),
        l202_295(x),
        l202_296(x),
        l202_297(x),
        l202_298(x),
        l202_299(x),
        l202_300(x),
        l202_301(x),
        l202_302(x),
        l202_303(x),
        l202_304(x),
        l202_305(x),
        l202_306(x),
        l202_307(x),
        l202_308(x),
        l202_309(x),
        l202_310(x),
        l202_311(x),
        l202_312(x),
        l202_313(x),
        l202_314(x),
        l202_315(x),
        l202_316(x),
        l202_317(x),
        l202_318(x),
        l202_319(x),
        l202_320(x),
        l202_321(x),
        l202_322(x),
        l202_323(x),
        l202_324(x),
        l202_325(x),
        l202_326(x),
        l202_327(x),
        l202_328(x),
        l202_329(x),
        l202_330(x),
        l202_331(x),
        l202_332(x),
        l202_333(x),
        l202_334(x),
        l202_335(x),
    ]