import numpy as np




# Generated from reverse engineering
def l254_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 304
    out = np.empty(304, dtype=np.float32)
    
    # for i in range(0, 104):
    for i in range(0, 104):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xff (len=8)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(104, 112):
    for i in range(0, 8):
        s = -1 * x[104 + i]
        s += biases[i]
        out[104 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(112, 120):
    for i in range(0, 8):
        s = x[96 + i] + x[144 + i]
        s += biases[i]
        out[112 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(120, 128):
    for i in range(0, 8):
        s = x[152 + i] + -1 * x[104 + i]
        out[120 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffff (len=16)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(128, 144):
    for i in range(0, 16):
        s = -1 * x[112 + i]
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(144, 160):
    for i in range(0, 16):
        s = x[128 + i] + x[144 + i]
        s += biases[i]
        out[144 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 176):
    for i in range(0, 16):
        s = x[128 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(176, 304):
    for i in range(0, 128):
        s = x[160 + i]
        out[176 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l254_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l254_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l254_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l254_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l254_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l254_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l254_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l254_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l254_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l254_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l254_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l254_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l254_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l254_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l254_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l254_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l254_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l254_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l254_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l254_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l254_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l254_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l254_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l254_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l254_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l254_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l254_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l254_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l254_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l254_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l254_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l254_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l254_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l254_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l254_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l254_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l254_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l254_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l254_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l254_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l254_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l254_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l254_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l254_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l254_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l254_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l254_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l254_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l254_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l254_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l254_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l254_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l254_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l254_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l254_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l254_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l254_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l254_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l254_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l254_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l254_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l254_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l254_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l254_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l254_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l254_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l254_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l254_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l254_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l254_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l254_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l254_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l254_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l254_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l254_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l254_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l254_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l254_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l254_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l254_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l254_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l254_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l254_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l254_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l254_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l254_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l254_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l254_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l254_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l254_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l254_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l254_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l254_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l254_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l254_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l254_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l254_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l254_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l254_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l254_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l254_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[100])
def l254_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[101])
def l254_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[102])
def l254_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[103])
def l254_104(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + 1.0)
def l254_105(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + 1.0)
def l254_106(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + 1.0)
def l254_107(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + 1.0)
def l254_108(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + 1.0)
def l254_109(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + 1.0)
def l254_110(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + 1.0)
def l254_111(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + 1.0)
def l254_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + x[144] + -1.0)
def l254_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + x[145] + -1.0)
def l254_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + x[146] + -1.0)
def l254_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + x[147] + -1.0)
def l254_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + x[148] + -1.0)
def l254_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + x[149] + -1.0)
def l254_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + x[150] + -1.0)
def l254_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + x[151] + -1.0)
def l254_120(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + x[152])
def l254_121(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + x[153])
def l254_122(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + x[154])
def l254_123(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + x[155])
def l254_124(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + x[156])
def l254_125(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + x[157])
def l254_126(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + x[158])
def l254_127(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + x[159])
def l254_128(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + 1.0)
def l254_129(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + 1.0)
def l254_130(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + 1.0)
def l254_131(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + 1.0)
def l254_132(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + 1.0)
def l254_133(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + 1.0)
def l254_134(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + 1.0)
def l254_135(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + 1.0)
def l254_136(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + 1.0)
def l254_137(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + 1.0)
def l254_138(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + 1.0)
def l254_139(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + 1.0)
def l254_140(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + 1.0)
def l254_141(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + 1.0)
def l254_142(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[126] + 1.0)
def l254_143(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[127] + 1.0)
def l254_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[128] + x[144] + -1.0)
def l254_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[129] + x[145] + -1.0)
def l254_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[130] + x[146] + -1.0)
def l254_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[131] + x[147] + -1.0)
def l254_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[132] + x[148] + -1.0)
def l254_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[133] + x[149] + -1.0)
def l254_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[134] + x[150] + -1.0)
def l254_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[135] + x[151] + -1.0)
def l254_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[136] + x[152] + -1.0)
def l254_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[137] + x[153] + -1.0)
def l254_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[138] + x[154] + -1.0)
def l254_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[139] + x[155] + -1.0)
def l254_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[140] + x[156] + -1.0)
def l254_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[141] + x[157] + -1.0)
def l254_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[142] + x[158] + -1.0)
def l254_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[143] + x[159] + -1.0)
def l254_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l254_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l254_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l254_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l254_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l254_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l254_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l254_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l254_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l254_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l254_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l254_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l254_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l254_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l254_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l254_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l254_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l254_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l254_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l254_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l254_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l254_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l254_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l254_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l254_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l254_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l254_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l254_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l254_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l254_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l254_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l254_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l254_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l254_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l254_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l254_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l254_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l254_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l254_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l254_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l254_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l254_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l254_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l254_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l254_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l254_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l254_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l254_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l254_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l254_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l254_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l254_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l254_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l254_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l254_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l254_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l254_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l254_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l254_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l254_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l254_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l254_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l254_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l254_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l254_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l254_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l254_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l254_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l254_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l254_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l254_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l254_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l254_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l254_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l254_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l254_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l254_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l254_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l254_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l254_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l254_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l254_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l254_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l254_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l254_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l254_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l254_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l254_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l254_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l254_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l254_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l254_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l254_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l254_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l254_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l254_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l254_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l254_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l254_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l254_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l254_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l254_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l254_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l254_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l254_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l254_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l254_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l254_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l254_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l254_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l254_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l254_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l254_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l254_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l254_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l254_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l254_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l254_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l254_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l254_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l254_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l254_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l254_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l254_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l254_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l254_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l254_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l254_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l254_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l254_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l254_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l254_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l254_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l254_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l254_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l254_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l254_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l254_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l254_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l254_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l254_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l254_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l254_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l254_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l254_(x):
    # x is a list (or vector) of length 288
    return [
        l254_0(x),
        l254_1(x),
        l254_2(x),
        l254_3(x),
        l254_4(x),
        l254_5(x),
        l254_6(x),
        l254_7(x),
        l254_8(x),
        l254_9(x),
        l254_10(x),
        l254_11(x),
        l254_12(x),
        l254_13(x),
        l254_14(x),
        l254_15(x),
        l254_16(x),
        l254_17(x),
        l254_18(x),
        l254_19(x),
        l254_20(x),
        l254_21(x),
        l254_22(x),
        l254_23(x),
        l254_24(x),
        l254_25(x),
        l254_26(x),
        l254_27(x),
        l254_28(x),
        l254_29(x),
        l254_30(x),
        l254_31(x),
        l254_32(x),
        l254_33(x),
        l254_34(x),
        l254_35(x),
        l254_36(x),
        l254_37(x),
        l254_38(x),
        l254_39(x),
        l254_40(x),
        l254_41(x),
        l254_42(x),
        l254_43(x),
        l254_44(x),
        l254_45(x),
        l254_46(x),
        l254_47(x),
        l254_48(x),
        l254_49(x),
        l254_50(x),
        l254_51(x),
        l254_52(x),
        l254_53(x),
        l254_54(x),
        l254_55(x),
        l254_56(x),
        l254_57(x),
        l254_58(x),
        l254_59(x),
        l254_60(x),
        l254_61(x),
        l254_62(x),
        l254_63(x),
        l254_64(x),
        l254_65(x),
        l254_66(x),
        l254_67(x),
        l254_68(x),
        l254_69(x),
        l254_70(x),
        l254_71(x),
        l254_72(x),
        l254_73(x),
        l254_74(x),
        l254_75(x),
        l254_76(x),
        l254_77(x),
        l254_78(x),
        l254_79(x),
        l254_80(x),
        l254_81(x),
        l254_82(x),
        l254_83(x),
        l254_84(x),
        l254_85(x),
        l254_86(x),
        l254_87(x),
        l254_88(x),
        l254_89(x),
        l254_90(x),
        l254_91(x),
        l254_92(x),
        l254_93(x),
        l254_94(x),
        l254_95(x),
        l254_96(x),
        l254_97(x),
        l254_98(x),
        l254_99(x),
        l254_100(x),
        l254_101(x),
        l254_102(x),
        l254_103(x),
        l254_104(x),
        l254_105(x),
        l254_106(x),
        l254_107(x),
        l254_108(x),
        l254_109(x),
        l254_110(x),
        l254_111(x),
        l254_112(x),
        l254_113(x),
        l254_114(x),
        l254_115(x),
        l254_116(x),
        l254_117(x),
        l254_118(x),
        l254_119(x),
        l254_120(x),
        l254_121(x),
        l254_122(x),
        l254_123(x),
        l254_124(x),
        l254_125(x),
        l254_126(x),
        l254_127(x),
        l254_128(x),
        l254_129(x),
        l254_130(x),
        l254_131(x),
        l254_132(x),
        l254_133(x),
        l254_134(x),
        l254_135(x),
        l254_136(x),
        l254_137(x),
        l254_138(x),
        l254_139(x),
        l254_140(x),
        l254_141(x),
        l254_142(x),
        l254_143(x),
        l254_144(x),
        l254_145(x),
        l254_146(x),
        l254_147(x),
        l254_148(x),
        l254_149(x),
        l254_150(x),
        l254_151(x),
        l254_152(x),
        l254_153(x),
        l254_154(x),
        l254_155(x),
        l254_156(x),
        l254_157(x),
        l254_158(x),
        l254_159(x),
        l254_160(x),
        l254_161(x),
        l254_162(x),
        l254_163(x),
        l254_164(x),
        l254_165(x),
        l254_166(x),
        l254_167(x),
        l254_168(x),
        l254_169(x),
        l254_170(x),
        l254_171(x),
        l254_172(x),
        l254_173(x),
        l254_174(x),
        l254_175(x),
        l254_176(x),
        l254_177(x),
        l254_178(x),
        l254_179(x),
        l254_180(x),
        l254_181(x),
        l254_182(x),
        l254_183(x),
        l254_184(x),
        l254_185(x),
        l254_186(x),
        l254_187(x),
        l254_188(x),
        l254_189(x),
        l254_190(x),
        l254_191(x),
        l254_192(x),
        l254_193(x),
        l254_194(x),
        l254_195(x),
        l254_196(x),
        l254_197(x),
        l254_198(x),
        l254_199(x),
        l254_200(x),
        l254_201(x),
        l254_202(x),
        l254_203(x),
        l254_204(x),
        l254_205(x),
        l254_206(x),
        l254_207(x),
        l254_208(x),
        l254_209(x),
        l254_210(x),
        l254_211(x),
        l254_212(x),
        l254_213(x),
        l254_214(x),
        l254_215(x),
        l254_216(x),
        l254_217(x),
        l254_218(x),
        l254_219(x),
        l254_220(x),
        l254_221(x),
        l254_222(x),
        l254_223(x),
        l254_224(x),
        l254_225(x),
        l254_226(x),
        l254_227(x),
        l254_228(x),
        l254_229(x),
        l254_230(x),
        l254_231(x),
        l254_232(x),
        l254_233(x),
        l254_234(x),
        l254_235(x),
        l254_236(x),
        l254_237(x),
        l254_238(x),
        l254_239(x),
        l254_240(x),
        l254_241(x),
        l254_242(x),
        l254_243(x),
        l254_244(x),
        l254_245(x),
        l254_246(x),
        l254_247(x),
        l254_248(x),
        l254_249(x),
        l254_250(x),
        l254_251(x),
        l254_252(x),
        l254_253(x),
        l254_254(x),
        l254_255(x),
        l254_256(x),
        l254_257(x),
        l254_258(x),
        l254_259(x),
        l254_260(x),
        l254_261(x),
        l254_262(x),
        l254_263(x),
        l254_264(x),
        l254_265(x),
        l254_266(x),
        l254_267(x),
        l254_268(x),
        l254_269(x),
        l254_270(x),
        l254_271(x),
        l254_272(x),
        l254_273(x),
        l254_274(x),
        l254_275(x),
        l254_276(x),
        l254_277(x),
        l254_278(x),
        l254_279(x),
        l254_280(x),
        l254_281(x),
        l254_282(x),
        l254_283(x),
        l254_284(x),
        l254_285(x),
        l254_286(x),
        l254_287(x),
        l254_288(x),
        l254_289(x),
        l254_290(x),
        l254_291(x),
        l254_292(x),
        l254_293(x),
        l254_294(x),
        l254_295(x),
        l254_296(x),
        l254_297(x),
        l254_298(x),
        l254_299(x),
        l254_300(x),
        l254_301(x),
        l254_302(x),
        l254_303(x),
    ]