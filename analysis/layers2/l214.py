import numpy as np




# Generated from reverse engineering
def l214_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 410
    out = np.empty(410, dtype=np.float32)
    
    # for i in range(0, 97):
    for i in range(0, 97):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x7fffffff (len=31)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(97, 128):
    for i in range(0, 31):
        s = -1 * x[97 + i] + -1 * x[128 + i]
        s += biases[i]
        out[97 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 129):
    for i in range(0, 1):
        s = x[190 + i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(129, 160):
    for i in range(0, 31):
        s = x[159 + i]
        out[129 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 193):
    for i in range(0, 33):
        s = x[191 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x1 (len=1)
    biases = [1.0]
    # for i in range(193, 194):
    for i in range(0, 1):
        s = -1 * x[224 + i]
        s += biases[i]
        out[193 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0]
    # for i in range(194, 195):
    for i in range(0, 1):
        s = x[223 + i] + x[257 + i]
        s += biases[i]
        out[194 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(195, 224):
    for i in range(0, 29):
        s = x[258 + i] + -1 * x[224 + i]
        out[195 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3fffffff (len=30)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(224, 254):
    for i in range(0, 30):
        s = -1 * x[225 + i]
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(254, 284):
    for i in range(0, 30):
        s = x[255 + i] + x[257 + i]
        s += biases[i]
        out[254 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(284, 286):
    for i in range(0, 2):
        s = x[255 + i]
        out[284 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(286, 330):
    for i in range(0, 44):
        s = x[287 + i]
        out[286 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [16.0, 16.0, 16.0, 16.0]
    # for i in range(330, 334):
    for i in range(0, 4):
        s = -1 * x[331 + i]
        s += biases[i]
        out[330 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(334, 338):
    for i in range(0, 4):
        s = x[331 + i]
        out[334 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-15.0, -15.0, -15.0, -15.0]
    # for i in range(338, 342):
    for i in range(0, 4):
        s = x[331 + i]
        s += biases[i]
        out[338 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-16.0, -16.0, -16.0, -16.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    # for i in range(342, 410):
    for i in range(0, 68):
        s = x[331 + i]
        s += biases[i]
        out[342 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l214_0(x):
    # x is a list (or vector) of length 399
    return max(0, x[0])
def l214_1(x):
    # x is a list (or vector) of length 399
    return max(0, x[1])
def l214_2(x):
    # x is a list (or vector) of length 399
    return max(0, x[2])
def l214_3(x):
    # x is a list (or vector) of length 399
    return max(0, x[3])
def l214_4(x):
    # x is a list (or vector) of length 399
    return max(0, x[4])
def l214_5(x):
    # x is a list (or vector) of length 399
    return max(0, x[5])
def l214_6(x):
    # x is a list (or vector) of length 399
    return max(0, x[6])
def l214_7(x):
    # x is a list (or vector) of length 399
    return max(0, x[7])
def l214_8(x):
    # x is a list (or vector) of length 399
    return max(0, x[8])
def l214_9(x):
    # x is a list (or vector) of length 399
    return max(0, x[9])
def l214_10(x):
    # x is a list (or vector) of length 399
    return max(0, x[10])
def l214_11(x):
    # x is a list (or vector) of length 399
    return max(0, x[11])
def l214_12(x):
    # x is a list (or vector) of length 399
    return max(0, x[12])
def l214_13(x):
    # x is a list (or vector) of length 399
    return max(0, x[13])
def l214_14(x):
    # x is a list (or vector) of length 399
    return max(0, x[14])
def l214_15(x):
    # x is a list (or vector) of length 399
    return max(0, x[15])
def l214_16(x):
    # x is a list (or vector) of length 399
    return max(0, x[16])
def l214_17(x):
    # x is a list (or vector) of length 399
    return max(0, x[17])
def l214_18(x):
    # x is a list (or vector) of length 399
    return max(0, x[18])
def l214_19(x):
    # x is a list (or vector) of length 399
    return max(0, x[19])
def l214_20(x):
    # x is a list (or vector) of length 399
    return max(0, x[20])
def l214_21(x):
    # x is a list (or vector) of length 399
    return max(0, x[21])
def l214_22(x):
    # x is a list (or vector) of length 399
    return max(0, x[22])
def l214_23(x):
    # x is a list (or vector) of length 399
    return max(0, x[23])
def l214_24(x):
    # x is a list (or vector) of length 399
    return max(0, x[24])
def l214_25(x):
    # x is a list (or vector) of length 399
    return max(0, x[25])
def l214_26(x):
    # x is a list (or vector) of length 399
    return max(0, x[26])
def l214_27(x):
    # x is a list (or vector) of length 399
    return max(0, x[27])
def l214_28(x):
    # x is a list (or vector) of length 399
    return max(0, x[28])
def l214_29(x):
    # x is a list (or vector) of length 399
    return max(0, x[29])
def l214_30(x):
    # x is a list (or vector) of length 399
    return max(0, x[30])
def l214_31(x):
    # x is a list (or vector) of length 399
    return max(0, x[31])
def l214_32(x):
    # x is a list (or vector) of length 399
    return max(0, x[32])
def l214_33(x):
    # x is a list (or vector) of length 399
    return max(0, x[33])
def l214_34(x):
    # x is a list (or vector) of length 399
    return max(0, x[34])
def l214_35(x):
    # x is a list (or vector) of length 399
    return max(0, x[35])
def l214_36(x):
    # x is a list (or vector) of length 399
    return max(0, x[36])
def l214_37(x):
    # x is a list (or vector) of length 399
    return max(0, x[37])
def l214_38(x):
    # x is a list (or vector) of length 399
    return max(0, x[38])
def l214_39(x):
    # x is a list (or vector) of length 399
    return max(0, x[39])
def l214_40(x):
    # x is a list (or vector) of length 399
    return max(0, x[40])
def l214_41(x):
    # x is a list (or vector) of length 399
    return max(0, x[41])
def l214_42(x):
    # x is a list (or vector) of length 399
    return max(0, x[42])
def l214_43(x):
    # x is a list (or vector) of length 399
    return max(0, x[43])
def l214_44(x):
    # x is a list (or vector) of length 399
    return max(0, x[44])
def l214_45(x):
    # x is a list (or vector) of length 399
    return max(0, x[45])
def l214_46(x):
    # x is a list (or vector) of length 399
    return max(0, x[46])
def l214_47(x):
    # x is a list (or vector) of length 399
    return max(0, x[47])
def l214_48(x):
    # x is a list (or vector) of length 399
    return max(0, x[48])
def l214_49(x):
    # x is a list (or vector) of length 399
    return max(0, x[49])
def l214_50(x):
    # x is a list (or vector) of length 399
    return max(0, x[50])
def l214_51(x):
    # x is a list (or vector) of length 399
    return max(0, x[51])
def l214_52(x):
    # x is a list (or vector) of length 399
    return max(0, x[52])
def l214_53(x):
    # x is a list (or vector) of length 399
    return max(0, x[53])
def l214_54(x):
    # x is a list (or vector) of length 399
    return max(0, x[54])
def l214_55(x):
    # x is a list (or vector) of length 399
    return max(0, x[55])
def l214_56(x):
    # x is a list (or vector) of length 399
    return max(0, x[56])
def l214_57(x):
    # x is a list (or vector) of length 399
    return max(0, x[57])
def l214_58(x):
    # x is a list (or vector) of length 399
    return max(0, x[58])
def l214_59(x):
    # x is a list (or vector) of length 399
    return max(0, x[59])
def l214_60(x):
    # x is a list (or vector) of length 399
    return max(0, x[60])
def l214_61(x):
    # x is a list (or vector) of length 399
    return max(0, x[61])
def l214_62(x):
    # x is a list (or vector) of length 399
    return max(0, x[62])
def l214_63(x):
    # x is a list (or vector) of length 399
    return max(0, x[63])
def l214_64(x):
    # x is a list (or vector) of length 399
    return max(0, x[64])
def l214_65(x):
    # x is a list (or vector) of length 399
    return max(0, x[65])
def l214_66(x):
    # x is a list (or vector) of length 399
    return max(0, x[66])
def l214_67(x):
    # x is a list (or vector) of length 399
    return max(0, x[67])
def l214_68(x):
    # x is a list (or vector) of length 399
    return max(0, x[68])
def l214_69(x):
    # x is a list (or vector) of length 399
    return max(0, x[69])
def l214_70(x):
    # x is a list (or vector) of length 399
    return max(0, x[70])
def l214_71(x):
    # x is a list (or vector) of length 399
    return max(0, x[71])
def l214_72(x):
    # x is a list (or vector) of length 399
    return max(0, x[72])
def l214_73(x):
    # x is a list (or vector) of length 399
    return max(0, x[73])
def l214_74(x):
    # x is a list (or vector) of length 399
    return max(0, x[74])
def l214_75(x):
    # x is a list (or vector) of length 399
    return max(0, x[75])
def l214_76(x):
    # x is a list (or vector) of length 399
    return max(0, x[76])
def l214_77(x):
    # x is a list (or vector) of length 399
    return max(0, x[77])
def l214_78(x):
    # x is a list (or vector) of length 399
    return max(0, x[78])
def l214_79(x):
    # x is a list (or vector) of length 399
    return max(0, x[79])
def l214_80(x):
    # x is a list (or vector) of length 399
    return max(0, x[80])
def l214_81(x):
    # x is a list (or vector) of length 399
    return max(0, x[81])
def l214_82(x):
    # x is a list (or vector) of length 399
    return max(0, x[82])
def l214_83(x):
    # x is a list (or vector) of length 399
    return max(0, x[83])
def l214_84(x):
    # x is a list (or vector) of length 399
    return max(0, x[84])
def l214_85(x):
    # x is a list (or vector) of length 399
    return max(0, x[85])
def l214_86(x):
    # x is a list (or vector) of length 399
    return max(0, x[86])
def l214_87(x):
    # x is a list (or vector) of length 399
    return max(0, x[87])
def l214_88(x):
    # x is a list (or vector) of length 399
    return max(0, x[88])
def l214_89(x):
    # x is a list (or vector) of length 399
    return max(0, x[89])
def l214_90(x):
    # x is a list (or vector) of length 399
    return max(0, x[90])
def l214_91(x):
    # x is a list (or vector) of length 399
    return max(0, x[91])
def l214_92(x):
    # x is a list (or vector) of length 399
    return max(0, x[92])
def l214_93(x):
    # x is a list (or vector) of length 399
    return max(0, x[93])
def l214_94(x):
    # x is a list (or vector) of length 399
    return max(0, x[94])
def l214_95(x):
    # x is a list (or vector) of length 399
    return max(0, x[95])
def l214_96(x):
    # x is a list (or vector) of length 399
    return max(0, x[96])
def l214_97(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[97] + -1.0*x[128] + 1.0)
def l214_98(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[98] + -1.0*x[129] + 1.0)
def l214_99(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[99] + -1.0*x[130] + 1.0)
def l214_100(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[100] + -1.0*x[131] + 1.0)
def l214_101(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[101] + -1.0*x[132] + 1.0)
def l214_102(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[102] + -1.0*x[133] + 1.0)
def l214_103(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[103] + -1.0*x[134] + 1.0)
def l214_104(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[104] + -1.0*x[135] + 1.0)
def l214_105(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[105] + -1.0*x[136] + 1.0)
def l214_106(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[106] + -1.0*x[137] + 1.0)
def l214_107(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[107] + -1.0*x[138] + 1.0)
def l214_108(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[108] + -1.0*x[139] + 1.0)
def l214_109(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[109] + -1.0*x[140] + 1.0)
def l214_110(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[110] + -1.0*x[141] + 1.0)
def l214_111(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[111] + -1.0*x[142] + 1.0)
def l214_112(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[112] + -1.0*x[143] + 1.0)
def l214_113(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[113] + -1.0*x[144] + 1.0)
def l214_114(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[114] + -1.0*x[145] + 1.0)
def l214_115(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[115] + -1.0*x[146] + 1.0)
def l214_116(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[116] + -1.0*x[147] + 1.0)
def l214_117(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[117] + -1.0*x[148] + 1.0)
def l214_118(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[118] + -1.0*x[149] + 1.0)
def l214_119(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[119] + -1.0*x[150] + 1.0)
def l214_120(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[120] + -1.0*x[151] + 1.0)
def l214_121(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[121] + -1.0*x[152] + 1.0)
def l214_122(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[122] + -1.0*x[153] + 1.0)
def l214_123(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[123] + -1.0*x[154] + 1.0)
def l214_124(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[124] + -1.0*x[155] + 1.0)
def l214_125(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[125] + -1.0*x[156] + 1.0)
def l214_126(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[126] + -1.0*x[157] + 1.0)
def l214_127(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[127] + -1.0*x[158] + 1.0)
def l214_128(x):
    # x is a list (or vector) of length 399
    return max(0, x[190])
def l214_129(x):
    # x is a list (or vector) of length 399
    return max(0, x[159])
def l214_130(x):
    # x is a list (or vector) of length 399
    return max(0, x[160])
def l214_131(x):
    # x is a list (or vector) of length 399
    return max(0, x[161])
def l214_132(x):
    # x is a list (or vector) of length 399
    return max(0, x[162])
def l214_133(x):
    # x is a list (or vector) of length 399
    return max(0, x[163])
def l214_134(x):
    # x is a list (or vector) of length 399
    return max(0, x[164])
def l214_135(x):
    # x is a list (or vector) of length 399
    return max(0, x[165])
def l214_136(x):
    # x is a list (or vector) of length 399
    return max(0, x[166])
def l214_137(x):
    # x is a list (or vector) of length 399
    return max(0, x[167])
def l214_138(x):
    # x is a list (or vector) of length 399
    return max(0, x[168])
def l214_139(x):
    # x is a list (or vector) of length 399
    return max(0, x[169])
def l214_140(x):
    # x is a list (or vector) of length 399
    return max(0, x[170])
def l214_141(x):
    # x is a list (or vector) of length 399
    return max(0, x[171])
def l214_142(x):
    # x is a list (or vector) of length 399
    return max(0, x[172])
def l214_143(x):
    # x is a list (or vector) of length 399
    return max(0, x[173])
def l214_144(x):
    # x is a list (or vector) of length 399
    return max(0, x[174])
def l214_145(x):
    # x is a list (or vector) of length 399
    return max(0, x[175])
def l214_146(x):
    # x is a list (or vector) of length 399
    return max(0, x[176])
def l214_147(x):
    # x is a list (or vector) of length 399
    return max(0, x[177])
def l214_148(x):
    # x is a list (or vector) of length 399
    return max(0, x[178])
def l214_149(x):
    # x is a list (or vector) of length 399
    return max(0, x[179])
def l214_150(x):
    # x is a list (or vector) of length 399
    return max(0, x[180])
def l214_151(x):
    # x is a list (or vector) of length 399
    return max(0, x[181])
def l214_152(x):
    # x is a list (or vector) of length 399
    return max(0, x[182])
def l214_153(x):
    # x is a list (or vector) of length 399
    return max(0, x[183])
def l214_154(x):
    # x is a list (or vector) of length 399
    return max(0, x[184])
def l214_155(x):
    # x is a list (or vector) of length 399
    return max(0, x[185])
def l214_156(x):
    # x is a list (or vector) of length 399
    return max(0, x[186])
def l214_157(x):
    # x is a list (or vector) of length 399
    return max(0, x[187])
def l214_158(x):
    # x is a list (or vector) of length 399
    return max(0, x[188])
def l214_159(x):
    # x is a list (or vector) of length 399
    return max(0, x[189])
def l214_160(x):
    # x is a list (or vector) of length 399
    return max(0, x[191])
def l214_161(x):
    # x is a list (or vector) of length 399
    return max(0, x[192])
def l214_162(x):
    # x is a list (or vector) of length 399
    return max(0, x[193])
def l214_163(x):
    # x is a list (or vector) of length 399
    return max(0, x[194])
def l214_164(x):
    # x is a list (or vector) of length 399
    return max(0, x[195])
def l214_165(x):
    # x is a list (or vector) of length 399
    return max(0, x[196])
def l214_166(x):
    # x is a list (or vector) of length 399
    return max(0, x[197])
def l214_167(x):
    # x is a list (or vector) of length 399
    return max(0, x[198])
def l214_168(x):
    # x is a list (or vector) of length 399
    return max(0, x[199])
def l214_169(x):
    # x is a list (or vector) of length 399
    return max(0, x[200])
def l214_170(x):
    # x is a list (or vector) of length 399
    return max(0, x[201])
def l214_171(x):
    # x is a list (or vector) of length 399
    return max(0, x[202])
def l214_172(x):
    # x is a list (or vector) of length 399
    return max(0, x[203])
def l214_173(x):
    # x is a list (or vector) of length 399
    return max(0, x[204])
def l214_174(x):
    # x is a list (or vector) of length 399
    return max(0, x[205])
def l214_175(x):
    # x is a list (or vector) of length 399
    return max(0, x[206])
def l214_176(x):
    # x is a list (or vector) of length 399
    return max(0, x[207])
def l214_177(x):
    # x is a list (or vector) of length 399
    return max(0, x[208])
def l214_178(x):
    # x is a list (or vector) of length 399
    return max(0, x[209])
def l214_179(x):
    # x is a list (or vector) of length 399
    return max(0, x[210])
def l214_180(x):
    # x is a list (or vector) of length 399
    return max(0, x[211])
def l214_181(x):
    # x is a list (or vector) of length 399
    return max(0, x[212])
def l214_182(x):
    # x is a list (or vector) of length 399
    return max(0, x[213])
def l214_183(x):
    # x is a list (or vector) of length 399
    return max(0, x[214])
def l214_184(x):
    # x is a list (or vector) of length 399
    return max(0, x[215])
def l214_185(x):
    # x is a list (or vector) of length 399
    return max(0, x[216])
def l214_186(x):
    # x is a list (or vector) of length 399
    return max(0, x[217])
def l214_187(x):
    # x is a list (or vector) of length 399
    return max(0, x[218])
def l214_188(x):
    # x is a list (or vector) of length 399
    return max(0, x[219])
def l214_189(x):
    # x is a list (or vector) of length 399
    return max(0, x[220])
def l214_190(x):
    # x is a list (or vector) of length 399
    return max(0, x[221])
def l214_191(x):
    # x is a list (or vector) of length 399
    return max(0, x[222])
def l214_192(x):
    # x is a list (or vector) of length 399
    return max(0, x[223])
def l214_193(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[224] + 1.0)
def l214_194(x):
    # x is a list (or vector) of length 399
    return max(0, x[223] + x[257] + -1.0)
def l214_195(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[224] + x[258])
def l214_196(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[225] + x[259])
def l214_197(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[226] + x[260])
def l214_198(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[227] + x[261])
def l214_199(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[228] + x[262])
def l214_200(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[229] + x[263])
def l214_201(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[230] + x[264])
def l214_202(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[231] + x[265])
def l214_203(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[232] + x[266])
def l214_204(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[233] + x[267])
def l214_205(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[234] + x[268])
def l214_206(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[235] + x[269])
def l214_207(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[236] + x[270])
def l214_208(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[237] + x[271])
def l214_209(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[238] + x[272])
def l214_210(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[239] + x[273])
def l214_211(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[240] + x[274])
def l214_212(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[241] + x[275])
def l214_213(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[242] + x[276])
def l214_214(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[243] + x[277])
def l214_215(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[244] + x[278])
def l214_216(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[245] + x[279])
def l214_217(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[246] + x[280])
def l214_218(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[247] + x[281])
def l214_219(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[248] + x[282])
def l214_220(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[249] + x[283])
def l214_221(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[250] + x[284])
def l214_222(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[251] + x[285])
def l214_223(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[252] + x[286])
def l214_224(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[225] + 1.0)
def l214_225(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[226] + 1.0)
def l214_226(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[227] + 1.0)
def l214_227(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[228] + 1.0)
def l214_228(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[229] + 1.0)
def l214_229(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[230] + 1.0)
def l214_230(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[231] + 1.0)
def l214_231(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[232] + 1.0)
def l214_232(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[233] + 1.0)
def l214_233(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[234] + 1.0)
def l214_234(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[235] + 1.0)
def l214_235(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[236] + 1.0)
def l214_236(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[237] + 1.0)
def l214_237(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[238] + 1.0)
def l214_238(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[239] + 1.0)
def l214_239(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[240] + 1.0)
def l214_240(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[241] + 1.0)
def l214_241(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[242] + 1.0)
def l214_242(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[243] + 1.0)
def l214_243(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[244] + 1.0)
def l214_244(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[245] + 1.0)
def l214_245(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[246] + 1.0)
def l214_246(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[247] + 1.0)
def l214_247(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[248] + 1.0)
def l214_248(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[249] + 1.0)
def l214_249(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[250] + 1.0)
def l214_250(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[251] + 1.0)
def l214_251(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[252] + 1.0)
def l214_252(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[253] + 1.0)
def l214_253(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[254] + 1.0)
def l214_254(x):
    # x is a list (or vector) of length 399
    return max(0, x[255] + x[257] + -1.0)
def l214_255(x):
    # x is a list (or vector) of length 399
    return max(0, x[256] + x[258] + -1.0)
def l214_256(x):
    # x is a list (or vector) of length 399
    return max(0, x[257] + x[259] + -1.0)
def l214_257(x):
    # x is a list (or vector) of length 399
    return max(0, x[258] + x[260] + -1.0)
def l214_258(x):
    # x is a list (or vector) of length 399
    return max(0, x[259] + x[261] + -1.0)
def l214_259(x):
    # x is a list (or vector) of length 399
    return max(0, x[260] + x[262] + -1.0)
def l214_260(x):
    # x is a list (or vector) of length 399
    return max(0, x[261] + x[263] + -1.0)
def l214_261(x):
    # x is a list (or vector) of length 399
    return max(0, x[262] + x[264] + -1.0)
def l214_262(x):
    # x is a list (or vector) of length 399
    return max(0, x[263] + x[265] + -1.0)
def l214_263(x):
    # x is a list (or vector) of length 399
    return max(0, x[264] + x[266] + -1.0)
def l214_264(x):
    # x is a list (or vector) of length 399
    return max(0, x[265] + x[267] + -1.0)
def l214_265(x):
    # x is a list (or vector) of length 399
    return max(0, x[266] + x[268] + -1.0)
def l214_266(x):
    # x is a list (or vector) of length 399
    return max(0, x[267] + x[269] + -1.0)
def l214_267(x):
    # x is a list (or vector) of length 399
    return max(0, x[268] + x[270] + -1.0)
def l214_268(x):
    # x is a list (or vector) of length 399
    return max(0, x[269] + x[271] + -1.0)
def l214_269(x):
    # x is a list (or vector) of length 399
    return max(0, x[270] + x[272] + -1.0)
def l214_270(x):
    # x is a list (or vector) of length 399
    return max(0, x[271] + x[273] + -1.0)
def l214_271(x):
    # x is a list (or vector) of length 399
    return max(0, x[272] + x[274] + -1.0)
def l214_272(x):
    # x is a list (or vector) of length 399
    return max(0, x[273] + x[275] + -1.0)
def l214_273(x):
    # x is a list (or vector) of length 399
    return max(0, x[274] + x[276] + -1.0)
def l214_274(x):
    # x is a list (or vector) of length 399
    return max(0, x[275] + x[277] + -1.0)
def l214_275(x):
    # x is a list (or vector) of length 399
    return max(0, x[276] + x[278] + -1.0)
def l214_276(x):
    # x is a list (or vector) of length 399
    return max(0, x[277] + x[279] + -1.0)
def l214_277(x):
    # x is a list (or vector) of length 399
    return max(0, x[278] + x[280] + -1.0)
def l214_278(x):
    # x is a list (or vector) of length 399
    return max(0, x[279] + x[281] + -1.0)
def l214_279(x):
    # x is a list (or vector) of length 399
    return max(0, x[280] + x[282] + -1.0)
def l214_280(x):
    # x is a list (or vector) of length 399
    return max(0, x[281] + x[283] + -1.0)
def l214_281(x):
    # x is a list (or vector) of length 399
    return max(0, x[282] + x[284] + -1.0)
def l214_282(x):
    # x is a list (or vector) of length 399
    return max(0, x[283] + x[285] + -1.0)
def l214_283(x):
    # x is a list (or vector) of length 399
    return max(0, x[284] + x[286] + -1.0)
def l214_284(x):
    # x is a list (or vector) of length 399
    return max(0, x[255])
def l214_285(x):
    # x is a list (or vector) of length 399
    return max(0, x[256])
def l214_286(x):
    # x is a list (or vector) of length 399
    return max(0, x[287])
def l214_287(x):
    # x is a list (or vector) of length 399
    return max(0, x[288])
def l214_288(x):
    # x is a list (or vector) of length 399
    return max(0, x[289])
def l214_289(x):
    # x is a list (or vector) of length 399
    return max(0, x[290])
def l214_290(x):
    # x is a list (or vector) of length 399
    return max(0, x[291])
def l214_291(x):
    # x is a list (or vector) of length 399
    return max(0, x[292])
def l214_292(x):
    # x is a list (or vector) of length 399
    return max(0, x[293])
def l214_293(x):
    # x is a list (or vector) of length 399
    return max(0, x[294])
def l214_294(x):
    # x is a list (or vector) of length 399
    return max(0, x[295])
def l214_295(x):
    # x is a list (or vector) of length 399
    return max(0, x[296])
def l214_296(x):
    # x is a list (or vector) of length 399
    return max(0, x[297])
def l214_297(x):
    # x is a list (or vector) of length 399
    return max(0, x[298])
def l214_298(x):
    # x is a list (or vector) of length 399
    return max(0, x[299])
def l214_299(x):
    # x is a list (or vector) of length 399
    return max(0, x[300])
def l214_300(x):
    # x is a list (or vector) of length 399
    return max(0, x[301])
def l214_301(x):
    # x is a list (or vector) of length 399
    return max(0, x[302])
def l214_302(x):
    # x is a list (or vector) of length 399
    return max(0, x[303])
def l214_303(x):
    # x is a list (or vector) of length 399
    return max(0, x[304])
def l214_304(x):
    # x is a list (or vector) of length 399
    return max(0, x[305])
def l214_305(x):
    # x is a list (or vector) of length 399
    return max(0, x[306])
def l214_306(x):
    # x is a list (or vector) of length 399
    return max(0, x[307])
def l214_307(x):
    # x is a list (or vector) of length 399
    return max(0, x[308])
def l214_308(x):
    # x is a list (or vector) of length 399
    return max(0, x[309])
def l214_309(x):
    # x is a list (or vector) of length 399
    return max(0, x[310])
def l214_310(x):
    # x is a list (or vector) of length 399
    return max(0, x[311])
def l214_311(x):
    # x is a list (or vector) of length 399
    return max(0, x[312])
def l214_312(x):
    # x is a list (or vector) of length 399
    return max(0, x[313])
def l214_313(x):
    # x is a list (or vector) of length 399
    return max(0, x[314])
def l214_314(x):
    # x is a list (or vector) of length 399
    return max(0, x[315])
def l214_315(x):
    # x is a list (or vector) of length 399
    return max(0, x[316])
def l214_316(x):
    # x is a list (or vector) of length 399
    return max(0, x[317])
def l214_317(x):
    # x is a list (or vector) of length 399
    return max(0, x[318])
def l214_318(x):
    # x is a list (or vector) of length 399
    return max(0, x[319])
def l214_319(x):
    # x is a list (or vector) of length 399
    return max(0, x[320])
def l214_320(x):
    # x is a list (or vector) of length 399
    return max(0, x[321])
def l214_321(x):
    # x is a list (or vector) of length 399
    return max(0, x[322])
def l214_322(x):
    # x is a list (or vector) of length 399
    return max(0, x[323])
def l214_323(x):
    # x is a list (or vector) of length 399
    return max(0, x[324])
def l214_324(x):
    # x is a list (or vector) of length 399
    return max(0, x[325])
def l214_325(x):
    # x is a list (or vector) of length 399
    return max(0, x[326])
def l214_326(x):
    # x is a list (or vector) of length 399
    return max(0, x[327])
def l214_327(x):
    # x is a list (or vector) of length 399
    return max(0, x[328])
def l214_328(x):
    # x is a list (or vector) of length 399
    return max(0, x[329])
def l214_329(x):
    # x is a list (or vector) of length 399
    return max(0, x[330])
def l214_330(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[331] + 16.0)
def l214_331(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[332] + 16.0)
def l214_332(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[333] + 16.0)
def l214_333(x):
    # x is a list (or vector) of length 399
    return max(0, -1.0*x[334] + 16.0)
def l214_334(x):
    # x is a list (or vector) of length 399
    return max(0, x[331])
def l214_335(x):
    # x is a list (or vector) of length 399
    return max(0, x[332])
def l214_336(x):
    # x is a list (or vector) of length 399
    return max(0, x[333])
def l214_337(x):
    # x is a list (or vector) of length 399
    return max(0, x[334])
def l214_338(x):
    # x is a list (or vector) of length 399
    return max(0, x[331] + -15.0)
def l214_339(x):
    # x is a list (or vector) of length 399
    return max(0, x[332] + -15.0)
def l214_340(x):
    # x is a list (or vector) of length 399
    return max(0, x[333] + -15.0)
def l214_341(x):
    # x is a list (or vector) of length 399
    return max(0, x[334] + -15.0)
def l214_342(x):
    # x is a list (or vector) of length 399
    return max(0, x[331] + -16.0)
def l214_343(x):
    # x is a list (or vector) of length 399
    return max(0, x[332] + -16.0)
def l214_344(x):
    # x is a list (or vector) of length 399
    return max(0, x[333] + -16.0)
def l214_345(x):
    # x is a list (or vector) of length 399
    return max(0, x[334] + -16.0)
def l214_346(x):
    # x is a list (or vector) of length 399
    return max(0, x[335])
def l214_347(x):
    # x is a list (or vector) of length 399
    return max(0, x[336])
def l214_348(x):
    # x is a list (or vector) of length 399
    return max(0, x[337])
def l214_349(x):
    # x is a list (or vector) of length 399
    return max(0, x[338])
def l214_350(x):
    # x is a list (or vector) of length 399
    return max(0, x[339])
def l214_351(x):
    # x is a list (or vector) of length 399
    return max(0, x[340])
def l214_352(x):
    # x is a list (or vector) of length 399
    return max(0, x[341])
def l214_353(x):
    # x is a list (or vector) of length 399
    return max(0, x[342])
def l214_354(x):
    # x is a list (or vector) of length 399
    return max(0, x[343])
def l214_355(x):
    # x is a list (or vector) of length 399
    return max(0, x[344])
def l214_356(x):
    # x is a list (or vector) of length 399
    return max(0, x[345])
def l214_357(x):
    # x is a list (or vector) of length 399
    return max(0, x[346])
def l214_358(x):
    # x is a list (or vector) of length 399
    return max(0, x[347])
def l214_359(x):
    # x is a list (or vector) of length 399
    return max(0, x[348])
def l214_360(x):
    # x is a list (or vector) of length 399
    return max(0, x[349])
def l214_361(x):
    # x is a list (or vector) of length 399
    return max(0, x[350])
def l214_362(x):
    # x is a list (or vector) of length 399
    return max(0, x[351])
def l214_363(x):
    # x is a list (or vector) of length 399
    return max(0, x[352])
def l214_364(x):
    # x is a list (or vector) of length 399
    return max(0, x[353])
def l214_365(x):
    # x is a list (or vector) of length 399
    return max(0, x[354])
def l214_366(x):
    # x is a list (or vector) of length 399
    return max(0, x[355])
def l214_367(x):
    # x is a list (or vector) of length 399
    return max(0, x[356])
def l214_368(x):
    # x is a list (or vector) of length 399
    return max(0, x[357])
def l214_369(x):
    # x is a list (or vector) of length 399
    return max(0, x[358])
def l214_370(x):
    # x is a list (or vector) of length 399
    return max(0, x[359])
def l214_371(x):
    # x is a list (or vector) of length 399
    return max(0, x[360])
def l214_372(x):
    # x is a list (or vector) of length 399
    return max(0, x[361])
def l214_373(x):
    # x is a list (or vector) of length 399
    return max(0, x[362])
def l214_374(x):
    # x is a list (or vector) of length 399
    return max(0, x[363])
def l214_375(x):
    # x is a list (or vector) of length 399
    return max(0, x[364])
def l214_376(x):
    # x is a list (or vector) of length 399
    return max(0, x[365])
def l214_377(x):
    # x is a list (or vector) of length 399
    return max(0, x[366])
def l214_378(x):
    # x is a list (or vector) of length 399
    return max(0, x[367])
def l214_379(x):
    # x is a list (or vector) of length 399
    return max(0, x[368])
def l214_380(x):
    # x is a list (or vector) of length 399
    return max(0, x[369])
def l214_381(x):
    # x is a list (or vector) of length 399
    return max(0, x[370])
def l214_382(x):
    # x is a list (or vector) of length 399
    return max(0, x[371])
def l214_383(x):
    # x is a list (or vector) of length 399
    return max(0, x[372])
def l214_384(x):
    # x is a list (or vector) of length 399
    return max(0, x[373])
def l214_385(x):
    # x is a list (or vector) of length 399
    return max(0, x[374])
def l214_386(x):
    # x is a list (or vector) of length 399
    return max(0, x[375])
def l214_387(x):
    # x is a list (or vector) of length 399
    return max(0, x[376])
def l214_388(x):
    # x is a list (or vector) of length 399
    return max(0, x[377])
def l214_389(x):
    # x is a list (or vector) of length 399
    return max(0, x[378])
def l214_390(x):
    # x is a list (or vector) of length 399
    return max(0, x[379])
def l214_391(x):
    # x is a list (or vector) of length 399
    return max(0, x[380])
def l214_392(x):
    # x is a list (or vector) of length 399
    return max(0, x[381])
def l214_393(x):
    # x is a list (or vector) of length 399
    return max(0, x[382])
def l214_394(x):
    # x is a list (or vector) of length 399
    return max(0, x[383])
def l214_395(x):
    # x is a list (or vector) of length 399
    return max(0, x[384])
def l214_396(x):
    # x is a list (or vector) of length 399
    return max(0, x[385])
def l214_397(x):
    # x is a list (or vector) of length 399
    return max(0, x[386])
def l214_398(x):
    # x is a list (or vector) of length 399
    return max(0, x[387])
def l214_399(x):
    # x is a list (or vector) of length 399
    return max(0, x[388])
def l214_400(x):
    # x is a list (or vector) of length 399
    return max(0, x[389])
def l214_401(x):
    # x is a list (or vector) of length 399
    return max(0, x[390])
def l214_402(x):
    # x is a list (or vector) of length 399
    return max(0, x[391])
def l214_403(x):
    # x is a list (or vector) of length 399
    return max(0, x[392])
def l214_404(x):
    # x is a list (or vector) of length 399
    return max(0, x[393])
def l214_405(x):
    # x is a list (or vector) of length 399
    return max(0, x[394])
def l214_406(x):
    # x is a list (or vector) of length 399
    return max(0, x[395])
def l214_407(x):
    # x is a list (or vector) of length 399
    return max(0, x[396])
def l214_408(x):
    # x is a list (or vector) of length 399
    return max(0, x[397])
def l214_409(x):
    # x is a list (or vector) of length 399
    return max(0, x[398])
def l214_(x):
    # x is a list (or vector) of length 399
    return [
        l214_0(x),
        l214_1(x),
        l214_2(x),
        l214_3(x),
        l214_4(x),
        l214_5(x),
        l214_6(x),
        l214_7(x),
        l214_8(x),
        l214_9(x),
        l214_10(x),
        l214_11(x),
        l214_12(x),
        l214_13(x),
        l214_14(x),
        l214_15(x),
        l214_16(x),
        l214_17(x),
        l214_18(x),
        l214_19(x),
        l214_20(x),
        l214_21(x),
        l214_22(x),
        l214_23(x),
        l214_24(x),
        l214_25(x),
        l214_26(x),
        l214_27(x),
        l214_28(x),
        l214_29(x),
        l214_30(x),
        l214_31(x),
        l214_32(x),
        l214_33(x),
        l214_34(x),
        l214_35(x),
        l214_36(x),
        l214_37(x),
        l214_38(x),
        l214_39(x),
        l214_40(x),
        l214_41(x),
        l214_42(x),
        l214_43(x),
        l214_44(x),
        l214_45(x),
        l214_46(x),
        l214_47(x),
        l214_48(x),
        l214_49(x),
        l214_50(x),
        l214_51(x),
        l214_52(x),
        l214_53(x),
        l214_54(x),
        l214_55(x),
        l214_56(x),
        l214_57(x),
        l214_58(x),
        l214_59(x),
        l214_60(x),
        l214_61(x),
        l214_62(x),
        l214_63(x),
        l214_64(x),
        l214_65(x),
        l214_66(x),
        l214_67(x),
        l214_68(x),
        l214_69(x),
        l214_70(x),
        l214_71(x),
        l214_72(x),
        l214_73(x),
        l214_74(x),
        l214_75(x),
        l214_76(x),
        l214_77(x),
        l214_78(x),
        l214_79(x),
        l214_80(x),
        l214_81(x),
        l214_82(x),
        l214_83(x),
        l214_84(x),
        l214_85(x),
        l214_86(x),
        l214_87(x),
        l214_88(x),
        l214_89(x),
        l214_90(x),
        l214_91(x),
        l214_92(x),
        l214_93(x),
        l214_94(x),
        l214_95(x),
        l214_96(x),
        l214_97(x),
        l214_98(x),
        l214_99(x),
        l214_100(x),
        l214_101(x),
        l214_102(x),
        l214_103(x),
        l214_104(x),
        l214_105(x),
        l214_106(x),
        l214_107(x),
        l214_108(x),
        l214_109(x),
        l214_110(x),
        l214_111(x),
        l214_112(x),
        l214_113(x),
        l214_114(x),
        l214_115(x),
        l214_116(x),
        l214_117(x),
        l214_118(x),
        l214_119(x),
        l214_120(x),
        l214_121(x),
        l214_122(x),
        l214_123(x),
        l214_124(x),
        l214_125(x),
        l214_126(x),
        l214_127(x),
        l214_128(x),
        l214_129(x),
        l214_130(x),
        l214_131(x),
        l214_132(x),
        l214_133(x),
        l214_134(x),
        l214_135(x),
        l214_136(x),
        l214_137(x),
        l214_138(x),
        l214_139(x),
        l214_140(x),
        l214_141(x),
        l214_142(x),
        l214_143(x),
        l214_144(x),
        l214_145(x),
        l214_146(x),
        l214_147(x),
        l214_148(x),
        l214_149(x),
        l214_150(x),
        l214_151(x),
        l214_152(x),
        l214_153(x),
        l214_154(x),
        l214_155(x),
        l214_156(x),
        l214_157(x),
        l214_158(x),
        l214_159(x),
        l214_160(x),
        l214_161(x),
        l214_162(x),
        l214_163(x),
        l214_164(x),
        l214_165(x),
        l214_166(x),
        l214_167(x),
        l214_168(x),
        l214_169(x),
        l214_170(x),
        l214_171(x),
        l214_172(x),
        l214_173(x),
        l214_174(x),
        l214_175(x),
        l214_176(x),
        l214_177(x),
        l214_178(x),
        l214_179(x),
        l214_180(x),
        l214_181(x),
        l214_182(x),
        l214_183(x),
        l214_184(x),
        l214_185(x),
        l214_186(x),
        l214_187(x),
        l214_188(x),
        l214_189(x),
        l214_190(x),
        l214_191(x),
        l214_192(x),
        l214_193(x),
        l214_194(x),
        l214_195(x),
        l214_196(x),
        l214_197(x),
        l214_198(x),
        l214_199(x),
        l214_200(x),
        l214_201(x),
        l214_202(x),
        l214_203(x),
        l214_204(x),
        l214_205(x),
        l214_206(x),
        l214_207(x),
        l214_208(x),
        l214_209(x),
        l214_210(x),
        l214_211(x),
        l214_212(x),
        l214_213(x),
        l214_214(x),
        l214_215(x),
        l214_216(x),
        l214_217(x),
        l214_218(x),
        l214_219(x),
        l214_220(x),
        l214_221(x),
        l214_222(x),
        l214_223(x),
        l214_224(x),
        l214_225(x),
        l214_226(x),
        l214_227(x),
        l214_228(x),
        l214_229(x),
        l214_230(x),
        l214_231(x),
        l214_232(x),
        l214_233(x),
        l214_234(x),
        l214_235(x),
        l214_236(x),
        l214_237(x),
        l214_238(x),
        l214_239(x),
        l214_240(x),
        l214_241(x),
        l214_242(x),
        l214_243(x),
        l214_244(x),
        l214_245(x),
        l214_246(x),
        l214_247(x),
        l214_248(x),
        l214_249(x),
        l214_250(x),
        l214_251(x),
        l214_252(x),
        l214_253(x),
        l214_254(x),
        l214_255(x),
        l214_256(x),
        l214_257(x),
        l214_258(x),
        l214_259(x),
        l214_260(x),
        l214_261(x),
        l214_262(x),
        l214_263(x),
        l214_264(x),
        l214_265(x),
        l214_266(x),
        l214_267(x),
        l214_268(x),
        l214_269(x),
        l214_270(x),
        l214_271(x),
        l214_272(x),
        l214_273(x),
        l214_274(x),
        l214_275(x),
        l214_276(x),
        l214_277(x),
        l214_278(x),
        l214_279(x),
        l214_280(x),
        l214_281(x),
        l214_282(x),
        l214_283(x),
        l214_284(x),
        l214_285(x),
        l214_286(x),
        l214_287(x),
        l214_288(x),
        l214_289(x),
        l214_290(x),
        l214_291(x),
        l214_292(x),
        l214_293(x),
        l214_294(x),
        l214_295(x),
        l214_296(x),
        l214_297(x),
        l214_298(x),
        l214_299(x),
        l214_300(x),
        l214_301(x),
        l214_302(x),
        l214_303(x),
        l214_304(x),
        l214_305(x),
        l214_306(x),
        l214_307(x),
        l214_308(x),
        l214_309(x),
        l214_310(x),
        l214_311(x),
        l214_312(x),
        l214_313(x),
        l214_314(x),
        l214_315(x),
        l214_316(x),
        l214_317(x),
        l214_318(x),
        l214_319(x),
        l214_320(x),
        l214_321(x),
        l214_322(x),
        l214_323(x),
        l214_324(x),
        l214_325(x),
        l214_326(x),
        l214_327(x),
        l214_328(x),
        l214_329(x),
        l214_330(x),
        l214_331(x),
        l214_332(x),
        l214_333(x),
        l214_334(x),
        l214_335(x),
        l214_336(x),
        l214_337(x),
        l214_338(x),
        l214_339(x),
        l214_340(x),
        l214_341(x),
        l214_342(x),
        l214_343(x),
        l214_344(x),
        l214_345(x),
        l214_346(x),
        l214_347(x),
        l214_348(x),
        l214_349(x),
        l214_350(x),
        l214_351(x),
        l214_352(x),
        l214_353(x),
        l214_354(x),
        l214_355(x),
        l214_356(x),
        l214_357(x),
        l214_358(x),
        l214_359(x),
        l214_360(x),
        l214_361(x),
        l214_362(x),
        l214_363(x),
        l214_364(x),
        l214_365(x),
        l214_366(x),
        l214_367(x),
        l214_368(x),
        l214_369(x),
        l214_370(x),
        l214_371(x),
        l214_372(x),
        l214_373(x),
        l214_374(x),
        l214_375(x),
        l214_376(x),
        l214_377(x),
        l214_378(x),
        l214_379(x),
        l214_380(x),
        l214_381(x),
        l214_382(x),
        l214_383(x),
        l214_384(x),
        l214_385(x),
        l214_386(x),
        l214_387(x),
        l214_388(x),
        l214_389(x),
        l214_390(x),
        l214_391(x),
        l214_392(x),
        l214_393(x),
        l214_394(x),
        l214_395(x),
        l214_396(x),
        l214_397(x),
        l214_398(x),
        l214_399(x),
        l214_400(x),
        l214_401(x),
        l214_402(x),
        l214_403(x),
        l214_404(x),
        l214_405(x),
        l214_406(x),
        l214_407(x),
        l214_408(x),
        l214_409(x),
    ]