import numpy as np




# Generated from reverse engineering
def l92_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 288
    out = np.empty(288, dtype=np.float32)
    
    # for i in range(0, 32):
    for i in range(0, 32):
        s = x[64 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(32, 39):
    for i in range(0, 7):
        s = x[0 + i] + x[121 + i] + -2.0 * x[i + 153]
        s += biases[i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(39, 64):
    for i in range(0, 25):
        s = x[7 + i] + x[96 + i] + -2.0 * x[i + 128]
        s += biases[i]
        out[39 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 71):
    for i in range(0, 7):
        s = x[0 + i] + x[121 + i] + -2.0 * x[i + 153]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(71, 96):
    for i in range(0, 25):
        s = x[7 + i] + x[96 + i] + -2.0 * x[i + 128]
        out[71 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(96, 103):
    for i in range(0, 7):
        s = x[0 + i] + x[121 + i] + -2.0 * x[i + 153]
        s += biases[i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(103, 128):
    for i in range(0, 25):
        s = x[7 + i] + x[96 + i] + -2.0 * x[i + 128]
        s += biases[i]
        out[103 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 192):
    for i in range(0, 64):
        s = x[0 + i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(192, 288):
    for i in range(0, 96):
        s = x[160 + i]
        out[192 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l92_0(x):
    # x is a list (or vector) of length 256
    return max(0, x[64])
def l92_1(x):
    # x is a list (or vector) of length 256
    return max(0, x[65])
def l92_2(x):
    # x is a list (or vector) of length 256
    return max(0, x[66])
def l92_3(x):
    # x is a list (or vector) of length 256
    return max(0, x[67])
def l92_4(x):
    # x is a list (or vector) of length 256
    return max(0, x[68])
def l92_5(x):
    # x is a list (or vector) of length 256
    return max(0, x[69])
def l92_6(x):
    # x is a list (or vector) of length 256
    return max(0, x[70])
def l92_7(x):
    # x is a list (or vector) of length 256
    return max(0, x[71])
def l92_8(x):
    # x is a list (or vector) of length 256
    return max(0, x[72])
def l92_9(x):
    # x is a list (or vector) of length 256
    return max(0, x[73])
def l92_10(x):
    # x is a list (or vector) of length 256
    return max(0, x[74])
def l92_11(x):
    # x is a list (or vector) of length 256
    return max(0, x[75])
def l92_12(x):
    # x is a list (or vector) of length 256
    return max(0, x[76])
def l92_13(x):
    # x is a list (or vector) of length 256
    return max(0, x[77])
def l92_14(x):
    # x is a list (or vector) of length 256
    return max(0, x[78])
def l92_15(x):
    # x is a list (or vector) of length 256
    return max(0, x[79])
def l92_16(x):
    # x is a list (or vector) of length 256
    return max(0, x[80])
def l92_17(x):
    # x is a list (or vector) of length 256
    return max(0, x[81])
def l92_18(x):
    # x is a list (or vector) of length 256
    return max(0, x[82])
def l92_19(x):
    # x is a list (or vector) of length 256
    return max(0, x[83])
def l92_20(x):
    # x is a list (or vector) of length 256
    return max(0, x[84])
def l92_21(x):
    # x is a list (or vector) of length 256
    return max(0, x[85])
def l92_22(x):
    # x is a list (or vector) of length 256
    return max(0, x[86])
def l92_23(x):
    # x is a list (or vector) of length 256
    return max(0, x[87])
def l92_24(x):
    # x is a list (or vector) of length 256
    return max(0, x[88])
def l92_25(x):
    # x is a list (or vector) of length 256
    return max(0, x[89])
def l92_26(x):
    # x is a list (or vector) of length 256
    return max(0, x[90])
def l92_27(x):
    # x is a list (or vector) of length 256
    return max(0, x[91])
def l92_28(x):
    # x is a list (or vector) of length 256
    return max(0, x[92])
def l92_29(x):
    # x is a list (or vector) of length 256
    return max(0, x[93])
def l92_30(x):
    # x is a list (or vector) of length 256
    return max(0, x[94])
def l92_31(x):
    # x is a list (or vector) of length 256
    return max(0, x[95])
def l92_32(x):
    # x is a list (or vector) of length 256
    return max(0, x[0] + x[121] + -2.0*x[153] + -1.0)
def l92_33(x):
    # x is a list (or vector) of length 256
    return max(0, x[1] + x[122] + -2.0*x[154] + -1.0)
def l92_34(x):
    # x is a list (or vector) of length 256
    return max(0, x[2] + x[123] + -2.0*x[155] + -1.0)
def l92_35(x):
    # x is a list (or vector) of length 256
    return max(0, x[3] + x[124] + -2.0*x[156] + -1.0)
def l92_36(x):
    # x is a list (or vector) of length 256
    return max(0, x[4] + x[125] + -2.0*x[157] + -1.0)
def l92_37(x):
    # x is a list (or vector) of length 256
    return max(0, x[5] + x[126] + -2.0*x[158] + -1.0)
def l92_38(x):
    # x is a list (or vector) of length 256
    return max(0, x[6] + x[127] + -2.0*x[159] + -1.0)
def l92_39(x):
    # x is a list (or vector) of length 256
    return max(0, x[7] + x[96] + -2.0*x[128] + -1.0)
def l92_40(x):
    # x is a list (or vector) of length 256
    return max(0, x[8] + x[97] + -2.0*x[129] + -1.0)
def l92_41(x):
    # x is a list (or vector) of length 256
    return max(0, x[9] + x[98] + -2.0*x[130] + -1.0)
def l92_42(x):
    # x is a list (or vector) of length 256
    return max(0, x[10] + x[99] + -2.0*x[131] + -1.0)
def l92_43(x):
    # x is a list (or vector) of length 256
    return max(0, x[11] + x[100] + -2.0*x[132] + -1.0)
def l92_44(x):
    # x is a list (or vector) of length 256
    return max(0, x[12] + x[101] + -2.0*x[133] + -1.0)
def l92_45(x):
    # x is a list (or vector) of length 256
    return max(0, x[13] + x[102] + -2.0*x[134] + -1.0)
def l92_46(x):
    # x is a list (or vector) of length 256
    return max(0, x[14] + x[103] + -2.0*x[135] + -1.0)
def l92_47(x):
    # x is a list (or vector) of length 256
    return max(0, x[15] + x[104] + -2.0*x[136] + -1.0)
def l92_48(x):
    # x is a list (or vector) of length 256
    return max(0, x[16] + x[105] + -2.0*x[137] + -1.0)
def l92_49(x):
    # x is a list (or vector) of length 256
    return max(0, x[17] + x[106] + -2.0*x[138] + -1.0)
def l92_50(x):
    # x is a list (or vector) of length 256
    return max(0, x[18] + x[107] + -2.0*x[139] + -1.0)
def l92_51(x):
    # x is a list (or vector) of length 256
    return max(0, x[19] + x[108] + -2.0*x[140] + -1.0)
def l92_52(x):
    # x is a list (or vector) of length 256
    return max(0, x[20] + x[109] + -2.0*x[141] + -1.0)
def l92_53(x):
    # x is a list (or vector) of length 256
    return max(0, x[21] + x[110] + -2.0*x[142] + -1.0)
def l92_54(x):
    # x is a list (or vector) of length 256
    return max(0, x[22] + x[111] + -2.0*x[143] + -1.0)
def l92_55(x):
    # x is a list (or vector) of length 256
    return max(0, x[23] + x[112] + -2.0*x[144] + -1.0)
def l92_56(x):
    # x is a list (or vector) of length 256
    return max(0, x[24] + x[113] + -2.0*x[145] + -1.0)
def l92_57(x):
    # x is a list (or vector) of length 256
    return max(0, x[25] + x[114] + -2.0*x[146] + -1.0)
def l92_58(x):
    # x is a list (or vector) of length 256
    return max(0, x[26] + x[115] + -2.0*x[147] + -1.0)
def l92_59(x):
    # x is a list (or vector) of length 256
    return max(0, x[27] + x[116] + -2.0*x[148] + -1.0)
def l92_60(x):
    # x is a list (or vector) of length 256
    return max(0, x[28] + x[117] + -2.0*x[149] + -1.0)
def l92_61(x):
    # x is a list (or vector) of length 256
    return max(0, x[29] + x[118] + -2.0*x[150] + -1.0)
def l92_62(x):
    # x is a list (or vector) of length 256
    return max(0, x[30] + x[119] + -2.0*x[151] + -1.0)
def l92_63(x):
    # x is a list (or vector) of length 256
    return max(0, x[31] + x[120] + -2.0*x[152] + -1.0)
def l92_64(x):
    # x is a list (or vector) of length 256
    return max(0, x[0] + x[121] + -2.0*x[153])
def l92_65(x):
    # x is a list (or vector) of length 256
    return max(0, x[1] + x[122] + -2.0*x[154])
def l92_66(x):
    # x is a list (or vector) of length 256
    return max(0, x[2] + x[123] + -2.0*x[155])
def l92_67(x):
    # x is a list (or vector) of length 256
    return max(0, x[3] + x[124] + -2.0*x[156])
def l92_68(x):
    # x is a list (or vector) of length 256
    return max(0, x[4] + x[125] + -2.0*x[157])
def l92_69(x):
    # x is a list (or vector) of length 256
    return max(0, x[5] + x[126] + -2.0*x[158])
def l92_70(x):
    # x is a list (or vector) of length 256
    return max(0, x[6] + x[127] + -2.0*x[159])
def l92_71(x):
    # x is a list (or vector) of length 256
    return max(0, x[7] + x[96] + -2.0*x[128])
def l92_72(x):
    # x is a list (or vector) of length 256
    return max(0, x[8] + x[97] + -2.0*x[129])
def l92_73(x):
    # x is a list (or vector) of length 256
    return max(0, x[9] + x[98] + -2.0*x[130])
def l92_74(x):
    # x is a list (or vector) of length 256
    return max(0, x[10] + x[99] + -2.0*x[131])
def l92_75(x):
    # x is a list (or vector) of length 256
    return max(0, x[11] + x[100] + -2.0*x[132])
def l92_76(x):
    # x is a list (or vector) of length 256
    return max(0, x[12] + x[101] + -2.0*x[133])
def l92_77(x):
    # x is a list (or vector) of length 256
    return max(0, x[13] + x[102] + -2.0*x[134])
def l92_78(x):
    # x is a list (or vector) of length 256
    return max(0, x[14] + x[103] + -2.0*x[135])
def l92_79(x):
    # x is a list (or vector) of length 256
    return max(0, x[15] + x[104] + -2.0*x[136])
def l92_80(x):
    # x is a list (or vector) of length 256
    return max(0, x[16] + x[105] + -2.0*x[137])
def l92_81(x):
    # x is a list (or vector) of length 256
    return max(0, x[17] + x[106] + -2.0*x[138])
def l92_82(x):
    # x is a list (or vector) of length 256
    return max(0, x[18] + x[107] + -2.0*x[139])
def l92_83(x):
    # x is a list (or vector) of length 256
    return max(0, x[19] + x[108] + -2.0*x[140])
def l92_84(x):
    # x is a list (or vector) of length 256
    return max(0, x[20] + x[109] + -2.0*x[141])
def l92_85(x):
    # x is a list (or vector) of length 256
    return max(0, x[21] + x[110] + -2.0*x[142])
def l92_86(x):
    # x is a list (or vector) of length 256
    return max(0, x[22] + x[111] + -2.0*x[143])
def l92_87(x):
    # x is a list (or vector) of length 256
    return max(0, x[23] + x[112] + -2.0*x[144])
def l92_88(x):
    # x is a list (or vector) of length 256
    return max(0, x[24] + x[113] + -2.0*x[145])
def l92_89(x):
    # x is a list (or vector) of length 256
    return max(0, x[25] + x[114] + -2.0*x[146])
def l92_90(x):
    # x is a list (or vector) of length 256
    return max(0, x[26] + x[115] + -2.0*x[147])
def l92_91(x):
    # x is a list (or vector) of length 256
    return max(0, x[27] + x[116] + -2.0*x[148])
def l92_92(x):
    # x is a list (or vector) of length 256
    return max(0, x[28] + x[117] + -2.0*x[149])
def l92_93(x):
    # x is a list (or vector) of length 256
    return max(0, x[29] + x[118] + -2.0*x[150])
def l92_94(x):
    # x is a list (or vector) of length 256
    return max(0, x[30] + x[119] + -2.0*x[151])
def l92_95(x):
    # x is a list (or vector) of length 256
    return max(0, x[31] + x[120] + -2.0*x[152])
def l92_96(x):
    # x is a list (or vector) of length 256
    return max(0, x[0] + x[121] + -2.0*x[153] + -1.0)
def l92_97(x):
    # x is a list (or vector) of length 256
    return max(0, x[1] + x[122] + -2.0*x[154] + -1.0)
def l92_98(x):
    # x is a list (or vector) of length 256
    return max(0, x[2] + x[123] + -2.0*x[155] + -1.0)
def l92_99(x):
    # x is a list (or vector) of length 256
    return max(0, x[3] + x[124] + -2.0*x[156] + -1.0)
def l92_100(x):
    # x is a list (or vector) of length 256
    return max(0, x[4] + x[125] + -2.0*x[157] + -1.0)
def l92_101(x):
    # x is a list (or vector) of length 256
    return max(0, x[5] + x[126] + -2.0*x[158] + -1.0)
def l92_102(x):
    # x is a list (or vector) of length 256
    return max(0, x[6] + x[127] + -2.0*x[159] + -1.0)
def l92_103(x):
    # x is a list (or vector) of length 256
    return max(0, x[7] + x[96] + -2.0*x[128] + -1.0)
def l92_104(x):
    # x is a list (or vector) of length 256
    return max(0, x[8] + x[97] + -2.0*x[129] + -1.0)
def l92_105(x):
    # x is a list (or vector) of length 256
    return max(0, x[9] + x[98] + -2.0*x[130] + -1.0)
def l92_106(x):
    # x is a list (or vector) of length 256
    return max(0, x[10] + x[99] + -2.0*x[131] + -1.0)
def l92_107(x):
    # x is a list (or vector) of length 256
    return max(0, x[11] + x[100] + -2.0*x[132] + -1.0)
def l92_108(x):
    # x is a list (or vector) of length 256
    return max(0, x[12] + x[101] + -2.0*x[133] + -1.0)
def l92_109(x):
    # x is a list (or vector) of length 256
    return max(0, x[13] + x[102] + -2.0*x[134] + -1.0)
def l92_110(x):
    # x is a list (or vector) of length 256
    return max(0, x[14] + x[103] + -2.0*x[135] + -1.0)
def l92_111(x):
    # x is a list (or vector) of length 256
    return max(0, x[15] + x[104] + -2.0*x[136] + -1.0)
def l92_112(x):
    # x is a list (or vector) of length 256
    return max(0, x[16] + x[105] + -2.0*x[137] + -1.0)
def l92_113(x):
    # x is a list (or vector) of length 256
    return max(0, x[17] + x[106] + -2.0*x[138] + -1.0)
def l92_114(x):
    # x is a list (or vector) of length 256
    return max(0, x[18] + x[107] + -2.0*x[139] + -1.0)
def l92_115(x):
    # x is a list (or vector) of length 256
    return max(0, x[19] + x[108] + -2.0*x[140] + -1.0)
def l92_116(x):
    # x is a list (or vector) of length 256
    return max(0, x[20] + x[109] + -2.0*x[141] + -1.0)
def l92_117(x):
    # x is a list (or vector) of length 256
    return max(0, x[21] + x[110] + -2.0*x[142] + -1.0)
def l92_118(x):
    # x is a list (or vector) of length 256
    return max(0, x[22] + x[111] + -2.0*x[143] + -1.0)
def l92_119(x):
    # x is a list (or vector) of length 256
    return max(0, x[23] + x[112] + -2.0*x[144] + -1.0)
def l92_120(x):
    # x is a list (or vector) of length 256
    return max(0, x[24] + x[113] + -2.0*x[145] + -1.0)
def l92_121(x):
    # x is a list (or vector) of length 256
    return max(0, x[25] + x[114] + -2.0*x[146] + -1.0)
def l92_122(x):
    # x is a list (or vector) of length 256
    return max(0, x[26] + x[115] + -2.0*x[147] + -1.0)
def l92_123(x):
    # x is a list (or vector) of length 256
    return max(0, x[27] + x[116] + -2.0*x[148] + -1.0)
def l92_124(x):
    # x is a list (or vector) of length 256
    return max(0, x[28] + x[117] + -2.0*x[149] + -1.0)
def l92_125(x):
    # x is a list (or vector) of length 256
    return max(0, x[29] + x[118] + -2.0*x[150] + -1.0)
def l92_126(x):
    # x is a list (or vector) of length 256
    return max(0, x[30] + x[119] + -2.0*x[151] + -1.0)
def l92_127(x):
    # x is a list (or vector) of length 256
    return max(0, x[31] + x[120] + -2.0*x[152] + -1.0)
def l92_128(x):
    # x is a list (or vector) of length 256
    return max(0, x[0])
def l92_129(x):
    # x is a list (or vector) of length 256
    return max(0, x[1])
def l92_130(x):
    # x is a list (or vector) of length 256
    return max(0, x[2])
def l92_131(x):
    # x is a list (or vector) of length 256
    return max(0, x[3])
def l92_132(x):
    # x is a list (or vector) of length 256
    return max(0, x[4])
def l92_133(x):
    # x is a list (or vector) of length 256
    return max(0, x[5])
def l92_134(x):
    # x is a list (or vector) of length 256
    return max(0, x[6])
def l92_135(x):
    # x is a list (or vector) of length 256
    return max(0, x[7])
def l92_136(x):
    # x is a list (or vector) of length 256
    return max(0, x[8])
def l92_137(x):
    # x is a list (or vector) of length 256
    return max(0, x[9])
def l92_138(x):
    # x is a list (or vector) of length 256
    return max(0, x[10])
def l92_139(x):
    # x is a list (or vector) of length 256
    return max(0, x[11])
def l92_140(x):
    # x is a list (or vector) of length 256
    return max(0, x[12])
def l92_141(x):
    # x is a list (or vector) of length 256
    return max(0, x[13])
def l92_142(x):
    # x is a list (or vector) of length 256
    return max(0, x[14])
def l92_143(x):
    # x is a list (or vector) of length 256
    return max(0, x[15])
def l92_144(x):
    # x is a list (or vector) of length 256
    return max(0, x[16])
def l92_145(x):
    # x is a list (or vector) of length 256
    return max(0, x[17])
def l92_146(x):
    # x is a list (or vector) of length 256
    return max(0, x[18])
def l92_147(x):
    # x is a list (or vector) of length 256
    return max(0, x[19])
def l92_148(x):
    # x is a list (or vector) of length 256
    return max(0, x[20])
def l92_149(x):
    # x is a list (or vector) of length 256
    return max(0, x[21])
def l92_150(x):
    # x is a list (or vector) of length 256
    return max(0, x[22])
def l92_151(x):
    # x is a list (or vector) of length 256
    return max(0, x[23])
def l92_152(x):
    # x is a list (or vector) of length 256
    return max(0, x[24])
def l92_153(x):
    # x is a list (or vector) of length 256
    return max(0, x[25])
def l92_154(x):
    # x is a list (or vector) of length 256
    return max(0, x[26])
def l92_155(x):
    # x is a list (or vector) of length 256
    return max(0, x[27])
def l92_156(x):
    # x is a list (or vector) of length 256
    return max(0, x[28])
def l92_157(x):
    # x is a list (or vector) of length 256
    return max(0, x[29])
def l92_158(x):
    # x is a list (or vector) of length 256
    return max(0, x[30])
def l92_159(x):
    # x is a list (or vector) of length 256
    return max(0, x[31])
def l92_160(x):
    # x is a list (or vector) of length 256
    return max(0, x[32])
def l92_161(x):
    # x is a list (or vector) of length 256
    return max(0, x[33])
def l92_162(x):
    # x is a list (or vector) of length 256
    return max(0, x[34])
def l92_163(x):
    # x is a list (or vector) of length 256
    return max(0, x[35])
def l92_164(x):
    # x is a list (or vector) of length 256
    return max(0, x[36])
def l92_165(x):
    # x is a list (or vector) of length 256
    return max(0, x[37])
def l92_166(x):
    # x is a list (or vector) of length 256
    return max(0, x[38])
def l92_167(x):
    # x is a list (or vector) of length 256
    return max(0, x[39])
def l92_168(x):
    # x is a list (or vector) of length 256
    return max(0, x[40])
def l92_169(x):
    # x is a list (or vector) of length 256
    return max(0, x[41])
def l92_170(x):
    # x is a list (or vector) of length 256
    return max(0, x[42])
def l92_171(x):
    # x is a list (or vector) of length 256
    return max(0, x[43])
def l92_172(x):
    # x is a list (or vector) of length 256
    return max(0, x[44])
def l92_173(x):
    # x is a list (or vector) of length 256
    return max(0, x[45])
def l92_174(x):
    # x is a list (or vector) of length 256
    return max(0, x[46])
def l92_175(x):
    # x is a list (or vector) of length 256
    return max(0, x[47])
def l92_176(x):
    # x is a list (or vector) of length 256
    return max(0, x[48])
def l92_177(x):
    # x is a list (or vector) of length 256
    return max(0, x[49])
def l92_178(x):
    # x is a list (or vector) of length 256
    return max(0, x[50])
def l92_179(x):
    # x is a list (or vector) of length 256
    return max(0, x[51])
def l92_180(x):
    # x is a list (or vector) of length 256
    return max(0, x[52])
def l92_181(x):
    # x is a list (or vector) of length 256
    return max(0, x[53])
def l92_182(x):
    # x is a list (or vector) of length 256
    return max(0, x[54])
def l92_183(x):
    # x is a list (or vector) of length 256
    return max(0, x[55])
def l92_184(x):
    # x is a list (or vector) of length 256
    return max(0, x[56])
def l92_185(x):
    # x is a list (or vector) of length 256
    return max(0, x[57])
def l92_186(x):
    # x is a list (or vector) of length 256
    return max(0, x[58])
def l92_187(x):
    # x is a list (or vector) of length 256
    return max(0, x[59])
def l92_188(x):
    # x is a list (or vector) of length 256
    return max(0, x[60])
def l92_189(x):
    # x is a list (or vector) of length 256
    return max(0, x[61])
def l92_190(x):
    # x is a list (or vector) of length 256
    return max(0, x[62])
def l92_191(x):
    # x is a list (or vector) of length 256
    return max(0, x[63])
def l92_192(x):
    # x is a list (or vector) of length 256
    return max(0, x[160])
def l92_193(x):
    # x is a list (or vector) of length 256
    return max(0, x[161])
def l92_194(x):
    # x is a list (or vector) of length 256
    return max(0, x[162])
def l92_195(x):
    # x is a list (or vector) of length 256
    return max(0, x[163])
def l92_196(x):
    # x is a list (or vector) of length 256
    return max(0, x[164])
def l92_197(x):
    # x is a list (or vector) of length 256
    return max(0, x[165])
def l92_198(x):
    # x is a list (or vector) of length 256
    return max(0, x[166])
def l92_199(x):
    # x is a list (or vector) of length 256
    return max(0, x[167])
def l92_200(x):
    # x is a list (or vector) of length 256
    return max(0, x[168])
def l92_201(x):
    # x is a list (or vector) of length 256
    return max(0, x[169])
def l92_202(x):
    # x is a list (or vector) of length 256
    return max(0, x[170])
def l92_203(x):
    # x is a list (or vector) of length 256
    return max(0, x[171])
def l92_204(x):
    # x is a list (or vector) of length 256
    return max(0, x[172])
def l92_205(x):
    # x is a list (or vector) of length 256
    return max(0, x[173])
def l92_206(x):
    # x is a list (or vector) of length 256
    return max(0, x[174])
def l92_207(x):
    # x is a list (or vector) of length 256
    return max(0, x[175])
def l92_208(x):
    # x is a list (or vector) of length 256
    return max(0, x[176])
def l92_209(x):
    # x is a list (or vector) of length 256
    return max(0, x[177])
def l92_210(x):
    # x is a list (or vector) of length 256
    return max(0, x[178])
def l92_211(x):
    # x is a list (or vector) of length 256
    return max(0, x[179])
def l92_212(x):
    # x is a list (or vector) of length 256
    return max(0, x[180])
def l92_213(x):
    # x is a list (or vector) of length 256
    return max(0, x[181])
def l92_214(x):
    # x is a list (or vector) of length 256
    return max(0, x[182])
def l92_215(x):
    # x is a list (or vector) of length 256
    return max(0, x[183])
def l92_216(x):
    # x is a list (or vector) of length 256
    return max(0, x[184])
def l92_217(x):
    # x is a list (or vector) of length 256
    return max(0, x[185])
def l92_218(x):
    # x is a list (or vector) of length 256
    return max(0, x[186])
def l92_219(x):
    # x is a list (or vector) of length 256
    return max(0, x[187])
def l92_220(x):
    # x is a list (or vector) of length 256
    return max(0, x[188])
def l92_221(x):
    # x is a list (or vector) of length 256
    return max(0, x[189])
def l92_222(x):
    # x is a list (or vector) of length 256
    return max(0, x[190])
def l92_223(x):
    # x is a list (or vector) of length 256
    return max(0, x[191])
def l92_224(x):
    # x is a list (or vector) of length 256
    return max(0, x[192])
def l92_225(x):
    # x is a list (or vector) of length 256
    return max(0, x[193])
def l92_226(x):
    # x is a list (or vector) of length 256
    return max(0, x[194])
def l92_227(x):
    # x is a list (or vector) of length 256
    return max(0, x[195])
def l92_228(x):
    # x is a list (or vector) of length 256
    return max(0, x[196])
def l92_229(x):
    # x is a list (or vector) of length 256
    return max(0, x[197])
def l92_230(x):
    # x is a list (or vector) of length 256
    return max(0, x[198])
def l92_231(x):
    # x is a list (or vector) of length 256
    return max(0, x[199])
def l92_232(x):
    # x is a list (or vector) of length 256
    return max(0, x[200])
def l92_233(x):
    # x is a list (or vector) of length 256
    return max(0, x[201])
def l92_234(x):
    # x is a list (or vector) of length 256
    return max(0, x[202])
def l92_235(x):
    # x is a list (or vector) of length 256
    return max(0, x[203])
def l92_236(x):
    # x is a list (or vector) of length 256
    return max(0, x[204])
def l92_237(x):
    # x is a list (or vector) of length 256
    return max(0, x[205])
def l92_238(x):
    # x is a list (or vector) of length 256
    return max(0, x[206])
def l92_239(x):
    # x is a list (or vector) of length 256
    return max(0, x[207])
def l92_240(x):
    # x is a list (or vector) of length 256
    return max(0, x[208])
def l92_241(x):
    # x is a list (or vector) of length 256
    return max(0, x[209])
def l92_242(x):
    # x is a list (or vector) of length 256
    return max(0, x[210])
def l92_243(x):
    # x is a list (or vector) of length 256
    return max(0, x[211])
def l92_244(x):
    # x is a list (or vector) of length 256
    return max(0, x[212])
def l92_245(x):
    # x is a list (or vector) of length 256
    return max(0, x[213])
def l92_246(x):
    # x is a list (or vector) of length 256
    return max(0, x[214])
def l92_247(x):
    # x is a list (or vector) of length 256
    return max(0, x[215])
def l92_248(x):
    # x is a list (or vector) of length 256
    return max(0, x[216])
def l92_249(x):
    # x is a list (or vector) of length 256
    return max(0, x[217])
def l92_250(x):
    # x is a list (or vector) of length 256
    return max(0, x[218])
def l92_251(x):
    # x is a list (or vector) of length 256
    return max(0, x[219])
def l92_252(x):
    # x is a list (or vector) of length 256
    return max(0, x[220])
def l92_253(x):
    # x is a list (or vector) of length 256
    return max(0, x[221])
def l92_254(x):
    # x is a list (or vector) of length 256
    return max(0, x[222])
def l92_255(x):
    # x is a list (or vector) of length 256
    return max(0, x[223])
def l92_256(x):
    # x is a list (or vector) of length 256
    return max(0, x[224])
def l92_257(x):
    # x is a list (or vector) of length 256
    return max(0, x[225])
def l92_258(x):
    # x is a list (or vector) of length 256
    return max(0, x[226])
def l92_259(x):
    # x is a list (or vector) of length 256
    return max(0, x[227])
def l92_260(x):
    # x is a list (or vector) of length 256
    return max(0, x[228])
def l92_261(x):
    # x is a list (or vector) of length 256
    return max(0, x[229])
def l92_262(x):
    # x is a list (or vector) of length 256
    return max(0, x[230])
def l92_263(x):
    # x is a list (or vector) of length 256
    return max(0, x[231])
def l92_264(x):
    # x is a list (or vector) of length 256
    return max(0, x[232])
def l92_265(x):
    # x is a list (or vector) of length 256
    return max(0, x[233])
def l92_266(x):
    # x is a list (or vector) of length 256
    return max(0, x[234])
def l92_267(x):
    # x is a list (or vector) of length 256
    return max(0, x[235])
def l92_268(x):
    # x is a list (or vector) of length 256
    return max(0, x[236])
def l92_269(x):
    # x is a list (or vector) of length 256
    return max(0, x[237])
def l92_270(x):
    # x is a list (or vector) of length 256
    return max(0, x[238])
def l92_271(x):
    # x is a list (or vector) of length 256
    return max(0, x[239])
def l92_272(x):
    # x is a list (or vector) of length 256
    return max(0, x[240])
def l92_273(x):
    # x is a list (or vector) of length 256
    return max(0, x[241])
def l92_274(x):
    # x is a list (or vector) of length 256
    return max(0, x[242])
def l92_275(x):
    # x is a list (or vector) of length 256
    return max(0, x[243])
def l92_276(x):
    # x is a list (or vector) of length 256
    return max(0, x[244])
def l92_277(x):
    # x is a list (or vector) of length 256
    return max(0, x[245])
def l92_278(x):
    # x is a list (or vector) of length 256
    return max(0, x[246])
def l92_279(x):
    # x is a list (or vector) of length 256
    return max(0, x[247])
def l92_280(x):
    # x is a list (or vector) of length 256
    return max(0, x[248])
def l92_281(x):
    # x is a list (or vector) of length 256
    return max(0, x[249])
def l92_282(x):
    # x is a list (or vector) of length 256
    return max(0, x[250])
def l92_283(x):
    # x is a list (or vector) of length 256
    return max(0, x[251])
def l92_284(x):
    # x is a list (or vector) of length 256
    return max(0, x[252])
def l92_285(x):
    # x is a list (or vector) of length 256
    return max(0, x[253])
def l92_286(x):
    # x is a list (or vector) of length 256
    return max(0, x[254])
def l92_287(x):
    # x is a list (or vector) of length 256
    return max(0, x[255])
def l92_(x):
    # x is a list (or vector) of length 256
    return [
        l92_0(x),
        l92_1(x),
        l92_2(x),
        l92_3(x),
        l92_4(x),
        l92_5(x),
        l92_6(x),
        l92_7(x),
        l92_8(x),
        l92_9(x),
        l92_10(x),
        l92_11(x),
        l92_12(x),
        l92_13(x),
        l92_14(x),
        l92_15(x),
        l92_16(x),
        l92_17(x),
        l92_18(x),
        l92_19(x),
        l92_20(x),
        l92_21(x),
        l92_22(x),
        l92_23(x),
        l92_24(x),
        l92_25(x),
        l92_26(x),
        l92_27(x),
        l92_28(x),
        l92_29(x),
        l92_30(x),
        l92_31(x),
        l92_32(x),
        l92_33(x),
        l92_34(x),
        l92_35(x),
        l92_36(x),
        l92_37(x),
        l92_38(x),
        l92_39(x),
        l92_40(x),
        l92_41(x),
        l92_42(x),
        l92_43(x),
        l92_44(x),
        l92_45(x),
        l92_46(x),
        l92_47(x),
        l92_48(x),
        l92_49(x),
        l92_50(x),
        l92_51(x),
        l92_52(x),
        l92_53(x),
        l92_54(x),
        l92_55(x),
        l92_56(x),
        l92_57(x),
        l92_58(x),
        l92_59(x),
        l92_60(x),
        l92_61(x),
        l92_62(x),
        l92_63(x),
        l92_64(x),
        l92_65(x),
        l92_66(x),
        l92_67(x),
        l92_68(x),
        l92_69(x),
        l92_70(x),
        l92_71(x),
        l92_72(x),
        l92_73(x),
        l92_74(x),
        l92_75(x),
        l92_76(x),
        l92_77(x),
        l92_78(x),
        l92_79(x),
        l92_80(x),
        l92_81(x),
        l92_82(x),
        l92_83(x),
        l92_84(x),
        l92_85(x),
        l92_86(x),
        l92_87(x),
        l92_88(x),
        l92_89(x),
        l92_90(x),
        l92_91(x),
        l92_92(x),
        l92_93(x),
        l92_94(x),
        l92_95(x),
        l92_96(x),
        l92_97(x),
        l92_98(x),
        l92_99(x),
        l92_100(x),
        l92_101(x),
        l92_102(x),
        l92_103(x),
        l92_104(x),
        l92_105(x),
        l92_106(x),
        l92_107(x),
        l92_108(x),
        l92_109(x),
        l92_110(x),
        l92_111(x),
        l92_112(x),
        l92_113(x),
        l92_114(x),
        l92_115(x),
        l92_116(x),
        l92_117(x),
        l92_118(x),
        l92_119(x),
        l92_120(x),
        l92_121(x),
        l92_122(x),
        l92_123(x),
        l92_124(x),
        l92_125(x),
        l92_126(x),
        l92_127(x),
        l92_128(x),
        l92_129(x),
        l92_130(x),
        l92_131(x),
        l92_132(x),
        l92_133(x),
        l92_134(x),
        l92_135(x),
        l92_136(x),
        l92_137(x),
        l92_138(x),
        l92_139(x),
        l92_140(x),
        l92_141(x),
        l92_142(x),
        l92_143(x),
        l92_144(x),
        l92_145(x),
        l92_146(x),
        l92_147(x),
        l92_148(x),
        l92_149(x),
        l92_150(x),
        l92_151(x),
        l92_152(x),
        l92_153(x),
        l92_154(x),
        l92_155(x),
        l92_156(x),
        l92_157(x),
        l92_158(x),
        l92_159(x),
        l92_160(x),
        l92_161(x),
        l92_162(x),
        l92_163(x),
        l92_164(x),
        l92_165(x),
        l92_166(x),
        l92_167(x),
        l92_168(x),
        l92_169(x),
        l92_170(x),
        l92_171(x),
        l92_172(x),
        l92_173(x),
        l92_174(x),
        l92_175(x),
        l92_176(x),
        l92_177(x),
        l92_178(x),
        l92_179(x),
        l92_180(x),
        l92_181(x),
        l92_182(x),
        l92_183(x),
        l92_184(x),
        l92_185(x),
        l92_186(x),
        l92_187(x),
        l92_188(x),
        l92_189(x),
        l92_190(x),
        l92_191(x),
        l92_192(x),
        l92_193(x),
        l92_194(x),
        l92_195(x),
        l92_196(x),
        l92_197(x),
        l92_198(x),
        l92_199(x),
        l92_200(x),
        l92_201(x),
        l92_202(x),
        l92_203(x),
        l92_204(x),
        l92_205(x),
        l92_206(x),
        l92_207(x),
        l92_208(x),
        l92_209(x),
        l92_210(x),
        l92_211(x),
        l92_212(x),
        l92_213(x),
        l92_214(x),
        l92_215(x),
        l92_216(x),
        l92_217(x),
        l92_218(x),
        l92_219(x),
        l92_220(x),
        l92_221(x),
        l92_222(x),
        l92_223(x),
        l92_224(x),
        l92_225(x),
        l92_226(x),
        l92_227(x),
        l92_228(x),
        l92_229(x),
        l92_230(x),
        l92_231(x),
        l92_232(x),
        l92_233(x),
        l92_234(x),
        l92_235(x),
        l92_236(x),
        l92_237(x),
        l92_238(x),
        l92_239(x),
        l92_240(x),
        l92_241(x),
        l92_242(x),
        l92_243(x),
        l92_244(x),
        l92_245(x),
        l92_246(x),
        l92_247(x),
        l92_248(x),
        l92_249(x),
        l92_250(x),
        l92_251(x),
        l92_252(x),
        l92_253(x),
        l92_254(x),
        l92_255(x),
        l92_256(x),
        l92_257(x),
        l92_258(x),
        l92_259(x),
        l92_260(x),
        l92_261(x),
        l92_262(x),
        l92_263(x),
        l92_264(x),
        l92_265(x),
        l92_266(x),
        l92_267(x),
        l92_268(x),
        l92_269(x),
        l92_270(x),
        l92_271(x),
        l92_272(x),
        l92_273(x),
        l92_274(x),
        l92_275(x),
        l92_276(x),
        l92_277(x),
        l92_278(x),
        l92_279(x),
        l92_280(x),
        l92_281(x),
        l92_282(x),
        l92_283(x),
        l92_284(x),
        l92_285(x),
        l92_286(x),
        l92_287(x),
    ]