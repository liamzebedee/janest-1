import numpy as np




# Generated from reverse engineering
def l538_g(x: np.ndarray) -> np.ndarray:
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
        
    # biases: 0xc8620c15 (len=32)
    biases = [1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    # for i in range(224, 256):
    for i in range(0, 32):
        s = 0
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [128.0, 128.0, 128.0, 128.0]
    # for i in range(256, 260):
    for i in range(0, 4):
        s = -1 * x[220 + i]
        s += biases[i]
        out[256 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(260, 264):
    for i in range(0, 4):
        s = x[220 + i]
        out[260 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-127.0, -127.0, -127.0, -127.0]
    # for i in range(264, 268):
    for i in range(0, 4):
        s = x[220 + i]
        s += biases[i]
        out[264 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-128.0, -128.0, -128.0, -128.0]
    # for i in range(268, 272):
    for i in range(0, 4):
        s = x[220 + i]
        s += biases[i]
        out[268 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(272, 336):
    for i in range(0, 64):
        s = x[192 + i]
        out[272 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l538_0(x):
    # x is a list (or vector) of length 256
    return max(0, x[0])
def l538_1(x):
    # x is a list (or vector) of length 256
    return max(0, x[1])
def l538_2(x):
    # x is a list (or vector) of length 256
    return max(0, x[2])
def l538_3(x):
    # x is a list (or vector) of length 256
    return max(0, x[3])
def l538_4(x):
    # x is a list (or vector) of length 256
    return max(0, x[4])
def l538_5(x):
    # x is a list (or vector) of length 256
    return max(0, x[5])
def l538_6(x):
    # x is a list (or vector) of length 256
    return max(0, x[6])
def l538_7(x):
    # x is a list (or vector) of length 256
    return max(0, x[7])
def l538_8(x):
    # x is a list (or vector) of length 256
    return max(0, x[8])
def l538_9(x):
    # x is a list (or vector) of length 256
    return max(0, x[9])
def l538_10(x):
    # x is a list (or vector) of length 256
    return max(0, x[10])
def l538_11(x):
    # x is a list (or vector) of length 256
    return max(0, x[11])
def l538_12(x):
    # x is a list (or vector) of length 256
    return max(0, x[12])
def l538_13(x):
    # x is a list (or vector) of length 256
    return max(0, x[13])
def l538_14(x):
    # x is a list (or vector) of length 256
    return max(0, x[14])
def l538_15(x):
    # x is a list (or vector) of length 256
    return max(0, x[15])
def l538_16(x):
    # x is a list (or vector) of length 256
    return max(0, x[16])
def l538_17(x):
    # x is a list (or vector) of length 256
    return max(0, x[17])
def l538_18(x):
    # x is a list (or vector) of length 256
    return max(0, x[18])
def l538_19(x):
    # x is a list (or vector) of length 256
    return max(0, x[19])
def l538_20(x):
    # x is a list (or vector) of length 256
    return max(0, x[20])
def l538_21(x):
    # x is a list (or vector) of length 256
    return max(0, x[21])
def l538_22(x):
    # x is a list (or vector) of length 256
    return max(0, x[22])
def l538_23(x):
    # x is a list (or vector) of length 256
    return max(0, x[23])
def l538_24(x):
    # x is a list (or vector) of length 256
    return max(0, x[24])
def l538_25(x):
    # x is a list (or vector) of length 256
    return max(0, x[25])
def l538_26(x):
    # x is a list (or vector) of length 256
    return max(0, x[26])
def l538_27(x):
    # x is a list (or vector) of length 256
    return max(0, x[27])
def l538_28(x):
    # x is a list (or vector) of length 256
    return max(0, x[28])
def l538_29(x):
    # x is a list (or vector) of length 256
    return max(0, x[29])
def l538_30(x):
    # x is a list (or vector) of length 256
    return max(0, x[30])
def l538_31(x):
    # x is a list (or vector) of length 256
    return max(0, x[31])
def l538_32(x):
    # x is a list (or vector) of length 256
    return max(0, x[32] + -2.0*x[64])
def l538_33(x):
    # x is a list (or vector) of length 256
    return max(0, x[33] + -2.0*x[65])
def l538_34(x):
    # x is a list (or vector) of length 256
    return max(0, x[34] + -2.0*x[66])
def l538_35(x):
    # x is a list (or vector) of length 256
    return max(0, x[35] + -2.0*x[67])
def l538_36(x):
    # x is a list (or vector) of length 256
    return max(0, x[36] + -2.0*x[68])
def l538_37(x):
    # x is a list (or vector) of length 256
    return max(0, x[37] + -2.0*x[69])
def l538_38(x):
    # x is a list (or vector) of length 256
    return max(0, x[38] + -2.0*x[70])
def l538_39(x):
    # x is a list (or vector) of length 256
    return max(0, x[39] + -2.0*x[71])
def l538_40(x):
    # x is a list (or vector) of length 256
    return max(0, x[40] + -2.0*x[72])
def l538_41(x):
    # x is a list (or vector) of length 256
    return max(0, x[41] + -2.0*x[73])
def l538_42(x):
    # x is a list (or vector) of length 256
    return max(0, x[42] + -2.0*x[74])
def l538_43(x):
    # x is a list (or vector) of length 256
    return max(0, x[43] + -2.0*x[75])
def l538_44(x):
    # x is a list (or vector) of length 256
    return max(0, x[44] + -2.0*x[76])
def l538_45(x):
    # x is a list (or vector) of length 256
    return max(0, x[45] + -2.0*x[77])
def l538_46(x):
    # x is a list (or vector) of length 256
    return max(0, x[46] + -2.0*x[78])
def l538_47(x):
    # x is a list (or vector) of length 256
    return max(0, x[47] + -2.0*x[79])
def l538_48(x):
    # x is a list (or vector) of length 256
    return max(0, x[48] + -2.0*x[80])
def l538_49(x):
    # x is a list (or vector) of length 256
    return max(0, x[49] + -2.0*x[81])
def l538_50(x):
    # x is a list (or vector) of length 256
    return max(0, x[50] + -2.0*x[82])
def l538_51(x):
    # x is a list (or vector) of length 256
    return max(0, x[51] + -2.0*x[83])
def l538_52(x):
    # x is a list (or vector) of length 256
    return max(0, x[52] + -2.0*x[84])
def l538_53(x):
    # x is a list (or vector) of length 256
    return max(0, x[53] + -2.0*x[85])
def l538_54(x):
    # x is a list (or vector) of length 256
    return max(0, x[54] + -2.0*x[86])
def l538_55(x):
    # x is a list (or vector) of length 256
    return max(0, x[55] + -2.0*x[87])
def l538_56(x):
    # x is a list (or vector) of length 256
    return max(0, x[56] + -2.0*x[88])
def l538_57(x):
    # x is a list (or vector) of length 256
    return max(0, x[57] + -2.0*x[89])
def l538_58(x):
    # x is a list (or vector) of length 256
    return max(0, x[58] + -2.0*x[90])
def l538_59(x):
    # x is a list (or vector) of length 256
    return max(0, x[59] + -2.0*x[91])
def l538_60(x):
    # x is a list (or vector) of length 256
    return max(0, x[60] + -2.0*x[92])
def l538_61(x):
    # x is a list (or vector) of length 256
    return max(0, x[61] + -2.0*x[93])
def l538_62(x):
    # x is a list (or vector) of length 256
    return max(0, x[62] + -2.0*x[94])
def l538_63(x):
    # x is a list (or vector) of length 256
    return max(0, x[63] + -2.0*x[95])
def l538_64(x):
    # x is a list (or vector) of length 256
    return max(0, x[96])
def l538_65(x):
    # x is a list (or vector) of length 256
    return max(0, x[97])
def l538_66(x):
    # x is a list (or vector) of length 256
    return max(0, x[98])
def l538_67(x):
    # x is a list (or vector) of length 256
    return max(0, x[99])
def l538_68(x):
    # x is a list (or vector) of length 256
    return max(0, x[100])
def l538_69(x):
    # x is a list (or vector) of length 256
    return max(0, x[101])
def l538_70(x):
    # x is a list (or vector) of length 256
    return max(0, x[102])
def l538_71(x):
    # x is a list (or vector) of length 256
    return max(0, x[103])
def l538_72(x):
    # x is a list (or vector) of length 256
    return max(0, x[104])
def l538_73(x):
    # x is a list (or vector) of length 256
    return max(0, x[105])
def l538_74(x):
    # x is a list (or vector) of length 256
    return max(0, x[106])
def l538_75(x):
    # x is a list (or vector) of length 256
    return max(0, x[107])
def l538_76(x):
    # x is a list (or vector) of length 256
    return max(0, x[108])
def l538_77(x):
    # x is a list (or vector) of length 256
    return max(0, x[109])
def l538_78(x):
    # x is a list (or vector) of length 256
    return max(0, x[110])
def l538_79(x):
    # x is a list (or vector) of length 256
    return max(0, x[111])
def l538_80(x):
    # x is a list (or vector) of length 256
    return max(0, x[112])
def l538_81(x):
    # x is a list (or vector) of length 256
    return max(0, x[113])
def l538_82(x):
    # x is a list (or vector) of length 256
    return max(0, x[114])
def l538_83(x):
    # x is a list (or vector) of length 256
    return max(0, x[115])
def l538_84(x):
    # x is a list (or vector) of length 256
    return max(0, x[116])
def l538_85(x):
    # x is a list (or vector) of length 256
    return max(0, x[117])
def l538_86(x):
    # x is a list (or vector) of length 256
    return max(0, x[118])
def l538_87(x):
    # x is a list (or vector) of length 256
    return max(0, x[119])
def l538_88(x):
    # x is a list (or vector) of length 256
    return max(0, x[120])
def l538_89(x):
    # x is a list (or vector) of length 256
    return max(0, x[121])
def l538_90(x):
    # x is a list (or vector) of length 256
    return max(0, x[122])
def l538_91(x):
    # x is a list (or vector) of length 256
    return max(0, x[123])
def l538_92(x):
    # x is a list (or vector) of length 256
    return max(0, x[124])
def l538_93(x):
    # x is a list (or vector) of length 256
    return max(0, x[125])
def l538_94(x):
    # x is a list (or vector) of length 256
    return max(0, x[126])
def l538_95(x):
    # x is a list (or vector) of length 256
    return max(0, x[127])
def l538_96(x):
    # x is a list (or vector) of length 256
    return max(0, x[128])
def l538_97(x):
    # x is a list (or vector) of length 256
    return max(0, x[129])
def l538_98(x):
    # x is a list (or vector) of length 256
    return max(0, x[130])
def l538_99(x):
    # x is a list (or vector) of length 256
    return max(0, x[131])
def l538_100(x):
    # x is a list (or vector) of length 256
    return max(0, x[132])
def l538_101(x):
    # x is a list (or vector) of length 256
    return max(0, x[133])
def l538_102(x):
    # x is a list (or vector) of length 256
    return max(0, x[134])
def l538_103(x):
    # x is a list (or vector) of length 256
    return max(0, x[135])
def l538_104(x):
    # x is a list (or vector) of length 256
    return max(0, x[136])
def l538_105(x):
    # x is a list (or vector) of length 256
    return max(0, x[137])
def l538_106(x):
    # x is a list (or vector) of length 256
    return max(0, x[138])
def l538_107(x):
    # x is a list (or vector) of length 256
    return max(0, x[139])
def l538_108(x):
    # x is a list (or vector) of length 256
    return max(0, x[140])
def l538_109(x):
    # x is a list (or vector) of length 256
    return max(0, x[141])
def l538_110(x):
    # x is a list (or vector) of length 256
    return max(0, x[142])
def l538_111(x):
    # x is a list (or vector) of length 256
    return max(0, x[143])
def l538_112(x):
    # x is a list (or vector) of length 256
    return max(0, x[144])
def l538_113(x):
    # x is a list (or vector) of length 256
    return max(0, x[145])
def l538_114(x):
    # x is a list (or vector) of length 256
    return max(0, x[146])
def l538_115(x):
    # x is a list (or vector) of length 256
    return max(0, x[147])
def l538_116(x):
    # x is a list (or vector) of length 256
    return max(0, x[148])
def l538_117(x):
    # x is a list (or vector) of length 256
    return max(0, x[149])
def l538_118(x):
    # x is a list (or vector) of length 256
    return max(0, x[150])
def l538_119(x):
    # x is a list (or vector) of length 256
    return max(0, x[151])
def l538_120(x):
    # x is a list (or vector) of length 256
    return max(0, x[152])
def l538_121(x):
    # x is a list (or vector) of length 256
    return max(0, x[153])
def l538_122(x):
    # x is a list (or vector) of length 256
    return max(0, x[154])
def l538_123(x):
    # x is a list (or vector) of length 256
    return max(0, x[155])
def l538_124(x):
    # x is a list (or vector) of length 256
    return max(0, x[156])
def l538_125(x):
    # x is a list (or vector) of length 256
    return max(0, x[157])
def l538_126(x):
    # x is a list (or vector) of length 256
    return max(0, x[158])
def l538_127(x):
    # x is a list (or vector) of length 256
    return max(0, x[159])
def l538_128(x):
    # x is a list (or vector) of length 256
    return max(0, x[32] + -2.0*x[64] + x[96] + -1.0)
def l538_129(x):
    # x is a list (or vector) of length 256
    return max(0, x[33] + -2.0*x[65] + x[97] + -1.0)
def l538_130(x):
    # x is a list (or vector) of length 256
    return max(0, x[34] + -2.0*x[66] + x[98] + -1.0)
def l538_131(x):
    # x is a list (or vector) of length 256
    return max(0, x[35] + -2.0*x[67] + x[99] + -1.0)
def l538_132(x):
    # x is a list (or vector) of length 256
    return max(0, x[36] + -2.0*x[68] + x[100] + -1.0)
def l538_133(x):
    # x is a list (or vector) of length 256
    return max(0, x[37] + -2.0*x[69] + x[101] + -1.0)
def l538_134(x):
    # x is a list (or vector) of length 256
    return max(0, x[38] + -2.0*x[70] + x[102] + -1.0)
def l538_135(x):
    # x is a list (or vector) of length 256
    return max(0, x[39] + -2.0*x[71] + x[103] + -1.0)
def l538_136(x):
    # x is a list (or vector) of length 256
    return max(0, x[40] + -2.0*x[72] + x[104] + -1.0)
def l538_137(x):
    # x is a list (or vector) of length 256
    return max(0, x[41] + -2.0*x[73] + x[105] + -1.0)
def l538_138(x):
    # x is a list (or vector) of length 256
    return max(0, x[42] + -2.0*x[74] + x[106] + -1.0)
def l538_139(x):
    # x is a list (or vector) of length 256
    return max(0, x[43] + -2.0*x[75] + x[107] + -1.0)
def l538_140(x):
    # x is a list (or vector) of length 256
    return max(0, x[44] + -2.0*x[76] + x[108] + -1.0)
def l538_141(x):
    # x is a list (or vector) of length 256
    return max(0, x[45] + -2.0*x[77] + x[109] + -1.0)
def l538_142(x):
    # x is a list (or vector) of length 256
    return max(0, x[46] + -2.0*x[78] + x[110] + -1.0)
def l538_143(x):
    # x is a list (or vector) of length 256
    return max(0, x[47] + -2.0*x[79] + x[111] + -1.0)
def l538_144(x):
    # x is a list (or vector) of length 256
    return max(0, x[48] + -2.0*x[80] + x[112] + -1.0)
def l538_145(x):
    # x is a list (or vector) of length 256
    return max(0, x[49] + -2.0*x[81] + x[113] + -1.0)
def l538_146(x):
    # x is a list (or vector) of length 256
    return max(0, x[50] + -2.0*x[82] + x[114] + -1.0)
def l538_147(x):
    # x is a list (or vector) of length 256
    return max(0, x[51] + -2.0*x[83] + x[115] + -1.0)
def l538_148(x):
    # x is a list (or vector) of length 256
    return max(0, x[52] + -2.0*x[84] + x[116] + -1.0)
def l538_149(x):
    # x is a list (or vector) of length 256
    return max(0, x[53] + -2.0*x[85] + x[117] + -1.0)
def l538_150(x):
    # x is a list (or vector) of length 256
    return max(0, x[54] + -2.0*x[86] + x[118] + -1.0)
def l538_151(x):
    # x is a list (or vector) of length 256
    return max(0, x[55] + -2.0*x[87] + x[119] + -1.0)
def l538_152(x):
    # x is a list (or vector) of length 256
    return max(0, x[56] + -2.0*x[88] + x[120] + -1.0)
def l538_153(x):
    # x is a list (or vector) of length 256
    return max(0, x[57] + -2.0*x[89] + x[121] + -1.0)
def l538_154(x):
    # x is a list (or vector) of length 256
    return max(0, x[58] + -2.0*x[90] + x[122] + -1.0)
def l538_155(x):
    # x is a list (or vector) of length 256
    return max(0, x[59] + -2.0*x[91] + x[123] + -1.0)
def l538_156(x):
    # x is a list (or vector) of length 256
    return max(0, x[60] + -2.0*x[92] + x[124] + -1.0)
def l538_157(x):
    # x is a list (or vector) of length 256
    return max(0, x[61] + -2.0*x[93] + x[125] + -1.0)
def l538_158(x):
    # x is a list (or vector) of length 256
    return max(0, x[62] + -2.0*x[94] + x[126] + -1.0)
def l538_159(x):
    # x is a list (or vector) of length 256
    return max(0, x[63] + -2.0*x[95] + x[127] + -1.0)
def l538_160(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[32] + 2.0*x[64] + x[128])
def l538_161(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[33] + 2.0*x[65] + x[129])
def l538_162(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[34] + 2.0*x[66] + x[130])
def l538_163(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[35] + 2.0*x[67] + x[131])
def l538_164(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[36] + 2.0*x[68] + x[132])
def l538_165(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[37] + 2.0*x[69] + x[133])
def l538_166(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[38] + 2.0*x[70] + x[134])
def l538_167(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[39] + 2.0*x[71] + x[135])
def l538_168(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[40] + 2.0*x[72] + x[136])
def l538_169(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[41] + 2.0*x[73] + x[137])
def l538_170(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[42] + 2.0*x[74] + x[138])
def l538_171(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[43] + 2.0*x[75] + x[139])
def l538_172(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[44] + 2.0*x[76] + x[140])
def l538_173(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[45] + 2.0*x[77] + x[141])
def l538_174(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[46] + 2.0*x[78] + x[142])
def l538_175(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[47] + 2.0*x[79] + x[143])
def l538_176(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[48] + 2.0*x[80] + x[144])
def l538_177(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[49] + 2.0*x[81] + x[145])
def l538_178(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[50] + 2.0*x[82] + x[146])
def l538_179(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[51] + 2.0*x[83] + x[147])
def l538_180(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[52] + 2.0*x[84] + x[148])
def l538_181(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[53] + 2.0*x[85] + x[149])
def l538_182(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[54] + 2.0*x[86] + x[150])
def l538_183(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[55] + 2.0*x[87] + x[151])
def l538_184(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[56] + 2.0*x[88] + x[152])
def l538_185(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[57] + 2.0*x[89] + x[153])
def l538_186(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[58] + 2.0*x[90] + x[154])
def l538_187(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[59] + 2.0*x[91] + x[155])
def l538_188(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[60] + 2.0*x[92] + x[156])
def l538_189(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[61] + 2.0*x[93] + x[157])
def l538_190(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[62] + 2.0*x[94] + x[158])
def l538_191(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[63] + 2.0*x[95] + x[159])
def l538_192(x):
    # x is a list (or vector) of length 256
    return max(0, x[160])
def l538_193(x):
    # x is a list (or vector) of length 256
    return max(0, x[161])
def l538_194(x):
    # x is a list (or vector) of length 256
    return max(0, x[162])
def l538_195(x):
    # x is a list (or vector) of length 256
    return max(0, x[163])
def l538_196(x):
    # x is a list (or vector) of length 256
    return max(0, x[164])
def l538_197(x):
    # x is a list (or vector) of length 256
    return max(0, x[165])
def l538_198(x):
    # x is a list (or vector) of length 256
    return max(0, x[166])
def l538_199(x):
    # x is a list (or vector) of length 256
    return max(0, x[167])
def l538_200(x):
    # x is a list (or vector) of length 256
    return max(0, x[168])
def l538_201(x):
    # x is a list (or vector) of length 256
    return max(0, x[169])
def l538_202(x):
    # x is a list (or vector) of length 256
    return max(0, x[170])
def l538_203(x):
    # x is a list (or vector) of length 256
    return max(0, x[171])
def l538_204(x):
    # x is a list (or vector) of length 256
    return max(0, x[172])
def l538_205(x):
    # x is a list (or vector) of length 256
    return max(0, x[173])
def l538_206(x):
    # x is a list (or vector) of length 256
    return max(0, x[174])
def l538_207(x):
    # x is a list (or vector) of length 256
    return max(0, x[175])
def l538_208(x):
    # x is a list (or vector) of length 256
    return max(0, x[176])
def l538_209(x):
    # x is a list (or vector) of length 256
    return max(0, x[177])
def l538_210(x):
    # x is a list (or vector) of length 256
    return max(0, x[178])
def l538_211(x):
    # x is a list (or vector) of length 256
    return max(0, x[179])
def l538_212(x):
    # x is a list (or vector) of length 256
    return max(0, x[180])
def l538_213(x):
    # x is a list (or vector) of length 256
    return max(0, x[181])
def l538_214(x):
    # x is a list (or vector) of length 256
    return max(0, x[182])
def l538_215(x):
    # x is a list (or vector) of length 256
    return max(0, x[183])
def l538_216(x):
    # x is a list (or vector) of length 256
    return max(0, x[184])
def l538_217(x):
    # x is a list (or vector) of length 256
    return max(0, x[185])
def l538_218(x):
    # x is a list (or vector) of length 256
    return max(0, x[186])
def l538_219(x):
    # x is a list (or vector) of length 256
    return max(0, x[187])
def l538_220(x):
    # x is a list (or vector) of length 256
    return max(0, x[188])
def l538_221(x):
    # x is a list (or vector) of length 256
    return max(0, x[189])
def l538_222(x):
    # x is a list (or vector) of length 256
    return max(0, x[190])
def l538_223(x):
    # x is a list (or vector) of length 256
    return max(0, x[191])
def l538_224(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l538_225(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l538_226(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_227(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_228(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l538_229(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_230(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_231(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_232(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_233(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l538_234(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l538_235(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_236(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_237(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_238(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l538_239(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_240(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_241(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_242(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_243(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_244(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l538_245(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l538_246(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_247(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_248(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_249(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_250(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_251(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l538_252(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_253(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l538_254(x):
    # x is a list (or vector) of length 256
    return max(0, 0)
def l538_255(x):
    # x is a list (or vector) of length 256
    return max(0, 1.0)
def l538_256(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[220] + 128.0)
def l538_257(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[221] + 128.0)
def l538_258(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[222] + 128.0)
def l538_259(x):
    # x is a list (or vector) of length 256
    return max(0, -1.0*x[223] + 128.0)
def l538_260(x):
    # x is a list (or vector) of length 256
    return max(0, x[220])
def l538_261(x):
    # x is a list (or vector) of length 256
    return max(0, x[221])
def l538_262(x):
    # x is a list (or vector) of length 256
    return max(0, x[222])
def l538_263(x):
    # x is a list (or vector) of length 256
    return max(0, x[223])
def l538_264(x):
    # x is a list (or vector) of length 256
    return max(0, x[220] + -127.0)
def l538_265(x):
    # x is a list (or vector) of length 256
    return max(0, x[221] + -127.0)
def l538_266(x):
    # x is a list (or vector) of length 256
    return max(0, x[222] + -127.0)
def l538_267(x):
    # x is a list (or vector) of length 256
    return max(0, x[223] + -127.0)
def l538_268(x):
    # x is a list (or vector) of length 256
    return max(0, x[220] + -128.0)
def l538_269(x):
    # x is a list (or vector) of length 256
    return max(0, x[221] + -128.0)
def l538_270(x):
    # x is a list (or vector) of length 256
    return max(0, x[222] + -128.0)
def l538_271(x):
    # x is a list (or vector) of length 256
    return max(0, x[223] + -128.0)
def l538_272(x):
    # x is a list (or vector) of length 256
    return max(0, x[192])
def l538_273(x):
    # x is a list (or vector) of length 256
    return max(0, x[193])
def l538_274(x):
    # x is a list (or vector) of length 256
    return max(0, x[194])
def l538_275(x):
    # x is a list (or vector) of length 256
    return max(0, x[195])
def l538_276(x):
    # x is a list (or vector) of length 256
    return max(0, x[196])
def l538_277(x):
    # x is a list (or vector) of length 256
    return max(0, x[197])
def l538_278(x):
    # x is a list (or vector) of length 256
    return max(0, x[198])
def l538_279(x):
    # x is a list (or vector) of length 256
    return max(0, x[199])
def l538_280(x):
    # x is a list (or vector) of length 256
    return max(0, x[200])
def l538_281(x):
    # x is a list (or vector) of length 256
    return max(0, x[201])
def l538_282(x):
    # x is a list (or vector) of length 256
    return max(0, x[202])
def l538_283(x):
    # x is a list (or vector) of length 256
    return max(0, x[203])
def l538_284(x):
    # x is a list (or vector) of length 256
    return max(0, x[204])
def l538_285(x):
    # x is a list (or vector) of length 256
    return max(0, x[205])
def l538_286(x):
    # x is a list (or vector) of length 256
    return max(0, x[206])
def l538_287(x):
    # x is a list (or vector) of length 256
    return max(0, x[207])
def l538_288(x):
    # x is a list (or vector) of length 256
    return max(0, x[208])
def l538_289(x):
    # x is a list (or vector) of length 256
    return max(0, x[209])
def l538_290(x):
    # x is a list (or vector) of length 256
    return max(0, x[210])
def l538_291(x):
    # x is a list (or vector) of length 256
    return max(0, x[211])
def l538_292(x):
    # x is a list (or vector) of length 256
    return max(0, x[212])
def l538_293(x):
    # x is a list (or vector) of length 256
    return max(0, x[213])
def l538_294(x):
    # x is a list (or vector) of length 256
    return max(0, x[214])
def l538_295(x):
    # x is a list (or vector) of length 256
    return max(0, x[215])
def l538_296(x):
    # x is a list (or vector) of length 256
    return max(0, x[216])
def l538_297(x):
    # x is a list (or vector) of length 256
    return max(0, x[217])
def l538_298(x):
    # x is a list (or vector) of length 256
    return max(0, x[218])
def l538_299(x):
    # x is a list (or vector) of length 256
    return max(0, x[219])
def l538_300(x):
    # x is a list (or vector) of length 256
    return max(0, x[220])
def l538_301(x):
    # x is a list (or vector) of length 256
    return max(0, x[221])
def l538_302(x):
    # x is a list (or vector) of length 256
    return max(0, x[222])
def l538_303(x):
    # x is a list (or vector) of length 256
    return max(0, x[223])
def l538_304(x):
    # x is a list (or vector) of length 256
    return max(0, x[224])
def l538_305(x):
    # x is a list (or vector) of length 256
    return max(0, x[225])
def l538_306(x):
    # x is a list (or vector) of length 256
    return max(0, x[226])
def l538_307(x):
    # x is a list (or vector) of length 256
    return max(0, x[227])
def l538_308(x):
    # x is a list (or vector) of length 256
    return max(0, x[228])
def l538_309(x):
    # x is a list (or vector) of length 256
    return max(0, x[229])
def l538_310(x):
    # x is a list (or vector) of length 256
    return max(0, x[230])
def l538_311(x):
    # x is a list (or vector) of length 256
    return max(0, x[231])
def l538_312(x):
    # x is a list (or vector) of length 256
    return max(0, x[232])
def l538_313(x):
    # x is a list (or vector) of length 256
    return max(0, x[233])
def l538_314(x):
    # x is a list (or vector) of length 256
    return max(0, x[234])
def l538_315(x):
    # x is a list (or vector) of length 256
    return max(0, x[235])
def l538_316(x):
    # x is a list (or vector) of length 256
    return max(0, x[236])
def l538_317(x):
    # x is a list (or vector) of length 256
    return max(0, x[237])
def l538_318(x):
    # x is a list (or vector) of length 256
    return max(0, x[238])
def l538_319(x):
    # x is a list (or vector) of length 256
    return max(0, x[239])
def l538_320(x):
    # x is a list (or vector) of length 256
    return max(0, x[240])
def l538_321(x):
    # x is a list (or vector) of length 256
    return max(0, x[241])
def l538_322(x):
    # x is a list (or vector) of length 256
    return max(0, x[242])
def l538_323(x):
    # x is a list (or vector) of length 256
    return max(0, x[243])
def l538_324(x):
    # x is a list (or vector) of length 256
    return max(0, x[244])
def l538_325(x):
    # x is a list (or vector) of length 256
    return max(0, x[245])
def l538_326(x):
    # x is a list (or vector) of length 256
    return max(0, x[246])
def l538_327(x):
    # x is a list (or vector) of length 256
    return max(0, x[247])
def l538_328(x):
    # x is a list (or vector) of length 256
    return max(0, x[248])
def l538_329(x):
    # x is a list (or vector) of length 256
    return max(0, x[249])
def l538_330(x):
    # x is a list (or vector) of length 256
    return max(0, x[250])
def l538_331(x):
    # x is a list (or vector) of length 256
    return max(0, x[251])
def l538_332(x):
    # x is a list (or vector) of length 256
    return max(0, x[252])
def l538_333(x):
    # x is a list (or vector) of length 256
    return max(0, x[253])
def l538_334(x):
    # x is a list (or vector) of length 256
    return max(0, x[254])
def l538_335(x):
    # x is a list (or vector) of length 256
    return max(0, x[255])
def l538_(x):
    # x is a list (or vector) of length 256
    return [
        l538_0(x),
        l538_1(x),
        l538_2(x),
        l538_3(x),
        l538_4(x),
        l538_5(x),
        l538_6(x),
        l538_7(x),
        l538_8(x),
        l538_9(x),
        l538_10(x),
        l538_11(x),
        l538_12(x),
        l538_13(x),
        l538_14(x),
        l538_15(x),
        l538_16(x),
        l538_17(x),
        l538_18(x),
        l538_19(x),
        l538_20(x),
        l538_21(x),
        l538_22(x),
        l538_23(x),
        l538_24(x),
        l538_25(x),
        l538_26(x),
        l538_27(x),
        l538_28(x),
        l538_29(x),
        l538_30(x),
        l538_31(x),
        l538_32(x),
        l538_33(x),
        l538_34(x),
        l538_35(x),
        l538_36(x),
        l538_37(x),
        l538_38(x),
        l538_39(x),
        l538_40(x),
        l538_41(x),
        l538_42(x),
        l538_43(x),
        l538_44(x),
        l538_45(x),
        l538_46(x),
        l538_47(x),
        l538_48(x),
        l538_49(x),
        l538_50(x),
        l538_51(x),
        l538_52(x),
        l538_53(x),
        l538_54(x),
        l538_55(x),
        l538_56(x),
        l538_57(x),
        l538_58(x),
        l538_59(x),
        l538_60(x),
        l538_61(x),
        l538_62(x),
        l538_63(x),
        l538_64(x),
        l538_65(x),
        l538_66(x),
        l538_67(x),
        l538_68(x),
        l538_69(x),
        l538_70(x),
        l538_71(x),
        l538_72(x),
        l538_73(x),
        l538_74(x),
        l538_75(x),
        l538_76(x),
        l538_77(x),
        l538_78(x),
        l538_79(x),
        l538_80(x),
        l538_81(x),
        l538_82(x),
        l538_83(x),
        l538_84(x),
        l538_85(x),
        l538_86(x),
        l538_87(x),
        l538_88(x),
        l538_89(x),
        l538_90(x),
        l538_91(x),
        l538_92(x),
        l538_93(x),
        l538_94(x),
        l538_95(x),
        l538_96(x),
        l538_97(x),
        l538_98(x),
        l538_99(x),
        l538_100(x),
        l538_101(x),
        l538_102(x),
        l538_103(x),
        l538_104(x),
        l538_105(x),
        l538_106(x),
        l538_107(x),
        l538_108(x),
        l538_109(x),
        l538_110(x),
        l538_111(x),
        l538_112(x),
        l538_113(x),
        l538_114(x),
        l538_115(x),
        l538_116(x),
        l538_117(x),
        l538_118(x),
        l538_119(x),
        l538_120(x),
        l538_121(x),
        l538_122(x),
        l538_123(x),
        l538_124(x),
        l538_125(x),
        l538_126(x),
        l538_127(x),
        l538_128(x),
        l538_129(x),
        l538_130(x),
        l538_131(x),
        l538_132(x),
        l538_133(x),
        l538_134(x),
        l538_135(x),
        l538_136(x),
        l538_137(x),
        l538_138(x),
        l538_139(x),
        l538_140(x),
        l538_141(x),
        l538_142(x),
        l538_143(x),
        l538_144(x),
        l538_145(x),
        l538_146(x),
        l538_147(x),
        l538_148(x),
        l538_149(x),
        l538_150(x),
        l538_151(x),
        l538_152(x),
        l538_153(x),
        l538_154(x),
        l538_155(x),
        l538_156(x),
        l538_157(x),
        l538_158(x),
        l538_159(x),
        l538_160(x),
        l538_161(x),
        l538_162(x),
        l538_163(x),
        l538_164(x),
        l538_165(x),
        l538_166(x),
        l538_167(x),
        l538_168(x),
        l538_169(x),
        l538_170(x),
        l538_171(x),
        l538_172(x),
        l538_173(x),
        l538_174(x),
        l538_175(x),
        l538_176(x),
        l538_177(x),
        l538_178(x),
        l538_179(x),
        l538_180(x),
        l538_181(x),
        l538_182(x),
        l538_183(x),
        l538_184(x),
        l538_185(x),
        l538_186(x),
        l538_187(x),
        l538_188(x),
        l538_189(x),
        l538_190(x),
        l538_191(x),
        l538_192(x),
        l538_193(x),
        l538_194(x),
        l538_195(x),
        l538_196(x),
        l538_197(x),
        l538_198(x),
        l538_199(x),
        l538_200(x),
        l538_201(x),
        l538_202(x),
        l538_203(x),
        l538_204(x),
        l538_205(x),
        l538_206(x),
        l538_207(x),
        l538_208(x),
        l538_209(x),
        l538_210(x),
        l538_211(x),
        l538_212(x),
        l538_213(x),
        l538_214(x),
        l538_215(x),
        l538_216(x),
        l538_217(x),
        l538_218(x),
        l538_219(x),
        l538_220(x),
        l538_221(x),
        l538_222(x),
        l538_223(x),
        l538_224(x),
        l538_225(x),
        l538_226(x),
        l538_227(x),
        l538_228(x),
        l538_229(x),
        l538_230(x),
        l538_231(x),
        l538_232(x),
        l538_233(x),
        l538_234(x),
        l538_235(x),
        l538_236(x),
        l538_237(x),
        l538_238(x),
        l538_239(x),
        l538_240(x),
        l538_241(x),
        l538_242(x),
        l538_243(x),
        l538_244(x),
        l538_245(x),
        l538_246(x),
        l538_247(x),
        l538_248(x),
        l538_249(x),
        l538_250(x),
        l538_251(x),
        l538_252(x),
        l538_253(x),
        l538_254(x),
        l538_255(x),
        l538_256(x),
        l538_257(x),
        l538_258(x),
        l538_259(x),
        l538_260(x),
        l538_261(x),
        l538_262(x),
        l538_263(x),
        l538_264(x),
        l538_265(x),
        l538_266(x),
        l538_267(x),
        l538_268(x),
        l538_269(x),
        l538_270(x),
        l538_271(x),
        l538_272(x),
        l538_273(x),
        l538_274(x),
        l538_275(x),
        l538_276(x),
        l538_277(x),
        l538_278(x),
        l538_279(x),
        l538_280(x),
        l538_281(x),
        l538_282(x),
        l538_283(x),
        l538_284(x),
        l538_285(x),
        l538_286(x),
        l538_287(x),
        l538_288(x),
        l538_289(x),
        l538_290(x),
        l538_291(x),
        l538_292(x),
        l538_293(x),
        l538_294(x),
        l538_295(x),
        l538_296(x),
        l538_297(x),
        l538_298(x),
        l538_299(x),
        l538_300(x),
        l538_301(x),
        l538_302(x),
        l538_303(x),
        l538_304(x),
        l538_305(x),
        l538_306(x),
        l538_307(x),
        l538_308(x),
        l538_309(x),
        l538_310(x),
        l538_311(x),
        l538_312(x),
        l538_313(x),
        l538_314(x),
        l538_315(x),
        l538_316(x),
        l538_317(x),
        l538_318(x),
        l538_319(x),
        l538_320(x),
        l538_321(x),
        l538_322(x),
        l538_323(x),
        l538_324(x),
        l538_325(x),
        l538_326(x),
        l538_327(x),
        l538_328(x),
        l538_329(x),
        l538_330(x),
        l538_331(x),
        l538_332(x),
        l538_333(x),
        l538_334(x),
        l538_335(x),
    ]