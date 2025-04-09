import numpy as np




# Generated from reverse engineering
def l326_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 318
    out = np.empty(318, dtype=np.float32)
    
    # for i in range(0, 97):
    for i in range(0, 97):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x1 (len=1)
    biases = [1.0]
    # for i in range(97, 98):
    for i in range(0, 1):
        s = -1 * x[97 + i]
        s += biases[i]
        out[97 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0]
    # for i in range(98, 99):
    for i in range(0, 1):
        s = x[96 + i] + x[130 + i]
        s += biases[i]
        out[98 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(99, 128):
    for i in range(0, 29):
        s = x[131 + i] + -1 * x[97 + i]
        out[99 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3fffffff (len=30)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(128, 158):
    for i in range(0, 30):
        s = -1 * x[98 + i]
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(158, 188):
    for i in range(0, 30):
        s = x[128 + i] + x[130 + i]
        s += biases[i]
        out[158 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(188, 190):
    for i in range(0, 2):
        s = x[128 + i]
        out[188 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(190, 318):
    for i in range(0, 128):
        s = x[160 + i]
        out[190 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l326_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l326_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l326_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l326_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l326_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l326_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l326_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l326_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l326_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l326_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l326_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l326_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l326_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l326_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l326_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l326_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l326_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l326_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l326_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l326_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l326_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l326_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l326_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l326_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l326_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l326_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l326_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l326_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l326_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l326_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l326_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l326_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l326_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l326_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l326_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l326_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l326_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l326_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l326_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l326_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l326_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l326_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l326_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l326_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l326_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l326_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l326_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l326_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l326_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l326_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l326_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l326_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l326_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l326_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l326_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l326_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l326_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l326_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l326_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l326_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l326_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l326_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l326_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l326_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l326_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l326_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l326_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l326_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l326_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l326_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l326_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l326_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l326_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l326_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l326_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l326_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l326_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l326_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l326_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l326_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l326_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l326_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l326_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l326_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l326_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l326_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l326_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l326_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l326_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l326_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l326_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l326_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l326_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l326_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l326_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l326_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l326_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l326_97(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[97] + 1.0)
def l326_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + x[130] + -1.0)
def l326_99(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[97] + x[131])
def l326_100(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[98] + x[132])
def l326_101(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[99] + x[133])
def l326_102(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[100] + x[134])
def l326_103(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[101] + x[135])
def l326_104(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[102] + x[136])
def l326_105(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[103] + x[137])
def l326_106(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + x[138])
def l326_107(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + x[139])
def l326_108(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + x[140])
def l326_109(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + x[141])
def l326_110(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + x[142])
def l326_111(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + x[143])
def l326_112(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + x[144])
def l326_113(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + x[145])
def l326_114(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + x[146])
def l326_115(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + x[147])
def l326_116(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + x[148])
def l326_117(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + x[149])
def l326_118(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + x[150])
def l326_119(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + x[151])
def l326_120(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + x[152])
def l326_121(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + x[153])
def l326_122(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + x[154])
def l326_123(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + x[155])
def l326_124(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + x[156])
def l326_125(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + x[157])
def l326_126(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + x[158])
def l326_127(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + x[159])
def l326_128(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[98] + 1.0)
def l326_129(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[99] + 1.0)
def l326_130(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[100] + 1.0)
def l326_131(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[101] + 1.0)
def l326_132(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[102] + 1.0)
def l326_133(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[103] + 1.0)
def l326_134(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + 1.0)
def l326_135(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + 1.0)
def l326_136(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + 1.0)
def l326_137(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + 1.0)
def l326_138(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + 1.0)
def l326_139(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + 1.0)
def l326_140(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + 1.0)
def l326_141(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + 1.0)
def l326_142(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + 1.0)
def l326_143(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + 1.0)
def l326_144(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + 1.0)
def l326_145(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + 1.0)
def l326_146(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + 1.0)
def l326_147(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + 1.0)
def l326_148(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + 1.0)
def l326_149(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + 1.0)
def l326_150(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + 1.0)
def l326_151(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + 1.0)
def l326_152(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + 1.0)
def l326_153(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + 1.0)
def l326_154(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + 1.0)
def l326_155(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + 1.0)
def l326_156(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[126] + 1.0)
def l326_157(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[127] + 1.0)
def l326_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[128] + x[130] + -1.0)
def l326_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[129] + x[131] + -1.0)
def l326_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[130] + x[132] + -1.0)
def l326_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[131] + x[133] + -1.0)
def l326_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[132] + x[134] + -1.0)
def l326_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[133] + x[135] + -1.0)
def l326_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[134] + x[136] + -1.0)
def l326_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[135] + x[137] + -1.0)
def l326_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[136] + x[138] + -1.0)
def l326_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[137] + x[139] + -1.0)
def l326_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[138] + x[140] + -1.0)
def l326_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[139] + x[141] + -1.0)
def l326_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[140] + x[142] + -1.0)
def l326_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[141] + x[143] + -1.0)
def l326_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[142] + x[144] + -1.0)
def l326_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[143] + x[145] + -1.0)
def l326_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[144] + x[146] + -1.0)
def l326_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[145] + x[147] + -1.0)
def l326_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[146] + x[148] + -1.0)
def l326_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[147] + x[149] + -1.0)
def l326_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[148] + x[150] + -1.0)
def l326_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[149] + x[151] + -1.0)
def l326_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[150] + x[152] + -1.0)
def l326_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[151] + x[153] + -1.0)
def l326_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[152] + x[154] + -1.0)
def l326_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[153] + x[155] + -1.0)
def l326_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[154] + x[156] + -1.0)
def l326_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[155] + x[157] + -1.0)
def l326_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[156] + x[158] + -1.0)
def l326_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[157] + x[159] + -1.0)
def l326_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l326_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l326_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l326_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l326_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l326_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l326_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l326_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l326_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l326_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l326_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l326_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l326_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l326_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l326_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l326_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l326_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l326_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l326_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l326_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l326_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l326_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l326_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l326_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l326_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l326_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l326_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l326_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l326_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l326_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l326_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l326_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l326_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l326_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l326_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l326_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l326_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l326_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l326_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l326_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l326_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l326_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l326_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l326_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l326_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l326_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l326_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l326_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l326_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l326_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l326_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l326_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l326_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l326_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l326_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l326_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l326_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l326_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l326_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l326_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l326_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l326_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l326_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l326_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l326_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l326_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l326_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l326_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l326_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l326_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l326_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l326_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l326_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l326_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l326_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l326_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l326_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l326_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l326_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l326_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l326_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l326_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l326_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l326_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l326_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l326_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l326_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l326_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l326_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l326_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l326_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l326_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l326_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l326_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l326_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l326_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l326_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l326_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l326_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l326_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l326_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l326_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l326_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l326_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l326_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l326_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l326_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l326_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l326_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l326_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l326_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l326_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l326_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l326_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l326_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l326_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l326_304(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l326_305(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l326_306(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l326_307(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l326_308(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l326_309(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l326_310(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l326_311(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l326_312(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l326_313(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l326_314(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l326_315(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l326_316(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l326_317(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l326_(x):
    # x is a list (or vector) of length 288
    return [
        l326_0(x),
        l326_1(x),
        l326_2(x),
        l326_3(x),
        l326_4(x),
        l326_5(x),
        l326_6(x),
        l326_7(x),
        l326_8(x),
        l326_9(x),
        l326_10(x),
        l326_11(x),
        l326_12(x),
        l326_13(x),
        l326_14(x),
        l326_15(x),
        l326_16(x),
        l326_17(x),
        l326_18(x),
        l326_19(x),
        l326_20(x),
        l326_21(x),
        l326_22(x),
        l326_23(x),
        l326_24(x),
        l326_25(x),
        l326_26(x),
        l326_27(x),
        l326_28(x),
        l326_29(x),
        l326_30(x),
        l326_31(x),
        l326_32(x),
        l326_33(x),
        l326_34(x),
        l326_35(x),
        l326_36(x),
        l326_37(x),
        l326_38(x),
        l326_39(x),
        l326_40(x),
        l326_41(x),
        l326_42(x),
        l326_43(x),
        l326_44(x),
        l326_45(x),
        l326_46(x),
        l326_47(x),
        l326_48(x),
        l326_49(x),
        l326_50(x),
        l326_51(x),
        l326_52(x),
        l326_53(x),
        l326_54(x),
        l326_55(x),
        l326_56(x),
        l326_57(x),
        l326_58(x),
        l326_59(x),
        l326_60(x),
        l326_61(x),
        l326_62(x),
        l326_63(x),
        l326_64(x),
        l326_65(x),
        l326_66(x),
        l326_67(x),
        l326_68(x),
        l326_69(x),
        l326_70(x),
        l326_71(x),
        l326_72(x),
        l326_73(x),
        l326_74(x),
        l326_75(x),
        l326_76(x),
        l326_77(x),
        l326_78(x),
        l326_79(x),
        l326_80(x),
        l326_81(x),
        l326_82(x),
        l326_83(x),
        l326_84(x),
        l326_85(x),
        l326_86(x),
        l326_87(x),
        l326_88(x),
        l326_89(x),
        l326_90(x),
        l326_91(x),
        l326_92(x),
        l326_93(x),
        l326_94(x),
        l326_95(x),
        l326_96(x),
        l326_97(x),
        l326_98(x),
        l326_99(x),
        l326_100(x),
        l326_101(x),
        l326_102(x),
        l326_103(x),
        l326_104(x),
        l326_105(x),
        l326_106(x),
        l326_107(x),
        l326_108(x),
        l326_109(x),
        l326_110(x),
        l326_111(x),
        l326_112(x),
        l326_113(x),
        l326_114(x),
        l326_115(x),
        l326_116(x),
        l326_117(x),
        l326_118(x),
        l326_119(x),
        l326_120(x),
        l326_121(x),
        l326_122(x),
        l326_123(x),
        l326_124(x),
        l326_125(x),
        l326_126(x),
        l326_127(x),
        l326_128(x),
        l326_129(x),
        l326_130(x),
        l326_131(x),
        l326_132(x),
        l326_133(x),
        l326_134(x),
        l326_135(x),
        l326_136(x),
        l326_137(x),
        l326_138(x),
        l326_139(x),
        l326_140(x),
        l326_141(x),
        l326_142(x),
        l326_143(x),
        l326_144(x),
        l326_145(x),
        l326_146(x),
        l326_147(x),
        l326_148(x),
        l326_149(x),
        l326_150(x),
        l326_151(x),
        l326_152(x),
        l326_153(x),
        l326_154(x),
        l326_155(x),
        l326_156(x),
        l326_157(x),
        l326_158(x),
        l326_159(x),
        l326_160(x),
        l326_161(x),
        l326_162(x),
        l326_163(x),
        l326_164(x),
        l326_165(x),
        l326_166(x),
        l326_167(x),
        l326_168(x),
        l326_169(x),
        l326_170(x),
        l326_171(x),
        l326_172(x),
        l326_173(x),
        l326_174(x),
        l326_175(x),
        l326_176(x),
        l326_177(x),
        l326_178(x),
        l326_179(x),
        l326_180(x),
        l326_181(x),
        l326_182(x),
        l326_183(x),
        l326_184(x),
        l326_185(x),
        l326_186(x),
        l326_187(x),
        l326_188(x),
        l326_189(x),
        l326_190(x),
        l326_191(x),
        l326_192(x),
        l326_193(x),
        l326_194(x),
        l326_195(x),
        l326_196(x),
        l326_197(x),
        l326_198(x),
        l326_199(x),
        l326_200(x),
        l326_201(x),
        l326_202(x),
        l326_203(x),
        l326_204(x),
        l326_205(x),
        l326_206(x),
        l326_207(x),
        l326_208(x),
        l326_209(x),
        l326_210(x),
        l326_211(x),
        l326_212(x),
        l326_213(x),
        l326_214(x),
        l326_215(x),
        l326_216(x),
        l326_217(x),
        l326_218(x),
        l326_219(x),
        l326_220(x),
        l326_221(x),
        l326_222(x),
        l326_223(x),
        l326_224(x),
        l326_225(x),
        l326_226(x),
        l326_227(x),
        l326_228(x),
        l326_229(x),
        l326_230(x),
        l326_231(x),
        l326_232(x),
        l326_233(x),
        l326_234(x),
        l326_235(x),
        l326_236(x),
        l326_237(x),
        l326_238(x),
        l326_239(x),
        l326_240(x),
        l326_241(x),
        l326_242(x),
        l326_243(x),
        l326_244(x),
        l326_245(x),
        l326_246(x),
        l326_247(x),
        l326_248(x),
        l326_249(x),
        l326_250(x),
        l326_251(x),
        l326_252(x),
        l326_253(x),
        l326_254(x),
        l326_255(x),
        l326_256(x),
        l326_257(x),
        l326_258(x),
        l326_259(x),
        l326_260(x),
        l326_261(x),
        l326_262(x),
        l326_263(x),
        l326_264(x),
        l326_265(x),
        l326_266(x),
        l326_267(x),
        l326_268(x),
        l326_269(x),
        l326_270(x),
        l326_271(x),
        l326_272(x),
        l326_273(x),
        l326_274(x),
        l326_275(x),
        l326_276(x),
        l326_277(x),
        l326_278(x),
        l326_279(x),
        l326_280(x),
        l326_281(x),
        l326_282(x),
        l326_283(x),
        l326_284(x),
        l326_285(x),
        l326_286(x),
        l326_287(x),
        l326_288(x),
        l326_289(x),
        l326_290(x),
        l326_291(x),
        l326_292(x),
        l326_293(x),
        l326_294(x),
        l326_295(x),
        l326_296(x),
        l326_297(x),
        l326_298(x),
        l326_299(x),
        l326_300(x),
        l326_301(x),
        l326_302(x),
        l326_303(x),
        l326_304(x),
        l326_305(x),
        l326_306(x),
        l326_307(x),
        l326_308(x),
        l326_309(x),
        l326_310(x),
        l326_311(x),
        l326_312(x),
        l326_313(x),
        l326_314(x),
        l326_315(x),
        l326_316(x),
        l326_317(x),
    ]