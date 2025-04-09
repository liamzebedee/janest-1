import numpy as np




# Generated from reverse engineering
def l334_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 312
    out = np.empty(312, dtype=np.float32)
    
    # for i in range(0, 100):
    for i in range(0, 100):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xf (len=4)
    biases = [1.0, 1.0, 1.0, 1.0]
    # for i in range(100, 104):
    for i in range(0, 4):
        s = -1 * x[100 + i]
        s += biases[i]
        out[100 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0]
    # for i in range(104, 108):
    for i in range(0, 4):
        s = x[96 + i] + x[136 + i]
        s += biases[i]
        out[104 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(108, 128):
    for i in range(0, 20):
        s = x[140 + i] + -1 * x[100 + i]
        out[108 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffffff (len=24)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(128, 152):
    for i in range(0, 24):
        s = -1 * x[104 + i]
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(152, 176):
    for i in range(0, 24):
        s = x[128 + i] + x[136 + i]
        s += biases[i]
        out[152 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(176, 184):
    for i in range(0, 8):
        s = x[128 + i]
        out[176 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(184, 312):
    for i in range(0, 128):
        s = x[160 + i]
        out[184 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l334_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l334_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l334_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l334_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l334_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l334_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l334_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l334_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l334_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l334_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l334_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l334_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l334_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l334_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l334_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l334_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l334_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l334_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l334_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l334_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l334_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l334_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l334_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l334_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l334_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l334_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l334_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l334_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l334_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l334_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l334_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l334_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l334_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l334_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l334_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l334_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l334_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l334_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l334_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l334_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l334_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l334_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l334_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l334_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l334_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l334_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l334_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l334_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l334_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l334_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l334_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l334_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l334_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l334_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l334_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l334_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l334_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l334_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l334_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l334_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l334_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l334_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l334_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l334_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l334_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l334_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l334_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l334_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l334_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l334_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l334_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l334_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l334_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l334_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l334_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l334_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l334_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l334_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l334_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l334_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l334_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l334_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l334_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l334_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l334_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l334_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l334_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l334_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l334_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l334_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l334_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l334_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l334_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l334_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l334_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l334_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l334_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l334_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l334_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l334_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l334_100(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[100] + 1.0)
def l334_101(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[101] + 1.0)
def l334_102(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[102] + 1.0)
def l334_103(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[103] + 1.0)
def l334_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + x[136] + -1.0)
def l334_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + x[137] + -1.0)
def l334_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + x[138] + -1.0)
def l334_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + x[139] + -1.0)
def l334_108(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[100] + x[140])
def l334_109(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[101] + x[141])
def l334_110(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[102] + x[142])
def l334_111(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[103] + x[143])
def l334_112(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + x[144])
def l334_113(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + x[145])
def l334_114(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + x[146])
def l334_115(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + x[147])
def l334_116(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + x[148])
def l334_117(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + x[149])
def l334_118(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + x[150])
def l334_119(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + x[151])
def l334_120(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + x[152])
def l334_121(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + x[153])
def l334_122(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + x[154])
def l334_123(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + x[155])
def l334_124(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + x[156])
def l334_125(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + x[157])
def l334_126(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + x[158])
def l334_127(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + x[159])
def l334_128(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + 1.0)
def l334_129(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + 1.0)
def l334_130(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + 1.0)
def l334_131(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + 1.0)
def l334_132(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + 1.0)
def l334_133(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + 1.0)
def l334_134(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + 1.0)
def l334_135(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + 1.0)
def l334_136(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + 1.0)
def l334_137(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + 1.0)
def l334_138(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + 1.0)
def l334_139(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + 1.0)
def l334_140(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + 1.0)
def l334_141(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + 1.0)
def l334_142(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + 1.0)
def l334_143(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + 1.0)
def l334_144(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + 1.0)
def l334_145(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + 1.0)
def l334_146(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + 1.0)
def l334_147(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + 1.0)
def l334_148(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + 1.0)
def l334_149(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + 1.0)
def l334_150(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[126] + 1.0)
def l334_151(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[127] + 1.0)
def l334_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[128] + x[136] + -1.0)
def l334_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[129] + x[137] + -1.0)
def l334_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[130] + x[138] + -1.0)
def l334_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[131] + x[139] + -1.0)
def l334_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[132] + x[140] + -1.0)
def l334_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[133] + x[141] + -1.0)
def l334_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[134] + x[142] + -1.0)
def l334_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[135] + x[143] + -1.0)
def l334_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[136] + x[144] + -1.0)
def l334_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[137] + x[145] + -1.0)
def l334_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[138] + x[146] + -1.0)
def l334_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[139] + x[147] + -1.0)
def l334_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[140] + x[148] + -1.0)
def l334_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[141] + x[149] + -1.0)
def l334_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[142] + x[150] + -1.0)
def l334_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[143] + x[151] + -1.0)
def l334_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[144] + x[152] + -1.0)
def l334_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[145] + x[153] + -1.0)
def l334_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[146] + x[154] + -1.0)
def l334_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[147] + x[155] + -1.0)
def l334_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[148] + x[156] + -1.0)
def l334_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[149] + x[157] + -1.0)
def l334_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[150] + x[158] + -1.0)
def l334_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[151] + x[159] + -1.0)
def l334_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l334_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l334_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l334_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l334_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l334_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l334_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l334_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l334_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l334_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l334_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l334_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l334_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l334_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l334_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l334_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l334_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l334_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l334_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l334_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l334_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l334_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l334_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l334_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l334_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l334_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l334_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l334_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l334_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l334_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l334_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l334_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l334_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l334_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l334_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l334_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l334_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l334_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l334_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l334_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l334_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l334_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l334_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l334_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l334_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l334_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l334_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l334_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l334_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l334_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l334_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l334_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l334_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l334_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l334_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l334_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l334_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l334_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l334_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l334_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l334_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l334_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l334_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l334_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l334_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l334_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l334_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l334_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l334_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l334_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l334_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l334_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l334_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l334_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l334_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l334_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l334_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l334_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l334_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l334_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l334_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l334_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l334_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l334_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l334_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l334_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l334_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l334_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l334_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l334_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l334_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l334_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l334_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l334_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l334_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l334_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l334_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l334_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l334_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l334_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l334_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l334_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l334_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l334_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l334_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l334_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l334_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l334_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l334_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l334_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l334_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l334_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l334_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l334_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l334_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l334_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l334_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l334_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l334_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l334_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l334_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l334_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l334_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l334_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l334_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l334_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l334_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l334_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l334_304(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l334_305(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l334_306(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l334_307(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l334_308(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l334_309(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l334_310(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l334_311(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l334_(x):
    # x is a list (or vector) of length 288
    return [
        l334_0(x),
        l334_1(x),
        l334_2(x),
        l334_3(x),
        l334_4(x),
        l334_5(x),
        l334_6(x),
        l334_7(x),
        l334_8(x),
        l334_9(x),
        l334_10(x),
        l334_11(x),
        l334_12(x),
        l334_13(x),
        l334_14(x),
        l334_15(x),
        l334_16(x),
        l334_17(x),
        l334_18(x),
        l334_19(x),
        l334_20(x),
        l334_21(x),
        l334_22(x),
        l334_23(x),
        l334_24(x),
        l334_25(x),
        l334_26(x),
        l334_27(x),
        l334_28(x),
        l334_29(x),
        l334_30(x),
        l334_31(x),
        l334_32(x),
        l334_33(x),
        l334_34(x),
        l334_35(x),
        l334_36(x),
        l334_37(x),
        l334_38(x),
        l334_39(x),
        l334_40(x),
        l334_41(x),
        l334_42(x),
        l334_43(x),
        l334_44(x),
        l334_45(x),
        l334_46(x),
        l334_47(x),
        l334_48(x),
        l334_49(x),
        l334_50(x),
        l334_51(x),
        l334_52(x),
        l334_53(x),
        l334_54(x),
        l334_55(x),
        l334_56(x),
        l334_57(x),
        l334_58(x),
        l334_59(x),
        l334_60(x),
        l334_61(x),
        l334_62(x),
        l334_63(x),
        l334_64(x),
        l334_65(x),
        l334_66(x),
        l334_67(x),
        l334_68(x),
        l334_69(x),
        l334_70(x),
        l334_71(x),
        l334_72(x),
        l334_73(x),
        l334_74(x),
        l334_75(x),
        l334_76(x),
        l334_77(x),
        l334_78(x),
        l334_79(x),
        l334_80(x),
        l334_81(x),
        l334_82(x),
        l334_83(x),
        l334_84(x),
        l334_85(x),
        l334_86(x),
        l334_87(x),
        l334_88(x),
        l334_89(x),
        l334_90(x),
        l334_91(x),
        l334_92(x),
        l334_93(x),
        l334_94(x),
        l334_95(x),
        l334_96(x),
        l334_97(x),
        l334_98(x),
        l334_99(x),
        l334_100(x),
        l334_101(x),
        l334_102(x),
        l334_103(x),
        l334_104(x),
        l334_105(x),
        l334_106(x),
        l334_107(x),
        l334_108(x),
        l334_109(x),
        l334_110(x),
        l334_111(x),
        l334_112(x),
        l334_113(x),
        l334_114(x),
        l334_115(x),
        l334_116(x),
        l334_117(x),
        l334_118(x),
        l334_119(x),
        l334_120(x),
        l334_121(x),
        l334_122(x),
        l334_123(x),
        l334_124(x),
        l334_125(x),
        l334_126(x),
        l334_127(x),
        l334_128(x),
        l334_129(x),
        l334_130(x),
        l334_131(x),
        l334_132(x),
        l334_133(x),
        l334_134(x),
        l334_135(x),
        l334_136(x),
        l334_137(x),
        l334_138(x),
        l334_139(x),
        l334_140(x),
        l334_141(x),
        l334_142(x),
        l334_143(x),
        l334_144(x),
        l334_145(x),
        l334_146(x),
        l334_147(x),
        l334_148(x),
        l334_149(x),
        l334_150(x),
        l334_151(x),
        l334_152(x),
        l334_153(x),
        l334_154(x),
        l334_155(x),
        l334_156(x),
        l334_157(x),
        l334_158(x),
        l334_159(x),
        l334_160(x),
        l334_161(x),
        l334_162(x),
        l334_163(x),
        l334_164(x),
        l334_165(x),
        l334_166(x),
        l334_167(x),
        l334_168(x),
        l334_169(x),
        l334_170(x),
        l334_171(x),
        l334_172(x),
        l334_173(x),
        l334_174(x),
        l334_175(x),
        l334_176(x),
        l334_177(x),
        l334_178(x),
        l334_179(x),
        l334_180(x),
        l334_181(x),
        l334_182(x),
        l334_183(x),
        l334_184(x),
        l334_185(x),
        l334_186(x),
        l334_187(x),
        l334_188(x),
        l334_189(x),
        l334_190(x),
        l334_191(x),
        l334_192(x),
        l334_193(x),
        l334_194(x),
        l334_195(x),
        l334_196(x),
        l334_197(x),
        l334_198(x),
        l334_199(x),
        l334_200(x),
        l334_201(x),
        l334_202(x),
        l334_203(x),
        l334_204(x),
        l334_205(x),
        l334_206(x),
        l334_207(x),
        l334_208(x),
        l334_209(x),
        l334_210(x),
        l334_211(x),
        l334_212(x),
        l334_213(x),
        l334_214(x),
        l334_215(x),
        l334_216(x),
        l334_217(x),
        l334_218(x),
        l334_219(x),
        l334_220(x),
        l334_221(x),
        l334_222(x),
        l334_223(x),
        l334_224(x),
        l334_225(x),
        l334_226(x),
        l334_227(x),
        l334_228(x),
        l334_229(x),
        l334_230(x),
        l334_231(x),
        l334_232(x),
        l334_233(x),
        l334_234(x),
        l334_235(x),
        l334_236(x),
        l334_237(x),
        l334_238(x),
        l334_239(x),
        l334_240(x),
        l334_241(x),
        l334_242(x),
        l334_243(x),
        l334_244(x),
        l334_245(x),
        l334_246(x),
        l334_247(x),
        l334_248(x),
        l334_249(x),
        l334_250(x),
        l334_251(x),
        l334_252(x),
        l334_253(x),
        l334_254(x),
        l334_255(x),
        l334_256(x),
        l334_257(x),
        l334_258(x),
        l334_259(x),
        l334_260(x),
        l334_261(x),
        l334_262(x),
        l334_263(x),
        l334_264(x),
        l334_265(x),
        l334_266(x),
        l334_267(x),
        l334_268(x),
        l334_269(x),
        l334_270(x),
        l334_271(x),
        l334_272(x),
        l334_273(x),
        l334_274(x),
        l334_275(x),
        l334_276(x),
        l334_277(x),
        l334_278(x),
        l334_279(x),
        l334_280(x),
        l334_281(x),
        l334_282(x),
        l334_283(x),
        l334_284(x),
        l334_285(x),
        l334_286(x),
        l334_287(x),
        l334_288(x),
        l334_289(x),
        l334_290(x),
        l334_291(x),
        l334_292(x),
        l334_293(x),
        l334_294(x),
        l334_295(x),
        l334_296(x),
        l334_297(x),
        l334_298(x),
        l334_299(x),
        l334_300(x),
        l334_301(x),
        l334_302(x),
        l334_303(x),
        l334_304(x),
        l334_305(x),
        l334_306(x),
        l334_307(x),
        l334_308(x),
        l334_309(x),
        l334_310(x),
        l334_311(x),
    ]