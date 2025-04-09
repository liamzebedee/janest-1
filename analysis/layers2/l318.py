import numpy as np




# Generated from reverse engineering
def l318_g(x: np.ndarray) -> np.ndarray:
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




def l318_0(x):
    # x is a list (or vector) of length 288
    return max(0, x[0])
def l318_1(x):
    # x is a list (or vector) of length 288
    return max(0, x[1])
def l318_2(x):
    # x is a list (or vector) of length 288
    return max(0, x[2])
def l318_3(x):
    # x is a list (or vector) of length 288
    return max(0, x[3])
def l318_4(x):
    # x is a list (or vector) of length 288
    return max(0, x[4])
def l318_5(x):
    # x is a list (or vector) of length 288
    return max(0, x[5])
def l318_6(x):
    # x is a list (or vector) of length 288
    return max(0, x[6])
def l318_7(x):
    # x is a list (or vector) of length 288
    return max(0, x[7])
def l318_8(x):
    # x is a list (or vector) of length 288
    return max(0, x[8])
def l318_9(x):
    # x is a list (or vector) of length 288
    return max(0, x[9])
def l318_10(x):
    # x is a list (or vector) of length 288
    return max(0, x[10])
def l318_11(x):
    # x is a list (or vector) of length 288
    return max(0, x[11])
def l318_12(x):
    # x is a list (or vector) of length 288
    return max(0, x[12])
def l318_13(x):
    # x is a list (or vector) of length 288
    return max(0, x[13])
def l318_14(x):
    # x is a list (or vector) of length 288
    return max(0, x[14])
def l318_15(x):
    # x is a list (or vector) of length 288
    return max(0, x[15])
def l318_16(x):
    # x is a list (or vector) of length 288
    return max(0, x[16])
def l318_17(x):
    # x is a list (or vector) of length 288
    return max(0, x[17])
def l318_18(x):
    # x is a list (or vector) of length 288
    return max(0, x[18])
def l318_19(x):
    # x is a list (or vector) of length 288
    return max(0, x[19])
def l318_20(x):
    # x is a list (or vector) of length 288
    return max(0, x[20])
def l318_21(x):
    # x is a list (or vector) of length 288
    return max(0, x[21])
def l318_22(x):
    # x is a list (or vector) of length 288
    return max(0, x[22])
def l318_23(x):
    # x is a list (or vector) of length 288
    return max(0, x[23])
def l318_24(x):
    # x is a list (or vector) of length 288
    return max(0, x[24])
def l318_25(x):
    # x is a list (or vector) of length 288
    return max(0, x[25])
def l318_26(x):
    # x is a list (or vector) of length 288
    return max(0, x[26])
def l318_27(x):
    # x is a list (or vector) of length 288
    return max(0, x[27])
def l318_28(x):
    # x is a list (or vector) of length 288
    return max(0, x[28])
def l318_29(x):
    # x is a list (or vector) of length 288
    return max(0, x[29])
def l318_30(x):
    # x is a list (or vector) of length 288
    return max(0, x[30])
def l318_31(x):
    # x is a list (or vector) of length 288
    return max(0, x[31])
def l318_32(x):
    # x is a list (or vector) of length 288
    return max(0, x[32])
def l318_33(x):
    # x is a list (or vector) of length 288
    return max(0, x[33])
def l318_34(x):
    # x is a list (or vector) of length 288
    return max(0, x[34])
def l318_35(x):
    # x is a list (or vector) of length 288
    return max(0, x[35])
def l318_36(x):
    # x is a list (or vector) of length 288
    return max(0, x[36])
def l318_37(x):
    # x is a list (or vector) of length 288
    return max(0, x[37])
def l318_38(x):
    # x is a list (or vector) of length 288
    return max(0, x[38])
def l318_39(x):
    # x is a list (or vector) of length 288
    return max(0, x[39])
def l318_40(x):
    # x is a list (or vector) of length 288
    return max(0, x[40])
def l318_41(x):
    # x is a list (or vector) of length 288
    return max(0, x[41])
def l318_42(x):
    # x is a list (or vector) of length 288
    return max(0, x[42])
def l318_43(x):
    # x is a list (or vector) of length 288
    return max(0, x[43])
def l318_44(x):
    # x is a list (or vector) of length 288
    return max(0, x[44])
def l318_45(x):
    # x is a list (or vector) of length 288
    return max(0, x[45])
def l318_46(x):
    # x is a list (or vector) of length 288
    return max(0, x[46])
def l318_47(x):
    # x is a list (or vector) of length 288
    return max(0, x[47])
def l318_48(x):
    # x is a list (or vector) of length 288
    return max(0, x[48])
def l318_49(x):
    # x is a list (or vector) of length 288
    return max(0, x[49])
def l318_50(x):
    # x is a list (or vector) of length 288
    return max(0, x[50])
def l318_51(x):
    # x is a list (or vector) of length 288
    return max(0, x[51])
def l318_52(x):
    # x is a list (or vector) of length 288
    return max(0, x[52])
def l318_53(x):
    # x is a list (or vector) of length 288
    return max(0, x[53])
def l318_54(x):
    # x is a list (or vector) of length 288
    return max(0, x[54])
def l318_55(x):
    # x is a list (or vector) of length 288
    return max(0, x[55])
def l318_56(x):
    # x is a list (or vector) of length 288
    return max(0, x[56])
def l318_57(x):
    # x is a list (or vector) of length 288
    return max(0, x[57])
def l318_58(x):
    # x is a list (or vector) of length 288
    return max(0, x[58])
def l318_59(x):
    # x is a list (or vector) of length 288
    return max(0, x[59])
def l318_60(x):
    # x is a list (or vector) of length 288
    return max(0, x[60])
def l318_61(x):
    # x is a list (or vector) of length 288
    return max(0, x[61])
def l318_62(x):
    # x is a list (or vector) of length 288
    return max(0, x[62])
def l318_63(x):
    # x is a list (or vector) of length 288
    return max(0, x[63])
def l318_64(x):
    # x is a list (or vector) of length 288
    return max(0, x[64])
def l318_65(x):
    # x is a list (or vector) of length 288
    return max(0, x[65])
def l318_66(x):
    # x is a list (or vector) of length 288
    return max(0, x[66])
def l318_67(x):
    # x is a list (or vector) of length 288
    return max(0, x[67])
def l318_68(x):
    # x is a list (or vector) of length 288
    return max(0, x[68])
def l318_69(x):
    # x is a list (or vector) of length 288
    return max(0, x[69])
def l318_70(x):
    # x is a list (or vector) of length 288
    return max(0, x[70])
def l318_71(x):
    # x is a list (or vector) of length 288
    return max(0, x[71])
def l318_72(x):
    # x is a list (or vector) of length 288
    return max(0, x[72])
def l318_73(x):
    # x is a list (or vector) of length 288
    return max(0, x[73])
def l318_74(x):
    # x is a list (or vector) of length 288
    return max(0, x[74])
def l318_75(x):
    # x is a list (or vector) of length 288
    return max(0, x[75])
def l318_76(x):
    # x is a list (or vector) of length 288
    return max(0, x[76])
def l318_77(x):
    # x is a list (or vector) of length 288
    return max(0, x[77])
def l318_78(x):
    # x is a list (or vector) of length 288
    return max(0, x[78])
def l318_79(x):
    # x is a list (or vector) of length 288
    return max(0, x[79])
def l318_80(x):
    # x is a list (or vector) of length 288
    return max(0, x[80])
def l318_81(x):
    # x is a list (or vector) of length 288
    return max(0, x[81])
def l318_82(x):
    # x is a list (or vector) of length 288
    return max(0, x[82])
def l318_83(x):
    # x is a list (or vector) of length 288
    return max(0, x[83])
def l318_84(x):
    # x is a list (or vector) of length 288
    return max(0, x[84])
def l318_85(x):
    # x is a list (or vector) of length 288
    return max(0, x[85])
def l318_86(x):
    # x is a list (or vector) of length 288
    return max(0, x[86])
def l318_87(x):
    # x is a list (or vector) of length 288
    return max(0, x[87])
def l318_88(x):
    # x is a list (or vector) of length 288
    return max(0, x[88])
def l318_89(x):
    # x is a list (or vector) of length 288
    return max(0, x[89])
def l318_90(x):
    # x is a list (or vector) of length 288
    return max(0, x[90])
def l318_91(x):
    # x is a list (or vector) of length 288
    return max(0, x[91])
def l318_92(x):
    # x is a list (or vector) of length 288
    return max(0, x[92])
def l318_93(x):
    # x is a list (or vector) of length 288
    return max(0, x[93])
def l318_94(x):
    # x is a list (or vector) of length 288
    return max(0, x[94])
def l318_95(x):
    # x is a list (or vector) of length 288
    return max(0, x[95])
def l318_96(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + -2.0*x[128] + x[160] + -1.0)
def l318_97(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + -2.0*x[129] + x[161] + -1.0)
def l318_98(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + -2.0*x[130] + x[162] + -1.0)
def l318_99(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + -2.0*x[131] + x[163] + -1.0)
def l318_100(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + -2.0*x[132] + x[164] + -1.0)
def l318_101(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + -2.0*x[133] + x[165] + -1.0)
def l318_102(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + -2.0*x[134] + x[166] + -1.0)
def l318_103(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + -2.0*x[135] + x[167] + -1.0)
def l318_104(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + -2.0*x[136] + x[168] + -1.0)
def l318_105(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + -2.0*x[137] + x[169] + -1.0)
def l318_106(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + -2.0*x[138] + x[170] + -1.0)
def l318_107(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + -2.0*x[139] + x[171] + -1.0)
def l318_108(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + -2.0*x[140] + x[172] + -1.0)
def l318_109(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + -2.0*x[141] + x[173] + -1.0)
def l318_110(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + -2.0*x[142] + x[174] + -1.0)
def l318_111(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + -2.0*x[143] + x[175] + -1.0)
def l318_112(x):
    # x is a list (or vector) of length 288
    return max(0, x[112] + -2.0*x[144] + x[176] + -1.0)
def l318_113(x):
    # x is a list (or vector) of length 288
    return max(0, x[113] + -2.0*x[145] + x[177] + -1.0)
def l318_114(x):
    # x is a list (or vector) of length 288
    return max(0, x[114] + -2.0*x[146] + x[178] + -1.0)
def l318_115(x):
    # x is a list (or vector) of length 288
    return max(0, x[115] + -2.0*x[147] + x[179] + -1.0)
def l318_116(x):
    # x is a list (or vector) of length 288
    return max(0, x[116] + -2.0*x[148] + x[180] + -1.0)
def l318_117(x):
    # x is a list (or vector) of length 288
    return max(0, x[117] + -2.0*x[149] + x[181] + -1.0)
def l318_118(x):
    # x is a list (or vector) of length 288
    return max(0, x[118] + -2.0*x[150] + x[182] + -1.0)
def l318_119(x):
    # x is a list (or vector) of length 288
    return max(0, x[119] + -2.0*x[151] + x[183] + -1.0)
def l318_120(x):
    # x is a list (or vector) of length 288
    return max(0, x[120] + -2.0*x[152] + x[184] + -1.0)
def l318_121(x):
    # x is a list (or vector) of length 288
    return max(0, x[121] + -2.0*x[153] + x[185] + -1.0)
def l318_122(x):
    # x is a list (or vector) of length 288
    return max(0, x[122] + -2.0*x[154] + x[186] + -1.0)
def l318_123(x):
    # x is a list (or vector) of length 288
    return max(0, x[123] + -2.0*x[155] + x[187] + -1.0)
def l318_124(x):
    # x is a list (or vector) of length 288
    return max(0, x[124] + -2.0*x[156] + x[188] + -1.0)
def l318_125(x):
    # x is a list (or vector) of length 288
    return max(0, x[125] + -2.0*x[157] + x[189] + -1.0)
def l318_126(x):
    # x is a list (or vector) of length 288
    return max(0, x[126] + -2.0*x[158] + x[190] + -1.0)
def l318_127(x):
    # x is a list (or vector) of length 288
    return max(0, x[127] + -2.0*x[159] + x[191] + -1.0)
def l318_128(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + -2.0*x[128] + x[160])
def l318_129(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + -2.0*x[129] + x[161])
def l318_130(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + -2.0*x[130] + x[162])
def l318_131(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + -2.0*x[131] + x[163])
def l318_132(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + -2.0*x[132] + x[164])
def l318_133(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + -2.0*x[133] + x[165])
def l318_134(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + -2.0*x[134] + x[166])
def l318_135(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + -2.0*x[135] + x[167])
def l318_136(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + -2.0*x[136] + x[168])
def l318_137(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + -2.0*x[137] + x[169])
def l318_138(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + -2.0*x[138] + x[170])
def l318_139(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + -2.0*x[139] + x[171])
def l318_140(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + -2.0*x[140] + x[172])
def l318_141(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + -2.0*x[141] + x[173])
def l318_142(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + -2.0*x[142] + x[174])
def l318_143(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + -2.0*x[143] + x[175])
def l318_144(x):
    # x is a list (or vector) of length 288
    return max(0, x[112] + -2.0*x[144] + x[176])
def l318_145(x):
    # x is a list (or vector) of length 288
    return max(0, x[113] + -2.0*x[145] + x[177])
def l318_146(x):
    # x is a list (or vector) of length 288
    return max(0, x[114] + -2.0*x[146] + x[178])
def l318_147(x):
    # x is a list (or vector) of length 288
    return max(0, x[115] + -2.0*x[147] + x[179])
def l318_148(x):
    # x is a list (or vector) of length 288
    return max(0, x[116] + -2.0*x[148] + x[180])
def l318_149(x):
    # x is a list (or vector) of length 288
    return max(0, x[117] + -2.0*x[149] + x[181])
def l318_150(x):
    # x is a list (or vector) of length 288
    return max(0, x[118] + -2.0*x[150] + x[182])
def l318_151(x):
    # x is a list (or vector) of length 288
    return max(0, x[119] + -2.0*x[151] + x[183])
def l318_152(x):
    # x is a list (or vector) of length 288
    return max(0, x[120] + -2.0*x[152] + x[184])
def l318_153(x):
    # x is a list (or vector) of length 288
    return max(0, x[121] + -2.0*x[153] + x[185])
def l318_154(x):
    # x is a list (or vector) of length 288
    return max(0, x[122] + -2.0*x[154] + x[186])
def l318_155(x):
    # x is a list (or vector) of length 288
    return max(0, x[123] + -2.0*x[155] + x[187])
def l318_156(x):
    # x is a list (or vector) of length 288
    return max(0, x[124] + -2.0*x[156] + x[188])
def l318_157(x):
    # x is a list (or vector) of length 288
    return max(0, x[125] + -2.0*x[157] + x[189])
def l318_158(x):
    # x is a list (or vector) of length 288
    return max(0, x[126] + -2.0*x[158] + x[190])
def l318_159(x):
    # x is a list (or vector) of length 288
    return max(0, x[127] + -2.0*x[159] + x[191])
def l318_160(x):
    # x is a list (or vector) of length 288
    return max(0, x[96] + -2.0*x[128] + x[160] + -1.0)
def l318_161(x):
    # x is a list (or vector) of length 288
    return max(0, x[97] + -2.0*x[129] + x[161] + -1.0)
def l318_162(x):
    # x is a list (or vector) of length 288
    return max(0, x[98] + -2.0*x[130] + x[162] + -1.0)
def l318_163(x):
    # x is a list (or vector) of length 288
    return max(0, x[99] + -2.0*x[131] + x[163] + -1.0)
def l318_164(x):
    # x is a list (or vector) of length 288
    return max(0, x[100] + -2.0*x[132] + x[164] + -1.0)
def l318_165(x):
    # x is a list (or vector) of length 288
    return max(0, x[101] + -2.0*x[133] + x[165] + -1.0)
def l318_166(x):
    # x is a list (or vector) of length 288
    return max(0, x[102] + -2.0*x[134] + x[166] + -1.0)
def l318_167(x):
    # x is a list (or vector) of length 288
    return max(0, x[103] + -2.0*x[135] + x[167] + -1.0)
def l318_168(x):
    # x is a list (or vector) of length 288
    return max(0, x[104] + -2.0*x[136] + x[168] + -1.0)
def l318_169(x):
    # x is a list (or vector) of length 288
    return max(0, x[105] + -2.0*x[137] + x[169] + -1.0)
def l318_170(x):
    # x is a list (or vector) of length 288
    return max(0, x[106] + -2.0*x[138] + x[170] + -1.0)
def l318_171(x):
    # x is a list (or vector) of length 288
    return max(0, x[107] + -2.0*x[139] + x[171] + -1.0)
def l318_172(x):
    # x is a list (or vector) of length 288
    return max(0, x[108] + -2.0*x[140] + x[172] + -1.0)
def l318_173(x):
    # x is a list (or vector) of length 288
    return max(0, x[109] + -2.0*x[141] + x[173] + -1.0)
def l318_174(x):
    # x is a list (or vector) of length 288
    return max(0, x[110] + -2.0*x[142] + x[174] + -1.0)
def l318_175(x):
    # x is a list (or vector) of length 288
    return max(0, x[111] + -2.0*x[143] + x[175] + -1.0)
def l318_176(x):
    # x is a list (or vector) of length 288
    return max(0, x[112] + -2.0*x[144] + x[176] + -1.0)
def l318_177(x):
    # x is a list (or vector) of length 288
    return max(0, x[113] + -2.0*x[145] + x[177] + -1.0)
def l318_178(x):
    # x is a list (or vector) of length 288
    return max(0, x[114] + -2.0*x[146] + x[178] + -1.0)
def l318_179(x):
    # x is a list (or vector) of length 288
    return max(0, x[115] + -2.0*x[147] + x[179] + -1.0)
def l318_180(x):
    # x is a list (or vector) of length 288
    return max(0, x[116] + -2.0*x[148] + x[180] + -1.0)
def l318_181(x):
    # x is a list (or vector) of length 288
    return max(0, x[117] + -2.0*x[149] + x[181] + -1.0)
def l318_182(x):
    # x is a list (or vector) of length 288
    return max(0, x[118] + -2.0*x[150] + x[182] + -1.0)
def l318_183(x):
    # x is a list (or vector) of length 288
    return max(0, x[119] + -2.0*x[151] + x[183] + -1.0)
def l318_184(x):
    # x is a list (or vector) of length 288
    return max(0, x[120] + -2.0*x[152] + x[184] + -1.0)
def l318_185(x):
    # x is a list (or vector) of length 288
    return max(0, x[121] + -2.0*x[153] + x[185] + -1.0)
def l318_186(x):
    # x is a list (or vector) of length 288
    return max(0, x[122] + -2.0*x[154] + x[186] + -1.0)
def l318_187(x):
    # x is a list (or vector) of length 288
    return max(0, x[123] + -2.0*x[155] + x[187] + -1.0)
def l318_188(x):
    # x is a list (or vector) of length 288
    return max(0, x[124] + -2.0*x[156] + x[188] + -1.0)
def l318_189(x):
    # x is a list (or vector) of length 288
    return max(0, x[125] + -2.0*x[157] + x[189] + -1.0)
def l318_190(x):
    # x is a list (or vector) of length 288
    return max(0, x[126] + -2.0*x[158] + x[190] + -1.0)
def l318_191(x):
    # x is a list (or vector) of length 288
    return max(0, x[127] + -2.0*x[159] + x[191] + -1.0)
def l318_192(x):
    # x is a list (or vector) of length 288
    return max(0, x[192])
def l318_193(x):
    # x is a list (or vector) of length 288
    return max(0, x[193])
def l318_194(x):
    # x is a list (or vector) of length 288
    return max(0, x[194])
def l318_195(x):
    # x is a list (or vector) of length 288
    return max(0, x[195])
def l318_196(x):
    # x is a list (or vector) of length 288
    return max(0, x[196])
def l318_197(x):
    # x is a list (or vector) of length 288
    return max(0, x[197])
def l318_198(x):
    # x is a list (or vector) of length 288
    return max(0, x[198])
def l318_199(x):
    # x is a list (or vector) of length 288
    return max(0, x[199])
def l318_200(x):
    # x is a list (or vector) of length 288
    return max(0, x[200])
def l318_201(x):
    # x is a list (or vector) of length 288
    return max(0, x[201])
def l318_202(x):
    # x is a list (or vector) of length 288
    return max(0, x[202])
def l318_203(x):
    # x is a list (or vector) of length 288
    return max(0, x[203])
def l318_204(x):
    # x is a list (or vector) of length 288
    return max(0, x[204])
def l318_205(x):
    # x is a list (or vector) of length 288
    return max(0, x[205])
def l318_206(x):
    # x is a list (or vector) of length 288
    return max(0, x[206])
def l318_207(x):
    # x is a list (or vector) of length 288
    return max(0, x[207])
def l318_208(x):
    # x is a list (or vector) of length 288
    return max(0, x[208])
def l318_209(x):
    # x is a list (or vector) of length 288
    return max(0, x[209])
def l318_210(x):
    # x is a list (or vector) of length 288
    return max(0, x[210])
def l318_211(x):
    # x is a list (or vector) of length 288
    return max(0, x[211])
def l318_212(x):
    # x is a list (or vector) of length 288
    return max(0, x[212])
def l318_213(x):
    # x is a list (or vector) of length 288
    return max(0, x[213])
def l318_214(x):
    # x is a list (or vector) of length 288
    return max(0, x[214])
def l318_215(x):
    # x is a list (or vector) of length 288
    return max(0, x[215])
def l318_216(x):
    # x is a list (or vector) of length 288
    return max(0, x[216])
def l318_217(x):
    # x is a list (or vector) of length 288
    return max(0, x[217])
def l318_218(x):
    # x is a list (or vector) of length 288
    return max(0, x[218])
def l318_219(x):
    # x is a list (or vector) of length 288
    return max(0, x[219])
def l318_220(x):
    # x is a list (or vector) of length 288
    return max(0, x[220])
def l318_221(x):
    # x is a list (or vector) of length 288
    return max(0, x[221])
def l318_222(x):
    # x is a list (or vector) of length 288
    return max(0, x[222])
def l318_223(x):
    # x is a list (or vector) of length 288
    return max(0, x[223])
def l318_224(x):
    # x is a list (or vector) of length 288
    return max(0, x[224])
def l318_225(x):
    # x is a list (or vector) of length 288
    return max(0, x[225])
def l318_226(x):
    # x is a list (or vector) of length 288
    return max(0, x[226])
def l318_227(x):
    # x is a list (or vector) of length 288
    return max(0, x[227])
def l318_228(x):
    # x is a list (or vector) of length 288
    return max(0, x[228])
def l318_229(x):
    # x is a list (or vector) of length 288
    return max(0, x[229])
def l318_230(x):
    # x is a list (or vector) of length 288
    return max(0, x[230])
def l318_231(x):
    # x is a list (or vector) of length 288
    return max(0, x[231])
def l318_232(x):
    # x is a list (or vector) of length 288
    return max(0, x[232])
def l318_233(x):
    # x is a list (or vector) of length 288
    return max(0, x[233])
def l318_234(x):
    # x is a list (or vector) of length 288
    return max(0, x[234])
def l318_235(x):
    # x is a list (or vector) of length 288
    return max(0, x[235])
def l318_236(x):
    # x is a list (or vector) of length 288
    return max(0, x[236])
def l318_237(x):
    # x is a list (or vector) of length 288
    return max(0, x[237])
def l318_238(x):
    # x is a list (or vector) of length 288
    return max(0, x[238])
def l318_239(x):
    # x is a list (or vector) of length 288
    return max(0, x[239])
def l318_240(x):
    # x is a list (or vector) of length 288
    return max(0, x[240])
def l318_241(x):
    # x is a list (or vector) of length 288
    return max(0, x[241])
def l318_242(x):
    # x is a list (or vector) of length 288
    return max(0, x[242])
def l318_243(x):
    # x is a list (or vector) of length 288
    return max(0, x[243])
def l318_244(x):
    # x is a list (or vector) of length 288
    return max(0, x[244])
def l318_245(x):
    # x is a list (or vector) of length 288
    return max(0, x[245])
def l318_246(x):
    # x is a list (or vector) of length 288
    return max(0, x[246])
def l318_247(x):
    # x is a list (or vector) of length 288
    return max(0, x[247])
def l318_248(x):
    # x is a list (or vector) of length 288
    return max(0, x[248])
def l318_249(x):
    # x is a list (or vector) of length 288
    return max(0, x[249])
def l318_250(x):
    # x is a list (or vector) of length 288
    return max(0, x[250])
def l318_251(x):
    # x is a list (or vector) of length 288
    return max(0, x[251])
def l318_252(x):
    # x is a list (or vector) of length 288
    return max(0, x[252])
def l318_253(x):
    # x is a list (or vector) of length 288
    return max(0, x[253])
def l318_254(x):
    # x is a list (or vector) of length 288
    return max(0, x[254])
def l318_255(x):
    # x is a list (or vector) of length 288
    return max(0, x[255])
def l318_256(x):
    # x is a list (or vector) of length 288
    return max(0, x[256])
def l318_257(x):
    # x is a list (or vector) of length 288
    return max(0, x[257])
def l318_258(x):
    # x is a list (or vector) of length 288
    return max(0, x[258])
def l318_259(x):
    # x is a list (or vector) of length 288
    return max(0, x[259])
def l318_260(x):
    # x is a list (or vector) of length 288
    return max(0, x[260])
def l318_261(x):
    # x is a list (or vector) of length 288
    return max(0, x[261])
def l318_262(x):
    # x is a list (or vector) of length 288
    return max(0, x[262])
def l318_263(x):
    # x is a list (or vector) of length 288
    return max(0, x[263])
def l318_264(x):
    # x is a list (or vector) of length 288
    return max(0, x[264])
def l318_265(x):
    # x is a list (or vector) of length 288
    return max(0, x[265])
def l318_266(x):
    # x is a list (or vector) of length 288
    return max(0, x[266])
def l318_267(x):
    # x is a list (or vector) of length 288
    return max(0, x[267])
def l318_268(x):
    # x is a list (or vector) of length 288
    return max(0, x[268])
def l318_269(x):
    # x is a list (or vector) of length 288
    return max(0, x[269])
def l318_270(x):
    # x is a list (or vector) of length 288
    return max(0, x[270])
def l318_271(x):
    # x is a list (or vector) of length 288
    return max(0, x[271])
def l318_272(x):
    # x is a list (or vector) of length 288
    return max(0, x[272])
def l318_273(x):
    # x is a list (or vector) of length 288
    return max(0, x[273])
def l318_274(x):
    # x is a list (or vector) of length 288
    return max(0, x[274])
def l318_275(x):
    # x is a list (or vector) of length 288
    return max(0, x[275])
def l318_276(x):
    # x is a list (or vector) of length 288
    return max(0, x[276])
def l318_277(x):
    # x is a list (or vector) of length 288
    return max(0, x[277])
def l318_278(x):
    # x is a list (or vector) of length 288
    return max(0, x[278])
def l318_279(x):
    # x is a list (or vector) of length 288
    return max(0, x[279])
def l318_280(x):
    # x is a list (or vector) of length 288
    return max(0, x[280])
def l318_281(x):
    # x is a list (or vector) of length 288
    return max(0, x[281])
def l318_282(x):
    # x is a list (or vector) of length 288
    return max(0, x[282])
def l318_283(x):
    # x is a list (or vector) of length 288
    return max(0, x[283])
def l318_284(x):
    # x is a list (or vector) of length 288
    return max(0, x[284])
def l318_285(x):
    # x is a list (or vector) of length 288
    return max(0, x[285])
def l318_286(x):
    # x is a list (or vector) of length 288
    return max(0, x[286])
def l318_287(x):
    # x is a list (or vector) of length 288
    return max(0, x[287])
def l318_(x):
    # x is a list (or vector) of length 288
    return [
        l318_0(x),
        l318_1(x),
        l318_2(x),
        l318_3(x),
        l318_4(x),
        l318_5(x),
        l318_6(x),
        l318_7(x),
        l318_8(x),
        l318_9(x),
        l318_10(x),
        l318_11(x),
        l318_12(x),
        l318_13(x),
        l318_14(x),
        l318_15(x),
        l318_16(x),
        l318_17(x),
        l318_18(x),
        l318_19(x),
        l318_20(x),
        l318_21(x),
        l318_22(x),
        l318_23(x),
        l318_24(x),
        l318_25(x),
        l318_26(x),
        l318_27(x),
        l318_28(x),
        l318_29(x),
        l318_30(x),
        l318_31(x),
        l318_32(x),
        l318_33(x),
        l318_34(x),
        l318_35(x),
        l318_36(x),
        l318_37(x),
        l318_38(x),
        l318_39(x),
        l318_40(x),
        l318_41(x),
        l318_42(x),
        l318_43(x),
        l318_44(x),
        l318_45(x),
        l318_46(x),
        l318_47(x),
        l318_48(x),
        l318_49(x),
        l318_50(x),
        l318_51(x),
        l318_52(x),
        l318_53(x),
        l318_54(x),
        l318_55(x),
        l318_56(x),
        l318_57(x),
        l318_58(x),
        l318_59(x),
        l318_60(x),
        l318_61(x),
        l318_62(x),
        l318_63(x),
        l318_64(x),
        l318_65(x),
        l318_66(x),
        l318_67(x),
        l318_68(x),
        l318_69(x),
        l318_70(x),
        l318_71(x),
        l318_72(x),
        l318_73(x),
        l318_74(x),
        l318_75(x),
        l318_76(x),
        l318_77(x),
        l318_78(x),
        l318_79(x),
        l318_80(x),
        l318_81(x),
        l318_82(x),
        l318_83(x),
        l318_84(x),
        l318_85(x),
        l318_86(x),
        l318_87(x),
        l318_88(x),
        l318_89(x),
        l318_90(x),
        l318_91(x),
        l318_92(x),
        l318_93(x),
        l318_94(x),
        l318_95(x),
        l318_96(x),
        l318_97(x),
        l318_98(x),
        l318_99(x),
        l318_100(x),
        l318_101(x),
        l318_102(x),
        l318_103(x),
        l318_104(x),
        l318_105(x),
        l318_106(x),
        l318_107(x),
        l318_108(x),
        l318_109(x),
        l318_110(x),
        l318_111(x),
        l318_112(x),
        l318_113(x),
        l318_114(x),
        l318_115(x),
        l318_116(x),
        l318_117(x),
        l318_118(x),
        l318_119(x),
        l318_120(x),
        l318_121(x),
        l318_122(x),
        l318_123(x),
        l318_124(x),
        l318_125(x),
        l318_126(x),
        l318_127(x),
        l318_128(x),
        l318_129(x),
        l318_130(x),
        l318_131(x),
        l318_132(x),
        l318_133(x),
        l318_134(x),
        l318_135(x),
        l318_136(x),
        l318_137(x),
        l318_138(x),
        l318_139(x),
        l318_140(x),
        l318_141(x),
        l318_142(x),
        l318_143(x),
        l318_144(x),
        l318_145(x),
        l318_146(x),
        l318_147(x),
        l318_148(x),
        l318_149(x),
        l318_150(x),
        l318_151(x),
        l318_152(x),
        l318_153(x),
        l318_154(x),
        l318_155(x),
        l318_156(x),
        l318_157(x),
        l318_158(x),
        l318_159(x),
        l318_160(x),
        l318_161(x),
        l318_162(x),
        l318_163(x),
        l318_164(x),
        l318_165(x),
        l318_166(x),
        l318_167(x),
        l318_168(x),
        l318_169(x),
        l318_170(x),
        l318_171(x),
        l318_172(x),
        l318_173(x),
        l318_174(x),
        l318_175(x),
        l318_176(x),
        l318_177(x),
        l318_178(x),
        l318_179(x),
        l318_180(x),
        l318_181(x),
        l318_182(x),
        l318_183(x),
        l318_184(x),
        l318_185(x),
        l318_186(x),
        l318_187(x),
        l318_188(x),
        l318_189(x),
        l318_190(x),
        l318_191(x),
        l318_192(x),
        l318_193(x),
        l318_194(x),
        l318_195(x),
        l318_196(x),
        l318_197(x),
        l318_198(x),
        l318_199(x),
        l318_200(x),
        l318_201(x),
        l318_202(x),
        l318_203(x),
        l318_204(x),
        l318_205(x),
        l318_206(x),
        l318_207(x),
        l318_208(x),
        l318_209(x),
        l318_210(x),
        l318_211(x),
        l318_212(x),
        l318_213(x),
        l318_214(x),
        l318_215(x),
        l318_216(x),
        l318_217(x),
        l318_218(x),
        l318_219(x),
        l318_220(x),
        l318_221(x),
        l318_222(x),
        l318_223(x),
        l318_224(x),
        l318_225(x),
        l318_226(x),
        l318_227(x),
        l318_228(x),
        l318_229(x),
        l318_230(x),
        l318_231(x),
        l318_232(x),
        l318_233(x),
        l318_234(x),
        l318_235(x),
        l318_236(x),
        l318_237(x),
        l318_238(x),
        l318_239(x),
        l318_240(x),
        l318_241(x),
        l318_242(x),
        l318_243(x),
        l318_244(x),
        l318_245(x),
        l318_246(x),
        l318_247(x),
        l318_248(x),
        l318_249(x),
        l318_250(x),
        l318_251(x),
        l318_252(x),
        l318_253(x),
        l318_254(x),
        l318_255(x),
        l318_256(x),
        l318_257(x),
        l318_258(x),
        l318_259(x),
        l318_260(x),
        l318_261(x),
        l318_262(x),
        l318_263(x),
        l318_264(x),
        l318_265(x),
        l318_266(x),
        l318_267(x),
        l318_268(x),
        l318_269(x),
        l318_270(x),
        l318_271(x),
        l318_272(x),
        l318_273(x),
        l318_274(x),
        l318_275(x),
        l318_276(x),
        l318_277(x),
        l318_278(x),
        l318_279(x),
        l318_280(x),
        l318_281(x),
        l318_282(x),
        l318_283(x),
        l318_284(x),
        l318_285(x),
        l318_286(x),
        l318_287(x),
    ]