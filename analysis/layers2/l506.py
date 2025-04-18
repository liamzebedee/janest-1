import numpy as np




# Generated from reverse engineering
def l506_g(x: np.ndarray) -> np.ndarray:
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




def l506_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l506_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l506_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l506_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l506_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l506_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l506_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l506_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l506_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l506_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l506_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l506_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l506_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l506_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l506_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l506_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l506_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l506_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l506_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l506_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l506_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l506_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l506_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l506_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l506_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l506_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l506_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l506_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l506_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l506_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l506_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l506_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l506_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l506_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l506_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l506_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l506_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l506_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l506_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l506_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l506_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l506_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l506_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l506_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l506_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l506_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l506_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l506_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l506_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l506_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l506_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l506_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l506_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l506_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l506_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l506_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l506_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l506_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l506_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l506_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l506_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l506_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l506_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l506_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l506_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l506_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l506_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l506_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l506_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l506_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l506_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l506_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l506_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l506_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l506_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l506_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l506_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l506_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l506_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l506_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l506_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l506_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l506_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l506_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l506_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l506_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l506_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l506_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l506_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l506_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l506_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l506_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l506_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l506_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l506_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l506_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l506_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l506_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[97])
def l506_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[98])
def l506_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[99])
def l506_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[100])
def l506_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[101])
def l506_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[102])
def l506_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[103])
def l506_104(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + 1.0)
def l506_105(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + 1.0)
def l506_106(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + 1.0)
def l506_107(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + 1.0)
def l506_108(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + 1.0)
def l506_109(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + 1.0)
def l506_110(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + 1.0)
def l506_111(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + 1.0)
def l506_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + x[144] + -1.0)
def l506_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + x[145] + -1.0)
def l506_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + x[146] + -1.0)
def l506_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + x[147] + -1.0)
def l506_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + x[148] + -1.0)
def l506_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + x[149] + -1.0)
def l506_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + x[150] + -1.0)
def l506_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + x[151] + -1.0)
def l506_120(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[104] + x[152])
def l506_121(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[105] + x[153])
def l506_122(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[106] + x[154])
def l506_123(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[107] + x[155])
def l506_124(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[108] + x[156])
def l506_125(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[109] + x[157])
def l506_126(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[110] + x[158])
def l506_127(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[111] + x[159])
def l506_128(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[112] + 1.0)
def l506_129(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[113] + 1.0)
def l506_130(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[114] + 1.0)
def l506_131(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[115] + 1.0)
def l506_132(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[116] + 1.0)
def l506_133(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[117] + 1.0)
def l506_134(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[118] + 1.0)
def l506_135(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[119] + 1.0)
def l506_136(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[120] + 1.0)
def l506_137(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[121] + 1.0)
def l506_138(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[122] + 1.0)
def l506_139(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[123] + 1.0)
def l506_140(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[124] + 1.0)
def l506_141(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[125] + 1.0)
def l506_142(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[126] + 1.0)
def l506_143(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[127] + 1.0)
def l506_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[128] + x[144] + -1.0)
def l506_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[129] + x[145] + -1.0)
def l506_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[130] + x[146] + -1.0)
def l506_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[131] + x[147] + -1.0)
def l506_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[132] + x[148] + -1.0)
def l506_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[133] + x[149] + -1.0)
def l506_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[134] + x[150] + -1.0)
def l506_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[135] + x[151] + -1.0)
def l506_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[136] + x[152] + -1.0)
def l506_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[137] + x[153] + -1.0)
def l506_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[138] + x[154] + -1.0)
def l506_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[139] + x[155] + -1.0)
def l506_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[140] + x[156] + -1.0)
def l506_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[141] + x[157] + -1.0)
def l506_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[142] + x[158] + -1.0)
def l506_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[143] + x[159] + -1.0)
def l506_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l506_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l506_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l506_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l506_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l506_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l506_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l506_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l506_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l506_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l506_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l506_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l506_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l506_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l506_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l506_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l506_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l506_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l506_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l506_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l506_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l506_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l506_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l506_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l506_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l506_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l506_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l506_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l506_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l506_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l506_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l506_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l506_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l506_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l506_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l506_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l506_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l506_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l506_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l506_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l506_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l506_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l506_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l506_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l506_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l506_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l506_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l506_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l506_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l506_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l506_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l506_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l506_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l506_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l506_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l506_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l506_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l506_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l506_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l506_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l506_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l506_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l506_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l506_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l506_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l506_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l506_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l506_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l506_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l506_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l506_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l506_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l506_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l506_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l506_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l506_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l506_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l506_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l506_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l506_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l506_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l506_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l506_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l506_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l506_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l506_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l506_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l506_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l506_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l506_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l506_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l506_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l506_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l506_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l506_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l506_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l506_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l506_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l506_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l506_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l506_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l506_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l506_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l506_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l506_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l506_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l506_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l506_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l506_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l506_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l506_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l506_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l506_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l506_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l506_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l506_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l506_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l506_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l506_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l506_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l506_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l506_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l506_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l506_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l506_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l506_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l506_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l506_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l506_288(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l506_289(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l506_290(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l506_291(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l506_292(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l506_293(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l506_294(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l506_295(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l506_296(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l506_297(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l506_298(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l506_299(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l506_300(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l506_301(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l506_302(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l506_303(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l506_(x):
    # x is a list (or vector) of length 288
    return [
        l506_0(x),
        l506_1(x),
        l506_2(x),
        l506_3(x),
        l506_4(x),
        l506_5(x),
        l506_6(x),
        l506_7(x),
        l506_8(x),
        l506_9(x),
        l506_10(x),
        l506_11(x),
        l506_12(x),
        l506_13(x),
        l506_14(x),
        l506_15(x),
        l506_16(x),
        l506_17(x),
        l506_18(x),
        l506_19(x),
        l506_20(x),
        l506_21(x),
        l506_22(x),
        l506_23(x),
        l506_24(x),
        l506_25(x),
        l506_26(x),
        l506_27(x),
        l506_28(x),
        l506_29(x),
        l506_30(x),
        l506_31(x),
        l506_32(x),
        l506_33(x),
        l506_34(x),
        l506_35(x),
        l506_36(x),
        l506_37(x),
        l506_38(x),
        l506_39(x),
        l506_40(x),
        l506_41(x),
        l506_42(x),
        l506_43(x),
        l506_44(x),
        l506_45(x),
        l506_46(x),
        l506_47(x),
        l506_48(x),
        l506_49(x),
        l506_50(x),
        l506_51(x),
        l506_52(x),
        l506_53(x),
        l506_54(x),
        l506_55(x),
        l506_56(x),
        l506_57(x),
        l506_58(x),
        l506_59(x),
        l506_60(x),
        l506_61(x),
        l506_62(x),
        l506_63(x),
        l506_64(x),
        l506_65(x),
        l506_66(x),
        l506_67(x),
        l506_68(x),
        l506_69(x),
        l506_70(x),
        l506_71(x),
        l506_72(x),
        l506_73(x),
        l506_74(x),
        l506_75(x),
        l506_76(x),
        l506_77(x),
        l506_78(x),
        l506_79(x),
        l506_80(x),
        l506_81(x),
        l506_82(x),
        l506_83(x),
        l506_84(x),
        l506_85(x),
        l506_86(x),
        l506_87(x),
        l506_88(x),
        l506_89(x),
        l506_90(x),
        l506_91(x),
        l506_92(x),
        l506_93(x),
        l506_94(x),
        l506_95(x),
        l506_96(x),
        l506_97(x),
        l506_98(x),
        l506_99(x),
        l506_100(x),
        l506_101(x),
        l506_102(x),
        l506_103(x),
        l506_104(x),
        l506_105(x),
        l506_106(x),
        l506_107(x),
        l506_108(x),
        l506_109(x),
        l506_110(x),
        l506_111(x),
        l506_112(x),
        l506_113(x),
        l506_114(x),
        l506_115(x),
        l506_116(x),
        l506_117(x),
        l506_118(x),
        l506_119(x),
        l506_120(x),
        l506_121(x),
        l506_122(x),
        l506_123(x),
        l506_124(x),
        l506_125(x),
        l506_126(x),
        l506_127(x),
        l506_128(x),
        l506_129(x),
        l506_130(x),
        l506_131(x),
        l506_132(x),
        l506_133(x),
        l506_134(x),
        l506_135(x),
        l506_136(x),
        l506_137(x),
        l506_138(x),
        l506_139(x),
        l506_140(x),
        l506_141(x),
        l506_142(x),
        l506_143(x),
        l506_144(x),
        l506_145(x),
        l506_146(x),
        l506_147(x),
        l506_148(x),
        l506_149(x),
        l506_150(x),
        l506_151(x),
        l506_152(x),
        l506_153(x),
        l506_154(x),
        l506_155(x),
        l506_156(x),
        l506_157(x),
        l506_158(x),
        l506_159(x),
        l506_160(x),
        l506_161(x),
        l506_162(x),
        l506_163(x),
        l506_164(x),
        l506_165(x),
        l506_166(x),
        l506_167(x),
        l506_168(x),
        l506_169(x),
        l506_170(x),
        l506_171(x),
        l506_172(x),
        l506_173(x),
        l506_174(x),
        l506_175(x),
        l506_176(x),
        l506_177(x),
        l506_178(x),
        l506_179(x),
        l506_180(x),
        l506_181(x),
        l506_182(x),
        l506_183(x),
        l506_184(x),
        l506_185(x),
        l506_186(x),
        l506_187(x),
        l506_188(x),
        l506_189(x),
        l506_190(x),
        l506_191(x),
        l506_192(x),
        l506_193(x),
        l506_194(x),
        l506_195(x),
        l506_196(x),
        l506_197(x),
        l506_198(x),
        l506_199(x),
        l506_200(x),
        l506_201(x),
        l506_202(x),
        l506_203(x),
        l506_204(x),
        l506_205(x),
        l506_206(x),
        l506_207(x),
        l506_208(x),
        l506_209(x),
        l506_210(x),
        l506_211(x),
        l506_212(x),
        l506_213(x),
        l506_214(x),
        l506_215(x),
        l506_216(x),
        l506_217(x),
        l506_218(x),
        l506_219(x),
        l506_220(x),
        l506_221(x),
        l506_222(x),
        l506_223(x),
        l506_224(x),
        l506_225(x),
        l506_226(x),
        l506_227(x),
        l506_228(x),
        l506_229(x),
        l506_230(x),
        l506_231(x),
        l506_232(x),
        l506_233(x),
        l506_234(x),
        l506_235(x),
        l506_236(x),
        l506_237(x),
        l506_238(x),
        l506_239(x),
        l506_240(x),
        l506_241(x),
        l506_242(x),
        l506_243(x),
        l506_244(x),
        l506_245(x),
        l506_246(x),
        l506_247(x),
        l506_248(x),
        l506_249(x),
        l506_250(x),
        l506_251(x),
        l506_252(x),
        l506_253(x),
        l506_254(x),
        l506_255(x),
        l506_256(x),
        l506_257(x),
        l506_258(x),
        l506_259(x),
        l506_260(x),
        l506_261(x),
        l506_262(x),
        l506_263(x),
        l506_264(x),
        l506_265(x),
        l506_266(x),
        l506_267(x),
        l506_268(x),
        l506_269(x),
        l506_270(x),
        l506_271(x),
        l506_272(x),
        l506_273(x),
        l506_274(x),
        l506_275(x),
        l506_276(x),
        l506_277(x),
        l506_278(x),
        l506_279(x),
        l506_280(x),
        l506_281(x),
        l506_282(x),
        l506_283(x),
        l506_284(x),
        l506_285(x),
        l506_286(x),
        l506_287(x),
        l506_288(x),
        l506_289(x),
        l506_290(x),
        l506_291(x),
        l506_292(x),
        l506_293(x),
        l506_294(x),
        l506_295(x),
        l506_296(x),
        l506_297(x),
        l506_298(x),
        l506_299(x),
        l506_300(x),
        l506_301(x),
        l506_302(x),
        l506_303(x),
    ]