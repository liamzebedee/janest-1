import numpy as np




# Generated from reverse engineering
def l486_g(x: np.ndarray) -> np.ndarray:
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




def l486_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l486_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l486_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l486_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l486_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l486_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l486_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l486_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l486_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l486_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l486_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l486_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l486_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l486_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l486_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l486_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l486_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l486_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l486_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l486_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l486_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l486_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l486_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l486_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l486_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l486_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l486_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l486_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l486_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l486_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l486_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l486_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l486_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l486_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l486_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l486_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l486_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l486_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l486_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l486_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l486_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l486_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l486_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l486_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l486_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l486_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l486_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l486_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l486_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l486_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l486_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l486_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l486_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l486_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l486_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l486_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l486_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l486_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l486_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l486_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l486_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l486_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l486_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l486_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l486_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l486_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l486_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l486_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l486_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l486_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l486_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l486_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l486_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l486_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l486_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l486_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l486_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l486_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l486_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l486_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l486_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l486_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l486_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l486_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l486_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l486_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l486_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l486_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l486_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l486_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l486_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l486_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l486_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l486_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l486_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l486_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l486_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + -2.0*x[128] + x[160] + -1.0)
def l486_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + -2.0*x[129] + x[161] + -1.0)
def l486_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + -2.0*x[130] + x[162] + -1.0)
def l486_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + -2.0*x[131] + x[163] + -1.0)
def l486_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + -2.0*x[132] + x[164] + -1.0)
def l486_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + -2.0*x[133] + x[165] + -1.0)
def l486_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + -2.0*x[134] + x[166] + -1.0)
def l486_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + -2.0*x[135] + x[167] + -1.0)
def l486_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + -2.0*x[136] + x[168] + -1.0)
def l486_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + -2.0*x[137] + x[169] + -1.0)
def l486_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + -2.0*x[138] + x[170] + -1.0)
def l486_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + -2.0*x[139] + x[171] + -1.0)
def l486_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + -2.0*x[140] + x[172] + -1.0)
def l486_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + -2.0*x[141] + x[173] + -1.0)
def l486_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + -2.0*x[142] + x[174] + -1.0)
def l486_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + -2.0*x[143] + x[175] + -1.0)
def l486_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[112] + -2.0*x[144] + x[176] + -1.0)
def l486_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[113] + -2.0*x[145] + x[177] + -1.0)
def l486_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[114] + -2.0*x[146] + x[178] + -1.0)
def l486_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[115] + -2.0*x[147] + x[179] + -1.0)
def l486_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[116] + -2.0*x[148] + x[180] + -1.0)
def l486_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[117] + -2.0*x[149] + x[181] + -1.0)
def l486_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[118] + -2.0*x[150] + x[182] + -1.0)
def l486_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[119] + -2.0*x[151] + x[183] + -1.0)
def l486_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[120] + -2.0*x[152] + x[184] + -1.0)
def l486_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[121] + -2.0*x[153] + x[185] + -1.0)
def l486_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[122] + -2.0*x[154] + x[186] + -1.0)
def l486_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[123] + -2.0*x[155] + x[187] + -1.0)
def l486_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[124] + -2.0*x[156] + x[188] + -1.0)
def l486_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[125] + -2.0*x[157] + x[189] + -1.0)
def l486_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[126] + -2.0*x[158] + x[190] + -1.0)
def l486_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[127] + -2.0*x[159] + x[191] + -1.0)
def l486_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + -2.0*x[128] + x[160])
def l486_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + -2.0*x[129] + x[161])
def l486_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + -2.0*x[130] + x[162])
def l486_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + -2.0*x[131] + x[163])
def l486_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + -2.0*x[132] + x[164])
def l486_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + -2.0*x[133] + x[165])
def l486_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + -2.0*x[134] + x[166])
def l486_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + -2.0*x[135] + x[167])
def l486_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + -2.0*x[136] + x[168])
def l486_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + -2.0*x[137] + x[169])
def l486_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + -2.0*x[138] + x[170])
def l486_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + -2.0*x[139] + x[171])
def l486_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + -2.0*x[140] + x[172])
def l486_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + -2.0*x[141] + x[173])
def l486_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + -2.0*x[142] + x[174])
def l486_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + -2.0*x[143] + x[175])
def l486_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[112] + -2.0*x[144] + x[176])
def l486_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[113] + -2.0*x[145] + x[177])
def l486_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[114] + -2.0*x[146] + x[178])
def l486_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[115] + -2.0*x[147] + x[179])
def l486_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[116] + -2.0*x[148] + x[180])
def l486_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[117] + -2.0*x[149] + x[181])
def l486_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[118] + -2.0*x[150] + x[182])
def l486_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[119] + -2.0*x[151] + x[183])
def l486_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[120] + -2.0*x[152] + x[184])
def l486_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[121] + -2.0*x[153] + x[185])
def l486_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[122] + -2.0*x[154] + x[186])
def l486_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[123] + -2.0*x[155] + x[187])
def l486_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[124] + -2.0*x[156] + x[188])
def l486_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[125] + -2.0*x[157] + x[189])
def l486_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[126] + -2.0*x[158] + x[190])
def l486_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[127] + -2.0*x[159] + x[191])
def l486_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + -2.0*x[128] + x[160] + -1.0)
def l486_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + -2.0*x[129] + x[161] + -1.0)
def l486_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + -2.0*x[130] + x[162] + -1.0)
def l486_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + -2.0*x[131] + x[163] + -1.0)
def l486_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + -2.0*x[132] + x[164] + -1.0)
def l486_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + -2.0*x[133] + x[165] + -1.0)
def l486_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + -2.0*x[134] + x[166] + -1.0)
def l486_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + -2.0*x[135] + x[167] + -1.0)
def l486_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + -2.0*x[136] + x[168] + -1.0)
def l486_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + -2.0*x[137] + x[169] + -1.0)
def l486_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + -2.0*x[138] + x[170] + -1.0)
def l486_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + -2.0*x[139] + x[171] + -1.0)
def l486_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + -2.0*x[140] + x[172] + -1.0)
def l486_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + -2.0*x[141] + x[173] + -1.0)
def l486_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + -2.0*x[142] + x[174] + -1.0)
def l486_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + -2.0*x[143] + x[175] + -1.0)
def l486_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[112] + -2.0*x[144] + x[176] + -1.0)
def l486_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[113] + -2.0*x[145] + x[177] + -1.0)
def l486_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[114] + -2.0*x[146] + x[178] + -1.0)
def l486_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[115] + -2.0*x[147] + x[179] + -1.0)
def l486_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[116] + -2.0*x[148] + x[180] + -1.0)
def l486_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[117] + -2.0*x[149] + x[181] + -1.0)
def l486_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[118] + -2.0*x[150] + x[182] + -1.0)
def l486_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[119] + -2.0*x[151] + x[183] + -1.0)
def l486_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[120] + -2.0*x[152] + x[184] + -1.0)
def l486_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[121] + -2.0*x[153] + x[185] + -1.0)
def l486_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[122] + -2.0*x[154] + x[186] + -1.0)
def l486_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[123] + -2.0*x[155] + x[187] + -1.0)
def l486_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[124] + -2.0*x[156] + x[188] + -1.0)
def l486_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[125] + -2.0*x[157] + x[189] + -1.0)
def l486_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[126] + -2.0*x[158] + x[190] + -1.0)
def l486_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[127] + -2.0*x[159] + x[191] + -1.0)
def l486_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l486_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l486_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l486_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l486_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l486_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l486_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l486_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l486_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l486_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l486_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l486_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l486_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l486_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l486_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l486_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l486_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l486_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l486_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l486_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l486_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l486_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l486_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l486_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l486_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l486_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l486_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l486_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l486_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l486_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l486_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l486_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l486_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l486_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l486_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l486_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l486_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l486_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l486_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l486_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l486_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l486_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l486_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l486_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l486_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l486_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l486_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l486_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l486_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l486_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l486_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l486_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l486_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l486_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l486_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l486_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l486_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l486_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l486_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l486_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l486_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l486_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l486_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l486_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l486_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l486_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l486_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l486_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l486_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l486_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l486_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l486_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l486_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l486_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l486_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l486_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l486_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l486_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l486_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l486_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l486_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l486_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l486_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l486_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l486_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l486_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l486_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l486_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l486_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l486_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l486_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l486_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l486_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l486_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l486_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l486_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l486_(x):
    # x is a list (or vector) of length 288
    return [
        l486_0(x),
        l486_1(x),
        l486_2(x),
        l486_3(x),
        l486_4(x),
        l486_5(x),
        l486_6(x),
        l486_7(x),
        l486_8(x),
        l486_9(x),
        l486_10(x),
        l486_11(x),
        l486_12(x),
        l486_13(x),
        l486_14(x),
        l486_15(x),
        l486_16(x),
        l486_17(x),
        l486_18(x),
        l486_19(x),
        l486_20(x),
        l486_21(x),
        l486_22(x),
        l486_23(x),
        l486_24(x),
        l486_25(x),
        l486_26(x),
        l486_27(x),
        l486_28(x),
        l486_29(x),
        l486_30(x),
        l486_31(x),
        l486_32(x),
        l486_33(x),
        l486_34(x),
        l486_35(x),
        l486_36(x),
        l486_37(x),
        l486_38(x),
        l486_39(x),
        l486_40(x),
        l486_41(x),
        l486_42(x),
        l486_43(x),
        l486_44(x),
        l486_45(x),
        l486_46(x),
        l486_47(x),
        l486_48(x),
        l486_49(x),
        l486_50(x),
        l486_51(x),
        l486_52(x),
        l486_53(x),
        l486_54(x),
        l486_55(x),
        l486_56(x),
        l486_57(x),
        l486_58(x),
        l486_59(x),
        l486_60(x),
        l486_61(x),
        l486_62(x),
        l486_63(x),
        l486_64(x),
        l486_65(x),
        l486_66(x),
        l486_67(x),
        l486_68(x),
        l486_69(x),
        l486_70(x),
        l486_71(x),
        l486_72(x),
        l486_73(x),
        l486_74(x),
        l486_75(x),
        l486_76(x),
        l486_77(x),
        l486_78(x),
        l486_79(x),
        l486_80(x),
        l486_81(x),
        l486_82(x),
        l486_83(x),
        l486_84(x),
        l486_85(x),
        l486_86(x),
        l486_87(x),
        l486_88(x),
        l486_89(x),
        l486_90(x),
        l486_91(x),
        l486_92(x),
        l486_93(x),
        l486_94(x),
        l486_95(x),
        l486_96(x),
        l486_97(x),
        l486_98(x),
        l486_99(x),
        l486_100(x),
        l486_101(x),
        l486_102(x),
        l486_103(x),
        l486_104(x),
        l486_105(x),
        l486_106(x),
        l486_107(x),
        l486_108(x),
        l486_109(x),
        l486_110(x),
        l486_111(x),
        l486_112(x),
        l486_113(x),
        l486_114(x),
        l486_115(x),
        l486_116(x),
        l486_117(x),
        l486_118(x),
        l486_119(x),
        l486_120(x),
        l486_121(x),
        l486_122(x),
        l486_123(x),
        l486_124(x),
        l486_125(x),
        l486_126(x),
        l486_127(x),
        l486_128(x),
        l486_129(x),
        l486_130(x),
        l486_131(x),
        l486_132(x),
        l486_133(x),
        l486_134(x),
        l486_135(x),
        l486_136(x),
        l486_137(x),
        l486_138(x),
        l486_139(x),
        l486_140(x),
        l486_141(x),
        l486_142(x),
        l486_143(x),
        l486_144(x),
        l486_145(x),
        l486_146(x),
        l486_147(x),
        l486_148(x),
        l486_149(x),
        l486_150(x),
        l486_151(x),
        l486_152(x),
        l486_153(x),
        l486_154(x),
        l486_155(x),
        l486_156(x),
        l486_157(x),
        l486_158(x),
        l486_159(x),
        l486_160(x),
        l486_161(x),
        l486_162(x),
        l486_163(x),
        l486_164(x),
        l486_165(x),
        l486_166(x),
        l486_167(x),
        l486_168(x),
        l486_169(x),
        l486_170(x),
        l486_171(x),
        l486_172(x),
        l486_173(x),
        l486_174(x),
        l486_175(x),
        l486_176(x),
        l486_177(x),
        l486_178(x),
        l486_179(x),
        l486_180(x),
        l486_181(x),
        l486_182(x),
        l486_183(x),
        l486_184(x),
        l486_185(x),
        l486_186(x),
        l486_187(x),
        l486_188(x),
        l486_189(x),
        l486_190(x),
        l486_191(x),
        l486_192(x),
        l486_193(x),
        l486_194(x),
        l486_195(x),
        l486_196(x),
        l486_197(x),
        l486_198(x),
        l486_199(x),
        l486_200(x),
        l486_201(x),
        l486_202(x),
        l486_203(x),
        l486_204(x),
        l486_205(x),
        l486_206(x),
        l486_207(x),
        l486_208(x),
        l486_209(x),
        l486_210(x),
        l486_211(x),
        l486_212(x),
        l486_213(x),
        l486_214(x),
        l486_215(x),
        l486_216(x),
        l486_217(x),
        l486_218(x),
        l486_219(x),
        l486_220(x),
        l486_221(x),
        l486_222(x),
        l486_223(x),
        l486_224(x),
        l486_225(x),
        l486_226(x),
        l486_227(x),
        l486_228(x),
        l486_229(x),
        l486_230(x),
        l486_231(x),
        l486_232(x),
        l486_233(x),
        l486_234(x),
        l486_235(x),
        l486_236(x),
        l486_237(x),
        l486_238(x),
        l486_239(x),
        l486_240(x),
        l486_241(x),
        l486_242(x),
        l486_243(x),
        l486_244(x),
        l486_245(x),
        l486_246(x),
        l486_247(x),
        l486_248(x),
        l486_249(x),
        l486_250(x),
        l486_251(x),
        l486_252(x),
        l486_253(x),
        l486_254(x),
        l486_255(x),
        l486_256(x),
        l486_257(x),
        l486_258(x),
        l486_259(x),
        l486_260(x),
        l486_261(x),
        l486_262(x),
        l486_263(x),
        l486_264(x),
        l486_265(x),
        l486_266(x),
        l486_267(x),
        l486_268(x),
        l486_269(x),
        l486_270(x),
        l486_271(x),
        l486_272(x),
        l486_273(x),
        l486_274(x),
        l486_275(x),
        l486_276(x),
        l486_277(x),
        l486_278(x),
        l486_279(x),
        l486_280(x),
        l486_281(x),
        l486_282(x),
        l486_283(x),
        l486_284(x),
        l486_285(x),
        l486_286(x),
        l486_287(x),
    ]