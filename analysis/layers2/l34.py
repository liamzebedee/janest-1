import numpy as np




# Generated from reverse engineering
def l34_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 336
    out = np.empty(336, dtype=np.float32)
    
    # for i in range(0, 128):
    for i in range(0, 128):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(128, 160):
    for i in range(0, 32):
        s = x[32 + i] + x[64 + i]
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 192):
    for i in range(0, 32):
        s = x[96 + i] + -1 * x[32 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(192, 193):
    for i in range(0, 1):
        s = x[156 + i]
        out[192 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(193, 194):
    for i in range(0, 1):
        s = x[152 + i]
        out[193 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(194, 195):
    for i in range(0, 1):
        s = x[148 + i]
        out[194 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(195, 196):
    for i in range(0, 1):
        s = x[144 + i]
        out[195 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(196, 197):
    for i in range(0, 1):
        s = x[140 + i]
        out[196 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(197, 198):
    for i in range(0, 1):
        s = x[136 + i]
        out[197 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(198, 199):
    for i in range(0, 1):
        s = x[132 + i]
        out[198 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(199, 200):
    for i in range(0, 1):
        s = x[128 + i]
        out[199 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(200, 201):
    for i in range(0, 1):
        s = x[157 + i]
        out[200 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(201, 202):
    for i in range(0, 1):
        s = x[153 + i]
        out[201 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(202, 203):
    for i in range(0, 1):
        s = x[149 + i]
        out[202 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(203, 204):
    for i in range(0, 1):
        s = x[145 + i]
        out[203 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(204, 205):
    for i in range(0, 1):
        s = x[141 + i]
        out[204 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(205, 206):
    for i in range(0, 1):
        s = x[137 + i]
        out[205 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(206, 207):
    for i in range(0, 1):
        s = x[133 + i]
        out[206 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(207, 208):
    for i in range(0, 1):
        s = x[129 + i]
        out[207 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(208, 209):
    for i in range(0, 1):
        s = x[158 + i]
        out[208 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(209, 210):
    for i in range(0, 1):
        s = x[154 + i]
        out[209 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(210, 211):
    for i in range(0, 1):
        s = x[150 + i]
        out[210 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(211, 212):
    for i in range(0, 1):
        s = x[146 + i]
        out[211 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(212, 213):
    for i in range(0, 1):
        s = x[142 + i]
        out[212 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(213, 214):
    for i in range(0, 1):
        s = x[138 + i]
        out[213 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(214, 215):
    for i in range(0, 1):
        s = x[134 + i]
        out[214 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(215, 216):
    for i in range(0, 1):
        s = x[130 + i]
        out[215 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(216, 217):
    for i in range(0, 1):
        s = x[159 + i]
        out[216 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(217, 218):
    for i in range(0, 1):
        s = x[155 + i]
        out[217 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(218, 219):
    for i in range(0, 1):
        s = x[151 + i]
        out[218 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(219, 220):
    for i in range(0, 1):
        s = x[147 + i]
        out[219 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(220, 221):
    for i in range(0, 1):
        s = x[143 + i]
        out[220 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(221, 222):
    for i in range(0, 1):
        s = x[139 + i]
        out[221 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(222, 223):
    for i in range(0, 1):
        s = x[135 + i]
        out[222 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(223, 224):
    for i in range(0, 1):
        s = x[131 + i]
        out[223 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x1e2556eb (len=32)
    biases = [0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0]
    # for i in range(224, 256):
    for i in range(0, 32):
        s = 0
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [128.0, 128.0, 128.0, 128.0]
    # for i in range(256, 260):
    for i in range(0, 4):
        s = -1 * x[164 + i]
        s += biases[i]
        out[256 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(260, 264):
    for i in range(0, 4):
        s = x[164 + i]
        out[260 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-127.0, -127.0, -127.0, -127.0]
    # for i in range(264, 268):
    for i in range(0, 4):
        s = x[164 + i]
        s += biases[i]
        out[264 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-128.0, -128.0, -128.0, -128.0]
    # for i in range(268, 272):
    for i in range(0, 4):
        s = x[164 + i]
        s += biases[i]
        out[268 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(272, 336):
    for i in range(0, 64):
        s = x[160 + i]
        out[272 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l34_0(x):
    # x is a list (or vector) of length 224
    return max(0, x[0])
def l34_1(x):
    # x is a list (or vector) of length 224
    return max(0, x[1])
def l34_2(x):
    # x is a list (or vector) of length 224
    return max(0, x[2])
def l34_3(x):
    # x is a list (or vector) of length 224
    return max(0, x[3])
def l34_4(x):
    # x is a list (or vector) of length 224
    return max(0, x[4])
def l34_5(x):
    # x is a list (or vector) of length 224
    return max(0, x[5])
def l34_6(x):
    # x is a list (or vector) of length 224
    return max(0, x[6])
def l34_7(x):
    # x is a list (or vector) of length 224
    return max(0, x[7])
def l34_8(x):
    # x is a list (or vector) of length 224
    return max(0, x[8])
def l34_9(x):
    # x is a list (or vector) of length 224
    return max(0, x[9])
def l34_10(x):
    # x is a list (or vector) of length 224
    return max(0, x[10])
def l34_11(x):
    # x is a list (or vector) of length 224
    return max(0, x[11])
def l34_12(x):
    # x is a list (or vector) of length 224
    return max(0, x[12])
def l34_13(x):
    # x is a list (or vector) of length 224
    return max(0, x[13])
def l34_14(x):
    # x is a list (or vector) of length 224
    return max(0, x[14])
def l34_15(x):
    # x is a list (or vector) of length 224
    return max(0, x[15])
def l34_16(x):
    # x is a list (or vector) of length 224
    return max(0, x[16])
def l34_17(x):
    # x is a list (or vector) of length 224
    return max(0, x[17])
def l34_18(x):
    # x is a list (or vector) of length 224
    return max(0, x[18])
def l34_19(x):
    # x is a list (or vector) of length 224
    return max(0, x[19])
def l34_20(x):
    # x is a list (or vector) of length 224
    return max(0, x[20])
def l34_21(x):
    # x is a list (or vector) of length 224
    return max(0, x[21])
def l34_22(x):
    # x is a list (or vector) of length 224
    return max(0, x[22])
def l34_23(x):
    # x is a list (or vector) of length 224
    return max(0, x[23])
def l34_24(x):
    # x is a list (or vector) of length 224
    return max(0, x[24])
def l34_25(x):
    # x is a list (or vector) of length 224
    return max(0, x[25])
def l34_26(x):
    # x is a list (or vector) of length 224
    return max(0, x[26])
def l34_27(x):
    # x is a list (or vector) of length 224
    return max(0, x[27])
def l34_28(x):
    # x is a list (or vector) of length 224
    return max(0, x[28])
def l34_29(x):
    # x is a list (or vector) of length 224
    return max(0, x[29])
def l34_30(x):
    # x is a list (or vector) of length 224
    return max(0, x[30])
def l34_31(x):
    # x is a list (or vector) of length 224
    return max(0, x[31])
def l34_32(x):
    # x is a list (or vector) of length 224
    return max(0, x[32])
def l34_33(x):
    # x is a list (or vector) of length 224
    return max(0, x[33])
def l34_34(x):
    # x is a list (or vector) of length 224
    return max(0, x[34])
def l34_35(x):
    # x is a list (or vector) of length 224
    return max(0, x[35])
def l34_36(x):
    # x is a list (or vector) of length 224
    return max(0, x[36])
def l34_37(x):
    # x is a list (or vector) of length 224
    return max(0, x[37])
def l34_38(x):
    # x is a list (or vector) of length 224
    return max(0, x[38])
def l34_39(x):
    # x is a list (or vector) of length 224
    return max(0, x[39])
def l34_40(x):
    # x is a list (or vector) of length 224
    return max(0, x[40])
def l34_41(x):
    # x is a list (or vector) of length 224
    return max(0, x[41])
def l34_42(x):
    # x is a list (or vector) of length 224
    return max(0, x[42])
def l34_43(x):
    # x is a list (or vector) of length 224
    return max(0, x[43])
def l34_44(x):
    # x is a list (or vector) of length 224
    return max(0, x[44])
def l34_45(x):
    # x is a list (or vector) of length 224
    return max(0, x[45])
def l34_46(x):
    # x is a list (or vector) of length 224
    return max(0, x[46])
def l34_47(x):
    # x is a list (or vector) of length 224
    return max(0, x[47])
def l34_48(x):
    # x is a list (or vector) of length 224
    return max(0, x[48])
def l34_49(x):
    # x is a list (or vector) of length 224
    return max(0, x[49])
def l34_50(x):
    # x is a list (or vector) of length 224
    return max(0, x[50])
def l34_51(x):
    # x is a list (or vector) of length 224
    return max(0, x[51])
def l34_52(x):
    # x is a list (or vector) of length 224
    return max(0, x[52])
def l34_53(x):
    # x is a list (or vector) of length 224
    return max(0, x[53])
def l34_54(x):
    # x is a list (or vector) of length 224
    return max(0, x[54])
def l34_55(x):
    # x is a list (or vector) of length 224
    return max(0, x[55])
def l34_56(x):
    # x is a list (or vector) of length 224
    return max(0, x[56])
def l34_57(x):
    # x is a list (or vector) of length 224
    return max(0, x[57])
def l34_58(x):
    # x is a list (or vector) of length 224
    return max(0, x[58])
def l34_59(x):
    # x is a list (or vector) of length 224
    return max(0, x[59])
def l34_60(x):
    # x is a list (or vector) of length 224
    return max(0, x[60])
def l34_61(x):
    # x is a list (or vector) of length 224
    return max(0, x[61])
def l34_62(x):
    # x is a list (or vector) of length 224
    return max(0, x[62])
def l34_63(x):
    # x is a list (or vector) of length 224
    return max(0, x[63])
def l34_64(x):
    # x is a list (or vector) of length 224
    return max(0, x[64])
def l34_65(x):
    # x is a list (or vector) of length 224
    return max(0, x[65])
def l34_66(x):
    # x is a list (or vector) of length 224
    return max(0, x[66])
def l34_67(x):
    # x is a list (or vector) of length 224
    return max(0, x[67])
def l34_68(x):
    # x is a list (or vector) of length 224
    return max(0, x[68])
def l34_69(x):
    # x is a list (or vector) of length 224
    return max(0, x[69])
def l34_70(x):
    # x is a list (or vector) of length 224
    return max(0, x[70])
def l34_71(x):
    # x is a list (or vector) of length 224
    return max(0, x[71])
def l34_72(x):
    # x is a list (or vector) of length 224
    return max(0, x[72])
def l34_73(x):
    # x is a list (or vector) of length 224
    return max(0, x[73])
def l34_74(x):
    # x is a list (or vector) of length 224
    return max(0, x[74])
def l34_75(x):
    # x is a list (or vector) of length 224
    return max(0, x[75])
def l34_76(x):
    # x is a list (or vector) of length 224
    return max(0, x[76])
def l34_77(x):
    # x is a list (or vector) of length 224
    return max(0, x[77])
def l34_78(x):
    # x is a list (or vector) of length 224
    return max(0, x[78])
def l34_79(x):
    # x is a list (or vector) of length 224
    return max(0, x[79])
def l34_80(x):
    # x is a list (or vector) of length 224
    return max(0, x[80])
def l34_81(x):
    # x is a list (or vector) of length 224
    return max(0, x[81])
def l34_82(x):
    # x is a list (or vector) of length 224
    return max(0, x[82])
def l34_83(x):
    # x is a list (or vector) of length 224
    return max(0, x[83])
def l34_84(x):
    # x is a list (or vector) of length 224
    return max(0, x[84])
def l34_85(x):
    # x is a list (or vector) of length 224
    return max(0, x[85])
def l34_86(x):
    # x is a list (or vector) of length 224
    return max(0, x[86])
def l34_87(x):
    # x is a list (or vector) of length 224
    return max(0, x[87])
def l34_88(x):
    # x is a list (or vector) of length 224
    return max(0, x[88])
def l34_89(x):
    # x is a list (or vector) of length 224
    return max(0, x[89])
def l34_90(x):
    # x is a list (or vector) of length 224
    return max(0, x[90])
def l34_91(x):
    # x is a list (or vector) of length 224
    return max(0, x[91])
def l34_92(x):
    # x is a list (or vector) of length 224
    return max(0, x[92])
def l34_93(x):
    # x is a list (or vector) of length 224
    return max(0, x[93])
def l34_94(x):
    # x is a list (or vector) of length 224
    return max(0, x[94])
def l34_95(x):
    # x is a list (or vector) of length 224
    return max(0, x[95])
def l34_96(x):
    # x is a list (or vector) of length 224
    return max(0, x[96])
def l34_97(x):
    # x is a list (or vector) of length 224
    return max(0, x[97])
def l34_98(x):
    # x is a list (or vector) of length 224
    return max(0, x[98])
def l34_99(x):
    # x is a list (or vector) of length 224
    return max(0, x[99])
def l34_100(x):
    # x is a list (or vector) of length 224
    return max(0, x[100])
def l34_101(x):
    # x is a list (or vector) of length 224
    return max(0, x[101])
def l34_102(x):
    # x is a list (or vector) of length 224
    return max(0, x[102])
def l34_103(x):
    # x is a list (or vector) of length 224
    return max(0, x[103])
def l34_104(x):
    # x is a list (or vector) of length 224
    return max(0, x[104])
def l34_105(x):
    # x is a list (or vector) of length 224
    return max(0, x[105])
def l34_106(x):
    # x is a list (or vector) of length 224
    return max(0, x[106])
def l34_107(x):
    # x is a list (or vector) of length 224
    return max(0, x[107])
def l34_108(x):
    # x is a list (or vector) of length 224
    return max(0, x[108])
def l34_109(x):
    # x is a list (or vector) of length 224
    return max(0, x[109])
def l34_110(x):
    # x is a list (or vector) of length 224
    return max(0, x[110])
def l34_111(x):
    # x is a list (or vector) of length 224
    return max(0, x[111])
def l34_112(x):
    # x is a list (or vector) of length 224
    return max(0, x[112])
def l34_113(x):
    # x is a list (or vector) of length 224
    return max(0, x[113])
def l34_114(x):
    # x is a list (or vector) of length 224
    return max(0, x[114])
def l34_115(x):
    # x is a list (or vector) of length 224
    return max(0, x[115])
def l34_116(x):
    # x is a list (or vector) of length 224
    return max(0, x[116])
def l34_117(x):
    # x is a list (or vector) of length 224
    return max(0, x[117])
def l34_118(x):
    # x is a list (or vector) of length 224
    return max(0, x[118])
def l34_119(x):
    # x is a list (or vector) of length 224
    return max(0, x[119])
def l34_120(x):
    # x is a list (or vector) of length 224
    return max(0, x[120])
def l34_121(x):
    # x is a list (or vector) of length 224
    return max(0, x[121])
def l34_122(x):
    # x is a list (or vector) of length 224
    return max(0, x[122])
def l34_123(x):
    # x is a list (or vector) of length 224
    return max(0, x[123])
def l34_124(x):
    # x is a list (or vector) of length 224
    return max(0, x[124])
def l34_125(x):
    # x is a list (or vector) of length 224
    return max(0, x[125])
def l34_126(x):
    # x is a list (or vector) of length 224
    return max(0, x[126])
def l34_127(x):
    # x is a list (or vector) of length 224
    return max(0, x[127])
def l34_128(x):
    # x is a list (or vector) of length 224
    return max(0, x[32] + x[64] + -1.0)
def l34_129(x):
    # x is a list (or vector) of length 224
    return max(0, x[33] + x[65] + -1.0)
def l34_130(x):
    # x is a list (or vector) of length 224
    return max(0, x[34] + x[66] + -1.0)
def l34_131(x):
    # x is a list (or vector) of length 224
    return max(0, x[35] + x[67] + -1.0)
def l34_132(x):
    # x is a list (or vector) of length 224
    return max(0, x[36] + x[68] + -1.0)
def l34_133(x):
    # x is a list (or vector) of length 224
    return max(0, x[37] + x[69] + -1.0)
def l34_134(x):
    # x is a list (or vector) of length 224
    return max(0, x[38] + x[70] + -1.0)
def l34_135(x):
    # x is a list (or vector) of length 224
    return max(0, x[39] + x[71] + -1.0)
def l34_136(x):
    # x is a list (or vector) of length 224
    return max(0, x[40] + x[72] + -1.0)
def l34_137(x):
    # x is a list (or vector) of length 224
    return max(0, x[41] + x[73] + -1.0)
def l34_138(x):
    # x is a list (or vector) of length 224
    return max(0, x[42] + x[74] + -1.0)
def l34_139(x):
    # x is a list (or vector) of length 224
    return max(0, x[43] + x[75] + -1.0)
def l34_140(x):
    # x is a list (or vector) of length 224
    return max(0, x[44] + x[76] + -1.0)
def l34_141(x):
    # x is a list (or vector) of length 224
    return max(0, x[45] + x[77] + -1.0)
def l34_142(x):
    # x is a list (or vector) of length 224
    return max(0, x[46] + x[78] + -1.0)
def l34_143(x):
    # x is a list (or vector) of length 224
    return max(0, x[47] + x[79] + -1.0)
def l34_144(x):
    # x is a list (or vector) of length 224
    return max(0, x[48] + x[80] + -1.0)
def l34_145(x):
    # x is a list (or vector) of length 224
    return max(0, x[49] + x[81] + -1.0)
def l34_146(x):
    # x is a list (or vector) of length 224
    return max(0, x[50] + x[82] + -1.0)
def l34_147(x):
    # x is a list (or vector) of length 224
    return max(0, x[51] + x[83] + -1.0)
def l34_148(x):
    # x is a list (or vector) of length 224
    return max(0, x[52] + x[84] + -1.0)
def l34_149(x):
    # x is a list (or vector) of length 224
    return max(0, x[53] + x[85] + -1.0)
def l34_150(x):
    # x is a list (or vector) of length 224
    return max(0, x[54] + x[86] + -1.0)
def l34_151(x):
    # x is a list (or vector) of length 224
    return max(0, x[55] + x[87] + -1.0)
def l34_152(x):
    # x is a list (or vector) of length 224
    return max(0, x[56] + x[88] + -1.0)
def l34_153(x):
    # x is a list (or vector) of length 224
    return max(0, x[57] + x[89] + -1.0)
def l34_154(x):
    # x is a list (or vector) of length 224
    return max(0, x[58] + x[90] + -1.0)
def l34_155(x):
    # x is a list (or vector) of length 224
    return max(0, x[59] + x[91] + -1.0)
def l34_156(x):
    # x is a list (or vector) of length 224
    return max(0, x[60] + x[92] + -1.0)
def l34_157(x):
    # x is a list (or vector) of length 224
    return max(0, x[61] + x[93] + -1.0)
def l34_158(x):
    # x is a list (or vector) of length 224
    return max(0, x[62] + x[94] + -1.0)
def l34_159(x):
    # x is a list (or vector) of length 224
    return max(0, x[63] + x[95] + -1.0)
def l34_160(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[32] + x[96])
def l34_161(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[33] + x[97])
def l34_162(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[34] + x[98])
def l34_163(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[35] + x[99])
def l34_164(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[36] + x[100])
def l34_165(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[37] + x[101])
def l34_166(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[38] + x[102])
def l34_167(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[39] + x[103])
def l34_168(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[40] + x[104])
def l34_169(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[41] + x[105])
def l34_170(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[42] + x[106])
def l34_171(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[43] + x[107])
def l34_172(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[44] + x[108])
def l34_173(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[45] + x[109])
def l34_174(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[46] + x[110])
def l34_175(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[47] + x[111])
def l34_176(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[48] + x[112])
def l34_177(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[49] + x[113])
def l34_178(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[50] + x[114])
def l34_179(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[51] + x[115])
def l34_180(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[52] + x[116])
def l34_181(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[53] + x[117])
def l34_182(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[54] + x[118])
def l34_183(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[55] + x[119])
def l34_184(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[56] + x[120])
def l34_185(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[57] + x[121])
def l34_186(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[58] + x[122])
def l34_187(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[59] + x[123])
def l34_188(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[60] + x[124])
def l34_189(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[61] + x[125])
def l34_190(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[62] + x[126])
def l34_191(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[63] + x[127])
def l34_192(x):
    # x is a list (or vector) of length 224
    return max(0, x[156])
def l34_193(x):
    # x is a list (or vector) of length 224
    return max(0, x[152])
def l34_194(x):
    # x is a list (or vector) of length 224
    return max(0, x[148])
def l34_195(x):
    # x is a list (or vector) of length 224
    return max(0, x[144])
def l34_196(x):
    # x is a list (or vector) of length 224
    return max(0, x[140])
def l34_197(x):
    # x is a list (or vector) of length 224
    return max(0, x[136])
def l34_198(x):
    # x is a list (or vector) of length 224
    return max(0, x[132])
def l34_199(x):
    # x is a list (or vector) of length 224
    return max(0, x[128])
def l34_200(x):
    # x is a list (or vector) of length 224
    return max(0, x[157])
def l34_201(x):
    # x is a list (or vector) of length 224
    return max(0, x[153])
def l34_202(x):
    # x is a list (or vector) of length 224
    return max(0, x[149])
def l34_203(x):
    # x is a list (or vector) of length 224
    return max(0, x[145])
def l34_204(x):
    # x is a list (or vector) of length 224
    return max(0, x[141])
def l34_205(x):
    # x is a list (or vector) of length 224
    return max(0, x[137])
def l34_206(x):
    # x is a list (or vector) of length 224
    return max(0, x[133])
def l34_207(x):
    # x is a list (or vector) of length 224
    return max(0, x[129])
def l34_208(x):
    # x is a list (or vector) of length 224
    return max(0, x[158])
def l34_209(x):
    # x is a list (or vector) of length 224
    return max(0, x[154])
def l34_210(x):
    # x is a list (or vector) of length 224
    return max(0, x[150])
def l34_211(x):
    # x is a list (or vector) of length 224
    return max(0, x[146])
def l34_212(x):
    # x is a list (or vector) of length 224
    return max(0, x[142])
def l34_213(x):
    # x is a list (or vector) of length 224
    return max(0, x[138])
def l34_214(x):
    # x is a list (or vector) of length 224
    return max(0, x[134])
def l34_215(x):
    # x is a list (or vector) of length 224
    return max(0, x[130])
def l34_216(x):
    # x is a list (or vector) of length 224
    return max(0, x[159])
def l34_217(x):
    # x is a list (or vector) of length 224
    return max(0, x[155])
def l34_218(x):
    # x is a list (or vector) of length 224
    return max(0, x[151])
def l34_219(x):
    # x is a list (or vector) of length 224
    return max(0, x[147])
def l34_220(x):
    # x is a list (or vector) of length 224
    return max(0, x[143])
def l34_221(x):
    # x is a list (or vector) of length 224
    return max(0, x[139])
def l34_222(x):
    # x is a list (or vector) of length 224
    return max(0, x[135])
def l34_223(x):
    # x is a list (or vector) of length 224
    return max(0, x[131])
def l34_224(x):
    # x is a list (or vector) of length 224
    return max(0, 0)
def l34_225(x):
    # x is a list (or vector) of length 224
    return max(0, 0)
def l34_226(x):
    # x is a list (or vector) of length 224
    return max(0, 0)
def l34_227(x):
    # x is a list (or vector) of length 224
    return max(0, 1.0)
def l34_228(x):
    # x is a list (or vector) of length 224
    return max(0, 1.0)
def l34_229(x):
    # x is a list (or vector) of length 224
    return max(0, 1.0)
def l34_230(x):
    # x is a list (or vector) of length 224
    return max(0, 1.0)
def l34_231(x):
    # x is a list (or vector) of length 224
    return max(0, 0)
def l34_232(x):
    # x is a list (or vector) of length 224
    return max(0, 0)
def l34_233(x):
    # x is a list (or vector) of length 224
    return max(0, 0)
def l34_234(x):
    # x is a list (or vector) of length 224
    return max(0, 1.0)
def l34_235(x):
    # x is a list (or vector) of length 224
    return max(0, 0)
def l34_236(x):
    # x is a list (or vector) of length 224
    return max(0, 0)
def l34_237(x):
    # x is a list (or vector) of length 224
    return max(0, 1.0)
def l34_238(x):
    # x is a list (or vector) of length 224
    return max(0, 0)
def l34_239(x):
    # x is a list (or vector) of length 224
    return max(0, 1.0)
def l34_240(x):
    # x is a list (or vector) of length 224
    return max(0, 0)
def l34_241(x):
    # x is a list (or vector) of length 224
    return max(0, 1.0)
def l34_242(x):
    # x is a list (or vector) of length 224
    return max(0, 0)
def l34_243(x):
    # x is a list (or vector) of length 224
    return max(0, 1.0)
def l34_244(x):
    # x is a list (or vector) of length 224
    return max(0, 0)
def l34_245(x):
    # x is a list (or vector) of length 224
    return max(0, 1.0)
def l34_246(x):
    # x is a list (or vector) of length 224
    return max(0, 1.0)
def l34_247(x):
    # x is a list (or vector) of length 224
    return max(0, 0)
def l34_248(x):
    # x is a list (or vector) of length 224
    return max(0, 1.0)
def l34_249(x):
    # x is a list (or vector) of length 224
    return max(0, 1.0)
def l34_250(x):
    # x is a list (or vector) of length 224
    return max(0, 1.0)
def l34_251(x):
    # x is a list (or vector) of length 224
    return max(0, 0)
def l34_252(x):
    # x is a list (or vector) of length 224
    return max(0, 1.0)
def l34_253(x):
    # x is a list (or vector) of length 224
    return max(0, 0)
def l34_254(x):
    # x is a list (or vector) of length 224
    return max(0, 1.0)
def l34_255(x):
    # x is a list (or vector) of length 224
    return max(0, 1.0)
def l34_256(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[164] + 128.0)
def l34_257(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[165] + 128.0)
def l34_258(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[166] + 128.0)
def l34_259(x):
    # x is a list (or vector) of length 224
    return max(0, -1.0*x[167] + 128.0)
def l34_260(x):
    # x is a list (or vector) of length 224
    return max(0, x[164])
def l34_261(x):
    # x is a list (or vector) of length 224
    return max(0, x[165])
def l34_262(x):
    # x is a list (or vector) of length 224
    return max(0, x[166])
def l34_263(x):
    # x is a list (or vector) of length 224
    return max(0, x[167])
def l34_264(x):
    # x is a list (or vector) of length 224
    return max(0, x[164] + -127.0)
def l34_265(x):
    # x is a list (or vector) of length 224
    return max(0, x[165] + -127.0)
def l34_266(x):
    # x is a list (or vector) of length 224
    return max(0, x[166] + -127.0)
def l34_267(x):
    # x is a list (or vector) of length 224
    return max(0, x[167] + -127.0)
def l34_268(x):
    # x is a list (or vector) of length 224
    return max(0, x[164] + -128.0)
def l34_269(x):
    # x is a list (or vector) of length 224
    return max(0, x[165] + -128.0)
def l34_270(x):
    # x is a list (or vector) of length 224
    return max(0, x[166] + -128.0)
def l34_271(x):
    # x is a list (or vector) of length 224
    return max(0, x[167] + -128.0)
def l34_272(x):
    # x is a list (or vector) of length 224
    return max(0, x[160])
def l34_273(x):
    # x is a list (or vector) of length 224
    return max(0, x[161])
def l34_274(x):
    # x is a list (or vector) of length 224
    return max(0, x[162])
def l34_275(x):
    # x is a list (or vector) of length 224
    return max(0, x[163])
def l34_276(x):
    # x is a list (or vector) of length 224
    return max(0, x[164])
def l34_277(x):
    # x is a list (or vector) of length 224
    return max(0, x[165])
def l34_278(x):
    # x is a list (or vector) of length 224
    return max(0, x[166])
def l34_279(x):
    # x is a list (or vector) of length 224
    return max(0, x[167])
def l34_280(x):
    # x is a list (or vector) of length 224
    return max(0, x[168])
def l34_281(x):
    # x is a list (or vector) of length 224
    return max(0, x[169])
def l34_282(x):
    # x is a list (or vector) of length 224
    return max(0, x[170])
def l34_283(x):
    # x is a list (or vector) of length 224
    return max(0, x[171])
def l34_284(x):
    # x is a list (or vector) of length 224
    return max(0, x[172])
def l34_285(x):
    # x is a list (or vector) of length 224
    return max(0, x[173])
def l34_286(x):
    # x is a list (or vector) of length 224
    return max(0, x[174])
def l34_287(x):
    # x is a list (or vector) of length 224
    return max(0, x[175])
def l34_288(x):
    # x is a list (or vector) of length 224
    return max(0, x[176])
def l34_289(x):
    # x is a list (or vector) of length 224
    return max(0, x[177])
def l34_290(x):
    # x is a list (or vector) of length 224
    return max(0, x[178])
def l34_291(x):
    # x is a list (or vector) of length 224
    return max(0, x[179])
def l34_292(x):
    # x is a list (or vector) of length 224
    return max(0, x[180])
def l34_293(x):
    # x is a list (or vector) of length 224
    return max(0, x[181])
def l34_294(x):
    # x is a list (or vector) of length 224
    return max(0, x[182])
def l34_295(x):
    # x is a list (or vector) of length 224
    return max(0, x[183])
def l34_296(x):
    # x is a list (or vector) of length 224
    return max(0, x[184])
def l34_297(x):
    # x is a list (or vector) of length 224
    return max(0, x[185])
def l34_298(x):
    # x is a list (or vector) of length 224
    return max(0, x[186])
def l34_299(x):
    # x is a list (or vector) of length 224
    return max(0, x[187])
def l34_300(x):
    # x is a list (or vector) of length 224
    return max(0, x[188])
def l34_301(x):
    # x is a list (or vector) of length 224
    return max(0, x[189])
def l34_302(x):
    # x is a list (or vector) of length 224
    return max(0, x[190])
def l34_303(x):
    # x is a list (or vector) of length 224
    return max(0, x[191])
def l34_304(x):
    # x is a list (or vector) of length 224
    return max(0, x[192])
def l34_305(x):
    # x is a list (or vector) of length 224
    return max(0, x[193])
def l34_306(x):
    # x is a list (or vector) of length 224
    return max(0, x[194])
def l34_307(x):
    # x is a list (or vector) of length 224
    return max(0, x[195])
def l34_308(x):
    # x is a list (or vector) of length 224
    return max(0, x[196])
def l34_309(x):
    # x is a list (or vector) of length 224
    return max(0, x[197])
def l34_310(x):
    # x is a list (or vector) of length 224
    return max(0, x[198])
def l34_311(x):
    # x is a list (or vector) of length 224
    return max(0, x[199])
def l34_312(x):
    # x is a list (or vector) of length 224
    return max(0, x[200])
def l34_313(x):
    # x is a list (or vector) of length 224
    return max(0, x[201])
def l34_314(x):
    # x is a list (or vector) of length 224
    return max(0, x[202])
def l34_315(x):
    # x is a list (or vector) of length 224
    return max(0, x[203])
def l34_316(x):
    # x is a list (or vector) of length 224
    return max(0, x[204])
def l34_317(x):
    # x is a list (or vector) of length 224
    return max(0, x[205])
def l34_318(x):
    # x is a list (or vector) of length 224
    return max(0, x[206])
def l34_319(x):
    # x is a list (or vector) of length 224
    return max(0, x[207])
def l34_320(x):
    # x is a list (or vector) of length 224
    return max(0, x[208])
def l34_321(x):
    # x is a list (or vector) of length 224
    return max(0, x[209])
def l34_322(x):
    # x is a list (or vector) of length 224
    return max(0, x[210])
def l34_323(x):
    # x is a list (or vector) of length 224
    return max(0, x[211])
def l34_324(x):
    # x is a list (or vector) of length 224
    return max(0, x[212])
def l34_325(x):
    # x is a list (or vector) of length 224
    return max(0, x[213])
def l34_326(x):
    # x is a list (or vector) of length 224
    return max(0, x[214])
def l34_327(x):
    # x is a list (or vector) of length 224
    return max(0, x[215])
def l34_328(x):
    # x is a list (or vector) of length 224
    return max(0, x[216])
def l34_329(x):
    # x is a list (or vector) of length 224
    return max(0, x[217])
def l34_330(x):
    # x is a list (or vector) of length 224
    return max(0, x[218])
def l34_331(x):
    # x is a list (or vector) of length 224
    return max(0, x[219])
def l34_332(x):
    # x is a list (or vector) of length 224
    return max(0, x[220])
def l34_333(x):
    # x is a list (or vector) of length 224
    return max(0, x[221])
def l34_334(x):
    # x is a list (or vector) of length 224
    return max(0, x[222])
def l34_335(x):
    # x is a list (or vector) of length 224
    return max(0, x[223])
def l34_(x):
    # x is a list (or vector) of length 224
    return [
        l34_0(x),
        l34_1(x),
        l34_2(x),
        l34_3(x),
        l34_4(x),
        l34_5(x),
        l34_6(x),
        l34_7(x),
        l34_8(x),
        l34_9(x),
        l34_10(x),
        l34_11(x),
        l34_12(x),
        l34_13(x),
        l34_14(x),
        l34_15(x),
        l34_16(x),
        l34_17(x),
        l34_18(x),
        l34_19(x),
        l34_20(x),
        l34_21(x),
        l34_22(x),
        l34_23(x),
        l34_24(x),
        l34_25(x),
        l34_26(x),
        l34_27(x),
        l34_28(x),
        l34_29(x),
        l34_30(x),
        l34_31(x),
        l34_32(x),
        l34_33(x),
        l34_34(x),
        l34_35(x),
        l34_36(x),
        l34_37(x),
        l34_38(x),
        l34_39(x),
        l34_40(x),
        l34_41(x),
        l34_42(x),
        l34_43(x),
        l34_44(x),
        l34_45(x),
        l34_46(x),
        l34_47(x),
        l34_48(x),
        l34_49(x),
        l34_50(x),
        l34_51(x),
        l34_52(x),
        l34_53(x),
        l34_54(x),
        l34_55(x),
        l34_56(x),
        l34_57(x),
        l34_58(x),
        l34_59(x),
        l34_60(x),
        l34_61(x),
        l34_62(x),
        l34_63(x),
        l34_64(x),
        l34_65(x),
        l34_66(x),
        l34_67(x),
        l34_68(x),
        l34_69(x),
        l34_70(x),
        l34_71(x),
        l34_72(x),
        l34_73(x),
        l34_74(x),
        l34_75(x),
        l34_76(x),
        l34_77(x),
        l34_78(x),
        l34_79(x),
        l34_80(x),
        l34_81(x),
        l34_82(x),
        l34_83(x),
        l34_84(x),
        l34_85(x),
        l34_86(x),
        l34_87(x),
        l34_88(x),
        l34_89(x),
        l34_90(x),
        l34_91(x),
        l34_92(x),
        l34_93(x),
        l34_94(x),
        l34_95(x),
        l34_96(x),
        l34_97(x),
        l34_98(x),
        l34_99(x),
        l34_100(x),
        l34_101(x),
        l34_102(x),
        l34_103(x),
        l34_104(x),
        l34_105(x),
        l34_106(x),
        l34_107(x),
        l34_108(x),
        l34_109(x),
        l34_110(x),
        l34_111(x),
        l34_112(x),
        l34_113(x),
        l34_114(x),
        l34_115(x),
        l34_116(x),
        l34_117(x),
        l34_118(x),
        l34_119(x),
        l34_120(x),
        l34_121(x),
        l34_122(x),
        l34_123(x),
        l34_124(x),
        l34_125(x),
        l34_126(x),
        l34_127(x),
        l34_128(x),
        l34_129(x),
        l34_130(x),
        l34_131(x),
        l34_132(x),
        l34_133(x),
        l34_134(x),
        l34_135(x),
        l34_136(x),
        l34_137(x),
        l34_138(x),
        l34_139(x),
        l34_140(x),
        l34_141(x),
        l34_142(x),
        l34_143(x),
        l34_144(x),
        l34_145(x),
        l34_146(x),
        l34_147(x),
        l34_148(x),
        l34_149(x),
        l34_150(x),
        l34_151(x),
        l34_152(x),
        l34_153(x),
        l34_154(x),
        l34_155(x),
        l34_156(x),
        l34_157(x),
        l34_158(x),
        l34_159(x),
        l34_160(x),
        l34_161(x),
        l34_162(x),
        l34_163(x),
        l34_164(x),
        l34_165(x),
        l34_166(x),
        l34_167(x),
        l34_168(x),
        l34_169(x),
        l34_170(x),
        l34_171(x),
        l34_172(x),
        l34_173(x),
        l34_174(x),
        l34_175(x),
        l34_176(x),
        l34_177(x),
        l34_178(x),
        l34_179(x),
        l34_180(x),
        l34_181(x),
        l34_182(x),
        l34_183(x),
        l34_184(x),
        l34_185(x),
        l34_186(x),
        l34_187(x),
        l34_188(x),
        l34_189(x),
        l34_190(x),
        l34_191(x),
        l34_192(x),
        l34_193(x),
        l34_194(x),
        l34_195(x),
        l34_196(x),
        l34_197(x),
        l34_198(x),
        l34_199(x),
        l34_200(x),
        l34_201(x),
        l34_202(x),
        l34_203(x),
        l34_204(x),
        l34_205(x),
        l34_206(x),
        l34_207(x),
        l34_208(x),
        l34_209(x),
        l34_210(x),
        l34_211(x),
        l34_212(x),
        l34_213(x),
        l34_214(x),
        l34_215(x),
        l34_216(x),
        l34_217(x),
        l34_218(x),
        l34_219(x),
        l34_220(x),
        l34_221(x),
        l34_222(x),
        l34_223(x),
        l34_224(x),
        l34_225(x),
        l34_226(x),
        l34_227(x),
        l34_228(x),
        l34_229(x),
        l34_230(x),
        l34_231(x),
        l34_232(x),
        l34_233(x),
        l34_234(x),
        l34_235(x),
        l34_236(x),
        l34_237(x),
        l34_238(x),
        l34_239(x),
        l34_240(x),
        l34_241(x),
        l34_242(x),
        l34_243(x),
        l34_244(x),
        l34_245(x),
        l34_246(x),
        l34_247(x),
        l34_248(x),
        l34_249(x),
        l34_250(x),
        l34_251(x),
        l34_252(x),
        l34_253(x),
        l34_254(x),
        l34_255(x),
        l34_256(x),
        l34_257(x),
        l34_258(x),
        l34_259(x),
        l34_260(x),
        l34_261(x),
        l34_262(x),
        l34_263(x),
        l34_264(x),
        l34_265(x),
        l34_266(x),
        l34_267(x),
        l34_268(x),
        l34_269(x),
        l34_270(x),
        l34_271(x),
        l34_272(x),
        l34_273(x),
        l34_274(x),
        l34_275(x),
        l34_276(x),
        l34_277(x),
        l34_278(x),
        l34_279(x),
        l34_280(x),
        l34_281(x),
        l34_282(x),
        l34_283(x),
        l34_284(x),
        l34_285(x),
        l34_286(x),
        l34_287(x),
        l34_288(x),
        l34_289(x),
        l34_290(x),
        l34_291(x),
        l34_292(x),
        l34_293(x),
        l34_294(x),
        l34_295(x),
        l34_296(x),
        l34_297(x),
        l34_298(x),
        l34_299(x),
        l34_300(x),
        l34_301(x),
        l34_302(x),
        l34_303(x),
        l34_304(x),
        l34_305(x),
        l34_306(x),
        l34_307(x),
        l34_308(x),
        l34_309(x),
        l34_310(x),
        l34_311(x),
        l34_312(x),
        l34_313(x),
        l34_314(x),
        l34_315(x),
        l34_316(x),
        l34_317(x),
        l34_318(x),
        l34_319(x),
        l34_320(x),
        l34_321(x),
        l34_322(x),
        l34_323(x),
        l34_324(x),
        l34_325(x),
        l34_326(x),
        l34_327(x),
        l34_328(x),
        l34_329(x),
        l34_330(x),
        l34_331(x),
        l34_332(x),
        l34_333(x),
        l34_334(x),
        l34_335(x),
    ]