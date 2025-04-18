import numpy as np




# Generated from reverse engineering
def l312_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 400
    out = np.empty(400, dtype=np.float32)
    
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
        
    # for i in range(176, 224):
    for i in range(0, 48):
        s = x[160 + i]
        out[176 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffff (len=16)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(224, 240):
    for i in range(0, 16):
        s = -1 * x[208 + i] + -1 * x[224 + i]
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(240, 256):
    for i in range(0, 16):
        s = x[256 + i]
        out[240 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(256, 272):
    for i in range(0, 16):
        s = x[240 + i]
        out[256 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(272, 328):
    for i in range(0, 56):
        s = x[272 + i]
        out[272 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xf (len=4)
    biases = [1.0, 1.0, 1.0, 1.0]
    # for i in range(328, 332):
    for i in range(0, 4):
        s = -1 * x[328 + i]
        s += biases[i]
        out[328 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(332, 336):
    for i in range(0, 4):
        s = x[332 + i] + -2.0 * x[i + 336] + 2.0 * x[i + 340]
        out[332 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(336, 400):
    for i in range(0, 64):
        s = x[344 + i]
        out[336 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l312_0(x):
    # x is a list (or vector) of length 408
    return max(0, x[0])
def l312_1(x):
    # x is a list (or vector) of length 408
    return max(0, x[1])
def l312_2(x):
    # x is a list (or vector) of length 408
    return max(0, x[2])
def l312_3(x):
    # x is a list (or vector) of length 408
    return max(0, x[3])
def l312_4(x):
    # x is a list (or vector) of length 408
    return max(0, x[4])
def l312_5(x):
    # x is a list (or vector) of length 408
    return max(0, x[5])
def l312_6(x):
    # x is a list (or vector) of length 408
    return max(0, x[6])
def l312_7(x):
    # x is a list (or vector) of length 408
    return max(0, x[7])
def l312_8(x):
    # x is a list (or vector) of length 408
    return max(0, x[8])
def l312_9(x):
    # x is a list (or vector) of length 408
    return max(0, x[9])
def l312_10(x):
    # x is a list (or vector) of length 408
    return max(0, x[10])
def l312_11(x):
    # x is a list (or vector) of length 408
    return max(0, x[11])
def l312_12(x):
    # x is a list (or vector) of length 408
    return max(0, x[12])
def l312_13(x):
    # x is a list (or vector) of length 408
    return max(0, x[13])
def l312_14(x):
    # x is a list (or vector) of length 408
    return max(0, x[14])
def l312_15(x):
    # x is a list (or vector) of length 408
    return max(0, x[15])
def l312_16(x):
    # x is a list (or vector) of length 408
    return max(0, x[16])
def l312_17(x):
    # x is a list (or vector) of length 408
    return max(0, x[17])
def l312_18(x):
    # x is a list (or vector) of length 408
    return max(0, x[18])
def l312_19(x):
    # x is a list (or vector) of length 408
    return max(0, x[19])
def l312_20(x):
    # x is a list (or vector) of length 408
    return max(0, x[20])
def l312_21(x):
    # x is a list (or vector) of length 408
    return max(0, x[21])
def l312_22(x):
    # x is a list (or vector) of length 408
    return max(0, x[22])
def l312_23(x):
    # x is a list (or vector) of length 408
    return max(0, x[23])
def l312_24(x):
    # x is a list (or vector) of length 408
    return max(0, x[24])
def l312_25(x):
    # x is a list (or vector) of length 408
    return max(0, x[25])
def l312_26(x):
    # x is a list (or vector) of length 408
    return max(0, x[26])
def l312_27(x):
    # x is a list (or vector) of length 408
    return max(0, x[27])
def l312_28(x):
    # x is a list (or vector) of length 408
    return max(0, x[28])
def l312_29(x):
    # x is a list (or vector) of length 408
    return max(0, x[29])
def l312_30(x):
    # x is a list (or vector) of length 408
    return max(0, x[30])
def l312_31(x):
    # x is a list (or vector) of length 408
    return max(0, x[31])
def l312_32(x):
    # x is a list (or vector) of length 408
    return max(0, x[32])
def l312_33(x):
    # x is a list (or vector) of length 408
    return max(0, x[33])
def l312_34(x):
    # x is a list (or vector) of length 408
    return max(0, x[34])
def l312_35(x):
    # x is a list (or vector) of length 408
    return max(0, x[35])
def l312_36(x):
    # x is a list (or vector) of length 408
    return max(0, x[36])
def l312_37(x):
    # x is a list (or vector) of length 408
    return max(0, x[37])
def l312_38(x):
    # x is a list (or vector) of length 408
    return max(0, x[38])
def l312_39(x):
    # x is a list (or vector) of length 408
    return max(0, x[39])
def l312_40(x):
    # x is a list (or vector) of length 408
    return max(0, x[40])
def l312_41(x):
    # x is a list (or vector) of length 408
    return max(0, x[41])
def l312_42(x):
    # x is a list (or vector) of length 408
    return max(0, x[42])
def l312_43(x):
    # x is a list (or vector) of length 408
    return max(0, x[43])
def l312_44(x):
    # x is a list (or vector) of length 408
    return max(0, x[44])
def l312_45(x):
    # x is a list (or vector) of length 408
    return max(0, x[45])
def l312_46(x):
    # x is a list (or vector) of length 408
    return max(0, x[46])
def l312_47(x):
    # x is a list (or vector) of length 408
    return max(0, x[47])
def l312_48(x):
    # x is a list (or vector) of length 408
    return max(0, x[48])
def l312_49(x):
    # x is a list (or vector) of length 408
    return max(0, x[49])
def l312_50(x):
    # x is a list (or vector) of length 408
    return max(0, x[50])
def l312_51(x):
    # x is a list (or vector) of length 408
    return max(0, x[51])
def l312_52(x):
    # x is a list (or vector) of length 408
    return max(0, x[52])
def l312_53(x):
    # x is a list (or vector) of length 408
    return max(0, x[53])
def l312_54(x):
    # x is a list (or vector) of length 408
    return max(0, x[54])
def l312_55(x):
    # x is a list (or vector) of length 408
    return max(0, x[55])
def l312_56(x):
    # x is a list (or vector) of length 408
    return max(0, x[56])
def l312_57(x):
    # x is a list (or vector) of length 408
    return max(0, x[57])
def l312_58(x):
    # x is a list (or vector) of length 408
    return max(0, x[58])
def l312_59(x):
    # x is a list (or vector) of length 408
    return max(0, x[59])
def l312_60(x):
    # x is a list (or vector) of length 408
    return max(0, x[60])
def l312_61(x):
    # x is a list (or vector) of length 408
    return max(0, x[61])
def l312_62(x):
    # x is a list (or vector) of length 408
    return max(0, x[62])
def l312_63(x):
    # x is a list (or vector) of length 408
    return max(0, x[63])
def l312_64(x):
    # x is a list (or vector) of length 408
    return max(0, x[64])
def l312_65(x):
    # x is a list (or vector) of length 408
    return max(0, x[65])
def l312_66(x):
    # x is a list (or vector) of length 408
    return max(0, x[66])
def l312_67(x):
    # x is a list (or vector) of length 408
    return max(0, x[67])
def l312_68(x):
    # x is a list (or vector) of length 408
    return max(0, x[68])
def l312_69(x):
    # x is a list (or vector) of length 408
    return max(0, x[69])
def l312_70(x):
    # x is a list (or vector) of length 408
    return max(0, x[70])
def l312_71(x):
    # x is a list (or vector) of length 408
    return max(0, x[71])
def l312_72(x):
    # x is a list (or vector) of length 408
    return max(0, x[72])
def l312_73(x):
    # x is a list (or vector) of length 408
    return max(0, x[73])
def l312_74(x):
    # x is a list (or vector) of length 408
    return max(0, x[74])
def l312_75(x):
    # x is a list (or vector) of length 408
    return max(0, x[75])
def l312_76(x):
    # x is a list (or vector) of length 408
    return max(0, x[76])
def l312_77(x):
    # x is a list (or vector) of length 408
    return max(0, x[77])
def l312_78(x):
    # x is a list (or vector) of length 408
    return max(0, x[78])
def l312_79(x):
    # x is a list (or vector) of length 408
    return max(0, x[79])
def l312_80(x):
    # x is a list (or vector) of length 408
    return max(0, x[80])
def l312_81(x):
    # x is a list (or vector) of length 408
    return max(0, x[81])
def l312_82(x):
    # x is a list (or vector) of length 408
    return max(0, x[82])
def l312_83(x):
    # x is a list (or vector) of length 408
    return max(0, x[83])
def l312_84(x):
    # x is a list (or vector) of length 408
    return max(0, x[84])
def l312_85(x):
    # x is a list (or vector) of length 408
    return max(0, x[85])
def l312_86(x):
    # x is a list (or vector) of length 408
    return max(0, x[86])
def l312_87(x):
    # x is a list (or vector) of length 408
    return max(0, x[87])
def l312_88(x):
    # x is a list (or vector) of length 408
    return max(0, x[88])
def l312_89(x):
    # x is a list (or vector) of length 408
    return max(0, x[89])
def l312_90(x):
    # x is a list (or vector) of length 408
    return max(0, x[90])
def l312_91(x):
    # x is a list (or vector) of length 408
    return max(0, x[91])
def l312_92(x):
    # x is a list (or vector) of length 408
    return max(0, x[92])
def l312_93(x):
    # x is a list (or vector) of length 408
    return max(0, x[93])
def l312_94(x):
    # x is a list (or vector) of length 408
    return max(0, x[94])
def l312_95(x):
    # x is a list (or vector) of length 408
    return max(0, x[95])
def l312_96(x):
    # x is a list (or vector) of length 408
    return max(0, x[96])
def l312_97(x):
    # x is a list (or vector) of length 408
    return max(0, x[97])
def l312_98(x):
    # x is a list (or vector) of length 408
    return max(0, x[98])
def l312_99(x):
    # x is a list (or vector) of length 408
    return max(0, x[99])
def l312_100(x):
    # x is a list (or vector) of length 408
    return max(0, x[100])
def l312_101(x):
    # x is a list (or vector) of length 408
    return max(0, x[101])
def l312_102(x):
    # x is a list (or vector) of length 408
    return max(0, x[102])
def l312_103(x):
    # x is a list (or vector) of length 408
    return max(0, x[103])
def l312_104(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[104] + 1.0)
def l312_105(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[105] + 1.0)
def l312_106(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[106] + 1.0)
def l312_107(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[107] + 1.0)
def l312_108(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[108] + 1.0)
def l312_109(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[109] + 1.0)
def l312_110(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[110] + 1.0)
def l312_111(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[111] + 1.0)
def l312_112(x):
    # x is a list (or vector) of length 408
    return max(0, x[96] + x[144] + -1.0)
def l312_113(x):
    # x is a list (or vector) of length 408
    return max(0, x[97] + x[145] + -1.0)
def l312_114(x):
    # x is a list (or vector) of length 408
    return max(0, x[98] + x[146] + -1.0)
def l312_115(x):
    # x is a list (or vector) of length 408
    return max(0, x[99] + x[147] + -1.0)
def l312_116(x):
    # x is a list (or vector) of length 408
    return max(0, x[100] + x[148] + -1.0)
def l312_117(x):
    # x is a list (or vector) of length 408
    return max(0, x[101] + x[149] + -1.0)
def l312_118(x):
    # x is a list (or vector) of length 408
    return max(0, x[102] + x[150] + -1.0)
def l312_119(x):
    # x is a list (or vector) of length 408
    return max(0, x[103] + x[151] + -1.0)
def l312_120(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[104] + x[152])
def l312_121(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[105] + x[153])
def l312_122(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[106] + x[154])
def l312_123(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[107] + x[155])
def l312_124(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[108] + x[156])
def l312_125(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[109] + x[157])
def l312_126(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[110] + x[158])
def l312_127(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[111] + x[159])
def l312_128(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[112] + 1.0)
def l312_129(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[113] + 1.0)
def l312_130(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[114] + 1.0)
def l312_131(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[115] + 1.0)
def l312_132(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[116] + 1.0)
def l312_133(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[117] + 1.0)
def l312_134(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[118] + 1.0)
def l312_135(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[119] + 1.0)
def l312_136(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[120] + 1.0)
def l312_137(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[121] + 1.0)
def l312_138(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[122] + 1.0)
def l312_139(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[123] + 1.0)
def l312_140(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[124] + 1.0)
def l312_141(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[125] + 1.0)
def l312_142(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[126] + 1.0)
def l312_143(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[127] + 1.0)
def l312_144(x):
    # x is a list (or vector) of length 408
    return max(0, x[128] + x[144] + -1.0)
def l312_145(x):
    # x is a list (or vector) of length 408
    return max(0, x[129] + x[145] + -1.0)
def l312_146(x):
    # x is a list (or vector) of length 408
    return max(0, x[130] + x[146] + -1.0)
def l312_147(x):
    # x is a list (or vector) of length 408
    return max(0, x[131] + x[147] + -1.0)
def l312_148(x):
    # x is a list (or vector) of length 408
    return max(0, x[132] + x[148] + -1.0)
def l312_149(x):
    # x is a list (or vector) of length 408
    return max(0, x[133] + x[149] + -1.0)
def l312_150(x):
    # x is a list (or vector) of length 408
    return max(0, x[134] + x[150] + -1.0)
def l312_151(x):
    # x is a list (or vector) of length 408
    return max(0, x[135] + x[151] + -1.0)
def l312_152(x):
    # x is a list (or vector) of length 408
    return max(0, x[136] + x[152] + -1.0)
def l312_153(x):
    # x is a list (or vector) of length 408
    return max(0, x[137] + x[153] + -1.0)
def l312_154(x):
    # x is a list (or vector) of length 408
    return max(0, x[138] + x[154] + -1.0)
def l312_155(x):
    # x is a list (or vector) of length 408
    return max(0, x[139] + x[155] + -1.0)
def l312_156(x):
    # x is a list (or vector) of length 408
    return max(0, x[140] + x[156] + -1.0)
def l312_157(x):
    # x is a list (or vector) of length 408
    return max(0, x[141] + x[157] + -1.0)
def l312_158(x):
    # x is a list (or vector) of length 408
    return max(0, x[142] + x[158] + -1.0)
def l312_159(x):
    # x is a list (or vector) of length 408
    return max(0, x[143] + x[159] + -1.0)
def l312_160(x):
    # x is a list (or vector) of length 408
    return max(0, x[128])
def l312_161(x):
    # x is a list (or vector) of length 408
    return max(0, x[129])
def l312_162(x):
    # x is a list (or vector) of length 408
    return max(0, x[130])
def l312_163(x):
    # x is a list (or vector) of length 408
    return max(0, x[131])
def l312_164(x):
    # x is a list (or vector) of length 408
    return max(0, x[132])
def l312_165(x):
    # x is a list (or vector) of length 408
    return max(0, x[133])
def l312_166(x):
    # x is a list (or vector) of length 408
    return max(0, x[134])
def l312_167(x):
    # x is a list (or vector) of length 408
    return max(0, x[135])
def l312_168(x):
    # x is a list (or vector) of length 408
    return max(0, x[136])
def l312_169(x):
    # x is a list (or vector) of length 408
    return max(0, x[137])
def l312_170(x):
    # x is a list (or vector) of length 408
    return max(0, x[138])
def l312_171(x):
    # x is a list (or vector) of length 408
    return max(0, x[139])
def l312_172(x):
    # x is a list (or vector) of length 408
    return max(0, x[140])
def l312_173(x):
    # x is a list (or vector) of length 408
    return max(0, x[141])
def l312_174(x):
    # x is a list (or vector) of length 408
    return max(0, x[142])
def l312_175(x):
    # x is a list (or vector) of length 408
    return max(0, x[143])
def l312_176(x):
    # x is a list (or vector) of length 408
    return max(0, x[160])
def l312_177(x):
    # x is a list (or vector) of length 408
    return max(0, x[161])
def l312_178(x):
    # x is a list (or vector) of length 408
    return max(0, x[162])
def l312_179(x):
    # x is a list (or vector) of length 408
    return max(0, x[163])
def l312_180(x):
    # x is a list (or vector) of length 408
    return max(0, x[164])
def l312_181(x):
    # x is a list (or vector) of length 408
    return max(0, x[165])
def l312_182(x):
    # x is a list (or vector) of length 408
    return max(0, x[166])
def l312_183(x):
    # x is a list (or vector) of length 408
    return max(0, x[167])
def l312_184(x):
    # x is a list (or vector) of length 408
    return max(0, x[168])
def l312_185(x):
    # x is a list (or vector) of length 408
    return max(0, x[169])
def l312_186(x):
    # x is a list (or vector) of length 408
    return max(0, x[170])
def l312_187(x):
    # x is a list (or vector) of length 408
    return max(0, x[171])
def l312_188(x):
    # x is a list (or vector) of length 408
    return max(0, x[172])
def l312_189(x):
    # x is a list (or vector) of length 408
    return max(0, x[173])
def l312_190(x):
    # x is a list (or vector) of length 408
    return max(0, x[174])
def l312_191(x):
    # x is a list (or vector) of length 408
    return max(0, x[175])
def l312_192(x):
    # x is a list (or vector) of length 408
    return max(0, x[176])
def l312_193(x):
    # x is a list (or vector) of length 408
    return max(0, x[177])
def l312_194(x):
    # x is a list (or vector) of length 408
    return max(0, x[178])
def l312_195(x):
    # x is a list (or vector) of length 408
    return max(0, x[179])
def l312_196(x):
    # x is a list (or vector) of length 408
    return max(0, x[180])
def l312_197(x):
    # x is a list (or vector) of length 408
    return max(0, x[181])
def l312_198(x):
    # x is a list (or vector) of length 408
    return max(0, x[182])
def l312_199(x):
    # x is a list (or vector) of length 408
    return max(0, x[183])
def l312_200(x):
    # x is a list (or vector) of length 408
    return max(0, x[184])
def l312_201(x):
    # x is a list (or vector) of length 408
    return max(0, x[185])
def l312_202(x):
    # x is a list (or vector) of length 408
    return max(0, x[186])
def l312_203(x):
    # x is a list (or vector) of length 408
    return max(0, x[187])
def l312_204(x):
    # x is a list (or vector) of length 408
    return max(0, x[188])
def l312_205(x):
    # x is a list (or vector) of length 408
    return max(0, x[189])
def l312_206(x):
    # x is a list (or vector) of length 408
    return max(0, x[190])
def l312_207(x):
    # x is a list (or vector) of length 408
    return max(0, x[191])
def l312_208(x):
    # x is a list (or vector) of length 408
    return max(0, x[192])
def l312_209(x):
    # x is a list (or vector) of length 408
    return max(0, x[193])
def l312_210(x):
    # x is a list (or vector) of length 408
    return max(0, x[194])
def l312_211(x):
    # x is a list (or vector) of length 408
    return max(0, x[195])
def l312_212(x):
    # x is a list (or vector) of length 408
    return max(0, x[196])
def l312_213(x):
    # x is a list (or vector) of length 408
    return max(0, x[197])
def l312_214(x):
    # x is a list (or vector) of length 408
    return max(0, x[198])
def l312_215(x):
    # x is a list (or vector) of length 408
    return max(0, x[199])
def l312_216(x):
    # x is a list (or vector) of length 408
    return max(0, x[200])
def l312_217(x):
    # x is a list (or vector) of length 408
    return max(0, x[201])
def l312_218(x):
    # x is a list (or vector) of length 408
    return max(0, x[202])
def l312_219(x):
    # x is a list (or vector) of length 408
    return max(0, x[203])
def l312_220(x):
    # x is a list (or vector) of length 408
    return max(0, x[204])
def l312_221(x):
    # x is a list (or vector) of length 408
    return max(0, x[205])
def l312_222(x):
    # x is a list (or vector) of length 408
    return max(0, x[206])
def l312_223(x):
    # x is a list (or vector) of length 408
    return max(0, x[207])
def l312_224(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[208] + -1.0*x[224] + 1.0)
def l312_225(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[209] + -1.0*x[225] + 1.0)
def l312_226(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[210] + -1.0*x[226] + 1.0)
def l312_227(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[211] + -1.0*x[227] + 1.0)
def l312_228(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[212] + -1.0*x[228] + 1.0)
def l312_229(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[213] + -1.0*x[229] + 1.0)
def l312_230(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[214] + -1.0*x[230] + 1.0)
def l312_231(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[215] + -1.0*x[231] + 1.0)
def l312_232(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[216] + -1.0*x[232] + 1.0)
def l312_233(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[217] + -1.0*x[233] + 1.0)
def l312_234(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[218] + -1.0*x[234] + 1.0)
def l312_235(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[219] + -1.0*x[235] + 1.0)
def l312_236(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[220] + -1.0*x[236] + 1.0)
def l312_237(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[221] + -1.0*x[237] + 1.0)
def l312_238(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[222] + -1.0*x[238] + 1.0)
def l312_239(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[223] + -1.0*x[239] + 1.0)
def l312_240(x):
    # x is a list (or vector) of length 408
    return max(0, x[256])
def l312_241(x):
    # x is a list (or vector) of length 408
    return max(0, x[257])
def l312_242(x):
    # x is a list (or vector) of length 408
    return max(0, x[258])
def l312_243(x):
    # x is a list (or vector) of length 408
    return max(0, x[259])
def l312_244(x):
    # x is a list (or vector) of length 408
    return max(0, x[260])
def l312_245(x):
    # x is a list (or vector) of length 408
    return max(0, x[261])
def l312_246(x):
    # x is a list (or vector) of length 408
    return max(0, x[262])
def l312_247(x):
    # x is a list (or vector) of length 408
    return max(0, x[263])
def l312_248(x):
    # x is a list (or vector) of length 408
    return max(0, x[264])
def l312_249(x):
    # x is a list (or vector) of length 408
    return max(0, x[265])
def l312_250(x):
    # x is a list (or vector) of length 408
    return max(0, x[266])
def l312_251(x):
    # x is a list (or vector) of length 408
    return max(0, x[267])
def l312_252(x):
    # x is a list (or vector) of length 408
    return max(0, x[268])
def l312_253(x):
    # x is a list (or vector) of length 408
    return max(0, x[269])
def l312_254(x):
    # x is a list (or vector) of length 408
    return max(0, x[270])
def l312_255(x):
    # x is a list (or vector) of length 408
    return max(0, x[271])
def l312_256(x):
    # x is a list (or vector) of length 408
    return max(0, x[240])
def l312_257(x):
    # x is a list (or vector) of length 408
    return max(0, x[241])
def l312_258(x):
    # x is a list (or vector) of length 408
    return max(0, x[242])
def l312_259(x):
    # x is a list (or vector) of length 408
    return max(0, x[243])
def l312_260(x):
    # x is a list (or vector) of length 408
    return max(0, x[244])
def l312_261(x):
    # x is a list (or vector) of length 408
    return max(0, x[245])
def l312_262(x):
    # x is a list (or vector) of length 408
    return max(0, x[246])
def l312_263(x):
    # x is a list (or vector) of length 408
    return max(0, x[247])
def l312_264(x):
    # x is a list (or vector) of length 408
    return max(0, x[248])
def l312_265(x):
    # x is a list (or vector) of length 408
    return max(0, x[249])
def l312_266(x):
    # x is a list (or vector) of length 408
    return max(0, x[250])
def l312_267(x):
    # x is a list (or vector) of length 408
    return max(0, x[251])
def l312_268(x):
    # x is a list (or vector) of length 408
    return max(0, x[252])
def l312_269(x):
    # x is a list (or vector) of length 408
    return max(0, x[253])
def l312_270(x):
    # x is a list (or vector) of length 408
    return max(0, x[254])
def l312_271(x):
    # x is a list (or vector) of length 408
    return max(0, x[255])
def l312_272(x):
    # x is a list (or vector) of length 408
    return max(0, x[272])
def l312_273(x):
    # x is a list (or vector) of length 408
    return max(0, x[273])
def l312_274(x):
    # x is a list (or vector) of length 408
    return max(0, x[274])
def l312_275(x):
    # x is a list (or vector) of length 408
    return max(0, x[275])
def l312_276(x):
    # x is a list (or vector) of length 408
    return max(0, x[276])
def l312_277(x):
    # x is a list (or vector) of length 408
    return max(0, x[277])
def l312_278(x):
    # x is a list (or vector) of length 408
    return max(0, x[278])
def l312_279(x):
    # x is a list (or vector) of length 408
    return max(0, x[279])
def l312_280(x):
    # x is a list (or vector) of length 408
    return max(0, x[280])
def l312_281(x):
    # x is a list (or vector) of length 408
    return max(0, x[281])
def l312_282(x):
    # x is a list (or vector) of length 408
    return max(0, x[282])
def l312_283(x):
    # x is a list (or vector) of length 408
    return max(0, x[283])
def l312_284(x):
    # x is a list (or vector) of length 408
    return max(0, x[284])
def l312_285(x):
    # x is a list (or vector) of length 408
    return max(0, x[285])
def l312_286(x):
    # x is a list (or vector) of length 408
    return max(0, x[286])
def l312_287(x):
    # x is a list (or vector) of length 408
    return max(0, x[287])
def l312_288(x):
    # x is a list (or vector) of length 408
    return max(0, x[288])
def l312_289(x):
    # x is a list (or vector) of length 408
    return max(0, x[289])
def l312_290(x):
    # x is a list (or vector) of length 408
    return max(0, x[290])
def l312_291(x):
    # x is a list (or vector) of length 408
    return max(0, x[291])
def l312_292(x):
    # x is a list (or vector) of length 408
    return max(0, x[292])
def l312_293(x):
    # x is a list (or vector) of length 408
    return max(0, x[293])
def l312_294(x):
    # x is a list (or vector) of length 408
    return max(0, x[294])
def l312_295(x):
    # x is a list (or vector) of length 408
    return max(0, x[295])
def l312_296(x):
    # x is a list (or vector) of length 408
    return max(0, x[296])
def l312_297(x):
    # x is a list (or vector) of length 408
    return max(0, x[297])
def l312_298(x):
    # x is a list (or vector) of length 408
    return max(0, x[298])
def l312_299(x):
    # x is a list (or vector) of length 408
    return max(0, x[299])
def l312_300(x):
    # x is a list (or vector) of length 408
    return max(0, x[300])
def l312_301(x):
    # x is a list (or vector) of length 408
    return max(0, x[301])
def l312_302(x):
    # x is a list (or vector) of length 408
    return max(0, x[302])
def l312_303(x):
    # x is a list (or vector) of length 408
    return max(0, x[303])
def l312_304(x):
    # x is a list (or vector) of length 408
    return max(0, x[304])
def l312_305(x):
    # x is a list (or vector) of length 408
    return max(0, x[305])
def l312_306(x):
    # x is a list (or vector) of length 408
    return max(0, x[306])
def l312_307(x):
    # x is a list (or vector) of length 408
    return max(0, x[307])
def l312_308(x):
    # x is a list (or vector) of length 408
    return max(0, x[308])
def l312_309(x):
    # x is a list (or vector) of length 408
    return max(0, x[309])
def l312_310(x):
    # x is a list (or vector) of length 408
    return max(0, x[310])
def l312_311(x):
    # x is a list (or vector) of length 408
    return max(0, x[311])
def l312_312(x):
    # x is a list (or vector) of length 408
    return max(0, x[312])
def l312_313(x):
    # x is a list (or vector) of length 408
    return max(0, x[313])
def l312_314(x):
    # x is a list (or vector) of length 408
    return max(0, x[314])
def l312_315(x):
    # x is a list (or vector) of length 408
    return max(0, x[315])
def l312_316(x):
    # x is a list (or vector) of length 408
    return max(0, x[316])
def l312_317(x):
    # x is a list (or vector) of length 408
    return max(0, x[317])
def l312_318(x):
    # x is a list (or vector) of length 408
    return max(0, x[318])
def l312_319(x):
    # x is a list (or vector) of length 408
    return max(0, x[319])
def l312_320(x):
    # x is a list (or vector) of length 408
    return max(0, x[320])
def l312_321(x):
    # x is a list (or vector) of length 408
    return max(0, x[321])
def l312_322(x):
    # x is a list (or vector) of length 408
    return max(0, x[322])
def l312_323(x):
    # x is a list (or vector) of length 408
    return max(0, x[323])
def l312_324(x):
    # x is a list (or vector) of length 408
    return max(0, x[324])
def l312_325(x):
    # x is a list (or vector) of length 408
    return max(0, x[325])
def l312_326(x):
    # x is a list (or vector) of length 408
    return max(0, x[326])
def l312_327(x):
    # x is a list (or vector) of length 408
    return max(0, x[327])
def l312_328(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[328] + 1.0)
def l312_329(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[329] + 1.0)
def l312_330(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[330] + 1.0)
def l312_331(x):
    # x is a list (or vector) of length 408
    return max(0, -1.0*x[331] + 1.0)
def l312_332(x):
    # x is a list (or vector) of length 408
    return max(0, x[332] + -2.0*x[336] + 2.0*x[340])
def l312_333(x):
    # x is a list (or vector) of length 408
    return max(0, x[333] + -2.0*x[337] + 2.0*x[341])
def l312_334(x):
    # x is a list (or vector) of length 408
    return max(0, x[334] + -2.0*x[338] + 2.0*x[342])
def l312_335(x):
    # x is a list (or vector) of length 408
    return max(0, x[335] + -2.0*x[339] + 2.0*x[343])
def l312_336(x):
    # x is a list (or vector) of length 408
    return max(0, x[344])
def l312_337(x):
    # x is a list (or vector) of length 408
    return max(0, x[345])
def l312_338(x):
    # x is a list (or vector) of length 408
    return max(0, x[346])
def l312_339(x):
    # x is a list (or vector) of length 408
    return max(0, x[347])
def l312_340(x):
    # x is a list (or vector) of length 408
    return max(0, x[348])
def l312_341(x):
    # x is a list (or vector) of length 408
    return max(0, x[349])
def l312_342(x):
    # x is a list (or vector) of length 408
    return max(0, x[350])
def l312_343(x):
    # x is a list (or vector) of length 408
    return max(0, x[351])
def l312_344(x):
    # x is a list (or vector) of length 408
    return max(0, x[352])
def l312_345(x):
    # x is a list (or vector) of length 408
    return max(0, x[353])
def l312_346(x):
    # x is a list (or vector) of length 408
    return max(0, x[354])
def l312_347(x):
    # x is a list (or vector) of length 408
    return max(0, x[355])
def l312_348(x):
    # x is a list (or vector) of length 408
    return max(0, x[356])
def l312_349(x):
    # x is a list (or vector) of length 408
    return max(0, x[357])
def l312_350(x):
    # x is a list (or vector) of length 408
    return max(0, x[358])
def l312_351(x):
    # x is a list (or vector) of length 408
    return max(0, x[359])
def l312_352(x):
    # x is a list (or vector) of length 408
    return max(0, x[360])
def l312_353(x):
    # x is a list (or vector) of length 408
    return max(0, x[361])
def l312_354(x):
    # x is a list (or vector) of length 408
    return max(0, x[362])
def l312_355(x):
    # x is a list (or vector) of length 408
    return max(0, x[363])
def l312_356(x):
    # x is a list (or vector) of length 408
    return max(0, x[364])
def l312_357(x):
    # x is a list (or vector) of length 408
    return max(0, x[365])
def l312_358(x):
    # x is a list (or vector) of length 408
    return max(0, x[366])
def l312_359(x):
    # x is a list (or vector) of length 408
    return max(0, x[367])
def l312_360(x):
    # x is a list (or vector) of length 408
    return max(0, x[368])
def l312_361(x):
    # x is a list (or vector) of length 408
    return max(0, x[369])
def l312_362(x):
    # x is a list (or vector) of length 408
    return max(0, x[370])
def l312_363(x):
    # x is a list (or vector) of length 408
    return max(0, x[371])
def l312_364(x):
    # x is a list (or vector) of length 408
    return max(0, x[372])
def l312_365(x):
    # x is a list (or vector) of length 408
    return max(0, x[373])
def l312_366(x):
    # x is a list (or vector) of length 408
    return max(0, x[374])
def l312_367(x):
    # x is a list (or vector) of length 408
    return max(0, x[375])
def l312_368(x):
    # x is a list (or vector) of length 408
    return max(0, x[376])
def l312_369(x):
    # x is a list (or vector) of length 408
    return max(0, x[377])
def l312_370(x):
    # x is a list (or vector) of length 408
    return max(0, x[378])
def l312_371(x):
    # x is a list (or vector) of length 408
    return max(0, x[379])
def l312_372(x):
    # x is a list (or vector) of length 408
    return max(0, x[380])
def l312_373(x):
    # x is a list (or vector) of length 408
    return max(0, x[381])
def l312_374(x):
    # x is a list (or vector) of length 408
    return max(0, x[382])
def l312_375(x):
    # x is a list (or vector) of length 408
    return max(0, x[383])
def l312_376(x):
    # x is a list (or vector) of length 408
    return max(0, x[384])
def l312_377(x):
    # x is a list (or vector) of length 408
    return max(0, x[385])
def l312_378(x):
    # x is a list (or vector) of length 408
    return max(0, x[386])
def l312_379(x):
    # x is a list (or vector) of length 408
    return max(0, x[387])
def l312_380(x):
    # x is a list (or vector) of length 408
    return max(0, x[388])
def l312_381(x):
    # x is a list (or vector) of length 408
    return max(0, x[389])
def l312_382(x):
    # x is a list (or vector) of length 408
    return max(0, x[390])
def l312_383(x):
    # x is a list (or vector) of length 408
    return max(0, x[391])
def l312_384(x):
    # x is a list (or vector) of length 408
    return max(0, x[392])
def l312_385(x):
    # x is a list (or vector) of length 408
    return max(0, x[393])
def l312_386(x):
    # x is a list (or vector) of length 408
    return max(0, x[394])
def l312_387(x):
    # x is a list (or vector) of length 408
    return max(0, x[395])
def l312_388(x):
    # x is a list (or vector) of length 408
    return max(0, x[396])
def l312_389(x):
    # x is a list (or vector) of length 408
    return max(0, x[397])
def l312_390(x):
    # x is a list (or vector) of length 408
    return max(0, x[398])
def l312_391(x):
    # x is a list (or vector) of length 408
    return max(0, x[399])
def l312_392(x):
    # x is a list (or vector) of length 408
    return max(0, x[400])
def l312_393(x):
    # x is a list (or vector) of length 408
    return max(0, x[401])
def l312_394(x):
    # x is a list (or vector) of length 408
    return max(0, x[402])
def l312_395(x):
    # x is a list (or vector) of length 408
    return max(0, x[403])
def l312_396(x):
    # x is a list (or vector) of length 408
    return max(0, x[404])
def l312_397(x):
    # x is a list (or vector) of length 408
    return max(0, x[405])
def l312_398(x):
    # x is a list (or vector) of length 408
    return max(0, x[406])
def l312_399(x):
    # x is a list (or vector) of length 408
    return max(0, x[407])
def l312_(x):
    # x is a list (or vector) of length 408
    return [
        l312_0(x),
        l312_1(x),
        l312_2(x),
        l312_3(x),
        l312_4(x),
        l312_5(x),
        l312_6(x),
        l312_7(x),
        l312_8(x),
        l312_9(x),
        l312_10(x),
        l312_11(x),
        l312_12(x),
        l312_13(x),
        l312_14(x),
        l312_15(x),
        l312_16(x),
        l312_17(x),
        l312_18(x),
        l312_19(x),
        l312_20(x),
        l312_21(x),
        l312_22(x),
        l312_23(x),
        l312_24(x),
        l312_25(x),
        l312_26(x),
        l312_27(x),
        l312_28(x),
        l312_29(x),
        l312_30(x),
        l312_31(x),
        l312_32(x),
        l312_33(x),
        l312_34(x),
        l312_35(x),
        l312_36(x),
        l312_37(x),
        l312_38(x),
        l312_39(x),
        l312_40(x),
        l312_41(x),
        l312_42(x),
        l312_43(x),
        l312_44(x),
        l312_45(x),
        l312_46(x),
        l312_47(x),
        l312_48(x),
        l312_49(x),
        l312_50(x),
        l312_51(x),
        l312_52(x),
        l312_53(x),
        l312_54(x),
        l312_55(x),
        l312_56(x),
        l312_57(x),
        l312_58(x),
        l312_59(x),
        l312_60(x),
        l312_61(x),
        l312_62(x),
        l312_63(x),
        l312_64(x),
        l312_65(x),
        l312_66(x),
        l312_67(x),
        l312_68(x),
        l312_69(x),
        l312_70(x),
        l312_71(x),
        l312_72(x),
        l312_73(x),
        l312_74(x),
        l312_75(x),
        l312_76(x),
        l312_77(x),
        l312_78(x),
        l312_79(x),
        l312_80(x),
        l312_81(x),
        l312_82(x),
        l312_83(x),
        l312_84(x),
        l312_85(x),
        l312_86(x),
        l312_87(x),
        l312_88(x),
        l312_89(x),
        l312_90(x),
        l312_91(x),
        l312_92(x),
        l312_93(x),
        l312_94(x),
        l312_95(x),
        l312_96(x),
        l312_97(x),
        l312_98(x),
        l312_99(x),
        l312_100(x),
        l312_101(x),
        l312_102(x),
        l312_103(x),
        l312_104(x),
        l312_105(x),
        l312_106(x),
        l312_107(x),
        l312_108(x),
        l312_109(x),
        l312_110(x),
        l312_111(x),
        l312_112(x),
        l312_113(x),
        l312_114(x),
        l312_115(x),
        l312_116(x),
        l312_117(x),
        l312_118(x),
        l312_119(x),
        l312_120(x),
        l312_121(x),
        l312_122(x),
        l312_123(x),
        l312_124(x),
        l312_125(x),
        l312_126(x),
        l312_127(x),
        l312_128(x),
        l312_129(x),
        l312_130(x),
        l312_131(x),
        l312_132(x),
        l312_133(x),
        l312_134(x),
        l312_135(x),
        l312_136(x),
        l312_137(x),
        l312_138(x),
        l312_139(x),
        l312_140(x),
        l312_141(x),
        l312_142(x),
        l312_143(x),
        l312_144(x),
        l312_145(x),
        l312_146(x),
        l312_147(x),
        l312_148(x),
        l312_149(x),
        l312_150(x),
        l312_151(x),
        l312_152(x),
        l312_153(x),
        l312_154(x),
        l312_155(x),
        l312_156(x),
        l312_157(x),
        l312_158(x),
        l312_159(x),
        l312_160(x),
        l312_161(x),
        l312_162(x),
        l312_163(x),
        l312_164(x),
        l312_165(x),
        l312_166(x),
        l312_167(x),
        l312_168(x),
        l312_169(x),
        l312_170(x),
        l312_171(x),
        l312_172(x),
        l312_173(x),
        l312_174(x),
        l312_175(x),
        l312_176(x),
        l312_177(x),
        l312_178(x),
        l312_179(x),
        l312_180(x),
        l312_181(x),
        l312_182(x),
        l312_183(x),
        l312_184(x),
        l312_185(x),
        l312_186(x),
        l312_187(x),
        l312_188(x),
        l312_189(x),
        l312_190(x),
        l312_191(x),
        l312_192(x),
        l312_193(x),
        l312_194(x),
        l312_195(x),
        l312_196(x),
        l312_197(x),
        l312_198(x),
        l312_199(x),
        l312_200(x),
        l312_201(x),
        l312_202(x),
        l312_203(x),
        l312_204(x),
        l312_205(x),
        l312_206(x),
        l312_207(x),
        l312_208(x),
        l312_209(x),
        l312_210(x),
        l312_211(x),
        l312_212(x),
        l312_213(x),
        l312_214(x),
        l312_215(x),
        l312_216(x),
        l312_217(x),
        l312_218(x),
        l312_219(x),
        l312_220(x),
        l312_221(x),
        l312_222(x),
        l312_223(x),
        l312_224(x),
        l312_225(x),
        l312_226(x),
        l312_227(x),
        l312_228(x),
        l312_229(x),
        l312_230(x),
        l312_231(x),
        l312_232(x),
        l312_233(x),
        l312_234(x),
        l312_235(x),
        l312_236(x),
        l312_237(x),
        l312_238(x),
        l312_239(x),
        l312_240(x),
        l312_241(x),
        l312_242(x),
        l312_243(x),
        l312_244(x),
        l312_245(x),
        l312_246(x),
        l312_247(x),
        l312_248(x),
        l312_249(x),
        l312_250(x),
        l312_251(x),
        l312_252(x),
        l312_253(x),
        l312_254(x),
        l312_255(x),
        l312_256(x),
        l312_257(x),
        l312_258(x),
        l312_259(x),
        l312_260(x),
        l312_261(x),
        l312_262(x),
        l312_263(x),
        l312_264(x),
        l312_265(x),
        l312_266(x),
        l312_267(x),
        l312_268(x),
        l312_269(x),
        l312_270(x),
        l312_271(x),
        l312_272(x),
        l312_273(x),
        l312_274(x),
        l312_275(x),
        l312_276(x),
        l312_277(x),
        l312_278(x),
        l312_279(x),
        l312_280(x),
        l312_281(x),
        l312_282(x),
        l312_283(x),
        l312_284(x),
        l312_285(x),
        l312_286(x),
        l312_287(x),
        l312_288(x),
        l312_289(x),
        l312_290(x),
        l312_291(x),
        l312_292(x),
        l312_293(x),
        l312_294(x),
        l312_295(x),
        l312_296(x),
        l312_297(x),
        l312_298(x),
        l312_299(x),
        l312_300(x),
        l312_301(x),
        l312_302(x),
        l312_303(x),
        l312_304(x),
        l312_305(x),
        l312_306(x),
        l312_307(x),
        l312_308(x),
        l312_309(x),
        l312_310(x),
        l312_311(x),
        l312_312(x),
        l312_313(x),
        l312_314(x),
        l312_315(x),
        l312_316(x),
        l312_317(x),
        l312_318(x),
        l312_319(x),
        l312_320(x),
        l312_321(x),
        l312_322(x),
        l312_323(x),
        l312_324(x),
        l312_325(x),
        l312_326(x),
        l312_327(x),
        l312_328(x),
        l312_329(x),
        l312_330(x),
        l312_331(x),
        l312_332(x),
        l312_333(x),
        l312_334(x),
        l312_335(x),
        l312_336(x),
        l312_337(x),
        l312_338(x),
        l312_339(x),
        l312_340(x),
        l312_341(x),
        l312_342(x),
        l312_343(x),
        l312_344(x),
        l312_345(x),
        l312_346(x),
        l312_347(x),
        l312_348(x),
        l312_349(x),
        l312_350(x),
        l312_351(x),
        l312_352(x),
        l312_353(x),
        l312_354(x),
        l312_355(x),
        l312_356(x),
        l312_357(x),
        l312_358(x),
        l312_359(x),
        l312_360(x),
        l312_361(x),
        l312_362(x),
        l312_363(x),
        l312_364(x),
        l312_365(x),
        l312_366(x),
        l312_367(x),
        l312_368(x),
        l312_369(x),
        l312_370(x),
        l312_371(x),
        l312_372(x),
        l312_373(x),
        l312_374(x),
        l312_375(x),
        l312_376(x),
        l312_377(x),
        l312_378(x),
        l312_379(x),
        l312_380(x),
        l312_381(x),
        l312_382(x),
        l312_383(x),
        l312_384(x),
        l312_385(x),
        l312_386(x),
        l312_387(x),
        l312_388(x),
        l312_389(x),
        l312_390(x),
        l312_391(x),
        l312_392(x),
        l312_393(x),
        l312_394(x),
        l312_395(x),
        l312_396(x),
        l312_397(x),
        l312_398(x),
        l312_399(x),
    ]