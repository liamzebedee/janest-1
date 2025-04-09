import numpy as np




# Generated from reverse engineering
def l66_g(x: np.ndarray) -> np.ndarray:
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




def l66_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l66_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l66_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l66_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l66_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l66_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l66_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l66_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l66_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l66_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l66_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l66_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l66_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l66_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l66_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l66_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l66_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l66_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l66_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l66_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l66_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l66_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l66_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l66_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l66_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l66_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l66_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l66_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l66_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l66_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l66_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l66_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l66_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l66_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l66_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l66_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l66_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l66_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l66_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l66_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l66_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l66_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l66_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l66_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l66_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l66_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l66_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l66_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l66_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l66_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l66_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l66_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l66_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l66_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l66_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l66_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l66_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l66_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l66_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l66_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l66_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l66_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l66_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l66_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l66_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l66_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l66_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l66_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l66_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l66_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l66_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l66_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l66_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l66_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l66_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l66_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l66_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l66_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l66_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l66_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l66_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l66_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l66_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l66_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l66_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l66_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l66_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l66_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l66_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l66_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l66_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l66_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l66_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l66_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l66_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l66_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l66_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + -2.0*x[128] + x[160] + -1.0)
def l66_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + -2.0*x[129] + x[161] + -1.0)
def l66_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + -2.0*x[130] + x[162] + -1.0)
def l66_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + -2.0*x[131] + x[163] + -1.0)
def l66_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + -2.0*x[132] + x[164] + -1.0)
def l66_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + -2.0*x[133] + x[165] + -1.0)
def l66_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + -2.0*x[134] + x[166] + -1.0)
def l66_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + -2.0*x[135] + x[167] + -1.0)
def l66_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + -2.0*x[136] + x[168] + -1.0)
def l66_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + -2.0*x[137] + x[169] + -1.0)
def l66_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + -2.0*x[138] + x[170] + -1.0)
def l66_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + -2.0*x[139] + x[171] + -1.0)
def l66_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + -2.0*x[140] + x[172] + -1.0)
def l66_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + -2.0*x[141] + x[173] + -1.0)
def l66_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + -2.0*x[142] + x[174] + -1.0)
def l66_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + -2.0*x[143] + x[175] + -1.0)
def l66_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[112] + -2.0*x[144] + x[176] + -1.0)
def l66_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[113] + -2.0*x[145] + x[177] + -1.0)
def l66_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[114] + -2.0*x[146] + x[178] + -1.0)
def l66_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[115] + -2.0*x[147] + x[179] + -1.0)
def l66_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[116] + -2.0*x[148] + x[180] + -1.0)
def l66_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[117] + -2.0*x[149] + x[181] + -1.0)
def l66_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[118] + -2.0*x[150] + x[182] + -1.0)
def l66_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[119] + -2.0*x[151] + x[183] + -1.0)
def l66_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[120] + -2.0*x[152] + x[184] + -1.0)
def l66_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[121] + -2.0*x[153] + x[185] + -1.0)
def l66_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[122] + -2.0*x[154] + x[186] + -1.0)
def l66_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[123] + -2.0*x[155] + x[187] + -1.0)
def l66_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[124] + -2.0*x[156] + x[188] + -1.0)
def l66_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[125] + -2.0*x[157] + x[189] + -1.0)
def l66_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[126] + -2.0*x[158] + x[190] + -1.0)
def l66_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[127] + -2.0*x[159] + x[191] + -1.0)
def l66_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + -2.0*x[128] + x[160])
def l66_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + -2.0*x[129] + x[161])
def l66_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + -2.0*x[130] + x[162])
def l66_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + -2.0*x[131] + x[163])
def l66_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + -2.0*x[132] + x[164])
def l66_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + -2.0*x[133] + x[165])
def l66_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + -2.0*x[134] + x[166])
def l66_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + -2.0*x[135] + x[167])
def l66_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + -2.0*x[136] + x[168])
def l66_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + -2.0*x[137] + x[169])
def l66_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + -2.0*x[138] + x[170])
def l66_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + -2.0*x[139] + x[171])
def l66_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + -2.0*x[140] + x[172])
def l66_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + -2.0*x[141] + x[173])
def l66_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + -2.0*x[142] + x[174])
def l66_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + -2.0*x[143] + x[175])
def l66_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[112] + -2.0*x[144] + x[176])
def l66_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[113] + -2.0*x[145] + x[177])
def l66_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[114] + -2.0*x[146] + x[178])
def l66_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[115] + -2.0*x[147] + x[179])
def l66_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[116] + -2.0*x[148] + x[180])
def l66_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[117] + -2.0*x[149] + x[181])
def l66_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[118] + -2.0*x[150] + x[182])
def l66_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[119] + -2.0*x[151] + x[183])
def l66_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[120] + -2.0*x[152] + x[184])
def l66_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[121] + -2.0*x[153] + x[185])
def l66_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[122] + -2.0*x[154] + x[186])
def l66_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[123] + -2.0*x[155] + x[187])
def l66_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[124] + -2.0*x[156] + x[188])
def l66_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[125] + -2.0*x[157] + x[189])
def l66_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[126] + -2.0*x[158] + x[190])
def l66_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[127] + -2.0*x[159] + x[191])
def l66_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + -2.0*x[128] + x[160] + -1.0)
def l66_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + -2.0*x[129] + x[161] + -1.0)
def l66_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + -2.0*x[130] + x[162] + -1.0)
def l66_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + -2.0*x[131] + x[163] + -1.0)
def l66_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + -2.0*x[132] + x[164] + -1.0)
def l66_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + -2.0*x[133] + x[165] + -1.0)
def l66_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + -2.0*x[134] + x[166] + -1.0)
def l66_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + -2.0*x[135] + x[167] + -1.0)
def l66_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + -2.0*x[136] + x[168] + -1.0)
def l66_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + -2.0*x[137] + x[169] + -1.0)
def l66_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + -2.0*x[138] + x[170] + -1.0)
def l66_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + -2.0*x[139] + x[171] + -1.0)
def l66_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + -2.0*x[140] + x[172] + -1.0)
def l66_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + -2.0*x[141] + x[173] + -1.0)
def l66_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + -2.0*x[142] + x[174] + -1.0)
def l66_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + -2.0*x[143] + x[175] + -1.0)
def l66_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[112] + -2.0*x[144] + x[176] + -1.0)
def l66_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[113] + -2.0*x[145] + x[177] + -1.0)
def l66_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[114] + -2.0*x[146] + x[178] + -1.0)
def l66_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[115] + -2.0*x[147] + x[179] + -1.0)
def l66_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[116] + -2.0*x[148] + x[180] + -1.0)
def l66_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[117] + -2.0*x[149] + x[181] + -1.0)
def l66_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[118] + -2.0*x[150] + x[182] + -1.0)
def l66_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[119] + -2.0*x[151] + x[183] + -1.0)
def l66_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[120] + -2.0*x[152] + x[184] + -1.0)
def l66_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[121] + -2.0*x[153] + x[185] + -1.0)
def l66_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[122] + -2.0*x[154] + x[186] + -1.0)
def l66_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[123] + -2.0*x[155] + x[187] + -1.0)
def l66_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[124] + -2.0*x[156] + x[188] + -1.0)
def l66_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[125] + -2.0*x[157] + x[189] + -1.0)
def l66_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[126] + -2.0*x[158] + x[190] + -1.0)
def l66_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[127] + -2.0*x[159] + x[191] + -1.0)
def l66_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l66_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l66_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l66_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l66_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l66_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l66_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l66_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l66_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l66_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l66_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l66_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l66_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l66_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l66_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l66_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l66_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l66_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l66_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l66_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l66_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l66_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l66_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l66_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l66_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l66_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l66_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l66_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l66_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l66_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l66_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l66_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l66_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l66_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l66_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l66_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l66_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l66_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l66_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l66_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l66_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l66_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l66_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l66_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l66_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l66_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l66_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l66_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l66_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l66_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l66_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l66_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l66_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l66_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l66_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l66_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l66_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l66_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l66_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l66_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l66_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l66_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l66_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l66_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l66_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l66_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l66_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l66_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l66_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l66_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l66_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l66_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l66_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l66_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l66_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l66_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l66_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l66_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l66_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l66_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l66_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l66_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l66_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l66_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l66_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l66_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l66_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l66_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l66_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l66_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l66_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l66_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l66_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l66_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l66_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l66_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l66_(x):
    # x is a list (or vector) of length 288
    return [
        l66_0(x),
        l66_1(x),
        l66_2(x),
        l66_3(x),
        l66_4(x),
        l66_5(x),
        l66_6(x),
        l66_7(x),
        l66_8(x),
        l66_9(x),
        l66_10(x),
        l66_11(x),
        l66_12(x),
        l66_13(x),
        l66_14(x),
        l66_15(x),
        l66_16(x),
        l66_17(x),
        l66_18(x),
        l66_19(x),
        l66_20(x),
        l66_21(x),
        l66_22(x),
        l66_23(x),
        l66_24(x),
        l66_25(x),
        l66_26(x),
        l66_27(x),
        l66_28(x),
        l66_29(x),
        l66_30(x),
        l66_31(x),
        l66_32(x),
        l66_33(x),
        l66_34(x),
        l66_35(x),
        l66_36(x),
        l66_37(x),
        l66_38(x),
        l66_39(x),
        l66_40(x),
        l66_41(x),
        l66_42(x),
        l66_43(x),
        l66_44(x),
        l66_45(x),
        l66_46(x),
        l66_47(x),
        l66_48(x),
        l66_49(x),
        l66_50(x),
        l66_51(x),
        l66_52(x),
        l66_53(x),
        l66_54(x),
        l66_55(x),
        l66_56(x),
        l66_57(x),
        l66_58(x),
        l66_59(x),
        l66_60(x),
        l66_61(x),
        l66_62(x),
        l66_63(x),
        l66_64(x),
        l66_65(x),
        l66_66(x),
        l66_67(x),
        l66_68(x),
        l66_69(x),
        l66_70(x),
        l66_71(x),
        l66_72(x),
        l66_73(x),
        l66_74(x),
        l66_75(x),
        l66_76(x),
        l66_77(x),
        l66_78(x),
        l66_79(x),
        l66_80(x),
        l66_81(x),
        l66_82(x),
        l66_83(x),
        l66_84(x),
        l66_85(x),
        l66_86(x),
        l66_87(x),
        l66_88(x),
        l66_89(x),
        l66_90(x),
        l66_91(x),
        l66_92(x),
        l66_93(x),
        l66_94(x),
        l66_95(x),
        l66_96(x),
        l66_97(x),
        l66_98(x),
        l66_99(x),
        l66_100(x),
        l66_101(x),
        l66_102(x),
        l66_103(x),
        l66_104(x),
        l66_105(x),
        l66_106(x),
        l66_107(x),
        l66_108(x),
        l66_109(x),
        l66_110(x),
        l66_111(x),
        l66_112(x),
        l66_113(x),
        l66_114(x),
        l66_115(x),
        l66_116(x),
        l66_117(x),
        l66_118(x),
        l66_119(x),
        l66_120(x),
        l66_121(x),
        l66_122(x),
        l66_123(x),
        l66_124(x),
        l66_125(x),
        l66_126(x),
        l66_127(x),
        l66_128(x),
        l66_129(x),
        l66_130(x),
        l66_131(x),
        l66_132(x),
        l66_133(x),
        l66_134(x),
        l66_135(x),
        l66_136(x),
        l66_137(x),
        l66_138(x),
        l66_139(x),
        l66_140(x),
        l66_141(x),
        l66_142(x),
        l66_143(x),
        l66_144(x),
        l66_145(x),
        l66_146(x),
        l66_147(x),
        l66_148(x),
        l66_149(x),
        l66_150(x),
        l66_151(x),
        l66_152(x),
        l66_153(x),
        l66_154(x),
        l66_155(x),
        l66_156(x),
        l66_157(x),
        l66_158(x),
        l66_159(x),
        l66_160(x),
        l66_161(x),
        l66_162(x),
        l66_163(x),
        l66_164(x),
        l66_165(x),
        l66_166(x),
        l66_167(x),
        l66_168(x),
        l66_169(x),
        l66_170(x),
        l66_171(x),
        l66_172(x),
        l66_173(x),
        l66_174(x),
        l66_175(x),
        l66_176(x),
        l66_177(x),
        l66_178(x),
        l66_179(x),
        l66_180(x),
        l66_181(x),
        l66_182(x),
        l66_183(x),
        l66_184(x),
        l66_185(x),
        l66_186(x),
        l66_187(x),
        l66_188(x),
        l66_189(x),
        l66_190(x),
        l66_191(x),
        l66_192(x),
        l66_193(x),
        l66_194(x),
        l66_195(x),
        l66_196(x),
        l66_197(x),
        l66_198(x),
        l66_199(x),
        l66_200(x),
        l66_201(x),
        l66_202(x),
        l66_203(x),
        l66_204(x),
        l66_205(x),
        l66_206(x),
        l66_207(x),
        l66_208(x),
        l66_209(x),
        l66_210(x),
        l66_211(x),
        l66_212(x),
        l66_213(x),
        l66_214(x),
        l66_215(x),
        l66_216(x),
        l66_217(x),
        l66_218(x),
        l66_219(x),
        l66_220(x),
        l66_221(x),
        l66_222(x),
        l66_223(x),
        l66_224(x),
        l66_225(x),
        l66_226(x),
        l66_227(x),
        l66_228(x),
        l66_229(x),
        l66_230(x),
        l66_231(x),
        l66_232(x),
        l66_233(x),
        l66_234(x),
        l66_235(x),
        l66_236(x),
        l66_237(x),
        l66_238(x),
        l66_239(x),
        l66_240(x),
        l66_241(x),
        l66_242(x),
        l66_243(x),
        l66_244(x),
        l66_245(x),
        l66_246(x),
        l66_247(x),
        l66_248(x),
        l66_249(x),
        l66_250(x),
        l66_251(x),
        l66_252(x),
        l66_253(x),
        l66_254(x),
        l66_255(x),
        l66_256(x),
        l66_257(x),
        l66_258(x),
        l66_259(x),
        l66_260(x),
        l66_261(x),
        l66_262(x),
        l66_263(x),
        l66_264(x),
        l66_265(x),
        l66_266(x),
        l66_267(x),
        l66_268(x),
        l66_269(x),
        l66_270(x),
        l66_271(x),
        l66_272(x),
        l66_273(x),
        l66_274(x),
        l66_275(x),
        l66_276(x),
        l66_277(x),
        l66_278(x),
        l66_279(x),
        l66_280(x),
        l66_281(x),
        l66_282(x),
        l66_283(x),
        l66_284(x),
        l66_285(x),
        l66_286(x),
        l66_287(x),
    ]