import numpy as np




# Generated from reverse engineering
def l402_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 288
    out = np.empty(288, dtype=np.float32)
    
    # for i in range(0, 96):
    for i in range(0, 96):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(96, 128):
    for i in range(0, 32):
        s = x[96 + i] + x[160 + i] + -2.0 * x[i + 128]
        s += biases[i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 160):
    for i in range(0, 32):
        s = x[96 + i] + x[160 + i] + -2.0 * x[i + 128]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(160, 192):
    for i in range(0, 32):
        s = x[96 + i] + x[160 + i] + -2.0 * x[i + 128]
        s += biases[i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(192, 288):
    for i in range(0, 96):
        s = x[192 + i]
        out[192 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l402_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l402_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l402_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l402_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l402_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l402_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l402_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l402_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l402_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l402_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l402_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l402_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l402_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l402_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l402_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l402_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l402_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l402_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l402_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l402_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l402_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l402_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l402_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l402_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l402_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l402_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l402_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l402_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l402_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l402_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l402_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l402_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l402_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l402_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l402_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l402_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l402_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l402_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l402_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l402_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l402_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l402_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l402_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l402_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l402_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l402_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l402_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l402_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l402_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l402_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l402_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l402_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l402_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l402_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l402_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l402_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l402_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l402_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l402_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l402_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l402_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l402_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l402_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l402_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l402_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l402_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l402_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l402_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l402_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l402_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l402_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l402_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l402_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l402_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l402_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l402_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l402_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l402_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l402_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l402_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l402_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l402_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l402_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l402_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l402_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l402_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l402_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l402_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l402_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l402_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l402_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l402_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l402_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l402_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l402_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l402_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l402_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + -2.0*x[128] + x[160] + -1.0)
def l402_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + -2.0*x[129] + x[161] + -1.0)
def l402_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + -2.0*x[130] + x[162] + -1.0)
def l402_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + -2.0*x[131] + x[163] + -1.0)
def l402_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + -2.0*x[132] + x[164] + -1.0)
def l402_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + -2.0*x[133] + x[165] + -1.0)
def l402_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + -2.0*x[134] + x[166] + -1.0)
def l402_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + -2.0*x[135] + x[167] + -1.0)
def l402_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + -2.0*x[136] + x[168] + -1.0)
def l402_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + -2.0*x[137] + x[169] + -1.0)
def l402_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + -2.0*x[138] + x[170] + -1.0)
def l402_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + -2.0*x[139] + x[171] + -1.0)
def l402_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + -2.0*x[140] + x[172] + -1.0)
def l402_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + -2.0*x[141] + x[173] + -1.0)
def l402_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + -2.0*x[142] + x[174] + -1.0)
def l402_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + -2.0*x[143] + x[175] + -1.0)
def l402_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[112] + -2.0*x[144] + x[176] + -1.0)
def l402_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[113] + -2.0*x[145] + x[177] + -1.0)
def l402_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[114] + -2.0*x[146] + x[178] + -1.0)
def l402_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[115] + -2.0*x[147] + x[179] + -1.0)
def l402_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[116] + -2.0*x[148] + x[180] + -1.0)
def l402_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[117] + -2.0*x[149] + x[181] + -1.0)
def l402_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[118] + -2.0*x[150] + x[182] + -1.0)
def l402_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[119] + -2.0*x[151] + x[183] + -1.0)
def l402_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[120] + -2.0*x[152] + x[184] + -1.0)
def l402_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[121] + -2.0*x[153] + x[185] + -1.0)
def l402_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[122] + -2.0*x[154] + x[186] + -1.0)
def l402_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[123] + -2.0*x[155] + x[187] + -1.0)
def l402_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[124] + -2.0*x[156] + x[188] + -1.0)
def l402_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[125] + -2.0*x[157] + x[189] + -1.0)
def l402_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[126] + -2.0*x[158] + x[190] + -1.0)
def l402_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[127] + -2.0*x[159] + x[191] + -1.0)
def l402_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + -2.0*x[128] + x[160])
def l402_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + -2.0*x[129] + x[161])
def l402_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + -2.0*x[130] + x[162])
def l402_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + -2.0*x[131] + x[163])
def l402_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + -2.0*x[132] + x[164])
def l402_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + -2.0*x[133] + x[165])
def l402_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + -2.0*x[134] + x[166])
def l402_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + -2.0*x[135] + x[167])
def l402_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + -2.0*x[136] + x[168])
def l402_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + -2.0*x[137] + x[169])
def l402_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + -2.0*x[138] + x[170])
def l402_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + -2.0*x[139] + x[171])
def l402_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + -2.0*x[140] + x[172])
def l402_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + -2.0*x[141] + x[173])
def l402_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + -2.0*x[142] + x[174])
def l402_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + -2.0*x[143] + x[175])
def l402_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[112] + -2.0*x[144] + x[176])
def l402_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[113] + -2.0*x[145] + x[177])
def l402_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[114] + -2.0*x[146] + x[178])
def l402_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[115] + -2.0*x[147] + x[179])
def l402_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[116] + -2.0*x[148] + x[180])
def l402_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[117] + -2.0*x[149] + x[181])
def l402_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[118] + -2.0*x[150] + x[182])
def l402_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[119] + -2.0*x[151] + x[183])
def l402_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[120] + -2.0*x[152] + x[184])
def l402_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[121] + -2.0*x[153] + x[185])
def l402_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[122] + -2.0*x[154] + x[186])
def l402_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[123] + -2.0*x[155] + x[187])
def l402_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[124] + -2.0*x[156] + x[188])
def l402_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[125] + -2.0*x[157] + x[189])
def l402_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[126] + -2.0*x[158] + x[190])
def l402_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[127] + -2.0*x[159] + x[191])
def l402_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + -2.0*x[128] + x[160] + -1.0)
def l402_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + -2.0*x[129] + x[161] + -1.0)
def l402_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + -2.0*x[130] + x[162] + -1.0)
def l402_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + -2.0*x[131] + x[163] + -1.0)
def l402_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + -2.0*x[132] + x[164] + -1.0)
def l402_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + -2.0*x[133] + x[165] + -1.0)
def l402_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + -2.0*x[134] + x[166] + -1.0)
def l402_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + -2.0*x[135] + x[167] + -1.0)
def l402_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + -2.0*x[136] + x[168] + -1.0)
def l402_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + -2.0*x[137] + x[169] + -1.0)
def l402_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + -2.0*x[138] + x[170] + -1.0)
def l402_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + -2.0*x[139] + x[171] + -1.0)
def l402_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + -2.0*x[140] + x[172] + -1.0)
def l402_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + -2.0*x[141] + x[173] + -1.0)
def l402_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + -2.0*x[142] + x[174] + -1.0)
def l402_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + -2.0*x[143] + x[175] + -1.0)
def l402_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[112] + -2.0*x[144] + x[176] + -1.0)
def l402_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[113] + -2.0*x[145] + x[177] + -1.0)
def l402_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[114] + -2.0*x[146] + x[178] + -1.0)
def l402_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[115] + -2.0*x[147] + x[179] + -1.0)
def l402_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[116] + -2.0*x[148] + x[180] + -1.0)
def l402_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[117] + -2.0*x[149] + x[181] + -1.0)
def l402_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[118] + -2.0*x[150] + x[182] + -1.0)
def l402_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[119] + -2.0*x[151] + x[183] + -1.0)
def l402_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[120] + -2.0*x[152] + x[184] + -1.0)
def l402_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[121] + -2.0*x[153] + x[185] + -1.0)
def l402_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[122] + -2.0*x[154] + x[186] + -1.0)
def l402_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[123] + -2.0*x[155] + x[187] + -1.0)
def l402_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[124] + -2.0*x[156] + x[188] + -1.0)
def l402_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[125] + -2.0*x[157] + x[189] + -1.0)
def l402_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[126] + -2.0*x[158] + x[190] + -1.0)
def l402_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[127] + -2.0*x[159] + x[191] + -1.0)
def l402_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l402_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l402_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l402_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l402_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l402_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l402_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l402_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l402_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l402_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l402_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l402_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l402_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l402_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l402_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l402_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l402_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l402_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l402_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l402_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l402_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l402_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l402_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l402_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l402_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l402_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l402_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l402_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l402_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l402_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l402_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l402_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l402_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l402_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l402_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l402_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l402_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l402_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l402_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l402_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l402_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l402_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l402_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l402_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l402_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l402_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l402_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l402_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l402_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l402_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l402_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l402_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l402_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l402_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l402_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l402_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l402_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l402_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l402_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l402_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l402_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l402_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l402_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l402_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l402_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l402_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l402_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l402_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l402_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l402_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l402_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l402_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l402_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l402_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l402_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l402_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l402_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l402_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l402_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l402_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l402_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l402_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l402_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l402_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l402_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l402_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l402_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l402_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l402_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l402_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l402_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l402_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l402_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l402_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l402_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l402_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l402_(x):
    # x is a list (or vector) of length 288
    return [
        l402_0(x),
        l402_1(x),
        l402_2(x),
        l402_3(x),
        l402_4(x),
        l402_5(x),
        l402_6(x),
        l402_7(x),
        l402_8(x),
        l402_9(x),
        l402_10(x),
        l402_11(x),
        l402_12(x),
        l402_13(x),
        l402_14(x),
        l402_15(x),
        l402_16(x),
        l402_17(x),
        l402_18(x),
        l402_19(x),
        l402_20(x),
        l402_21(x),
        l402_22(x),
        l402_23(x),
        l402_24(x),
        l402_25(x),
        l402_26(x),
        l402_27(x),
        l402_28(x),
        l402_29(x),
        l402_30(x),
        l402_31(x),
        l402_32(x),
        l402_33(x),
        l402_34(x),
        l402_35(x),
        l402_36(x),
        l402_37(x),
        l402_38(x),
        l402_39(x),
        l402_40(x),
        l402_41(x),
        l402_42(x),
        l402_43(x),
        l402_44(x),
        l402_45(x),
        l402_46(x),
        l402_47(x),
        l402_48(x),
        l402_49(x),
        l402_50(x),
        l402_51(x),
        l402_52(x),
        l402_53(x),
        l402_54(x),
        l402_55(x),
        l402_56(x),
        l402_57(x),
        l402_58(x),
        l402_59(x),
        l402_60(x),
        l402_61(x),
        l402_62(x),
        l402_63(x),
        l402_64(x),
        l402_65(x),
        l402_66(x),
        l402_67(x),
        l402_68(x),
        l402_69(x),
        l402_70(x),
        l402_71(x),
        l402_72(x),
        l402_73(x),
        l402_74(x),
        l402_75(x),
        l402_76(x),
        l402_77(x),
        l402_78(x),
        l402_79(x),
        l402_80(x),
        l402_81(x),
        l402_82(x),
        l402_83(x),
        l402_84(x),
        l402_85(x),
        l402_86(x),
        l402_87(x),
        l402_88(x),
        l402_89(x),
        l402_90(x),
        l402_91(x),
        l402_92(x),
        l402_93(x),
        l402_94(x),
        l402_95(x),
        l402_96(x),
        l402_97(x),
        l402_98(x),
        l402_99(x),
        l402_100(x),
        l402_101(x),
        l402_102(x),
        l402_103(x),
        l402_104(x),
        l402_105(x),
        l402_106(x),
        l402_107(x),
        l402_108(x),
        l402_109(x),
        l402_110(x),
        l402_111(x),
        l402_112(x),
        l402_113(x),
        l402_114(x),
        l402_115(x),
        l402_116(x),
        l402_117(x),
        l402_118(x),
        l402_119(x),
        l402_120(x),
        l402_121(x),
        l402_122(x),
        l402_123(x),
        l402_124(x),
        l402_125(x),
        l402_126(x),
        l402_127(x),
        l402_128(x),
        l402_129(x),
        l402_130(x),
        l402_131(x),
        l402_132(x),
        l402_133(x),
        l402_134(x),
        l402_135(x),
        l402_136(x),
        l402_137(x),
        l402_138(x),
        l402_139(x),
        l402_140(x),
        l402_141(x),
        l402_142(x),
        l402_143(x),
        l402_144(x),
        l402_145(x),
        l402_146(x),
        l402_147(x),
        l402_148(x),
        l402_149(x),
        l402_150(x),
        l402_151(x),
        l402_152(x),
        l402_153(x),
        l402_154(x),
        l402_155(x),
        l402_156(x),
        l402_157(x),
        l402_158(x),
        l402_159(x),
        l402_160(x),
        l402_161(x),
        l402_162(x),
        l402_163(x),
        l402_164(x),
        l402_165(x),
        l402_166(x),
        l402_167(x),
        l402_168(x),
        l402_169(x),
        l402_170(x),
        l402_171(x),
        l402_172(x),
        l402_173(x),
        l402_174(x),
        l402_175(x),
        l402_176(x),
        l402_177(x),
        l402_178(x),
        l402_179(x),
        l402_180(x),
        l402_181(x),
        l402_182(x),
        l402_183(x),
        l402_184(x),
        l402_185(x),
        l402_186(x),
        l402_187(x),
        l402_188(x),
        l402_189(x),
        l402_190(x),
        l402_191(x),
        l402_192(x),
        l402_193(x),
        l402_194(x),
        l402_195(x),
        l402_196(x),
        l402_197(x),
        l402_198(x),
        l402_199(x),
        l402_200(x),
        l402_201(x),
        l402_202(x),
        l402_203(x),
        l402_204(x),
        l402_205(x),
        l402_206(x),
        l402_207(x),
        l402_208(x),
        l402_209(x),
        l402_210(x),
        l402_211(x),
        l402_212(x),
        l402_213(x),
        l402_214(x),
        l402_215(x),
        l402_216(x),
        l402_217(x),
        l402_218(x),
        l402_219(x),
        l402_220(x),
        l402_221(x),
        l402_222(x),
        l402_223(x),
        l402_224(x),
        l402_225(x),
        l402_226(x),
        l402_227(x),
        l402_228(x),
        l402_229(x),
        l402_230(x),
        l402_231(x),
        l402_232(x),
        l402_233(x),
        l402_234(x),
        l402_235(x),
        l402_236(x),
        l402_237(x),
        l402_238(x),
        l402_239(x),
        l402_240(x),
        l402_241(x),
        l402_242(x),
        l402_243(x),
        l402_244(x),
        l402_245(x),
        l402_246(x),
        l402_247(x),
        l402_248(x),
        l402_249(x),
        l402_250(x),
        l402_251(x),
        l402_252(x),
        l402_253(x),
        l402_254(x),
        l402_255(x),
        l402_256(x),
        l402_257(x),
        l402_258(x),
        l402_259(x),
        l402_260(x),
        l402_261(x),
        l402_262(x),
        l402_263(x),
        l402_264(x),
        l402_265(x),
        l402_266(x),
        l402_267(x),
        l402_268(x),
        l402_269(x),
        l402_270(x),
        l402_271(x),
        l402_272(x),
        l402_273(x),
        l402_274(x),
        l402_275(x),
        l402_276(x),
        l402_277(x),
        l402_278(x),
        l402_279(x),
        l402_280(x),
        l402_281(x),
        l402_282(x),
        l402_283(x),
        l402_284(x),
        l402_285(x),
        l402_286(x),
        l402_287(x),
    ]