import numpy as np




# Generated from reverse engineering
def l376_g(x: np.ndarray) -> np.ndarray:
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




def l376_0(x):
    # x is a list (or vector) of length 340
    return max(0, x[0])
def l376_1(x):
    # x is a list (or vector) of length 340
    return max(0, x[1])
def l376_2(x):
    # x is a list (or vector) of length 340
    return max(0, x[2])
def l376_3(x):
    # x is a list (or vector) of length 340
    return max(0, x[3])
def l376_4(x):
    # x is a list (or vector) of length 340
    return max(0, x[4])
def l376_5(x):
    # x is a list (or vector) of length 340
    return max(0, x[5])
def l376_6(x):
    # x is a list (or vector) of length 340
    return max(0, x[6])
def l376_7(x):
    # x is a list (or vector) of length 340
    return max(0, x[7])
def l376_8(x):
    # x is a list (or vector) of length 340
    return max(0, x[8])
def l376_9(x):
    # x is a list (or vector) of length 340
    return max(0, x[9])
def l376_10(x):
    # x is a list (or vector) of length 340
    return max(0, x[10])
def l376_11(x):
    # x is a list (or vector) of length 340
    return max(0, x[11])
def l376_12(x):
    # x is a list (or vector) of length 340
    return max(0, x[12])
def l376_13(x):
    # x is a list (or vector) of length 340
    return max(0, x[13])
def l376_14(x):
    # x is a list (or vector) of length 340
    return max(0, x[14])
def l376_15(x):
    # x is a list (or vector) of length 340
    return max(0, x[15])
def l376_16(x):
    # x is a list (or vector) of length 340
    return max(0, x[16])
def l376_17(x):
    # x is a list (or vector) of length 340
    return max(0, x[17])
def l376_18(x):
    # x is a list (or vector) of length 340
    return max(0, x[18])
def l376_19(x):
    # x is a list (or vector) of length 340
    return max(0, x[19])
def l376_20(x):
    # x is a list (or vector) of length 340
    return max(0, x[20])
def l376_21(x):
    # x is a list (or vector) of length 340
    return max(0, x[21])
def l376_22(x):
    # x is a list (or vector) of length 340
    return max(0, x[22])
def l376_23(x):
    # x is a list (or vector) of length 340
    return max(0, x[23])
def l376_24(x):
    # x is a list (or vector) of length 340
    return max(0, x[24])
def l376_25(x):
    # x is a list (or vector) of length 340
    return max(0, x[25])
def l376_26(x):
    # x is a list (or vector) of length 340
    return max(0, x[26])
def l376_27(x):
    # x is a list (or vector) of length 340
    return max(0, x[27])
def l376_28(x):
    # x is a list (or vector) of length 340
    return max(0, x[28])
def l376_29(x):
    # x is a list (or vector) of length 340
    return max(0, x[29])
def l376_30(x):
    # x is a list (or vector) of length 340
    return max(0, x[30])
def l376_31(x):
    # x is a list (or vector) of length 340
    return max(0, x[31])
def l376_32(x):
    # x is a list (or vector) of length 340
    return max(0, x[32])
def l376_33(x):
    # x is a list (or vector) of length 340
    return max(0, x[33])
def l376_34(x):
    # x is a list (or vector) of length 340
    return max(0, x[34])
def l376_35(x):
    # x is a list (or vector) of length 340
    return max(0, x[35])
def l376_36(x):
    # x is a list (or vector) of length 340
    return max(0, x[36])
def l376_37(x):
    # x is a list (or vector) of length 340
    return max(0, x[37])
def l376_38(x):
    # x is a list (or vector) of length 340
    return max(0, x[38])
def l376_39(x):
    # x is a list (or vector) of length 340
    return max(0, x[39])
def l376_40(x):
    # x is a list (or vector) of length 340
    return max(0, x[40])
def l376_41(x):
    # x is a list (or vector) of length 340
    return max(0, x[41])
def l376_42(x):
    # x is a list (or vector) of length 340
    return max(0, x[42])
def l376_43(x):
    # x is a list (or vector) of length 340
    return max(0, x[43])
def l376_44(x):
    # x is a list (or vector) of length 340
    return max(0, x[44])
def l376_45(x):
    # x is a list (or vector) of length 340
    return max(0, x[45])
def l376_46(x):
    # x is a list (or vector) of length 340
    return max(0, x[46])
def l376_47(x):
    # x is a list (or vector) of length 340
    return max(0, x[47])
def l376_48(x):
    # x is a list (or vector) of length 340
    return max(0, x[48])
def l376_49(x):
    # x is a list (or vector) of length 340
    return max(0, x[49])
def l376_50(x):
    # x is a list (or vector) of length 340
    return max(0, x[50])
def l376_51(x):
    # x is a list (or vector) of length 340
    return max(0, x[51])
def l376_52(x):
    # x is a list (or vector) of length 340
    return max(0, x[52])
def l376_53(x):
    # x is a list (or vector) of length 340
    return max(0, x[53])
def l376_54(x):
    # x is a list (or vector) of length 340
    return max(0, x[54])
def l376_55(x):
    # x is a list (or vector) of length 340
    return max(0, x[55])
def l376_56(x):
    # x is a list (or vector) of length 340
    return max(0, x[56])
def l376_57(x):
    # x is a list (or vector) of length 340
    return max(0, x[57])
def l376_58(x):
    # x is a list (or vector) of length 340
    return max(0, x[58])
def l376_59(x):
    # x is a list (or vector) of length 340
    return max(0, x[59])
def l376_60(x):
    # x is a list (or vector) of length 340
    return max(0, x[60])
def l376_61(x):
    # x is a list (or vector) of length 340
    return max(0, x[61])
def l376_62(x):
    # x is a list (or vector) of length 340
    return max(0, x[62])
def l376_63(x):
    # x is a list (or vector) of length 340
    return max(0, x[63])
def l376_64(x):
    # x is a list (or vector) of length 340
    return max(0, x[64])
def l376_65(x):
    # x is a list (or vector) of length 340
    return max(0, x[65])
def l376_66(x):
    # x is a list (or vector) of length 340
    return max(0, x[66])
def l376_67(x):
    # x is a list (or vector) of length 340
    return max(0, x[67])
def l376_68(x):
    # x is a list (or vector) of length 340
    return max(0, x[68])
def l376_69(x):
    # x is a list (or vector) of length 340
    return max(0, x[69])
def l376_70(x):
    # x is a list (or vector) of length 340
    return max(0, x[70])
def l376_71(x):
    # x is a list (or vector) of length 340
    return max(0, x[71])
def l376_72(x):
    # x is a list (or vector) of length 340
    return max(0, x[72])
def l376_73(x):
    # x is a list (or vector) of length 340
    return max(0, x[73])
def l376_74(x):
    # x is a list (or vector) of length 340
    return max(0, x[74])
def l376_75(x):
    # x is a list (or vector) of length 340
    return max(0, x[75])
def l376_76(x):
    # x is a list (or vector) of length 340
    return max(0, x[76])
def l376_77(x):
    # x is a list (or vector) of length 340
    return max(0, x[77])
def l376_78(x):
    # x is a list (or vector) of length 340
    return max(0, x[78])
def l376_79(x):
    # x is a list (or vector) of length 340
    return max(0, x[79])
def l376_80(x):
    # x is a list (or vector) of length 340
    return max(0, x[80])
def l376_81(x):
    # x is a list (or vector) of length 340
    return max(0, x[81])
def l376_82(x):
    # x is a list (or vector) of length 340
    return max(0, x[82])
def l376_83(x):
    # x is a list (or vector) of length 340
    return max(0, x[83])
def l376_84(x):
    # x is a list (or vector) of length 340
    return max(0, x[84])
def l376_85(x):
    # x is a list (or vector) of length 340
    return max(0, x[85])
def l376_86(x):
    # x is a list (or vector) of length 340
    return max(0, x[86])
def l376_87(x):
    # x is a list (or vector) of length 340
    return max(0, x[87])
def l376_88(x):
    # x is a list (or vector) of length 340
    return max(0, x[88])
def l376_89(x):
    # x is a list (or vector) of length 340
    return max(0, x[89])
def l376_90(x):
    # x is a list (or vector) of length 340
    return max(0, x[90])
def l376_91(x):
    # x is a list (or vector) of length 340
    return max(0, x[91])
def l376_92(x):
    # x is a list (or vector) of length 340
    return max(0, x[92])
def l376_93(x):
    # x is a list (or vector) of length 340
    return max(0, x[93])
def l376_94(x):
    # x is a list (or vector) of length 340
    return max(0, x[94])
def l376_95(x):
    # x is a list (or vector) of length 340
    return max(0, x[95])
def l376_96(x):
    # x is a list (or vector) of length 340
    return max(0, x[96] + x[128] + -1.0)
def l376_97(x):
    # x is a list (or vector) of length 340
    return max(0, x[97] + x[129] + -1.0)
def l376_98(x):
    # x is a list (or vector) of length 340
    return max(0, x[98] + x[130] + -1.0)
def l376_99(x):
    # x is a list (or vector) of length 340
    return max(0, x[99] + x[131] + -1.0)
def l376_100(x):
    # x is a list (or vector) of length 340
    return max(0, x[100] + x[132] + -1.0)
def l376_101(x):
    # x is a list (or vector) of length 340
    return max(0, x[101] + x[133] + -1.0)
def l376_102(x):
    # x is a list (or vector) of length 340
    return max(0, x[102] + x[134] + -1.0)
def l376_103(x):
    # x is a list (or vector) of length 340
    return max(0, x[103] + x[135] + -1.0)
def l376_104(x):
    # x is a list (or vector) of length 340
    return max(0, x[104] + x[136] + -1.0)
def l376_105(x):
    # x is a list (or vector) of length 340
    return max(0, x[105] + x[137] + -1.0)
def l376_106(x):
    # x is a list (or vector) of length 340
    return max(0, x[106] + x[138] + -1.0)
def l376_107(x):
    # x is a list (or vector) of length 340
    return max(0, x[107] + x[139] + -1.0)
def l376_108(x):
    # x is a list (or vector) of length 340
    return max(0, x[108] + x[140] + -1.0)
def l376_109(x):
    # x is a list (or vector) of length 340
    return max(0, x[109] + x[141] + -1.0)
def l376_110(x):
    # x is a list (or vector) of length 340
    return max(0, x[110] + x[142] + -1.0)
def l376_111(x):
    # x is a list (or vector) of length 340
    return max(0, x[111] + x[143] + -1.0)
def l376_112(x):
    # x is a list (or vector) of length 340
    return max(0, x[112] + x[144] + -1.0)
def l376_113(x):
    # x is a list (or vector) of length 340
    return max(0, x[113] + x[145] + -1.0)
def l376_114(x):
    # x is a list (or vector) of length 340
    return max(0, x[114] + x[146] + -1.0)
def l376_115(x):
    # x is a list (or vector) of length 340
    return max(0, x[115] + x[147] + -1.0)
def l376_116(x):
    # x is a list (or vector) of length 340
    return max(0, x[116] + x[148] + -1.0)
def l376_117(x):
    # x is a list (or vector) of length 340
    return max(0, x[117] + x[149] + -1.0)
def l376_118(x):
    # x is a list (or vector) of length 340
    return max(0, x[118] + x[150] + -1.0)
def l376_119(x):
    # x is a list (or vector) of length 340
    return max(0, x[119] + x[151] + -1.0)
def l376_120(x):
    # x is a list (or vector) of length 340
    return max(0, x[120] + x[152] + -1.0)
def l376_121(x):
    # x is a list (or vector) of length 340
    return max(0, x[121] + x[153] + -1.0)
def l376_122(x):
    # x is a list (or vector) of length 340
    return max(0, x[122] + x[154] + -1.0)
def l376_123(x):
    # x is a list (or vector) of length 340
    return max(0, x[123] + x[155] + -1.0)
def l376_124(x):
    # x is a list (or vector) of length 340
    return max(0, x[124] + x[156] + -1.0)
def l376_125(x):
    # x is a list (or vector) of length 340
    return max(0, x[125] + x[157] + -1.0)
def l376_126(x):
    # x is a list (or vector) of length 340
    return max(0, x[126] + x[158] + -1.0)
def l376_127(x):
    # x is a list (or vector) of length 340
    return max(0, x[127] + x[159] + -1.0)
def l376_128(x):
    # x is a list (or vector) of length 340
    return max(0, x[96] + x[128])
def l376_129(x):
    # x is a list (or vector) of length 340
    return max(0, x[97] + x[129])
def l376_130(x):
    # x is a list (or vector) of length 340
    return max(0, x[98] + x[130])
def l376_131(x):
    # x is a list (or vector) of length 340
    return max(0, x[99] + x[131])
def l376_132(x):
    # x is a list (or vector) of length 340
    return max(0, x[100] + x[132])
def l376_133(x):
    # x is a list (or vector) of length 340
    return max(0, x[101] + x[133])
def l376_134(x):
    # x is a list (or vector) of length 340
    return max(0, x[102] + x[134])
def l376_135(x):
    # x is a list (or vector) of length 340
    return max(0, x[103] + x[135])
def l376_136(x):
    # x is a list (or vector) of length 340
    return max(0, x[104] + x[136])
def l376_137(x):
    # x is a list (or vector) of length 340
    return max(0, x[105] + x[137])
def l376_138(x):
    # x is a list (or vector) of length 340
    return max(0, x[106] + x[138])
def l376_139(x):
    # x is a list (or vector) of length 340
    return max(0, x[107] + x[139])
def l376_140(x):
    # x is a list (or vector) of length 340
    return max(0, x[108] + x[140])
def l376_141(x):
    # x is a list (or vector) of length 340
    return max(0, x[109] + x[141])
def l376_142(x):
    # x is a list (or vector) of length 340
    return max(0, x[110] + x[142])
def l376_143(x):
    # x is a list (or vector) of length 340
    return max(0, x[111] + x[143])
def l376_144(x):
    # x is a list (or vector) of length 340
    return max(0, x[112] + x[144])
def l376_145(x):
    # x is a list (or vector) of length 340
    return max(0, x[113] + x[145])
def l376_146(x):
    # x is a list (or vector) of length 340
    return max(0, x[114] + x[146])
def l376_147(x):
    # x is a list (or vector) of length 340
    return max(0, x[115] + x[147])
def l376_148(x):
    # x is a list (or vector) of length 340
    return max(0, x[116] + x[148])
def l376_149(x):
    # x is a list (or vector) of length 340
    return max(0, x[117] + x[149])
def l376_150(x):
    # x is a list (or vector) of length 340
    return max(0, x[118] + x[150])
def l376_151(x):
    # x is a list (or vector) of length 340
    return max(0, x[119] + x[151])
def l376_152(x):
    # x is a list (or vector) of length 340
    return max(0, x[120] + x[152])
def l376_153(x):
    # x is a list (or vector) of length 340
    return max(0, x[121] + x[153])
def l376_154(x):
    # x is a list (or vector) of length 340
    return max(0, x[122] + x[154])
def l376_155(x):
    # x is a list (or vector) of length 340
    return max(0, x[123] + x[155])
def l376_156(x):
    # x is a list (or vector) of length 340
    return max(0, x[124] + x[156])
def l376_157(x):
    # x is a list (or vector) of length 340
    return max(0, x[125] + x[157])
def l376_158(x):
    # x is a list (or vector) of length 340
    return max(0, x[126] + x[158])
def l376_159(x):
    # x is a list (or vector) of length 340
    return max(0, x[127] + x[159])
def l376_160(x):
    # x is a list (or vector) of length 340
    return max(0, x[96] + x[128] + -1.0)
def l376_161(x):
    # x is a list (or vector) of length 340
    return max(0, x[97] + x[129] + -1.0)
def l376_162(x):
    # x is a list (or vector) of length 340
    return max(0, x[98] + x[130] + -1.0)
def l376_163(x):
    # x is a list (or vector) of length 340
    return max(0, x[99] + x[131] + -1.0)
def l376_164(x):
    # x is a list (or vector) of length 340
    return max(0, x[100] + x[132] + -1.0)
def l376_165(x):
    # x is a list (or vector) of length 340
    return max(0, x[101] + x[133] + -1.0)
def l376_166(x):
    # x is a list (or vector) of length 340
    return max(0, x[102] + x[134] + -1.0)
def l376_167(x):
    # x is a list (or vector) of length 340
    return max(0, x[103] + x[135] + -1.0)
def l376_168(x):
    # x is a list (or vector) of length 340
    return max(0, x[104] + x[136] + -1.0)
def l376_169(x):
    # x is a list (or vector) of length 340
    return max(0, x[105] + x[137] + -1.0)
def l376_170(x):
    # x is a list (or vector) of length 340
    return max(0, x[106] + x[138] + -1.0)
def l376_171(x):
    # x is a list (or vector) of length 340
    return max(0, x[107] + x[139] + -1.0)
def l376_172(x):
    # x is a list (or vector) of length 340
    return max(0, x[108] + x[140] + -1.0)
def l376_173(x):
    # x is a list (or vector) of length 340
    return max(0, x[109] + x[141] + -1.0)
def l376_174(x):
    # x is a list (or vector) of length 340
    return max(0, x[110] + x[142] + -1.0)
def l376_175(x):
    # x is a list (or vector) of length 340
    return max(0, x[111] + x[143] + -1.0)
def l376_176(x):
    # x is a list (or vector) of length 340
    return max(0, x[112] + x[144] + -1.0)
def l376_177(x):
    # x is a list (or vector) of length 340
    return max(0, x[113] + x[145] + -1.0)
def l376_178(x):
    # x is a list (or vector) of length 340
    return max(0, x[114] + x[146] + -1.0)
def l376_179(x):
    # x is a list (or vector) of length 340
    return max(0, x[115] + x[147] + -1.0)
def l376_180(x):
    # x is a list (or vector) of length 340
    return max(0, x[116] + x[148] + -1.0)
def l376_181(x):
    # x is a list (or vector) of length 340
    return max(0, x[117] + x[149] + -1.0)
def l376_182(x):
    # x is a list (or vector) of length 340
    return max(0, x[118] + x[150] + -1.0)
def l376_183(x):
    # x is a list (or vector) of length 340
    return max(0, x[119] + x[151] + -1.0)
def l376_184(x):
    # x is a list (or vector) of length 340
    return max(0, x[120] + x[152] + -1.0)
def l376_185(x):
    # x is a list (or vector) of length 340
    return max(0, x[121] + x[153] + -1.0)
def l376_186(x):
    # x is a list (or vector) of length 340
    return max(0, x[122] + x[154] + -1.0)
def l376_187(x):
    # x is a list (or vector) of length 340
    return max(0, x[123] + x[155] + -1.0)
def l376_188(x):
    # x is a list (or vector) of length 340
    return max(0, x[124] + x[156] + -1.0)
def l376_189(x):
    # x is a list (or vector) of length 340
    return max(0, x[125] + x[157] + -1.0)
def l376_190(x):
    # x is a list (or vector) of length 340
    return max(0, x[126] + x[158] + -1.0)
def l376_191(x):
    # x is a list (or vector) of length 340
    return max(0, x[127] + x[159] + -1.0)
def l376_192(x):
    # x is a list (or vector) of length 340
    return max(0, x[160])
def l376_193(x):
    # x is a list (or vector) of length 340
    return max(0, x[161])
def l376_194(x):
    # x is a list (or vector) of length 340
    return max(0, x[162])
def l376_195(x):
    # x is a list (or vector) of length 340
    return max(0, x[163])
def l376_196(x):
    # x is a list (or vector) of length 340
    return max(0, x[164])
def l376_197(x):
    # x is a list (or vector) of length 340
    return max(0, x[165])
def l376_198(x):
    # x is a list (or vector) of length 340
    return max(0, x[166])
def l376_199(x):
    # x is a list (or vector) of length 340
    return max(0, x[167])
def l376_200(x):
    # x is a list (or vector) of length 340
    return max(0, x[168])
def l376_201(x):
    # x is a list (or vector) of length 340
    return max(0, x[169])
def l376_202(x):
    # x is a list (or vector) of length 340
    return max(0, x[170])
def l376_203(x):
    # x is a list (or vector) of length 340
    return max(0, x[171])
def l376_204(x):
    # x is a list (or vector) of length 340
    return max(0, x[172])
def l376_205(x):
    # x is a list (or vector) of length 340
    return max(0, x[173])
def l376_206(x):
    # x is a list (or vector) of length 340
    return max(0, x[174])
def l376_207(x):
    # x is a list (or vector) of length 340
    return max(0, x[175])
def l376_208(x):
    # x is a list (or vector) of length 340
    return max(0, x[176])
def l376_209(x):
    # x is a list (or vector) of length 340
    return max(0, x[177])
def l376_210(x):
    # x is a list (or vector) of length 340
    return max(0, x[178])
def l376_211(x):
    # x is a list (or vector) of length 340
    return max(0, x[179])
def l376_212(x):
    # x is a list (or vector) of length 340
    return max(0, x[180])
def l376_213(x):
    # x is a list (or vector) of length 340
    return max(0, x[181])
def l376_214(x):
    # x is a list (or vector) of length 340
    return max(0, x[182])
def l376_215(x):
    # x is a list (or vector) of length 340
    return max(0, x[183])
def l376_216(x):
    # x is a list (or vector) of length 340
    return max(0, x[184])
def l376_217(x):
    # x is a list (or vector) of length 340
    return max(0, x[185])
def l376_218(x):
    # x is a list (or vector) of length 340
    return max(0, x[186])
def l376_219(x):
    # x is a list (or vector) of length 340
    return max(0, x[187])
def l376_220(x):
    # x is a list (or vector) of length 340
    return max(0, x[188])
def l376_221(x):
    # x is a list (or vector) of length 340
    return max(0, x[189])
def l376_222(x):
    # x is a list (or vector) of length 340
    return max(0, x[190])
def l376_223(x):
    # x is a list (or vector) of length 340
    return max(0, x[191])
def l376_224(x):
    # x is a list (or vector) of length 340
    return max(0, x[192] + -2.0*x[224])
def l376_225(x):
    # x is a list (or vector) of length 340
    return max(0, x[193] + -2.0*x[225])
def l376_226(x):
    # x is a list (or vector) of length 340
    return max(0, x[194] + -2.0*x[226])
def l376_227(x):
    # x is a list (or vector) of length 340
    return max(0, x[195] + -2.0*x[227])
def l376_228(x):
    # x is a list (or vector) of length 340
    return max(0, x[196] + -2.0*x[228])
def l376_229(x):
    # x is a list (or vector) of length 340
    return max(0, x[197] + -2.0*x[229])
def l376_230(x):
    # x is a list (or vector) of length 340
    return max(0, x[198] + -2.0*x[230])
def l376_231(x):
    # x is a list (or vector) of length 340
    return max(0, x[199] + -2.0*x[231])
def l376_232(x):
    # x is a list (or vector) of length 340
    return max(0, x[200] + -2.0*x[232])
def l376_233(x):
    # x is a list (or vector) of length 340
    return max(0, x[201] + -2.0*x[233])
def l376_234(x):
    # x is a list (or vector) of length 340
    return max(0, x[202] + -2.0*x[234])
def l376_235(x):
    # x is a list (or vector) of length 340
    return max(0, x[203] + -2.0*x[235])
def l376_236(x):
    # x is a list (or vector) of length 340
    return max(0, x[204] + -2.0*x[236])
def l376_237(x):
    # x is a list (or vector) of length 340
    return max(0, x[205] + -2.0*x[237])
def l376_238(x):
    # x is a list (or vector) of length 340
    return max(0, x[206] + -2.0*x[238])
def l376_239(x):
    # x is a list (or vector) of length 340
    return max(0, x[207] + -2.0*x[239])
def l376_240(x):
    # x is a list (or vector) of length 340
    return max(0, x[208] + -2.0*x[240])
def l376_241(x):
    # x is a list (or vector) of length 340
    return max(0, x[209] + -2.0*x[241])
def l376_242(x):
    # x is a list (or vector) of length 340
    return max(0, x[210] + -2.0*x[242])
def l376_243(x):
    # x is a list (or vector) of length 340
    return max(0, x[211] + -2.0*x[243])
def l376_244(x):
    # x is a list (or vector) of length 340
    return max(0, x[212] + -2.0*x[244])
def l376_245(x):
    # x is a list (or vector) of length 340
    return max(0, x[213] + -2.0*x[245])
def l376_246(x):
    # x is a list (or vector) of length 340
    return max(0, x[214] + -2.0*x[246])
def l376_247(x):
    # x is a list (or vector) of length 340
    return max(0, x[215] + -2.0*x[247])
def l376_248(x):
    # x is a list (or vector) of length 340
    return max(0, x[216] + -2.0*x[248])
def l376_249(x):
    # x is a list (or vector) of length 340
    return max(0, x[217] + -2.0*x[249])
def l376_250(x):
    # x is a list (or vector) of length 340
    return max(0, x[218] + -2.0*x[250])
def l376_251(x):
    # x is a list (or vector) of length 340
    return max(0, x[219] + -2.0*x[251])
def l376_252(x):
    # x is a list (or vector) of length 340
    return max(0, x[220] + -2.0*x[252])
def l376_253(x):
    # x is a list (or vector) of length 340
    return max(0, x[221] + -2.0*x[253])
def l376_254(x):
    # x is a list (or vector) of length 340
    return max(0, x[222] + -2.0*x[254])
def l376_255(x):
    # x is a list (or vector) of length 340
    return max(0, x[223] + -2.0*x[255])
def l376_256(x):
    # x is a list (or vector) of length 340
    return max(0, x[256])
def l376_257(x):
    # x is a list (or vector) of length 340
    return max(0, x[257])
def l376_258(x):
    # x is a list (or vector) of length 340
    return max(0, x[258])
def l376_259(x):
    # x is a list (or vector) of length 340
    return max(0, x[259])
def l376_260(x):
    # x is a list (or vector) of length 340
    return max(0, -1.0*x[260] + 1.0)
def l376_261(x):
    # x is a list (or vector) of length 340
    return max(0, -1.0*x[261] + 1.0)
def l376_262(x):
    # x is a list (or vector) of length 340
    return max(0, -1.0*x[262] + 1.0)
def l376_263(x):
    # x is a list (or vector) of length 340
    return max(0, -1.0*x[263] + 1.0)
def l376_264(x):
    # x is a list (or vector) of length 340
    return max(0, x[264] + -64.0*x[268] + 64.0*x[272])
def l376_265(x):
    # x is a list (or vector) of length 340
    return max(0, x[265] + -64.0*x[269] + 64.0*x[273])
def l376_266(x):
    # x is a list (or vector) of length 340
    return max(0, x[266] + -64.0*x[270] + 64.0*x[274])
def l376_267(x):
    # x is a list (or vector) of length 340
    return max(0, x[267] + -64.0*x[271] + 64.0*x[275])
def l376_268(x):
    # x is a list (or vector) of length 340
    return max(0, x[276])
def l376_269(x):
    # x is a list (or vector) of length 340
    return max(0, x[277])
def l376_270(x):
    # x is a list (or vector) of length 340
    return max(0, x[278])
def l376_271(x):
    # x is a list (or vector) of length 340
    return max(0, x[279])
def l376_272(x):
    # x is a list (or vector) of length 340
    return max(0, x[280])
def l376_273(x):
    # x is a list (or vector) of length 340
    return max(0, x[281])
def l376_274(x):
    # x is a list (or vector) of length 340
    return max(0, x[282])
def l376_275(x):
    # x is a list (or vector) of length 340
    return max(0, x[283])
def l376_276(x):
    # x is a list (or vector) of length 340
    return max(0, x[284])
def l376_277(x):
    # x is a list (or vector) of length 340
    return max(0, x[285])
def l376_278(x):
    # x is a list (or vector) of length 340
    return max(0, x[286])
def l376_279(x):
    # x is a list (or vector) of length 340
    return max(0, x[287])
def l376_280(x):
    # x is a list (or vector) of length 340
    return max(0, x[288])
def l376_281(x):
    # x is a list (or vector) of length 340
    return max(0, x[289])
def l376_282(x):
    # x is a list (or vector) of length 340
    return max(0, x[290])
def l376_283(x):
    # x is a list (or vector) of length 340
    return max(0, x[291])
def l376_284(x):
    # x is a list (or vector) of length 340
    return max(0, x[292])
def l376_285(x):
    # x is a list (or vector) of length 340
    return max(0, x[293])
def l376_286(x):
    # x is a list (or vector) of length 340
    return max(0, x[294])
def l376_287(x):
    # x is a list (or vector) of length 340
    return max(0, x[295])
def l376_288(x):
    # x is a list (or vector) of length 340
    return max(0, x[296])
def l376_289(x):
    # x is a list (or vector) of length 340
    return max(0, x[297])
def l376_290(x):
    # x is a list (or vector) of length 340
    return max(0, x[298])
def l376_291(x):
    # x is a list (or vector) of length 340
    return max(0, x[299])
def l376_292(x):
    # x is a list (or vector) of length 340
    return max(0, x[300])
def l376_293(x):
    # x is a list (or vector) of length 340
    return max(0, x[301])
def l376_294(x):
    # x is a list (or vector) of length 340
    return max(0, x[302])
def l376_295(x):
    # x is a list (or vector) of length 340
    return max(0, x[303])
def l376_296(x):
    # x is a list (or vector) of length 340
    return max(0, x[304])
def l376_297(x):
    # x is a list (or vector) of length 340
    return max(0, x[305])
def l376_298(x):
    # x is a list (or vector) of length 340
    return max(0, x[306])
def l376_299(x):
    # x is a list (or vector) of length 340
    return max(0, x[307])
def l376_300(x):
    # x is a list (or vector) of length 340
    return max(0, x[308])
def l376_301(x):
    # x is a list (or vector) of length 340
    return max(0, x[309])
def l376_302(x):
    # x is a list (or vector) of length 340
    return max(0, x[310])
def l376_303(x):
    # x is a list (or vector) of length 340
    return max(0, x[311])
def l376_304(x):
    # x is a list (or vector) of length 340
    return max(0, x[312])
def l376_305(x):
    # x is a list (or vector) of length 340
    return max(0, x[313])
def l376_306(x):
    # x is a list (or vector) of length 340
    return max(0, x[314])
def l376_307(x):
    # x is a list (or vector) of length 340
    return max(0, x[315])
def l376_308(x):
    # x is a list (or vector) of length 340
    return max(0, x[316])
def l376_309(x):
    # x is a list (or vector) of length 340
    return max(0, x[317])
def l376_310(x):
    # x is a list (or vector) of length 340
    return max(0, x[318])
def l376_311(x):
    # x is a list (or vector) of length 340
    return max(0, x[319])
def l376_312(x):
    # x is a list (or vector) of length 340
    return max(0, x[320])
def l376_313(x):
    # x is a list (or vector) of length 340
    return max(0, x[321])
def l376_314(x):
    # x is a list (or vector) of length 340
    return max(0, x[322])
def l376_315(x):
    # x is a list (or vector) of length 340
    return max(0, x[323])
def l376_316(x):
    # x is a list (or vector) of length 340
    return max(0, x[324])
def l376_317(x):
    # x is a list (or vector) of length 340
    return max(0, x[325])
def l376_318(x):
    # x is a list (or vector) of length 340
    return max(0, x[326])
def l376_319(x):
    # x is a list (or vector) of length 340
    return max(0, x[327])
def l376_320(x):
    # x is a list (or vector) of length 340
    return max(0, x[328])
def l376_321(x):
    # x is a list (or vector) of length 340
    return max(0, x[329])
def l376_322(x):
    # x is a list (or vector) of length 340
    return max(0, x[330])
def l376_323(x):
    # x is a list (or vector) of length 340
    return max(0, x[331])
def l376_324(x):
    # x is a list (or vector) of length 340
    return max(0, x[332])
def l376_325(x):
    # x is a list (or vector) of length 340
    return max(0, x[333])
def l376_326(x):
    # x is a list (or vector) of length 340
    return max(0, x[334])
def l376_327(x):
    # x is a list (or vector) of length 340
    return max(0, x[335])
def l376_328(x):
    # x is a list (or vector) of length 340
    return max(0, x[336])
def l376_329(x):
    # x is a list (or vector) of length 340
    return max(0, x[337])
def l376_330(x):
    # x is a list (or vector) of length 340
    return max(0, x[338])
def l376_331(x):
    # x is a list (or vector) of length 340
    return max(0, x[339])
def l376_(x):
    # x is a list (or vector) of length 340
    return [
        l376_0(x),
        l376_1(x),
        l376_2(x),
        l376_3(x),
        l376_4(x),
        l376_5(x),
        l376_6(x),
        l376_7(x),
        l376_8(x),
        l376_9(x),
        l376_10(x),
        l376_11(x),
        l376_12(x),
        l376_13(x),
        l376_14(x),
        l376_15(x),
        l376_16(x),
        l376_17(x),
        l376_18(x),
        l376_19(x),
        l376_20(x),
        l376_21(x),
        l376_22(x),
        l376_23(x),
        l376_24(x),
        l376_25(x),
        l376_26(x),
        l376_27(x),
        l376_28(x),
        l376_29(x),
        l376_30(x),
        l376_31(x),
        l376_32(x),
        l376_33(x),
        l376_34(x),
        l376_35(x),
        l376_36(x),
        l376_37(x),
        l376_38(x),
        l376_39(x),
        l376_40(x),
        l376_41(x),
        l376_42(x),
        l376_43(x),
        l376_44(x),
        l376_45(x),
        l376_46(x),
        l376_47(x),
        l376_48(x),
        l376_49(x),
        l376_50(x),
        l376_51(x),
        l376_52(x),
        l376_53(x),
        l376_54(x),
        l376_55(x),
        l376_56(x),
        l376_57(x),
        l376_58(x),
        l376_59(x),
        l376_60(x),
        l376_61(x),
        l376_62(x),
        l376_63(x),
        l376_64(x),
        l376_65(x),
        l376_66(x),
        l376_67(x),
        l376_68(x),
        l376_69(x),
        l376_70(x),
        l376_71(x),
        l376_72(x),
        l376_73(x),
        l376_74(x),
        l376_75(x),
        l376_76(x),
        l376_77(x),
        l376_78(x),
        l376_79(x),
        l376_80(x),
        l376_81(x),
        l376_82(x),
        l376_83(x),
        l376_84(x),
        l376_85(x),
        l376_86(x),
        l376_87(x),
        l376_88(x),
        l376_89(x),
        l376_90(x),
        l376_91(x),
        l376_92(x),
        l376_93(x),
        l376_94(x),
        l376_95(x),
        l376_96(x),
        l376_97(x),
        l376_98(x),
        l376_99(x),
        l376_100(x),
        l376_101(x),
        l376_102(x),
        l376_103(x),
        l376_104(x),
        l376_105(x),
        l376_106(x),
        l376_107(x),
        l376_108(x),
        l376_109(x),
        l376_110(x),
        l376_111(x),
        l376_112(x),
        l376_113(x),
        l376_114(x),
        l376_115(x),
        l376_116(x),
        l376_117(x),
        l376_118(x),
        l376_119(x),
        l376_120(x),
        l376_121(x),
        l376_122(x),
        l376_123(x),
        l376_124(x),
        l376_125(x),
        l376_126(x),
        l376_127(x),
        l376_128(x),
        l376_129(x),
        l376_130(x),
        l376_131(x),
        l376_132(x),
        l376_133(x),
        l376_134(x),
        l376_135(x),
        l376_136(x),
        l376_137(x),
        l376_138(x),
        l376_139(x),
        l376_140(x),
        l376_141(x),
        l376_142(x),
        l376_143(x),
        l376_144(x),
        l376_145(x),
        l376_146(x),
        l376_147(x),
        l376_148(x),
        l376_149(x),
        l376_150(x),
        l376_151(x),
        l376_152(x),
        l376_153(x),
        l376_154(x),
        l376_155(x),
        l376_156(x),
        l376_157(x),
        l376_158(x),
        l376_159(x),
        l376_160(x),
        l376_161(x),
        l376_162(x),
        l376_163(x),
        l376_164(x),
        l376_165(x),
        l376_166(x),
        l376_167(x),
        l376_168(x),
        l376_169(x),
        l376_170(x),
        l376_171(x),
        l376_172(x),
        l376_173(x),
        l376_174(x),
        l376_175(x),
        l376_176(x),
        l376_177(x),
        l376_178(x),
        l376_179(x),
        l376_180(x),
        l376_181(x),
        l376_182(x),
        l376_183(x),
        l376_184(x),
        l376_185(x),
        l376_186(x),
        l376_187(x),
        l376_188(x),
        l376_189(x),
        l376_190(x),
        l376_191(x),
        l376_192(x),
        l376_193(x),
        l376_194(x),
        l376_195(x),
        l376_196(x),
        l376_197(x),
        l376_198(x),
        l376_199(x),
        l376_200(x),
        l376_201(x),
        l376_202(x),
        l376_203(x),
        l376_204(x),
        l376_205(x),
        l376_206(x),
        l376_207(x),
        l376_208(x),
        l376_209(x),
        l376_210(x),
        l376_211(x),
        l376_212(x),
        l376_213(x),
        l376_214(x),
        l376_215(x),
        l376_216(x),
        l376_217(x),
        l376_218(x),
        l376_219(x),
        l376_220(x),
        l376_221(x),
        l376_222(x),
        l376_223(x),
        l376_224(x),
        l376_225(x),
        l376_226(x),
        l376_227(x),
        l376_228(x),
        l376_229(x),
        l376_230(x),
        l376_231(x),
        l376_232(x),
        l376_233(x),
        l376_234(x),
        l376_235(x),
        l376_236(x),
        l376_237(x),
        l376_238(x),
        l376_239(x),
        l376_240(x),
        l376_241(x),
        l376_242(x),
        l376_243(x),
        l376_244(x),
        l376_245(x),
        l376_246(x),
        l376_247(x),
        l376_248(x),
        l376_249(x),
        l376_250(x),
        l376_251(x),
        l376_252(x),
        l376_253(x),
        l376_254(x),
        l376_255(x),
        l376_256(x),
        l376_257(x),
        l376_258(x),
        l376_259(x),
        l376_260(x),
        l376_261(x),
        l376_262(x),
        l376_263(x),
        l376_264(x),
        l376_265(x),
        l376_266(x),
        l376_267(x),
        l376_268(x),
        l376_269(x),
        l376_270(x),
        l376_271(x),
        l376_272(x),
        l376_273(x),
        l376_274(x),
        l376_275(x),
        l376_276(x),
        l376_277(x),
        l376_278(x),
        l376_279(x),
        l376_280(x),
        l376_281(x),
        l376_282(x),
        l376_283(x),
        l376_284(x),
        l376_285(x),
        l376_286(x),
        l376_287(x),
        l376_288(x),
        l376_289(x),
        l376_290(x),
        l376_291(x),
        l376_292(x),
        l376_293(x),
        l376_294(x),
        l376_295(x),
        l376_296(x),
        l376_297(x),
        l376_298(x),
        l376_299(x),
        l376_300(x),
        l376_301(x),
        l376_302(x),
        l376_303(x),
        l376_304(x),
        l376_305(x),
        l376_306(x),
        l376_307(x),
        l376_308(x),
        l376_309(x),
        l376_310(x),
        l376_311(x),
        l376_312(x),
        l376_313(x),
        l376_314(x),
        l376_315(x),
        l376_316(x),
        l376_317(x),
        l376_318(x),
        l376_319(x),
        l376_320(x),
        l376_321(x),
        l376_322(x),
        l376_323(x),
        l376_324(x),
        l376_325(x),
        l376_326(x),
        l376_327(x),
        l376_328(x),
        l376_329(x),
        l376_330(x),
        l376_331(x),
    ]