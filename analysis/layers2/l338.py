import numpy as np




# Generated from reverse engineering
def l338_g(x: np.ndarray) -> np.ndarray:
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




def l338_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l338_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l338_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l338_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l338_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l338_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l338_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l338_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l338_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l338_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l338_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l338_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l338_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l338_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l338_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l338_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l338_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l338_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l338_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l338_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l338_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l338_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l338_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l338_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l338_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l338_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l338_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l338_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l338_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l338_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l338_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l338_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l338_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l338_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l338_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l338_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l338_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l338_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l338_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l338_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l338_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l338_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l338_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l338_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l338_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l338_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l338_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l338_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l338_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l338_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l338_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l338_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l338_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l338_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l338_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l338_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l338_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l338_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l338_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l338_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l338_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l338_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l338_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l338_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l338_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l338_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l338_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l338_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l338_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l338_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l338_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l338_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l338_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l338_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l338_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l338_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l338_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l338_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l338_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l338_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l338_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l338_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l338_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l338_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l338_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l338_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l338_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l338_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l338_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l338_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l338_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l338_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l338_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l338_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l338_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l338_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l338_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l338_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l338_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l338_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l338_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[100])
def l338_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[101])
def l338_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[102])
def l338_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[103])
def l338_104(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + 1.0)
def l338_105(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + 1.0)
def l338_106(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + 1.0)
def l338_107(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + 1.0)
def l338_108(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + 1.0)
def l338_109(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + 1.0)
def l338_110(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + 1.0)
def l338_111(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + 1.0)
def l338_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + x[144] + -1.0)
def l338_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + x[145] + -1.0)
def l338_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + x[146] + -1.0)
def l338_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + x[147] + -1.0)
def l338_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + x[148] + -1.0)
def l338_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + x[149] + -1.0)
def l338_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + x[150] + -1.0)
def l338_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + x[151] + -1.0)
def l338_120(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + x[152])
def l338_121(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + x[153])
def l338_122(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + x[154])
def l338_123(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + x[155])
def l338_124(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + x[156])
def l338_125(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + x[157])
def l338_126(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + x[158])
def l338_127(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + x[159])
def l338_128(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + 1.0)
def l338_129(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + 1.0)
def l338_130(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + 1.0)
def l338_131(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + 1.0)
def l338_132(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + 1.0)
def l338_133(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + 1.0)
def l338_134(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + 1.0)
def l338_135(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + 1.0)
def l338_136(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + 1.0)
def l338_137(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + 1.0)
def l338_138(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + 1.0)
def l338_139(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + 1.0)
def l338_140(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + 1.0)
def l338_141(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + 1.0)
def l338_142(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[126] + 1.0)
def l338_143(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[127] + 1.0)
def l338_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[128] + x[144] + -1.0)
def l338_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[129] + x[145] + -1.0)
def l338_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[130] + x[146] + -1.0)
def l338_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[131] + x[147] + -1.0)
def l338_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[132] + x[148] + -1.0)
def l338_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[133] + x[149] + -1.0)
def l338_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[134] + x[150] + -1.0)
def l338_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[135] + x[151] + -1.0)
def l338_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[136] + x[152] + -1.0)
def l338_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[137] + x[153] + -1.0)
def l338_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[138] + x[154] + -1.0)
def l338_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[139] + x[155] + -1.0)
def l338_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[140] + x[156] + -1.0)
def l338_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[141] + x[157] + -1.0)
def l338_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[142] + x[158] + -1.0)
def l338_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[143] + x[159] + -1.0)
def l338_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l338_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l338_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l338_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l338_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l338_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l338_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l338_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l338_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l338_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l338_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l338_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l338_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l338_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l338_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l338_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l338_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l338_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l338_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l338_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l338_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l338_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l338_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l338_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l338_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l338_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l338_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l338_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l338_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l338_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l338_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l338_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l338_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l338_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l338_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l338_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l338_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l338_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l338_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l338_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l338_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l338_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l338_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l338_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l338_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l338_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l338_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l338_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l338_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l338_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l338_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l338_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l338_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l338_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l338_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l338_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l338_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l338_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l338_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l338_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l338_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l338_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l338_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l338_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l338_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l338_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l338_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l338_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l338_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l338_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l338_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l338_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l338_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l338_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l338_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l338_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l338_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l338_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l338_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l338_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l338_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l338_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l338_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l338_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l338_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l338_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l338_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l338_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l338_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l338_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l338_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l338_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l338_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l338_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l338_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l338_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l338_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l338_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l338_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l338_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l338_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l338_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l338_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l338_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l338_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l338_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l338_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l338_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l338_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l338_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l338_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l338_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l338_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l338_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l338_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l338_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l338_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l338_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l338_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l338_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l338_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l338_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l338_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l338_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l338_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l338_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l338_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l338_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l338_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l338_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l338_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l338_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l338_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l338_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l338_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l338_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l338_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l338_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l338_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l338_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l338_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l338_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l338_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l338_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l338_(x):
    # x is a list (or vector) of length 288
    return [
        l338_0(x),
        l338_1(x),
        l338_2(x),
        l338_3(x),
        l338_4(x),
        l338_5(x),
        l338_6(x),
        l338_7(x),
        l338_8(x),
        l338_9(x),
        l338_10(x),
        l338_11(x),
        l338_12(x),
        l338_13(x),
        l338_14(x),
        l338_15(x),
        l338_16(x),
        l338_17(x),
        l338_18(x),
        l338_19(x),
        l338_20(x),
        l338_21(x),
        l338_22(x),
        l338_23(x),
        l338_24(x),
        l338_25(x),
        l338_26(x),
        l338_27(x),
        l338_28(x),
        l338_29(x),
        l338_30(x),
        l338_31(x),
        l338_32(x),
        l338_33(x),
        l338_34(x),
        l338_35(x),
        l338_36(x),
        l338_37(x),
        l338_38(x),
        l338_39(x),
        l338_40(x),
        l338_41(x),
        l338_42(x),
        l338_43(x),
        l338_44(x),
        l338_45(x),
        l338_46(x),
        l338_47(x),
        l338_48(x),
        l338_49(x),
        l338_50(x),
        l338_51(x),
        l338_52(x),
        l338_53(x),
        l338_54(x),
        l338_55(x),
        l338_56(x),
        l338_57(x),
        l338_58(x),
        l338_59(x),
        l338_60(x),
        l338_61(x),
        l338_62(x),
        l338_63(x),
        l338_64(x),
        l338_65(x),
        l338_66(x),
        l338_67(x),
        l338_68(x),
        l338_69(x),
        l338_70(x),
        l338_71(x),
        l338_72(x),
        l338_73(x),
        l338_74(x),
        l338_75(x),
        l338_76(x),
        l338_77(x),
        l338_78(x),
        l338_79(x),
        l338_80(x),
        l338_81(x),
        l338_82(x),
        l338_83(x),
        l338_84(x),
        l338_85(x),
        l338_86(x),
        l338_87(x),
        l338_88(x),
        l338_89(x),
        l338_90(x),
        l338_91(x),
        l338_92(x),
        l338_93(x),
        l338_94(x),
        l338_95(x),
        l338_96(x),
        l338_97(x),
        l338_98(x),
        l338_99(x),
        l338_100(x),
        l338_101(x),
        l338_102(x),
        l338_103(x),
        l338_104(x),
        l338_105(x),
        l338_106(x),
        l338_107(x),
        l338_108(x),
        l338_109(x),
        l338_110(x),
        l338_111(x),
        l338_112(x),
        l338_113(x),
        l338_114(x),
        l338_115(x),
        l338_116(x),
        l338_117(x),
        l338_118(x),
        l338_119(x),
        l338_120(x),
        l338_121(x),
        l338_122(x),
        l338_123(x),
        l338_124(x),
        l338_125(x),
        l338_126(x),
        l338_127(x),
        l338_128(x),
        l338_129(x),
        l338_130(x),
        l338_131(x),
        l338_132(x),
        l338_133(x),
        l338_134(x),
        l338_135(x),
        l338_136(x),
        l338_137(x),
        l338_138(x),
        l338_139(x),
        l338_140(x),
        l338_141(x),
        l338_142(x),
        l338_143(x),
        l338_144(x),
        l338_145(x),
        l338_146(x),
        l338_147(x),
        l338_148(x),
        l338_149(x),
        l338_150(x),
        l338_151(x),
        l338_152(x),
        l338_153(x),
        l338_154(x),
        l338_155(x),
        l338_156(x),
        l338_157(x),
        l338_158(x),
        l338_159(x),
        l338_160(x),
        l338_161(x),
        l338_162(x),
        l338_163(x),
        l338_164(x),
        l338_165(x),
        l338_166(x),
        l338_167(x),
        l338_168(x),
        l338_169(x),
        l338_170(x),
        l338_171(x),
        l338_172(x),
        l338_173(x),
        l338_174(x),
        l338_175(x),
        l338_176(x),
        l338_177(x),
        l338_178(x),
        l338_179(x),
        l338_180(x),
        l338_181(x),
        l338_182(x),
        l338_183(x),
        l338_184(x),
        l338_185(x),
        l338_186(x),
        l338_187(x),
        l338_188(x),
        l338_189(x),
        l338_190(x),
        l338_191(x),
        l338_192(x),
        l338_193(x),
        l338_194(x),
        l338_195(x),
        l338_196(x),
        l338_197(x),
        l338_198(x),
        l338_199(x),
        l338_200(x),
        l338_201(x),
        l338_202(x),
        l338_203(x),
        l338_204(x),
        l338_205(x),
        l338_206(x),
        l338_207(x),
        l338_208(x),
        l338_209(x),
        l338_210(x),
        l338_211(x),
        l338_212(x),
        l338_213(x),
        l338_214(x),
        l338_215(x),
        l338_216(x),
        l338_217(x),
        l338_218(x),
        l338_219(x),
        l338_220(x),
        l338_221(x),
        l338_222(x),
        l338_223(x),
        l338_224(x),
        l338_225(x),
        l338_226(x),
        l338_227(x),
        l338_228(x),
        l338_229(x),
        l338_230(x),
        l338_231(x),
        l338_232(x),
        l338_233(x),
        l338_234(x),
        l338_235(x),
        l338_236(x),
        l338_237(x),
        l338_238(x),
        l338_239(x),
        l338_240(x),
        l338_241(x),
        l338_242(x),
        l338_243(x),
        l338_244(x),
        l338_245(x),
        l338_246(x),
        l338_247(x),
        l338_248(x),
        l338_249(x),
        l338_250(x),
        l338_251(x),
        l338_252(x),
        l338_253(x),
        l338_254(x),
        l338_255(x),
        l338_256(x),
        l338_257(x),
        l338_258(x),
        l338_259(x),
        l338_260(x),
        l338_261(x),
        l338_262(x),
        l338_263(x),
        l338_264(x),
        l338_265(x),
        l338_266(x),
        l338_267(x),
        l338_268(x),
        l338_269(x),
        l338_270(x),
        l338_271(x),
        l338_272(x),
        l338_273(x),
        l338_274(x),
        l338_275(x),
        l338_276(x),
        l338_277(x),
        l338_278(x),
        l338_279(x),
        l338_280(x),
        l338_281(x),
        l338_282(x),
        l338_283(x),
        l338_284(x),
        l338_285(x),
        l338_286(x),
        l338_287(x),
        l338_288(x),
        l338_289(x),
        l338_290(x),
        l338_291(x),
        l338_292(x),
        l338_293(x),
        l338_294(x),
        l338_295(x),
        l338_296(x),
        l338_297(x),
        l338_298(x),
        l338_299(x),
        l338_300(x),
        l338_301(x),
        l338_302(x),
        l338_303(x),
    ]