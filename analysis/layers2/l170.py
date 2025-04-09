import numpy as np




# Generated from reverse engineering
def l170_g(x: np.ndarray) -> np.ndarray:
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




def l170_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l170_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l170_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l170_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l170_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l170_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l170_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l170_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l170_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l170_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l170_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l170_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l170_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l170_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l170_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l170_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l170_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l170_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l170_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l170_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l170_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l170_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l170_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l170_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l170_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l170_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l170_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l170_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l170_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l170_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l170_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l170_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l170_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l170_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l170_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l170_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l170_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l170_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l170_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l170_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l170_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l170_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l170_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l170_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l170_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l170_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l170_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l170_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l170_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l170_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l170_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l170_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l170_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l170_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l170_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l170_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l170_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l170_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l170_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l170_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l170_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l170_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l170_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l170_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l170_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l170_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l170_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l170_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l170_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l170_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l170_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l170_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l170_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l170_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l170_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l170_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l170_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l170_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l170_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l170_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l170_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l170_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l170_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l170_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l170_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l170_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l170_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l170_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l170_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l170_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l170_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l170_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l170_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l170_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l170_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l170_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l170_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l170_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l170_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l170_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l170_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[100])
def l170_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[101])
def l170_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[102])
def l170_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[103])
def l170_104(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + 1.0)
def l170_105(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + 1.0)
def l170_106(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + 1.0)
def l170_107(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + 1.0)
def l170_108(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + 1.0)
def l170_109(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + 1.0)
def l170_110(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + 1.0)
def l170_111(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + 1.0)
def l170_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + x[144] + -1.0)
def l170_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + x[145] + -1.0)
def l170_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + x[146] + -1.0)
def l170_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + x[147] + -1.0)
def l170_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + x[148] + -1.0)
def l170_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + x[149] + -1.0)
def l170_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + x[150] + -1.0)
def l170_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + x[151] + -1.0)
def l170_120(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + x[152])
def l170_121(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + x[153])
def l170_122(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + x[154])
def l170_123(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + x[155])
def l170_124(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + x[156])
def l170_125(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + x[157])
def l170_126(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + x[158])
def l170_127(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + x[159])
def l170_128(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + 1.0)
def l170_129(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + 1.0)
def l170_130(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + 1.0)
def l170_131(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + 1.0)
def l170_132(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + 1.0)
def l170_133(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + 1.0)
def l170_134(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + 1.0)
def l170_135(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + 1.0)
def l170_136(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + 1.0)
def l170_137(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + 1.0)
def l170_138(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + 1.0)
def l170_139(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + 1.0)
def l170_140(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + 1.0)
def l170_141(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + 1.0)
def l170_142(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[126] + 1.0)
def l170_143(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[127] + 1.0)
def l170_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[128] + x[144] + -1.0)
def l170_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[129] + x[145] + -1.0)
def l170_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[130] + x[146] + -1.0)
def l170_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[131] + x[147] + -1.0)
def l170_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[132] + x[148] + -1.0)
def l170_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[133] + x[149] + -1.0)
def l170_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[134] + x[150] + -1.0)
def l170_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[135] + x[151] + -1.0)
def l170_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[136] + x[152] + -1.0)
def l170_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[137] + x[153] + -1.0)
def l170_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[138] + x[154] + -1.0)
def l170_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[139] + x[155] + -1.0)
def l170_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[140] + x[156] + -1.0)
def l170_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[141] + x[157] + -1.0)
def l170_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[142] + x[158] + -1.0)
def l170_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[143] + x[159] + -1.0)
def l170_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l170_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l170_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l170_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l170_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l170_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l170_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l170_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l170_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l170_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l170_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l170_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l170_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l170_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l170_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l170_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l170_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l170_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l170_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l170_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l170_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l170_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l170_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l170_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l170_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l170_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l170_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l170_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l170_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l170_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l170_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l170_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l170_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l170_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l170_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l170_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l170_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l170_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l170_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l170_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l170_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l170_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l170_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l170_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l170_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l170_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l170_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l170_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l170_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l170_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l170_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l170_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l170_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l170_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l170_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l170_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l170_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l170_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l170_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l170_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l170_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l170_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l170_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l170_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l170_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l170_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l170_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l170_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l170_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l170_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l170_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l170_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l170_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l170_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l170_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l170_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l170_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l170_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l170_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l170_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l170_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l170_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l170_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l170_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l170_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l170_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l170_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l170_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l170_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l170_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l170_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l170_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l170_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l170_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l170_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l170_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l170_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l170_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l170_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l170_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l170_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l170_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l170_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l170_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l170_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l170_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l170_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l170_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l170_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l170_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l170_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l170_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l170_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l170_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l170_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l170_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l170_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l170_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l170_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l170_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l170_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l170_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l170_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l170_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l170_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l170_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l170_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l170_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l170_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l170_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l170_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l170_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l170_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l170_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l170_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l170_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l170_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l170_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l170_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l170_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l170_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l170_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l170_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l170_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l170_(x):
    # x is a list (or vector) of length 288
    return [
        l170_0(x),
        l170_1(x),
        l170_2(x),
        l170_3(x),
        l170_4(x),
        l170_5(x),
        l170_6(x),
        l170_7(x),
        l170_8(x),
        l170_9(x),
        l170_10(x),
        l170_11(x),
        l170_12(x),
        l170_13(x),
        l170_14(x),
        l170_15(x),
        l170_16(x),
        l170_17(x),
        l170_18(x),
        l170_19(x),
        l170_20(x),
        l170_21(x),
        l170_22(x),
        l170_23(x),
        l170_24(x),
        l170_25(x),
        l170_26(x),
        l170_27(x),
        l170_28(x),
        l170_29(x),
        l170_30(x),
        l170_31(x),
        l170_32(x),
        l170_33(x),
        l170_34(x),
        l170_35(x),
        l170_36(x),
        l170_37(x),
        l170_38(x),
        l170_39(x),
        l170_40(x),
        l170_41(x),
        l170_42(x),
        l170_43(x),
        l170_44(x),
        l170_45(x),
        l170_46(x),
        l170_47(x),
        l170_48(x),
        l170_49(x),
        l170_50(x),
        l170_51(x),
        l170_52(x),
        l170_53(x),
        l170_54(x),
        l170_55(x),
        l170_56(x),
        l170_57(x),
        l170_58(x),
        l170_59(x),
        l170_60(x),
        l170_61(x),
        l170_62(x),
        l170_63(x),
        l170_64(x),
        l170_65(x),
        l170_66(x),
        l170_67(x),
        l170_68(x),
        l170_69(x),
        l170_70(x),
        l170_71(x),
        l170_72(x),
        l170_73(x),
        l170_74(x),
        l170_75(x),
        l170_76(x),
        l170_77(x),
        l170_78(x),
        l170_79(x),
        l170_80(x),
        l170_81(x),
        l170_82(x),
        l170_83(x),
        l170_84(x),
        l170_85(x),
        l170_86(x),
        l170_87(x),
        l170_88(x),
        l170_89(x),
        l170_90(x),
        l170_91(x),
        l170_92(x),
        l170_93(x),
        l170_94(x),
        l170_95(x),
        l170_96(x),
        l170_97(x),
        l170_98(x),
        l170_99(x),
        l170_100(x),
        l170_101(x),
        l170_102(x),
        l170_103(x),
        l170_104(x),
        l170_105(x),
        l170_106(x),
        l170_107(x),
        l170_108(x),
        l170_109(x),
        l170_110(x),
        l170_111(x),
        l170_112(x),
        l170_113(x),
        l170_114(x),
        l170_115(x),
        l170_116(x),
        l170_117(x),
        l170_118(x),
        l170_119(x),
        l170_120(x),
        l170_121(x),
        l170_122(x),
        l170_123(x),
        l170_124(x),
        l170_125(x),
        l170_126(x),
        l170_127(x),
        l170_128(x),
        l170_129(x),
        l170_130(x),
        l170_131(x),
        l170_132(x),
        l170_133(x),
        l170_134(x),
        l170_135(x),
        l170_136(x),
        l170_137(x),
        l170_138(x),
        l170_139(x),
        l170_140(x),
        l170_141(x),
        l170_142(x),
        l170_143(x),
        l170_144(x),
        l170_145(x),
        l170_146(x),
        l170_147(x),
        l170_148(x),
        l170_149(x),
        l170_150(x),
        l170_151(x),
        l170_152(x),
        l170_153(x),
        l170_154(x),
        l170_155(x),
        l170_156(x),
        l170_157(x),
        l170_158(x),
        l170_159(x),
        l170_160(x),
        l170_161(x),
        l170_162(x),
        l170_163(x),
        l170_164(x),
        l170_165(x),
        l170_166(x),
        l170_167(x),
        l170_168(x),
        l170_169(x),
        l170_170(x),
        l170_171(x),
        l170_172(x),
        l170_173(x),
        l170_174(x),
        l170_175(x),
        l170_176(x),
        l170_177(x),
        l170_178(x),
        l170_179(x),
        l170_180(x),
        l170_181(x),
        l170_182(x),
        l170_183(x),
        l170_184(x),
        l170_185(x),
        l170_186(x),
        l170_187(x),
        l170_188(x),
        l170_189(x),
        l170_190(x),
        l170_191(x),
        l170_192(x),
        l170_193(x),
        l170_194(x),
        l170_195(x),
        l170_196(x),
        l170_197(x),
        l170_198(x),
        l170_199(x),
        l170_200(x),
        l170_201(x),
        l170_202(x),
        l170_203(x),
        l170_204(x),
        l170_205(x),
        l170_206(x),
        l170_207(x),
        l170_208(x),
        l170_209(x),
        l170_210(x),
        l170_211(x),
        l170_212(x),
        l170_213(x),
        l170_214(x),
        l170_215(x),
        l170_216(x),
        l170_217(x),
        l170_218(x),
        l170_219(x),
        l170_220(x),
        l170_221(x),
        l170_222(x),
        l170_223(x),
        l170_224(x),
        l170_225(x),
        l170_226(x),
        l170_227(x),
        l170_228(x),
        l170_229(x),
        l170_230(x),
        l170_231(x),
        l170_232(x),
        l170_233(x),
        l170_234(x),
        l170_235(x),
        l170_236(x),
        l170_237(x),
        l170_238(x),
        l170_239(x),
        l170_240(x),
        l170_241(x),
        l170_242(x),
        l170_243(x),
        l170_244(x),
        l170_245(x),
        l170_246(x),
        l170_247(x),
        l170_248(x),
        l170_249(x),
        l170_250(x),
        l170_251(x),
        l170_252(x),
        l170_253(x),
        l170_254(x),
        l170_255(x),
        l170_256(x),
        l170_257(x),
        l170_258(x),
        l170_259(x),
        l170_260(x),
        l170_261(x),
        l170_262(x),
        l170_263(x),
        l170_264(x),
        l170_265(x),
        l170_266(x),
        l170_267(x),
        l170_268(x),
        l170_269(x),
        l170_270(x),
        l170_271(x),
        l170_272(x),
        l170_273(x),
        l170_274(x),
        l170_275(x),
        l170_276(x),
        l170_277(x),
        l170_278(x),
        l170_279(x),
        l170_280(x),
        l170_281(x),
        l170_282(x),
        l170_283(x),
        l170_284(x),
        l170_285(x),
        l170_286(x),
        l170_287(x),
        l170_288(x),
        l170_289(x),
        l170_290(x),
        l170_291(x),
        l170_292(x),
        l170_293(x),
        l170_294(x),
        l170_295(x),
        l170_296(x),
        l170_297(x),
        l170_298(x),
        l170_299(x),
        l170_300(x),
        l170_301(x),
        l170_302(x),
        l170_303(x),
    ]