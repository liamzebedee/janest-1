import numpy as np




# Generated from reverse engineering
def l250_g(x: np.ndarray) -> np.ndarray:
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




def l250_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l250_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l250_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l250_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l250_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l250_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l250_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l250_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l250_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l250_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l250_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l250_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l250_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l250_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l250_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l250_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l250_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l250_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l250_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l250_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l250_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l250_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l250_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l250_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l250_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l250_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l250_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l250_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l250_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l250_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l250_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l250_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l250_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l250_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l250_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l250_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l250_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l250_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l250_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l250_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l250_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l250_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l250_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l250_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l250_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l250_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l250_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l250_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l250_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l250_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l250_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l250_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l250_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l250_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l250_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l250_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l250_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l250_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l250_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l250_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l250_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l250_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l250_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l250_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l250_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l250_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l250_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l250_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l250_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l250_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l250_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l250_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l250_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l250_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l250_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l250_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l250_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l250_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l250_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l250_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l250_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l250_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l250_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l250_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l250_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l250_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l250_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l250_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l250_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l250_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l250_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l250_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l250_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l250_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l250_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l250_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l250_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l250_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l250_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l250_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l250_100(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[100] + 1.0)
def l250_101(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[101] + 1.0)
def l250_102(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[102] + 1.0)
def l250_103(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[103] + 1.0)
def l250_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + x[136] + -1.0)
def l250_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + x[137] + -1.0)
def l250_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + x[138] + -1.0)
def l250_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + x[139] + -1.0)
def l250_108(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[100] + x[140])
def l250_109(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[101] + x[141])
def l250_110(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[102] + x[142])
def l250_111(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[103] + x[143])
def l250_112(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + x[144])
def l250_113(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + x[145])
def l250_114(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + x[146])
def l250_115(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + x[147])
def l250_116(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + x[148])
def l250_117(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + x[149])
def l250_118(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + x[150])
def l250_119(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + x[151])
def l250_120(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + x[152])
def l250_121(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + x[153])
def l250_122(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + x[154])
def l250_123(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + x[155])
def l250_124(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + x[156])
def l250_125(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + x[157])
def l250_126(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + x[158])
def l250_127(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + x[159])
def l250_128(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + 1.0)
def l250_129(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + 1.0)
def l250_130(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + 1.0)
def l250_131(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + 1.0)
def l250_132(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + 1.0)
def l250_133(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + 1.0)
def l250_134(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + 1.0)
def l250_135(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + 1.0)
def l250_136(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + 1.0)
def l250_137(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + 1.0)
def l250_138(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + 1.0)
def l250_139(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + 1.0)
def l250_140(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + 1.0)
def l250_141(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + 1.0)
def l250_142(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + 1.0)
def l250_143(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + 1.0)
def l250_144(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + 1.0)
def l250_145(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + 1.0)
def l250_146(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + 1.0)
def l250_147(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + 1.0)
def l250_148(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + 1.0)
def l250_149(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + 1.0)
def l250_150(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[126] + 1.0)
def l250_151(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[127] + 1.0)
def l250_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[128] + x[136] + -1.0)
def l250_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[129] + x[137] + -1.0)
def l250_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[130] + x[138] + -1.0)
def l250_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[131] + x[139] + -1.0)
def l250_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[132] + x[140] + -1.0)
def l250_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[133] + x[141] + -1.0)
def l250_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[134] + x[142] + -1.0)
def l250_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[135] + x[143] + -1.0)
def l250_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[136] + x[144] + -1.0)
def l250_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[137] + x[145] + -1.0)
def l250_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[138] + x[146] + -1.0)
def l250_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[139] + x[147] + -1.0)
def l250_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[140] + x[148] + -1.0)
def l250_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[141] + x[149] + -1.0)
def l250_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[142] + x[150] + -1.0)
def l250_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[143] + x[151] + -1.0)
def l250_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[144] + x[152] + -1.0)
def l250_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[145] + x[153] + -1.0)
def l250_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[146] + x[154] + -1.0)
def l250_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[147] + x[155] + -1.0)
def l250_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[148] + x[156] + -1.0)
def l250_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[149] + x[157] + -1.0)
def l250_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[150] + x[158] + -1.0)
def l250_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[151] + x[159] + -1.0)
def l250_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l250_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l250_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l250_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l250_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l250_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l250_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l250_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l250_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l250_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l250_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l250_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l250_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l250_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l250_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l250_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l250_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l250_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l250_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l250_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l250_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l250_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l250_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l250_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l250_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l250_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l250_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l250_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l250_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l250_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l250_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l250_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l250_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l250_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l250_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l250_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l250_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l250_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l250_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l250_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l250_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l250_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l250_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l250_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l250_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l250_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l250_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l250_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l250_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l250_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l250_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l250_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l250_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l250_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l250_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l250_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l250_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l250_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l250_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l250_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l250_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l250_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l250_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l250_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l250_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l250_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l250_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l250_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l250_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l250_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l250_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l250_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l250_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l250_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l250_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l250_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l250_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l250_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l250_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l250_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l250_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l250_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l250_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l250_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l250_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l250_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l250_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l250_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l250_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l250_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l250_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l250_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l250_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l250_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l250_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l250_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l250_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l250_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l250_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l250_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l250_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l250_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l250_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l250_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l250_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l250_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l250_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l250_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l250_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l250_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l250_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l250_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l250_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l250_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l250_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l250_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l250_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l250_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l250_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l250_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l250_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l250_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l250_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l250_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l250_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l250_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l250_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l250_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l250_304(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l250_305(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l250_306(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l250_307(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l250_308(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l250_309(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l250_310(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l250_311(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l250_(x):
    # x is a list (or vector) of length 288
    return [
        l250_0(x),
        l250_1(x),
        l250_2(x),
        l250_3(x),
        l250_4(x),
        l250_5(x),
        l250_6(x),
        l250_7(x),
        l250_8(x),
        l250_9(x),
        l250_10(x),
        l250_11(x),
        l250_12(x),
        l250_13(x),
        l250_14(x),
        l250_15(x),
        l250_16(x),
        l250_17(x),
        l250_18(x),
        l250_19(x),
        l250_20(x),
        l250_21(x),
        l250_22(x),
        l250_23(x),
        l250_24(x),
        l250_25(x),
        l250_26(x),
        l250_27(x),
        l250_28(x),
        l250_29(x),
        l250_30(x),
        l250_31(x),
        l250_32(x),
        l250_33(x),
        l250_34(x),
        l250_35(x),
        l250_36(x),
        l250_37(x),
        l250_38(x),
        l250_39(x),
        l250_40(x),
        l250_41(x),
        l250_42(x),
        l250_43(x),
        l250_44(x),
        l250_45(x),
        l250_46(x),
        l250_47(x),
        l250_48(x),
        l250_49(x),
        l250_50(x),
        l250_51(x),
        l250_52(x),
        l250_53(x),
        l250_54(x),
        l250_55(x),
        l250_56(x),
        l250_57(x),
        l250_58(x),
        l250_59(x),
        l250_60(x),
        l250_61(x),
        l250_62(x),
        l250_63(x),
        l250_64(x),
        l250_65(x),
        l250_66(x),
        l250_67(x),
        l250_68(x),
        l250_69(x),
        l250_70(x),
        l250_71(x),
        l250_72(x),
        l250_73(x),
        l250_74(x),
        l250_75(x),
        l250_76(x),
        l250_77(x),
        l250_78(x),
        l250_79(x),
        l250_80(x),
        l250_81(x),
        l250_82(x),
        l250_83(x),
        l250_84(x),
        l250_85(x),
        l250_86(x),
        l250_87(x),
        l250_88(x),
        l250_89(x),
        l250_90(x),
        l250_91(x),
        l250_92(x),
        l250_93(x),
        l250_94(x),
        l250_95(x),
        l250_96(x),
        l250_97(x),
        l250_98(x),
        l250_99(x),
        l250_100(x),
        l250_101(x),
        l250_102(x),
        l250_103(x),
        l250_104(x),
        l250_105(x),
        l250_106(x),
        l250_107(x),
        l250_108(x),
        l250_109(x),
        l250_110(x),
        l250_111(x),
        l250_112(x),
        l250_113(x),
        l250_114(x),
        l250_115(x),
        l250_116(x),
        l250_117(x),
        l250_118(x),
        l250_119(x),
        l250_120(x),
        l250_121(x),
        l250_122(x),
        l250_123(x),
        l250_124(x),
        l250_125(x),
        l250_126(x),
        l250_127(x),
        l250_128(x),
        l250_129(x),
        l250_130(x),
        l250_131(x),
        l250_132(x),
        l250_133(x),
        l250_134(x),
        l250_135(x),
        l250_136(x),
        l250_137(x),
        l250_138(x),
        l250_139(x),
        l250_140(x),
        l250_141(x),
        l250_142(x),
        l250_143(x),
        l250_144(x),
        l250_145(x),
        l250_146(x),
        l250_147(x),
        l250_148(x),
        l250_149(x),
        l250_150(x),
        l250_151(x),
        l250_152(x),
        l250_153(x),
        l250_154(x),
        l250_155(x),
        l250_156(x),
        l250_157(x),
        l250_158(x),
        l250_159(x),
        l250_160(x),
        l250_161(x),
        l250_162(x),
        l250_163(x),
        l250_164(x),
        l250_165(x),
        l250_166(x),
        l250_167(x),
        l250_168(x),
        l250_169(x),
        l250_170(x),
        l250_171(x),
        l250_172(x),
        l250_173(x),
        l250_174(x),
        l250_175(x),
        l250_176(x),
        l250_177(x),
        l250_178(x),
        l250_179(x),
        l250_180(x),
        l250_181(x),
        l250_182(x),
        l250_183(x),
        l250_184(x),
        l250_185(x),
        l250_186(x),
        l250_187(x),
        l250_188(x),
        l250_189(x),
        l250_190(x),
        l250_191(x),
        l250_192(x),
        l250_193(x),
        l250_194(x),
        l250_195(x),
        l250_196(x),
        l250_197(x),
        l250_198(x),
        l250_199(x),
        l250_200(x),
        l250_201(x),
        l250_202(x),
        l250_203(x),
        l250_204(x),
        l250_205(x),
        l250_206(x),
        l250_207(x),
        l250_208(x),
        l250_209(x),
        l250_210(x),
        l250_211(x),
        l250_212(x),
        l250_213(x),
        l250_214(x),
        l250_215(x),
        l250_216(x),
        l250_217(x),
        l250_218(x),
        l250_219(x),
        l250_220(x),
        l250_221(x),
        l250_222(x),
        l250_223(x),
        l250_224(x),
        l250_225(x),
        l250_226(x),
        l250_227(x),
        l250_228(x),
        l250_229(x),
        l250_230(x),
        l250_231(x),
        l250_232(x),
        l250_233(x),
        l250_234(x),
        l250_235(x),
        l250_236(x),
        l250_237(x),
        l250_238(x),
        l250_239(x),
        l250_240(x),
        l250_241(x),
        l250_242(x),
        l250_243(x),
        l250_244(x),
        l250_245(x),
        l250_246(x),
        l250_247(x),
        l250_248(x),
        l250_249(x),
        l250_250(x),
        l250_251(x),
        l250_252(x),
        l250_253(x),
        l250_254(x),
        l250_255(x),
        l250_256(x),
        l250_257(x),
        l250_258(x),
        l250_259(x),
        l250_260(x),
        l250_261(x),
        l250_262(x),
        l250_263(x),
        l250_264(x),
        l250_265(x),
        l250_266(x),
        l250_267(x),
        l250_268(x),
        l250_269(x),
        l250_270(x),
        l250_271(x),
        l250_272(x),
        l250_273(x),
        l250_274(x),
        l250_275(x),
        l250_276(x),
        l250_277(x),
        l250_278(x),
        l250_279(x),
        l250_280(x),
        l250_281(x),
        l250_282(x),
        l250_283(x),
        l250_284(x),
        l250_285(x),
        l250_286(x),
        l250_287(x),
        l250_288(x),
        l250_289(x),
        l250_290(x),
        l250_291(x),
        l250_292(x),
        l250_293(x),
        l250_294(x),
        l250_295(x),
        l250_296(x),
        l250_297(x),
        l250_298(x),
        l250_299(x),
        l250_300(x),
        l250_301(x),
        l250_302(x),
        l250_303(x),
        l250_304(x),
        l250_305(x),
        l250_306(x),
        l250_307(x),
        l250_308(x),
        l250_309(x),
        l250_310(x),
        l250_311(x),
    ]