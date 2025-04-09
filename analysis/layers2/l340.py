import numpy as np




# Generated from reverse engineering
def l340_g(x: np.ndarray) -> np.ndarray:
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




def l340_0(x):
    # x is a list (or vector) of length 304
    return max(0, x[0])
def l340_1(x):
    # x is a list (or vector) of length 304
    return max(0, x[1])
def l340_2(x):
    # x is a list (or vector) of length 304
    return max(0, x[2])
def l340_3(x):
    # x is a list (or vector) of length 304
    return max(0, x[3])
def l340_4(x):
    # x is a list (or vector) of length 304
    return max(0, x[4])
def l340_5(x):
    # x is a list (or vector) of length 304
    return max(0, x[5])
def l340_6(x):
    # x is a list (or vector) of length 304
    return max(0, x[6])
def l340_7(x):
    # x is a list (or vector) of length 304
    return max(0, x[7])
def l340_8(x):
    # x is a list (or vector) of length 304
    return max(0, x[8])
def l340_9(x):
    # x is a list (or vector) of length 304
    return max(0, x[9])
def l340_10(x):
    # x is a list (or vector) of length 304
    return max(0, x[10])
def l340_11(x):
    # x is a list (or vector) of length 304
    return max(0, x[11])
def l340_12(x):
    # x is a list (or vector) of length 304
    return max(0, x[12])
def l340_13(x):
    # x is a list (or vector) of length 304
    return max(0, x[13])
def l340_14(x):
    # x is a list (or vector) of length 304
    return max(0, x[14])
def l340_15(x):
    # x is a list (or vector) of length 304
    return max(0, x[15])
def l340_16(x):
    # x is a list (or vector) of length 304
    return max(0, x[16])
def l340_17(x):
    # x is a list (or vector) of length 304
    return max(0, x[17])
def l340_18(x):
    # x is a list (or vector) of length 304
    return max(0, x[18])
def l340_19(x):
    # x is a list (or vector) of length 304
    return max(0, x[19])
def l340_20(x):
    # x is a list (or vector) of length 304
    return max(0, x[20])
def l340_21(x):
    # x is a list (or vector) of length 304
    return max(0, x[21])
def l340_22(x):
    # x is a list (or vector) of length 304
    return max(0, x[22])
def l340_23(x):
    # x is a list (or vector) of length 304
    return max(0, x[23])
def l340_24(x):
    # x is a list (or vector) of length 304
    return max(0, x[24])
def l340_25(x):
    # x is a list (or vector) of length 304
    return max(0, x[25])
def l340_26(x):
    # x is a list (or vector) of length 304
    return max(0, x[26])
def l340_27(x):
    # x is a list (or vector) of length 304
    return max(0, x[27])
def l340_28(x):
    # x is a list (or vector) of length 304
    return max(0, x[28])
def l340_29(x):
    # x is a list (or vector) of length 304
    return max(0, x[29])
def l340_30(x):
    # x is a list (or vector) of length 304
    return max(0, x[30])
def l340_31(x):
    # x is a list (or vector) of length 304
    return max(0, x[31])
def l340_32(x):
    # x is a list (or vector) of length 304
    return max(0, x[32])
def l340_33(x):
    # x is a list (or vector) of length 304
    return max(0, x[33])
def l340_34(x):
    # x is a list (or vector) of length 304
    return max(0, x[34])
def l340_35(x):
    # x is a list (or vector) of length 304
    return max(0, x[35])
def l340_36(x):
    # x is a list (or vector) of length 304
    return max(0, x[36])
def l340_37(x):
    # x is a list (or vector) of length 304
    return max(0, x[37])
def l340_38(x):
    # x is a list (or vector) of length 304
    return max(0, x[38])
def l340_39(x):
    # x is a list (or vector) of length 304
    return max(0, x[39])
def l340_40(x):
    # x is a list (or vector) of length 304
    return max(0, x[40])
def l340_41(x):
    # x is a list (or vector) of length 304
    return max(0, x[41])
def l340_42(x):
    # x is a list (or vector) of length 304
    return max(0, x[42])
def l340_43(x):
    # x is a list (or vector) of length 304
    return max(0, x[43])
def l340_44(x):
    # x is a list (or vector) of length 304
    return max(0, x[44])
def l340_45(x):
    # x is a list (or vector) of length 304
    return max(0, x[45])
def l340_46(x):
    # x is a list (or vector) of length 304
    return max(0, x[46])
def l340_47(x):
    # x is a list (or vector) of length 304
    return max(0, x[47])
def l340_48(x):
    # x is a list (or vector) of length 304
    return max(0, x[48])
def l340_49(x):
    # x is a list (or vector) of length 304
    return max(0, x[49])
def l340_50(x):
    # x is a list (or vector) of length 304
    return max(0, x[50])
def l340_51(x):
    # x is a list (or vector) of length 304
    return max(0, x[51])
def l340_52(x):
    # x is a list (or vector) of length 304
    return max(0, x[52])
def l340_53(x):
    # x is a list (or vector) of length 304
    return max(0, x[53])
def l340_54(x):
    # x is a list (or vector) of length 304
    return max(0, x[54])
def l340_55(x):
    # x is a list (or vector) of length 304
    return max(0, x[55])
def l340_56(x):
    # x is a list (or vector) of length 304
    return max(0, x[56])
def l340_57(x):
    # x is a list (or vector) of length 304
    return max(0, x[57])
def l340_58(x):
    # x is a list (or vector) of length 304
    return max(0, x[58])
def l340_59(x):
    # x is a list (or vector) of length 304
    return max(0, x[59])
def l340_60(x):
    # x is a list (or vector) of length 304
    return max(0, x[60])
def l340_61(x):
    # x is a list (or vector) of length 304
    return max(0, x[61])
def l340_62(x):
    # x is a list (or vector) of length 304
    return max(0, x[62])
def l340_63(x):
    # x is a list (or vector) of length 304
    return max(0, x[63])
def l340_64(x):
    # x is a list (or vector) of length 304
    return max(0, x[64])
def l340_65(x):
    # x is a list (or vector) of length 304
    return max(0, x[65])
def l340_66(x):
    # x is a list (or vector) of length 304
    return max(0, x[66])
def l340_67(x):
    # x is a list (or vector) of length 304
    return max(0, x[67])
def l340_68(x):
    # x is a list (or vector) of length 304
    return max(0, x[68])
def l340_69(x):
    # x is a list (or vector) of length 304
    return max(0, x[69])
def l340_70(x):
    # x is a list (or vector) of length 304
    return max(0, x[70])
def l340_71(x):
    # x is a list (or vector) of length 304
    return max(0, x[71])
def l340_72(x):
    # x is a list (or vector) of length 304
    return max(0, x[72])
def l340_73(x):
    # x is a list (or vector) of length 304
    return max(0, x[73])
def l340_74(x):
    # x is a list (or vector) of length 304
    return max(0, x[74])
def l340_75(x):
    # x is a list (or vector) of length 304
    return max(0, x[75])
def l340_76(x):
    # x is a list (or vector) of length 304
    return max(0, x[76])
def l340_77(x):
    # x is a list (or vector) of length 304
    return max(0, x[77])
def l340_78(x):
    # x is a list (or vector) of length 304
    return max(0, x[78])
def l340_79(x):
    # x is a list (or vector) of length 304
    return max(0, x[79])
def l340_80(x):
    # x is a list (or vector) of length 304
    return max(0, x[80])
def l340_81(x):
    # x is a list (or vector) of length 304
    return max(0, x[81])
def l340_82(x):
    # x is a list (or vector) of length 304
    return max(0, x[82])
def l340_83(x):
    # x is a list (or vector) of length 304
    return max(0, x[83])
def l340_84(x):
    # x is a list (or vector) of length 304
    return max(0, x[84])
def l340_85(x):
    # x is a list (or vector) of length 304
    return max(0, x[85])
def l340_86(x):
    # x is a list (or vector) of length 304
    return max(0, x[86])
def l340_87(x):
    # x is a list (or vector) of length 304
    return max(0, x[87])
def l340_88(x):
    # x is a list (or vector) of length 304
    return max(0, x[88])
def l340_89(x):
    # x is a list (or vector) of length 304
    return max(0, x[89])
def l340_90(x):
    # x is a list (or vector) of length 304
    return max(0, x[90])
def l340_91(x):
    # x is a list (or vector) of length 304
    return max(0, x[91])
def l340_92(x):
    # x is a list (or vector) of length 304
    return max(0, x[92])
def l340_93(x):
    # x is a list (or vector) of length 304
    return max(0, x[93])
def l340_94(x):
    # x is a list (or vector) of length 304
    return max(0, x[94])
def l340_95(x):
    # x is a list (or vector) of length 304
    return max(0, x[95])
def l340_96(x):
    # x is a list (or vector) of length 304
    return max(0, x[96])
def l340_97(x):
    # x is a list (or vector) of length 304
    return max(0, x[97])
def l340_98(x):
    # x is a list (or vector) of length 304
    return max(0, x[98])
def l340_99(x):
    # x is a list (or vector) of length 304
    return max(0, x[99])
def l340_100(x):
    # x is a list (or vector) of length 304
    return max(0, x[100])
def l340_101(x):
    # x is a list (or vector) of length 304
    return max(0, x[101])
def l340_102(x):
    # x is a list (or vector) of length 304
    return max(0, x[102])
def l340_103(x):
    # x is a list (or vector) of length 304
    return max(0, x[103])
def l340_104(x):
    # x is a list (or vector) of length 304
    return max(0, x[104])
def l340_105(x):
    # x is a list (or vector) of length 304
    return max(0, x[105])
def l340_106(x):
    # x is a list (or vector) of length 304
    return max(0, x[106])
def l340_107(x):
    # x is a list (or vector) of length 304
    return max(0, x[107])
def l340_108(x):
    # x is a list (or vector) of length 304
    return max(0, x[108])
def l340_109(x):
    # x is a list (or vector) of length 304
    return max(0, x[109])
def l340_110(x):
    # x is a list (or vector) of length 304
    return max(0, x[110])
def l340_111(x):
    # x is a list (or vector) of length 304
    return max(0, x[111])
def l340_112(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[112] + -1.0*x[128] + 1.0)
def l340_113(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[113] + -1.0*x[129] + 1.0)
def l340_114(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[114] + -1.0*x[130] + 1.0)
def l340_115(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[115] + -1.0*x[131] + 1.0)
def l340_116(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[116] + -1.0*x[132] + 1.0)
def l340_117(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[117] + -1.0*x[133] + 1.0)
def l340_118(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[118] + -1.0*x[134] + 1.0)
def l340_119(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[119] + -1.0*x[135] + 1.0)
def l340_120(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[120] + -1.0*x[136] + 1.0)
def l340_121(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[121] + -1.0*x[137] + 1.0)
def l340_122(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[122] + -1.0*x[138] + 1.0)
def l340_123(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[123] + -1.0*x[139] + 1.0)
def l340_124(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[124] + -1.0*x[140] + 1.0)
def l340_125(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[125] + -1.0*x[141] + 1.0)
def l340_126(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[126] + -1.0*x[142] + 1.0)
def l340_127(x):
    # x is a list (or vector) of length 304
    return max(0, -1.0*x[127] + -1.0*x[143] + 1.0)
def l340_128(x):
    # x is a list (or vector) of length 304
    return max(0, x[160])
def l340_129(x):
    # x is a list (or vector) of length 304
    return max(0, x[161])
def l340_130(x):
    # x is a list (or vector) of length 304
    return max(0, x[162])
def l340_131(x):
    # x is a list (or vector) of length 304
    return max(0, x[163])
def l340_132(x):
    # x is a list (or vector) of length 304
    return max(0, x[164])
def l340_133(x):
    # x is a list (or vector) of length 304
    return max(0, x[165])
def l340_134(x):
    # x is a list (or vector) of length 304
    return max(0, x[166])
def l340_135(x):
    # x is a list (or vector) of length 304
    return max(0, x[167])
def l340_136(x):
    # x is a list (or vector) of length 304
    return max(0, x[168])
def l340_137(x):
    # x is a list (or vector) of length 304
    return max(0, x[169])
def l340_138(x):
    # x is a list (or vector) of length 304
    return max(0, x[170])
def l340_139(x):
    # x is a list (or vector) of length 304
    return max(0, x[171])
def l340_140(x):
    # x is a list (or vector) of length 304
    return max(0, x[172])
def l340_141(x):
    # x is a list (or vector) of length 304
    return max(0, x[173])
def l340_142(x):
    # x is a list (or vector) of length 304
    return max(0, x[174])
def l340_143(x):
    # x is a list (or vector) of length 304
    return max(0, x[175])
def l340_144(x):
    # x is a list (or vector) of length 304
    return max(0, x[144])
def l340_145(x):
    # x is a list (or vector) of length 304
    return max(0, x[145])
def l340_146(x):
    # x is a list (or vector) of length 304
    return max(0, x[146])
def l340_147(x):
    # x is a list (or vector) of length 304
    return max(0, x[147])
def l340_148(x):
    # x is a list (or vector) of length 304
    return max(0, x[148])
def l340_149(x):
    # x is a list (or vector) of length 304
    return max(0, x[149])
def l340_150(x):
    # x is a list (or vector) of length 304
    return max(0, x[150])
def l340_151(x):
    # x is a list (or vector) of length 304
    return max(0, x[151])
def l340_152(x):
    # x is a list (or vector) of length 304
    return max(0, x[152])
def l340_153(x):
    # x is a list (or vector) of length 304
    return max(0, x[153])
def l340_154(x):
    # x is a list (or vector) of length 304
    return max(0, x[154])
def l340_155(x):
    # x is a list (or vector) of length 304
    return max(0, x[155])
def l340_156(x):
    # x is a list (or vector) of length 304
    return max(0, x[156])
def l340_157(x):
    # x is a list (or vector) of length 304
    return max(0, x[157])
def l340_158(x):
    # x is a list (or vector) of length 304
    return max(0, x[158])
def l340_159(x):
    # x is a list (or vector) of length 304
    return max(0, x[159])
def l340_160(x):
    # x is a list (or vector) of length 304
    return max(0, x[176])
def l340_161(x):
    # x is a list (or vector) of length 304
    return max(0, x[177])
def l340_162(x):
    # x is a list (or vector) of length 304
    return max(0, x[178])
def l340_163(x):
    # x is a list (or vector) of length 304
    return max(0, x[179])
def l340_164(x):
    # x is a list (or vector) of length 304
    return max(0, x[180])
def l340_165(x):
    # x is a list (or vector) of length 304
    return max(0, x[181])
def l340_166(x):
    # x is a list (or vector) of length 304
    return max(0, x[182])
def l340_167(x):
    # x is a list (or vector) of length 304
    return max(0, x[183])
def l340_168(x):
    # x is a list (or vector) of length 304
    return max(0, x[184])
def l340_169(x):
    # x is a list (or vector) of length 304
    return max(0, x[185])
def l340_170(x):
    # x is a list (or vector) of length 304
    return max(0, x[186])
def l340_171(x):
    # x is a list (or vector) of length 304
    return max(0, x[187])
def l340_172(x):
    # x is a list (or vector) of length 304
    return max(0, x[188])
def l340_173(x):
    # x is a list (or vector) of length 304
    return max(0, x[189])
def l340_174(x):
    # x is a list (or vector) of length 304
    return max(0, x[190])
def l340_175(x):
    # x is a list (or vector) of length 304
    return max(0, x[191])
def l340_176(x):
    # x is a list (or vector) of length 304
    return max(0, x[192])
def l340_177(x):
    # x is a list (or vector) of length 304
    return max(0, x[193])
def l340_178(x):
    # x is a list (or vector) of length 304
    return max(0, x[194])
def l340_179(x):
    # x is a list (or vector) of length 304
    return max(0, x[195])
def l340_180(x):
    # x is a list (or vector) of length 304
    return max(0, x[196])
def l340_181(x):
    # x is a list (or vector) of length 304
    return max(0, x[197])
def l340_182(x):
    # x is a list (or vector) of length 304
    return max(0, x[198])
def l340_183(x):
    # x is a list (or vector) of length 304
    return max(0, x[199])
def l340_184(x):
    # x is a list (or vector) of length 304
    return max(0, x[200])
def l340_185(x):
    # x is a list (or vector) of length 304
    return max(0, x[201])
def l340_186(x):
    # x is a list (or vector) of length 304
    return max(0, x[202])
def l340_187(x):
    # x is a list (or vector) of length 304
    return max(0, x[203])
def l340_188(x):
    # x is a list (or vector) of length 304
    return max(0, x[204])
def l340_189(x):
    # x is a list (or vector) of length 304
    return max(0, x[205])
def l340_190(x):
    # x is a list (or vector) of length 304
    return max(0, x[206])
def l340_191(x):
    # x is a list (or vector) of length 304
    return max(0, x[207])
def l340_192(x):
    # x is a list (or vector) of length 304
    return max(0, x[208])
def l340_193(x):
    # x is a list (or vector) of length 304
    return max(0, x[209])
def l340_194(x):
    # x is a list (or vector) of length 304
    return max(0, x[210])
def l340_195(x):
    # x is a list (or vector) of length 304
    return max(0, x[211])
def l340_196(x):
    # x is a list (or vector) of length 304
    return max(0, x[212])
def l340_197(x):
    # x is a list (or vector) of length 304
    return max(0, x[213])
def l340_198(x):
    # x is a list (or vector) of length 304
    return max(0, x[214])
def l340_199(x):
    # x is a list (or vector) of length 304
    return max(0, x[215])
def l340_200(x):
    # x is a list (or vector) of length 304
    return max(0, x[216])
def l340_201(x):
    # x is a list (or vector) of length 304
    return max(0, x[217])
def l340_202(x):
    # x is a list (or vector) of length 304
    return max(0, x[218])
def l340_203(x):
    # x is a list (or vector) of length 304
    return max(0, x[219])
def l340_204(x):
    # x is a list (or vector) of length 304
    return max(0, x[220])
def l340_205(x):
    # x is a list (or vector) of length 304
    return max(0, x[221])
def l340_206(x):
    # x is a list (or vector) of length 304
    return max(0, x[222])
def l340_207(x):
    # x is a list (or vector) of length 304
    return max(0, x[223])
def l340_208(x):
    # x is a list (or vector) of length 304
    return max(0, x[224])
def l340_209(x):
    # x is a list (or vector) of length 304
    return max(0, x[225])
def l340_210(x):
    # x is a list (or vector) of length 304
    return max(0, x[226])
def l340_211(x):
    # x is a list (or vector) of length 304
    return max(0, x[227])
def l340_212(x):
    # x is a list (or vector) of length 304
    return max(0, x[228])
def l340_213(x):
    # x is a list (or vector) of length 304
    return max(0, x[229])
def l340_214(x):
    # x is a list (or vector) of length 304
    return max(0, x[230])
def l340_215(x):
    # x is a list (or vector) of length 304
    return max(0, x[231])
def l340_216(x):
    # x is a list (or vector) of length 304
    return max(0, x[232])
def l340_217(x):
    # x is a list (or vector) of length 304
    return max(0, x[233])
def l340_218(x):
    # x is a list (or vector) of length 304
    return max(0, x[234])
def l340_219(x):
    # x is a list (or vector) of length 304
    return max(0, x[235])
def l340_220(x):
    # x is a list (or vector) of length 304
    return max(0, x[236])
def l340_221(x):
    # x is a list (or vector) of length 304
    return max(0, x[237])
def l340_222(x):
    # x is a list (or vector) of length 304
    return max(0, x[238])
def l340_223(x):
    # x is a list (or vector) of length 304
    return max(0, x[239])
def l340_224(x):
    # x is a list (or vector) of length 304
    return max(0, x[240])
def l340_225(x):
    # x is a list (or vector) of length 304
    return max(0, x[241])
def l340_226(x):
    # x is a list (or vector) of length 304
    return max(0, x[242])
def l340_227(x):
    # x is a list (or vector) of length 304
    return max(0, x[243])
def l340_228(x):
    # x is a list (or vector) of length 304
    return max(0, x[244])
def l340_229(x):
    # x is a list (or vector) of length 304
    return max(0, x[245])
def l340_230(x):
    # x is a list (or vector) of length 304
    return max(0, x[246])
def l340_231(x):
    # x is a list (or vector) of length 304
    return max(0, x[247])
def l340_232(x):
    # x is a list (or vector) of length 304
    return max(0, x[248])
def l340_233(x):
    # x is a list (or vector) of length 304
    return max(0, x[249])
def l340_234(x):
    # x is a list (or vector) of length 304
    return max(0, x[250])
def l340_235(x):
    # x is a list (or vector) of length 304
    return max(0, x[251])
def l340_236(x):
    # x is a list (or vector) of length 304
    return max(0, x[252])
def l340_237(x):
    # x is a list (or vector) of length 304
    return max(0, x[253])
def l340_238(x):
    # x is a list (or vector) of length 304
    return max(0, x[254])
def l340_239(x):
    # x is a list (or vector) of length 304
    return max(0, x[255])
def l340_240(x):
    # x is a list (or vector) of length 304
    return max(0, x[256])
def l340_241(x):
    # x is a list (or vector) of length 304
    return max(0, x[257])
def l340_242(x):
    # x is a list (or vector) of length 304
    return max(0, x[258])
def l340_243(x):
    # x is a list (or vector) of length 304
    return max(0, x[259])
def l340_244(x):
    # x is a list (or vector) of length 304
    return max(0, x[260])
def l340_245(x):
    # x is a list (or vector) of length 304
    return max(0, x[261])
def l340_246(x):
    # x is a list (or vector) of length 304
    return max(0, x[262])
def l340_247(x):
    # x is a list (or vector) of length 304
    return max(0, x[263])
def l340_248(x):
    # x is a list (or vector) of length 304
    return max(0, x[264])
def l340_249(x):
    # x is a list (or vector) of length 304
    return max(0, x[265])
def l340_250(x):
    # x is a list (or vector) of length 304
    return max(0, x[266])
def l340_251(x):
    # x is a list (or vector) of length 304
    return max(0, x[267])
def l340_252(x):
    # x is a list (or vector) of length 304
    return max(0, x[268])
def l340_253(x):
    # x is a list (or vector) of length 304
    return max(0, x[269])
def l340_254(x):
    # x is a list (or vector) of length 304
    return max(0, x[270])
def l340_255(x):
    # x is a list (or vector) of length 304
    return max(0, x[271])
def l340_256(x):
    # x is a list (or vector) of length 304
    return max(0, x[272])
def l340_257(x):
    # x is a list (or vector) of length 304
    return max(0, x[273])
def l340_258(x):
    # x is a list (or vector) of length 304
    return max(0, x[274])
def l340_259(x):
    # x is a list (or vector) of length 304
    return max(0, x[275])
def l340_260(x):
    # x is a list (or vector) of length 304
    return max(0, x[276])
def l340_261(x):
    # x is a list (or vector) of length 304
    return max(0, x[277])
def l340_262(x):
    # x is a list (or vector) of length 304
    return max(0, x[278])
def l340_263(x):
    # x is a list (or vector) of length 304
    return max(0, x[279])
def l340_264(x):
    # x is a list (or vector) of length 304
    return max(0, x[280])
def l340_265(x):
    # x is a list (or vector) of length 304
    return max(0, x[281])
def l340_266(x):
    # x is a list (or vector) of length 304
    return max(0, x[282])
def l340_267(x):
    # x is a list (or vector) of length 304
    return max(0, x[283])
def l340_268(x):
    # x is a list (or vector) of length 304
    return max(0, x[284])
def l340_269(x):
    # x is a list (or vector) of length 304
    return max(0, x[285])
def l340_270(x):
    # x is a list (or vector) of length 304
    return max(0, x[286])
def l340_271(x):
    # x is a list (or vector) of length 304
    return max(0, x[287])
def l340_272(x):
    # x is a list (or vector) of length 304
    return max(0, x[288])
def l340_273(x):
    # x is a list (or vector) of length 304
    return max(0, x[289])
def l340_274(x):
    # x is a list (or vector) of length 304
    return max(0, x[290])
def l340_275(x):
    # x is a list (or vector) of length 304
    return max(0, x[291])
def l340_276(x):
    # x is a list (or vector) of length 304
    return max(0, x[292])
def l340_277(x):
    # x is a list (or vector) of length 304
    return max(0, x[293])
def l340_278(x):
    # x is a list (or vector) of length 304
    return max(0, x[294])
def l340_279(x):
    # x is a list (or vector) of length 304
    return max(0, x[295])
def l340_280(x):
    # x is a list (or vector) of length 304
    return max(0, x[296])
def l340_281(x):
    # x is a list (or vector) of length 304
    return max(0, x[297])
def l340_282(x):
    # x is a list (or vector) of length 304
    return max(0, x[298])
def l340_283(x):
    # x is a list (or vector) of length 304
    return max(0, x[299])
def l340_284(x):
    # x is a list (or vector) of length 304
    return max(0, x[300])
def l340_285(x):
    # x is a list (or vector) of length 304
    return max(0, x[301])
def l340_286(x):
    # x is a list (or vector) of length 304
    return max(0, x[302])
def l340_287(x):
    # x is a list (or vector) of length 304
    return max(0, x[303])
def l340_(x):
    # x is a list (or vector) of length 304
    return [
        l340_0(x),
        l340_1(x),
        l340_2(x),
        l340_3(x),
        l340_4(x),
        l340_5(x),
        l340_6(x),
        l340_7(x),
        l340_8(x),
        l340_9(x),
        l340_10(x),
        l340_11(x),
        l340_12(x),
        l340_13(x),
        l340_14(x),
        l340_15(x),
        l340_16(x),
        l340_17(x),
        l340_18(x),
        l340_19(x),
        l340_20(x),
        l340_21(x),
        l340_22(x),
        l340_23(x),
        l340_24(x),
        l340_25(x),
        l340_26(x),
        l340_27(x),
        l340_28(x),
        l340_29(x),
        l340_30(x),
        l340_31(x),
        l340_32(x),
        l340_33(x),
        l340_34(x),
        l340_35(x),
        l340_36(x),
        l340_37(x),
        l340_38(x),
        l340_39(x),
        l340_40(x),
        l340_41(x),
        l340_42(x),
        l340_43(x),
        l340_44(x),
        l340_45(x),
        l340_46(x),
        l340_47(x),
        l340_48(x),
        l340_49(x),
        l340_50(x),
        l340_51(x),
        l340_52(x),
        l340_53(x),
        l340_54(x),
        l340_55(x),
        l340_56(x),
        l340_57(x),
        l340_58(x),
        l340_59(x),
        l340_60(x),
        l340_61(x),
        l340_62(x),
        l340_63(x),
        l340_64(x),
        l340_65(x),
        l340_66(x),
        l340_67(x),
        l340_68(x),
        l340_69(x),
        l340_70(x),
        l340_71(x),
        l340_72(x),
        l340_73(x),
        l340_74(x),
        l340_75(x),
        l340_76(x),
        l340_77(x),
        l340_78(x),
        l340_79(x),
        l340_80(x),
        l340_81(x),
        l340_82(x),
        l340_83(x),
        l340_84(x),
        l340_85(x),
        l340_86(x),
        l340_87(x),
        l340_88(x),
        l340_89(x),
        l340_90(x),
        l340_91(x),
        l340_92(x),
        l340_93(x),
        l340_94(x),
        l340_95(x),
        l340_96(x),
        l340_97(x),
        l340_98(x),
        l340_99(x),
        l340_100(x),
        l340_101(x),
        l340_102(x),
        l340_103(x),
        l340_104(x),
        l340_105(x),
        l340_106(x),
        l340_107(x),
        l340_108(x),
        l340_109(x),
        l340_110(x),
        l340_111(x),
        l340_112(x),
        l340_113(x),
        l340_114(x),
        l340_115(x),
        l340_116(x),
        l340_117(x),
        l340_118(x),
        l340_119(x),
        l340_120(x),
        l340_121(x),
        l340_122(x),
        l340_123(x),
        l340_124(x),
        l340_125(x),
        l340_126(x),
        l340_127(x),
        l340_128(x),
        l340_129(x),
        l340_130(x),
        l340_131(x),
        l340_132(x),
        l340_133(x),
        l340_134(x),
        l340_135(x),
        l340_136(x),
        l340_137(x),
        l340_138(x),
        l340_139(x),
        l340_140(x),
        l340_141(x),
        l340_142(x),
        l340_143(x),
        l340_144(x),
        l340_145(x),
        l340_146(x),
        l340_147(x),
        l340_148(x),
        l340_149(x),
        l340_150(x),
        l340_151(x),
        l340_152(x),
        l340_153(x),
        l340_154(x),
        l340_155(x),
        l340_156(x),
        l340_157(x),
        l340_158(x),
        l340_159(x),
        l340_160(x),
        l340_161(x),
        l340_162(x),
        l340_163(x),
        l340_164(x),
        l340_165(x),
        l340_166(x),
        l340_167(x),
        l340_168(x),
        l340_169(x),
        l340_170(x),
        l340_171(x),
        l340_172(x),
        l340_173(x),
        l340_174(x),
        l340_175(x),
        l340_176(x),
        l340_177(x),
        l340_178(x),
        l340_179(x),
        l340_180(x),
        l340_181(x),
        l340_182(x),
        l340_183(x),
        l340_184(x),
        l340_185(x),
        l340_186(x),
        l340_187(x),
        l340_188(x),
        l340_189(x),
        l340_190(x),
        l340_191(x),
        l340_192(x),
        l340_193(x),
        l340_194(x),
        l340_195(x),
        l340_196(x),
        l340_197(x),
        l340_198(x),
        l340_199(x),
        l340_200(x),
        l340_201(x),
        l340_202(x),
        l340_203(x),
        l340_204(x),
        l340_205(x),
        l340_206(x),
        l340_207(x),
        l340_208(x),
        l340_209(x),
        l340_210(x),
        l340_211(x),
        l340_212(x),
        l340_213(x),
        l340_214(x),
        l340_215(x),
        l340_216(x),
        l340_217(x),
        l340_218(x),
        l340_219(x),
        l340_220(x),
        l340_221(x),
        l340_222(x),
        l340_223(x),
        l340_224(x),
        l340_225(x),
        l340_226(x),
        l340_227(x),
        l340_228(x),
        l340_229(x),
        l340_230(x),
        l340_231(x),
        l340_232(x),
        l340_233(x),
        l340_234(x),
        l340_235(x),
        l340_236(x),
        l340_237(x),
        l340_238(x),
        l340_239(x),
        l340_240(x),
        l340_241(x),
        l340_242(x),
        l340_243(x),
        l340_244(x),
        l340_245(x),
        l340_246(x),
        l340_247(x),
        l340_248(x),
        l340_249(x),
        l340_250(x),
        l340_251(x),
        l340_252(x),
        l340_253(x),
        l340_254(x),
        l340_255(x),
        l340_256(x),
        l340_257(x),
        l340_258(x),
        l340_259(x),
        l340_260(x),
        l340_261(x),
        l340_262(x),
        l340_263(x),
        l340_264(x),
        l340_265(x),
        l340_266(x),
        l340_267(x),
        l340_268(x),
        l340_269(x),
        l340_270(x),
        l340_271(x),
        l340_272(x),
        l340_273(x),
        l340_274(x),
        l340_275(x),
        l340_276(x),
        l340_277(x),
        l340_278(x),
        l340_279(x),
        l340_280(x),
        l340_281(x),
        l340_282(x),
        l340_283(x),
        l340_284(x),
        l340_285(x),
        l340_286(x),
        l340_287(x),
    ]