import numpy as np




# Generated from reverse engineering
def l368_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 256
    out = np.empty(256, dtype=np.float32)
    
    # for i in range(0, 32):
    for i in range(0, 32):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(32, 33):
    for i in range(0, 1):
        s = x[96 + i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(33, 49):
    for i in range(0, 16):
        s = x[32 + i] + x[97 + i]
        out[33 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x7fff (len=15)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(49, 64):
    for i in range(0, 15):
        s = x[113 + i] + -1 * x[48 + i]
        s += biases[i]
        out[49 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0]
    # for i in range(64, 65):
    for i in range(0, 1):
        s = x[96 + i]
        s += biases[i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(65, 81):
    for i in range(0, 16):
        s = x[32 + i] + x[97 + i]
        s += biases[i]
        out[65 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(81, 96):
    for i in range(0, 15):
        s = x[113 + i] + -1 * x[48 + i]
        out[81 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 256):
    for i in range(0, 160):
        s = x[128 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l368_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l368_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l368_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l368_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l368_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l368_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l368_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l368_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l368_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l368_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l368_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l368_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l368_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l368_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l368_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l368_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l368_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l368_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l368_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l368_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l368_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l368_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l368_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l368_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l368_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l368_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l368_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l368_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l368_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l368_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l368_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l368_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l368_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l368_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[32] + x[97])
def l368_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[33] + x[98])
def l368_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[34] + x[99])
def l368_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[35] + x[100])
def l368_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[36] + x[101])
def l368_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[37] + x[102])
def l368_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[38] + x[103])
def l368_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[39] + x[104])
def l368_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[40] + x[105])
def l368_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[41] + x[106])
def l368_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[42] + x[107])
def l368_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[43] + x[108])
def l368_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[44] + x[109])
def l368_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[45] + x[110])
def l368_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[46] + x[111])
def l368_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[47] + x[112])
def l368_49(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + x[113] + 1.0)
def l368_50(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + x[114] + 1.0)
def l368_51(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + x[115] + 1.0)
def l368_52(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + x[116] + 1.0)
def l368_53(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + x[117] + 1.0)
def l368_54(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + x[118] + 1.0)
def l368_55(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + x[119] + 1.0)
def l368_56(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + x[120] + 1.0)
def l368_57(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + x[121] + 1.0)
def l368_58(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + x[122] + 1.0)
def l368_59(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + x[123] + 1.0)
def l368_60(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + x[124] + 1.0)
def l368_61(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + x[125] + 1.0)
def l368_62(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + x[126] + 1.0)
def l368_63(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[62] + x[127] + 1.0)
def l368_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + -1.0)
def l368_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[32] + x[97] + -1.0)
def l368_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[33] + x[98] + -1.0)
def l368_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[34] + x[99] + -1.0)
def l368_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[35] + x[100] + -1.0)
def l368_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[36] + x[101] + -1.0)
def l368_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[37] + x[102] + -1.0)
def l368_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[38] + x[103] + -1.0)
def l368_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[39] + x[104] + -1.0)
def l368_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[40] + x[105] + -1.0)
def l368_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[41] + x[106] + -1.0)
def l368_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[42] + x[107] + -1.0)
def l368_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[43] + x[108] + -1.0)
def l368_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[44] + x[109] + -1.0)
def l368_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[45] + x[110] + -1.0)
def l368_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[46] + x[111] + -1.0)
def l368_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[47] + x[112] + -1.0)
def l368_81(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + x[113])
def l368_82(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + x[114])
def l368_83(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + x[115])
def l368_84(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + x[116])
def l368_85(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + x[117])
def l368_86(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + x[118])
def l368_87(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + x[119])
def l368_88(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + x[120])
def l368_89(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + x[121])
def l368_90(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + x[122])
def l368_91(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + x[123])
def l368_92(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + x[124])
def l368_93(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + x[125])
def l368_94(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + x[126])
def l368_95(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[62] + x[127])
def l368_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l368_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l368_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l368_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l368_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l368_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l368_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l368_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l368_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l368_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l368_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l368_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l368_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l368_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l368_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l368_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l368_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[144])
def l368_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[145])
def l368_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[146])
def l368_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[147])
def l368_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[148])
def l368_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[149])
def l368_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[150])
def l368_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[151])
def l368_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[152])
def l368_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[153])
def l368_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[154])
def l368_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[155])
def l368_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[156])
def l368_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[157])
def l368_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[158])
def l368_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[159])
def l368_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l368_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l368_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l368_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l368_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l368_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l368_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l368_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l368_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l368_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l368_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l368_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l368_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l368_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l368_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l368_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l368_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l368_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l368_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l368_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l368_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l368_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l368_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l368_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l368_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l368_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l368_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l368_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l368_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l368_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l368_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l368_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l368_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l368_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l368_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l368_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l368_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l368_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l368_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l368_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l368_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l368_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l368_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l368_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l368_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l368_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l368_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l368_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l368_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l368_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l368_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l368_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l368_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l368_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l368_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l368_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l368_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l368_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l368_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l368_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l368_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l368_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l368_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l368_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l368_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l368_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l368_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l368_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l368_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l368_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l368_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l368_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l368_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l368_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l368_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l368_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l368_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l368_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l368_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l368_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l368_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l368_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l368_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l368_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l368_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l368_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l368_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l368_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l368_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l368_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l368_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l368_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l368_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l368_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l368_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l368_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l368_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l368_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l368_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l368_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l368_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l368_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l368_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l368_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l368_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l368_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l368_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l368_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l368_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l368_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l368_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l368_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l368_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l368_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l368_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l368_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l368_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l368_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l368_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l368_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l368_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l368_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l368_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l368_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l368_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l368_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l368_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l368_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l368_(x):
    # x is a list (or vector) of length 288
    return [
        l368_0(x),
        l368_1(x),
        l368_2(x),
        l368_3(x),
        l368_4(x),
        l368_5(x),
        l368_6(x),
        l368_7(x),
        l368_8(x),
        l368_9(x),
        l368_10(x),
        l368_11(x),
        l368_12(x),
        l368_13(x),
        l368_14(x),
        l368_15(x),
        l368_16(x),
        l368_17(x),
        l368_18(x),
        l368_19(x),
        l368_20(x),
        l368_21(x),
        l368_22(x),
        l368_23(x),
        l368_24(x),
        l368_25(x),
        l368_26(x),
        l368_27(x),
        l368_28(x),
        l368_29(x),
        l368_30(x),
        l368_31(x),
        l368_32(x),
        l368_33(x),
        l368_34(x),
        l368_35(x),
        l368_36(x),
        l368_37(x),
        l368_38(x),
        l368_39(x),
        l368_40(x),
        l368_41(x),
        l368_42(x),
        l368_43(x),
        l368_44(x),
        l368_45(x),
        l368_46(x),
        l368_47(x),
        l368_48(x),
        l368_49(x),
        l368_50(x),
        l368_51(x),
        l368_52(x),
        l368_53(x),
        l368_54(x),
        l368_55(x),
        l368_56(x),
        l368_57(x),
        l368_58(x),
        l368_59(x),
        l368_60(x),
        l368_61(x),
        l368_62(x),
        l368_63(x),
        l368_64(x),
        l368_65(x),
        l368_66(x),
        l368_67(x),
        l368_68(x),
        l368_69(x),
        l368_70(x),
        l368_71(x),
        l368_72(x),
        l368_73(x),
        l368_74(x),
        l368_75(x),
        l368_76(x),
        l368_77(x),
        l368_78(x),
        l368_79(x),
        l368_80(x),
        l368_81(x),
        l368_82(x),
        l368_83(x),
        l368_84(x),
        l368_85(x),
        l368_86(x),
        l368_87(x),
        l368_88(x),
        l368_89(x),
        l368_90(x),
        l368_91(x),
        l368_92(x),
        l368_93(x),
        l368_94(x),
        l368_95(x),
        l368_96(x),
        l368_97(x),
        l368_98(x),
        l368_99(x),
        l368_100(x),
        l368_101(x),
        l368_102(x),
        l368_103(x),
        l368_104(x),
        l368_105(x),
        l368_106(x),
        l368_107(x),
        l368_108(x),
        l368_109(x),
        l368_110(x),
        l368_111(x),
        l368_112(x),
        l368_113(x),
        l368_114(x),
        l368_115(x),
        l368_116(x),
        l368_117(x),
        l368_118(x),
        l368_119(x),
        l368_120(x),
        l368_121(x),
        l368_122(x),
        l368_123(x),
        l368_124(x),
        l368_125(x),
        l368_126(x),
        l368_127(x),
        l368_128(x),
        l368_129(x),
        l368_130(x),
        l368_131(x),
        l368_132(x),
        l368_133(x),
        l368_134(x),
        l368_135(x),
        l368_136(x),
        l368_137(x),
        l368_138(x),
        l368_139(x),
        l368_140(x),
        l368_141(x),
        l368_142(x),
        l368_143(x),
        l368_144(x),
        l368_145(x),
        l368_146(x),
        l368_147(x),
        l368_148(x),
        l368_149(x),
        l368_150(x),
        l368_151(x),
        l368_152(x),
        l368_153(x),
        l368_154(x),
        l368_155(x),
        l368_156(x),
        l368_157(x),
        l368_158(x),
        l368_159(x),
        l368_160(x),
        l368_161(x),
        l368_162(x),
        l368_163(x),
        l368_164(x),
        l368_165(x),
        l368_166(x),
        l368_167(x),
        l368_168(x),
        l368_169(x),
        l368_170(x),
        l368_171(x),
        l368_172(x),
        l368_173(x),
        l368_174(x),
        l368_175(x),
        l368_176(x),
        l368_177(x),
        l368_178(x),
        l368_179(x),
        l368_180(x),
        l368_181(x),
        l368_182(x),
        l368_183(x),
        l368_184(x),
        l368_185(x),
        l368_186(x),
        l368_187(x),
        l368_188(x),
        l368_189(x),
        l368_190(x),
        l368_191(x),
        l368_192(x),
        l368_193(x),
        l368_194(x),
        l368_195(x),
        l368_196(x),
        l368_197(x),
        l368_198(x),
        l368_199(x),
        l368_200(x),
        l368_201(x),
        l368_202(x),
        l368_203(x),
        l368_204(x),
        l368_205(x),
        l368_206(x),
        l368_207(x),
        l368_208(x),
        l368_209(x),
        l368_210(x),
        l368_211(x),
        l368_212(x),
        l368_213(x),
        l368_214(x),
        l368_215(x),
        l368_216(x),
        l368_217(x),
        l368_218(x),
        l368_219(x),
        l368_220(x),
        l368_221(x),
        l368_222(x),
        l368_223(x),
        l368_224(x),
        l368_225(x),
        l368_226(x),
        l368_227(x),
        l368_228(x),
        l368_229(x),
        l368_230(x),
        l368_231(x),
        l368_232(x),
        l368_233(x),
        l368_234(x),
        l368_235(x),
        l368_236(x),
        l368_237(x),
        l368_238(x),
        l368_239(x),
        l368_240(x),
        l368_241(x),
        l368_242(x),
        l368_243(x),
        l368_244(x),
        l368_245(x),
        l368_246(x),
        l368_247(x),
        l368_248(x),
        l368_249(x),
        l368_250(x),
        l368_251(x),
        l368_252(x),
        l368_253(x),
        l368_254(x),
        l368_255(x),
    ]