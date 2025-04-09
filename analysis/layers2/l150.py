import numpy as np




# Generated from reverse engineering
def l150_g(x: np.ndarray) -> np.ndarray:
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




def l150_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l150_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l150_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l150_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l150_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l150_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l150_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l150_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l150_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l150_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l150_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l150_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l150_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l150_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l150_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l150_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l150_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l150_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l150_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l150_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l150_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l150_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l150_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l150_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l150_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l150_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l150_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l150_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l150_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l150_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l150_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l150_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l150_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l150_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l150_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l150_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l150_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l150_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l150_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l150_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l150_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l150_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l150_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l150_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l150_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l150_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l150_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l150_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l150_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l150_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l150_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l150_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l150_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l150_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l150_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l150_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l150_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l150_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l150_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l150_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l150_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l150_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l150_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l150_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l150_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l150_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l150_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l150_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l150_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l150_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l150_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l150_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l150_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l150_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l150_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l150_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l150_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l150_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l150_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l150_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l150_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l150_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l150_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l150_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l150_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l150_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l150_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l150_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l150_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l150_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l150_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l150_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l150_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l150_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l150_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l150_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l150_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + -2.0*x[128] + x[160] + -1.0)
def l150_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + -2.0*x[129] + x[161] + -1.0)
def l150_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + -2.0*x[130] + x[162] + -1.0)
def l150_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + -2.0*x[131] + x[163] + -1.0)
def l150_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + -2.0*x[132] + x[164] + -1.0)
def l150_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + -2.0*x[133] + x[165] + -1.0)
def l150_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + -2.0*x[134] + x[166] + -1.0)
def l150_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + -2.0*x[135] + x[167] + -1.0)
def l150_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + -2.0*x[136] + x[168] + -1.0)
def l150_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + -2.0*x[137] + x[169] + -1.0)
def l150_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + -2.0*x[138] + x[170] + -1.0)
def l150_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + -2.0*x[139] + x[171] + -1.0)
def l150_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + -2.0*x[140] + x[172] + -1.0)
def l150_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + -2.0*x[141] + x[173] + -1.0)
def l150_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + -2.0*x[142] + x[174] + -1.0)
def l150_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + -2.0*x[143] + x[175] + -1.0)
def l150_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[112] + -2.0*x[144] + x[176] + -1.0)
def l150_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[113] + -2.0*x[145] + x[177] + -1.0)
def l150_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[114] + -2.0*x[146] + x[178] + -1.0)
def l150_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[115] + -2.0*x[147] + x[179] + -1.0)
def l150_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[116] + -2.0*x[148] + x[180] + -1.0)
def l150_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[117] + -2.0*x[149] + x[181] + -1.0)
def l150_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[118] + -2.0*x[150] + x[182] + -1.0)
def l150_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[119] + -2.0*x[151] + x[183] + -1.0)
def l150_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[120] + -2.0*x[152] + x[184] + -1.0)
def l150_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[121] + -2.0*x[153] + x[185] + -1.0)
def l150_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[122] + -2.0*x[154] + x[186] + -1.0)
def l150_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[123] + -2.0*x[155] + x[187] + -1.0)
def l150_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[124] + -2.0*x[156] + x[188] + -1.0)
def l150_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[125] + -2.0*x[157] + x[189] + -1.0)
def l150_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[126] + -2.0*x[158] + x[190] + -1.0)
def l150_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[127] + -2.0*x[159] + x[191] + -1.0)
def l150_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + -2.0*x[128] + x[160])
def l150_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + -2.0*x[129] + x[161])
def l150_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + -2.0*x[130] + x[162])
def l150_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + -2.0*x[131] + x[163])
def l150_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + -2.0*x[132] + x[164])
def l150_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + -2.0*x[133] + x[165])
def l150_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + -2.0*x[134] + x[166])
def l150_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + -2.0*x[135] + x[167])
def l150_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + -2.0*x[136] + x[168])
def l150_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + -2.0*x[137] + x[169])
def l150_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + -2.0*x[138] + x[170])
def l150_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + -2.0*x[139] + x[171])
def l150_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + -2.0*x[140] + x[172])
def l150_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + -2.0*x[141] + x[173])
def l150_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + -2.0*x[142] + x[174])
def l150_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + -2.0*x[143] + x[175])
def l150_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[112] + -2.0*x[144] + x[176])
def l150_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[113] + -2.0*x[145] + x[177])
def l150_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[114] + -2.0*x[146] + x[178])
def l150_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[115] + -2.0*x[147] + x[179])
def l150_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[116] + -2.0*x[148] + x[180])
def l150_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[117] + -2.0*x[149] + x[181])
def l150_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[118] + -2.0*x[150] + x[182])
def l150_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[119] + -2.0*x[151] + x[183])
def l150_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[120] + -2.0*x[152] + x[184])
def l150_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[121] + -2.0*x[153] + x[185])
def l150_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[122] + -2.0*x[154] + x[186])
def l150_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[123] + -2.0*x[155] + x[187])
def l150_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[124] + -2.0*x[156] + x[188])
def l150_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[125] + -2.0*x[157] + x[189])
def l150_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[126] + -2.0*x[158] + x[190])
def l150_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[127] + -2.0*x[159] + x[191])
def l150_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + -2.0*x[128] + x[160] + -1.0)
def l150_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + -2.0*x[129] + x[161] + -1.0)
def l150_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + -2.0*x[130] + x[162] + -1.0)
def l150_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + -2.0*x[131] + x[163] + -1.0)
def l150_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + -2.0*x[132] + x[164] + -1.0)
def l150_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + -2.0*x[133] + x[165] + -1.0)
def l150_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + -2.0*x[134] + x[166] + -1.0)
def l150_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + -2.0*x[135] + x[167] + -1.0)
def l150_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + -2.0*x[136] + x[168] + -1.0)
def l150_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + -2.0*x[137] + x[169] + -1.0)
def l150_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + -2.0*x[138] + x[170] + -1.0)
def l150_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + -2.0*x[139] + x[171] + -1.0)
def l150_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + -2.0*x[140] + x[172] + -1.0)
def l150_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + -2.0*x[141] + x[173] + -1.0)
def l150_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + -2.0*x[142] + x[174] + -1.0)
def l150_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + -2.0*x[143] + x[175] + -1.0)
def l150_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[112] + -2.0*x[144] + x[176] + -1.0)
def l150_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[113] + -2.0*x[145] + x[177] + -1.0)
def l150_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[114] + -2.0*x[146] + x[178] + -1.0)
def l150_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[115] + -2.0*x[147] + x[179] + -1.0)
def l150_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[116] + -2.0*x[148] + x[180] + -1.0)
def l150_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[117] + -2.0*x[149] + x[181] + -1.0)
def l150_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[118] + -2.0*x[150] + x[182] + -1.0)
def l150_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[119] + -2.0*x[151] + x[183] + -1.0)
def l150_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[120] + -2.0*x[152] + x[184] + -1.0)
def l150_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[121] + -2.0*x[153] + x[185] + -1.0)
def l150_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[122] + -2.0*x[154] + x[186] + -1.0)
def l150_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[123] + -2.0*x[155] + x[187] + -1.0)
def l150_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[124] + -2.0*x[156] + x[188] + -1.0)
def l150_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[125] + -2.0*x[157] + x[189] + -1.0)
def l150_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[126] + -2.0*x[158] + x[190] + -1.0)
def l150_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[127] + -2.0*x[159] + x[191] + -1.0)
def l150_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l150_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l150_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l150_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l150_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l150_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l150_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l150_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l150_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l150_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l150_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l150_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l150_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l150_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l150_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l150_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l150_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l150_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l150_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l150_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l150_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l150_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l150_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l150_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l150_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l150_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l150_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l150_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l150_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l150_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l150_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l150_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l150_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l150_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l150_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l150_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l150_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l150_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l150_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l150_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l150_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l150_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l150_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l150_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l150_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l150_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l150_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l150_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l150_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l150_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l150_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l150_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l150_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l150_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l150_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l150_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l150_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l150_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l150_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l150_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l150_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l150_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l150_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l150_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l150_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l150_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l150_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l150_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l150_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l150_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l150_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l150_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l150_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l150_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l150_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l150_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l150_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l150_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l150_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l150_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l150_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l150_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l150_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l150_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l150_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l150_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l150_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l150_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l150_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l150_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l150_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l150_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l150_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l150_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l150_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l150_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l150_(x):
    # x is a list (or vector) of length 288
    return [
        l150_0(x),
        l150_1(x),
        l150_2(x),
        l150_3(x),
        l150_4(x),
        l150_5(x),
        l150_6(x),
        l150_7(x),
        l150_8(x),
        l150_9(x),
        l150_10(x),
        l150_11(x),
        l150_12(x),
        l150_13(x),
        l150_14(x),
        l150_15(x),
        l150_16(x),
        l150_17(x),
        l150_18(x),
        l150_19(x),
        l150_20(x),
        l150_21(x),
        l150_22(x),
        l150_23(x),
        l150_24(x),
        l150_25(x),
        l150_26(x),
        l150_27(x),
        l150_28(x),
        l150_29(x),
        l150_30(x),
        l150_31(x),
        l150_32(x),
        l150_33(x),
        l150_34(x),
        l150_35(x),
        l150_36(x),
        l150_37(x),
        l150_38(x),
        l150_39(x),
        l150_40(x),
        l150_41(x),
        l150_42(x),
        l150_43(x),
        l150_44(x),
        l150_45(x),
        l150_46(x),
        l150_47(x),
        l150_48(x),
        l150_49(x),
        l150_50(x),
        l150_51(x),
        l150_52(x),
        l150_53(x),
        l150_54(x),
        l150_55(x),
        l150_56(x),
        l150_57(x),
        l150_58(x),
        l150_59(x),
        l150_60(x),
        l150_61(x),
        l150_62(x),
        l150_63(x),
        l150_64(x),
        l150_65(x),
        l150_66(x),
        l150_67(x),
        l150_68(x),
        l150_69(x),
        l150_70(x),
        l150_71(x),
        l150_72(x),
        l150_73(x),
        l150_74(x),
        l150_75(x),
        l150_76(x),
        l150_77(x),
        l150_78(x),
        l150_79(x),
        l150_80(x),
        l150_81(x),
        l150_82(x),
        l150_83(x),
        l150_84(x),
        l150_85(x),
        l150_86(x),
        l150_87(x),
        l150_88(x),
        l150_89(x),
        l150_90(x),
        l150_91(x),
        l150_92(x),
        l150_93(x),
        l150_94(x),
        l150_95(x),
        l150_96(x),
        l150_97(x),
        l150_98(x),
        l150_99(x),
        l150_100(x),
        l150_101(x),
        l150_102(x),
        l150_103(x),
        l150_104(x),
        l150_105(x),
        l150_106(x),
        l150_107(x),
        l150_108(x),
        l150_109(x),
        l150_110(x),
        l150_111(x),
        l150_112(x),
        l150_113(x),
        l150_114(x),
        l150_115(x),
        l150_116(x),
        l150_117(x),
        l150_118(x),
        l150_119(x),
        l150_120(x),
        l150_121(x),
        l150_122(x),
        l150_123(x),
        l150_124(x),
        l150_125(x),
        l150_126(x),
        l150_127(x),
        l150_128(x),
        l150_129(x),
        l150_130(x),
        l150_131(x),
        l150_132(x),
        l150_133(x),
        l150_134(x),
        l150_135(x),
        l150_136(x),
        l150_137(x),
        l150_138(x),
        l150_139(x),
        l150_140(x),
        l150_141(x),
        l150_142(x),
        l150_143(x),
        l150_144(x),
        l150_145(x),
        l150_146(x),
        l150_147(x),
        l150_148(x),
        l150_149(x),
        l150_150(x),
        l150_151(x),
        l150_152(x),
        l150_153(x),
        l150_154(x),
        l150_155(x),
        l150_156(x),
        l150_157(x),
        l150_158(x),
        l150_159(x),
        l150_160(x),
        l150_161(x),
        l150_162(x),
        l150_163(x),
        l150_164(x),
        l150_165(x),
        l150_166(x),
        l150_167(x),
        l150_168(x),
        l150_169(x),
        l150_170(x),
        l150_171(x),
        l150_172(x),
        l150_173(x),
        l150_174(x),
        l150_175(x),
        l150_176(x),
        l150_177(x),
        l150_178(x),
        l150_179(x),
        l150_180(x),
        l150_181(x),
        l150_182(x),
        l150_183(x),
        l150_184(x),
        l150_185(x),
        l150_186(x),
        l150_187(x),
        l150_188(x),
        l150_189(x),
        l150_190(x),
        l150_191(x),
        l150_192(x),
        l150_193(x),
        l150_194(x),
        l150_195(x),
        l150_196(x),
        l150_197(x),
        l150_198(x),
        l150_199(x),
        l150_200(x),
        l150_201(x),
        l150_202(x),
        l150_203(x),
        l150_204(x),
        l150_205(x),
        l150_206(x),
        l150_207(x),
        l150_208(x),
        l150_209(x),
        l150_210(x),
        l150_211(x),
        l150_212(x),
        l150_213(x),
        l150_214(x),
        l150_215(x),
        l150_216(x),
        l150_217(x),
        l150_218(x),
        l150_219(x),
        l150_220(x),
        l150_221(x),
        l150_222(x),
        l150_223(x),
        l150_224(x),
        l150_225(x),
        l150_226(x),
        l150_227(x),
        l150_228(x),
        l150_229(x),
        l150_230(x),
        l150_231(x),
        l150_232(x),
        l150_233(x),
        l150_234(x),
        l150_235(x),
        l150_236(x),
        l150_237(x),
        l150_238(x),
        l150_239(x),
        l150_240(x),
        l150_241(x),
        l150_242(x),
        l150_243(x),
        l150_244(x),
        l150_245(x),
        l150_246(x),
        l150_247(x),
        l150_248(x),
        l150_249(x),
        l150_250(x),
        l150_251(x),
        l150_252(x),
        l150_253(x),
        l150_254(x),
        l150_255(x),
        l150_256(x),
        l150_257(x),
        l150_258(x),
        l150_259(x),
        l150_260(x),
        l150_261(x),
        l150_262(x),
        l150_263(x),
        l150_264(x),
        l150_265(x),
        l150_266(x),
        l150_267(x),
        l150_268(x),
        l150_269(x),
        l150_270(x),
        l150_271(x),
        l150_272(x),
        l150_273(x),
        l150_274(x),
        l150_275(x),
        l150_276(x),
        l150_277(x),
        l150_278(x),
        l150_279(x),
        l150_280(x),
        l150_281(x),
        l150_282(x),
        l150_283(x),
        l150_284(x),
        l150_285(x),
        l150_286(x),
        l150_287(x),
    ]