import numpy as np




# Generated from reverse engineering
def l256_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 288
    out = np.empty(288, dtype=np.float32)
    
    # for i in range(0, 112):
    for i in range(0, 112):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffff (len=16)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(112, 128):
    for i in range(0, 16):
        s = -1 * x[112 + i] + -1 * x[128 + i]
        s += biases[i]
        out[112 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 144):
    for i in range(0, 16):
        s = x[160 + i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(144, 160):
    for i in range(0, 16):
        s = x[144 + i]
        out[144 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 288):
    for i in range(0, 128):
        s = x[176 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l256_0(x):
    # x is a list (or vector) of length 304
    return max(0, x[0])
def l256_1(x):
    # x is a list (or vector) of length 304
    return max(0, x[1])
def l256_2(x):
    # x is a list (or vector) of length 304
    return max(0, x[2])
def l256_3(x):
    # x is a list (or vector) of length 304
    return max(0, x[3])
def l256_4(x):
    # x is a list (or vector) of length 304
    return max(0, x[4])
def l256_5(x):
    # x is a list (or vector) of length 304
    return max(0, x[5])
def l256_6(x):
    # x is a list (or vector) of length 304
    return max(0, x[6])
def l256_7(x):
    # x is a list (or vector) of length 304
    return max(0, x[7])
def l256_8(x):
    # x is a list (or vector) of length 304
    return max(0, x[8])
def l256_9(x):
    # x is a list (or vector) of length 304
    return max(0, x[9])
def l256_10(x):
    # x is a list (or vector) of length 304
    return max(0, x[10])
def l256_11(x):
    # x is a list (or vector) of length 304
    return max(0, x[11])
def l256_12(x):
    # x is a list (or vector) of length 304
    return max(0, x[12])
def l256_13(x):
    # x is a list (or vector) of length 304
    return max(0, x[13])
def l256_14(x):
    # x is a list (or vector) of length 304
    return max(0, x[14])
def l256_15(x):
    # x is a list (or vector) of length 304
    return max(0, x[15])
def l256_16(x):
    # x is a list (or vector) of length 304
    return max(0, x[16])
def l256_17(x):
    # x is a list (or vector) of length 304
    return max(0, x[17])
def l256_18(x):
    # x is a list (or vector) of length 304
    return max(0, x[18])
def l256_19(x):
    # x is a list (or vector) of length 304
    return max(0, x[19])
def l256_20(x):
    # x is a list (or vector) of length 304
    return max(0, x[20])
def l256_21(x):
    # x is a list (or vector) of length 304
    return max(0, x[21])
def l256_22(x):
    # x is a list (or vector) of length 304
    return max(0, x[22])
def l256_23(x):
    # x is a list (or vector) of length 304
    return max(0, x[23])
def l256_24(x):
    # x is a list (or vector) of length 304
    return max(0, x[24])
def l256_25(x):
    # x is a list (or vector) of length 304
    return max(0, x[25])
def l256_26(x):
    # x is a list (or vector) of length 304
    return max(0, x[26])
def l256_27(x):
    # x is a list (or vector) of length 304
    return max(0, x[27])
def l256_28(x):
    # x is a list (or vector) of length 304
    return max(0, x[28])
def l256_29(x):
    # x is a list (or vector) of length 304
    return max(0, x[29])
def l256_30(x):
    # x is a list (or vector) of length 304
    return max(0, x[30])
def l256_31(x):
    # x is a list (or vector) of length 304
    return max(0, x[31])
def l256_32(x):
    # x is a list (or vector) of length 304
    return max(0, x[32])
def l256_33(x):
    # x is a list (or vector) of length 304
    return max(0, x[33])
def l256_34(x):
    # x is a list (or vector) of length 304
    return max(0, x[34])
def l256_35(x):
    # x is a list (or vector) of length 304
    return max(0, x[35])
def l256_36(x):
    # x is a list (or vector) of length 304
    return max(0, x[36])
def l256_37(x):
    # x is a list (or vector) of length 304
    return max(0, x[37])
def l256_38(x):
    # x is a list (or vector) of length 304
    return max(0, x[38])
def l256_39(x):
    # x is a list (or vector) of length 304
    return max(0, x[39])
def l256_40(x):
    # x is a list (or vector) of length 304
    return max(0, x[40])
def l256_41(x):
    # x is a list (or vector) of length 304
    return max(0, x[41])
def l256_42(x):
    # x is a list (or vector) of length 304
    return max(0, x[42])
def l256_43(x):
    # x is a list (or vector) of length 304
    return max(0, x[43])
def l256_44(x):
    # x is a list (or vector) of length 304
    return max(0, x[44])
def l256_45(x):
    # x is a list (or vector) of length 304
    return max(0, x[45])
def l256_46(x):
    # x is a list (or vector) of length 304
    return max(0, x[46])
def l256_47(x):
    # x is a list (or vector) of length 304
    return max(0, x[47])
def l256_48(x):
    # x is a list (or vector) of length 304
    return max(0, x[48])
def l256_49(x):
    # x is a list (or vector) of length 304
    return max(0, x[49])
def l256_50(x):
    # x is a list (or vector) of length 304
    return max(0, x[50])
def l256_51(x):
    # x is a list (or vector) of length 304
    return max(0, x[51])
def l256_52(x):
    # x is a list (or vector) of length 304
    return max(0, x[52])
def l256_53(x):
    # x is a list (or vector) of length 304
    return max(0, x[53])
def l256_54(x):
    # x is a list (or vector) of length 304
    return max(0, x[54])
def l256_55(x):
    # x is a list (or vector) of length 304
    return max(0, x[55])
def l256_56(x):
    # x is a list (or vector) of length 304
    return max(0, x[56])
def l256_57(x):
    # x is a list (or vector) of length 304
    return max(0, x[57])
def l256_58(x):
    # x is a list (or vector) of length 304
    return max(0, x[58])
def l256_59(x):
    # x is a list (or vector) of length 304
    return max(0, x[59])
def l256_60(x):
    # x is a list (or vector) of length 304
    return max(0, x[60])
def l256_61(x):
    # x is a list (or vector) of length 304
    return max(0, x[61])
def l256_62(x):
    # x is a list (or vector) of length 304
    return max(0, x[62])
def l256_63(x):
    # x is a list (or vector) of length 304
    return max(0, x[63])
def l256_64(x):
    # x is a list (or vector) of length 304
    return max(0, x[64])
def l256_65(x):
    # x is a list (or vector) of length 304
    return max(0, x[65])
def l256_66(x):
    # x is a list (or vector) of length 304
    return max(0, x[66])
def l256_67(x):
    # x is a list (or vector) of length 304
    return max(0, x[67])
def l256_68(x):
    # x is a list (or vector) of length 304
    return max(0, x[68])
def l256_69(x):
    # x is a list (or vector) of length 304
    return max(0, x[69])
def l256_70(x):
    # x is a list (or vector) of length 304
    return max(0, x[70])
def l256_71(x):
    # x is a list (or vector) of length 304
    return max(0, x[71])
def l256_72(x):
    # x is a list (or vector) of length 304
    return max(0, x[72])
def l256_73(x):
    # x is a list (or vector) of length 304
    return max(0, x[73])
def l256_74(x):
    # x is a list (or vector) of length 304
    return max(0, x[74])
def l256_75(x):
    # x is a list (or vector) of length 304
    return max(0, x[75])
def l256_76(x):
    # x is a list (or vector) of length 304
    return max(0, x[76])
def l256_77(x):
    # x is a list (or vector) of length 304
    return max(0, x[77])
def l256_78(x):
    # x is a list (or vector) of length 304
    return max(0, x[78])
def l256_79(x):
    # x is a list (or vector) of length 304
    return max(0, x[79])
def l256_80(x):
    # x is a list (or vector) of length 304
    return max(0, x[80])
def l256_81(x):
    # x is a list (or vector) of length 304
    return max(0, x[81])
def l256_82(x):
    # x is a list (or vector) of length 304
    return max(0, x[82])
def l256_83(x):
    # x is a list (or vector) of length 304
    return max(0, x[83])
def l256_84(x):
    # x is a list (or vector) of length 304
    return max(0, x[84])
def l256_85(x):
    # x is a list (or vector) of length 304
    return max(0, x[85])
def l256_86(x):
    # x is a list (or vector) of length 304
    return max(0, x[86])
def l256_87(x):
    # x is a list (or vector) of length 304
    return max(0, x[87])
def l256_88(x):
    # x is a list (or vector) of length 304
    return max(0, x[88])
def l256_89(x):
    # x is a list (or vector) of length 304
    return max(0, x[89])
def l256_90(x):
    # x is a list (or vector) of length 304
    return max(0, x[90])
def l256_91(x):
    # x is a list (or vector) of length 304
    return max(0, x[91])
def l256_92(x):
    # x is a list (or vector) of length 304
    return max(0, x[92])
def l256_93(x):
    # x is a list (or vector) of length 304
    return max(0, x[93])
def l256_94(x):
    # x is a list (or vector) of length 304
    return max(0, x[94])
def l256_95(x):
    # x is a list (or vector) of length 304
    return max(0, x[95])
def l256_96(x):
    # x is a list (or vector) of length 304
    return max(0, x[96])
def l256_97(x):
    # x is a list (or vector) of length 304
    return max(0, x[97])
def l256_98(x):
    # x is a list (or vector) of length 304
    return max(0, x[98])
def l256_99(x):
    # x is a list (or vector) of length 304
    return max(0, x[99])
def l256_100(x):
    # x is a list (or vector) of length 304
    return max(0, x[100])
def l256_101(x):
    # x is a list (or vector) of length 304
    return max(0, x[101])
def l256_102(x):
    # x is a list (or vector) of length 304
    return max(0, x[102])
def l256_103(x):
    # x is a list (or vector) of length 304
    return max(0, x[103])
def l256_104(x):
    # x is a list (or vector) of length 304
    return max(0, x[104])
def l256_105(x):
    # x is a list (or vector) of length 304
    return max(0, x[105])
def l256_106(x):
    # x is a list (or vector) of length 304
    return max(0, x[106])
def l256_107(x):
    # x is a list (or vector) of length 304
    return max(0, x[107])
def l256_108(x):
    # x is a list (or vector) of length 304
    return max(0, x[108])
def l256_109(x):
    # x is a list (or vector) of length 304
    return max(0, x[109])
def l256_110(x):
    # x is a list (or vector) of length 304
    return max(0, x[110])
def l256_111(x):
    # x is a list (or vector) of length 304
    return max(0, x[111])
def l256_112(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[112] + -1.0*x[128] + 1.0)
def l256_113(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[113] + -1.0*x[129] + 1.0)
def l256_114(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[114] + -1.0*x[130] + 1.0)
def l256_115(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[115] + -1.0*x[131] + 1.0)
def l256_116(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[116] + -1.0*x[132] + 1.0)
def l256_117(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[117] + -1.0*x[133] + 1.0)
def l256_118(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[118] + -1.0*x[134] + 1.0)
def l256_119(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[119] + -1.0*x[135] + 1.0)
def l256_120(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[120] + -1.0*x[136] + 1.0)
def l256_121(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[121] + -1.0*x[137] + 1.0)
def l256_122(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[122] + -1.0*x[138] + 1.0)
def l256_123(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[123] + -1.0*x[139] + 1.0)
def l256_124(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[124] + -1.0*x[140] + 1.0)
def l256_125(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[125] + -1.0*x[141] + 1.0)
def l256_126(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[126] + -1.0*x[142] + 1.0)
def l256_127(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[127] + -1.0*x[143] + 1.0)
def l256_128(x):
    # x is a list (or vector) of length 304
    return max(0, x[160])
def l256_129(x):
    # x is a list (or vector) of length 304
    return max(0, x[161])
def l256_130(x):
    # x is a list (or vector) of length 304
    return max(0, x[162])
def l256_131(x):
    # x is a list (or vector) of length 304
    return max(0, x[163])
def l256_132(x):
    # x is a list (or vector) of length 304
    return max(0, x[164])
def l256_133(x):
    # x is a list (or vector) of length 304
    return max(0, x[165])
def l256_134(x):
    # x is a list (or vector) of length 304
    return max(0, x[166])
def l256_135(x):
    # x is a list (or vector) of length 304
    return max(0, x[167])
def l256_136(x):
    # x is a list (or vector) of length 304
    return max(0, x[168])
def l256_137(x):
    # x is a list (or vector) of length 304
    return max(0, x[169])
def l256_138(x):
    # x is a list (or vector) of length 304
    return max(0, x[170])
def l256_139(x):
    # x is a list (or vector) of length 304
    return max(0, x[171])
def l256_140(x):
    # x is a list (or vector) of length 304
    return max(0, x[172])
def l256_141(x):
    # x is a list (or vector) of length 304
    return max(0, x[173])
def l256_142(x):
    # x is a list (or vector) of length 304
    return max(0, x[174])
def l256_143(x):
    # x is a list (or vector) of length 304
    return max(0, x[175])
def l256_144(x):
    # x is a list (or vector) of length 304
    return max(0, x[144])
def l256_145(x):
    # x is a list (or vector) of length 304
    return max(0, x[145])
def l256_146(x):
    # x is a list (or vector) of length 304
    return max(0, x[146])
def l256_147(x):
    # x is a list (or vector) of length 304
    return max(0, x[147])
def l256_148(x):
    # x is a list (or vector) of length 304
    return max(0, x[148])
def l256_149(x):
    # x is a list (or vector) of length 304
    return max(0, x[149])
def l256_150(x):
    # x is a list (or vector) of length 304
    return max(0, x[150])
def l256_151(x):
    # x is a list (or vector) of length 304
    return max(0, x[151])
def l256_152(x):
    # x is a list (or vector) of length 304
    return max(0, x[152])
def l256_153(x):
    # x is a list (or vector) of length 304
    return max(0, x[153])
def l256_154(x):
    # x is a list (or vector) of length 304
    return max(0, x[154])
def l256_155(x):
    # x is a list (or vector) of length 304
    return max(0, x[155])
def l256_156(x):
    # x is a list (or vector) of length 304
    return max(0, x[156])
def l256_157(x):
    # x is a list (or vector) of length 304
    return max(0, x[157])
def l256_158(x):
    # x is a list (or vector) of length 304
    return max(0, x[158])
def l256_159(x):
    # x is a list (or vector) of length 304
    return max(0, x[159])
def l256_160(x):
    # x is a list (or vector) of length 304
    return max(0, x[176])
def l256_161(x):
    # x is a list (or vector) of length 304
    return max(0, x[177])
def l256_162(x):
    # x is a list (or vector) of length 304
    return max(0, x[178])
def l256_163(x):
    # x is a list (or vector) of length 304
    return max(0, x[179])
def l256_164(x):
    # x is a list (or vector) of length 304
    return max(0, x[180])
def l256_165(x):
    # x is a list (or vector) of length 304
    return max(0, x[181])
def l256_166(x):
    # x is a list (or vector) of length 304
    return max(0, x[182])
def l256_167(x):
    # x is a list (or vector) of length 304
    return max(0, x[183])
def l256_168(x):
    # x is a list (or vector) of length 304
    return max(0, x[184])
def l256_169(x):
    # x is a list (or vector) of length 304
    return max(0, x[185])
def l256_170(x):
    # x is a list (or vector) of length 304
    return max(0, x[186])
def l256_171(x):
    # x is a list (or vector) of length 304
    return max(0, x[187])
def l256_172(x):
    # x is a list (or vector) of length 304
    return max(0, x[188])
def l256_173(x):
    # x is a list (or vector) of length 304
    return max(0, x[189])
def l256_174(x):
    # x is a list (or vector) of length 304
    return max(0, x[190])
def l256_175(x):
    # x is a list (or vector) of length 304
    return max(0, x[191])
def l256_176(x):
    # x is a list (or vector) of length 304
    return max(0, x[192])
def l256_177(x):
    # x is a list (or vector) of length 304
    return max(0, x[193])
def l256_178(x):
    # x is a list (or vector) of length 304
    return max(0, x[194])
def l256_179(x):
    # x is a list (or vector) of length 304
    return max(0, x[195])
def l256_180(x):
    # x is a list (or vector) of length 304
    return max(0, x[196])
def l256_181(x):
    # x is a list (or vector) of length 304
    return max(0, x[197])
def l256_182(x):
    # x is a list (or vector) of length 304
    return max(0, x[198])
def l256_183(x):
    # x is a list (or vector) of length 304
    return max(0, x[199])
def l256_184(x):
    # x is a list (or vector) of length 304
    return max(0, x[200])
def l256_185(x):
    # x is a list (or vector) of length 304
    return max(0, x[201])
def l256_186(x):
    # x is a list (or vector) of length 304
    return max(0, x[202])
def l256_187(x):
    # x is a list (or vector) of length 304
    return max(0, x[203])
def l256_188(x):
    # x is a list (or vector) of length 304
    return max(0, x[204])
def l256_189(x):
    # x is a list (or vector) of length 304
    return max(0, x[205])
def l256_190(x):
    # x is a list (or vector) of length 304
    return max(0, x[206])
def l256_191(x):
    # x is a list (or vector) of length 304
    return max(0, x[207])
def l256_192(x):
    # x is a list (or vector) of length 304
    return max(0, x[208])
def l256_193(x):
    # x is a list (or vector) of length 304
    return max(0, x[209])
def l256_194(x):
    # x is a list (or vector) of length 304
    return max(0, x[210])
def l256_195(x):
    # x is a list (or vector) of length 304
    return max(0, x[211])
def l256_196(x):
    # x is a list (or vector) of length 304
    return max(0, x[212])
def l256_197(x):
    # x is a list (or vector) of length 304
    return max(0, x[213])
def l256_198(x):
    # x is a list (or vector) of length 304
    return max(0, x[214])
def l256_199(x):
    # x is a list (or vector) of length 304
    return max(0, x[215])
def l256_200(x):
    # x is a list (or vector) of length 304
    return max(0, x[216])
def l256_201(x):
    # x is a list (or vector) of length 304
    return max(0, x[217])
def l256_202(x):
    # x is a list (or vector) of length 304
    return max(0, x[218])
def l256_203(x):
    # x is a list (or vector) of length 304
    return max(0, x[219])
def l256_204(x):
    # x is a list (or vector) of length 304
    return max(0, x[220])
def l256_205(x):
    # x is a list (or vector) of length 304
    return max(0, x[221])
def l256_206(x):
    # x is a list (or vector) of length 304
    return max(0, x[222])
def l256_207(x):
    # x is a list (or vector) of length 304
    return max(0, x[223])
def l256_208(x):
    # x is a list (or vector) of length 304
    return max(0, x[224])
def l256_209(x):
    # x is a list (or vector) of length 304
    return max(0, x[225])
def l256_210(x):
    # x is a list (or vector) of length 304
    return max(0, x[226])
def l256_211(x):
    # x is a list (or vector) of length 304
    return max(0, x[227])
def l256_212(x):
    # x is a list (or vector) of length 304
    return max(0, x[228])
def l256_213(x):
    # x is a list (or vector) of length 304
    return max(0, x[229])
def l256_214(x):
    # x is a list (or vector) of length 304
    return max(0, x[230])
def l256_215(x):
    # x is a list (or vector) of length 304
    return max(0, x[231])
def l256_216(x):
    # x is a list (or vector) of length 304
    return max(0, x[232])
def l256_217(x):
    # x is a list (or vector) of length 304
    return max(0, x[233])
def l256_218(x):
    # x is a list (or vector) of length 304
    return max(0, x[234])
def l256_219(x):
    # x is a list (or vector) of length 304
    return max(0, x[235])
def l256_220(x):
    # x is a list (or vector) of length 304
    return max(0, x[236])
def l256_221(x):
    # x is a list (or vector) of length 304
    return max(0, x[237])
def l256_222(x):
    # x is a list (or vector) of length 304
    return max(0, x[238])
def l256_223(x):
    # x is a list (or vector) of length 304
    return max(0, x[239])
def l256_224(x):
    # x is a list (or vector) of length 304
    return max(0, x[240])
def l256_225(x):
    # x is a list (or vector) of length 304
    return max(0, x[241])
def l256_226(x):
    # x is a list (or vector) of length 304
    return max(0, x[242])
def l256_227(x):
    # x is a list (or vector) of length 304
    return max(0, x[243])
def l256_228(x):
    # x is a list (or vector) of length 304
    return max(0, x[244])
def l256_229(x):
    # x is a list (or vector) of length 304
    return max(0, x[245])
def l256_230(x):
    # x is a list (or vector) of length 304
    return max(0, x[246])
def l256_231(x):
    # x is a list (or vector) of length 304
    return max(0, x[247])
def l256_232(x):
    # x is a list (or vector) of length 304
    return max(0, x[248])
def l256_233(x):
    # x is a list (or vector) of length 304
    return max(0, x[249])
def l256_234(x):
    # x is a list (or vector) of length 304
    return max(0, x[250])
def l256_235(x):
    # x is a list (or vector) of length 304
    return max(0, x[251])
def l256_236(x):
    # x is a list (or vector) of length 304
    return max(0, x[252])
def l256_237(x):
    # x is a list (or vector) of length 304
    return max(0, x[253])
def l256_238(x):
    # x is a list (or vector) of length 304
    return max(0, x[254])
def l256_239(x):
    # x is a list (or vector) of length 304
    return max(0, x[255])
def l256_240(x):
    # x is a list (or vector) of length 304
    return max(0, x[256])
def l256_241(x):
    # x is a list (or vector) of length 304
    return max(0, x[257])
def l256_242(x):
    # x is a list (or vector) of length 304
    return max(0, x[258])
def l256_243(x):
    # x is a list (or vector) of length 304
    return max(0, x[259])
def l256_244(x):
    # x is a list (or vector) of length 304
    return max(0, x[260])
def l256_245(x):
    # x is a list (or vector) of length 304
    return max(0, x[261])
def l256_246(x):
    # x is a list (or vector) of length 304
    return max(0, x[262])
def l256_247(x):
    # x is a list (or vector) of length 304
    return max(0, x[263])
def l256_248(x):
    # x is a list (or vector) of length 304
    return max(0, x[264])
def l256_249(x):
    # x is a list (or vector) of length 304
    return max(0, x[265])
def l256_250(x):
    # x is a list (or vector) of length 304
    return max(0, x[266])
def l256_251(x):
    # x is a list (or vector) of length 304
    return max(0, x[267])
def l256_252(x):
    # x is a list (or vector) of length 304
    return max(0, x[268])
def l256_253(x):
    # x is a list (or vector) of length 304
    return max(0, x[269])
def l256_254(x):
    # x is a list (or vector) of length 304
    return max(0, x[270])
def l256_255(x):
    # x is a list (or vector) of length 304
    return max(0, x[271])
def l256_256(x):
    # x is a list (or vector) of length 304
    return max(0, x[272])
def l256_257(x):
    # x is a list (or vector) of length 304
    return max(0, x[273])
def l256_258(x):
    # x is a list (or vector) of length 304
    return max(0, x[274])
def l256_259(x):
    # x is a list (or vector) of length 304
    return max(0, x[275])
def l256_260(x):
    # x is a list (or vector) of length 304
    return max(0, x[276])
def l256_261(x):
    # x is a list (or vector) of length 304
    return max(0, x[277])
def l256_262(x):
    # x is a list (or vector) of length 304
    return max(0, x[278])
def l256_263(x):
    # x is a list (or vector) of length 304
    return max(0, x[279])
def l256_264(x):
    # x is a list (or vector) of length 304
    return max(0, x[280])
def l256_265(x):
    # x is a list (or vector) of length 304
    return max(0, x[281])
def l256_266(x):
    # x is a list (or vector) of length 304
    return max(0, x[282])
def l256_267(x):
    # x is a list (or vector) of length 304
    return max(0, x[283])
def l256_268(x):
    # x is a list (or vector) of length 304
    return max(0, x[284])
def l256_269(x):
    # x is a list (or vector) of length 304
    return max(0, x[285])
def l256_270(x):
    # x is a list (or vector) of length 304
    return max(0, x[286])
def l256_271(x):
    # x is a list (or vector) of length 304
    return max(0, x[287])
def l256_272(x):
    # x is a list (or vector) of length 304
    return max(0, x[288])
def l256_273(x):
    # x is a list (or vector) of length 304
    return max(0, x[289])
def l256_274(x):
    # x is a list (or vector) of length 304
    return max(0, x[290])
def l256_275(x):
    # x is a list (or vector) of length 304
    return max(0, x[291])
def l256_276(x):
    # x is a list (or vector) of length 304
    return max(0, x[292])
def l256_277(x):
    # x is a list (or vector) of length 304
    return max(0, x[293])
def l256_278(x):
    # x is a list (or vector) of length 304
    return max(0, x[294])
def l256_279(x):
    # x is a list (or vector) of length 304
    return max(0, x[295])
def l256_280(x):
    # x is a list (or vector) of length 304
    return max(0, x[296])
def l256_281(x):
    # x is a list (or vector) of length 304
    return max(0, x[297])
def l256_282(x):
    # x is a list (or vector) of length 304
    return max(0, x[298])
def l256_283(x):
    # x is a list (or vector) of length 304
    return max(0, x[299])
def l256_284(x):
    # x is a list (or vector) of length 304
    return max(0, x[300])
def l256_285(x):
    # x is a list (or vector) of length 304
    return max(0, x[301])
def l256_286(x):
    # x is a list (or vector) of length 304
    return max(0, x[302])
def l256_287(x):
    # x is a list (or vector) of length 304
    return max(0, x[303])
def l256_(x):
    # x is a list (or vector) of length 304
    return [
        l256_0(x),
        l256_1(x),
        l256_2(x),
        l256_3(x),
        l256_4(x),
        l256_5(x),
        l256_6(x),
        l256_7(x),
        l256_8(x),
        l256_9(x),
        l256_10(x),
        l256_11(x),
        l256_12(x),
        l256_13(x),
        l256_14(x),
        l256_15(x),
        l256_16(x),
        l256_17(x),
        l256_18(x),
        l256_19(x),
        l256_20(x),
        l256_21(x),
        l256_22(x),
        l256_23(x),
        l256_24(x),
        l256_25(x),
        l256_26(x),
        l256_27(x),
        l256_28(x),
        l256_29(x),
        l256_30(x),
        l256_31(x),
        l256_32(x),
        l256_33(x),
        l256_34(x),
        l256_35(x),
        l256_36(x),
        l256_37(x),
        l256_38(x),
        l256_39(x),
        l256_40(x),
        l256_41(x),
        l256_42(x),
        l256_43(x),
        l256_44(x),
        l256_45(x),
        l256_46(x),
        l256_47(x),
        l256_48(x),
        l256_49(x),
        l256_50(x),
        l256_51(x),
        l256_52(x),
        l256_53(x),
        l256_54(x),
        l256_55(x),
        l256_56(x),
        l256_57(x),
        l256_58(x),
        l256_59(x),
        l256_60(x),
        l256_61(x),
        l256_62(x),
        l256_63(x),
        l256_64(x),
        l256_65(x),
        l256_66(x),
        l256_67(x),
        l256_68(x),
        l256_69(x),
        l256_70(x),
        l256_71(x),
        l256_72(x),
        l256_73(x),
        l256_74(x),
        l256_75(x),
        l256_76(x),
        l256_77(x),
        l256_78(x),
        l256_79(x),
        l256_80(x),
        l256_81(x),
        l256_82(x),
        l256_83(x),
        l256_84(x),
        l256_85(x),
        l256_86(x),
        l256_87(x),
        l256_88(x),
        l256_89(x),
        l256_90(x),
        l256_91(x),
        l256_92(x),
        l256_93(x),
        l256_94(x),
        l256_95(x),
        l256_96(x),
        l256_97(x),
        l256_98(x),
        l256_99(x),
        l256_100(x),
        l256_101(x),
        l256_102(x),
        l256_103(x),
        l256_104(x),
        l256_105(x),
        l256_106(x),
        l256_107(x),
        l256_108(x),
        l256_109(x),
        l256_110(x),
        l256_111(x),
        l256_112(x),
        l256_113(x),
        l256_114(x),
        l256_115(x),
        l256_116(x),
        l256_117(x),
        l256_118(x),
        l256_119(x),
        l256_120(x),
        l256_121(x),
        l256_122(x),
        l256_123(x),
        l256_124(x),
        l256_125(x),
        l256_126(x),
        l256_127(x),
        l256_128(x),
        l256_129(x),
        l256_130(x),
        l256_131(x),
        l256_132(x),
        l256_133(x),
        l256_134(x),
        l256_135(x),
        l256_136(x),
        l256_137(x),
        l256_138(x),
        l256_139(x),
        l256_140(x),
        l256_141(x),
        l256_142(x),
        l256_143(x),
        l256_144(x),
        l256_145(x),
        l256_146(x),
        l256_147(x),
        l256_148(x),
        l256_149(x),
        l256_150(x),
        l256_151(x),
        l256_152(x),
        l256_153(x),
        l256_154(x),
        l256_155(x),
        l256_156(x),
        l256_157(x),
        l256_158(x),
        l256_159(x),
        l256_160(x),
        l256_161(x),
        l256_162(x),
        l256_163(x),
        l256_164(x),
        l256_165(x),
        l256_166(x),
        l256_167(x),
        l256_168(x),
        l256_169(x),
        l256_170(x),
        l256_171(x),
        l256_172(x),
        l256_173(x),
        l256_174(x),
        l256_175(x),
        l256_176(x),
        l256_177(x),
        l256_178(x),
        l256_179(x),
        l256_180(x),
        l256_181(x),
        l256_182(x),
        l256_183(x),
        l256_184(x),
        l256_185(x),
        l256_186(x),
        l256_187(x),
        l256_188(x),
        l256_189(x),
        l256_190(x),
        l256_191(x),
        l256_192(x),
        l256_193(x),
        l256_194(x),
        l256_195(x),
        l256_196(x),
        l256_197(x),
        l256_198(x),
        l256_199(x),
        l256_200(x),
        l256_201(x),
        l256_202(x),
        l256_203(x),
        l256_204(x),
        l256_205(x),
        l256_206(x),
        l256_207(x),
        l256_208(x),
        l256_209(x),
        l256_210(x),
        l256_211(x),
        l256_212(x),
        l256_213(x),
        l256_214(x),
        l256_215(x),
        l256_216(x),
        l256_217(x),
        l256_218(x),
        l256_219(x),
        l256_220(x),
        l256_221(x),
        l256_222(x),
        l256_223(x),
        l256_224(x),
        l256_225(x),
        l256_226(x),
        l256_227(x),
        l256_228(x),
        l256_229(x),
        l256_230(x),
        l256_231(x),
        l256_232(x),
        l256_233(x),
        l256_234(x),
        l256_235(x),
        l256_236(x),
        l256_237(x),
        l256_238(x),
        l256_239(x),
        l256_240(x),
        l256_241(x),
        l256_242(x),
        l256_243(x),
        l256_244(x),
        l256_245(x),
        l256_246(x),
        l256_247(x),
        l256_248(x),
        l256_249(x),
        l256_250(x),
        l256_251(x),
        l256_252(x),
        l256_253(x),
        l256_254(x),
        l256_255(x),
        l256_256(x),
        l256_257(x),
        l256_258(x),
        l256_259(x),
        l256_260(x),
        l256_261(x),
        l256_262(x),
        l256_263(x),
        l256_264(x),
        l256_265(x),
        l256_266(x),
        l256_267(x),
        l256_268(x),
        l256_269(x),
        l256_270(x),
        l256_271(x),
        l256_272(x),
        l256_273(x),
        l256_274(x),
        l256_275(x),
        l256_276(x),
        l256_277(x),
        l256_278(x),
        l256_279(x),
        l256_280(x),
        l256_281(x),
        l256_282(x),
        l256_283(x),
        l256_284(x),
        l256_285(x),
        l256_286(x),
        l256_287(x),
    ]