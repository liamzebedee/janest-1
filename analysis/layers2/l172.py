import numpy as np




# Generated from reverse engineering
def l172_g(x: np.ndarray) -> np.ndarray:
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




def l172_0(x):
    # x is a list (or vector) of length 304
    return max(0, x[0])
def l172_1(x):
    # x is a list (or vector) of length 304
    return max(0, x[1])
def l172_2(x):
    # x is a list (or vector) of length 304
    return max(0, x[2])
def l172_3(x):
    # x is a list (or vector) of length 304
    return max(0, x[3])
def l172_4(x):
    # x is a list (or vector) of length 304
    return max(0, x[4])
def l172_5(x):
    # x is a list (or vector) of length 304
    return max(0, x[5])
def l172_6(x):
    # x is a list (or vector) of length 304
    return max(0, x[6])
def l172_7(x):
    # x is a list (or vector) of length 304
    return max(0, x[7])
def l172_8(x):
    # x is a list (or vector) of length 304
    return max(0, x[8])
def l172_9(x):
    # x is a list (or vector) of length 304
    return max(0, x[9])
def l172_10(x):
    # x is a list (or vector) of length 304
    return max(0, x[10])
def l172_11(x):
    # x is a list (or vector) of length 304
    return max(0, x[11])
def l172_12(x):
    # x is a list (or vector) of length 304
    return max(0, x[12])
def l172_13(x):
    # x is a list (or vector) of length 304
    return max(0, x[13])
def l172_14(x):
    # x is a list (or vector) of length 304
    return max(0, x[14])
def l172_15(x):
    # x is a list (or vector) of length 304
    return max(0, x[15])
def l172_16(x):
    # x is a list (or vector) of length 304
    return max(0, x[16])
def l172_17(x):
    # x is a list (or vector) of length 304
    return max(0, x[17])
def l172_18(x):
    # x is a list (or vector) of length 304
    return max(0, x[18])
def l172_19(x):
    # x is a list (or vector) of length 304
    return max(0, x[19])
def l172_20(x):
    # x is a list (or vector) of length 304
    return max(0, x[20])
def l172_21(x):
    # x is a list (or vector) of length 304
    return max(0, x[21])
def l172_22(x):
    # x is a list (or vector) of length 304
    return max(0, x[22])
def l172_23(x):
    # x is a list (or vector) of length 304
    return max(0, x[23])
def l172_24(x):
    # x is a list (or vector) of length 304
    return max(0, x[24])
def l172_25(x):
    # x is a list (or vector) of length 304
    return max(0, x[25])
def l172_26(x):
    # x is a list (or vector) of length 304
    return max(0, x[26])
def l172_27(x):
    # x is a list (or vector) of length 304
    return max(0, x[27])
def l172_28(x):
    # x is a list (or vector) of length 304
    return max(0, x[28])
def l172_29(x):
    # x is a list (or vector) of length 304
    return max(0, x[29])
def l172_30(x):
    # x is a list (or vector) of length 304
    return max(0, x[30])
def l172_31(x):
    # x is a list (or vector) of length 304
    return max(0, x[31])
def l172_32(x):
    # x is a list (or vector) of length 304
    return max(0, x[32])
def l172_33(x):
    # x is a list (or vector) of length 304
    return max(0, x[33])
def l172_34(x):
    # x is a list (or vector) of length 304
    return max(0, x[34])
def l172_35(x):
    # x is a list (or vector) of length 304
    return max(0, x[35])
def l172_36(x):
    # x is a list (or vector) of length 304
    return max(0, x[36])
def l172_37(x):
    # x is a list (or vector) of length 304
    return max(0, x[37])
def l172_38(x):
    # x is a list (or vector) of length 304
    return max(0, x[38])
def l172_39(x):
    # x is a list (or vector) of length 304
    return max(0, x[39])
def l172_40(x):
    # x is a list (or vector) of length 304
    return max(0, x[40])
def l172_41(x):
    # x is a list (or vector) of length 304
    return max(0, x[41])
def l172_42(x):
    # x is a list (or vector) of length 304
    return max(0, x[42])
def l172_43(x):
    # x is a list (or vector) of length 304
    return max(0, x[43])
def l172_44(x):
    # x is a list (or vector) of length 304
    return max(0, x[44])
def l172_45(x):
    # x is a list (or vector) of length 304
    return max(0, x[45])
def l172_46(x):
    # x is a list (or vector) of length 304
    return max(0, x[46])
def l172_47(x):
    # x is a list (or vector) of length 304
    return max(0, x[47])
def l172_48(x):
    # x is a list (or vector) of length 304
    return max(0, x[48])
def l172_49(x):
    # x is a list (or vector) of length 304
    return max(0, x[49])
def l172_50(x):
    # x is a list (or vector) of length 304
    return max(0, x[50])
def l172_51(x):
    # x is a list (or vector) of length 304
    return max(0, x[51])
def l172_52(x):
    # x is a list (or vector) of length 304
    return max(0, x[52])
def l172_53(x):
    # x is a list (or vector) of length 304
    return max(0, x[53])
def l172_54(x):
    # x is a list (or vector) of length 304
    return max(0, x[54])
def l172_55(x):
    # x is a list (or vector) of length 304
    return max(0, x[55])
def l172_56(x):
    # x is a list (or vector) of length 304
    return max(0, x[56])
def l172_57(x):
    # x is a list (or vector) of length 304
    return max(0, x[57])
def l172_58(x):
    # x is a list (or vector) of length 304
    return max(0, x[58])
def l172_59(x):
    # x is a list (or vector) of length 304
    return max(0, x[59])
def l172_60(x):
    # x is a list (or vector) of length 304
    return max(0, x[60])
def l172_61(x):
    # x is a list (or vector) of length 304
    return max(0, x[61])
def l172_62(x):
    # x is a list (or vector) of length 304
    return max(0, x[62])
def l172_63(x):
    # x is a list (or vector) of length 304
    return max(0, x[63])
def l172_64(x):
    # x is a list (or vector) of length 304
    return max(0, x[64])
def l172_65(x):
    # x is a list (or vector) of length 304
    return max(0, x[65])
def l172_66(x):
    # x is a list (or vector) of length 304
    return max(0, x[66])
def l172_67(x):
    # x is a list (or vector) of length 304
    return max(0, x[67])
def l172_68(x):
    # x is a list (or vector) of length 304
    return max(0, x[68])
def l172_69(x):
    # x is a list (or vector) of length 304
    return max(0, x[69])
def l172_70(x):
    # x is a list (or vector) of length 304
    return max(0, x[70])
def l172_71(x):
    # x is a list (or vector) of length 304
    return max(0, x[71])
def l172_72(x):
    # x is a list (or vector) of length 304
    return max(0, x[72])
def l172_73(x):
    # x is a list (or vector) of length 304
    return max(0, x[73])
def l172_74(x):
    # x is a list (or vector) of length 304
    return max(0, x[74])
def l172_75(x):
    # x is a list (or vector) of length 304
    return max(0, x[75])
def l172_76(x):
    # x is a list (or vector) of length 304
    return max(0, x[76])
def l172_77(x):
    # x is a list (or vector) of length 304
    return max(0, x[77])
def l172_78(x):
    # x is a list (or vector) of length 304
    return max(0, x[78])
def l172_79(x):
    # x is a list (or vector) of length 304
    return max(0, x[79])
def l172_80(x):
    # x is a list (or vector) of length 304
    return max(0, x[80])
def l172_81(x):
    # x is a list (or vector) of length 304
    return max(0, x[81])
def l172_82(x):
    # x is a list (or vector) of length 304
    return max(0, x[82])
def l172_83(x):
    # x is a list (or vector) of length 304
    return max(0, x[83])
def l172_84(x):
    # x is a list (or vector) of length 304
    return max(0, x[84])
def l172_85(x):
    # x is a list (or vector) of length 304
    return max(0, x[85])
def l172_86(x):
    # x is a list (or vector) of length 304
    return max(0, x[86])
def l172_87(x):
    # x is a list (or vector) of length 304
    return max(0, x[87])
def l172_88(x):
    # x is a list (or vector) of length 304
    return max(0, x[88])
def l172_89(x):
    # x is a list (or vector) of length 304
    return max(0, x[89])
def l172_90(x):
    # x is a list (or vector) of length 304
    return max(0, x[90])
def l172_91(x):
    # x is a list (or vector) of length 304
    return max(0, x[91])
def l172_92(x):
    # x is a list (or vector) of length 304
    return max(0, x[92])
def l172_93(x):
    # x is a list (or vector) of length 304
    return max(0, x[93])
def l172_94(x):
    # x is a list (or vector) of length 304
    return max(0, x[94])
def l172_95(x):
    # x is a list (or vector) of length 304
    return max(0, x[95])
def l172_96(x):
    # x is a list (or vector) of length 304
    return max(0, x[96])
def l172_97(x):
    # x is a list (or vector) of length 304
    return max(0, x[97])
def l172_98(x):
    # x is a list (or vector) of length 304
    return max(0, x[98])
def l172_99(x):
    # x is a list (or vector) of length 304
    return max(0, x[99])
def l172_100(x):
    # x is a list (or vector) of length 304
    return max(0, x[100])
def l172_101(x):
    # x is a list (or vector) of length 304
    return max(0, x[101])
def l172_102(x):
    # x is a list (or vector) of length 304
    return max(0, x[102])
def l172_103(x):
    # x is a list (or vector) of length 304
    return max(0, x[103])
def l172_104(x):
    # x is a list (or vector) of length 304
    return max(0, x[104])
def l172_105(x):
    # x is a list (or vector) of length 304
    return max(0, x[105])
def l172_106(x):
    # x is a list (or vector) of length 304
    return max(0, x[106])
def l172_107(x):
    # x is a list (or vector) of length 304
    return max(0, x[107])
def l172_108(x):
    # x is a list (or vector) of length 304
    return max(0, x[108])
def l172_109(x):
    # x is a list (or vector) of length 304
    return max(0, x[109])
def l172_110(x):
    # x is a list (or vector) of length 304
    return max(0, x[110])
def l172_111(x):
    # x is a list (or vector) of length 304
    return max(0, x[111])
def l172_112(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[112] + -1.0*x[128] + 1.0)
def l172_113(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[113] + -1.0*x[129] + 1.0)
def l172_114(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[114] + -1.0*x[130] + 1.0)
def l172_115(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[115] + -1.0*x[131] + 1.0)
def l172_116(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[116] + -1.0*x[132] + 1.0)
def l172_117(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[117] + -1.0*x[133] + 1.0)
def l172_118(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[118] + -1.0*x[134] + 1.0)
def l172_119(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[119] + -1.0*x[135] + 1.0)
def l172_120(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[120] + -1.0*x[136] + 1.0)
def l172_121(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[121] + -1.0*x[137] + 1.0)
def l172_122(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[122] + -1.0*x[138] + 1.0)
def l172_123(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[123] + -1.0*x[139] + 1.0)
def l172_124(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[124] + -1.0*x[140] + 1.0)
def l172_125(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[125] + -1.0*x[141] + 1.0)
def l172_126(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[126] + -1.0*x[142] + 1.0)
def l172_127(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[127] + -1.0*x[143] + 1.0)
def l172_128(x):
    # x is a list (or vector) of length 304
    return max(0, x[160])
def l172_129(x):
    # x is a list (or vector) of length 304
    return max(0, x[161])
def l172_130(x):
    # x is a list (or vector) of length 304
    return max(0, x[162])
def l172_131(x):
    # x is a list (or vector) of length 304
    return max(0, x[163])
def l172_132(x):
    # x is a list (or vector) of length 304
    return max(0, x[164])
def l172_133(x):
    # x is a list (or vector) of length 304
    return max(0, x[165])
def l172_134(x):
    # x is a list (or vector) of length 304
    return max(0, x[166])
def l172_135(x):
    # x is a list (or vector) of length 304
    return max(0, x[167])
def l172_136(x):
    # x is a list (or vector) of length 304
    return max(0, x[168])
def l172_137(x):
    # x is a list (or vector) of length 304
    return max(0, x[169])
def l172_138(x):
    # x is a list (or vector) of length 304
    return max(0, x[170])
def l172_139(x):
    # x is a list (or vector) of length 304
    return max(0, x[171])
def l172_140(x):
    # x is a list (or vector) of length 304
    return max(0, x[172])
def l172_141(x):
    # x is a list (or vector) of length 304
    return max(0, x[173])
def l172_142(x):
    # x is a list (or vector) of length 304
    return max(0, x[174])
def l172_143(x):
    # x is a list (or vector) of length 304
    return max(0, x[175])
def l172_144(x):
    # x is a list (or vector) of length 304
    return max(0, x[144])
def l172_145(x):
    # x is a list (or vector) of length 304
    return max(0, x[145])
def l172_146(x):
    # x is a list (or vector) of length 304
    return max(0, x[146])
def l172_147(x):
    # x is a list (or vector) of length 304
    return max(0, x[147])
def l172_148(x):
    # x is a list (or vector) of length 304
    return max(0, x[148])
def l172_149(x):
    # x is a list (or vector) of length 304
    return max(0, x[149])
def l172_150(x):
    # x is a list (or vector) of length 304
    return max(0, x[150])
def l172_151(x):
    # x is a list (or vector) of length 304
    return max(0, x[151])
def l172_152(x):
    # x is a list (or vector) of length 304
    return max(0, x[152])
def l172_153(x):
    # x is a list (or vector) of length 304
    return max(0, x[153])
def l172_154(x):
    # x is a list (or vector) of length 304
    return max(0, x[154])
def l172_155(x):
    # x is a list (or vector) of length 304
    return max(0, x[155])
def l172_156(x):
    # x is a list (or vector) of length 304
    return max(0, x[156])
def l172_157(x):
    # x is a list (or vector) of length 304
    return max(0, x[157])
def l172_158(x):
    # x is a list (or vector) of length 304
    return max(0, x[158])
def l172_159(x):
    # x is a list (or vector) of length 304
    return max(0, x[159])
def l172_160(x):
    # x is a list (or vector) of length 304
    return max(0, x[176])
def l172_161(x):
    # x is a list (or vector) of length 304
    return max(0, x[177])
def l172_162(x):
    # x is a list (or vector) of length 304
    return max(0, x[178])
def l172_163(x):
    # x is a list (or vector) of length 304
    return max(0, x[179])
def l172_164(x):
    # x is a list (or vector) of length 304
    return max(0, x[180])
def l172_165(x):
    # x is a list (or vector) of length 304
    return max(0, x[181])
def l172_166(x):
    # x is a list (or vector) of length 304
    return max(0, x[182])
def l172_167(x):
    # x is a list (or vector) of length 304
    return max(0, x[183])
def l172_168(x):
    # x is a list (or vector) of length 304
    return max(0, x[184])
def l172_169(x):
    # x is a list (or vector) of length 304
    return max(0, x[185])
def l172_170(x):
    # x is a list (or vector) of length 304
    return max(0, x[186])
def l172_171(x):
    # x is a list (or vector) of length 304
    return max(0, x[187])
def l172_172(x):
    # x is a list (or vector) of length 304
    return max(0, x[188])
def l172_173(x):
    # x is a list (or vector) of length 304
    return max(0, x[189])
def l172_174(x):
    # x is a list (or vector) of length 304
    return max(0, x[190])
def l172_175(x):
    # x is a list (or vector) of length 304
    return max(0, x[191])
def l172_176(x):
    # x is a list (or vector) of length 304
    return max(0, x[192])
def l172_177(x):
    # x is a list (or vector) of length 304
    return max(0, x[193])
def l172_178(x):
    # x is a list (or vector) of length 304
    return max(0, x[194])
def l172_179(x):
    # x is a list (or vector) of length 304
    return max(0, x[195])
def l172_180(x):
    # x is a list (or vector) of length 304
    return max(0, x[196])
def l172_181(x):
    # x is a list (or vector) of length 304
    return max(0, x[197])
def l172_182(x):
    # x is a list (or vector) of length 304
    return max(0, x[198])
def l172_183(x):
    # x is a list (or vector) of length 304
    return max(0, x[199])
def l172_184(x):
    # x is a list (or vector) of length 304
    return max(0, x[200])
def l172_185(x):
    # x is a list (or vector) of length 304
    return max(0, x[201])
def l172_186(x):
    # x is a list (or vector) of length 304
    return max(0, x[202])
def l172_187(x):
    # x is a list (or vector) of length 304
    return max(0, x[203])
def l172_188(x):
    # x is a list (or vector) of length 304
    return max(0, x[204])
def l172_189(x):
    # x is a list (or vector) of length 304
    return max(0, x[205])
def l172_190(x):
    # x is a list (or vector) of length 304
    return max(0, x[206])
def l172_191(x):
    # x is a list (or vector) of length 304
    return max(0, x[207])
def l172_192(x):
    # x is a list (or vector) of length 304
    return max(0, x[208])
def l172_193(x):
    # x is a list (or vector) of length 304
    return max(0, x[209])
def l172_194(x):
    # x is a list (or vector) of length 304
    return max(0, x[210])
def l172_195(x):
    # x is a list (or vector) of length 304
    return max(0, x[211])
def l172_196(x):
    # x is a list (or vector) of length 304
    return max(0, x[212])
def l172_197(x):
    # x is a list (or vector) of length 304
    return max(0, x[213])
def l172_198(x):
    # x is a list (or vector) of length 304
    return max(0, x[214])
def l172_199(x):
    # x is a list (or vector) of length 304
    return max(0, x[215])
def l172_200(x):
    # x is a list (or vector) of length 304
    return max(0, x[216])
def l172_201(x):
    # x is a list (or vector) of length 304
    return max(0, x[217])
def l172_202(x):
    # x is a list (or vector) of length 304
    return max(0, x[218])
def l172_203(x):
    # x is a list (or vector) of length 304
    return max(0, x[219])
def l172_204(x):
    # x is a list (or vector) of length 304
    return max(0, x[220])
def l172_205(x):
    # x is a list (or vector) of length 304
    return max(0, x[221])
def l172_206(x):
    # x is a list (or vector) of length 304
    return max(0, x[222])
def l172_207(x):
    # x is a list (or vector) of length 304
    return max(0, x[223])
def l172_208(x):
    # x is a list (or vector) of length 304
    return max(0, x[224])
def l172_209(x):
    # x is a list (or vector) of length 304
    return max(0, x[225])
def l172_210(x):
    # x is a list (or vector) of length 304
    return max(0, x[226])
def l172_211(x):
    # x is a list (or vector) of length 304
    return max(0, x[227])
def l172_212(x):
    # x is a list (or vector) of length 304
    return max(0, x[228])
def l172_213(x):
    # x is a list (or vector) of length 304
    return max(0, x[229])
def l172_214(x):
    # x is a list (or vector) of length 304
    return max(0, x[230])
def l172_215(x):
    # x is a list (or vector) of length 304
    return max(0, x[231])
def l172_216(x):
    # x is a list (or vector) of length 304
    return max(0, x[232])
def l172_217(x):
    # x is a list (or vector) of length 304
    return max(0, x[233])
def l172_218(x):
    # x is a list (or vector) of length 304
    return max(0, x[234])
def l172_219(x):
    # x is a list (or vector) of length 304
    return max(0, x[235])
def l172_220(x):
    # x is a list (or vector) of length 304
    return max(0, x[236])
def l172_221(x):
    # x is a list (or vector) of length 304
    return max(0, x[237])
def l172_222(x):
    # x is a list (or vector) of length 304
    return max(0, x[238])
def l172_223(x):
    # x is a list (or vector) of length 304
    return max(0, x[239])
def l172_224(x):
    # x is a list (or vector) of length 304
    return max(0, x[240])
def l172_225(x):
    # x is a list (or vector) of length 304
    return max(0, x[241])
def l172_226(x):
    # x is a list (or vector) of length 304
    return max(0, x[242])
def l172_227(x):
    # x is a list (or vector) of length 304
    return max(0, x[243])
def l172_228(x):
    # x is a list (or vector) of length 304
    return max(0, x[244])
def l172_229(x):
    # x is a list (or vector) of length 304
    return max(0, x[245])
def l172_230(x):
    # x is a list (or vector) of length 304
    return max(0, x[246])
def l172_231(x):
    # x is a list (or vector) of length 304
    return max(0, x[247])
def l172_232(x):
    # x is a list (or vector) of length 304
    return max(0, x[248])
def l172_233(x):
    # x is a list (or vector) of length 304
    return max(0, x[249])
def l172_234(x):
    # x is a list (or vector) of length 304
    return max(0, x[250])
def l172_235(x):
    # x is a list (or vector) of length 304
    return max(0, x[251])
def l172_236(x):
    # x is a list (or vector) of length 304
    return max(0, x[252])
def l172_237(x):
    # x is a list (or vector) of length 304
    return max(0, x[253])
def l172_238(x):
    # x is a list (or vector) of length 304
    return max(0, x[254])
def l172_239(x):
    # x is a list (or vector) of length 304
    return max(0, x[255])
def l172_240(x):
    # x is a list (or vector) of length 304
    return max(0, x[256])
def l172_241(x):
    # x is a list (or vector) of length 304
    return max(0, x[257])
def l172_242(x):
    # x is a list (or vector) of length 304
    return max(0, x[258])
def l172_243(x):
    # x is a list (or vector) of length 304
    return max(0, x[259])
def l172_244(x):
    # x is a list (or vector) of length 304
    return max(0, x[260])
def l172_245(x):
    # x is a list (or vector) of length 304
    return max(0, x[261])
def l172_246(x):
    # x is a list (or vector) of length 304
    return max(0, x[262])
def l172_247(x):
    # x is a list (or vector) of length 304
    return max(0, x[263])
def l172_248(x):
    # x is a list (or vector) of length 304
    return max(0, x[264])
def l172_249(x):
    # x is a list (or vector) of length 304
    return max(0, x[265])
def l172_250(x):
    # x is a list (or vector) of length 304
    return max(0, x[266])
def l172_251(x):
    # x is a list (or vector) of length 304
    return max(0, x[267])
def l172_252(x):
    # x is a list (or vector) of length 304
    return max(0, x[268])
def l172_253(x):
    # x is a list (or vector) of length 304
    return max(0, x[269])
def l172_254(x):
    # x is a list (or vector) of length 304
    return max(0, x[270])
def l172_255(x):
    # x is a list (or vector) of length 304
    return max(0, x[271])
def l172_256(x):
    # x is a list (or vector) of length 304
    return max(0, x[272])
def l172_257(x):
    # x is a list (or vector) of length 304
    return max(0, x[273])
def l172_258(x):
    # x is a list (or vector) of length 304
    return max(0, x[274])
def l172_259(x):
    # x is a list (or vector) of length 304
    return max(0, x[275])
def l172_260(x):
    # x is a list (or vector) of length 304
    return max(0, x[276])
def l172_261(x):
    # x is a list (or vector) of length 304
    return max(0, x[277])
def l172_262(x):
    # x is a list (or vector) of length 304
    return max(0, x[278])
def l172_263(x):
    # x is a list (or vector) of length 304
    return max(0, x[279])
def l172_264(x):
    # x is a list (or vector) of length 304
    return max(0, x[280])
def l172_265(x):
    # x is a list (or vector) of length 304
    return max(0, x[281])
def l172_266(x):
    # x is a list (or vector) of length 304
    return max(0, x[282])
def l172_267(x):
    # x is a list (or vector) of length 304
    return max(0, x[283])
def l172_268(x):
    # x is a list (or vector) of length 304
    return max(0, x[284])
def l172_269(x):
    # x is a list (or vector) of length 304
    return max(0, x[285])
def l172_270(x):
    # x is a list (or vector) of length 304
    return max(0, x[286])
def l172_271(x):
    # x is a list (or vector) of length 304
    return max(0, x[287])
def l172_272(x):
    # x is a list (or vector) of length 304
    return max(0, x[288])
def l172_273(x):
    # x is a list (or vector) of length 304
    return max(0, x[289])
def l172_274(x):
    # x is a list (or vector) of length 304
    return max(0, x[290])
def l172_275(x):
    # x is a list (or vector) of length 304
    return max(0, x[291])
def l172_276(x):
    # x is a list (or vector) of length 304
    return max(0, x[292])
def l172_277(x):
    # x is a list (or vector) of length 304
    return max(0, x[293])
def l172_278(x):
    # x is a list (or vector) of length 304
    return max(0, x[294])
def l172_279(x):
    # x is a list (or vector) of length 304
    return max(0, x[295])
def l172_280(x):
    # x is a list (or vector) of length 304
    return max(0, x[296])
def l172_281(x):
    # x is a list (or vector) of length 304
    return max(0, x[297])
def l172_282(x):
    # x is a list (or vector) of length 304
    return max(0, x[298])
def l172_283(x):
    # x is a list (or vector) of length 304
    return max(0, x[299])
def l172_284(x):
    # x is a list (or vector) of length 304
    return max(0, x[300])
def l172_285(x):
    # x is a list (or vector) of length 304
    return max(0, x[301])
def l172_286(x):
    # x is a list (or vector) of length 304
    return max(0, x[302])
def l172_287(x):
    # x is a list (or vector) of length 304
    return max(0, x[303])
def l172_(x):
    # x is a list (or vector) of length 304
    return [
        l172_0(x),
        l172_1(x),
        l172_2(x),
        l172_3(x),
        l172_4(x),
        l172_5(x),
        l172_6(x),
        l172_7(x),
        l172_8(x),
        l172_9(x),
        l172_10(x),
        l172_11(x),
        l172_12(x),
        l172_13(x),
        l172_14(x),
        l172_15(x),
        l172_16(x),
        l172_17(x),
        l172_18(x),
        l172_19(x),
        l172_20(x),
        l172_21(x),
        l172_22(x),
        l172_23(x),
        l172_24(x),
        l172_25(x),
        l172_26(x),
        l172_27(x),
        l172_28(x),
        l172_29(x),
        l172_30(x),
        l172_31(x),
        l172_32(x),
        l172_33(x),
        l172_34(x),
        l172_35(x),
        l172_36(x),
        l172_37(x),
        l172_38(x),
        l172_39(x),
        l172_40(x),
        l172_41(x),
        l172_42(x),
        l172_43(x),
        l172_44(x),
        l172_45(x),
        l172_46(x),
        l172_47(x),
        l172_48(x),
        l172_49(x),
        l172_50(x),
        l172_51(x),
        l172_52(x),
        l172_53(x),
        l172_54(x),
        l172_55(x),
        l172_56(x),
        l172_57(x),
        l172_58(x),
        l172_59(x),
        l172_60(x),
        l172_61(x),
        l172_62(x),
        l172_63(x),
        l172_64(x),
        l172_65(x),
        l172_66(x),
        l172_67(x),
        l172_68(x),
        l172_69(x),
        l172_70(x),
        l172_71(x),
        l172_72(x),
        l172_73(x),
        l172_74(x),
        l172_75(x),
        l172_76(x),
        l172_77(x),
        l172_78(x),
        l172_79(x),
        l172_80(x),
        l172_81(x),
        l172_82(x),
        l172_83(x),
        l172_84(x),
        l172_85(x),
        l172_86(x),
        l172_87(x),
        l172_88(x),
        l172_89(x),
        l172_90(x),
        l172_91(x),
        l172_92(x),
        l172_93(x),
        l172_94(x),
        l172_95(x),
        l172_96(x),
        l172_97(x),
        l172_98(x),
        l172_99(x),
        l172_100(x),
        l172_101(x),
        l172_102(x),
        l172_103(x),
        l172_104(x),
        l172_105(x),
        l172_106(x),
        l172_107(x),
        l172_108(x),
        l172_109(x),
        l172_110(x),
        l172_111(x),
        l172_112(x),
        l172_113(x),
        l172_114(x),
        l172_115(x),
        l172_116(x),
        l172_117(x),
        l172_118(x),
        l172_119(x),
        l172_120(x),
        l172_121(x),
        l172_122(x),
        l172_123(x),
        l172_124(x),
        l172_125(x),
        l172_126(x),
        l172_127(x),
        l172_128(x),
        l172_129(x),
        l172_130(x),
        l172_131(x),
        l172_132(x),
        l172_133(x),
        l172_134(x),
        l172_135(x),
        l172_136(x),
        l172_137(x),
        l172_138(x),
        l172_139(x),
        l172_140(x),
        l172_141(x),
        l172_142(x),
        l172_143(x),
        l172_144(x),
        l172_145(x),
        l172_146(x),
        l172_147(x),
        l172_148(x),
        l172_149(x),
        l172_150(x),
        l172_151(x),
        l172_152(x),
        l172_153(x),
        l172_154(x),
        l172_155(x),
        l172_156(x),
        l172_157(x),
        l172_158(x),
        l172_159(x),
        l172_160(x),
        l172_161(x),
        l172_162(x),
        l172_163(x),
        l172_164(x),
        l172_165(x),
        l172_166(x),
        l172_167(x),
        l172_168(x),
        l172_169(x),
        l172_170(x),
        l172_171(x),
        l172_172(x),
        l172_173(x),
        l172_174(x),
        l172_175(x),
        l172_176(x),
        l172_177(x),
        l172_178(x),
        l172_179(x),
        l172_180(x),
        l172_181(x),
        l172_182(x),
        l172_183(x),
        l172_184(x),
        l172_185(x),
        l172_186(x),
        l172_187(x),
        l172_188(x),
        l172_189(x),
        l172_190(x),
        l172_191(x),
        l172_192(x),
        l172_193(x),
        l172_194(x),
        l172_195(x),
        l172_196(x),
        l172_197(x),
        l172_198(x),
        l172_199(x),
        l172_200(x),
        l172_201(x),
        l172_202(x),
        l172_203(x),
        l172_204(x),
        l172_205(x),
        l172_206(x),
        l172_207(x),
        l172_208(x),
        l172_209(x),
        l172_210(x),
        l172_211(x),
        l172_212(x),
        l172_213(x),
        l172_214(x),
        l172_215(x),
        l172_216(x),
        l172_217(x),
        l172_218(x),
        l172_219(x),
        l172_220(x),
        l172_221(x),
        l172_222(x),
        l172_223(x),
        l172_224(x),
        l172_225(x),
        l172_226(x),
        l172_227(x),
        l172_228(x),
        l172_229(x),
        l172_230(x),
        l172_231(x),
        l172_232(x),
        l172_233(x),
        l172_234(x),
        l172_235(x),
        l172_236(x),
        l172_237(x),
        l172_238(x),
        l172_239(x),
        l172_240(x),
        l172_241(x),
        l172_242(x),
        l172_243(x),
        l172_244(x),
        l172_245(x),
        l172_246(x),
        l172_247(x),
        l172_248(x),
        l172_249(x),
        l172_250(x),
        l172_251(x),
        l172_252(x),
        l172_253(x),
        l172_254(x),
        l172_255(x),
        l172_256(x),
        l172_257(x),
        l172_258(x),
        l172_259(x),
        l172_260(x),
        l172_261(x),
        l172_262(x),
        l172_263(x),
        l172_264(x),
        l172_265(x),
        l172_266(x),
        l172_267(x),
        l172_268(x),
        l172_269(x),
        l172_270(x),
        l172_271(x),
        l172_272(x),
        l172_273(x),
        l172_274(x),
        l172_275(x),
        l172_276(x),
        l172_277(x),
        l172_278(x),
        l172_279(x),
        l172_280(x),
        l172_281(x),
        l172_282(x),
        l172_283(x),
        l172_284(x),
        l172_285(x),
        l172_286(x),
        l172_287(x),
    ]