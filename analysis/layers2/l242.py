import numpy as np




# Generated from reverse engineering
def l242_g(x: np.ndarray) -> np.ndarray:
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




def l242_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l242_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l242_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l242_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l242_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l242_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l242_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l242_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l242_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l242_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l242_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l242_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l242_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l242_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l242_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l242_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l242_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l242_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l242_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l242_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l242_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l242_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l242_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l242_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l242_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l242_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l242_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l242_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l242_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l242_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l242_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l242_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l242_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l242_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l242_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l242_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l242_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l242_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l242_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l242_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l242_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l242_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l242_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l242_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l242_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l242_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l242_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l242_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l242_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l242_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l242_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l242_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l242_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l242_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l242_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l242_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l242_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l242_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l242_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l242_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l242_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l242_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l242_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l242_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l242_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l242_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l242_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l242_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l242_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l242_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l242_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l242_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l242_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l242_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l242_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l242_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l242_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l242_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l242_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l242_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l242_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l242_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l242_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l242_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l242_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l242_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l242_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l242_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l242_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l242_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l242_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l242_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l242_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l242_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l242_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l242_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l242_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l242_97(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[97] + 1.0)
def l242_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + x[130] + -1.0)
def l242_99(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[97] + x[131])
def l242_100(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[98] + x[132])
def l242_101(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[99] + x[133])
def l242_102(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[100] + x[134])
def l242_103(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[101] + x[135])
def l242_104(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[102] + x[136])
def l242_105(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[103] + x[137])
def l242_106(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + x[138])
def l242_107(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + x[139])
def l242_108(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + x[140])
def l242_109(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + x[141])
def l242_110(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + x[142])
def l242_111(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + x[143])
def l242_112(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + x[144])
def l242_113(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + x[145])
def l242_114(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + x[146])
def l242_115(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + x[147])
def l242_116(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + x[148])
def l242_117(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + x[149])
def l242_118(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + x[150])
def l242_119(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + x[151])
def l242_120(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + x[152])
def l242_121(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + x[153])
def l242_122(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + x[154])
def l242_123(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + x[155])
def l242_124(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + x[156])
def l242_125(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + x[157])
def l242_126(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + x[158])
def l242_127(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + x[159])
def l242_128(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[98] + 1.0)
def l242_129(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[99] + 1.0)
def l242_130(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[100] + 1.0)
def l242_131(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[101] + 1.0)
def l242_132(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[102] + 1.0)
def l242_133(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[103] + 1.0)
def l242_134(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + 1.0)
def l242_135(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + 1.0)
def l242_136(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + 1.0)
def l242_137(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + 1.0)
def l242_138(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + 1.0)
def l242_139(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + 1.0)
def l242_140(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + 1.0)
def l242_141(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + 1.0)
def l242_142(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + 1.0)
def l242_143(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + 1.0)
def l242_144(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + 1.0)
def l242_145(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + 1.0)
def l242_146(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + 1.0)
def l242_147(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + 1.0)
def l242_148(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + 1.0)
def l242_149(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + 1.0)
def l242_150(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + 1.0)
def l242_151(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + 1.0)
def l242_152(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + 1.0)
def l242_153(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + 1.0)
def l242_154(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + 1.0)
def l242_155(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + 1.0)
def l242_156(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[126] + 1.0)
def l242_157(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[127] + 1.0)
def l242_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[128] + x[130] + -1.0)
def l242_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[129] + x[131] + -1.0)
def l242_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[130] + x[132] + -1.0)
def l242_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[131] + x[133] + -1.0)
def l242_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[132] + x[134] + -1.0)
def l242_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[133] + x[135] + -1.0)
def l242_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[134] + x[136] + -1.0)
def l242_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[135] + x[137] + -1.0)
def l242_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[136] + x[138] + -1.0)
def l242_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[137] + x[139] + -1.0)
def l242_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[138] + x[140] + -1.0)
def l242_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[139] + x[141] + -1.0)
def l242_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[140] + x[142] + -1.0)
def l242_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[141] + x[143] + -1.0)
def l242_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[142] + x[144] + -1.0)
def l242_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[143] + x[145] + -1.0)
def l242_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[144] + x[146] + -1.0)
def l242_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[145] + x[147] + -1.0)
def l242_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[146] + x[148] + -1.0)
def l242_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[147] + x[149] + -1.0)
def l242_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[148] + x[150] + -1.0)
def l242_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[149] + x[151] + -1.0)
def l242_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[150] + x[152] + -1.0)
def l242_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[151] + x[153] + -1.0)
def l242_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[152] + x[154] + -1.0)
def l242_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[153] + x[155] + -1.0)
def l242_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[154] + x[156] + -1.0)
def l242_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[155] + x[157] + -1.0)
def l242_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[156] + x[158] + -1.0)
def l242_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[157] + x[159] + -1.0)
def l242_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l242_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l242_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l242_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l242_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l242_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l242_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l242_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l242_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l242_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l242_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l242_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l242_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l242_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l242_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l242_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l242_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l242_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l242_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l242_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l242_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l242_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l242_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l242_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l242_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l242_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l242_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l242_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l242_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l242_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l242_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l242_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l242_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l242_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l242_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l242_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l242_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l242_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l242_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l242_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l242_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l242_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l242_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l242_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l242_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l242_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l242_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l242_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l242_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l242_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l242_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l242_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l242_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l242_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l242_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l242_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l242_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l242_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l242_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l242_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l242_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l242_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l242_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l242_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l242_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l242_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l242_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l242_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l242_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l242_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l242_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l242_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l242_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l242_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l242_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l242_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l242_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l242_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l242_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l242_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l242_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l242_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l242_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l242_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l242_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l242_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l242_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l242_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l242_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l242_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l242_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l242_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l242_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l242_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l242_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l242_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l242_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l242_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l242_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l242_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l242_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l242_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l242_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l242_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l242_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l242_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l242_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l242_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l242_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l242_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l242_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l242_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l242_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l242_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l242_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l242_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l242_304(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l242_305(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l242_306(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l242_307(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l242_308(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l242_309(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l242_310(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l242_311(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l242_312(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l242_313(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l242_314(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l242_315(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l242_316(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l242_317(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l242_(x):
    # x is a list (or vector) of length 288
    return [
        l242_0(x),
        l242_1(x),
        l242_2(x),
        l242_3(x),
        l242_4(x),
        l242_5(x),
        l242_6(x),
        l242_7(x),
        l242_8(x),
        l242_9(x),
        l242_10(x),
        l242_11(x),
        l242_12(x),
        l242_13(x),
        l242_14(x),
        l242_15(x),
        l242_16(x),
        l242_17(x),
        l242_18(x),
        l242_19(x),
        l242_20(x),
        l242_21(x),
        l242_22(x),
        l242_23(x),
        l242_24(x),
        l242_25(x),
        l242_26(x),
        l242_27(x),
        l242_28(x),
        l242_29(x),
        l242_30(x),
        l242_31(x),
        l242_32(x),
        l242_33(x),
        l242_34(x),
        l242_35(x),
        l242_36(x),
        l242_37(x),
        l242_38(x),
        l242_39(x),
        l242_40(x),
        l242_41(x),
        l242_42(x),
        l242_43(x),
        l242_44(x),
        l242_45(x),
        l242_46(x),
        l242_47(x),
        l242_48(x),
        l242_49(x),
        l242_50(x),
        l242_51(x),
        l242_52(x),
        l242_53(x),
        l242_54(x),
        l242_55(x),
        l242_56(x),
        l242_57(x),
        l242_58(x),
        l242_59(x),
        l242_60(x),
        l242_61(x),
        l242_62(x),
        l242_63(x),
        l242_64(x),
        l242_65(x),
        l242_66(x),
        l242_67(x),
        l242_68(x),
        l242_69(x),
        l242_70(x),
        l242_71(x),
        l242_72(x),
        l242_73(x),
        l242_74(x),
        l242_75(x),
        l242_76(x),
        l242_77(x),
        l242_78(x),
        l242_79(x),
        l242_80(x),
        l242_81(x),
        l242_82(x),
        l242_83(x),
        l242_84(x),
        l242_85(x),
        l242_86(x),
        l242_87(x),
        l242_88(x),
        l242_89(x),
        l242_90(x),
        l242_91(x),
        l242_92(x),
        l242_93(x),
        l242_94(x),
        l242_95(x),
        l242_96(x),
        l242_97(x),
        l242_98(x),
        l242_99(x),
        l242_100(x),
        l242_101(x),
        l242_102(x),
        l242_103(x),
        l242_104(x),
        l242_105(x),
        l242_106(x),
        l242_107(x),
        l242_108(x),
        l242_109(x),
        l242_110(x),
        l242_111(x),
        l242_112(x),
        l242_113(x),
        l242_114(x),
        l242_115(x),
        l242_116(x),
        l242_117(x),
        l242_118(x),
        l242_119(x),
        l242_120(x),
        l242_121(x),
        l242_122(x),
        l242_123(x),
        l242_124(x),
        l242_125(x),
        l242_126(x),
        l242_127(x),
        l242_128(x),
        l242_129(x),
        l242_130(x),
        l242_131(x),
        l242_132(x),
        l242_133(x),
        l242_134(x),
        l242_135(x),
        l242_136(x),
        l242_137(x),
        l242_138(x),
        l242_139(x),
        l242_140(x),
        l242_141(x),
        l242_142(x),
        l242_143(x),
        l242_144(x),
        l242_145(x),
        l242_146(x),
        l242_147(x),
        l242_148(x),
        l242_149(x),
        l242_150(x),
        l242_151(x),
        l242_152(x),
        l242_153(x),
        l242_154(x),
        l242_155(x),
        l242_156(x),
        l242_157(x),
        l242_158(x),
        l242_159(x),
        l242_160(x),
        l242_161(x),
        l242_162(x),
        l242_163(x),
        l242_164(x),
        l242_165(x),
        l242_166(x),
        l242_167(x),
        l242_168(x),
        l242_169(x),
        l242_170(x),
        l242_171(x),
        l242_172(x),
        l242_173(x),
        l242_174(x),
        l242_175(x),
        l242_176(x),
        l242_177(x),
        l242_178(x),
        l242_179(x),
        l242_180(x),
        l242_181(x),
        l242_182(x),
        l242_183(x),
        l242_184(x),
        l242_185(x),
        l242_186(x),
        l242_187(x),
        l242_188(x),
        l242_189(x),
        l242_190(x),
        l242_191(x),
        l242_192(x),
        l242_193(x),
        l242_194(x),
        l242_195(x),
        l242_196(x),
        l242_197(x),
        l242_198(x),
        l242_199(x),
        l242_200(x),
        l242_201(x),
        l242_202(x),
        l242_203(x),
        l242_204(x),
        l242_205(x),
        l242_206(x),
        l242_207(x),
        l242_208(x),
        l242_209(x),
        l242_210(x),
        l242_211(x),
        l242_212(x),
        l242_213(x),
        l242_214(x),
        l242_215(x),
        l242_216(x),
        l242_217(x),
        l242_218(x),
        l242_219(x),
        l242_220(x),
        l242_221(x),
        l242_222(x),
        l242_223(x),
        l242_224(x),
        l242_225(x),
        l242_226(x),
        l242_227(x),
        l242_228(x),
        l242_229(x),
        l242_230(x),
        l242_231(x),
        l242_232(x),
        l242_233(x),
        l242_234(x),
        l242_235(x),
        l242_236(x),
        l242_237(x),
        l242_238(x),
        l242_239(x),
        l242_240(x),
        l242_241(x),
        l242_242(x),
        l242_243(x),
        l242_244(x),
        l242_245(x),
        l242_246(x),
        l242_247(x),
        l242_248(x),
        l242_249(x),
        l242_250(x),
        l242_251(x),
        l242_252(x),
        l242_253(x),
        l242_254(x),
        l242_255(x),
        l242_256(x),
        l242_257(x),
        l242_258(x),
        l242_259(x),
        l242_260(x),
        l242_261(x),
        l242_262(x),
        l242_263(x),
        l242_264(x),
        l242_265(x),
        l242_266(x),
        l242_267(x),
        l242_268(x),
        l242_269(x),
        l242_270(x),
        l242_271(x),
        l242_272(x),
        l242_273(x),
        l242_274(x),
        l242_275(x),
        l242_276(x),
        l242_277(x),
        l242_278(x),
        l242_279(x),
        l242_280(x),
        l242_281(x),
        l242_282(x),
        l242_283(x),
        l242_284(x),
        l242_285(x),
        l242_286(x),
        l242_287(x),
        l242_288(x),
        l242_289(x),
        l242_290(x),
        l242_291(x),
        l242_292(x),
        l242_293(x),
        l242_294(x),
        l242_295(x),
        l242_296(x),
        l242_297(x),
        l242_298(x),
        l242_299(x),
        l242_300(x),
        l242_301(x),
        l242_302(x),
        l242_303(x),
        l242_304(x),
        l242_305(x),
        l242_306(x),
        l242_307(x),
        l242_308(x),
        l242_309(x),
        l242_310(x),
        l242_311(x),
        l242_312(x),
        l242_313(x),
        l242_314(x),
        l242_315(x),
        l242_316(x),
        l242_317(x),
    ]