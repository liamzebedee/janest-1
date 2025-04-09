import numpy as np




# Generated from reverse engineering
def l330_g(x: np.ndarray) -> np.ndarray:
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




def l330_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l330_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l330_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l330_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l330_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l330_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l330_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l330_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l330_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l330_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l330_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l330_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l330_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l330_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l330_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l330_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l330_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l330_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l330_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l330_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l330_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l330_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l330_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l330_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l330_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l330_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l330_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l330_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l330_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l330_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l330_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l330_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l330_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l330_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l330_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l330_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l330_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l330_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l330_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l330_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l330_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l330_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l330_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l330_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l330_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l330_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l330_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l330_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l330_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l330_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l330_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l330_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l330_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l330_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l330_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l330_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l330_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l330_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l330_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l330_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l330_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l330_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l330_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l330_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l330_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l330_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l330_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l330_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l330_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l330_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l330_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l330_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l330_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l330_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l330_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l330_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l330_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l330_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l330_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l330_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l330_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l330_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l330_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l330_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l330_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l330_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l330_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l330_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l330_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l330_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l330_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l330_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l330_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l330_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l330_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l330_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l330_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l330_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l330_98(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[98] + 1.0)
def l330_99(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[99] + 1.0)
def l330_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + x[132] + -1.0)
def l330_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + x[133] + -1.0)
def l330_102(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[98] + x[134])
def l330_103(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[99] + x[135])
def l330_104(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[100] + x[136])
def l330_105(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[101] + x[137])
def l330_106(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[102] + x[138])
def l330_107(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[103] + x[139])
def l330_108(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + x[140])
def l330_109(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + x[141])
def l330_110(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + x[142])
def l330_111(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + x[143])
def l330_112(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + x[144])
def l330_113(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + x[145])
def l330_114(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + x[146])
def l330_115(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + x[147])
def l330_116(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + x[148])
def l330_117(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + x[149])
def l330_118(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + x[150])
def l330_119(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + x[151])
def l330_120(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + x[152])
def l330_121(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + x[153])
def l330_122(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + x[154])
def l330_123(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + x[155])
def l330_124(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + x[156])
def l330_125(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + x[157])
def l330_126(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + x[158])
def l330_127(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + x[159])
def l330_128(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[100] + 1.0)
def l330_129(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[101] + 1.0)
def l330_130(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[102] + 1.0)
def l330_131(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[103] + 1.0)
def l330_132(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + 1.0)
def l330_133(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + 1.0)
def l330_134(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + 1.0)
def l330_135(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + 1.0)
def l330_136(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + 1.0)
def l330_137(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + 1.0)
def l330_138(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + 1.0)
def l330_139(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + 1.0)
def l330_140(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + 1.0)
def l330_141(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + 1.0)
def l330_142(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + 1.0)
def l330_143(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + 1.0)
def l330_144(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + 1.0)
def l330_145(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + 1.0)
def l330_146(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + 1.0)
def l330_147(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + 1.0)
def l330_148(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + 1.0)
def l330_149(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + 1.0)
def l330_150(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + 1.0)
def l330_151(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + 1.0)
def l330_152(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + 1.0)
def l330_153(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + 1.0)
def l330_154(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[126] + 1.0)
def l330_155(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[127] + 1.0)
def l330_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[128] + x[132] + -1.0)
def l330_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[129] + x[133] + -1.0)
def l330_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[130] + x[134] + -1.0)
def l330_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[131] + x[135] + -1.0)
def l330_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[132] + x[136] + -1.0)
def l330_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[133] + x[137] + -1.0)
def l330_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[134] + x[138] + -1.0)
def l330_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[135] + x[139] + -1.0)
def l330_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[136] + x[140] + -1.0)
def l330_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[137] + x[141] + -1.0)
def l330_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[138] + x[142] + -1.0)
def l330_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[139] + x[143] + -1.0)
def l330_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[140] + x[144] + -1.0)
def l330_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[141] + x[145] + -1.0)
def l330_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[142] + x[146] + -1.0)
def l330_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[143] + x[147] + -1.0)
def l330_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[144] + x[148] + -1.0)
def l330_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[145] + x[149] + -1.0)
def l330_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[146] + x[150] + -1.0)
def l330_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[147] + x[151] + -1.0)
def l330_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[148] + x[152] + -1.0)
def l330_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[149] + x[153] + -1.0)
def l330_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[150] + x[154] + -1.0)
def l330_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[151] + x[155] + -1.0)
def l330_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[152] + x[156] + -1.0)
def l330_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[153] + x[157] + -1.0)
def l330_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[154] + x[158] + -1.0)
def l330_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[155] + x[159] + -1.0)
def l330_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l330_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l330_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l330_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l330_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l330_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l330_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l330_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l330_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l330_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l330_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l330_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l330_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l330_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l330_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l330_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l330_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l330_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l330_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l330_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l330_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l330_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l330_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l330_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l330_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l330_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l330_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l330_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l330_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l330_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l330_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l330_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l330_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l330_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l330_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l330_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l330_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l330_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l330_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l330_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l330_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l330_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l330_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l330_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l330_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l330_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l330_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l330_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l330_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l330_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l330_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l330_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l330_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l330_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l330_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l330_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l330_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l330_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l330_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l330_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l330_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l330_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l330_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l330_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l330_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l330_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l330_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l330_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l330_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l330_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l330_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l330_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l330_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l330_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l330_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l330_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l330_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l330_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l330_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l330_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l330_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l330_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l330_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l330_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l330_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l330_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l330_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l330_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l330_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l330_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l330_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l330_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l330_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l330_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l330_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l330_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l330_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l330_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l330_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l330_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l330_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l330_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l330_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l330_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l330_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l330_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l330_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l330_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l330_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l330_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l330_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l330_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l330_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l330_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l330_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l330_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l330_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l330_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l330_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l330_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l330_304(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l330_305(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l330_306(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l330_307(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l330_308(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l330_309(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l330_310(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l330_311(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l330_312(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l330_313(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l330_314(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l330_315(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l330_(x):
    # x is a list (or vector) of length 288
    return [
        l330_0(x),
        l330_1(x),
        l330_2(x),
        l330_3(x),
        l330_4(x),
        l330_5(x),
        l330_6(x),
        l330_7(x),
        l330_8(x),
        l330_9(x),
        l330_10(x),
        l330_11(x),
        l330_12(x),
        l330_13(x),
        l330_14(x),
        l330_15(x),
        l330_16(x),
        l330_17(x),
        l330_18(x),
        l330_19(x),
        l330_20(x),
        l330_21(x),
        l330_22(x),
        l330_23(x),
        l330_24(x),
        l330_25(x),
        l330_26(x),
        l330_27(x),
        l330_28(x),
        l330_29(x),
        l330_30(x),
        l330_31(x),
        l330_32(x),
        l330_33(x),
        l330_34(x),
        l330_35(x),
        l330_36(x),
        l330_37(x),
        l330_38(x),
        l330_39(x),
        l330_40(x),
        l330_41(x),
        l330_42(x),
        l330_43(x),
        l330_44(x),
        l330_45(x),
        l330_46(x),
        l330_47(x),
        l330_48(x),
        l330_49(x),
        l330_50(x),
        l330_51(x),
        l330_52(x),
        l330_53(x),
        l330_54(x),
        l330_55(x),
        l330_56(x),
        l330_57(x),
        l330_58(x),
        l330_59(x),
        l330_60(x),
        l330_61(x),
        l330_62(x),
        l330_63(x),
        l330_64(x),
        l330_65(x),
        l330_66(x),
        l330_67(x),
        l330_68(x),
        l330_69(x),
        l330_70(x),
        l330_71(x),
        l330_72(x),
        l330_73(x),
        l330_74(x),
        l330_75(x),
        l330_76(x),
        l330_77(x),
        l330_78(x),
        l330_79(x),
        l330_80(x),
        l330_81(x),
        l330_82(x),
        l330_83(x),
        l330_84(x),
        l330_85(x),
        l330_86(x),
        l330_87(x),
        l330_88(x),
        l330_89(x),
        l330_90(x),
        l330_91(x),
        l330_92(x),
        l330_93(x),
        l330_94(x),
        l330_95(x),
        l330_96(x),
        l330_97(x),
        l330_98(x),
        l330_99(x),
        l330_100(x),
        l330_101(x),
        l330_102(x),
        l330_103(x),
        l330_104(x),
        l330_105(x),
        l330_106(x),
        l330_107(x),
        l330_108(x),
        l330_109(x),
        l330_110(x),
        l330_111(x),
        l330_112(x),
        l330_113(x),
        l330_114(x),
        l330_115(x),
        l330_116(x),
        l330_117(x),
        l330_118(x),
        l330_119(x),
        l330_120(x),
        l330_121(x),
        l330_122(x),
        l330_123(x),
        l330_124(x),
        l330_125(x),
        l330_126(x),
        l330_127(x),
        l330_128(x),
        l330_129(x),
        l330_130(x),
        l330_131(x),
        l330_132(x),
        l330_133(x),
        l330_134(x),
        l330_135(x),
        l330_136(x),
        l330_137(x),
        l330_138(x),
        l330_139(x),
        l330_140(x),
        l330_141(x),
        l330_142(x),
        l330_143(x),
        l330_144(x),
        l330_145(x),
        l330_146(x),
        l330_147(x),
        l330_148(x),
        l330_149(x),
        l330_150(x),
        l330_151(x),
        l330_152(x),
        l330_153(x),
        l330_154(x),
        l330_155(x),
        l330_156(x),
        l330_157(x),
        l330_158(x),
        l330_159(x),
        l330_160(x),
        l330_161(x),
        l330_162(x),
        l330_163(x),
        l330_164(x),
        l330_165(x),
        l330_166(x),
        l330_167(x),
        l330_168(x),
        l330_169(x),
        l330_170(x),
        l330_171(x),
        l330_172(x),
        l330_173(x),
        l330_174(x),
        l330_175(x),
        l330_176(x),
        l330_177(x),
        l330_178(x),
        l330_179(x),
        l330_180(x),
        l330_181(x),
        l330_182(x),
        l330_183(x),
        l330_184(x),
        l330_185(x),
        l330_186(x),
        l330_187(x),
        l330_188(x),
        l330_189(x),
        l330_190(x),
        l330_191(x),
        l330_192(x),
        l330_193(x),
        l330_194(x),
        l330_195(x),
        l330_196(x),
        l330_197(x),
        l330_198(x),
        l330_199(x),
        l330_200(x),
        l330_201(x),
        l330_202(x),
        l330_203(x),
        l330_204(x),
        l330_205(x),
        l330_206(x),
        l330_207(x),
        l330_208(x),
        l330_209(x),
        l330_210(x),
        l330_211(x),
        l330_212(x),
        l330_213(x),
        l330_214(x),
        l330_215(x),
        l330_216(x),
        l330_217(x),
        l330_218(x),
        l330_219(x),
        l330_220(x),
        l330_221(x),
        l330_222(x),
        l330_223(x),
        l330_224(x),
        l330_225(x),
        l330_226(x),
        l330_227(x),
        l330_228(x),
        l330_229(x),
        l330_230(x),
        l330_231(x),
        l330_232(x),
        l330_233(x),
        l330_234(x),
        l330_235(x),
        l330_236(x),
        l330_237(x),
        l330_238(x),
        l330_239(x),
        l330_240(x),
        l330_241(x),
        l330_242(x),
        l330_243(x),
        l330_244(x),
        l330_245(x),
        l330_246(x),
        l330_247(x),
        l330_248(x),
        l330_249(x),
        l330_250(x),
        l330_251(x),
        l330_252(x),
        l330_253(x),
        l330_254(x),
        l330_255(x),
        l330_256(x),
        l330_257(x),
        l330_258(x),
        l330_259(x),
        l330_260(x),
        l330_261(x),
        l330_262(x),
        l330_263(x),
        l330_264(x),
        l330_265(x),
        l330_266(x),
        l330_267(x),
        l330_268(x),
        l330_269(x),
        l330_270(x),
        l330_271(x),
        l330_272(x),
        l330_273(x),
        l330_274(x),
        l330_275(x),
        l330_276(x),
        l330_277(x),
        l330_278(x),
        l330_279(x),
        l330_280(x),
        l330_281(x),
        l330_282(x),
        l330_283(x),
        l330_284(x),
        l330_285(x),
        l330_286(x),
        l330_287(x),
        l330_288(x),
        l330_289(x),
        l330_290(x),
        l330_291(x),
        l330_292(x),
        l330_293(x),
        l330_294(x),
        l330_295(x),
        l330_296(x),
        l330_297(x),
        l330_298(x),
        l330_299(x),
        l330_300(x),
        l330_301(x),
        l330_302(x),
        l330_303(x),
        l330_304(x),
        l330_305(x),
        l330_306(x),
        l330_307(x),
        l330_308(x),
        l330_309(x),
        l330_310(x),
        l330_311(x),
        l330_312(x),
        l330_313(x),
        l330_314(x),
        l330_315(x),
    ]