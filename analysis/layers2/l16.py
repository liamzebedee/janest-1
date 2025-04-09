import numpy as np




# Generated from reverse engineering
def l16_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 208
    out = np.empty(208, dtype=np.float32)
    
    # for i in range(0, 136):
    for i in range(0, 136):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xf (len=4)
    biases = [1.0, 1.0, 1.0, 1.0]
    # for i in range(136, 140):
    for i in range(0, 4):
        s = -1 * x[136 + i]
        s += biases[i]
        out[136 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(140, 144):
    for i in range(0, 4):
        s = x[140 + i] + -32.0 * x[i + 144] + 32.0 * x[i + 148]
        out[140 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(144, 208):
    for i in range(0, 64):
        s = x[152 + i]
        out[144 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l16_0(x):
    # x is a list (or vector) of length 216
    return max(0, x[0])
def l16_1(x):
    # x is a list (or vector) of length 216
    return max(0, x[1])
def l16_2(x):
    # x is a list (or vector) of length 216
    return max(0, x[2])
def l16_3(x):
    # x is a list (or vector) of length 216
    return max(0, x[3])
def l16_4(x):
    # x is a list (or vector) of length 216
    return max(0, x[4])
def l16_5(x):
    # x is a list (or vector) of length 216
    return max(0, x[5])
def l16_6(x):
    # x is a list (or vector) of length 216
    return max(0, x[6])
def l16_7(x):
    # x is a list (or vector) of length 216
    return max(0, x[7])
def l16_8(x):
    # x is a list (or vector) of length 216
    return max(0, x[8])
def l16_9(x):
    # x is a list (or vector) of length 216
    return max(0, x[9])
def l16_10(x):
    # x is a list (or vector) of length 216
    return max(0, x[10])
def l16_11(x):
    # x is a list (or vector) of length 216
    return max(0, x[11])
def l16_12(x):
    # x is a list (or vector) of length 216
    return max(0, x[12])
def l16_13(x):
    # x is a list (or vector) of length 216
    return max(0, x[13])
def l16_14(x):
    # x is a list (or vector) of length 216
    return max(0, x[14])
def l16_15(x):
    # x is a list (or vector) of length 216
    return max(0, x[15])
def l16_16(x):
    # x is a list (or vector) of length 216
    return max(0, x[16])
def l16_17(x):
    # x is a list (or vector) of length 216
    return max(0, x[17])
def l16_18(x):
    # x is a list (or vector) of length 216
    return max(0, x[18])
def l16_19(x):
    # x is a list (or vector) of length 216
    return max(0, x[19])
def l16_20(x):
    # x is a list (or vector) of length 216
    return max(0, x[20])
def l16_21(x):
    # x is a list (or vector) of length 216
    return max(0, x[21])
def l16_22(x):
    # x is a list (or vector) of length 216
    return max(0, x[22])
def l16_23(x):
    # x is a list (or vector) of length 216
    return max(0, x[23])
def l16_24(x):
    # x is a list (or vector) of length 216
    return max(0, x[24])
def l16_25(x):
    # x is a list (or vector) of length 216
    return max(0, x[25])
def l16_26(x):
    # x is a list (or vector) of length 216
    return max(0, x[26])
def l16_27(x):
    # x is a list (or vector) of length 216
    return max(0, x[27])
def l16_28(x):
    # x is a list (or vector) of length 216
    return max(0, x[28])
def l16_29(x):
    # x is a list (or vector) of length 216
    return max(0, x[29])
def l16_30(x):
    # x is a list (or vector) of length 216
    return max(0, x[30])
def l16_31(x):
    # x is a list (or vector) of length 216
    return max(0, x[31])
def l16_32(x):
    # x is a list (or vector) of length 216
    return max(0, x[32])
def l16_33(x):
    # x is a list (or vector) of length 216
    return max(0, x[33])
def l16_34(x):
    # x is a list (or vector) of length 216
    return max(0, x[34])
def l16_35(x):
    # x is a list (or vector) of length 216
    return max(0, x[35])
def l16_36(x):
    # x is a list (or vector) of length 216
    return max(0, x[36])
def l16_37(x):
    # x is a list (or vector) of length 216
    return max(0, x[37])
def l16_38(x):
    # x is a list (or vector) of length 216
    return max(0, x[38])
def l16_39(x):
    # x is a list (or vector) of length 216
    return max(0, x[39])
def l16_40(x):
    # x is a list (or vector) of length 216
    return max(0, x[40])
def l16_41(x):
    # x is a list (or vector) of length 216
    return max(0, x[41])
def l16_42(x):
    # x is a list (or vector) of length 216
    return max(0, x[42])
def l16_43(x):
    # x is a list (or vector) of length 216
    return max(0, x[43])
def l16_44(x):
    # x is a list (or vector) of length 216
    return max(0, x[44])
def l16_45(x):
    # x is a list (or vector) of length 216
    return max(0, x[45])
def l16_46(x):
    # x is a list (or vector) of length 216
    return max(0, x[46])
def l16_47(x):
    # x is a list (or vector) of length 216
    return max(0, x[47])
def l16_48(x):
    # x is a list (or vector) of length 216
    return max(0, x[48])
def l16_49(x):
    # x is a list (or vector) of length 216
    return max(0, x[49])
def l16_50(x):
    # x is a list (or vector) of length 216
    return max(0, x[50])
def l16_51(x):
    # x is a list (or vector) of length 216
    return max(0, x[51])
def l16_52(x):
    # x is a list (or vector) of length 216
    return max(0, x[52])
def l16_53(x):
    # x is a list (or vector) of length 216
    return max(0, x[53])
def l16_54(x):
    # x is a list (or vector) of length 216
    return max(0, x[54])
def l16_55(x):
    # x is a list (or vector) of length 216
    return max(0, x[55])
def l16_56(x):
    # x is a list (or vector) of length 216
    return max(0, x[56])
def l16_57(x):
    # x is a list (or vector) of length 216
    return max(0, x[57])
def l16_58(x):
    # x is a list (or vector) of length 216
    return max(0, x[58])
def l16_59(x):
    # x is a list (or vector) of length 216
    return max(0, x[59])
def l16_60(x):
    # x is a list (or vector) of length 216
    return max(0, x[60])
def l16_61(x):
    # x is a list (or vector) of length 216
    return max(0, x[61])
def l16_62(x):
    # x is a list (or vector) of length 216
    return max(0, x[62])
def l16_63(x):
    # x is a list (or vector) of length 216
    return max(0, x[63])
def l16_64(x):
    # x is a list (or vector) of length 216
    return max(0, x[64])
def l16_65(x):
    # x is a list (or vector) of length 216
    return max(0, x[65])
def l16_66(x):
    # x is a list (or vector) of length 216
    return max(0, x[66])
def l16_67(x):
    # x is a list (or vector) of length 216
    return max(0, x[67])
def l16_68(x):
    # x is a list (or vector) of length 216
    return max(0, x[68])
def l16_69(x):
    # x is a list (or vector) of length 216
    return max(0, x[69])
def l16_70(x):
    # x is a list (or vector) of length 216
    return max(0, x[70])
def l16_71(x):
    # x is a list (or vector) of length 216
    return max(0, x[71])
def l16_72(x):
    # x is a list (or vector) of length 216
    return max(0, x[72])
def l16_73(x):
    # x is a list (or vector) of length 216
    return max(0, x[73])
def l16_74(x):
    # x is a list (or vector) of length 216
    return max(0, x[74])
def l16_75(x):
    # x is a list (or vector) of length 216
    return max(0, x[75])
def l16_76(x):
    # x is a list (or vector) of length 216
    return max(0, x[76])
def l16_77(x):
    # x is a list (or vector) of length 216
    return max(0, x[77])
def l16_78(x):
    # x is a list (or vector) of length 216
    return max(0, x[78])
def l16_79(x):
    # x is a list (or vector) of length 216
    return max(0, x[79])
def l16_80(x):
    # x is a list (or vector) of length 216
    return max(0, x[80])
def l16_81(x):
    # x is a list (or vector) of length 216
    return max(0, x[81])
def l16_82(x):
    # x is a list (or vector) of length 216
    return max(0, x[82])
def l16_83(x):
    # x is a list (or vector) of length 216
    return max(0, x[83])
def l16_84(x):
    # x is a list (or vector) of length 216
    return max(0, x[84])
def l16_85(x):
    # x is a list (or vector) of length 216
    return max(0, x[85])
def l16_86(x):
    # x is a list (or vector) of length 216
    return max(0, x[86])
def l16_87(x):
    # x is a list (or vector) of length 216
    return max(0, x[87])
def l16_88(x):
    # x is a list (or vector) of length 216
    return max(0, x[88])
def l16_89(x):
    # x is a list (or vector) of length 216
    return max(0, x[89])
def l16_90(x):
    # x is a list (or vector) of length 216
    return max(0, x[90])
def l16_91(x):
    # x is a list (or vector) of length 216
    return max(0, x[91])
def l16_92(x):
    # x is a list (or vector) of length 216
    return max(0, x[92])
def l16_93(x):
    # x is a list (or vector) of length 216
    return max(0, x[93])
def l16_94(x):
    # x is a list (or vector) of length 216
    return max(0, x[94])
def l16_95(x):
    # x is a list (or vector) of length 216
    return max(0, x[95])
def l16_96(x):
    # x is a list (or vector) of length 216
    return max(0, x[96])
def l16_97(x):
    # x is a list (or vector) of length 216
    return max(0, x[97])
def l16_98(x):
    # x is a list (or vector) of length 216
    return max(0, x[98])
def l16_99(x):
    # x is a list (or vector) of length 216
    return max(0, x[99])
def l16_100(x):
    # x is a list (or vector) of length 216
    return max(0, x[100])
def l16_101(x):
    # x is a list (or vector) of length 216
    return max(0, x[101])
def l16_102(x):
    # x is a list (or vector) of length 216
    return max(0, x[102])
def l16_103(x):
    # x is a list (or vector) of length 216
    return max(0, x[103])
def l16_104(x):
    # x is a list (or vector) of length 216
    return max(0, x[104])
def l16_105(x):
    # x is a list (or vector) of length 216
    return max(0, x[105])
def l16_106(x):
    # x is a list (or vector) of length 216
    return max(0, x[106])
def l16_107(x):
    # x is a list (or vector) of length 216
    return max(0, x[107])
def l16_108(x):
    # x is a list (or vector) of length 216
    return max(0, x[108])
def l16_109(x):
    # x is a list (or vector) of length 216
    return max(0, x[109])
def l16_110(x):
    # x is a list (or vector) of length 216
    return max(0, x[110])
def l16_111(x):
    # x is a list (or vector) of length 216
    return max(0, x[111])
def l16_112(x):
    # x is a list (or vector) of length 216
    return max(0, x[112])
def l16_113(x):
    # x is a list (or vector) of length 216
    return max(0, x[113])
def l16_114(x):
    # x is a list (or vector) of length 216
    return max(0, x[114])
def l16_115(x):
    # x is a list (or vector) of length 216
    return max(0, x[115])
def l16_116(x):
    # x is a list (or vector) of length 216
    return max(0, x[116])
def l16_117(x):
    # x is a list (or vector) of length 216
    return max(0, x[117])
def l16_118(x):
    # x is a list (or vector) of length 216
    return max(0, x[118])
def l16_119(x):
    # x is a list (or vector) of length 216
    return max(0, x[119])
def l16_120(x):
    # x is a list (or vector) of length 216
    return max(0, x[120])
def l16_121(x):
    # x is a list (or vector) of length 216
    return max(0, x[121])
def l16_122(x):
    # x is a list (or vector) of length 216
    return max(0, x[122])
def l16_123(x):
    # x is a list (or vector) of length 216
    return max(0, x[123])
def l16_124(x):
    # x is a list (or vector) of length 216
    return max(0, x[124])
def l16_125(x):
    # x is a list (or vector) of length 216
    return max(0, x[125])
def l16_126(x):
    # x is a list (or vector) of length 216
    return max(0, x[126])
def l16_127(x):
    # x is a list (or vector) of length 216
    return max(0, x[127])
def l16_128(x):
    # x is a list (or vector) of length 216
    return max(0, x[128])
def l16_129(x):
    # x is a list (or vector) of length 216
    return max(0, x[129])
def l16_130(x):
    # x is a list (or vector) of length 216
    return max(0, x[130])
def l16_131(x):
    # x is a list (or vector) of length 216
    return max(0, x[131])
def l16_132(x):
    # x is a list (or vector) of length 216
    return max(0, x[132])
def l16_133(x):
    # x is a list (or vector) of length 216
    return max(0, x[133])
def l16_134(x):
    # x is a list (or vector) of length 216
    return max(0, x[134])
def l16_135(x):
    # x is a list (or vector) of length 216
    return max(0, x[135])
def l16_136(x):
    # x is a list (or vector) of length 216
    return max(0, -1.0*x[136] + 1.0)
def l16_137(x):
    # x is a list (or vector) of length 216
    return max(0, -1.0*x[137] + 1.0)
def l16_138(x):
    # x is a list (or vector) of length 216
    return max(0, -1.0*x[138] + 1.0)
def l16_139(x):
    # x is a list (or vector) of length 216
    return max(0, -1.0*x[139] + 1.0)
def l16_140(x):
    # x is a list (or vector) of length 216
    return max(0, x[140] + -32.0*x[144] + 32.0*x[148])
def l16_141(x):
    # x is a list (or vector) of length 216
    return max(0, x[141] + -32.0*x[145] + 32.0*x[149])
def l16_142(x):
    # x is a list (or vector) of length 216
    return max(0, x[142] + -32.0*x[146] + 32.0*x[150])
def l16_143(x):
    # x is a list (or vector) of length 216
    return max(0, x[143] + -32.0*x[147] + 32.0*x[151])
def l16_144(x):
    # x is a list (or vector) of length 216
    return max(0, x[152])
def l16_145(x):
    # x is a list (or vector) of length 216
    return max(0, x[153])
def l16_146(x):
    # x is a list (or vector) of length 216
    return max(0, x[154])
def l16_147(x):
    # x is a list (or vector) of length 216
    return max(0, x[155])
def l16_148(x):
    # x is a list (or vector) of length 216
    return max(0, x[156])
def l16_149(x):
    # x is a list (or vector) of length 216
    return max(0, x[157])
def l16_150(x):
    # x is a list (or vector) of length 216
    return max(0, x[158])
def l16_151(x):
    # x is a list (or vector) of length 216
    return max(0, x[159])
def l16_152(x):
    # x is a list (or vector) of length 216
    return max(0, x[160])
def l16_153(x):
    # x is a list (or vector) of length 216
    return max(0, x[161])
def l16_154(x):
    # x is a list (or vector) of length 216
    return max(0, x[162])
def l16_155(x):
    # x is a list (or vector) of length 216
    return max(0, x[163])
def l16_156(x):
    # x is a list (or vector) of length 216
    return max(0, x[164])
def l16_157(x):
    # x is a list (or vector) of length 216
    return max(0, x[165])
def l16_158(x):
    # x is a list (or vector) of length 216
    return max(0, x[166])
def l16_159(x):
    # x is a list (or vector) of length 216
    return max(0, x[167])
def l16_160(x):
    # x is a list (or vector) of length 216
    return max(0, x[168])
def l16_161(x):
    # x is a list (or vector) of length 216
    return max(0, x[169])
def l16_162(x):
    # x is a list (or vector) of length 216
    return max(0, x[170])
def l16_163(x):
    # x is a list (or vector) of length 216
    return max(0, x[171])
def l16_164(x):
    # x is a list (or vector) of length 216
    return max(0, x[172])
def l16_165(x):
    # x is a list (or vector) of length 216
    return max(0, x[173])
def l16_166(x):
    # x is a list (or vector) of length 216
    return max(0, x[174])
def l16_167(x):
    # x is a list (or vector) of length 216
    return max(0, x[175])
def l16_168(x):
    # x is a list (or vector) of length 216
    return max(0, x[176])
def l16_169(x):
    # x is a list (or vector) of length 216
    return max(0, x[177])
def l16_170(x):
    # x is a list (or vector) of length 216
    return max(0, x[178])
def l16_171(x):
    # x is a list (or vector) of length 216
    return max(0, x[179])
def l16_172(x):
    # x is a list (or vector) of length 216
    return max(0, x[180])
def l16_173(x):
    # x is a list (or vector) of length 216
    return max(0, x[181])
def l16_174(x):
    # x is a list (or vector) of length 216
    return max(0, x[182])
def l16_175(x):
    # x is a list (or vector) of length 216
    return max(0, x[183])
def l16_176(x):
    # x is a list (or vector) of length 216
    return max(0, x[184])
def l16_177(x):
    # x is a list (or vector) of length 216
    return max(0, x[185])
def l16_178(x):
    # x is a list (or vector) of length 216
    return max(0, x[186])
def l16_179(x):
    # x is a list (or vector) of length 216
    return max(0, x[187])
def l16_180(x):
    # x is a list (or vector) of length 216
    return max(0, x[188])
def l16_181(x):
    # x is a list (or vector) of length 216
    return max(0, x[189])
def l16_182(x):
    # x is a list (or vector) of length 216
    return max(0, x[190])
def l16_183(x):
    # x is a list (or vector) of length 216
    return max(0, x[191])
def l16_184(x):
    # x is a list (or vector) of length 216
    return max(0, x[192])
def l16_185(x):
    # x is a list (or vector) of length 216
    return max(0, x[193])
def l16_186(x):
    # x is a list (or vector) of length 216
    return max(0, x[194])
def l16_187(x):
    # x is a list (or vector) of length 216
    return max(0, x[195])
def l16_188(x):
    # x is a list (or vector) of length 216
    return max(0, x[196])
def l16_189(x):
    # x is a list (or vector) of length 216
    return max(0, x[197])
def l16_190(x):
    # x is a list (or vector) of length 216
    return max(0, x[198])
def l16_191(x):
    # x is a list (or vector) of length 216
    return max(0, x[199])
def l16_192(x):
    # x is a list (or vector) of length 216
    return max(0, x[200])
def l16_193(x):
    # x is a list (or vector) of length 216
    return max(0, x[201])
def l16_194(x):
    # x is a list (or vector) of length 216
    return max(0, x[202])
def l16_195(x):
    # x is a list (or vector) of length 216
    return max(0, x[203])
def l16_196(x):
    # x is a list (or vector) of length 216
    return max(0, x[204])
def l16_197(x):
    # x is a list (or vector) of length 216
    return max(0, x[205])
def l16_198(x):
    # x is a list (or vector) of length 216
    return max(0, x[206])
def l16_199(x):
    # x is a list (or vector) of length 216
    return max(0, x[207])
def l16_200(x):
    # x is a list (or vector) of length 216
    return max(0, x[208])
def l16_201(x):
    # x is a list (or vector) of length 216
    return max(0, x[209])
def l16_202(x):
    # x is a list (or vector) of length 216
    return max(0, x[210])
def l16_203(x):
    # x is a list (or vector) of length 216
    return max(0, x[211])
def l16_204(x):
    # x is a list (or vector) of length 216
    return max(0, x[212])
def l16_205(x):
    # x is a list (or vector) of length 216
    return max(0, x[213])
def l16_206(x):
    # x is a list (or vector) of length 216
    return max(0, x[214])
def l16_207(x):
    # x is a list (or vector) of length 216
    return max(0, x[215])
def l16_(x):
    # x is a list (or vector) of length 216
    return [
        l16_0(x),
        l16_1(x),
        l16_2(x),
        l16_3(x),
        l16_4(x),
        l16_5(x),
        l16_6(x),
        l16_7(x),
        l16_8(x),
        l16_9(x),
        l16_10(x),
        l16_11(x),
        l16_12(x),
        l16_13(x),
        l16_14(x),
        l16_15(x),
        l16_16(x),
        l16_17(x),
        l16_18(x),
        l16_19(x),
        l16_20(x),
        l16_21(x),
        l16_22(x),
        l16_23(x),
        l16_24(x),
        l16_25(x),
        l16_26(x),
        l16_27(x),
        l16_28(x),
        l16_29(x),
        l16_30(x),
        l16_31(x),
        l16_32(x),
        l16_33(x),
        l16_34(x),
        l16_35(x),
        l16_36(x),
        l16_37(x),
        l16_38(x),
        l16_39(x),
        l16_40(x),
        l16_41(x),
        l16_42(x),
        l16_43(x),
        l16_44(x),
        l16_45(x),
        l16_46(x),
        l16_47(x),
        l16_48(x),
        l16_49(x),
        l16_50(x),
        l16_51(x),
        l16_52(x),
        l16_53(x),
        l16_54(x),
        l16_55(x),
        l16_56(x),
        l16_57(x),
        l16_58(x),
        l16_59(x),
        l16_60(x),
        l16_61(x),
        l16_62(x),
        l16_63(x),
        l16_64(x),
        l16_65(x),
        l16_66(x),
        l16_67(x),
        l16_68(x),
        l16_69(x),
        l16_70(x),
        l16_71(x),
        l16_72(x),
        l16_73(x),
        l16_74(x),
        l16_75(x),
        l16_76(x),
        l16_77(x),
        l16_78(x),
        l16_79(x),
        l16_80(x),
        l16_81(x),
        l16_82(x),
        l16_83(x),
        l16_84(x),
        l16_85(x),
        l16_86(x),
        l16_87(x),
        l16_88(x),
        l16_89(x),
        l16_90(x),
        l16_91(x),
        l16_92(x),
        l16_93(x),
        l16_94(x),
        l16_95(x),
        l16_96(x),
        l16_97(x),
        l16_98(x),
        l16_99(x),
        l16_100(x),
        l16_101(x),
        l16_102(x),
        l16_103(x),
        l16_104(x),
        l16_105(x),
        l16_106(x),
        l16_107(x),
        l16_108(x),
        l16_109(x),
        l16_110(x),
        l16_111(x),
        l16_112(x),
        l16_113(x),
        l16_114(x),
        l16_115(x),
        l16_116(x),
        l16_117(x),
        l16_118(x),
        l16_119(x),
        l16_120(x),
        l16_121(x),
        l16_122(x),
        l16_123(x),
        l16_124(x),
        l16_125(x),
        l16_126(x),
        l16_127(x),
        l16_128(x),
        l16_129(x),
        l16_130(x),
        l16_131(x),
        l16_132(x),
        l16_133(x),
        l16_134(x),
        l16_135(x),
        l16_136(x),
        l16_137(x),
        l16_138(x),
        l16_139(x),
        l16_140(x),
        l16_141(x),
        l16_142(x),
        l16_143(x),
        l16_144(x),
        l16_145(x),
        l16_146(x),
        l16_147(x),
        l16_148(x),
        l16_149(x),
        l16_150(x),
        l16_151(x),
        l16_152(x),
        l16_153(x),
        l16_154(x),
        l16_155(x),
        l16_156(x),
        l16_157(x),
        l16_158(x),
        l16_159(x),
        l16_160(x),
        l16_161(x),
        l16_162(x),
        l16_163(x),
        l16_164(x),
        l16_165(x),
        l16_166(x),
        l16_167(x),
        l16_168(x),
        l16_169(x),
        l16_170(x),
        l16_171(x),
        l16_172(x),
        l16_173(x),
        l16_174(x),
        l16_175(x),
        l16_176(x),
        l16_177(x),
        l16_178(x),
        l16_179(x),
        l16_180(x),
        l16_181(x),
        l16_182(x),
        l16_183(x),
        l16_184(x),
        l16_185(x),
        l16_186(x),
        l16_187(x),
        l16_188(x),
        l16_189(x),
        l16_190(x),
        l16_191(x),
        l16_192(x),
        l16_193(x),
        l16_194(x),
        l16_195(x),
        l16_196(x),
        l16_197(x),
        l16_198(x),
        l16_199(x),
        l16_200(x),
        l16_201(x),
        l16_202(x),
        l16_203(x),
        l16_204(x),
        l16_205(x),
        l16_206(x),
        l16_207(x),
    ]