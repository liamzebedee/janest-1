import numpy as np




# Generated from reverse engineering
def l344_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 288
    out = np.empty(288, dtype=np.float32)
    
    # for i in range(0, 32):
    for i in range(0, 32):
        s = x[64 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(32, 54):
    for i in range(0, 22):
        s = x[0 + i] + x[106 + i] + -2.0 * x[i + 138]
        s += biases[i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(54, 64):
    for i in range(0, 10):
        s = x[22 + i] + x[96 + i] + -2.0 * x[i + 128]
        s += biases[i]
        out[54 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 86):
    for i in range(0, 22):
        s = x[0 + i] + x[106 + i] + -2.0 * x[i + 138]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(86, 96):
    for i in range(0, 10):
        s = x[22 + i] + x[96 + i] + -2.0 * x[i + 128]
        out[86 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(96, 118):
    for i in range(0, 22):
        s = x[0 + i] + x[106 + i] + -2.0 * x[i + 138]
        s += biases[i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(118, 128):
    for i in range(0, 10):
        s = x[22 + i] + x[96 + i] + -2.0 * x[i + 128]
        s += biases[i]
        out[118 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 192):
    for i in range(0, 64):
        s = x[0 + i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(192, 288):
    for i in range(0, 96):
        s = x[160 + i]
        out[192 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l344_0(x):
    # x is a list (or vector) of length 256
    return max(0, x[64])
def l344_1(x):
    # x is a list (or vector) of length 256
    return max(0, x[65])
def l344_2(x):
    # x is a list (or vector) of length 256
    return max(0, x[66])
def l344_3(x):
    # x is a list (or vector) of length 256
    return max(0, x[67])
def l344_4(x):
    # x is a list (or vector) of length 256
    return max(0, x[68])
def l344_5(x):
    # x is a list (or vector) of length 256
    return max(0, x[69])
def l344_6(x):
    # x is a list (or vector) of length 256
    return max(0, x[70])
def l344_7(x):
    # x is a list (or vector) of length 256
    return max(0, x[71])
def l344_8(x):
    # x is a list (or vector) of length 256
    return max(0, x[72])
def l344_9(x):
    # x is a list (or vector) of length 256
    return max(0, x[73])
def l344_10(x):
    # x is a list (or vector) of length 256
    return max(0, x[74])
def l344_11(x):
    # x is a list (or vector) of length 256
    return max(0, x[75])
def l344_12(x):
    # x is a list (or vector) of length 256
    return max(0, x[76])
def l344_13(x):
    # x is a list (or vector) of length 256
    return max(0, x[77])
def l344_14(x):
    # x is a list (or vector) of length 256
    return max(0, x[78])
def l344_15(x):
    # x is a list (or vector) of length 256
    return max(0, x[79])
def l344_16(x):
    # x is a list (or vector) of length 256
    return max(0, x[80])
def l344_17(x):
    # x is a list (or vector) of length 256
    return max(0, x[81])
def l344_18(x):
    # x is a list (or vector) of length 256
    return max(0, x[82])
def l344_19(x):
    # x is a list (or vector) of length 256
    return max(0, x[83])
def l344_20(x):
    # x is a list (or vector) of length 256
    return max(0, x[84])
def l344_21(x):
    # x is a list (or vector) of length 256
    return max(0, x[85])
def l344_22(x):
    # x is a list (or vector) of length 256
    return max(0, x[86])
def l344_23(x):
    # x is a list (or vector) of length 256
    return max(0, x[87])
def l344_24(x):
    # x is a list (or vector) of length 256
    return max(0, x[88])
def l344_25(x):
    # x is a list (or vector) of length 256
    return max(0, x[89])
def l344_26(x):
    # x is a list (or vector) of length 256
    return max(0, x[90])
def l344_27(x):
    # x is a list (or vector) of length 256
    return max(0, x[91])
def l344_28(x):
    # x is a list (or vector) of length 256
    return max(0, x[92])
def l344_29(x):
    # x is a list (or vector) of length 256
    return max(0, x[93])
def l344_30(x):
    # x is a list (or vector) of length 256
    return max(0, x[94])
def l344_31(x):
    # x is a list (or vector) of length 256
    return max(0, x[95])
def l344_32(x):
    # x is a list (or vector) of length 256
    return max(0, x[0] + x[106] + -2.0*x[138] + -1.0)
def l344_33(x):
    # x is a list (or vector) of length 256
    return max(0, x[1] + x[107] + -2.0*x[139] + -1.0)
def l344_34(x):
    # x is a list (or vector) of length 256
    return max(0, x[2] + x[108] + -2.0*x[140] + -1.0)
def l344_35(x):
    # x is a list (or vector) of length 256
    return max(0, x[3] + x[109] + -2.0*x[141] + -1.0)
def l344_36(x):
    # x is a list (or vector) of length 256
    return max(0, x[4] + x[110] + -2.0*x[142] + -1.0)
def l344_37(x):
    # x is a list (or vector) of length 256
    return max(0, x[5] + x[111] + -2.0*x[143] + -1.0)
def l344_38(x):
    # x is a list (or vector) of length 256
    return max(0, x[6] + x[112] + -2.0*x[144] + -1.0)
def l344_39(x):
    # x is a list (or vector) of length 256
    return max(0, x[7] + x[113] + -2.0*x[145] + -1.0)
def l344_40(x):
    # x is a list (or vector) of length 256
    return max(0, x[8] + x[114] + -2.0*x[146] + -1.0)
def l344_41(x):
    # x is a list (or vector) of length 256
    return max(0, x[9] + x[115] + -2.0*x[147] + -1.0)
def l344_42(x):
    # x is a list (or vector) of length 256
    return max(0, x[10] + x[116] + -2.0*x[148] + -1.0)
def l344_43(x):
    # x is a list (or vector) of length 256
    return max(0, x[11] + x[117] + -2.0*x[149] + -1.0)
def l344_44(x):
    # x is a list (or vector) of length 256
    return max(0, x[12] + x[118] + -2.0*x[150] + -1.0)
def l344_45(x):
    # x is a list (or vector) of length 256
    return max(0, x[13] + x[119] + -2.0*x[151] + -1.0)
def l344_46(x):
    # x is a list (or vector) of length 256
    return max(0, x[14] + x[120] + -2.0*x[152] + -1.0)
def l344_47(x):
    # x is a list (or vector) of length 256
    return max(0, x[15] + x[121] + -2.0*x[153] + -1.0)
def l344_48(x):
    # x is a list (or vector) of length 256
    return max(0, x[16] + x[122] + -2.0*x[154] + -1.0)
def l344_49(x):
    # x is a list (or vector) of length 256
    return max(0, x[17] + x[123] + -2.0*x[155] + -1.0)
def l344_50(x):
    # x is a list (or vector) of length 256
    return max(0, x[18] + x[124] + -2.0*x[156] + -1.0)
def l344_51(x):
    # x is a list (or vector) of length 256
    return max(0, x[19] + x[125] + -2.0*x[157] + -1.0)
def l344_52(x):
    # x is a list (or vector) of length 256
    return max(0, x[20] + x[126] + -2.0*x[158] + -1.0)
def l344_53(x):
    # x is a list (or vector) of length 256
    return max(0, x[21] + x[127] + -2.0*x[159] + -1.0)
def l344_54(x):
    # x is a list (or vector) of length 256
    return max(0, x[22] + x[96] + -2.0*x[128] + -1.0)
def l344_55(x):
    # x is a list (or vector) of length 256
    return max(0, x[23] + x[97] + -2.0*x[129] + -1.0)
def l344_56(x):
    # x is a list (or vector) of length 256
    return max(0, x[24] + x[98] + -2.0*x[130] + -1.0)
def l344_57(x):
    # x is a list (or vector) of length 256
    return max(0, x[25] + x[99] + -2.0*x[131] + -1.0)
def l344_58(x):
    # x is a list (or vector) of length 256
    return max(0, x[26] + x[100] + -2.0*x[132] + -1.0)
def l344_59(x):
    # x is a list (or vector) of length 256
    return max(0, x[27] + x[101] + -2.0*x[133] + -1.0)
def l344_60(x):
    # x is a list (or vector) of length 256
    return max(0, x[28] + x[102] + -2.0*x[134] + -1.0)
def l344_61(x):
    # x is a list (or vector) of length 256
    return max(0, x[29] + x[103] + -2.0*x[135] + -1.0)
def l344_62(x):
    # x is a list (or vector) of length 256
    return max(0, x[30] + x[104] + -2.0*x[136] + -1.0)
def l344_63(x):
    # x is a list (or vector) of length 256
    return max(0, x[31] + x[105] + -2.0*x[137] + -1.0)
def l344_64(x):
    # x is a list (or vector) of length 256
    return max(0, x[0] + x[106] + -2.0*x[138])
def l344_65(x):
    # x is a list (or vector) of length 256
    return max(0, x[1] + x[107] + -2.0*x[139])
def l344_66(x):
    # x is a list (or vector) of length 256
    return max(0, x[2] + x[108] + -2.0*x[140])
def l344_67(x):
    # x is a list (or vector) of length 256
    return max(0, x[3] + x[109] + -2.0*x[141])
def l344_68(x):
    # x is a list (or vector) of length 256
    return max(0, x[4] + x[110] + -2.0*x[142])
def l344_69(x):
    # x is a list (or vector) of length 256
    return max(0, x[5] + x[111] + -2.0*x[143])
def l344_70(x):
    # x is a list (or vector) of length 256
    return max(0, x[6] + x[112] + -2.0*x[144])
def l344_71(x):
    # x is a list (or vector) of length 256
    return max(0, x[7] + x[113] + -2.0*x[145])
def l344_72(x):
    # x is a list (or vector) of length 256
    return max(0, x[8] + x[114] + -2.0*x[146])
def l344_73(x):
    # x is a list (or vector) of length 256
    return max(0, x[9] + x[115] + -2.0*x[147])
def l344_74(x):
    # x is a list (or vector) of length 256
    return max(0, x[10] + x[116] + -2.0*x[148])
def l344_75(x):
    # x is a list (or vector) of length 256
    return max(0, x[11] + x[117] + -2.0*x[149])
def l344_76(x):
    # x is a list (or vector) of length 256
    return max(0, x[12] + x[118] + -2.0*x[150])
def l344_77(x):
    # x is a list (or vector) of length 256
    return max(0, x[13] + x[119] + -2.0*x[151])
def l344_78(x):
    # x is a list (or vector) of length 256
    return max(0, x[14] + x[120] + -2.0*x[152])
def l344_79(x):
    # x is a list (or vector) of length 256
    return max(0, x[15] + x[121] + -2.0*x[153])
def l344_80(x):
    # x is a list (or vector) of length 256
    return max(0, x[16] + x[122] + -2.0*x[154])
def l344_81(x):
    # x is a list (or vector) of length 256
    return max(0, x[17] + x[123] + -2.0*x[155])
def l344_82(x):
    # x is a list (or vector) of length 256
    return max(0, x[18] + x[124] + -2.0*x[156])
def l344_83(x):
    # x is a list (or vector) of length 256
    return max(0, x[19] + x[125] + -2.0*x[157])
def l344_84(x):
    # x is a list (or vector) of length 256
    return max(0, x[20] + x[126] + -2.0*x[158])
def l344_85(x):
    # x is a list (or vector) of length 256
    return max(0, x[21] + x[127] + -2.0*x[159])
def l344_86(x):
    # x is a list (or vector) of length 256
    return max(0, x[22] + x[96] + -2.0*x[128])
def l344_87(x):
    # x is a list (or vector) of length 256
    return max(0, x[23] + x[97] + -2.0*x[129])
def l344_88(x):
    # x is a list (or vector) of length 256
    return max(0, x[24] + x[98] + -2.0*x[130])
def l344_89(x):
    # x is a list (or vector) of length 256
    return max(0, x[25] + x[99] + -2.0*x[131])
def l344_90(x):
    # x is a list (or vector) of length 256
    return max(0, x[26] + x[100] + -2.0*x[132])
def l344_91(x):
    # x is a list (or vector) of length 256
    return max(0, x[27] + x[101] + -2.0*x[133])
def l344_92(x):
    # x is a list (or vector) of length 256
    return max(0, x[28] + x[102] + -2.0*x[134])
def l344_93(x):
    # x is a list (or vector) of length 256
    return max(0, x[29] + x[103] + -2.0*x[135])
def l344_94(x):
    # x is a list (or vector) of length 256
    return max(0, x[30] + x[104] + -2.0*x[136])
def l344_95(x):
    # x is a list (or vector) of length 256
    return max(0, x[31] + x[105] + -2.0*x[137])
def l344_96(x):
    # x is a list (or vector) of length 256
    return max(0, x[0] + x[106] + -2.0*x[138] + -1.0)
def l344_97(x):
    # x is a list (or vector) of length 256
    return max(0, x[1] + x[107] + -2.0*x[139] + -1.0)
def l344_98(x):
    # x is a list (or vector) of length 256
    return max(0, x[2] + x[108] + -2.0*x[140] + -1.0)
def l344_99(x):
    # x is a list (or vector) of length 256
    return max(0, x[3] + x[109] + -2.0*x[141] + -1.0)
def l344_100(x):
    # x is a list (or vector) of length 256
    return max(0, x[4] + x[110] + -2.0*x[142] + -1.0)
def l344_101(x):
    # x is a list (or vector) of length 256
    return max(0, x[5] + x[111] + -2.0*x[143] + -1.0)
def l344_102(x):
    # x is a list (or vector) of length 256
    return max(0, x[6] + x[112] + -2.0*x[144] + -1.0)
def l344_103(x):
    # x is a list (or vector) of length 256
    return max(0, x[7] + x[113] + -2.0*x[145] + -1.0)
def l344_104(x):
    # x is a list (or vector) of length 256
    return max(0, x[8] + x[114] + -2.0*x[146] + -1.0)
def l344_105(x):
    # x is a list (or vector) of length 256
    return max(0, x[9] + x[115] + -2.0*x[147] + -1.0)
def l344_106(x):
    # x is a list (or vector) of length 256
    return max(0, x[10] + x[116] + -2.0*x[148] + -1.0)
def l344_107(x):
    # x is a list (or vector) of length 256
    return max(0, x[11] + x[117] + -2.0*x[149] + -1.0)
def l344_108(x):
    # x is a list (or vector) of length 256
    return max(0, x[12] + x[118] + -2.0*x[150] + -1.0)
def l344_109(x):
    # x is a list (or vector) of length 256
    return max(0, x[13] + x[119] + -2.0*x[151] + -1.0)
def l344_110(x):
    # x is a list (or vector) of length 256
    return max(0, x[14] + x[120] + -2.0*x[152] + -1.0)
def l344_111(x):
    # x is a list (or vector) of length 256
    return max(0, x[15] + x[121] + -2.0*x[153] + -1.0)
def l344_112(x):
    # x is a list (or vector) of length 256
    return max(0, x[16] + x[122] + -2.0*x[154] + -1.0)
def l344_113(x):
    # x is a list (or vector) of length 256
    return max(0, x[17] + x[123] + -2.0*x[155] + -1.0)
def l344_114(x):
    # x is a list (or vector) of length 256
    return max(0, x[18] + x[124] + -2.0*x[156] + -1.0)
def l344_115(x):
    # x is a list (or vector) of length 256
    return max(0, x[19] + x[125] + -2.0*x[157] + -1.0)
def l344_116(x):
    # x is a list (or vector) of length 256
    return max(0, x[20] + x[126] + -2.0*x[158] + -1.0)
def l344_117(x):
    # x is a list (or vector) of length 256
    return max(0, x[21] + x[127] + -2.0*x[159] + -1.0)
def l344_118(x):
    # x is a list (or vector) of length 256
    return max(0, x[22] + x[96] + -2.0*x[128] + -1.0)
def l344_119(x):
    # x is a list (or vector) of length 256
    return max(0, x[23] + x[97] + -2.0*x[129] + -1.0)
def l344_120(x):
    # x is a list (or vector) of length 256
    return max(0, x[24] + x[98] + -2.0*x[130] + -1.0)
def l344_121(x):
    # x is a list (or vector) of length 256
    return max(0, x[25] + x[99] + -2.0*x[131] + -1.0)
def l344_122(x):
    # x is a list (or vector) of length 256
    return max(0, x[26] + x[100] + -2.0*x[132] + -1.0)
def l344_123(x):
    # x is a list (or vector) of length 256
    return max(0, x[27] + x[101] + -2.0*x[133] + -1.0)
def l344_124(x):
    # x is a list (or vector) of length 256
    return max(0, x[28] + x[102] + -2.0*x[134] + -1.0)
def l344_125(x):
    # x is a list (or vector) of length 256
    return max(0, x[29] + x[103] + -2.0*x[135] + -1.0)
def l344_126(x):
    # x is a list (or vector) of length 256
    return max(0, x[30] + x[104] + -2.0*x[136] + -1.0)
def l344_127(x):
    # x is a list (or vector) of length 256
    return max(0, x[31] + x[105] + -2.0*x[137] + -1.0)
def l344_128(x):
    # x is a list (or vector) of length 256
    return max(0, x[0])
def l344_129(x):
    # x is a list (or vector) of length 256
    return max(0, x[1])
def l344_130(x):
    # x is a list (or vector) of length 256
    return max(0, x[2])
def l344_131(x):
    # x is a list (or vector) of length 256
    return max(0, x[3])
def l344_132(x):
    # x is a list (or vector) of length 256
    return max(0, x[4])
def l344_133(x):
    # x is a list (or vector) of length 256
    return max(0, x[5])
def l344_134(x):
    # x is a list (or vector) of length 256
    return max(0, x[6])
def l344_135(x):
    # x is a list (or vector) of length 256
    return max(0, x[7])
def l344_136(x):
    # x is a list (or vector) of length 256
    return max(0, x[8])
def l344_137(x):
    # x is a list (or vector) of length 256
    return max(0, x[9])
def l344_138(x):
    # x is a list (or vector) of length 256
    return max(0, x[10])
def l344_139(x):
    # x is a list (or vector) of length 256
    return max(0, x[11])
def l344_140(x):
    # x is a list (or vector) of length 256
    return max(0, x[12])
def l344_141(x):
    # x is a list (or vector) of length 256
    return max(0, x[13])
def l344_142(x):
    # x is a list (or vector) of length 256
    return max(0, x[14])
def l344_143(x):
    # x is a list (or vector) of length 256
    return max(0, x[15])
def l344_144(x):
    # x is a list (or vector) of length 256
    return max(0, x[16])
def l344_145(x):
    # x is a list (or vector) of length 256
    return max(0, x[17])
def l344_146(x):
    # x is a list (or vector) of length 256
    return max(0, x[18])
def l344_147(x):
    # x is a list (or vector) of length 256
    return max(0, x[19])
def l344_148(x):
    # x is a list (or vector) of length 256
    return max(0, x[20])
def l344_149(x):
    # x is a list (or vector) of length 256
    return max(0, x[21])
def l344_150(x):
    # x is a list (or vector) of length 256
    return max(0, x[22])
def l344_151(x):
    # x is a list (or vector) of length 256
    return max(0, x[23])
def l344_152(x):
    # x is a list (or vector) of length 256
    return max(0, x[24])
def l344_153(x):
    # x is a list (or vector) of length 256
    return max(0, x[25])
def l344_154(x):
    # x is a list (or vector) of length 256
    return max(0, x[26])
def l344_155(x):
    # x is a list (or vector) of length 256
    return max(0, x[27])
def l344_156(x):
    # x is a list (or vector) of length 256
    return max(0, x[28])
def l344_157(x):
    # x is a list (or vector) of length 256
    return max(0, x[29])
def l344_158(x):
    # x is a list (or vector) of length 256
    return max(0, x[30])
def l344_159(x):
    # x is a list (or vector) of length 256
    return max(0, x[31])
def l344_160(x):
    # x is a list (or vector) of length 256
    return max(0, x[32])
def l344_161(x):
    # x is a list (or vector) of length 256
    return max(0, x[33])
def l344_162(x):
    # x is a list (or vector) of length 256
    return max(0, x[34])
def l344_163(x):
    # x is a list (or vector) of length 256
    return max(0, x[35])
def l344_164(x):
    # x is a list (or vector) of length 256
    return max(0, x[36])
def l344_165(x):
    # x is a list (or vector) of length 256
    return max(0, x[37])
def l344_166(x):
    # x is a list (or vector) of length 256
    return max(0, x[38])
def l344_167(x):
    # x is a list (or vector) of length 256
    return max(0, x[39])
def l344_168(x):
    # x is a list (or vector) of length 256
    return max(0, x[40])
def l344_169(x):
    # x is a list (or vector) of length 256
    return max(0, x[41])
def l344_170(x):
    # x is a list (or vector) of length 256
    return max(0, x[42])
def l344_171(x):
    # x is a list (or vector) of length 256
    return max(0, x[43])
def l344_172(x):
    # x is a list (or vector) of length 256
    return max(0, x[44])
def l344_173(x):
    # x is a list (or vector) of length 256
    return max(0, x[45])
def l344_174(x):
    # x is a list (or vector) of length 256
    return max(0, x[46])
def l344_175(x):
    # x is a list (or vector) of length 256
    return max(0, x[47])
def l344_176(x):
    # x is a list (or vector) of length 256
    return max(0, x[48])
def l344_177(x):
    # x is a list (or vector) of length 256
    return max(0, x[49])
def l344_178(x):
    # x is a list (or vector) of length 256
    return max(0, x[50])
def l344_179(x):
    # x is a list (or vector) of length 256
    return max(0, x[51])
def l344_180(x):
    # x is a list (or vector) of length 256
    return max(0, x[52])
def l344_181(x):
    # x is a list (or vector) of length 256
    return max(0, x[53])
def l344_182(x):
    # x is a list (or vector) of length 256
    return max(0, x[54])
def l344_183(x):
    # x is a list (or vector) of length 256
    return max(0, x[55])
def l344_184(x):
    # x is a list (or vector) of length 256
    return max(0, x[56])
def l344_185(x):
    # x is a list (or vector) of length 256
    return max(0, x[57])
def l344_186(x):
    # x is a list (or vector) of length 256
    return max(0, x[58])
def l344_187(x):
    # x is a list (or vector) of length 256
    return max(0, x[59])
def l344_188(x):
    # x is a list (or vector) of length 256
    return max(0, x[60])
def l344_189(x):
    # x is a list (or vector) of length 256
    return max(0, x[61])
def l344_190(x):
    # x is a list (or vector) of length 256
    return max(0, x[62])
def l344_191(x):
    # x is a list (or vector) of length 256
    return max(0, x[63])
def l344_192(x):
    # x is a list (or vector) of length 256
    return max(0, x[160])
def l344_193(x):
    # x is a list (or vector) of length 256
    return max(0, x[161])
def l344_194(x):
    # x is a list (or vector) of length 256
    return max(0, x[162])
def l344_195(x):
    # x is a list (or vector) of length 256
    return max(0, x[163])
def l344_196(x):
    # x is a list (or vector) of length 256
    return max(0, x[164])
def l344_197(x):
    # x is a list (or vector) of length 256
    return max(0, x[165])
def l344_198(x):
    # x is a list (or vector) of length 256
    return max(0, x[166])
def l344_199(x):
    # x is a list (or vector) of length 256
    return max(0, x[167])
def l344_200(x):
    # x is a list (or vector) of length 256
    return max(0, x[168])
def l344_201(x):
    # x is a list (or vector) of length 256
    return max(0, x[169])
def l344_202(x):
    # x is a list (or vector) of length 256
    return max(0, x[170])
def l344_203(x):
    # x is a list (or vector) of length 256
    return max(0, x[171])
def l344_204(x):
    # x is a list (or vector) of length 256
    return max(0, x[172])
def l344_205(x):
    # x is a list (or vector) of length 256
    return max(0, x[173])
def l344_206(x):
    # x is a list (or vector) of length 256
    return max(0, x[174])
def l344_207(x):
    # x is a list (or vector) of length 256
    return max(0, x[175])
def l344_208(x):
    # x is a list (or vector) of length 256
    return max(0, x[176])
def l344_209(x):
    # x is a list (or vector) of length 256
    return max(0, x[177])
def l344_210(x):
    # x is a list (or vector) of length 256
    return max(0, x[178])
def l344_211(x):
    # x is a list (or vector) of length 256
    return max(0, x[179])
def l344_212(x):
    # x is a list (or vector) of length 256
    return max(0, x[180])
def l344_213(x):
    # x is a list (or vector) of length 256
    return max(0, x[181])
def l344_214(x):
    # x is a list (or vector) of length 256
    return max(0, x[182])
def l344_215(x):
    # x is a list (or vector) of length 256
    return max(0, x[183])
def l344_216(x):
    # x is a list (or vector) of length 256
    return max(0, x[184])
def l344_217(x):
    # x is a list (or vector) of length 256
    return max(0, x[185])
def l344_218(x):
    # x is a list (or vector) of length 256
    return max(0, x[186])
def l344_219(x):
    # x is a list (or vector) of length 256
    return max(0, x[187])
def l344_220(x):
    # x is a list (or vector) of length 256
    return max(0, x[188])
def l344_221(x):
    # x is a list (or vector) of length 256
    return max(0, x[189])
def l344_222(x):
    # x is a list (or vector) of length 256
    return max(0, x[190])
def l344_223(x):
    # x is a list (or vector) of length 256
    return max(0, x[191])
def l344_224(x):
    # x is a list (or vector) of length 256
    return max(0, x[192])
def l344_225(x):
    # x is a list (or vector) of length 256
    return max(0, x[193])
def l344_226(x):
    # x is a list (or vector) of length 256
    return max(0, x[194])
def l344_227(x):
    # x is a list (or vector) of length 256
    return max(0, x[195])
def l344_228(x):
    # x is a list (or vector) of length 256
    return max(0, x[196])
def l344_229(x):
    # x is a list (or vector) of length 256
    return max(0, x[197])
def l344_230(x):
    # x is a list (or vector) of length 256
    return max(0, x[198])
def l344_231(x):
    # x is a list (or vector) of length 256
    return max(0, x[199])
def l344_232(x):
    # x is a list (or vector) of length 256
    return max(0, x[200])
def l344_233(x):
    # x is a list (or vector) of length 256
    return max(0, x[201])
def l344_234(x):
    # x is a list (or vector) of length 256
    return max(0, x[202])
def l344_235(x):
    # x is a list (or vector) of length 256
    return max(0, x[203])
def l344_236(x):
    # x is a list (or vector) of length 256
    return max(0, x[204])
def l344_237(x):
    # x is a list (or vector) of length 256
    return max(0, x[205])
def l344_238(x):
    # x is a list (or vector) of length 256
    return max(0, x[206])
def l344_239(x):
    # x is a list (or vector) of length 256
    return max(0, x[207])
def l344_240(x):
    # x is a list (or vector) of length 256
    return max(0, x[208])
def l344_241(x):
    # x is a list (or vector) of length 256
    return max(0, x[209])
def l344_242(x):
    # x is a list (or vector) of length 256
    return max(0, x[210])
def l344_243(x):
    # x is a list (or vector) of length 256
    return max(0, x[211])
def l344_244(x):
    # x is a list (or vector) of length 256
    return max(0, x[212])
def l344_245(x):
    # x is a list (or vector) of length 256
    return max(0, x[213])
def l344_246(x):
    # x is a list (or vector) of length 256
    return max(0, x[214])
def l344_247(x):
    # x is a list (or vector) of length 256
    return max(0, x[215])
def l344_248(x):
    # x is a list (or vector) of length 256
    return max(0, x[216])
def l344_249(x):
    # x is a list (or vector) of length 256
    return max(0, x[217])
def l344_250(x):
    # x is a list (or vector) of length 256
    return max(0, x[218])
def l344_251(x):
    # x is a list (or vector) of length 256
    return max(0, x[219])
def l344_252(x):
    # x is a list (or vector) of length 256
    return max(0, x[220])
def l344_253(x):
    # x is a list (or vector) of length 256
    return max(0, x[221])
def l344_254(x):
    # x is a list (or vector) of length 256
    return max(0, x[222])
def l344_255(x):
    # x is a list (or vector) of length 256
    return max(0, x[223])
def l344_256(x):
    # x is a list (or vector) of length 256
    return max(0, x[224])
def l344_257(x):
    # x is a list (or vector) of length 256
    return max(0, x[225])
def l344_258(x):
    # x is a list (or vector) of length 256
    return max(0, x[226])
def l344_259(x):
    # x is a list (or vector) of length 256
    return max(0, x[227])
def l344_260(x):
    # x is a list (or vector) of length 256
    return max(0, x[228])
def l344_261(x):
    # x is a list (or vector) of length 256
    return max(0, x[229])
def l344_262(x):
    # x is a list (or vector) of length 256
    return max(0, x[230])
def l344_263(x):
    # x is a list (or vector) of length 256
    return max(0, x[231])
def l344_264(x):
    # x is a list (or vector) of length 256
    return max(0, x[232])
def l344_265(x):
    # x is a list (or vector) of length 256
    return max(0, x[233])
def l344_266(x):
    # x is a list (or vector) of length 256
    return max(0, x[234])
def l344_267(x):
    # x is a list (or vector) of length 256
    return max(0, x[235])
def l344_268(x):
    # x is a list (or vector) of length 256
    return max(0, x[236])
def l344_269(x):
    # x is a list (or vector) of length 256
    return max(0, x[237])
def l344_270(x):
    # x is a list (or vector) of length 256
    return max(0, x[238])
def l344_271(x):
    # x is a list (or vector) of length 256
    return max(0, x[239])
def l344_272(x):
    # x is a list (or vector) of length 256
    return max(0, x[240])
def l344_273(x):
    # x is a list (or vector) of length 256
    return max(0, x[241])
def l344_274(x):
    # x is a list (or vector) of length 256
    return max(0, x[242])
def l344_275(x):
    # x is a list (or vector) of length 256
    return max(0, x[243])
def l344_276(x):
    # x is a list (or vector) of length 256
    return max(0, x[244])
def l344_277(x):
    # x is a list (or vector) of length 256
    return max(0, x[245])
def l344_278(x):
    # x is a list (or vector) of length 256
    return max(0, x[246])
def l344_279(x):
    # x is a list (or vector) of length 256
    return max(0, x[247])
def l344_280(x):
    # x is a list (or vector) of length 256
    return max(0, x[248])
def l344_281(x):
    # x is a list (or vector) of length 256
    return max(0, x[249])
def l344_282(x):
    # x is a list (or vector) of length 256
    return max(0, x[250])
def l344_283(x):
    # x is a list (or vector) of length 256
    return max(0, x[251])
def l344_284(x):
    # x is a list (or vector) of length 256
    return max(0, x[252])
def l344_285(x):
    # x is a list (or vector) of length 256
    return max(0, x[253])
def l344_286(x):
    # x is a list (or vector) of length 256
    return max(0, x[254])
def l344_287(x):
    # x is a list (or vector) of length 256
    return max(0, x[255])
def l344_(x):
    # x is a list (or vector) of length 256
    return [
        l344_0(x),
        l344_1(x),
        l344_2(x),
        l344_3(x),
        l344_4(x),
        l344_5(x),
        l344_6(x),
        l344_7(x),
        l344_8(x),
        l344_9(x),
        l344_10(x),
        l344_11(x),
        l344_12(x),
        l344_13(x),
        l344_14(x),
        l344_15(x),
        l344_16(x),
        l344_17(x),
        l344_18(x),
        l344_19(x),
        l344_20(x),
        l344_21(x),
        l344_22(x),
        l344_23(x),
        l344_24(x),
        l344_25(x),
        l344_26(x),
        l344_27(x),
        l344_28(x),
        l344_29(x),
        l344_30(x),
        l344_31(x),
        l344_32(x),
        l344_33(x),
        l344_34(x),
        l344_35(x),
        l344_36(x),
        l344_37(x),
        l344_38(x),
        l344_39(x),
        l344_40(x),
        l344_41(x),
        l344_42(x),
        l344_43(x),
        l344_44(x),
        l344_45(x),
        l344_46(x),
        l344_47(x),
        l344_48(x),
        l344_49(x),
        l344_50(x),
        l344_51(x),
        l344_52(x),
        l344_53(x),
        l344_54(x),
        l344_55(x),
        l344_56(x),
        l344_57(x),
        l344_58(x),
        l344_59(x),
        l344_60(x),
        l344_61(x),
        l344_62(x),
        l344_63(x),
        l344_64(x),
        l344_65(x),
        l344_66(x),
        l344_67(x),
        l344_68(x),
        l344_69(x),
        l344_70(x),
        l344_71(x),
        l344_72(x),
        l344_73(x),
        l344_74(x),
        l344_75(x),
        l344_76(x),
        l344_77(x),
        l344_78(x),
        l344_79(x),
        l344_80(x),
        l344_81(x),
        l344_82(x),
        l344_83(x),
        l344_84(x),
        l344_85(x),
        l344_86(x),
        l344_87(x),
        l344_88(x),
        l344_89(x),
        l344_90(x),
        l344_91(x),
        l344_92(x),
        l344_93(x),
        l344_94(x),
        l344_95(x),
        l344_96(x),
        l344_97(x),
        l344_98(x),
        l344_99(x),
        l344_100(x),
        l344_101(x),
        l344_102(x),
        l344_103(x),
        l344_104(x),
        l344_105(x),
        l344_106(x),
        l344_107(x),
        l344_108(x),
        l344_109(x),
        l344_110(x),
        l344_111(x),
        l344_112(x),
        l344_113(x),
        l344_114(x),
        l344_115(x),
        l344_116(x),
        l344_117(x),
        l344_118(x),
        l344_119(x),
        l344_120(x),
        l344_121(x),
        l344_122(x),
        l344_123(x),
        l344_124(x),
        l344_125(x),
        l344_126(x),
        l344_127(x),
        l344_128(x),
        l344_129(x),
        l344_130(x),
        l344_131(x),
        l344_132(x),
        l344_133(x),
        l344_134(x),
        l344_135(x),
        l344_136(x),
        l344_137(x),
        l344_138(x),
        l344_139(x),
        l344_140(x),
        l344_141(x),
        l344_142(x),
        l344_143(x),
        l344_144(x),
        l344_145(x),
        l344_146(x),
        l344_147(x),
        l344_148(x),
        l344_149(x),
        l344_150(x),
        l344_151(x),
        l344_152(x),
        l344_153(x),
        l344_154(x),
        l344_155(x),
        l344_156(x),
        l344_157(x),
        l344_158(x),
        l344_159(x),
        l344_160(x),
        l344_161(x),
        l344_162(x),
        l344_163(x),
        l344_164(x),
        l344_165(x),
        l344_166(x),
        l344_167(x),
        l344_168(x),
        l344_169(x),
        l344_170(x),
        l344_171(x),
        l344_172(x),
        l344_173(x),
        l344_174(x),
        l344_175(x),
        l344_176(x),
        l344_177(x),
        l344_178(x),
        l344_179(x),
        l344_180(x),
        l344_181(x),
        l344_182(x),
        l344_183(x),
        l344_184(x),
        l344_185(x),
        l344_186(x),
        l344_187(x),
        l344_188(x),
        l344_189(x),
        l344_190(x),
        l344_191(x),
        l344_192(x),
        l344_193(x),
        l344_194(x),
        l344_195(x),
        l344_196(x),
        l344_197(x),
        l344_198(x),
        l344_199(x),
        l344_200(x),
        l344_201(x),
        l344_202(x),
        l344_203(x),
        l344_204(x),
        l344_205(x),
        l344_206(x),
        l344_207(x),
        l344_208(x),
        l344_209(x),
        l344_210(x),
        l344_211(x),
        l344_212(x),
        l344_213(x),
        l344_214(x),
        l344_215(x),
        l344_216(x),
        l344_217(x),
        l344_218(x),
        l344_219(x),
        l344_220(x),
        l344_221(x),
        l344_222(x),
        l344_223(x),
        l344_224(x),
        l344_225(x),
        l344_226(x),
        l344_227(x),
        l344_228(x),
        l344_229(x),
        l344_230(x),
        l344_231(x),
        l344_232(x),
        l344_233(x),
        l344_234(x),
        l344_235(x),
        l344_236(x),
        l344_237(x),
        l344_238(x),
        l344_239(x),
        l344_240(x),
        l344_241(x),
        l344_242(x),
        l344_243(x),
        l344_244(x),
        l344_245(x),
        l344_246(x),
        l344_247(x),
        l344_248(x),
        l344_249(x),
        l344_250(x),
        l344_251(x),
        l344_252(x),
        l344_253(x),
        l344_254(x),
        l344_255(x),
        l344_256(x),
        l344_257(x),
        l344_258(x),
        l344_259(x),
        l344_260(x),
        l344_261(x),
        l344_262(x),
        l344_263(x),
        l344_264(x),
        l344_265(x),
        l344_266(x),
        l344_267(x),
        l344_268(x),
        l344_269(x),
        l344_270(x),
        l344_271(x),
        l344_272(x),
        l344_273(x),
        l344_274(x),
        l344_275(x),
        l344_276(x),
        l344_277(x),
        l344_278(x),
        l344_279(x),
        l344_280(x),
        l344_281(x),
        l344_282(x),
        l344_283(x),
        l344_284(x),
        l344_285(x),
        l344_286(x),
        l344_287(x),
    ]