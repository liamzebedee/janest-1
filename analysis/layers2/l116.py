import numpy as np




# Generated from reverse engineering
def l116_g(x: np.ndarray) -> np.ndarray:
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




def l116_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l116_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l116_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l116_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l116_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l116_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l116_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l116_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l116_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l116_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l116_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l116_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l116_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l116_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l116_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l116_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l116_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l116_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l116_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l116_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l116_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l116_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l116_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l116_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l116_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l116_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l116_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l116_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l116_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l116_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l116_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l116_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l116_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[96])
def l116_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[32] + x[97])
def l116_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[33] + x[98])
def l116_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[34] + x[99])
def l116_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[35] + x[100])
def l116_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[36] + x[101])
def l116_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[37] + x[102])
def l116_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[38] + x[103])
def l116_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[39] + x[104])
def l116_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[40] + x[105])
def l116_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[41] + x[106])
def l116_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[42] + x[107])
def l116_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[43] + x[108])
def l116_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[44] + x[109])
def l116_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[45] + x[110])
def l116_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[46] + x[111])
def l116_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[47] + x[112])
def l116_49(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + x[113] + 1.0)
def l116_50(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + x[114] + 1.0)
def l116_51(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + x[115] + 1.0)
def l116_52(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + x[116] + 1.0)
def l116_53(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + x[117] + 1.0)
def l116_54(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + x[118] + 1.0)
def l116_55(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + x[119] + 1.0)
def l116_56(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + x[120] + 1.0)
def l116_57(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + x[121] + 1.0)
def l116_58(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + x[122] + 1.0)
def l116_59(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + x[123] + 1.0)
def l116_60(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + x[124] + 1.0)
def l116_61(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + x[125] + 1.0)
def l116_62(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + x[126] + 1.0)
def l116_63(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[62] + x[127] + 1.0)
def l116_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + -1.0)
def l116_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[32] + x[97] + -1.0)
def l116_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[33] + x[98] + -1.0)
def l116_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[34] + x[99] + -1.0)
def l116_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[35] + x[100] + -1.0)
def l116_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[36] + x[101] + -1.0)
def l116_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[37] + x[102] + -1.0)
def l116_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[38] + x[103] + -1.0)
def l116_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[39] + x[104] + -1.0)
def l116_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[40] + x[105] + -1.0)
def l116_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[41] + x[106] + -1.0)
def l116_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[42] + x[107] + -1.0)
def l116_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[43] + x[108] + -1.0)
def l116_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[44] + x[109] + -1.0)
def l116_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[45] + x[110] + -1.0)
def l116_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[46] + x[111] + -1.0)
def l116_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[47] + x[112] + -1.0)
def l116_81(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[48] + x[113])
def l116_82(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[49] + x[114])
def l116_83(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[50] + x[115])
def l116_84(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[51] + x[116])
def l116_85(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[52] + x[117])
def l116_86(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[53] + x[118])
def l116_87(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[54] + x[119])
def l116_88(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[55] + x[120])
def l116_89(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[56] + x[121])
def l116_90(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[57] + x[122])
def l116_91(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[58] + x[123])
def l116_92(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[59] + x[124])
def l116_93(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[60] + x[125])
def l116_94(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[61] + x[126])
def l116_95(x):
    # x is a list (or vector) of length 288
    return max(0, -1.0*x[62] + x[127])
def l116_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[128])
def l116_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[129])
def l116_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[130])
def l116_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[131])
def l116_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[132])
def l116_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[133])
def l116_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[134])
def l116_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[135])
def l116_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[136])
def l116_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[137])
def l116_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[138])
def l116_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[139])
def l116_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[140])
def l116_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[141])
def l116_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[142])
def l116_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[143])
def l116_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[144])
def l116_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[145])
def l116_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[146])
def l116_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[147])
def l116_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[148])
def l116_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[149])
def l116_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[150])
def l116_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[151])
def l116_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[152])
def l116_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[153])
def l116_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[154])
def l116_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[155])
def l116_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[156])
def l116_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[157])
def l116_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[158])
def l116_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[159])
def l116_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[160])
def l116_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[161])
def l116_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[162])
def l116_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[163])
def l116_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[164])
def l116_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[165])
def l116_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[166])
def l116_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[167])
def l116_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[168])
def l116_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[169])
def l116_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[170])
def l116_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[171])
def l116_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[172])
def l116_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[173])
def l116_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[174])
def l116_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[175])
def l116_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[176])
def l116_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[177])
def l116_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[178])
def l116_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[179])
def l116_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[180])
def l116_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[181])
def l116_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[182])
def l116_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[183])
def l116_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[184])
def l116_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[185])
def l116_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[186])
def l116_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[187])
def l116_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[188])
def l116_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[189])
def l116_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[190])
def l116_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[191])
def l116_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l116_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l116_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l116_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l116_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l116_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l116_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l116_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l116_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l116_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l116_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l116_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l116_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l116_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l116_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l116_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l116_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l116_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l116_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l116_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l116_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l116_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l116_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l116_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l116_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l116_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l116_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l116_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l116_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l116_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l116_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l116_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l116_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l116_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l116_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l116_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l116_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l116_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l116_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l116_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l116_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l116_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l116_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l116_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l116_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l116_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l116_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l116_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l116_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l116_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l116_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l116_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l116_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l116_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l116_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l116_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l116_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l116_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l116_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l116_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l116_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l116_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l116_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l116_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l116_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l116_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l116_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l116_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l116_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l116_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l116_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l116_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l116_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l116_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l116_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l116_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l116_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l116_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l116_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l116_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l116_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l116_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l116_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l116_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l116_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l116_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l116_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l116_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l116_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l116_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l116_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l116_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l116_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l116_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l116_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l116_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l116_(x):
    # x is a list (or vector) of length 288
    return [
        l116_0(x),
        l116_1(x),
        l116_2(x),
        l116_3(x),
        l116_4(x),
        l116_5(x),
        l116_6(x),
        l116_7(x),
        l116_8(x),
        l116_9(x),
        l116_10(x),
        l116_11(x),
        l116_12(x),
        l116_13(x),
        l116_14(x),
        l116_15(x),
        l116_16(x),
        l116_17(x),
        l116_18(x),
        l116_19(x),
        l116_20(x),
        l116_21(x),
        l116_22(x),
        l116_23(x),
        l116_24(x),
        l116_25(x),
        l116_26(x),
        l116_27(x),
        l116_28(x),
        l116_29(x),
        l116_30(x),
        l116_31(x),
        l116_32(x),
        l116_33(x),
        l116_34(x),
        l116_35(x),
        l116_36(x),
        l116_37(x),
        l116_38(x),
        l116_39(x),
        l116_40(x),
        l116_41(x),
        l116_42(x),
        l116_43(x),
        l116_44(x),
        l116_45(x),
        l116_46(x),
        l116_47(x),
        l116_48(x),
        l116_49(x),
        l116_50(x),
        l116_51(x),
        l116_52(x),
        l116_53(x),
        l116_54(x),
        l116_55(x),
        l116_56(x),
        l116_57(x),
        l116_58(x),
        l116_59(x),
        l116_60(x),
        l116_61(x),
        l116_62(x),
        l116_63(x),
        l116_64(x),
        l116_65(x),
        l116_66(x),
        l116_67(x),
        l116_68(x),
        l116_69(x),
        l116_70(x),
        l116_71(x),
        l116_72(x),
        l116_73(x),
        l116_74(x),
        l116_75(x),
        l116_76(x),
        l116_77(x),
        l116_78(x),
        l116_79(x),
        l116_80(x),
        l116_81(x),
        l116_82(x),
        l116_83(x),
        l116_84(x),
        l116_85(x),
        l116_86(x),
        l116_87(x),
        l116_88(x),
        l116_89(x),
        l116_90(x),
        l116_91(x),
        l116_92(x),
        l116_93(x),
        l116_94(x),
        l116_95(x),
        l116_96(x),
        l116_97(x),
        l116_98(x),
        l116_99(x),
        l116_100(x),
        l116_101(x),
        l116_102(x),
        l116_103(x),
        l116_104(x),
        l116_105(x),
        l116_106(x),
        l116_107(x),
        l116_108(x),
        l116_109(x),
        l116_110(x),
        l116_111(x),
        l116_112(x),
        l116_113(x),
        l116_114(x),
        l116_115(x),
        l116_116(x),
        l116_117(x),
        l116_118(x),
        l116_119(x),
        l116_120(x),
        l116_121(x),
        l116_122(x),
        l116_123(x),
        l116_124(x),
        l116_125(x),
        l116_126(x),
        l116_127(x),
        l116_128(x),
        l116_129(x),
        l116_130(x),
        l116_131(x),
        l116_132(x),
        l116_133(x),
        l116_134(x),
        l116_135(x),
        l116_136(x),
        l116_137(x),
        l116_138(x),
        l116_139(x),
        l116_140(x),
        l116_141(x),
        l116_142(x),
        l116_143(x),
        l116_144(x),
        l116_145(x),
        l116_146(x),
        l116_147(x),
        l116_148(x),
        l116_149(x),
        l116_150(x),
        l116_151(x),
        l116_152(x),
        l116_153(x),
        l116_154(x),
        l116_155(x),
        l116_156(x),
        l116_157(x),
        l116_158(x),
        l116_159(x),
        l116_160(x),
        l116_161(x),
        l116_162(x),
        l116_163(x),
        l116_164(x),
        l116_165(x),
        l116_166(x),
        l116_167(x),
        l116_168(x),
        l116_169(x),
        l116_170(x),
        l116_171(x),
        l116_172(x),
        l116_173(x),
        l116_174(x),
        l116_175(x),
        l116_176(x),
        l116_177(x),
        l116_178(x),
        l116_179(x),
        l116_180(x),
        l116_181(x),
        l116_182(x),
        l116_183(x),
        l116_184(x),
        l116_185(x),
        l116_186(x),
        l116_187(x),
        l116_188(x),
        l116_189(x),
        l116_190(x),
        l116_191(x),
        l116_192(x),
        l116_193(x),
        l116_194(x),
        l116_195(x),
        l116_196(x),
        l116_197(x),
        l116_198(x),
        l116_199(x),
        l116_200(x),
        l116_201(x),
        l116_202(x),
        l116_203(x),
        l116_204(x),
        l116_205(x),
        l116_206(x),
        l116_207(x),
        l116_208(x),
        l116_209(x),
        l116_210(x),
        l116_211(x),
        l116_212(x),
        l116_213(x),
        l116_214(x),
        l116_215(x),
        l116_216(x),
        l116_217(x),
        l116_218(x),
        l116_219(x),
        l116_220(x),
        l116_221(x),
        l116_222(x),
        l116_223(x),
        l116_224(x),
        l116_225(x),
        l116_226(x),
        l116_227(x),
        l116_228(x),
        l116_229(x),
        l116_230(x),
        l116_231(x),
        l116_232(x),
        l116_233(x),
        l116_234(x),
        l116_235(x),
        l116_236(x),
        l116_237(x),
        l116_238(x),
        l116_239(x),
        l116_240(x),
        l116_241(x),
        l116_242(x),
        l116_243(x),
        l116_244(x),
        l116_245(x),
        l116_246(x),
        l116_247(x),
        l116_248(x),
        l116_249(x),
        l116_250(x),
        l116_251(x),
        l116_252(x),
        l116_253(x),
        l116_254(x),
        l116_255(x),
    ]