import numpy as np




# Generated from reverse engineering
def l460_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 332
    out = np.empty(332, dtype=np.float32)
    
    # for i in range(0, 96):
    for i in range(0, 96):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(96, 128):
    for i in range(0, 32):
        s = x[96 + i] + x[128 + i]
        s += biases[i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 160):
    for i in range(0, 32):
        s = x[96 + i] + x[128 + i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(160, 192):
    for i in range(0, 32):
        s = x[96 + i] + x[128 + i]
        s += biases[i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(192, 224):
    for i in range(0, 32):
        s = x[160 + i]
        out[192 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(224, 256):
    for i in range(0, 32):
        s = x[192 + i] + -2.0 * x[i + 224]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(256, 260):
    for i in range(0, 4):
        s = x[256 + i]
        out[256 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xf (len=4)
    biases = [1.0, 1.0, 1.0, 1.0]
    # for i in range(260, 264):
    for i in range(0, 4):
        s = -1 * x[260 + i]
        s += biases[i]
        out[260 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(264, 268):
    for i in range(0, 4):
        s = x[264 + i] + -64.0 * x[i + 268] + 64.0 * x[i + 272]
        out[264 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(268, 332):
    for i in range(0, 64):
        s = x[276 + i]
        out[268 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l460_0(x):
    # x is a list (or vector) of length 340
    return max(0, x[0])
def l460_1(x):
    # x is a list (or vector) of length 340
    return max(0, x[1])
def l460_2(x):
    # x is a list (or vector) of length 340
    return max(0, x[2])
def l460_3(x):
    # x is a list (or vector) of length 340
    return max(0, x[3])
def l460_4(x):
    # x is a list (or vector) of length 340
    return max(0, x[4])
def l460_5(x):
    # x is a list (or vector) of length 340
    return max(0, x[5])
def l460_6(x):
    # x is a list (or vector) of length 340
    return max(0, x[6])
def l460_7(x):
    # x is a list (or vector) of length 340
    return max(0, x[7])
def l460_8(x):
    # x is a list (or vector) of length 340
    return max(0, x[8])
def l460_9(x):
    # x is a list (or vector) of length 340
    return max(0, x[9])
def l460_10(x):
    # x is a list (or vector) of length 340
    return max(0, x[10])
def l460_11(x):
    # x is a list (or vector) of length 340
    return max(0, x[11])
def l460_12(x):
    # x is a list (or vector) of length 340
    return max(0, x[12])
def l460_13(x):
    # x is a list (or vector) of length 340
    return max(0, x[13])
def l460_14(x):
    # x is a list (or vector) of length 340
    return max(0, x[14])
def l460_15(x):
    # x is a list (or vector) of length 340
    return max(0, x[15])
def l460_16(x):
    # x is a list (or vector) of length 340
    return max(0, x[16])
def l460_17(x):
    # x is a list (or vector) of length 340
    return max(0, x[17])
def l460_18(x):
    # x is a list (or vector) of length 340
    return max(0, x[18])
def l460_19(x):
    # x is a list (or vector) of length 340
    return max(0, x[19])
def l460_20(x):
    # x is a list (or vector) of length 340
    return max(0, x[20])
def l460_21(x):
    # x is a list (or vector) of length 340
    return max(0, x[21])
def l460_22(x):
    # x is a list (or vector) of length 340
    return max(0, x[22])
def l460_23(x):
    # x is a list (or vector) of length 340
    return max(0, x[23])
def l460_24(x):
    # x is a list (or vector) of length 340
    return max(0, x[24])
def l460_25(x):
    # x is a list (or vector) of length 340
    return max(0, x[25])
def l460_26(x):
    # x is a list (or vector) of length 340
    return max(0, x[26])
def l460_27(x):
    # x is a list (or vector) of length 340
    return max(0, x[27])
def l460_28(x):
    # x is a list (or vector) of length 340
    return max(0, x[28])
def l460_29(x):
    # x is a list (or vector) of length 340
    return max(0, x[29])
def l460_30(x):
    # x is a list (or vector) of length 340
    return max(0, x[30])
def l460_31(x):
    # x is a list (or vector) of length 340
    return max(0, x[31])
def l460_32(x):
    # x is a list (or vector) of length 340
    return max(0, x[32])
def l460_33(x):
    # x is a list (or vector) of length 340
    return max(0, x[33])
def l460_34(x):
    # x is a list (or vector) of length 340
    return max(0, x[34])
def l460_35(x):
    # x is a list (or vector) of length 340
    return max(0, x[35])
def l460_36(x):
    # x is a list (or vector) of length 340
    return max(0, x[36])
def l460_37(x):
    # x is a list (or vector) of length 340
    return max(0, x[37])
def l460_38(x):
    # x is a list (or vector) of length 340
    return max(0, x[38])
def l460_39(x):
    # x is a list (or vector) of length 340
    return max(0, x[39])
def l460_40(x):
    # x is a list (or vector) of length 340
    return max(0, x[40])
def l460_41(x):
    # x is a list (or vector) of length 340
    return max(0, x[41])
def l460_42(x):
    # x is a list (or vector) of length 340
    return max(0, x[42])
def l460_43(x):
    # x is a list (or vector) of length 340
    return max(0, x[43])
def l460_44(x):
    # x is a list (or vector) of length 340
    return max(0, x[44])
def l460_45(x):
    # x is a list (or vector) of length 340
    return max(0, x[45])
def l460_46(x):
    # x is a list (or vector) of length 340
    return max(0, x[46])
def l460_47(x):
    # x is a list (or vector) of length 340
    return max(0, x[47])
def l460_48(x):
    # x is a list (or vector) of length 340
    return max(0, x[48])
def l460_49(x):
    # x is a list (or vector) of length 340
    return max(0, x[49])
def l460_50(x):
    # x is a list (or vector) of length 340
    return max(0, x[50])
def l460_51(x):
    # x is a list (or vector) of length 340
    return max(0, x[51])
def l460_52(x):
    # x is a list (or vector) of length 340
    return max(0, x[52])
def l460_53(x):
    # x is a list (or vector) of length 340
    return max(0, x[53])
def l460_54(x):
    # x is a list (or vector) of length 340
    return max(0, x[54])
def l460_55(x):
    # x is a list (or vector) of length 340
    return max(0, x[55])
def l460_56(x):
    # x is a list (or vector) of length 340
    return max(0, x[56])
def l460_57(x):
    # x is a list (or vector) of length 340
    return max(0, x[57])
def l460_58(x):
    # x is a list (or vector) of length 340
    return max(0, x[58])
def l460_59(x):
    # x is a list (or vector) of length 340
    return max(0, x[59])
def l460_60(x):
    # x is a list (or vector) of length 340
    return max(0, x[60])
def l460_61(x):
    # x is a list (or vector) of length 340
    return max(0, x[61])
def l460_62(x):
    # x is a list (or vector) of length 340
    return max(0, x[62])
def l460_63(x):
    # x is a list (or vector) of length 340
    return max(0, x[63])
def l460_64(x):
    # x is a list (or vector) of length 340
    return max(0, x[64])
def l460_65(x):
    # x is a list (or vector) of length 340
    return max(0, x[65])
def l460_66(x):
    # x is a list (or vector) of length 340
    return max(0, x[66])
def l460_67(x):
    # x is a list (or vector) of length 340
    return max(0, x[67])
def l460_68(x):
    # x is a list (or vector) of length 340
    return max(0, x[68])
def l460_69(x):
    # x is a list (or vector) of length 340
    return max(0, x[69])
def l460_70(x):
    # x is a list (or vector) of length 340
    return max(0, x[70])
def l460_71(x):
    # x is a list (or vector) of length 340
    return max(0, x[71])
def l460_72(x):
    # x is a list (or vector) of length 340
    return max(0, x[72])
def l460_73(x):
    # x is a list (or vector) of length 340
    return max(0, x[73])
def l460_74(x):
    # x is a list (or vector) of length 340
    return max(0, x[74])
def l460_75(x):
    # x is a list (or vector) of length 340
    return max(0, x[75])
def l460_76(x):
    # x is a list (or vector) of length 340
    return max(0, x[76])
def l460_77(x):
    # x is a list (or vector) of length 340
    return max(0, x[77])
def l460_78(x):
    # x is a list (or vector) of length 340
    return max(0, x[78])
def l460_79(x):
    # x is a list (or vector) of length 340
    return max(0, x[79])
def l460_80(x):
    # x is a list (or vector) of length 340
    return max(0, x[80])
def l460_81(x):
    # x is a list (or vector) of length 340
    return max(0, x[81])
def l460_82(x):
    # x is a list (or vector) of length 340
    return max(0, x[82])
def l460_83(x):
    # x is a list (or vector) of length 340
    return max(0, x[83])
def l460_84(x):
    # x is a list (or vector) of length 340
    return max(0, x[84])
def l460_85(x):
    # x is a list (or vector) of length 340
    return max(0, x[85])
def l460_86(x):
    # x is a list (or vector) of length 340
    return max(0, x[86])
def l460_87(x):
    # x is a list (or vector) of length 340
    return max(0, x[87])
def l460_88(x):
    # x is a list (or vector) of length 340
    return max(0, x[88])
def l460_89(x):
    # x is a list (or vector) of length 340
    return max(0, x[89])
def l460_90(x):
    # x is a list (or vector) of length 340
    return max(0, x[90])
def l460_91(x):
    # x is a list (or vector) of length 340
    return max(0, x[91])
def l460_92(x):
    # x is a list (or vector) of length 340
    return max(0, x[92])
def l460_93(x):
    # x is a list (or vector) of length 340
    return max(0, x[93])
def l460_94(x):
    # x is a list (or vector) of length 340
    return max(0, x[94])
def l460_95(x):
    # x is a list (or vector) of length 340
    return max(0, x[95])
def l460_96(x):
    # x is a list (or vector) of length 340
    return max(0, x[96] + x[128] + -1.0)
def l460_97(x):
    # x is a list (or vector) of length 340
    return max(0, x[97] + x[129] + -1.0)
def l460_98(x):
    # x is a list (or vector) of length 340
    return max(0, x[98] + x[130] + -1.0)
def l460_99(x):
    # x is a list (or vector) of length 340
    return max(0, x[99] + x[131] + -1.0)
def l460_100(x):
    # x is a list (or vector) of length 340
    return max(0, x[100] + x[132] + -1.0)
def l460_101(x):
    # x is a list (or vector) of length 340
    return max(0, x[101] + x[133] + -1.0)
def l460_102(x):
    # x is a list (or vector) of length 340
    return max(0, x[102] + x[134] + -1.0)
def l460_103(x):
    # x is a list (or vector) of length 340
    return max(0, x[103] + x[135] + -1.0)
def l460_104(x):
    # x is a list (or vector) of length 340
    return max(0, x[104] + x[136] + -1.0)
def l460_105(x):
    # x is a list (or vector) of length 340
    return max(0, x[105] + x[137] + -1.0)
def l460_106(x):
    # x is a list (or vector) of length 340
    return max(0, x[106] + x[138] + -1.0)
def l460_107(x):
    # x is a list (or vector) of length 340
    return max(0, x[107] + x[139] + -1.0)
def l460_108(x):
    # x is a list (or vector) of length 340
    return max(0, x[108] + x[140] + -1.0)
def l460_109(x):
    # x is a list (or vector) of length 340
    return max(0, x[109] + x[141] + -1.0)
def l460_110(x):
    # x is a list (or vector) of length 340
    return max(0, x[110] + x[142] + -1.0)
def l460_111(x):
    # x is a list (or vector) of length 340
    return max(0, x[111] + x[143] + -1.0)
def l460_112(x):
    # x is a list (or vector) of length 340
    return max(0, x[112] + x[144] + -1.0)
def l460_113(x):
    # x is a list (or vector) of length 340
    return max(0, x[113] + x[145] + -1.0)
def l460_114(x):
    # x is a list (or vector) of length 340
    return max(0, x[114] + x[146] + -1.0)
def l460_115(x):
    # x is a list (or vector) of length 340
    return max(0, x[115] + x[147] + -1.0)
def l460_116(x):
    # x is a list (or vector) of length 340
    return max(0, x[116] + x[148] + -1.0)
def l460_117(x):
    # x is a list (or vector) of length 340
    return max(0, x[117] + x[149] + -1.0)
def l460_118(x):
    # x is a list (or vector) of length 340
    return max(0, x[118] + x[150] + -1.0)
def l460_119(x):
    # x is a list (or vector) of length 340
    return max(0, x[119] + x[151] + -1.0)
def l460_120(x):
    # x is a list (or vector) of length 340
    return max(0, x[120] + x[152] + -1.0)
def l460_121(x):
    # x is a list (or vector) of length 340
    return max(0, x[121] + x[153] + -1.0)
def l460_122(x):
    # x is a list (or vector) of length 340
    return max(0, x[122] + x[154] + -1.0)
def l460_123(x):
    # x is a list (or vector) of length 340
    return max(0, x[123] + x[155] + -1.0)
def l460_124(x):
    # x is a list (or vector) of length 340
    return max(0, x[124] + x[156] + -1.0)
def l460_125(x):
    # x is a list (or vector) of length 340
    return max(0, x[125] + x[157] + -1.0)
def l460_126(x):
    # x is a list (or vector) of length 340
    return max(0, x[126] + x[158] + -1.0)
def l460_127(x):
    # x is a list (or vector) of length 340
    return max(0, x[127] + x[159] + -1.0)
def l460_128(x):
    # x is a list (or vector) of length 340
    return max(0, x[96] + x[128])
def l460_129(x):
    # x is a list (or vector) of length 340
    return max(0, x[97] + x[129])
def l460_130(x):
    # x is a list (or vector) of length 340
    return max(0, x[98] + x[130])
def l460_131(x):
    # x is a list (or vector) of length 340
    return max(0, x[99] + x[131])
def l460_132(x):
    # x is a list (or vector) of length 340
    return max(0, x[100] + x[132])
def l460_133(x):
    # x is a list (or vector) of length 340
    return max(0, x[101] + x[133])
def l460_134(x):
    # x is a list (or vector) of length 340
    return max(0, x[102] + x[134])
def l460_135(x):
    # x is a list (or vector) of length 340
    return max(0, x[103] + x[135])
def l460_136(x):
    # x is a list (or vector) of length 340
    return max(0, x[104] + x[136])
def l460_137(x):
    # x is a list (or vector) of length 340
    return max(0, x[105] + x[137])
def l460_138(x):
    # x is a list (or vector) of length 340
    return max(0, x[106] + x[138])
def l460_139(x):
    # x is a list (or vector) of length 340
    return max(0, x[107] + x[139])
def l460_140(x):
    # x is a list (or vector) of length 340
    return max(0, x[108] + x[140])
def l460_141(x):
    # x is a list (or vector) of length 340
    return max(0, x[109] + x[141])
def l460_142(x):
    # x is a list (or vector) of length 340
    return max(0, x[110] + x[142])
def l460_143(x):
    # x is a list (or vector) of length 340
    return max(0, x[111] + x[143])
def l460_144(x):
    # x is a list (or vector) of length 340
    return max(0, x[112] + x[144])
def l460_145(x):
    # x is a list (or vector) of length 340
    return max(0, x[113] + x[145])
def l460_146(x):
    # x is a list (or vector) of length 340
    return max(0, x[114] + x[146])
def l460_147(x):
    # x is a list (or vector) of length 340
    return max(0, x[115] + x[147])
def l460_148(x):
    # x is a list (or vector) of length 340
    return max(0, x[116] + x[148])
def l460_149(x):
    # x is a list (or vector) of length 340
    return max(0, x[117] + x[149])
def l460_150(x):
    # x is a list (or vector) of length 340
    return max(0, x[118] + x[150])
def l460_151(x):
    # x is a list (or vector) of length 340
    return max(0, x[119] + x[151])
def l460_152(x):
    # x is a list (or vector) of length 340
    return max(0, x[120] + x[152])
def l460_153(x):
    # x is a list (or vector) of length 340
    return max(0, x[121] + x[153])
def l460_154(x):
    # x is a list (or vector) of length 340
    return max(0, x[122] + x[154])
def l460_155(x):
    # x is a list (or vector) of length 340
    return max(0, x[123] + x[155])
def l460_156(x):
    # x is a list (or vector) of length 340
    return max(0, x[124] + x[156])
def l460_157(x):
    # x is a list (or vector) of length 340
    return max(0, x[125] + x[157])
def l460_158(x):
    # x is a list (or vector) of length 340
    return max(0, x[126] + x[158])
def l460_159(x):
    # x is a list (or vector) of length 340
    return max(0, x[127] + x[159])
def l460_160(x):
    # x is a list (or vector) of length 340
    return max(0, x[96] + x[128] + -1.0)
def l460_161(x):
    # x is a list (or vector) of length 340
    return max(0, x[97] + x[129] + -1.0)
def l460_162(x):
    # x is a list (or vector) of length 340
    return max(0, x[98] + x[130] + -1.0)
def l460_163(x):
    # x is a list (or vector) of length 340
    return max(0, x[99] + x[131] + -1.0)
def l460_164(x):
    # x is a list (or vector) of length 340
    return max(0, x[100] + x[132] + -1.0)
def l460_165(x):
    # x is a list (or vector) of length 340
    return max(0, x[101] + x[133] + -1.0)
def l460_166(x):
    # x is a list (or vector) of length 340
    return max(0, x[102] + x[134] + -1.0)
def l460_167(x):
    # x is a list (or vector) of length 340
    return max(0, x[103] + x[135] + -1.0)
def l460_168(x):
    # x is a list (or vector) of length 340
    return max(0, x[104] + x[136] + -1.0)
def l460_169(x):
    # x is a list (or vector) of length 340
    return max(0, x[105] + x[137] + -1.0)
def l460_170(x):
    # x is a list (or vector) of length 340
    return max(0, x[106] + x[138] + -1.0)
def l460_171(x):
    # x is a list (or vector) of length 340
    return max(0, x[107] + x[139] + -1.0)
def l460_172(x):
    # x is a list (or vector) of length 340
    return max(0, x[108] + x[140] + -1.0)
def l460_173(x):
    # x is a list (or vector) of length 340
    return max(0, x[109] + x[141] + -1.0)
def l460_174(x):
    # x is a list (or vector) of length 340
    return max(0, x[110] + x[142] + -1.0)
def l460_175(x):
    # x is a list (or vector) of length 340
    return max(0, x[111] + x[143] + -1.0)
def l460_176(x):
    # x is a list (or vector) of length 340
    return max(0, x[112] + x[144] + -1.0)
def l460_177(x):
    # x is a list (or vector) of length 340
    return max(0, x[113] + x[145] + -1.0)
def l460_178(x):
    # x is a list (or vector) of length 340
    return max(0, x[114] + x[146] + -1.0)
def l460_179(x):
    # x is a list (or vector) of length 340
    return max(0, x[115] + x[147] + -1.0)
def l460_180(x):
    # x is a list (or vector) of length 340
    return max(0, x[116] + x[148] + -1.0)
def l460_181(x):
    # x is a list (or vector) of length 340
    return max(0, x[117] + x[149] + -1.0)
def l460_182(x):
    # x is a list (or vector) of length 340
    return max(0, x[118] + x[150] + -1.0)
def l460_183(x):
    # x is a list (or vector) of length 340
    return max(0, x[119] + x[151] + -1.0)
def l460_184(x):
    # x is a list (or vector) of length 340
    return max(0, x[120] + x[152] + -1.0)
def l460_185(x):
    # x is a list (or vector) of length 340
    return max(0, x[121] + x[153] + -1.0)
def l460_186(x):
    # x is a list (or vector) of length 340
    return max(0, x[122] + x[154] + -1.0)
def l460_187(x):
    # x is a list (or vector) of length 340
    return max(0, x[123] + x[155] + -1.0)
def l460_188(x):
    # x is a list (or vector) of length 340
    return max(0, x[124] + x[156] + -1.0)
def l460_189(x):
    # x is a list (or vector) of length 340
    return max(0, x[125] + x[157] + -1.0)
def l460_190(x):
    # x is a list (or vector) of length 340
    return max(0, x[126] + x[158] + -1.0)
def l460_191(x):
    # x is a list (or vector) of length 340
    return max(0, x[127] + x[159] + -1.0)
def l460_192(x):
    # x is a list (or vector) of length 340
    return max(0, x[160])
def l460_193(x):
    # x is a list (or vector) of length 340
    return max(0, x[161])
def l460_194(x):
    # x is a list (or vector) of length 340
    return max(0, x[162])
def l460_195(x):
    # x is a list (or vector) of length 340
    return max(0, x[163])
def l460_196(x):
    # x is a list (or vector) of length 340
    return max(0, x[164])
def l460_197(x):
    # x is a list (or vector) of length 340
    return max(0, x[165])
def l460_198(x):
    # x is a list (or vector) of length 340
    return max(0, x[166])
def l460_199(x):
    # x is a list (or vector) of length 340
    return max(0, x[167])
def l460_200(x):
    # x is a list (or vector) of length 340
    return max(0, x[168])
def l460_201(x):
    # x is a list (or vector) of length 340
    return max(0, x[169])
def l460_202(x):
    # x is a list (or vector) of length 340
    return max(0, x[170])
def l460_203(x):
    # x is a list (or vector) of length 340
    return max(0, x[171])
def l460_204(x):
    # x is a list (or vector) of length 340
    return max(0, x[172])
def l460_205(x):
    # x is a list (or vector) of length 340
    return max(0, x[173])
def l460_206(x):
    # x is a list (or vector) of length 340
    return max(0, x[174])
def l460_207(x):
    # x is a list (or vector) of length 340
    return max(0, x[175])
def l460_208(x):
    # x is a list (or vector) of length 340
    return max(0, x[176])
def l460_209(x):
    # x is a list (or vector) of length 340
    return max(0, x[177])
def l460_210(x):
    # x is a list (or vector) of length 340
    return max(0, x[178])
def l460_211(x):
    # x is a list (or vector) of length 340
    return max(0, x[179])
def l460_212(x):
    # x is a list (or vector) of length 340
    return max(0, x[180])
def l460_213(x):
    # x is a list (or vector) of length 340
    return max(0, x[181])
def l460_214(x):
    # x is a list (or vector) of length 340
    return max(0, x[182])
def l460_215(x):
    # x is a list (or vector) of length 340
    return max(0, x[183])
def l460_216(x):
    # x is a list (or vector) of length 340
    return max(0, x[184])
def l460_217(x):
    # x is a list (or vector) of length 340
    return max(0, x[185])
def l460_218(x):
    # x is a list (or vector) of length 340
    return max(0, x[186])
def l460_219(x):
    # x is a list (or vector) of length 340
    return max(0, x[187])
def l460_220(x):
    # x is a list (or vector) of length 340
    return max(0, x[188])
def l460_221(x):
    # x is a list (or vector) of length 340
    return max(0, x[189])
def l460_222(x):
    # x is a list (or vector) of length 340
    return max(0, x[190])
def l460_223(x):
    # x is a list (or vector) of length 340
    return max(0, x[191])
def l460_224(x):
    # x is a list (or vector) of length 340
    return max(0, x[192] + -2.0*x[224])
def l460_225(x):
    # x is a list (or vector) of length 340
    return max(0, x[193] + -2.0*x[225])
def l460_226(x):
    # x is a list (or vector) of length 340
    return max(0, x[194] + -2.0*x[226])
def l460_227(x):
    # x is a list (or vector) of length 340
    return max(0, x[195] + -2.0*x[227])
def l460_228(x):
    # x is a list (or vector) of length 340
    return max(0, x[196] + -2.0*x[228])
def l460_229(x):
    # x is a list (or vector) of length 340
    return max(0, x[197] + -2.0*x[229])
def l460_230(x):
    # x is a list (or vector) of length 340
    return max(0, x[198] + -2.0*x[230])
def l460_231(x):
    # x is a list (or vector) of length 340
    return max(0, x[199] + -2.0*x[231])
def l460_232(x):
    # x is a list (or vector) of length 340
    return max(0, x[200] + -2.0*x[232])
def l460_233(x):
    # x is a list (or vector) of length 340
    return max(0, x[201] + -2.0*x[233])
def l460_234(x):
    # x is a list (or vector) of length 340
    return max(0, x[202] + -2.0*x[234])
def l460_235(x):
    # x is a list (or vector) of length 340
    return max(0, x[203] + -2.0*x[235])
def l460_236(x):
    # x is a list (or vector) of length 340
    return max(0, x[204] + -2.0*x[236])
def l460_237(x):
    # x is a list (or vector) of length 340
    return max(0, x[205] + -2.0*x[237])
def l460_238(x):
    # x is a list (or vector) of length 340
    return max(0, x[206] + -2.0*x[238])
def l460_239(x):
    # x is a list (or vector) of length 340
    return max(0, x[207] + -2.0*x[239])
def l460_240(x):
    # x is a list (or vector) of length 340
    return max(0, x[208] + -2.0*x[240])
def l460_241(x):
    # x is a list (or vector) of length 340
    return max(0, x[209] + -2.0*x[241])
def l460_242(x):
    # x is a list (or vector) of length 340
    return max(0, x[210] + -2.0*x[242])
def l460_243(x):
    # x is a list (or vector) of length 340
    return max(0, x[211] + -2.0*x[243])
def l460_244(x):
    # x is a list (or vector) of length 340
    return max(0, x[212] + -2.0*x[244])
def l460_245(x):
    # x is a list (or vector) of length 340
    return max(0, x[213] + -2.0*x[245])
def l460_246(x):
    # x is a list (or vector) of length 340
    return max(0, x[214] + -2.0*x[246])
def l460_247(x):
    # x is a list (or vector) of length 340
    return max(0, x[215] + -2.0*x[247])
def l460_248(x):
    # x is a list (or vector) of length 340
    return max(0, x[216] + -2.0*x[248])
def l460_249(x):
    # x is a list (or vector) of length 340
    return max(0, x[217] + -2.0*x[249])
def l460_250(x):
    # x is a list (or vector) of length 340
    return max(0, x[218] + -2.0*x[250])
def l460_251(x):
    # x is a list (or vector) of length 340
    return max(0, x[219] + -2.0*x[251])
def l460_252(x):
    # x is a list (or vector) of length 340
    return max(0, x[220] + -2.0*x[252])
def l460_253(x):
    # x is a list (or vector) of length 340
    return max(0, x[221] + -2.0*x[253])
def l460_254(x):
    # x is a list (or vector) of length 340
    return max(0, x[222] + -2.0*x[254])
def l460_255(x):
    # x is a list (or vector) of length 340
    return max(0, x[223] + -2.0*x[255])
def l460_256(x):
    # x is a list (or vector) of length 340
    return max(0, x[256])
def l460_257(x):
    # x is a list (or vector) of length 340
    return max(0, x[257])
def l460_258(x):
    # x is a list (or vector) of length 340
    return max(0, x[258])
def l460_259(x):
    # x is a list (or vector) of length 340
    return max(0, x[259])
def l460_260(x):
    # x is a list (or vector) of length 340
    return max(0, -1.0*x[260] + 1.0)
def l460_261(x):
    # x is a list (or vector) of length 340
    return max(0, -1.0*x[261] + 1.0)
def l460_262(x):
    # x is a list (or vector) of length 340
    return max(0, -1.0*x[262] + 1.0)
def l460_263(x):
    # x is a list (or vector) of length 340
    return max(0, -1.0*x[263] + 1.0)
def l460_264(x):
    # x is a list (or vector) of length 340
    return max(0, x[264] + -64.0*x[268] + 64.0*x[272])
def l460_265(x):
    # x is a list (or vector) of length 340
    return max(0, x[265] + -64.0*x[269] + 64.0*x[273])
def l460_266(x):
    # x is a list (or vector) of length 340
    return max(0, x[266] + -64.0*x[270] + 64.0*x[274])
def l460_267(x):
    # x is a list (or vector) of length 340
    return max(0, x[267] + -64.0*x[271] + 64.0*x[275])
def l460_268(x):
    # x is a list (or vector) of length 340
    return max(0, x[276])
def l460_269(x):
    # x is a list (or vector) of length 340
    return max(0, x[277])
def l460_270(x):
    # x is a list (or vector) of length 340
    return max(0, x[278])
def l460_271(x):
    # x is a list (or vector) of length 340
    return max(0, x[279])
def l460_272(x):
    # x is a list (or vector) of length 340
    return max(0, x[280])
def l460_273(x):
    # x is a list (or vector) of length 340
    return max(0, x[281])
def l460_274(x):
    # x is a list (or vector) of length 340
    return max(0, x[282])
def l460_275(x):
    # x is a list (or vector) of length 340
    return max(0, x[283])
def l460_276(x):
    # x is a list (or vector) of length 340
    return max(0, x[284])
def l460_277(x):
    # x is a list (or vector) of length 340
    return max(0, x[285])
def l460_278(x):
    # x is a list (or vector) of length 340
    return max(0, x[286])
def l460_279(x):
    # x is a list (or vector) of length 340
    return max(0, x[287])
def l460_280(x):
    # x is a list (or vector) of length 340
    return max(0, x[288])
def l460_281(x):
    # x is a list (or vector) of length 340
    return max(0, x[289])
def l460_282(x):
    # x is a list (or vector) of length 340
    return max(0, x[290])
def l460_283(x):
    # x is a list (or vector) of length 340
    return max(0, x[291])
def l460_284(x):
    # x is a list (or vector) of length 340
    return max(0, x[292])
def l460_285(x):
    # x is a list (or vector) of length 340
    return max(0, x[293])
def l460_286(x):
    # x is a list (or vector) of length 340
    return max(0, x[294])
def l460_287(x):
    # x is a list (or vector) of length 340
    return max(0, x[295])
def l460_288(x):
    # x is a list (or vector) of length 340
    return max(0, x[296])
def l460_289(x):
    # x is a list (or vector) of length 340
    return max(0, x[297])
def l460_290(x):
    # x is a list (or vector) of length 340
    return max(0, x[298])
def l460_291(x):
    # x is a list (or vector) of length 340
    return max(0, x[299])
def l460_292(x):
    # x is a list (or vector) of length 340
    return max(0, x[300])
def l460_293(x):
    # x is a list (or vector) of length 340
    return max(0, x[301])
def l460_294(x):
    # x is a list (or vector) of length 340
    return max(0, x[302])
def l460_295(x):
    # x is a list (or vector) of length 340
    return max(0, x[303])
def l460_296(x):
    # x is a list (or vector) of length 340
    return max(0, x[304])
def l460_297(x):
    # x is a list (or vector) of length 340
    return max(0, x[305])
def l460_298(x):
    # x is a list (or vector) of length 340
    return max(0, x[306])
def l460_299(x):
    # x is a list (or vector) of length 340
    return max(0, x[307])
def l460_300(x):
    # x is a list (or vector) of length 340
    return max(0, x[308])
def l460_301(x):
    # x is a list (or vector) of length 340
    return max(0, x[309])
def l460_302(x):
    # x is a list (or vector) of length 340
    return max(0, x[310])
def l460_303(x):
    # x is a list (or vector) of length 340
    return max(0, x[311])
def l460_304(x):
    # x is a list (or vector) of length 340
    return max(0, x[312])
def l460_305(x):
    # x is a list (or vector) of length 340
    return max(0, x[313])
def l460_306(x):
    # x is a list (or vector) of length 340
    return max(0, x[314])
def l460_307(x):
    # x is a list (or vector) of length 340
    return max(0, x[315])
def l460_308(x):
    # x is a list (or vector) of length 340
    return max(0, x[316])
def l460_309(x):
    # x is a list (or vector) of length 340
    return max(0, x[317])
def l460_310(x):
    # x is a list (or vector) of length 340
    return max(0, x[318])
def l460_311(x):
    # x is a list (or vector) of length 340
    return max(0, x[319])
def l460_312(x):
    # x is a list (or vector) of length 340
    return max(0, x[320])
def l460_313(x):
    # x is a list (or vector) of length 340
    return max(0, x[321])
def l460_314(x):
    # x is a list (or vector) of length 340
    return max(0, x[322])
def l460_315(x):
    # x is a list (or vector) of length 340
    return max(0, x[323])
def l460_316(x):
    # x is a list (or vector) of length 340
    return max(0, x[324])
def l460_317(x):
    # x is a list (or vector) of length 340
    return max(0, x[325])
def l460_318(x):
    # x is a list (or vector) of length 340
    return max(0, x[326])
def l460_319(x):
    # x is a list (or vector) of length 340
    return max(0, x[327])
def l460_320(x):
    # x is a list (or vector) of length 340
    return max(0, x[328])
def l460_321(x):
    # x is a list (or vector) of length 340
    return max(0, x[329])
def l460_322(x):
    # x is a list (or vector) of length 340
    return max(0, x[330])
def l460_323(x):
    # x is a list (or vector) of length 340
    return max(0, x[331])
def l460_324(x):
    # x is a list (or vector) of length 340
    return max(0, x[332])
def l460_325(x):
    # x is a list (or vector) of length 340
    return max(0, x[333])
def l460_326(x):
    # x is a list (or vector) of length 340
    return max(0, x[334])
def l460_327(x):
    # x is a list (or vector) of length 340
    return max(0, x[335])
def l460_328(x):
    # x is a list (or vector) of length 340
    return max(0, x[336])
def l460_329(x):
    # x is a list (or vector) of length 340
    return max(0, x[337])
def l460_330(x):
    # x is a list (or vector) of length 340
    return max(0, x[338])
def l460_331(x):
    # x is a list (or vector) of length 340
    return max(0, x[339])
def l460_(x):
    # x is a list (or vector) of length 340
    return [
        l460_0(x),
        l460_1(x),
        l460_2(x),
        l460_3(x),
        l460_4(x),
        l460_5(x),
        l460_6(x),
        l460_7(x),
        l460_8(x),
        l460_9(x),
        l460_10(x),
        l460_11(x),
        l460_12(x),
        l460_13(x),
        l460_14(x),
        l460_15(x),
        l460_16(x),
        l460_17(x),
        l460_18(x),
        l460_19(x),
        l460_20(x),
        l460_21(x),
        l460_22(x),
        l460_23(x),
        l460_24(x),
        l460_25(x),
        l460_26(x),
        l460_27(x),
        l460_28(x),
        l460_29(x),
        l460_30(x),
        l460_31(x),
        l460_32(x),
        l460_33(x),
        l460_34(x),
        l460_35(x),
        l460_36(x),
        l460_37(x),
        l460_38(x),
        l460_39(x),
        l460_40(x),
        l460_41(x),
        l460_42(x),
        l460_43(x),
        l460_44(x),
        l460_45(x),
        l460_46(x),
        l460_47(x),
        l460_48(x),
        l460_49(x),
        l460_50(x),
        l460_51(x),
        l460_52(x),
        l460_53(x),
        l460_54(x),
        l460_55(x),
        l460_56(x),
        l460_57(x),
        l460_58(x),
        l460_59(x),
        l460_60(x),
        l460_61(x),
        l460_62(x),
        l460_63(x),
        l460_64(x),
        l460_65(x),
        l460_66(x),
        l460_67(x),
        l460_68(x),
        l460_69(x),
        l460_70(x),
        l460_71(x),
        l460_72(x),
        l460_73(x),
        l460_74(x),
        l460_75(x),
        l460_76(x),
        l460_77(x),
        l460_78(x),
        l460_79(x),
        l460_80(x),
        l460_81(x),
        l460_82(x),
        l460_83(x),
        l460_84(x),
        l460_85(x),
        l460_86(x),
        l460_87(x),
        l460_88(x),
        l460_89(x),
        l460_90(x),
        l460_91(x),
        l460_92(x),
        l460_93(x),
        l460_94(x),
        l460_95(x),
        l460_96(x),
        l460_97(x),
        l460_98(x),
        l460_99(x),
        l460_100(x),
        l460_101(x),
        l460_102(x),
        l460_103(x),
        l460_104(x),
        l460_105(x),
        l460_106(x),
        l460_107(x),
        l460_108(x),
        l460_109(x),
        l460_110(x),
        l460_111(x),
        l460_112(x),
        l460_113(x),
        l460_114(x),
        l460_115(x),
        l460_116(x),
        l460_117(x),
        l460_118(x),
        l460_119(x),
        l460_120(x),
        l460_121(x),
        l460_122(x),
        l460_123(x),
        l460_124(x),
        l460_125(x),
        l460_126(x),
        l460_127(x),
        l460_128(x),
        l460_129(x),
        l460_130(x),
        l460_131(x),
        l460_132(x),
        l460_133(x),
        l460_134(x),
        l460_135(x),
        l460_136(x),
        l460_137(x),
        l460_138(x),
        l460_139(x),
        l460_140(x),
        l460_141(x),
        l460_142(x),
        l460_143(x),
        l460_144(x),
        l460_145(x),
        l460_146(x),
        l460_147(x),
        l460_148(x),
        l460_149(x),
        l460_150(x),
        l460_151(x),
        l460_152(x),
        l460_153(x),
        l460_154(x),
        l460_155(x),
        l460_156(x),
        l460_157(x),
        l460_158(x),
        l460_159(x),
        l460_160(x),
        l460_161(x),
        l460_162(x),
        l460_163(x),
        l460_164(x),
        l460_165(x),
        l460_166(x),
        l460_167(x),
        l460_168(x),
        l460_169(x),
        l460_170(x),
        l460_171(x),
        l460_172(x),
        l460_173(x),
        l460_174(x),
        l460_175(x),
        l460_176(x),
        l460_177(x),
        l460_178(x),
        l460_179(x),
        l460_180(x),
        l460_181(x),
        l460_182(x),
        l460_183(x),
        l460_184(x),
        l460_185(x),
        l460_186(x),
        l460_187(x),
        l460_188(x),
        l460_189(x),
        l460_190(x),
        l460_191(x),
        l460_192(x),
        l460_193(x),
        l460_194(x),
        l460_195(x),
        l460_196(x),
        l460_197(x),
        l460_198(x),
        l460_199(x),
        l460_200(x),
        l460_201(x),
        l460_202(x),
        l460_203(x),
        l460_204(x),
        l460_205(x),
        l460_206(x),
        l460_207(x),
        l460_208(x),
        l460_209(x),
        l460_210(x),
        l460_211(x),
        l460_212(x),
        l460_213(x),
        l460_214(x),
        l460_215(x),
        l460_216(x),
        l460_217(x),
        l460_218(x),
        l460_219(x),
        l460_220(x),
        l460_221(x),
        l460_222(x),
        l460_223(x),
        l460_224(x),
        l460_225(x),
        l460_226(x),
        l460_227(x),
        l460_228(x),
        l460_229(x),
        l460_230(x),
        l460_231(x),
        l460_232(x),
        l460_233(x),
        l460_234(x),
        l460_235(x),
        l460_236(x),
        l460_237(x),
        l460_238(x),
        l460_239(x),
        l460_240(x),
        l460_241(x),
        l460_242(x),
        l460_243(x),
        l460_244(x),
        l460_245(x),
        l460_246(x),
        l460_247(x),
        l460_248(x),
        l460_249(x),
        l460_250(x),
        l460_251(x),
        l460_252(x),
        l460_253(x),
        l460_254(x),
        l460_255(x),
        l460_256(x),
        l460_257(x),
        l460_258(x),
        l460_259(x),
        l460_260(x),
        l460_261(x),
        l460_262(x),
        l460_263(x),
        l460_264(x),
        l460_265(x),
        l460_266(x),
        l460_267(x),
        l460_268(x),
        l460_269(x),
        l460_270(x),
        l460_271(x),
        l460_272(x),
        l460_273(x),
        l460_274(x),
        l460_275(x),
        l460_276(x),
        l460_277(x),
        l460_278(x),
        l460_279(x),
        l460_280(x),
        l460_281(x),
        l460_282(x),
        l460_283(x),
        l460_284(x),
        l460_285(x),
        l460_286(x),
        l460_287(x),
        l460_288(x),
        l460_289(x),
        l460_290(x),
        l460_291(x),
        l460_292(x),
        l460_293(x),
        l460_294(x),
        l460_295(x),
        l460_296(x),
        l460_297(x),
        l460_298(x),
        l460_299(x),
        l460_300(x),
        l460_301(x),
        l460_302(x),
        l460_303(x),
        l460_304(x),
        l460_305(x),
        l460_306(x),
        l460_307(x),
        l460_308(x),
        l460_309(x),
        l460_310(x),
        l460_311(x),
        l460_312(x),
        l460_313(x),
        l460_314(x),
        l460_315(x),
        l460_316(x),
        l460_317(x),
        l460_318(x),
        l460_319(x),
        l460_320(x),
        l460_321(x),
        l460_322(x),
        l460_323(x),
        l460_324(x),
        l460_325(x),
        l460_326(x),
        l460_327(x),
        l460_328(x),
        l460_329(x),
        l460_330(x),
        l460_331(x),
    ]