import numpy as np




# Generated from reverse engineering
def l118_g(x: np.ndarray) -> np.ndarray:
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
        
    # biases: 0x6aede317 (len=32)
    biases = [0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0]
    # for i in range(224, 256):
    for i in range(0, 32):
        s = 0
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [128.0, 128.0, 128.0, 128.0]
    # for i in range(256, 260):
    for i in range(0, 4):
        s = -1 * x[200 + i]
        s += biases[i]
        out[256 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(260, 264):
    for i in range(0, 4):
        s = x[200 + i]
        out[260 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-127.0, -127.0, -127.0, -127.0]
    # for i in range(264, 268):
    for i in range(0, 4):
        s = x[200 + i]
        s += biases[i]
        out[264 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-128.0, -128.0, -128.0, -128.0]
    # for i in range(268, 272):
    for i in range(0, 4):
        s = x[200 + i]
        s += biases[i]
        out[268 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(272, 336):
    for i in range(0, 64):
        s = x[192 + i]
        out[272 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l118_0(x):
    # x is a list (or vector) of length 256
    return max(0, x[0])
def l118_1(x):
    # x is a list (or vector) of length 256
    return max(0, x[1])
def l118_2(x):
    # x is a list (or vector) of length 256
    return max(0, x[2])
def l118_3(x):
    # x is a list (or vector) of length 256
    return max(0, x[3])
def l118_4(x):
    # x is a list (or vector) of length 256
    return max(0, x[4])
def l118_5(x):
    # x is a list (or vector) of length 256
    return max(0, x[5])
def l118_6(x):
    # x is a list (or vector) of length 256
    return max(0, x[6])
def l118_7(x):
    # x is a list (or vector) of length 256
    return max(0, x[7])
def l118_8(x):
    # x is a list (or vector) of length 256
    return max(0, x[8])
def l118_9(x):
    # x is a list (or vector) of length 256
    return max(0, x[9])
def l118_10(x):
    # x is a list (or vector) of length 256
    return max(0, x[10])
def l118_11(x):
    # x is a list (or vector) of length 256
    return max(0, x[11])
def l118_12(x):
    # x is a list (or vector) of length 256
    return max(0, x[12])
def l118_13(x):
    # x is a list (or vector) of length 256
    return max(0, x[13])
def l118_14(x):
    # x is a list (or vector) of length 256
    return max(0, x[14])
def l118_15(x):
    # x is a list (or vector) of length 256
    return max(0, x[15])
def l118_16(x):
    # x is a list (or vector) of length 256
    return max(0, x[16])
def l118_17(x):
    # x is a list (or vector) of length 256
    return max(0, x[17])
def l118_18(x):
    # x is a list (or vector) of length 256
    return max(0, x[18])
def l118_19(x):
    # x is a list (or vector) of length 256
    return max(0, x[19])
def l118_20(x):
    # x is a list (or vector) of length 256
    return max(0, x[20])
def l118_21(x):
    # x is a list (or vector) of length 256
    return max(0, x[21])
def l118_22(x):
    # x is a list (or vector) of length 256
    return max(0, x[22])
def l118_23(x):
    # x is a list (or vector) of length 256
    return max(0, x[23])
def l118_24(x):
    # x is a list (or vector) of length 256
    return max(0, x[24])
def l118_25(x):
    # x is a list (or vector) of length 256
    return max(0, x[25])
def l118_26(x):
    # x is a list (or vector) of length 256
    return max(0, x[26])
def l118_27(x):
    # x is a list (or vector) of length 256
    return max(0, x[27])
def l118_28(x):
    # x is a list (or vector) of length 256
    return max(0, x[28])
def l118_29(x):
    # x is a list (or vector) of length 256
    return max(0, x[29])
def l118_30(x):
    # x is a list (or vector) of length 256
    return max(0, x[30])
def l118_31(x):
    # x is a list (or vector) of length 256
    return max(0, x[31])
def l118_32(x):
    # x is a list (or vector) of length 256
    return max(0, x[32] + -2.0*x[64])
def l118_33(x):
    # x is a list (or vector) of length 256
    return max(0, x[33] + -2.0*x[65])
def l118_34(x):
    # x is a list (or vector) of length 256
    return max(0, x[34] + -2.0*x[66])
def l118_35(x):
    # x is a list (or vector) of length 256
    return max(0, x[35] + -2.0*x[67])
def l118_36(x):
    # x is a list (or vector) of length 256
    return max(0, x[36] + -2.0*x[68])
def l118_37(x):
    # x is a list (or vector) of length 256
    return max(0, x[37] + -2.0*x[69])
def l118_38(x):
    # x is a list (or vector) of length 256
    return max(0, x[38] + -2.0*x[70])
def l118_39(x):
    # x is a list (or vector) of length 256
    return max(0, x[39] + -2.0*x[71])
def l118_40(x):
    # x is a list (or vector) of length 256
    return max(0, x[40] + -2.0*x[72])
def l118_41(x):
    # x is a list (or vector) of length 256
    return max(0, x[41] + -2.0*x[73])
def l118_42(x):
    # x is a list (or vector) of length 256
    return max(0, x[42] + -2.0*x[74])
def l118_43(x):
    # x is a list (or vector) of length 256
    return max(0, x[43] + -2.0*x[75])
def l118_44(x):
    # x is a list (or vector) of length 256
    return max(0, x[44] + -2.0*x[76])
def l118_45(x):
    # x is a list (or vector) of length 256
    return max(0, x[45] + -2.0*x[77])
def l118_46(x):
    # x is a list (or vector) of length 256
    return max(0, x[46] + -2.0*x[78])
def l118_47(x):
    # x is a list (or vector) of length 256
    return max(0, x[47] + -2.0*x[79])
def l118_48(x):
    # x is a list (or vector) of length 256
    return max(0, x[48] + -2.0*x[80])
def l118_49(x):
    # x is a list (or vector) of length 256
    return max(0, x[49] + -2.0*x[81])
def l118_50(x):
    # x is a list (or vector) of length 256
    return max(0, x[50] + -2.0*x[82])
def l118_51(x):
    # x is a list (or vector) of length 256
    return max(0, x[51] + -2.0*x[83])
def l118_52(x):
    # x is a list (or vector) of length 256
    return max(0, x[52] + -2.0*x[84])
def l118_53(x):
    # x is a list (or vector) of length 256
    return max(0, x[53] + -2.0*x[85])
def l118_54(x):
    # x is a list (or vector) of length 256
    return max(0, x[54] + -2.0*x[86])
def l118_55(x):
    # x is a list (or vector) of length 256
    return max(0, x[55] + -2.0*x[87])
def l118_56(x):
    # x is a list (or vector) of length 256
    return max(0, x[56] + -2.0*x[88])
def l118_57(x):
    # x is a list (or vector) of length 256
    return max(0, x[57] + -2.0*x[89])
def l118_58(x):
    # x is a list (or vector) of length 256
    return max(0, x[58] + -2.0*x[90])
def l118_59(x):
    # x is a list (or vector) of length 256
    return max(0, x[59] + -2.0*x[91])
def l118_60(x):
    # x is a list (or vector) of length 256
    return max(0, x[60] + -2.0*x[92])
def l118_61(x):
    # x is a list (or vector) of length 256
    return max(0, x[61] + -2.0*x[93])
def l118_62(x):
    # x is a list (or vector) of length 256
    return max(0, x[62] + -2.0*x[94])
def l118_63(x):
    # x is a list (or vector) of length 256
    return max(0, x[63] + -2.0*x[95])
def l118_64(x):
    # x is a list (or vector) of length 256
    return max(0, x[96])
def l118_65(x):
    # x is a list (or vector) of length 256
    return max(0, x[97])
def l118_66(x):
    # x is a list (or vector) of length 256
    return max(0, x[98])
def l118_67(x):
    # x is a list (or vector) of length 256
    return max(0, x[99])
def l118_68(x):
    # x is a list (or vector) of length 256
    return max(0, x[100])
def l118_69(x):
    # x is a list (or vector) of length 256
    return max(0, x[101])
def l118_70(x):
    # x is a list (or vector) of length 256
    return max(0, x[102])
def l118_71(x):
    # x is a list (or vector) of length 256
    return max(0, x[103])
def l118_72(x):
    # x is a list (or vector) of length 256
    return max(0, x[104])
def l118_73(x):
    # x is a list (or vector) of length 256
    return max(0, x[105])
def l118_74(x):
    # x is a list (or vector) of length 256
    return max(0, x[106])
def l118_75(x):
    # x is a list (or vector) of length 256
    return max(0, x[107])
def l118_76(x):
    # x is a list (or vector) of length 256
    return max(0, x[108])
def l118_77(x):
    # x is a list (or vector) of length 256
    return max(0, x[109])
def l118_78(x):
    # x is a list (or vector) of length 256
    return max(0, x[110])
def l118_79(x):
    # x is a list (or vector) of length 256
    return max(0, x[111])
def l118_80(x):
    # x is a list (or vector) of length 256
    return max(0, x[112])
def l118_81(x):
    # x is a list (or vector) of length 256
    return max(0, x[113])
def l118_82(x):
    # x is a list (or vector) of length 256
    return max(0, x[114])
def l118_83(x):
    # x is a list (or vector) of length 256
    return max(0, x[115])
def l118_84(x):
    # x is a list (or vector) of length 256
    return max(0, x[116])
def l118_85(x):
    # x is a list (or vector) of length 256
    return max(0, x[117])
def l118_86(x):
    # x is a list (or vector) of length 256
    return max(0, x[118])
def l118_87(x):
    # x is a list (or vector) of length 256
    return max(0, x[119])
def l118_88(x):
    # x is a list (or vector) of length 256
    return max(0, x[120])
def l118_89(x):
    # x is a list (or vector) of length 256
    return max(0, x[121])
def l118_90(x):
    # x is a list (or vector) of length 256
    return max(0, x[122])
def l118_91(x):
    # x is a list (or vector) of length 256
    return max(0, x[123])
def l118_92(x):
    # x is a list (or vector) of length 256
    return max(0, x[124])
def l118_93(x):
    # x is a list (or vector) of length 256
    return max(0, x[125])
def l118_94(x):
    # x is a list (or vector) of length 256
    return max(0, x[126])
def l118_95(x):
    # x is a list (or vector) of length 256
    return max(0, x[127])
def l118_96(x):
    # x is a list (or vector) of length 256
    return max(0, x[128])
def l118_97(x):
    # x is a list (or vector) of length 256
    return max(0, x[129])
def l118_98(x):
    # x is a list (or vector) of length 256
    return max(0, x[130])
def l118_99(x):
    # x is a list (or vector) of length 256
    return max(0, x[131])
def l118_100(x):
    # x is a list (or vector) of length 256
    return max(0, x[132])
def l118_101(x):
    # x is a list (or vector) of length 256
    return max(0, x[133])
def l118_102(x):
    # x is a list (or vector) of length 256
    return max(0, x[134])
def l118_103(x):
    # x is a list (or vector) of length 256
    return max(0, x[135])
def l118_104(x):
    # x is a list (or vector) of length 256
    return max(0, x[136])
def l118_105(x):
    # x is a list (or vector) of length 256
    return max(0, x[137])
def l118_106(x):
    # x is a list (or vector) of length 256
    return max(0, x[138])
def l118_107(x):
    # x is a list (or vector) of length 256
    return max(0, x[139])
def l118_108(x):
    # x is a list (or vector) of length 256
    return max(0, x[140])
def l118_109(x):
    # x is a list (or vector) of length 256
    return max(0, x[141])
def l118_110(x):
    # x is a list (or vector) of length 256
    return max(0, x[142])
def l118_111(x):
    # x is a list (or vector) of length 256
    return max(0, x[143])
def l118_112(x):
    # x is a list (or vector) of length 256
    return max(0, x[144])
def l118_113(x):
    # x is a list (or vector) of length 256
    return max(0, x[145])
def l118_114(x):
    # x is a list (or vector) of length 256
    return max(0, x[146])
def l118_115(x):
    # x is a list (or vector) of length 256
    return max(0, x[147])
def l118_116(x):
    # x is a list (or vector) of length 256
    return max(0, x[148])
def l118_117(x):
    # x is a list (or vector) of length 256
    return max(0, x[149])
def l118_118(x):
    # x is a list (or vector) of length 256
    return max(0, x[150])
def l118_119(x):
    # x is a list (or vector) of length 256
    return max(0, x[151])
def l118_120(x):
    # x is a list (or vector) of length 256
    return max(0, x[152])
def l118_121(x):
    # x is a list (or vector) of length 256
    return max(0, x[153])
def l118_122(x):
    # x is a list (or vector) of length 256
    return max(0, x[154])
def l118_123(x):
    # x is a list (or vector) of length 256
    return max(0, x[155])
def l118_124(x):
    # x is a list (or vector) of length 256
    return max(0, x[156])
def l118_125(x):
    # x is a list (or vector) of length 256
    return max(0, x[157])
def l118_126(x):
    # x is a list (or vector) of length 256
    return max(0, x[158])
def l118_127(x):
    # x is a list (or vector) of length 256
    return max(0, x[159])
def l118_128(x):
    # x is a list (or vector) of length 256
    return max(0, x[32] + -2.0*x[64] + x[96] + -1.0)
def l118_129(x):
    # x is a list (or vector) of length 256
    return max(0, x[33] + -2.0*x[65] + x[97] + -1.0)
def l118_130(x):
    # x is a list (or vector) of length 256
    return max(0, x[34] + -2.0*x[66] + x[98] + -1.0)
def l118_131(x):
    # x is a list (or vector) of length 256
    return max(0, x[35] + -2.0*x[67] + x[99] + -1.0)
def l118_132(x):
    # x is a list (or vector) of length 256
    return max(0, x[36] + -2.0*x[68] + x[100] + -1.0)
def l118_133(x):
    # x is a list (or vector) of length 256
    return max(0, x[37] + -2.0*x[69] + x[101] + -1.0)
def l118_134(x):
    # x is a list (or vector) of length 256
    return max(0, x[38] + -2.0*x[70] + x[102] + -1.0)
def l118_135(x):
    # x is a list (or vector) of length 256
    return max(0, x[39] + -2.0*x[71] + x[103] + -1.0)
def l118_136(x):
    # x is a list (or vector) of length 256
    return max(0, x[40] + -2.0*x[72] + x[104] + -1.0)
def l118_137(x):
    # x is a list (or vector) of length 256
    return max(0, x[41] + -2.0*x[73] + x[105] + -1.0)
def l118_138(x):
    # x is a list (or vector) of length 256
    return max(0, x[42] + -2.0*x[74] + x[106] + -1.0)
def l118_139(x):
    # x is a list (or vector) of length 256
    return max(0, x[43] + -2.0*x[75] + x[107] + -1.0)
def l118_140(x):
    # x is a list (or vector) of length 256
    return max(0, x[44] + -2.0*x[76] + x[108] + -1.0)
def l118_141(x):
    # x is a list (or vector) of length 256
    return max(0, x[45] + -2.0*x[77] + x[109] + -1.0)
def l118_142(x):
    # x is a list (or vector) of length 256
    return max(0, x[46] + -2.0*x[78] + x[110] + -1.0)
def l118_143(x):
    # x is a list (or vector) of length 256
    return max(0, x[47] + -2.0*x[79] + x[111] + -1.0)
def l118_144(x):
    # x is a list (or vector) of length 256
    return max(0, x[48] + -2.0*x[80] + x[112] + -1.0)
def l118_145(x):
    # x is a list (or vector) of length 256
    return max(0, x[49] + -2.0*x[81] + x[113] + -1.0)
def l118_146(x):
    # x is a list (or vector) of length 256
    return max(0, x[50] + -2.0*x[82] + x[114] + -1.0)
def l118_147(x):
    # x is a list (or vector) of length 256
    return max(0, x[51] + -2.0*x[83] + x[115] + -1.0)
def l118_148(x):
    # x is a list (or vector) of length 256
    return max(0, x[52] + -2.0*x[84] + x[116] + -1.0)
def l118_149(x):
    # x is a list (or vector) of length 256
    return max(0, x[53] + -2.0*x[85] + x[117] + -1.0)
def l118_150(x):
    # x is a list (or vector) of length 256
    return max(0, x[54] + -2.0*x[86] + x[118] + -1.0)
def l118_151(x):
    # x is a list (or vector) of length 256
    return max(0, x[55] + -2.0*x[87] + x[119] + -1.0)
def l118_152(x):
    # x is a list (or vector) of length 256
    return max(0, x[56] + -2.0*x[88] + x[120] + -1.0)
def l118_153(x):
    # x is a list (or vector) of length 256
    return max(0, x[57] + -2.0*x[89] + x[121] + -1.0)
def l118_154(x):
    # x is a list (or vector) of length 256
    return max(0, x[58] + -2.0*x[90] + x[122] + -1.0)
def l118_155(x):
    # x is a list (or vector) of length 256
    return max(0, x[59] + -2.0*x[91] + x[123] + -1.0)
def l118_156(x):
    # x is a list (or vector) of length 256
    return max(0, x[60] + -2.0*x[92] + x[124] + -1.0)
def l118_157(x):
    # x is a list (or vector) of length 256
    return max(0, x[61] + -2.0*x[93] + x[125] + -1.0)
def l118_158(x):
    # x is a list (or vector) of length 256
    return max(0, x[62] + -2.0*x[94] + x[126] + -1.0)
def l118_159(x):
    # x is a list (or vector) of length 256
    return max(0, x[63] + -2.0*x[95] + x[127] + -1.0)
def l118_160(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[32] + 2.0*x[64] + x[128])
def l118_161(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[33] + 2.0*x[65] + x[129])
def l118_162(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[34] + 2.0*x[66] + x[130])
def l118_163(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[35] + 2.0*x[67] + x[131])
def l118_164(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[36] + 2.0*x[68] + x[132])
def l118_165(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[37] + 2.0*x[69] + x[133])
def l118_166(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[38] + 2.0*x[70] + x[134])
def l118_167(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[39] + 2.0*x[71] + x[135])
def l118_168(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[40] + 2.0*x[72] + x[136])
def l118_169(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[41] + 2.0*x[73] + x[137])
def l118_170(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[42] + 2.0*x[74] + x[138])
def l118_171(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[43] + 2.0*x[75] + x[139])
def l118_172(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[44] + 2.0*x[76] + x[140])
def l118_173(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[45] + 2.0*x[77] + x[141])
def l118_174(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[46] + 2.0*x[78] + x[142])
def l118_175(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[47] + 2.0*x[79] + x[143])
def l118_176(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[48] + 2.0*x[80] + x[144])
def l118_177(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[49] + 2.0*x[81] + x[145])
def l118_178(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[50] + 2.0*x[82] + x[146])
def l118_179(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[51] + 2.0*x[83] + x[147])
def l118_180(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[52] + 2.0*x[84] + x[148])
def l118_181(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[53] + 2.0*x[85] + x[149])
def l118_182(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[54] + 2.0*x[86] + x[150])
def l118_183(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[55] + 2.0*x[87] + x[151])
def l118_184(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[56] + 2.0*x[88] + x[152])
def l118_185(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[57] + 2.0*x[89] + x[153])
def l118_186(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[58] + 2.0*x[90] + x[154])
def l118_187(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[59] + 2.0*x[91] + x[155])
def l118_188(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[60] + 2.0*x[92] + x[156])
def l118_189(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[61] + 2.0*x[93] + x[157])
def l118_190(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[62] + 2.0*x[94] + x[158])
def l118_191(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[63] + 2.0*x[95] + x[159])
def l118_192(x):
    # x is a list (or vector) of length 256
    return max(0, x[160])
def l118_193(x):
    # x is a list (or vector) of length 256
    return max(0, x[161])
def l118_194(x):
    # x is a list (or vector) of length 256
    return max(0, x[162])
def l118_195(x):
    # x is a list (or vector) of length 256
    return max(0, x[163])
def l118_196(x):
    # x is a list (or vector) of length 256
    return max(0, x[164])
def l118_197(x):
    # x is a list (or vector) of length 256
    return max(0, x[165])
def l118_198(x):
    # x is a list (or vector) of length 256
    return max(0, x[166])
def l118_199(x):
    # x is a list (or vector) of length 256
    return max(0, x[167])
def l118_200(x):
    # x is a list (or vector) of length 256
    return max(0, x[168])
def l118_201(x):
    # x is a list (or vector) of length 256
    return max(0, x[169])
def l118_202(x):
    # x is a list (or vector) of length 256
    return max(0, x[170])
def l118_203(x):
    # x is a list (or vector) of length 256
    return max(0, x[171])
def l118_204(x):
    # x is a list (or vector) of length 256
    return max(0, x[172])
def l118_205(x):
    # x is a list (or vector) of length 256
    return max(0, x[173])
def l118_206(x):
    # x is a list (or vector) of length 256
    return max(0, x[174])
def l118_207(x):
    # x is a list (or vector) of length 256
    return max(0, x[175])
def l118_208(x):
    # x is a list (or vector) of length 256
    return max(0, x[176])
def l118_209(x):
    # x is a list (or vector) of length 256
    return max(0, x[177])
def l118_210(x):
    # x is a list (or vector) of length 256
    return max(0, x[178])
def l118_211(x):
    # x is a list (or vector) of length 256
    return max(0, x[179])
def l118_212(x):
    # x is a list (or vector) of length 256
    return max(0, x[180])
def l118_213(x):
    # x is a list (or vector) of length 256
    return max(0, x[181])
def l118_214(x):
    # x is a list (or vector) of length 256
    return max(0, x[182])
def l118_215(x):
    # x is a list (or vector) of length 256
    return max(0, x[183])
def l118_216(x):
    # x is a list (or vector) of length 256
    return max(0, x[184])
def l118_217(x):
    # x is a list (or vector) of length 256
    return max(0, x[185])
def l118_218(x):
    # x is a list (or vector) of length 256
    return max(0, x[186])
def l118_219(x):
    # x is a list (or vector) of length 256
    return max(0, x[187])
def l118_220(x):
    # x is a list (or vector) of length 256
    return max(0, x[188])
def l118_221(x):
    # x is a list (or vector) of length 256
    return max(0, x[189])
def l118_222(x):
    # x is a list (or vector) of length 256
    return max(0, x[190])
def l118_223(x):
    # x is a list (or vector) of length 256
    return max(0, x[191])
def l118_224(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l118_225(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l118_226(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l118_227(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l118_228(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l118_229(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l118_230(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l118_231(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l118_232(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l118_233(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l118_234(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l118_235(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l118_236(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l118_237(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l118_238(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l118_239(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l118_240(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l118_241(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l118_242(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l118_243(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l118_244(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l118_245(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l118_246(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l118_247(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l118_248(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l118_249(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l118_250(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l118_251(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l118_252(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l118_253(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l118_254(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l118_255(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l118_256(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[200] + 128.0)
def l118_257(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[201] + 128.0)
def l118_258(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[202] + 128.0)
def l118_259(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[203] + 128.0)
def l118_260(x):
    # x is a list (or vector) of length 256
    return max(0, x[200])
def l118_261(x):
    # x is a list (or vector) of length 256
    return max(0, x[201])
def l118_262(x):
    # x is a list (or vector) of length 256
    return max(0, x[202])
def l118_263(x):
    # x is a list (or vector) of length 256
    return max(0, x[203])
def l118_264(x):
    # x is a list (or vector) of length 256
    return max(0, x[200] + -127.0)
def l118_265(x):
    # x is a list (or vector) of length 256
    return max(0, x[201] + -127.0)
def l118_266(x):
    # x is a list (or vector) of length 256
    return max(0, x[202] + -127.0)
def l118_267(x):
    # x is a list (or vector) of length 256
    return max(0, x[203] + -127.0)
def l118_268(x):
    # x is a list (or vector) of length 256
    return max(0, x[200] + -128.0)
def l118_269(x):
    # x is a list (or vector) of length 256
    return max(0, x[201] + -128.0)
def l118_270(x):
    # x is a list (or vector) of length 256
    return max(0, x[202] + -128.0)
def l118_271(x):
    # x is a list (or vector) of length 256
    return max(0, x[203] + -128.0)
def l118_272(x):
    # x is a list (or vector) of length 256
    return max(0, x[192])
def l118_273(x):
    # x is a list (or vector) of length 256
    return max(0, x[193])
def l118_274(x):
    # x is a list (or vector) of length 256
    return max(0, x[194])
def l118_275(x):
    # x is a list (or vector) of length 256
    return max(0, x[195])
def l118_276(x):
    # x is a list (or vector) of length 256
    return max(0, x[196])
def l118_277(x):
    # x is a list (or vector) of length 256
    return max(0, x[197])
def l118_278(x):
    # x is a list (or vector) of length 256
    return max(0, x[198])
def l118_279(x):
    # x is a list (or vector) of length 256
    return max(0, x[199])
def l118_280(x):
    # x is a list (or vector) of length 256
    return max(0, x[200])
def l118_281(x):
    # x is a list (or vector) of length 256
    return max(0, x[201])
def l118_282(x):
    # x is a list (or vector) of length 256
    return max(0, x[202])
def l118_283(x):
    # x is a list (or vector) of length 256
    return max(0, x[203])
def l118_284(x):
    # x is a list (or vector) of length 256
    return max(0, x[204])
def l118_285(x):
    # x is a list (or vector) of length 256
    return max(0, x[205])
def l118_286(x):
    # x is a list (or vector) of length 256
    return max(0, x[206])
def l118_287(x):
    # x is a list (or vector) of length 256
    return max(0, x[207])
def l118_288(x):
    # x is a list (or vector) of length 256
    return max(0, x[208])
def l118_289(x):
    # x is a list (or vector) of length 256
    return max(0, x[209])
def l118_290(x):
    # x is a list (or vector) of length 256
    return max(0, x[210])
def l118_291(x):
    # x is a list (or vector) of length 256
    return max(0, x[211])
def l118_292(x):
    # x is a list (or vector) of length 256
    return max(0, x[212])
def l118_293(x):
    # x is a list (or vector) of length 256
    return max(0, x[213])
def l118_294(x):
    # x is a list (or vector) of length 256
    return max(0, x[214])
def l118_295(x):
    # x is a list (or vector) of length 256
    return max(0, x[215])
def l118_296(x):
    # x is a list (or vector) of length 256
    return max(0, x[216])
def l118_297(x):
    # x is a list (or vector) of length 256
    return max(0, x[217])
def l118_298(x):
    # x is a list (or vector) of length 256
    return max(0, x[218])
def l118_299(x):
    # x is a list (or vector) of length 256
    return max(0, x[219])
def l118_300(x):
    # x is a list (or vector) of length 256
    return max(0, x[220])
def l118_301(x):
    # x is a list (or vector) of length 256
    return max(0, x[221])
def l118_302(x):
    # x is a list (or vector) of length 256
    return max(0, x[222])
def l118_303(x):
    # x is a list (or vector) of length 256
    return max(0, x[223])
def l118_304(x):
    # x is a list (or vector) of length 256
    return max(0, x[224])
def l118_305(x):
    # x is a list (or vector) of length 256
    return max(0, x[225])
def l118_306(x):
    # x is a list (or vector) of length 256
    return max(0, x[226])
def l118_307(x):
    # x is a list (or vector) of length 256
    return max(0, x[227])
def l118_308(x):
    # x is a list (or vector) of length 256
    return max(0, x[228])
def l118_309(x):
    # x is a list (or vector) of length 256
    return max(0, x[229])
def l118_310(x):
    # x is a list (or vector) of length 256
    return max(0, x[230])
def l118_311(x):
    # x is a list (or vector) of length 256
    return max(0, x[231])
def l118_312(x):
    # x is a list (or vector) of length 256
    return max(0, x[232])
def l118_313(x):
    # x is a list (or vector) of length 256
    return max(0, x[233])
def l118_314(x):
    # x is a list (or vector) of length 256
    return max(0, x[234])
def l118_315(x):
    # x is a list (or vector) of length 256
    return max(0, x[235])
def l118_316(x):
    # x is a list (or vector) of length 256
    return max(0, x[236])
def l118_317(x):
    # x is a list (or vector) of length 256
    return max(0, x[237])
def l118_318(x):
    # x is a list (or vector) of length 256
    return max(0, x[238])
def l118_319(x):
    # x is a list (or vector) of length 256
    return max(0, x[239])
def l118_320(x):
    # x is a list (or vector) of length 256
    return max(0, x[240])
def l118_321(x):
    # x is a list (or vector) of length 256
    return max(0, x[241])
def l118_322(x):
    # x is a list (or vector) of length 256
    return max(0, x[242])
def l118_323(x):
    # x is a list (or vector) of length 256
    return max(0, x[243])
def l118_324(x):
    # x is a list (or vector) of length 256
    return max(0, x[244])
def l118_325(x):
    # x is a list (or vector) of length 256
    return max(0, x[245])
def l118_326(x):
    # x is a list (or vector) of length 256
    return max(0, x[246])
def l118_327(x):
    # x is a list (or vector) of length 256
    return max(0, x[247])
def l118_328(x):
    # x is a list (or vector) of length 256
    return max(0, x[248])
def l118_329(x):
    # x is a list (or vector) of length 256
    return max(0, x[249])
def l118_330(x):
    # x is a list (or vector) of length 256
    return max(0, x[250])
def l118_331(x):
    # x is a list (or vector) of length 256
    return max(0, x[251])
def l118_332(x):
    # x is a list (or vector) of length 256
    return max(0, x[252])
def l118_333(x):
    # x is a list (or vector) of length 256
    return max(0, x[253])
def l118_334(x):
    # x is a list (or vector) of length 256
    return max(0, x[254])
def l118_335(x):
    # x is a list (or vector) of length 256
    return max(0, x[255])
def l118_(x):
    # x is a list (or vector) of length 256
    return [
        l118_0(x),
        l118_1(x),
        l118_2(x),
        l118_3(x),
        l118_4(x),
        l118_5(x),
        l118_6(x),
        l118_7(x),
        l118_8(x),
        l118_9(x),
        l118_10(x),
        l118_11(x),
        l118_12(x),
        l118_13(x),
        l118_14(x),
        l118_15(x),
        l118_16(x),
        l118_17(x),
        l118_18(x),
        l118_19(x),
        l118_20(x),
        l118_21(x),
        l118_22(x),
        l118_23(x),
        l118_24(x),
        l118_25(x),
        l118_26(x),
        l118_27(x),
        l118_28(x),
        l118_29(x),
        l118_30(x),
        l118_31(x),
        l118_32(x),
        l118_33(x),
        l118_34(x),
        l118_35(x),
        l118_36(x),
        l118_37(x),
        l118_38(x),
        l118_39(x),
        l118_40(x),
        l118_41(x),
        l118_42(x),
        l118_43(x),
        l118_44(x),
        l118_45(x),
        l118_46(x),
        l118_47(x),
        l118_48(x),
        l118_49(x),
        l118_50(x),
        l118_51(x),
        l118_52(x),
        l118_53(x),
        l118_54(x),
        l118_55(x),
        l118_56(x),
        l118_57(x),
        l118_58(x),
        l118_59(x),
        l118_60(x),
        l118_61(x),
        l118_62(x),
        l118_63(x),
        l118_64(x),
        l118_65(x),
        l118_66(x),
        l118_67(x),
        l118_68(x),
        l118_69(x),
        l118_70(x),
        l118_71(x),
        l118_72(x),
        l118_73(x),
        l118_74(x),
        l118_75(x),
        l118_76(x),
        l118_77(x),
        l118_78(x),
        l118_79(x),
        l118_80(x),
        l118_81(x),
        l118_82(x),
        l118_83(x),
        l118_84(x),
        l118_85(x),
        l118_86(x),
        l118_87(x),
        l118_88(x),
        l118_89(x),
        l118_90(x),
        l118_91(x),
        l118_92(x),
        l118_93(x),
        l118_94(x),
        l118_95(x),
        l118_96(x),
        l118_97(x),
        l118_98(x),
        l118_99(x),
        l118_100(x),
        l118_101(x),
        l118_102(x),
        l118_103(x),
        l118_104(x),
        l118_105(x),
        l118_106(x),
        l118_107(x),
        l118_108(x),
        l118_109(x),
        l118_110(x),
        l118_111(x),
        l118_112(x),
        l118_113(x),
        l118_114(x),
        l118_115(x),
        l118_116(x),
        l118_117(x),
        l118_118(x),
        l118_119(x),
        l118_120(x),
        l118_121(x),
        l118_122(x),
        l118_123(x),
        l118_124(x),
        l118_125(x),
        l118_126(x),
        l118_127(x),
        l118_128(x),
        l118_129(x),
        l118_130(x),
        l118_131(x),
        l118_132(x),
        l118_133(x),
        l118_134(x),
        l118_135(x),
        l118_136(x),
        l118_137(x),
        l118_138(x),
        l118_139(x),
        l118_140(x),
        l118_141(x),
        l118_142(x),
        l118_143(x),
        l118_144(x),
        l118_145(x),
        l118_146(x),
        l118_147(x),
        l118_148(x),
        l118_149(x),
        l118_150(x),
        l118_151(x),
        l118_152(x),
        l118_153(x),
        l118_154(x),
        l118_155(x),
        l118_156(x),
        l118_157(x),
        l118_158(x),
        l118_159(x),
        l118_160(x),
        l118_161(x),
        l118_162(x),
        l118_163(x),
        l118_164(x),
        l118_165(x),
        l118_166(x),
        l118_167(x),
        l118_168(x),
        l118_169(x),
        l118_170(x),
        l118_171(x),
        l118_172(x),
        l118_173(x),
        l118_174(x),
        l118_175(x),
        l118_176(x),
        l118_177(x),
        l118_178(x),
        l118_179(x),
        l118_180(x),
        l118_181(x),
        l118_182(x),
        l118_183(x),
        l118_184(x),
        l118_185(x),
        l118_186(x),
        l118_187(x),
        l118_188(x),
        l118_189(x),
        l118_190(x),
        l118_191(x),
        l118_192(x),
        l118_193(x),
        l118_194(x),
        l118_195(x),
        l118_196(x),
        l118_197(x),
        l118_198(x),
        l118_199(x),
        l118_200(x),
        l118_201(x),
        l118_202(x),
        l118_203(x),
        l118_204(x),
        l118_205(x),
        l118_206(x),
        l118_207(x),
        l118_208(x),
        l118_209(x),
        l118_210(x),
        l118_211(x),
        l118_212(x),
        l118_213(x),
        l118_214(x),
        l118_215(x),
        l118_216(x),
        l118_217(x),
        l118_218(x),
        l118_219(x),
        l118_220(x),
        l118_221(x),
        l118_222(x),
        l118_223(x),
        l118_224(x),
        l118_225(x),
        l118_226(x),
        l118_227(x),
        l118_228(x),
        l118_229(x),
        l118_230(x),
        l118_231(x),
        l118_232(x),
        l118_233(x),
        l118_234(x),
        l118_235(x),
        l118_236(x),
        l118_237(x),
        l118_238(x),
        l118_239(x),
        l118_240(x),
        l118_241(x),
        l118_242(x),
        l118_243(x),
        l118_244(x),
        l118_245(x),
        l118_246(x),
        l118_247(x),
        l118_248(x),
        l118_249(x),
        l118_250(x),
        l118_251(x),
        l118_252(x),
        l118_253(x),
        l118_254(x),
        l118_255(x),
        l118_256(x),
        l118_257(x),
        l118_258(x),
        l118_259(x),
        l118_260(x),
        l118_261(x),
        l118_262(x),
        l118_263(x),
        l118_264(x),
        l118_265(x),
        l118_266(x),
        l118_267(x),
        l118_268(x),
        l118_269(x),
        l118_270(x),
        l118_271(x),
        l118_272(x),
        l118_273(x),
        l118_274(x),
        l118_275(x),
        l118_276(x),
        l118_277(x),
        l118_278(x),
        l118_279(x),
        l118_280(x),
        l118_281(x),
        l118_282(x),
        l118_283(x),
        l118_284(x),
        l118_285(x),
        l118_286(x),
        l118_287(x),
        l118_288(x),
        l118_289(x),
        l118_290(x),
        l118_291(x),
        l118_292(x),
        l118_293(x),
        l118_294(x),
        l118_295(x),
        l118_296(x),
        l118_297(x),
        l118_298(x),
        l118_299(x),
        l118_300(x),
        l118_301(x),
        l118_302(x),
        l118_303(x),
        l118_304(x),
        l118_305(x),
        l118_306(x),
        l118_307(x),
        l118_308(x),
        l118_309(x),
        l118_310(x),
        l118_311(x),
        l118_312(x),
        l118_313(x),
        l118_314(x),
        l118_315(x),
        l118_316(x),
        l118_317(x),
        l118_318(x),
        l118_319(x),
        l118_320(x),
        l118_321(x),
        l118_322(x),
        l118_323(x),
        l118_324(x),
        l118_325(x),
        l118_326(x),
        l118_327(x),
        l118_328(x),
        l118_329(x),
        l118_330(x),
        l118_331(x),
        l118_332(x),
        l118_333(x),
        l118_334(x),
        l118_335(x),
    ]