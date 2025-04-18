import numpy as np




# Generated from reverse engineering
def l422_g(x: np.ndarray) -> np.ndarray:
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




def l422_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l422_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l422_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l422_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l422_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l422_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l422_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l422_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l422_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l422_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l422_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l422_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l422_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l422_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l422_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l422_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l422_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l422_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l422_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l422_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l422_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l422_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l422_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l422_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l422_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l422_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l422_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l422_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l422_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l422_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l422_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l422_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l422_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l422_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l422_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l422_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l422_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l422_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l422_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l422_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l422_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l422_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l422_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l422_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l422_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l422_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l422_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l422_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l422_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l422_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l422_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l422_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l422_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l422_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l422_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l422_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l422_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l422_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l422_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l422_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l422_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l422_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l422_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l422_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l422_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l422_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l422_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l422_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l422_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l422_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l422_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l422_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l422_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l422_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l422_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l422_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l422_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l422_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l422_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l422_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l422_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l422_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l422_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l422_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l422_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l422_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l422_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l422_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l422_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l422_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l422_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l422_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l422_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l422_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l422_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l422_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l422_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l422_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l422_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l422_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l422_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[100])
def l422_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[101])
def l422_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[102])
def l422_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[103])
def l422_104(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + 1.0)
def l422_105(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + 1.0)
def l422_106(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + 1.0)
def l422_107(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + 1.0)
def l422_108(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + 1.0)
def l422_109(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + 1.0)
def l422_110(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + 1.0)
def l422_111(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + 1.0)
def l422_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + x[144] + -1.0)
def l422_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + x[145] + -1.0)
def l422_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + x[146] + -1.0)
def l422_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + x[147] + -1.0)
def l422_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + x[148] + -1.0)
def l422_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + x[149] + -1.0)
def l422_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + x[150] + -1.0)
def l422_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + x[151] + -1.0)
def l422_120(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + x[152])
def l422_121(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + x[153])
def l422_122(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + x[154])
def l422_123(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + x[155])
def l422_124(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + x[156])
def l422_125(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + x[157])
def l422_126(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + x[158])
def l422_127(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + x[159])
def l422_128(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + 1.0)
def l422_129(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + 1.0)
def l422_130(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + 1.0)
def l422_131(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + 1.0)
def l422_132(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + 1.0)
def l422_133(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + 1.0)
def l422_134(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + 1.0)
def l422_135(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + 1.0)
def l422_136(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + 1.0)
def l422_137(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + 1.0)
def l422_138(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + 1.0)
def l422_139(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + 1.0)
def l422_140(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + 1.0)
def l422_141(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + 1.0)
def l422_142(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[126] + 1.0)
def l422_143(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[127] + 1.0)
def l422_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[128] + x[144] + -1.0)
def l422_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[129] + x[145] + -1.0)
def l422_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[130] + x[146] + -1.0)
def l422_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[131] + x[147] + -1.0)
def l422_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[132] + x[148] + -1.0)
def l422_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[133] + x[149] + -1.0)
def l422_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[134] + x[150] + -1.0)
def l422_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[135] + x[151] + -1.0)
def l422_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[136] + x[152] + -1.0)
def l422_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[137] + x[153] + -1.0)
def l422_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[138] + x[154] + -1.0)
def l422_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[139] + x[155] + -1.0)
def l422_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[140] + x[156] + -1.0)
def l422_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[141] + x[157] + -1.0)
def l422_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[142] + x[158] + -1.0)
def l422_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[143] + x[159] + -1.0)
def l422_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l422_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l422_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l422_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l422_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l422_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l422_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l422_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l422_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l422_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l422_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l422_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l422_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l422_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l422_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l422_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l422_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l422_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l422_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l422_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l422_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l422_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l422_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l422_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l422_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l422_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l422_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l422_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l422_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l422_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l422_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l422_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l422_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l422_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l422_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l422_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l422_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l422_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l422_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l422_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l422_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l422_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l422_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l422_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l422_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l422_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l422_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l422_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l422_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l422_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l422_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l422_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l422_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l422_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l422_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l422_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l422_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l422_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l422_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l422_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l422_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l422_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l422_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l422_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l422_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l422_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l422_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l422_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l422_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l422_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l422_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l422_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l422_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l422_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l422_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l422_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l422_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l422_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l422_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l422_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l422_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l422_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l422_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l422_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l422_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l422_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l422_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l422_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l422_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l422_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l422_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l422_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l422_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l422_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l422_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l422_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l422_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l422_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l422_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l422_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l422_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l422_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l422_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l422_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l422_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l422_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l422_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l422_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l422_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l422_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l422_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l422_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l422_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l422_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l422_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l422_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l422_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l422_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l422_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l422_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l422_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l422_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l422_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l422_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l422_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l422_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l422_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l422_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l422_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l422_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l422_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l422_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l422_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l422_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l422_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l422_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l422_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l422_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l422_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l422_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l422_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l422_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l422_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l422_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l422_(x):
    # x is a list (or vector) of length 288
    return [
        l422_0(x),
        l422_1(x),
        l422_2(x),
        l422_3(x),
        l422_4(x),
        l422_5(x),
        l422_6(x),
        l422_7(x),
        l422_8(x),
        l422_9(x),
        l422_10(x),
        l422_11(x),
        l422_12(x),
        l422_13(x),
        l422_14(x),
        l422_15(x),
        l422_16(x),
        l422_17(x),
        l422_18(x),
        l422_19(x),
        l422_20(x),
        l422_21(x),
        l422_22(x),
        l422_23(x),
        l422_24(x),
        l422_25(x),
        l422_26(x),
        l422_27(x),
        l422_28(x),
        l422_29(x),
        l422_30(x),
        l422_31(x),
        l422_32(x),
        l422_33(x),
        l422_34(x),
        l422_35(x),
        l422_36(x),
        l422_37(x),
        l422_38(x),
        l422_39(x),
        l422_40(x),
        l422_41(x),
        l422_42(x),
        l422_43(x),
        l422_44(x),
        l422_45(x),
        l422_46(x),
        l422_47(x),
        l422_48(x),
        l422_49(x),
        l422_50(x),
        l422_51(x),
        l422_52(x),
        l422_53(x),
        l422_54(x),
        l422_55(x),
        l422_56(x),
        l422_57(x),
        l422_58(x),
        l422_59(x),
        l422_60(x),
        l422_61(x),
        l422_62(x),
        l422_63(x),
        l422_64(x),
        l422_65(x),
        l422_66(x),
        l422_67(x),
        l422_68(x),
        l422_69(x),
        l422_70(x),
        l422_71(x),
        l422_72(x),
        l422_73(x),
        l422_74(x),
        l422_75(x),
        l422_76(x),
        l422_77(x),
        l422_78(x),
        l422_79(x),
        l422_80(x),
        l422_81(x),
        l422_82(x),
        l422_83(x),
        l422_84(x),
        l422_85(x),
        l422_86(x),
        l422_87(x),
        l422_88(x),
        l422_89(x),
        l422_90(x),
        l422_91(x),
        l422_92(x),
        l422_93(x),
        l422_94(x),
        l422_95(x),
        l422_96(x),
        l422_97(x),
        l422_98(x),
        l422_99(x),
        l422_100(x),
        l422_101(x),
        l422_102(x),
        l422_103(x),
        l422_104(x),
        l422_105(x),
        l422_106(x),
        l422_107(x),
        l422_108(x),
        l422_109(x),
        l422_110(x),
        l422_111(x),
        l422_112(x),
        l422_113(x),
        l422_114(x),
        l422_115(x),
        l422_116(x),
        l422_117(x),
        l422_118(x),
        l422_119(x),
        l422_120(x),
        l422_121(x),
        l422_122(x),
        l422_123(x),
        l422_124(x),
        l422_125(x),
        l422_126(x),
        l422_127(x),
        l422_128(x),
        l422_129(x),
        l422_130(x),
        l422_131(x),
        l422_132(x),
        l422_133(x),
        l422_134(x),
        l422_135(x),
        l422_136(x),
        l422_137(x),
        l422_138(x),
        l422_139(x),
        l422_140(x),
        l422_141(x),
        l422_142(x),
        l422_143(x),
        l422_144(x),
        l422_145(x),
        l422_146(x),
        l422_147(x),
        l422_148(x),
        l422_149(x),
        l422_150(x),
        l422_151(x),
        l422_152(x),
        l422_153(x),
        l422_154(x),
        l422_155(x),
        l422_156(x),
        l422_157(x),
        l422_158(x),
        l422_159(x),
        l422_160(x),
        l422_161(x),
        l422_162(x),
        l422_163(x),
        l422_164(x),
        l422_165(x),
        l422_166(x),
        l422_167(x),
        l422_168(x),
        l422_169(x),
        l422_170(x),
        l422_171(x),
        l422_172(x),
        l422_173(x),
        l422_174(x),
        l422_175(x),
        l422_176(x),
        l422_177(x),
        l422_178(x),
        l422_179(x),
        l422_180(x),
        l422_181(x),
        l422_182(x),
        l422_183(x),
        l422_184(x),
        l422_185(x),
        l422_186(x),
        l422_187(x),
        l422_188(x),
        l422_189(x),
        l422_190(x),
        l422_191(x),
        l422_192(x),
        l422_193(x),
        l422_194(x),
        l422_195(x),
        l422_196(x),
        l422_197(x),
        l422_198(x),
        l422_199(x),
        l422_200(x),
        l422_201(x),
        l422_202(x),
        l422_203(x),
        l422_204(x),
        l422_205(x),
        l422_206(x),
        l422_207(x),
        l422_208(x),
        l422_209(x),
        l422_210(x),
        l422_211(x),
        l422_212(x),
        l422_213(x),
        l422_214(x),
        l422_215(x),
        l422_216(x),
        l422_217(x),
        l422_218(x),
        l422_219(x),
        l422_220(x),
        l422_221(x),
        l422_222(x),
        l422_223(x),
        l422_224(x),
        l422_225(x),
        l422_226(x),
        l422_227(x),
        l422_228(x),
        l422_229(x),
        l422_230(x),
        l422_231(x),
        l422_232(x),
        l422_233(x),
        l422_234(x),
        l422_235(x),
        l422_236(x),
        l422_237(x),
        l422_238(x),
        l422_239(x),
        l422_240(x),
        l422_241(x),
        l422_242(x),
        l422_243(x),
        l422_244(x),
        l422_245(x),
        l422_246(x),
        l422_247(x),
        l422_248(x),
        l422_249(x),
        l422_250(x),
        l422_251(x),
        l422_252(x),
        l422_253(x),
        l422_254(x),
        l422_255(x),
        l422_256(x),
        l422_257(x),
        l422_258(x),
        l422_259(x),
        l422_260(x),
        l422_261(x),
        l422_262(x),
        l422_263(x),
        l422_264(x),
        l422_265(x),
        l422_266(x),
        l422_267(x),
        l422_268(x),
        l422_269(x),
        l422_270(x),
        l422_271(x),
        l422_272(x),
        l422_273(x),
        l422_274(x),
        l422_275(x),
        l422_276(x),
        l422_277(x),
        l422_278(x),
        l422_279(x),
        l422_280(x),
        l422_281(x),
        l422_282(x),
        l422_283(x),
        l422_284(x),
        l422_285(x),
        l422_286(x),
        l422_287(x),
        l422_288(x),
        l422_289(x),
        l422_290(x),
        l422_291(x),
        l422_292(x),
        l422_293(x),
        l422_294(x),
        l422_295(x),
        l422_296(x),
        l422_297(x),
        l422_298(x),
        l422_299(x),
        l422_300(x),
        l422_301(x),
        l422_302(x),
        l422_303(x),
    ]