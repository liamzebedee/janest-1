import numpy as np




# Generated from reverse engineering
def l414_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 316
    out = np.empty(316, dtype=np.float32)
    
    # for i in range(0, 98):
    for i in range(0, 98):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3 (len=2)
    biases = [1.0, 1.0]
    # for i in range(98, 100):
    for i in range(0, 2):
        s = -1 * x[98 + i]
        s += biases[i]
        out[98 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0]
    # for i in range(100, 102):
    for i in range(0, 2):
        s = x[96 + i] + x[132 + i]
        s += biases[i]
        out[100 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(102, 128):
    for i in range(0, 26):
        s = x[134 + i] + -1 * x[98 + i]
        out[102 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xfffffff (len=28)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(128, 156):
    for i in range(0, 28):
        s = -1 * x[100 + i]
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(156, 184):
    for i in range(0, 28):
        s = x[128 + i] + x[132 + i]
        s += biases[i]
        out[156 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(184, 188):
    for i in range(0, 4):
        s = x[128 + i]
        out[184 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(188, 316):
    for i in range(0, 128):
        s = x[160 + i]
        out[188 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l414_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l414_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l414_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l414_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l414_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l414_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l414_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l414_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l414_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l414_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l414_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l414_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l414_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l414_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l414_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l414_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l414_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l414_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l414_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l414_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l414_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l414_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l414_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l414_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l414_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l414_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l414_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l414_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l414_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l414_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l414_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l414_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l414_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l414_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l414_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l414_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l414_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l414_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l414_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l414_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l414_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l414_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l414_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l414_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l414_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l414_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l414_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l414_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l414_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l414_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l414_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l414_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l414_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l414_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l414_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l414_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l414_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l414_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l414_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l414_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l414_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l414_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l414_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l414_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l414_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l414_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l414_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l414_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l414_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l414_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l414_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l414_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l414_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l414_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l414_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l414_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l414_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l414_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l414_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l414_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l414_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l414_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l414_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l414_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l414_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l414_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l414_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l414_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l414_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l414_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l414_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l414_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l414_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l414_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l414_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l414_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l414_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l414_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l414_98(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[98] + 1.0)
def l414_99(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[99] + 1.0)
def l414_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + x[132] + -1.0)
def l414_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + x[133] + -1.0)
def l414_102(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[98] + x[134])
def l414_103(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[99] + x[135])
def l414_104(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[100] + x[136])
def l414_105(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[101] + x[137])
def l414_106(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[102] + x[138])
def l414_107(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[103] + x[139])
def l414_108(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + x[140])
def l414_109(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + x[141])
def l414_110(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + x[142])
def l414_111(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + x[143])
def l414_112(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + x[144])
def l414_113(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + x[145])
def l414_114(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + x[146])
def l414_115(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + x[147])
def l414_116(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + x[148])
def l414_117(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + x[149])
def l414_118(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + x[150])
def l414_119(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + x[151])
def l414_120(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + x[152])
def l414_121(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + x[153])
def l414_122(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + x[154])
def l414_123(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + x[155])
def l414_124(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + x[156])
def l414_125(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + x[157])
def l414_126(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + x[158])
def l414_127(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + x[159])
def l414_128(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[100] + 1.0)
def l414_129(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[101] + 1.0)
def l414_130(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[102] + 1.0)
def l414_131(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[103] + 1.0)
def l414_132(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + 1.0)
def l414_133(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + 1.0)
def l414_134(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + 1.0)
def l414_135(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + 1.0)
def l414_136(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + 1.0)
def l414_137(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + 1.0)
def l414_138(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + 1.0)
def l414_139(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + 1.0)
def l414_140(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + 1.0)
def l414_141(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + 1.0)
def l414_142(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + 1.0)
def l414_143(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + 1.0)
def l414_144(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + 1.0)
def l414_145(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + 1.0)
def l414_146(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + 1.0)
def l414_147(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + 1.0)
def l414_148(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + 1.0)
def l414_149(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + 1.0)
def l414_150(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + 1.0)
def l414_151(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + 1.0)
def l414_152(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + 1.0)
def l414_153(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + 1.0)
def l414_154(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[126] + 1.0)
def l414_155(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[127] + 1.0)
def l414_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[128] + x[132] + -1.0)
def l414_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[129] + x[133] + -1.0)
def l414_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[130] + x[134] + -1.0)
def l414_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[131] + x[135] + -1.0)
def l414_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[132] + x[136] + -1.0)
def l414_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[133] + x[137] + -1.0)
def l414_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[134] + x[138] + -1.0)
def l414_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[135] + x[139] + -1.0)
def l414_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[136] + x[140] + -1.0)
def l414_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[137] + x[141] + -1.0)
def l414_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[138] + x[142] + -1.0)
def l414_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[139] + x[143] + -1.0)
def l414_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[140] + x[144] + -1.0)
def l414_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[141] + x[145] + -1.0)
def l414_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[142] + x[146] + -1.0)
def l414_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[143] + x[147] + -1.0)
def l414_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[144] + x[148] + -1.0)
def l414_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[145] + x[149] + -1.0)
def l414_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[146] + x[150] + -1.0)
def l414_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[147] + x[151] + -1.0)
def l414_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[148] + x[152] + -1.0)
def l414_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[149] + x[153] + -1.0)
def l414_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[150] + x[154] + -1.0)
def l414_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[151] + x[155] + -1.0)
def l414_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[152] + x[156] + -1.0)
def l414_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[153] + x[157] + -1.0)
def l414_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[154] + x[158] + -1.0)
def l414_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[155] + x[159] + -1.0)
def l414_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l414_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l414_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l414_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l414_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l414_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l414_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l414_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l414_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l414_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l414_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l414_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l414_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l414_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l414_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l414_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l414_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l414_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l414_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l414_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l414_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l414_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l414_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l414_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l414_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l414_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l414_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l414_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l414_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l414_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l414_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l414_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l414_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l414_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l414_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l414_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l414_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l414_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l414_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l414_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l414_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l414_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l414_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l414_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l414_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l414_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l414_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l414_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l414_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l414_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l414_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l414_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l414_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l414_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l414_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l414_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l414_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l414_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l414_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l414_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l414_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l414_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l414_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l414_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l414_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l414_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l414_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l414_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l414_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l414_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l414_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l414_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l414_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l414_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l414_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l414_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l414_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l414_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l414_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l414_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l414_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l414_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l414_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l414_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l414_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l414_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l414_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l414_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l414_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l414_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l414_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l414_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l414_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l414_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l414_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l414_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l414_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l414_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l414_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l414_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l414_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l414_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l414_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l414_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l414_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l414_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l414_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l414_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l414_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l414_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l414_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l414_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l414_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l414_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l414_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l414_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l414_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l414_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l414_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l414_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l414_304(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l414_305(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l414_306(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l414_307(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l414_308(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l414_309(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l414_310(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l414_311(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l414_312(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l414_313(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l414_314(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l414_315(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l414_(x):
    # x is a list (or vector) of length 288
    return [
        l414_0(x),
        l414_1(x),
        l414_2(x),
        l414_3(x),
        l414_4(x),
        l414_5(x),
        l414_6(x),
        l414_7(x),
        l414_8(x),
        l414_9(x),
        l414_10(x),
        l414_11(x),
        l414_12(x),
        l414_13(x),
        l414_14(x),
        l414_15(x),
        l414_16(x),
        l414_17(x),
        l414_18(x),
        l414_19(x),
        l414_20(x),
        l414_21(x),
        l414_22(x),
        l414_23(x),
        l414_24(x),
        l414_25(x),
        l414_26(x),
        l414_27(x),
        l414_28(x),
        l414_29(x),
        l414_30(x),
        l414_31(x),
        l414_32(x),
        l414_33(x),
        l414_34(x),
        l414_35(x),
        l414_36(x),
        l414_37(x),
        l414_38(x),
        l414_39(x),
        l414_40(x),
        l414_41(x),
        l414_42(x),
        l414_43(x),
        l414_44(x),
        l414_45(x),
        l414_46(x),
        l414_47(x),
        l414_48(x),
        l414_49(x),
        l414_50(x),
        l414_51(x),
        l414_52(x),
        l414_53(x),
        l414_54(x),
        l414_55(x),
        l414_56(x),
        l414_57(x),
        l414_58(x),
        l414_59(x),
        l414_60(x),
        l414_61(x),
        l414_62(x),
        l414_63(x),
        l414_64(x),
        l414_65(x),
        l414_66(x),
        l414_67(x),
        l414_68(x),
        l414_69(x),
        l414_70(x),
        l414_71(x),
        l414_72(x),
        l414_73(x),
        l414_74(x),
        l414_75(x),
        l414_76(x),
        l414_77(x),
        l414_78(x),
        l414_79(x),
        l414_80(x),
        l414_81(x),
        l414_82(x),
        l414_83(x),
        l414_84(x),
        l414_85(x),
        l414_86(x),
        l414_87(x),
        l414_88(x),
        l414_89(x),
        l414_90(x),
        l414_91(x),
        l414_92(x),
        l414_93(x),
        l414_94(x),
        l414_95(x),
        l414_96(x),
        l414_97(x),
        l414_98(x),
        l414_99(x),
        l414_100(x),
        l414_101(x),
        l414_102(x),
        l414_103(x),
        l414_104(x),
        l414_105(x),
        l414_106(x),
        l414_107(x),
        l414_108(x),
        l414_109(x),
        l414_110(x),
        l414_111(x),
        l414_112(x),
        l414_113(x),
        l414_114(x),
        l414_115(x),
        l414_116(x),
        l414_117(x),
        l414_118(x),
        l414_119(x),
        l414_120(x),
        l414_121(x),
        l414_122(x),
        l414_123(x),
        l414_124(x),
        l414_125(x),
        l414_126(x),
        l414_127(x),
        l414_128(x),
        l414_129(x),
        l414_130(x),
        l414_131(x),
        l414_132(x),
        l414_133(x),
        l414_134(x),
        l414_135(x),
        l414_136(x),
        l414_137(x),
        l414_138(x),
        l414_139(x),
        l414_140(x),
        l414_141(x),
        l414_142(x),
        l414_143(x),
        l414_144(x),
        l414_145(x),
        l414_146(x),
        l414_147(x),
        l414_148(x),
        l414_149(x),
        l414_150(x),
        l414_151(x),
        l414_152(x),
        l414_153(x),
        l414_154(x),
        l414_155(x),
        l414_156(x),
        l414_157(x),
        l414_158(x),
        l414_159(x),
        l414_160(x),
        l414_161(x),
        l414_162(x),
        l414_163(x),
        l414_164(x),
        l414_165(x),
        l414_166(x),
        l414_167(x),
        l414_168(x),
        l414_169(x),
        l414_170(x),
        l414_171(x),
        l414_172(x),
        l414_173(x),
        l414_174(x),
        l414_175(x),
        l414_176(x),
        l414_177(x),
        l414_178(x),
        l414_179(x),
        l414_180(x),
        l414_181(x),
        l414_182(x),
        l414_183(x),
        l414_184(x),
        l414_185(x),
        l414_186(x),
        l414_187(x),
        l414_188(x),
        l414_189(x),
        l414_190(x),
        l414_191(x),
        l414_192(x),
        l414_193(x),
        l414_194(x),
        l414_195(x),
        l414_196(x),
        l414_197(x),
        l414_198(x),
        l414_199(x),
        l414_200(x),
        l414_201(x),
        l414_202(x),
        l414_203(x),
        l414_204(x),
        l414_205(x),
        l414_206(x),
        l414_207(x),
        l414_208(x),
        l414_209(x),
        l414_210(x),
        l414_211(x),
        l414_212(x),
        l414_213(x),
        l414_214(x),
        l414_215(x),
        l414_216(x),
        l414_217(x),
        l414_218(x),
        l414_219(x),
        l414_220(x),
        l414_221(x),
        l414_222(x),
        l414_223(x),
        l414_224(x),
        l414_225(x),
        l414_226(x),
        l414_227(x),
        l414_228(x),
        l414_229(x),
        l414_230(x),
        l414_231(x),
        l414_232(x),
        l414_233(x),
        l414_234(x),
        l414_235(x),
        l414_236(x),
        l414_237(x),
        l414_238(x),
        l414_239(x),
        l414_240(x),
        l414_241(x),
        l414_242(x),
        l414_243(x),
        l414_244(x),
        l414_245(x),
        l414_246(x),
        l414_247(x),
        l414_248(x),
        l414_249(x),
        l414_250(x),
        l414_251(x),
        l414_252(x),
        l414_253(x),
        l414_254(x),
        l414_255(x),
        l414_256(x),
        l414_257(x),
        l414_258(x),
        l414_259(x),
        l414_260(x),
        l414_261(x),
        l414_262(x),
        l414_263(x),
        l414_264(x),
        l414_265(x),
        l414_266(x),
        l414_267(x),
        l414_268(x),
        l414_269(x),
        l414_270(x),
        l414_271(x),
        l414_272(x),
        l414_273(x),
        l414_274(x),
        l414_275(x),
        l414_276(x),
        l414_277(x),
        l414_278(x),
        l414_279(x),
        l414_280(x),
        l414_281(x),
        l414_282(x),
        l414_283(x),
        l414_284(x),
        l414_285(x),
        l414_286(x),
        l414_287(x),
        l414_288(x),
        l414_289(x),
        l414_290(x),
        l414_291(x),
        l414_292(x),
        l414_293(x),
        l414_294(x),
        l414_295(x),
        l414_296(x),
        l414_297(x),
        l414_298(x),
        l414_299(x),
        l414_300(x),
        l414_301(x),
        l414_302(x),
        l414_303(x),
        l414_304(x),
        l414_305(x),
        l414_306(x),
        l414_307(x),
        l414_308(x),
        l414_309(x),
        l414_310(x),
        l414_311(x),
        l414_312(x),
        l414_313(x),
        l414_314(x),
        l414_315(x),
    ]