import numpy as np




# Generated from reverse engineering
def l12_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 204
    out = np.empty(204, dtype=np.float32)
    
    # for i in range(0, 132):
    for i in range(0, 132):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xf (len=4)
    biases = [1.0, 1.0, 1.0, 1.0]
    # for i in range(132, 136):
    for i in range(0, 4):
        s = -1 * x[132 + i]
        s += biases[i]
        out[132 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(136, 140):
    for i in range(0, 4):
        s = x[136 + i] + -64.0 * x[i + 140] + 64.0 * x[i + 144]
        out[136 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(140, 204):
    for i in range(0, 64):
        s = x[148 + i]
        out[140 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l12_0(x):
    # x is a list (or vector) of length 212
    return max(0, x[0])
def l12_1(x):
    # x is a list (or vector) of length 212
    return max(0, x[1])
def l12_2(x):
    # x is a list (or vector) of length 212
    return max(0, x[2])
def l12_3(x):
    # x is a list (or vector) of length 212
    return max(0, x[3])
def l12_4(x):
    # x is a list (or vector) of length 212
    return max(0, x[4])
def l12_5(x):
    # x is a list (or vector) of length 212
    return max(0, x[5])
def l12_6(x):
    # x is a list (or vector) of length 212
    return max(0, x[6])
def l12_7(x):
    # x is a list (or vector) of length 212
    return max(0, x[7])
def l12_8(x):
    # x is a list (or vector) of length 212
    return max(0, x[8])
def l12_9(x):
    # x is a list (or vector) of length 212
    return max(0, x[9])
def l12_10(x):
    # x is a list (or vector) of length 212
    return max(0, x[10])
def l12_11(x):
    # x is a list (or vector) of length 212
    return max(0, x[11])
def l12_12(x):
    # x is a list (or vector) of length 212
    return max(0, x[12])
def l12_13(x):
    # x is a list (or vector) of length 212
    return max(0, x[13])
def l12_14(x):
    # x is a list (or vector) of length 212
    return max(0, x[14])
def l12_15(x):
    # x is a list (or vector) of length 212
    return max(0, x[15])
def l12_16(x):
    # x is a list (or vector) of length 212
    return max(0, x[16])
def l12_17(x):
    # x is a list (or vector) of length 212
    return max(0, x[17])
def l12_18(x):
    # x is a list (or vector) of length 212
    return max(0, x[18])
def l12_19(x):
    # x is a list (or vector) of length 212
    return max(0, x[19])
def l12_20(x):
    # x is a list (or vector) of length 212
    return max(0, x[20])
def l12_21(x):
    # x is a list (or vector) of length 212
    return max(0, x[21])
def l12_22(x):
    # x is a list (or vector) of length 212
    return max(0, x[22])
def l12_23(x):
    # x is a list (or vector) of length 212
    return max(0, x[23])
def l12_24(x):
    # x is a list (or vector) of length 212
    return max(0, x[24])
def l12_25(x):
    # x is a list (or vector) of length 212
    return max(0, x[25])
def l12_26(x):
    # x is a list (or vector) of length 212
    return max(0, x[26])
def l12_27(x):
    # x is a list (or vector) of length 212
    return max(0, x[27])
def l12_28(x):
    # x is a list (or vector) of length 212
    return max(0, x[28])
def l12_29(x):
    # x is a list (or vector) of length 212
    return max(0, x[29])
def l12_30(x):
    # x is a list (or vector) of length 212
    return max(0, x[30])
def l12_31(x):
    # x is a list (or vector) of length 212
    return max(0, x[31])
def l12_32(x):
    # x is a list (or vector) of length 212
    return max(0, x[32])
def l12_33(x):
    # x is a list (or vector) of length 212
    return max(0, x[33])
def l12_34(x):
    # x is a list (or vector) of length 212
    return max(0, x[34])
def l12_35(x):
    # x is a list (or vector) of length 212
    return max(0, x[35])
def l12_36(x):
    # x is a list (or vector) of length 212
    return max(0, x[36])
def l12_37(x):
    # x is a list (or vector) of length 212
    return max(0, x[37])
def l12_38(x):
    # x is a list (or vector) of length 212
    return max(0, x[38])
def l12_39(x):
    # x is a list (or vector) of length 212
    return max(0, x[39])
def l12_40(x):
    # x is a list (or vector) of length 212
    return max(0, x[40])
def l12_41(x):
    # x is a list (or vector) of length 212
    return max(0, x[41])
def l12_42(x):
    # x is a list (or vector) of length 212
    return max(0, x[42])
def l12_43(x):
    # x is a list (or vector) of length 212
    return max(0, x[43])
def l12_44(x):
    # x is a list (or vector) of length 212
    return max(0, x[44])
def l12_45(x):
    # x is a list (or vector) of length 212
    return max(0, x[45])
def l12_46(x):
    # x is a list (or vector) of length 212
    return max(0, x[46])
def l12_47(x):
    # x is a list (or vector) of length 212
    return max(0, x[47])
def l12_48(x):
    # x is a list (or vector) of length 212
    return max(0, x[48])
def l12_49(x):
    # x is a list (or vector) of length 212
    return max(0, x[49])
def l12_50(x):
    # x is a list (or vector) of length 212
    return max(0, x[50])
def l12_51(x):
    # x is a list (or vector) of length 212
    return max(0, x[51])
def l12_52(x):
    # x is a list (or vector) of length 212
    return max(0, x[52])
def l12_53(x):
    # x is a list (or vector) of length 212
    return max(0, x[53])
def l12_54(x):
    # x is a list (or vector) of length 212
    return max(0, x[54])
def l12_55(x):
    # x is a list (or vector) of length 212
    return max(0, x[55])
def l12_56(x):
    # x is a list (or vector) of length 212
    return max(0, x[56])
def l12_57(x):
    # x is a list (or vector) of length 212
    return max(0, x[57])
def l12_58(x):
    # x is a list (or vector) of length 212
    return max(0, x[58])
def l12_59(x):
    # x is a list (or vector) of length 212
    return max(0, x[59])
def l12_60(x):
    # x is a list (or vector) of length 212
    return max(0, x[60])
def l12_61(x):
    # x is a list (or vector) of length 212
    return max(0, x[61])
def l12_62(x):
    # x is a list (or vector) of length 212
    return max(0, x[62])
def l12_63(x):
    # x is a list (or vector) of length 212
    return max(0, x[63])
def l12_64(x):
    # x is a list (or vector) of length 212
    return max(0, x[64])
def l12_65(x):
    # x is a list (or vector) of length 212
    return max(0, x[65])
def l12_66(x):
    # x is a list (or vector) of length 212
    return max(0, x[66])
def l12_67(x):
    # x is a list (or vector) of length 212
    return max(0, x[67])
def l12_68(x):
    # x is a list (or vector) of length 212
    return max(0, x[68])
def l12_69(x):
    # x is a list (or vector) of length 212
    return max(0, x[69])
def l12_70(x):
    # x is a list (or vector) of length 212
    return max(0, x[70])
def l12_71(x):
    # x is a list (or vector) of length 212
    return max(0, x[71])
def l12_72(x):
    # x is a list (or vector) of length 212
    return max(0, x[72])
def l12_73(x):
    # x is a list (or vector) of length 212
    return max(0, x[73])
def l12_74(x):
    # x is a list (or vector) of length 212
    return max(0, x[74])
def l12_75(x):
    # x is a list (or vector) of length 212
    return max(0, x[75])
def l12_76(x):
    # x is a list (or vector) of length 212
    return max(0, x[76])
def l12_77(x):
    # x is a list (or vector) of length 212
    return max(0, x[77])
def l12_78(x):
    # x is a list (or vector) of length 212
    return max(0, x[78])
def l12_79(x):
    # x is a list (or vector) of length 212
    return max(0, x[79])
def l12_80(x):
    # x is a list (or vector) of length 212
    return max(0, x[80])
def l12_81(x):
    # x is a list (or vector) of length 212
    return max(0, x[81])
def l12_82(x):
    # x is a list (or vector) of length 212
    return max(0, x[82])
def l12_83(x):
    # x is a list (or vector) of length 212
    return max(0, x[83])
def l12_84(x):
    # x is a list (or vector) of length 212
    return max(0, x[84])
def l12_85(x):
    # x is a list (or vector) of length 212
    return max(0, x[85])
def l12_86(x):
    # x is a list (or vector) of length 212
    return max(0, x[86])
def l12_87(x):
    # x is a list (or vector) of length 212
    return max(0, x[87])
def l12_88(x):
    # x is a list (or vector) of length 212
    return max(0, x[88])
def l12_89(x):
    # x is a list (or vector) of length 212
    return max(0, x[89])
def l12_90(x):
    # x is a list (or vector) of length 212
    return max(0, x[90])
def l12_91(x):
    # x is a list (or vector) of length 212
    return max(0, x[91])
def l12_92(x):
    # x is a list (or vector) of length 212
    return max(0, x[92])
def l12_93(x):
    # x is a list (or vector) of length 212
    return max(0, x[93])
def l12_94(x):
    # x is a list (or vector) of length 212
    return max(0, x[94])
def l12_95(x):
    # x is a list (or vector) of length 212
    return max(0, x[95])
def l12_96(x):
    # x is a list (or vector) of length 212
    return max(0, x[96])
def l12_97(x):
    # x is a list (or vector) of length 212
    return max(0, x[97])
def l12_98(x):
    # x is a list (or vector) of length 212
    return max(0, x[98])
def l12_99(x):
    # x is a list (or vector) of length 212
    return max(0, x[99])
def l12_100(x):
    # x is a list (or vector) of length 212
    return max(0, x[100])
def l12_101(x):
    # x is a list (or vector) of length 212
    return max(0, x[101])
def l12_102(x):
    # x is a list (or vector) of length 212
    return max(0, x[102])
def l12_103(x):
    # x is a list (or vector) of length 212
    return max(0, x[103])
def l12_104(x):
    # x is a list (or vector) of length 212
    return max(0, x[104])
def l12_105(x):
    # x is a list (or vector) of length 212
    return max(0, x[105])
def l12_106(x):
    # x is a list (or vector) of length 212
    return max(0, x[106])
def l12_107(x):
    # x is a list (or vector) of length 212
    return max(0, x[107])
def l12_108(x):
    # x is a list (or vector) of length 212
    return max(0, x[108])
def l12_109(x):
    # x is a list (or vector) of length 212
    return max(0, x[109])
def l12_110(x):
    # x is a list (or vector) of length 212
    return max(0, x[110])
def l12_111(x):
    # x is a list (or vector) of length 212
    return max(0, x[111])
def l12_112(x):
    # x is a list (or vector) of length 212
    return max(0, x[112])
def l12_113(x):
    # x is a list (or vector) of length 212
    return max(0, x[113])
def l12_114(x):
    # x is a list (or vector) of length 212
    return max(0, x[114])
def l12_115(x):
    # x is a list (or vector) of length 212
    return max(0, x[115])
def l12_116(x):
    # x is a list (or vector) of length 212
    return max(0, x[116])
def l12_117(x):
    # x is a list (or vector) of length 212
    return max(0, x[117])
def l12_118(x):
    # x is a list (or vector) of length 212
    return max(0, x[118])
def l12_119(x):
    # x is a list (or vector) of length 212
    return max(0, x[119])
def l12_120(x):
    # x is a list (or vector) of length 212
    return max(0, x[120])
def l12_121(x):
    # x is a list (or vector) of length 212
    return max(0, x[121])
def l12_122(x):
    # x is a list (or vector) of length 212
    return max(0, x[122])
def l12_123(x):
    # x is a list (or vector) of length 212
    return max(0, x[123])
def l12_124(x):
    # x is a list (or vector) of length 212
    return max(0, x[124])
def l12_125(x):
    # x is a list (or vector) of length 212
    return max(0, x[125])
def l12_126(x):
    # x is a list (or vector) of length 212
    return max(0, x[126])
def l12_127(x):
    # x is a list (or vector) of length 212
    return max(0, x[127])
def l12_128(x):
    # x is a list (or vector) of length 212
    return max(0, x[128])
def l12_129(x):
    # x is a list (or vector) of length 212
    return max(0, x[129])
def l12_130(x):
    # x is a list (or vector) of length 212
    return max(0, x[130])
def l12_131(x):
    # x is a list (or vector) of length 212
    return max(0, x[131])
def l12_132(x):
    # x is a list (or vector) of length 212
    return max(0, -1.0*x[132] + 1.0)
def l12_133(x):
    # x is a list (or vector) of length 212
    return max(0, -1.0*x[133] + 1.0)
def l12_134(x):
    # x is a list (or vector) of length 212
    return max(0, -1.0*x[134] + 1.0)
def l12_135(x):
    # x is a list (or vector) of length 212
    return max(0, -1.0*x[135] + 1.0)
def l12_136(x):
    # x is a list (or vector) of length 212
    return max(0, x[136] + -64.0*x[140] + 64.0*x[144])
def l12_137(x):
    # x is a list (or vector) of length 212
    return max(0, x[137] + -64.0*x[141] + 64.0*x[145])
def l12_138(x):
    # x is a list (or vector) of length 212
    return max(0, x[138] + -64.0*x[142] + 64.0*x[146])
def l12_139(x):
    # x is a list (or vector) of length 212
    return max(0, x[139] + -64.0*x[143] + 64.0*x[147])
def l12_140(x):
    # x is a list (or vector) of length 212
    return max(0, x[148])
def l12_141(x):
    # x is a list (or vector) of length 212
    return max(0, x[149])
def l12_142(x):
    # x is a list (or vector) of length 212
    return max(0, x[150])
def l12_143(x):
    # x is a list (or vector) of length 212
    return max(0, x[151])
def l12_144(x):
    # x is a list (or vector) of length 212
    return max(0, x[152])
def l12_145(x):
    # x is a list (or vector) of length 212
    return max(0, x[153])
def l12_146(x):
    # x is a list (or vector) of length 212
    return max(0, x[154])
def l12_147(x):
    # x is a list (or vector) of length 212
    return max(0, x[155])
def l12_148(x):
    # x is a list (or vector) of length 212
    return max(0, x[156])
def l12_149(x):
    # x is a list (or vector) of length 212
    return max(0, x[157])
def l12_150(x):
    # x is a list (or vector) of length 212
    return max(0, x[158])
def l12_151(x):
    # x is a list (or vector) of length 212
    return max(0, x[159])
def l12_152(x):
    # x is a list (or vector) of length 212
    return max(0, x[160])
def l12_153(x):
    # x is a list (or vector) of length 212
    return max(0, x[161])
def l12_154(x):
    # x is a list (or vector) of length 212
    return max(0, x[162])
def l12_155(x):
    # x is a list (or vector) of length 212
    return max(0, x[163])
def l12_156(x):
    # x is a list (or vector) of length 212
    return max(0, x[164])
def l12_157(x):
    # x is a list (or vector) of length 212
    return max(0, x[165])
def l12_158(x):
    # x is a list (or vector) of length 212
    return max(0, x[166])
def l12_159(x):
    # x is a list (or vector) of length 212
    return max(0, x[167])
def l12_160(x):
    # x is a list (or vector) of length 212
    return max(0, x[168])
def l12_161(x):
    # x is a list (or vector) of length 212
    return max(0, x[169])
def l12_162(x):
    # x is a list (or vector) of length 212
    return max(0, x[170])
def l12_163(x):
    # x is a list (or vector) of length 212
    return max(0, x[171])
def l12_164(x):
    # x is a list (or vector) of length 212
    return max(0, x[172])
def l12_165(x):
    # x is a list (or vector) of length 212
    return max(0, x[173])
def l12_166(x):
    # x is a list (or vector) of length 212
    return max(0, x[174])
def l12_167(x):
    # x is a list (or vector) of length 212
    return max(0, x[175])
def l12_168(x):
    # x is a list (or vector) of length 212
    return max(0, x[176])
def l12_169(x):
    # x is a list (or vector) of length 212
    return max(0, x[177])
def l12_170(x):
    # x is a list (or vector) of length 212
    return max(0, x[178])
def l12_171(x):
    # x is a list (or vector) of length 212
    return max(0, x[179])
def l12_172(x):
    # x is a list (or vector) of length 212
    return max(0, x[180])
def l12_173(x):
    # x is a list (or vector) of length 212
    return max(0, x[181])
def l12_174(x):
    # x is a list (or vector) of length 212
    return max(0, x[182])
def l12_175(x):
    # x is a list (or vector) of length 212
    return max(0, x[183])
def l12_176(x):
    # x is a list (or vector) of length 212
    return max(0, x[184])
def l12_177(x):
    # x is a list (or vector) of length 212
    return max(0, x[185])
def l12_178(x):
    # x is a list (or vector) of length 212
    return max(0, x[186])
def l12_179(x):
    # x is a list (or vector) of length 212
    return max(0, x[187])
def l12_180(x):
    # x is a list (or vector) of length 212
    return max(0, x[188])
def l12_181(x):
    # x is a list (or vector) of length 212
    return max(0, x[189])
def l12_182(x):
    # x is a list (or vector) of length 212
    return max(0, x[190])
def l12_183(x):
    # x is a list (or vector) of length 212
    return max(0, x[191])
def l12_184(x):
    # x is a list (or vector) of length 212
    return max(0, x[192])
def l12_185(x):
    # x is a list (or vector) of length 212
    return max(0, x[193])
def l12_186(x):
    # x is a list (or vector) of length 212
    return max(0, x[194])
def l12_187(x):
    # x is a list (or vector) of length 212
    return max(0, x[195])
def l12_188(x):
    # x is a list (or vector) of length 212
    return max(0, x[196])
def l12_189(x):
    # x is a list (or vector) of length 212
    return max(0, x[197])
def l12_190(x):
    # x is a list (or vector) of length 212
    return max(0, x[198])
def l12_191(x):
    # x is a list (or vector) of length 212
    return max(0, x[199])
def l12_192(x):
    # x is a list (or vector) of length 212
    return max(0, x[200])
def l12_193(x):
    # x is a list (or vector) of length 212
    return max(0, x[201])
def l12_194(x):
    # x is a list (or vector) of length 212
    return max(0, x[202])
def l12_195(x):
    # x is a list (or vector) of length 212
    return max(0, x[203])
def l12_196(x):
    # x is a list (or vector) of length 212
    return max(0, x[204])
def l12_197(x):
    # x is a list (or vector) of length 212
    return max(0, x[205])
def l12_198(x):
    # x is a list (or vector) of length 212
    return max(0, x[206])
def l12_199(x):
    # x is a list (or vector) of length 212
    return max(0, x[207])
def l12_200(x):
    # x is a list (or vector) of length 212
    return max(0, x[208])
def l12_201(x):
    # x is a list (or vector) of length 212
    return max(0, x[209])
def l12_202(x):
    # x is a list (or vector) of length 212
    return max(0, x[210])
def l12_203(x):
    # x is a list (or vector) of length 212
    return max(0, x[211])
def l12_(x):
    # x is a list (or vector) of length 212
    return [
        l12_0(x),
        l12_1(x),
        l12_2(x),
        l12_3(x),
        l12_4(x),
        l12_5(x),
        l12_6(x),
        l12_7(x),
        l12_8(x),
        l12_9(x),
        l12_10(x),
        l12_11(x),
        l12_12(x),
        l12_13(x),
        l12_14(x),
        l12_15(x),
        l12_16(x),
        l12_17(x),
        l12_18(x),
        l12_19(x),
        l12_20(x),
        l12_21(x),
        l12_22(x),
        l12_23(x),
        l12_24(x),
        l12_25(x),
        l12_26(x),
        l12_27(x),
        l12_28(x),
        l12_29(x),
        l12_30(x),
        l12_31(x),
        l12_32(x),
        l12_33(x),
        l12_34(x),
        l12_35(x),
        l12_36(x),
        l12_37(x),
        l12_38(x),
        l12_39(x),
        l12_40(x),
        l12_41(x),
        l12_42(x),
        l12_43(x),
        l12_44(x),
        l12_45(x),
        l12_46(x),
        l12_47(x),
        l12_48(x),
        l12_49(x),
        l12_50(x),
        l12_51(x),
        l12_52(x),
        l12_53(x),
        l12_54(x),
        l12_55(x),
        l12_56(x),
        l12_57(x),
        l12_58(x),
        l12_59(x),
        l12_60(x),
        l12_61(x),
        l12_62(x),
        l12_63(x),
        l12_64(x),
        l12_65(x),
        l12_66(x),
        l12_67(x),
        l12_68(x),
        l12_69(x),
        l12_70(x),
        l12_71(x),
        l12_72(x),
        l12_73(x),
        l12_74(x),
        l12_75(x),
        l12_76(x),
        l12_77(x),
        l12_78(x),
        l12_79(x),
        l12_80(x),
        l12_81(x),
        l12_82(x),
        l12_83(x),
        l12_84(x),
        l12_85(x),
        l12_86(x),
        l12_87(x),
        l12_88(x),
        l12_89(x),
        l12_90(x),
        l12_91(x),
        l12_92(x),
        l12_93(x),
        l12_94(x),
        l12_95(x),
        l12_96(x),
        l12_97(x),
        l12_98(x),
        l12_99(x),
        l12_100(x),
        l12_101(x),
        l12_102(x),
        l12_103(x),
        l12_104(x),
        l12_105(x),
        l12_106(x),
        l12_107(x),
        l12_108(x),
        l12_109(x),
        l12_110(x),
        l12_111(x),
        l12_112(x),
        l12_113(x),
        l12_114(x),
        l12_115(x),
        l12_116(x),
        l12_117(x),
        l12_118(x),
        l12_119(x),
        l12_120(x),
        l12_121(x),
        l12_122(x),
        l12_123(x),
        l12_124(x),
        l12_125(x),
        l12_126(x),
        l12_127(x),
        l12_128(x),
        l12_129(x),
        l12_130(x),
        l12_131(x),
        l12_132(x),
        l12_133(x),
        l12_134(x),
        l12_135(x),
        l12_136(x),
        l12_137(x),
        l12_138(x),
        l12_139(x),
        l12_140(x),
        l12_141(x),
        l12_142(x),
        l12_143(x),
        l12_144(x),
        l12_145(x),
        l12_146(x),
        l12_147(x),
        l12_148(x),
        l12_149(x),
        l12_150(x),
        l12_151(x),
        l12_152(x),
        l12_153(x),
        l12_154(x),
        l12_155(x),
        l12_156(x),
        l12_157(x),
        l12_158(x),
        l12_159(x),
        l12_160(x),
        l12_161(x),
        l12_162(x),
        l12_163(x),
        l12_164(x),
        l12_165(x),
        l12_166(x),
        l12_167(x),
        l12_168(x),
        l12_169(x),
        l12_170(x),
        l12_171(x),
        l12_172(x),
        l12_173(x),
        l12_174(x),
        l12_175(x),
        l12_176(x),
        l12_177(x),
        l12_178(x),
        l12_179(x),
        l12_180(x),
        l12_181(x),
        l12_182(x),
        l12_183(x),
        l12_184(x),
        l12_185(x),
        l12_186(x),
        l12_187(x),
        l12_188(x),
        l12_189(x),
        l12_190(x),
        l12_191(x),
        l12_192(x),
        l12_193(x),
        l12_194(x),
        l12_195(x),
        l12_196(x),
        l12_197(x),
        l12_198(x),
        l12_199(x),
        l12_200(x),
        l12_201(x),
        l12_202(x),
        l12_203(x),
    ]