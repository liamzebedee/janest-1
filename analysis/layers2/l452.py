import numpy as np




# Generated from reverse engineering
def l452_g(x: np.ndarray) -> np.ndarray:
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




def l452_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l452_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l452_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l452_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l452_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l452_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l452_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l452_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l452_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l452_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l452_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l452_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l452_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l452_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l452_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l452_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l452_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l452_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l452_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l452_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l452_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l452_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l452_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l452_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l452_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l452_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l452_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l452_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l452_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l452_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l452_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l452_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l452_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l452_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[32] + x[97])
def l452_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[33] + x[98])
def l452_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[34] + x[99])
def l452_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[35] + x[100])
def l452_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[36] + x[101])
def l452_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[37] + x[102])
def l452_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[38] + x[103])
def l452_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[39] + x[104])
def l452_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[40] + x[105])
def l452_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[41] + x[106])
def l452_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[42] + x[107])
def l452_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[43] + x[108])
def l452_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[44] + x[109])
def l452_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[45] + x[110])
def l452_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[46] + x[111])
def l452_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[47] + x[112])
def l452_49(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + x[113] + 1.0)
def l452_50(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + x[114] + 1.0)
def l452_51(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + x[115] + 1.0)
def l452_52(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + x[116] + 1.0)
def l452_53(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + x[117] + 1.0)
def l452_54(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + x[118] + 1.0)
def l452_55(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + x[119] + 1.0)
def l452_56(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + x[120] + 1.0)
def l452_57(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + x[121] + 1.0)
def l452_58(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + x[122] + 1.0)
def l452_59(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + x[123] + 1.0)
def l452_60(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + x[124] + 1.0)
def l452_61(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + x[125] + 1.0)
def l452_62(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + x[126] + 1.0)
def l452_63(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[62] + x[127] + 1.0)
def l452_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + -1.0)
def l452_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[32] + x[97] + -1.0)
def l452_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[33] + x[98] + -1.0)
def l452_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[34] + x[99] + -1.0)
def l452_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[35] + x[100] + -1.0)
def l452_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[36] + x[101] + -1.0)
def l452_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[37] + x[102] + -1.0)
def l452_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[38] + x[103] + -1.0)
def l452_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[39] + x[104] + -1.0)
def l452_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[40] + x[105] + -1.0)
def l452_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[41] + x[106] + -1.0)
def l452_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[42] + x[107] + -1.0)
def l452_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[43] + x[108] + -1.0)
def l452_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[44] + x[109] + -1.0)
def l452_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[45] + x[110] + -1.0)
def l452_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[46] + x[111] + -1.0)
def l452_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[47] + x[112] + -1.0)
def l452_81(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + x[113])
def l452_82(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + x[114])
def l452_83(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + x[115])
def l452_84(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + x[116])
def l452_85(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + x[117])
def l452_86(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + x[118])
def l452_87(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + x[119])
def l452_88(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + x[120])
def l452_89(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + x[121])
def l452_90(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + x[122])
def l452_91(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + x[123])
def l452_92(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + x[124])
def l452_93(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + x[125])
def l452_94(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + x[126])
def l452_95(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[62] + x[127])
def l452_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l452_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l452_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l452_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l452_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l452_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l452_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l452_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l452_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l452_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l452_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l452_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l452_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l452_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l452_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l452_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l452_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[144])
def l452_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[145])
def l452_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[146])
def l452_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[147])
def l452_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[148])
def l452_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[149])
def l452_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[150])
def l452_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[151])
def l452_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[152])
def l452_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[153])
def l452_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[154])
def l452_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[155])
def l452_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[156])
def l452_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[157])
def l452_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[158])
def l452_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[159])
def l452_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l452_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l452_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l452_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l452_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l452_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l452_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l452_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l452_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l452_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l452_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l452_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l452_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l452_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l452_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l452_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l452_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l452_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l452_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l452_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l452_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l452_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l452_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l452_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l452_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l452_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l452_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l452_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l452_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l452_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l452_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l452_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l452_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l452_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l452_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l452_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l452_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l452_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l452_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l452_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l452_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l452_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l452_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l452_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l452_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l452_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l452_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l452_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l452_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l452_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l452_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l452_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l452_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l452_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l452_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l452_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l452_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l452_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l452_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l452_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l452_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l452_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l452_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l452_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l452_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l452_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l452_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l452_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l452_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l452_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l452_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l452_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l452_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l452_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l452_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l452_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l452_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l452_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l452_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l452_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l452_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l452_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l452_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l452_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l452_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l452_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l452_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l452_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l452_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l452_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l452_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l452_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l452_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l452_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l452_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l452_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l452_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l452_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l452_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l452_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l452_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l452_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l452_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l452_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l452_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l452_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l452_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l452_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l452_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l452_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l452_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l452_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l452_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l452_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l452_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l452_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l452_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l452_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l452_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l452_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l452_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l452_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l452_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l452_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l452_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l452_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l452_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l452_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l452_(x):
    # x is a list (or vector) of length 288
    return [
        l452_0(x),
        l452_1(x),
        l452_2(x),
        l452_3(x),
        l452_4(x),
        l452_5(x),
        l452_6(x),
        l452_7(x),
        l452_8(x),
        l452_9(x),
        l452_10(x),
        l452_11(x),
        l452_12(x),
        l452_13(x),
        l452_14(x),
        l452_15(x),
        l452_16(x),
        l452_17(x),
        l452_18(x),
        l452_19(x),
        l452_20(x),
        l452_21(x),
        l452_22(x),
        l452_23(x),
        l452_24(x),
        l452_25(x),
        l452_26(x),
        l452_27(x),
        l452_28(x),
        l452_29(x),
        l452_30(x),
        l452_31(x),
        l452_32(x),
        l452_33(x),
        l452_34(x),
        l452_35(x),
        l452_36(x),
        l452_37(x),
        l452_38(x),
        l452_39(x),
        l452_40(x),
        l452_41(x),
        l452_42(x),
        l452_43(x),
        l452_44(x),
        l452_45(x),
        l452_46(x),
        l452_47(x),
        l452_48(x),
        l452_49(x),
        l452_50(x),
        l452_51(x),
        l452_52(x),
        l452_53(x),
        l452_54(x),
        l452_55(x),
        l452_56(x),
        l452_57(x),
        l452_58(x),
        l452_59(x),
        l452_60(x),
        l452_61(x),
        l452_62(x),
        l452_63(x),
        l452_64(x),
        l452_65(x),
        l452_66(x),
        l452_67(x),
        l452_68(x),
        l452_69(x),
        l452_70(x),
        l452_71(x),
        l452_72(x),
        l452_73(x),
        l452_74(x),
        l452_75(x),
        l452_76(x),
        l452_77(x),
        l452_78(x),
        l452_79(x),
        l452_80(x),
        l452_81(x),
        l452_82(x),
        l452_83(x),
        l452_84(x),
        l452_85(x),
        l452_86(x),
        l452_87(x),
        l452_88(x),
        l452_89(x),
        l452_90(x),
        l452_91(x),
        l452_92(x),
        l452_93(x),
        l452_94(x),
        l452_95(x),
        l452_96(x),
        l452_97(x),
        l452_98(x),
        l452_99(x),
        l452_100(x),
        l452_101(x),
        l452_102(x),
        l452_103(x),
        l452_104(x),
        l452_105(x),
        l452_106(x),
        l452_107(x),
        l452_108(x),
        l452_109(x),
        l452_110(x),
        l452_111(x),
        l452_112(x),
        l452_113(x),
        l452_114(x),
        l452_115(x),
        l452_116(x),
        l452_117(x),
        l452_118(x),
        l452_119(x),
        l452_120(x),
        l452_121(x),
        l452_122(x),
        l452_123(x),
        l452_124(x),
        l452_125(x),
        l452_126(x),
        l452_127(x),
        l452_128(x),
        l452_129(x),
        l452_130(x),
        l452_131(x),
        l452_132(x),
        l452_133(x),
        l452_134(x),
        l452_135(x),
        l452_136(x),
        l452_137(x),
        l452_138(x),
        l452_139(x),
        l452_140(x),
        l452_141(x),
        l452_142(x),
        l452_143(x),
        l452_144(x),
        l452_145(x),
        l452_146(x),
        l452_147(x),
        l452_148(x),
        l452_149(x),
        l452_150(x),
        l452_151(x),
        l452_152(x),
        l452_153(x),
        l452_154(x),
        l452_155(x),
        l452_156(x),
        l452_157(x),
        l452_158(x),
        l452_159(x),
        l452_160(x),
        l452_161(x),
        l452_162(x),
        l452_163(x),
        l452_164(x),
        l452_165(x),
        l452_166(x),
        l452_167(x),
        l452_168(x),
        l452_169(x),
        l452_170(x),
        l452_171(x),
        l452_172(x),
        l452_173(x),
        l452_174(x),
        l452_175(x),
        l452_176(x),
        l452_177(x),
        l452_178(x),
        l452_179(x),
        l452_180(x),
        l452_181(x),
        l452_182(x),
        l452_183(x),
        l452_184(x),
        l452_185(x),
        l452_186(x),
        l452_187(x),
        l452_188(x),
        l452_189(x),
        l452_190(x),
        l452_191(x),
        l452_192(x),
        l452_193(x),
        l452_194(x),
        l452_195(x),
        l452_196(x),
        l452_197(x),
        l452_198(x),
        l452_199(x),
        l452_200(x),
        l452_201(x),
        l452_202(x),
        l452_203(x),
        l452_204(x),
        l452_205(x),
        l452_206(x),
        l452_207(x),
        l452_208(x),
        l452_209(x),
        l452_210(x),
        l452_211(x),
        l452_212(x),
        l452_213(x),
        l452_214(x),
        l452_215(x),
        l452_216(x),
        l452_217(x),
        l452_218(x),
        l452_219(x),
        l452_220(x),
        l452_221(x),
        l452_222(x),
        l452_223(x),
        l452_224(x),
        l452_225(x),
        l452_226(x),
        l452_227(x),
        l452_228(x),
        l452_229(x),
        l452_230(x),
        l452_231(x),
        l452_232(x),
        l452_233(x),
        l452_234(x),
        l452_235(x),
        l452_236(x),
        l452_237(x),
        l452_238(x),
        l452_239(x),
        l452_240(x),
        l452_241(x),
        l452_242(x),
        l452_243(x),
        l452_244(x),
        l452_245(x),
        l452_246(x),
        l452_247(x),
        l452_248(x),
        l452_249(x),
        l452_250(x),
        l452_251(x),
        l452_252(x),
        l452_253(x),
        l452_254(x),
        l452_255(x),
    ]