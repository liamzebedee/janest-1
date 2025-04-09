import numpy as np




# Generated from reverse engineering
def l398_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 352
    out = np.empty(352, dtype=np.float32)
    
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
        
    # for i in range(160, 192):
    for i in range(0, 32):
        s = x[176 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(192, 193):
    for i in range(0, 1):
        s = x[272 + i]
        out[192 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(193, 209):
    for i in range(0, 16):
        s = x[208 + i] + x[273 + i]
        out[193 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x7fff (len=15)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(209, 224):
    for i in range(0, 15):
        s = x[289 + i] + -1 * x[224 + i]
        s += biases[i]
        out[209 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0]
    # for i in range(224, 225):
    for i in range(0, 1):
        s = x[272 + i]
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(225, 241):
    for i in range(0, 16):
        s = x[208 + i] + x[273 + i]
        s += biases[i]
        out[225 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(241, 256):
    for i in range(0, 15):
        s = x[289 + i] + -1 * x[224 + i]
        out[241 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(256, 257):
    for i in range(0, 1):
        s = x[332 + i]
        out[256 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(257, 258):
    for i in range(0, 1):
        s = x[328 + i]
        out[257 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(258, 259):
    for i in range(0, 1):
        s = x[324 + i]
        out[258 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(259, 260):
    for i in range(0, 1):
        s = x[320 + i]
        out[259 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(260, 261):
    for i in range(0, 1):
        s = x[316 + i]
        out[260 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(261, 262):
    for i in range(0, 1):
        s = x[312 + i]
        out[261 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(262, 263):
    for i in range(0, 1):
        s = x[308 + i]
        out[262 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(263, 264):
    for i in range(0, 1):
        s = x[304 + i]
        out[263 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(264, 265):
    for i in range(0, 1):
        s = x[333 + i]
        out[264 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(265, 266):
    for i in range(0, 1):
        s = x[329 + i]
        out[265 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(266, 267):
    for i in range(0, 1):
        s = x[325 + i]
        out[266 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(267, 268):
    for i in range(0, 1):
        s = x[321 + i]
        out[267 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(268, 269):
    for i in range(0, 1):
        s = x[317 + i]
        out[268 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(269, 270):
    for i in range(0, 1):
        s = x[313 + i]
        out[269 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(270, 271):
    for i in range(0, 1):
        s = x[309 + i]
        out[270 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(271, 272):
    for i in range(0, 1):
        s = x[305 + i]
        out[271 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(272, 273):
    for i in range(0, 1):
        s = x[334 + i]
        out[272 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(273, 274):
    for i in range(0, 1):
        s = x[330 + i]
        out[273 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(274, 275):
    for i in range(0, 1):
        s = x[326 + i]
        out[274 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(275, 276):
    for i in range(0, 1):
        s = x[322 + i]
        out[275 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(276, 277):
    for i in range(0, 1):
        s = x[318 + i]
        out[276 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(277, 278):
    for i in range(0, 1):
        s = x[314 + i]
        out[277 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(278, 279):
    for i in range(0, 1):
        s = x[310 + i]
        out[278 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(279, 280):
    for i in range(0, 1):
        s = x[306 + i]
        out[279 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(280, 281):
    for i in range(0, 1):
        s = x[335 + i]
        out[280 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(281, 282):
    for i in range(0, 1):
        s = x[331 + i]
        out[281 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(282, 283):
    for i in range(0, 1):
        s = x[327 + i]
        out[282 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(283, 284):
    for i in range(0, 1):
        s = x[323 + i]
        out[283 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(284, 285):
    for i in range(0, 1):
        s = x[319 + i]
        out[284 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(285, 286):
    for i in range(0, 1):
        s = x[315 + i]
        out[285 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(286, 287):
    for i in range(0, 1):
        s = x[311 + i]
        out[286 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(287, 288):
    for i in range(0, 1):
        s = x[307 + i]
        out[287 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(288, 352):
    for i in range(0, 64):
        s = x[336 + i]
        out[288 + i] = s if s > 0 else 0.0 # ReLu
        
    return out




def l398_0(x):
    # x is a list (or vector) of length 400
    return max(0, x[0])
def l398_1(x):
    # x is a list (or vector) of length 400
    return max(0, x[1])
def l398_2(x):
    # x is a list (or vector) of length 400
    return max(0, x[2])
def l398_3(x):
    # x is a list (or vector) of length 400
    return max(0, x[3])
def l398_4(x):
    # x is a list (or vector) of length 400
    return max(0, x[4])
def l398_5(x):
    # x is a list (or vector) of length 400
    return max(0, x[5])
def l398_6(x):
    # x is a list (or vector) of length 400
    return max(0, x[6])
def l398_7(x):
    # x is a list (or vector) of length 400
    return max(0, x[7])
def l398_8(x):
    # x is a list (or vector) of length 400
    return max(0, x[8])
def l398_9(x):
    # x is a list (or vector) of length 400
    return max(0, x[9])
def l398_10(x):
    # x is a list (or vector) of length 400
    return max(0, x[10])
def l398_11(x):
    # x is a list (or vector) of length 400
    return max(0, x[11])
def l398_12(x):
    # x is a list (or vector) of length 400
    return max(0, x[12])
def l398_13(x):
    # x is a list (or vector) of length 400
    return max(0, x[13])
def l398_14(x):
    # x is a list (or vector) of length 400
    return max(0, x[14])
def l398_15(x):
    # x is a list (or vector) of length 400
    return max(0, x[15])
def l398_16(x):
    # x is a list (or vector) of length 400
    return max(0, x[16])
def l398_17(x):
    # x is a list (or vector) of length 400
    return max(0, x[17])
def l398_18(x):
    # x is a list (or vector) of length 400
    return max(0, x[18])
def l398_19(x):
    # x is a list (or vector) of length 400
    return max(0, x[19])
def l398_20(x):
    # x is a list (or vector) of length 400
    return max(0, x[20])
def l398_21(x):
    # x is a list (or vector) of length 400
    return max(0, x[21])
def l398_22(x):
    # x is a list (or vector) of length 400
    return max(0, x[22])
def l398_23(x):
    # x is a list (or vector) of length 400
    return max(0, x[23])
def l398_24(x):
    # x is a list (or vector) of length 400
    return max(0, x[24])
def l398_25(x):
    # x is a list (or vector) of length 400
    return max(0, x[25])
def l398_26(x):
    # x is a list (or vector) of length 400
    return max(0, x[26])
def l398_27(x):
    # x is a list (or vector) of length 400
    return max(0, x[27])
def l398_28(x):
    # x is a list (or vector) of length 400
    return max(0, x[28])
def l398_29(x):
    # x is a list (or vector) of length 400
    return max(0, x[29])
def l398_30(x):
    # x is a list (or vector) of length 400
    return max(0, x[30])
def l398_31(x):
    # x is a list (or vector) of length 400
    return max(0, x[31])
def l398_32(x):
    # x is a list (or vector) of length 400
    return max(0, x[32])
def l398_33(x):
    # x is a list (or vector) of length 400
    return max(0, x[33])
def l398_34(x):
    # x is a list (or vector) of length 400
    return max(0, x[34])
def l398_35(x):
    # x is a list (or vector) of length 400
    return max(0, x[35])
def l398_36(x):
    # x is a list (or vector) of length 400
    return max(0, x[36])
def l398_37(x):
    # x is a list (or vector) of length 400
    return max(0, x[37])
def l398_38(x):
    # x is a list (or vector) of length 400
    return max(0, x[38])
def l398_39(x):
    # x is a list (or vector) of length 400
    return max(0, x[39])
def l398_40(x):
    # x is a list (or vector) of length 400
    return max(0, x[40])
def l398_41(x):
    # x is a list (or vector) of length 400
    return max(0, x[41])
def l398_42(x):
    # x is a list (or vector) of length 400
    return max(0, x[42])
def l398_43(x):
    # x is a list (or vector) of length 400
    return max(0, x[43])
def l398_44(x):
    # x is a list (or vector) of length 400
    return max(0, x[44])
def l398_45(x):
    # x is a list (or vector) of length 400
    return max(0, x[45])
def l398_46(x):
    # x is a list (or vector) of length 400
    return max(0, x[46])
def l398_47(x):
    # x is a list (or vector) of length 400
    return max(0, x[47])
def l398_48(x):
    # x is a list (or vector) of length 400
    return max(0, x[48])
def l398_49(x):
    # x is a list (or vector) of length 400
    return max(0, x[49])
def l398_50(x):
    # x is a list (or vector) of length 400
    return max(0, x[50])
def l398_51(x):
    # x is a list (or vector) of length 400
    return max(0, x[51])
def l398_52(x):
    # x is a list (or vector) of length 400
    return max(0, x[52])
def l398_53(x):
    # x is a list (or vector) of length 400
    return max(0, x[53])
def l398_54(x):
    # x is a list (or vector) of length 400
    return max(0, x[54])
def l398_55(x):
    # x is a list (or vector) of length 400
    return max(0, x[55])
def l398_56(x):
    # x is a list (or vector) of length 400
    return max(0, x[56])
def l398_57(x):
    # x is a list (or vector) of length 400
    return max(0, x[57])
def l398_58(x):
    # x is a list (or vector) of length 400
    return max(0, x[58])
def l398_59(x):
    # x is a list (or vector) of length 400
    return max(0, x[59])
def l398_60(x):
    # x is a list (or vector) of length 400
    return max(0, x[60])
def l398_61(x):
    # x is a list (or vector) of length 400
    return max(0, x[61])
def l398_62(x):
    # x is a list (or vector) of length 400
    return max(0, x[62])
def l398_63(x):
    # x is a list (or vector) of length 400
    return max(0, x[63])
def l398_64(x):
    # x is a list (or vector) of length 400
    return max(0, x[64])
def l398_65(x):
    # x is a list (or vector) of length 400
    return max(0, x[65])
def l398_66(x):
    # x is a list (or vector) of length 400
    return max(0, x[66])
def l398_67(x):
    # x is a list (or vector) of length 400
    return max(0, x[67])
def l398_68(x):
    # x is a list (or vector) of length 400
    return max(0, x[68])
def l398_69(x):
    # x is a list (or vector) of length 400
    return max(0, x[69])
def l398_70(x):
    # x is a list (or vector) of length 400
    return max(0, x[70])
def l398_71(x):
    # x is a list (or vector) of length 400
    return max(0, x[71])
def l398_72(x):
    # x is a list (or vector) of length 400
    return max(0, x[72])
def l398_73(x):
    # x is a list (or vector) of length 400
    return max(0, x[73])
def l398_74(x):
    # x is a list (or vector) of length 400
    return max(0, x[74])
def l398_75(x):
    # x is a list (or vector) of length 400
    return max(0, x[75])
def l398_76(x):
    # x is a list (or vector) of length 400
    return max(0, x[76])
def l398_77(x):
    # x is a list (or vector) of length 400
    return max(0, x[77])
def l398_78(x):
    # x is a list (or vector) of length 400
    return max(0, x[78])
def l398_79(x):
    # x is a list (or vector) of length 400
    return max(0, x[79])
def l398_80(x):
    # x is a list (or vector) of length 400
    return max(0, x[80])
def l398_81(x):
    # x is a list (or vector) of length 400
    return max(0, x[81])
def l398_82(x):
    # x is a list (or vector) of length 400
    return max(0, x[82])
def l398_83(x):
    # x is a list (or vector) of length 400
    return max(0, x[83])
def l398_84(x):
    # x is a list (or vector) of length 400
    return max(0, x[84])
def l398_85(x):
    # x is a list (or vector) of length 400
    return max(0, x[85])
def l398_86(x):
    # x is a list (or vector) of length 400
    return max(0, x[86])
def l398_87(x):
    # x is a list (or vector) of length 400
    return max(0, x[87])
def l398_88(x):
    # x is a list (or vector) of length 400
    return max(0, x[88])
def l398_89(x):
    # x is a list (or vector) of length 400
    return max(0, x[89])
def l398_90(x):
    # x is a list (or vector) of length 400
    return max(0, x[90])
def l398_91(x):
    # x is a list (or vector) of length 400
    return max(0, x[91])
def l398_92(x):
    # x is a list (or vector) of length 400
    return max(0, x[92])
def l398_93(x):
    # x is a list (or vector) of length 400
    return max(0, x[93])
def l398_94(x):
    # x is a list (or vector) of length 400
    return max(0, x[94])
def l398_95(x):
    # x is a list (or vector) of length 400
    return max(0, x[95])
def l398_96(x):
    # x is a list (or vector) of length 400
    return max(0, x[96])
def l398_97(x):
    # x is a list (or vector) of length 400
    return max(0, x[97])
def l398_98(x):
    # x is a list (or vector) of length 400
    return max(0, x[98])
def l398_99(x):
    # x is a list (or vector) of length 400
    return max(0, x[99])
def l398_100(x):
    # x is a list (or vector) of length 400
    return max(0, x[100])
def l398_101(x):
    # x is a list (or vector) of length 400
    return max(0, x[101])
def l398_102(x):
    # x is a list (or vector) of length 400
    return max(0, x[102])
def l398_103(x):
    # x is a list (or vector) of length 400
    return max(0, x[103])
def l398_104(x):
    # x is a list (or vector) of length 400
    return max(0, x[104])
def l398_105(x):
    # x is a list (or vector) of length 400
    return max(0, x[105])
def l398_106(x):
    # x is a list (or vector) of length 400
    return max(0, x[106])
def l398_107(x):
    # x is a list (or vector) of length 400
    return max(0, x[107])
def l398_108(x):
    # x is a list (or vector) of length 400
    return max(0, x[108])
def l398_109(x):
    # x is a list (or vector) of length 400
    return max(0, x[109])
def l398_110(x):
    # x is a list (or vector) of length 400
    return max(0, x[110])
def l398_111(x):
    # x is a list (or vector) of length 400
    return max(0, x[111])
def l398_112(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[112] + -1.0*x[128] + 1.0)
def l398_113(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[113] + -1.0*x[129] + 1.0)
def l398_114(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[114] + -1.0*x[130] + 1.0)
def l398_115(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[115] + -1.0*x[131] + 1.0)
def l398_116(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[116] + -1.0*x[132] + 1.0)
def l398_117(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[117] + -1.0*x[133] + 1.0)
def l398_118(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[118] + -1.0*x[134] + 1.0)
def l398_119(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[119] + -1.0*x[135] + 1.0)
def l398_120(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[120] + -1.0*x[136] + 1.0)
def l398_121(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[121] + -1.0*x[137] + 1.0)
def l398_122(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[122] + -1.0*x[138] + 1.0)
def l398_123(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[123] + -1.0*x[139] + 1.0)
def l398_124(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[124] + -1.0*x[140] + 1.0)
def l398_125(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[125] + -1.0*x[141] + 1.0)
def l398_126(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[126] + -1.0*x[142] + 1.0)
def l398_127(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[127] + -1.0*x[143] + 1.0)
def l398_128(x):
    # x is a list (or vector) of length 400
    return max(0, x[160])
def l398_129(x):
    # x is a list (or vector) of length 400
    return max(0, x[161])
def l398_130(x):
    # x is a list (or vector) of length 400
    return max(0, x[162])
def l398_131(x):
    # x is a list (or vector) of length 400
    return max(0, x[163])
def l398_132(x):
    # x is a list (or vector) of length 400
    return max(0, x[164])
def l398_133(x):
    # x is a list (or vector) of length 400
    return max(0, x[165])
def l398_134(x):
    # x is a list (or vector) of length 400
    return max(0, x[166])
def l398_135(x):
    # x is a list (or vector) of length 400
    return max(0, x[167])
def l398_136(x):
    # x is a list (or vector) of length 400
    return max(0, x[168])
def l398_137(x):
    # x is a list (or vector) of length 400
    return max(0, x[169])
def l398_138(x):
    # x is a list (or vector) of length 400
    return max(0, x[170])
def l398_139(x):
    # x is a list (or vector) of length 400
    return max(0, x[171])
def l398_140(x):
    # x is a list (or vector) of length 400
    return max(0, x[172])
def l398_141(x):
    # x is a list (or vector) of length 400
    return max(0, x[173])
def l398_142(x):
    # x is a list (or vector) of length 400
    return max(0, x[174])
def l398_143(x):
    # x is a list (or vector) of length 400
    return max(0, x[175])
def l398_144(x):
    # x is a list (or vector) of length 400
    return max(0, x[144])
def l398_145(x):
    # x is a list (or vector) of length 400
    return max(0, x[145])
def l398_146(x):
    # x is a list (or vector) of length 400
    return max(0, x[146])
def l398_147(x):
    # x is a list (or vector) of length 400
    return max(0, x[147])
def l398_148(x):
    # x is a list (or vector) of length 400
    return max(0, x[148])
def l398_149(x):
    # x is a list (or vector) of length 400
    return max(0, x[149])
def l398_150(x):
    # x is a list (or vector) of length 400
    return max(0, x[150])
def l398_151(x):
    # x is a list (or vector) of length 400
    return max(0, x[151])
def l398_152(x):
    # x is a list (or vector) of length 400
    return max(0, x[152])
def l398_153(x):
    # x is a list (or vector) of length 400
    return max(0, x[153])
def l398_154(x):
    # x is a list (or vector) of length 400
    return max(0, x[154])
def l398_155(x):
    # x is a list (or vector) of length 400
    return max(0, x[155])
def l398_156(x):
    # x is a list (or vector) of length 400
    return max(0, x[156])
def l398_157(x):
    # x is a list (or vector) of length 400
    return max(0, x[157])
def l398_158(x):
    # x is a list (or vector) of length 400
    return max(0, x[158])
def l398_159(x):
    # x is a list (or vector) of length 400
    return max(0, x[159])
def l398_160(x):
    # x is a list (or vector) of length 400
    return max(0, x[176])
def l398_161(x):
    # x is a list (or vector) of length 400
    return max(0, x[177])
def l398_162(x):
    # x is a list (or vector) of length 400
    return max(0, x[178])
def l398_163(x):
    # x is a list (or vector) of length 400
    return max(0, x[179])
def l398_164(x):
    # x is a list (or vector) of length 400
    return max(0, x[180])
def l398_165(x):
    # x is a list (or vector) of length 400
    return max(0, x[181])
def l398_166(x):
    # x is a list (or vector) of length 400
    return max(0, x[182])
def l398_167(x):
    # x is a list (or vector) of length 400
    return max(0, x[183])
def l398_168(x):
    # x is a list (or vector) of length 400
    return max(0, x[184])
def l398_169(x):
    # x is a list (or vector) of length 400
    return max(0, x[185])
def l398_170(x):
    # x is a list (or vector) of length 400
    return max(0, x[186])
def l398_171(x):
    # x is a list (or vector) of length 400
    return max(0, x[187])
def l398_172(x):
    # x is a list (or vector) of length 400
    return max(0, x[188])
def l398_173(x):
    # x is a list (or vector) of length 400
    return max(0, x[189])
def l398_174(x):
    # x is a list (or vector) of length 400
    return max(0, x[190])
def l398_175(x):
    # x is a list (or vector) of length 400
    return max(0, x[191])
def l398_176(x):
    # x is a list (or vector) of length 400
    return max(0, x[192])
def l398_177(x):
    # x is a list (or vector) of length 400
    return max(0, x[193])
def l398_178(x):
    # x is a list (or vector) of length 400
    return max(0, x[194])
def l398_179(x):
    # x is a list (or vector) of length 400
    return max(0, x[195])
def l398_180(x):
    # x is a list (or vector) of length 400
    return max(0, x[196])
def l398_181(x):
    # x is a list (or vector) of length 400
    return max(0, x[197])
def l398_182(x):
    # x is a list (or vector) of length 400
    return max(0, x[198])
def l398_183(x):
    # x is a list (or vector) of length 400
    return max(0, x[199])
def l398_184(x):
    # x is a list (or vector) of length 400
    return max(0, x[200])
def l398_185(x):
    # x is a list (or vector) of length 400
    return max(0, x[201])
def l398_186(x):
    # x is a list (or vector) of length 400
    return max(0, x[202])
def l398_187(x):
    # x is a list (or vector) of length 400
    return max(0, x[203])
def l398_188(x):
    # x is a list (or vector) of length 400
    return max(0, x[204])
def l398_189(x):
    # x is a list (or vector) of length 400
    return max(0, x[205])
def l398_190(x):
    # x is a list (or vector) of length 400
    return max(0, x[206])
def l398_191(x):
    # x is a list (or vector) of length 400
    return max(0, x[207])
def l398_192(x):
    # x is a list (or vector) of length 400
    return max(0, x[272])
def l398_193(x):
    # x is a list (or vector) of length 400
    return max(0, x[208] + x[273])
def l398_194(x):
    # x is a list (or vector) of length 400
    return max(0, x[209] + x[274])
def l398_195(x):
    # x is a list (or vector) of length 400
    return max(0, x[210] + x[275])
def l398_196(x):
    # x is a list (or vector) of length 400
    return max(0, x[211] + x[276])
def l398_197(x):
    # x is a list (or vector) of length 400
    return max(0, x[212] + x[277])
def l398_198(x):
    # x is a list (or vector) of length 400
    return max(0, x[213] + x[278])
def l398_199(x):
    # x is a list (or vector) of length 400
    return max(0, x[214] + x[279])
def l398_200(x):
    # x is a list (or vector) of length 400
    return max(0, x[215] + x[280])
def l398_201(x):
    # x is a list (or vector) of length 400
    return max(0, x[216] + x[281])
def l398_202(x):
    # x is a list (or vector) of length 400
    return max(0, x[217] + x[282])
def l398_203(x):
    # x is a list (or vector) of length 400
    return max(0, x[218] + x[283])
def l398_204(x):
    # x is a list (or vector) of length 400
    return max(0, x[219] + x[284])
def l398_205(x):
    # x is a list (or vector) of length 400
    return max(0, x[220] + x[285])
def l398_206(x):
    # x is a list (or vector) of length 400
    return max(0, x[221] + x[286])
def l398_207(x):
    # x is a list (or vector) of length 400
    return max(0, x[222] + x[287])
def l398_208(x):
    # x is a list (or vector) of length 400
    return max(0, x[223] + x[288])
def l398_209(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[224] + x[289] + 1.0)
def l398_210(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[225] + x[290] + 1.0)
def l398_211(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[226] + x[291] + 1.0)
def l398_212(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[227] + x[292] + 1.0)
def l398_213(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[228] + x[293] + 1.0)
def l398_214(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[229] + x[294] + 1.0)
def l398_215(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[230] + x[295] + 1.0)
def l398_216(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[231] + x[296] + 1.0)
def l398_217(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[232] + x[297] + 1.0)
def l398_218(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[233] + x[298] + 1.0)
def l398_219(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[234] + x[299] + 1.0)
def l398_220(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[235] + x[300] + 1.0)
def l398_221(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[236] + x[301] + 1.0)
def l398_222(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[237] + x[302] + 1.0)
def l398_223(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[238] + x[303] + 1.0)
def l398_224(x):
    # x is a list (or vector) of length 400
    return max(0, x[272] + -1.0)
def l398_225(x):
    # x is a list (or vector) of length 400
    return max(0, x[208] + x[273] + -1.0)
def l398_226(x):
    # x is a list (or vector) of length 400
    return max(0, x[209] + x[274] + -1.0)
def l398_227(x):
    # x is a list (or vector) of length 400
    return max(0, x[210] + x[275] + -1.0)
def l398_228(x):
    # x is a list (or vector) of length 400
    return max(0, x[211] + x[276] + -1.0)
def l398_229(x):
    # x is a list (or vector) of length 400
    return max(0, x[212] + x[277] + -1.0)
def l398_230(x):
    # x is a list (or vector) of length 400
    return max(0, x[213] + x[278] + -1.0)
def l398_231(x):
    # x is a list (or vector) of length 400
    return max(0, x[214] + x[279] + -1.0)
def l398_232(x):
    # x is a list (or vector) of length 400
    return max(0, x[215] + x[280] + -1.0)
def l398_233(x):
    # x is a list (or vector) of length 400
    return max(0, x[216] + x[281] + -1.0)
def l398_234(x):
    # x is a list (or vector) of length 400
    return max(0, x[217] + x[282] + -1.0)
def l398_235(x):
    # x is a list (or vector) of length 400
    return max(0, x[218] + x[283] + -1.0)
def l398_236(x):
    # x is a list (or vector) of length 400
    return max(0, x[219] + x[284] + -1.0)
def l398_237(x):
    # x is a list (or vector) of length 400
    return max(0, x[220] + x[285] + -1.0)
def l398_238(x):
    # x is a list (or vector) of length 400
    return max(0, x[221] + x[286] + -1.0)
def l398_239(x):
    # x is a list (or vector) of length 400
    return max(0, x[222] + x[287] + -1.0)
def l398_240(x):
    # x is a list (or vector) of length 400
    return max(0, x[223] + x[288] + -1.0)
def l398_241(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[224] + x[289])
def l398_242(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[225] + x[290])
def l398_243(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[226] + x[291])
def l398_244(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[227] + x[292])
def l398_245(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[228] + x[293])
def l398_246(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[229] + x[294])
def l398_247(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[230] + x[295])
def l398_248(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[231] + x[296])
def l398_249(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[232] + x[297])
def l398_250(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[233] + x[298])
def l398_251(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[234] + x[299])
def l398_252(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[235] + x[300])
def l398_253(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[236] + x[301])
def l398_254(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[237] + x[302])
def l398_255(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[238] + x[303])
def l398_256(x):
    # x is a list (or vector) of length 400
    return max(0, x[332])
def l398_257(x):
    # x is a list (or vector) of length 400
    return max(0, x[328])
def l398_258(x):
    # x is a list (or vector) of length 400
    return max(0, x[324])
def l398_259(x):
    # x is a list (or vector) of length 400
    return max(0, x[320])
def l398_260(x):
    # x is a list (or vector) of length 400
    return max(0, x[316])
def l398_261(x):
    # x is a list (or vector) of length 400
    return max(0, x[312])
def l398_262(x):
    # x is a list (or vector) of length 400
    return max(0, x[308])
def l398_263(x):
    # x is a list (or vector) of length 400
    return max(0, x[304])
def l398_264(x):
    # x is a list (or vector) of length 400
    return max(0, x[333])
def l398_265(x):
    # x is a list (or vector) of length 400
    return max(0, x[329])
def l398_266(x):
    # x is a list (or vector) of length 400
    return max(0, x[325])
def l398_267(x):
    # x is a list (or vector) of length 400
    return max(0, x[321])
def l398_268(x):
    # x is a list (or vector) of length 400
    return max(0, x[317])
def l398_269(x):
    # x is a list (or vector) of length 400
    return max(0, x[313])
def l398_270(x):
    # x is a list (or vector) of length 400
    return max(0, x[309])
def l398_271(x):
    # x is a list (or vector) of length 400
    return max(0, x[305])
def l398_272(x):
    # x is a list (or vector) of length 400
    return max(0, x[334])
def l398_273(x):
    # x is a list (or vector) of length 400
    return max(0, x[330])
def l398_274(x):
    # x is a list (or vector) of length 400
    return max(0, x[326])
def l398_275(x):
    # x is a list (or vector) of length 400
    return max(0, x[322])
def l398_276(x):
    # x is a list (or vector) of length 400
    return max(0, x[318])
def l398_277(x):
    # x is a list (or vector) of length 400
    return max(0, x[314])
def l398_278(x):
    # x is a list (or vector) of length 400
    return max(0, x[310])
def l398_279(x):
    # x is a list (or vector) of length 400
    return max(0, x[306])
def l398_280(x):
    # x is a list (or vector) of length 400
    return max(0, x[335])
def l398_281(x):
    # x is a list (or vector) of length 400
    return max(0, x[331])
def l398_282(x):
    # x is a list (or vector) of length 400
    return max(0, x[327])
def l398_283(x):
    # x is a list (or vector) of length 400
    return max(0, x[323])
def l398_284(x):
    # x is a list (or vector) of length 400
    return max(0, x[319])
def l398_285(x):
    # x is a list (or vector) of length 400
    return max(0, x[315])
def l398_286(x):
    # x is a list (or vector) of length 400
    return max(0, x[311])
def l398_287(x):
    # x is a list (or vector) of length 400
    return max(0, x[307])
def l398_288(x):
    # x is a list (or vector) of length 400
    return max(0, x[336])
def l398_289(x):
    # x is a list (or vector) of length 400
    return max(0, x[337])
def l398_290(x):
    # x is a list (or vector) of length 400
    return max(0, x[338])
def l398_291(x):
    # x is a list (or vector) of length 400
    return max(0, x[339])
def l398_292(x):
    # x is a list (or vector) of length 400
    return max(0, x[340])
def l398_293(x):
    # x is a list (or vector) of length 400
    return max(0, x[341])
def l398_294(x):
    # x is a list (or vector) of length 400
    return max(0, x[342])
def l398_295(x):
    # x is a list (or vector) of length 400
    return max(0, x[343])
def l398_296(x):
    # x is a list (or vector) of length 400
    return max(0, x[344])
def l398_297(x):
    # x is a list (or vector) of length 400
    return max(0, x[345])
def l398_298(x):
    # x is a list (or vector) of length 400
    return max(0, x[346])
def l398_299(x):
    # x is a list (or vector) of length 400
    return max(0, x[347])
def l398_300(x):
    # x is a list (or vector) of length 400
    return max(0, x[348])
def l398_301(x):
    # x is a list (or vector) of length 400
    return max(0, x[349])
def l398_302(x):
    # x is a list (or vector) of length 400
    return max(0, x[350])
def l398_303(x):
    # x is a list (or vector) of length 400
    return max(0, x[351])
def l398_304(x):
    # x is a list (or vector) of length 400
    return max(0, x[352])
def l398_305(x):
    # x is a list (or vector) of length 400
    return max(0, x[353])
def l398_306(x):
    # x is a list (or vector) of length 400
    return max(0, x[354])
def l398_307(x):
    # x is a list (or vector) of length 400
    return max(0, x[355])
def l398_308(x):
    # x is a list (or vector) of length 400
    return max(0, x[356])
def l398_309(x):
    # x is a list (or vector) of length 400
    return max(0, x[357])
def l398_310(x):
    # x is a list (or vector) of length 400
    return max(0, x[358])
def l398_311(x):
    # x is a list (or vector) of length 400
    return max(0, x[359])
def l398_312(x):
    # x is a list (or vector) of length 400
    return max(0, x[360])
def l398_313(x):
    # x is a list (or vector) of length 400
    return max(0, x[361])
def l398_314(x):
    # x is a list (or vector) of length 400
    return max(0, x[362])
def l398_315(x):
    # x is a list (or vector) of length 400
    return max(0, x[363])
def l398_316(x):
    # x is a list (or vector) of length 400
    return max(0, x[364])
def l398_317(x):
    # x is a list (or vector) of length 400
    return max(0, x[365])
def l398_318(x):
    # x is a list (or vector) of length 400
    return max(0, x[366])
def l398_319(x):
    # x is a list (or vector) of length 400
    return max(0, x[367])
def l398_320(x):
    # x is a list (or vector) of length 400
    return max(0, x[368])
def l398_321(x):
    # x is a list (or vector) of length 400
    return max(0, x[369])
def l398_322(x):
    # x is a list (or vector) of length 400
    return max(0, x[370])
def l398_323(x):
    # x is a list (or vector) of length 400
    return max(0, x[371])
def l398_324(x):
    # x is a list (or vector) of length 400
    return max(0, x[372])
def l398_325(x):
    # x is a list (or vector) of length 400
    return max(0, x[373])
def l398_326(x):
    # x is a list (or vector) of length 400
    return max(0, x[374])
def l398_327(x):
    # x is a list (or vector) of length 400
    return max(0, x[375])
def l398_328(x):
    # x is a list (or vector) of length 400
    return max(0, x[376])
def l398_329(x):
    # x is a list (or vector) of length 400
    return max(0, x[377])
def l398_330(x):
    # x is a list (or vector) of length 400
    return max(0, x[378])
def l398_331(x):
    # x is a list (or vector) of length 400
    return max(0, x[379])
def l398_332(x):
    # x is a list (or vector) of length 400
    return max(0, x[380])
def l398_333(x):
    # x is a list (or vector) of length 400
    return max(0, x[381])
def l398_334(x):
    # x is a list (or vector) of length 400
    return max(0, x[382])
def l398_335(x):
    # x is a list (or vector) of length 400
    return max(0, x[383])
def l398_336(x):
    # x is a list (or vector) of length 400
    return max(0, x[384])
def l398_337(x):
    # x is a list (or vector) of length 400
    return max(0, x[385])
def l398_338(x):
    # x is a list (or vector) of length 400
    return max(0, x[386])
def l398_339(x):
    # x is a list (or vector) of length 400
    return max(0, x[387])
def l398_340(x):
    # x is a list (or vector) of length 400
    return max(0, x[388])
def l398_341(x):
    # x is a list (or vector) of length 400
    return max(0, x[389])
def l398_342(x):
    # x is a list (or vector) of length 400
    return max(0, x[390])
def l398_343(x):
    # x is a list (or vector) of length 400
    return max(0, x[391])
def l398_344(x):
    # x is a list (or vector) of length 400
    return max(0, x[392])
def l398_345(x):
    # x is a list (or vector) of length 400
    return max(0, x[393])
def l398_346(x):
    # x is a list (or vector) of length 400
    return max(0, x[394])
def l398_347(x):
    # x is a list (or vector) of length 400
    return max(0, x[395])
def l398_348(x):
    # x is a list (or vector) of length 400
    return max(0, x[396])
def l398_349(x):
    # x is a list (or vector) of length 400
    return max(0, x[397])
def l398_350(x):
    # x is a list (or vector) of length 400
    return max(0, x[398])
def l398_351(x):
    # x is a list (or vector) of length 400
    return max(0, x[399])
def l398_(x):
    # x is a list (or vector) of length 400
    return [
        l398_0(x),
        l398_1(x),
        l398_2(x),
        l398_3(x),
        l398_4(x),
        l398_5(x),
        l398_6(x),
        l398_7(x),
        l398_8(x),
        l398_9(x),
        l398_10(x),
        l398_11(x),
        l398_12(x),
        l398_13(x),
        l398_14(x),
        l398_15(x),
        l398_16(x),
        l398_17(x),
        l398_18(x),
        l398_19(x),
        l398_20(x),
        l398_21(x),
        l398_22(x),
        l398_23(x),
        l398_24(x),
        l398_25(x),
        l398_26(x),
        l398_27(x),
        l398_28(x),
        l398_29(x),
        l398_30(x),
        l398_31(x),
        l398_32(x),
        l398_33(x),
        l398_34(x),
        l398_35(x),
        l398_36(x),
        l398_37(x),
        l398_38(x),
        l398_39(x),
        l398_40(x),
        l398_41(x),
        l398_42(x),
        l398_43(x),
        l398_44(x),
        l398_45(x),
        l398_46(x),
        l398_47(x),
        l398_48(x),
        l398_49(x),
        l398_50(x),
        l398_51(x),
        l398_52(x),
        l398_53(x),
        l398_54(x),
        l398_55(x),
        l398_56(x),
        l398_57(x),
        l398_58(x),
        l398_59(x),
        l398_60(x),
        l398_61(x),
        l398_62(x),
        l398_63(x),
        l398_64(x),
        l398_65(x),
        l398_66(x),
        l398_67(x),
        l398_68(x),
        l398_69(x),
        l398_70(x),
        l398_71(x),
        l398_72(x),
        l398_73(x),
        l398_74(x),
        l398_75(x),
        l398_76(x),
        l398_77(x),
        l398_78(x),
        l398_79(x),
        l398_80(x),
        l398_81(x),
        l398_82(x),
        l398_83(x),
        l398_84(x),
        l398_85(x),
        l398_86(x),
        l398_87(x),
        l398_88(x),
        l398_89(x),
        l398_90(x),
        l398_91(x),
        l398_92(x),
        l398_93(x),
        l398_94(x),
        l398_95(x),
        l398_96(x),
        l398_97(x),
        l398_98(x),
        l398_99(x),
        l398_100(x),
        l398_101(x),
        l398_102(x),
        l398_103(x),
        l398_104(x),
        l398_105(x),
        l398_106(x),
        l398_107(x),
        l398_108(x),
        l398_109(x),
        l398_110(x),
        l398_111(x),
        l398_112(x),
        l398_113(x),
        l398_114(x),
        l398_115(x),
        l398_116(x),
        l398_117(x),
        l398_118(x),
        l398_119(x),
        l398_120(x),
        l398_121(x),
        l398_122(x),
        l398_123(x),
        l398_124(x),
        l398_125(x),
        l398_126(x),
        l398_127(x),
        l398_128(x),
        l398_129(x),
        l398_130(x),
        l398_131(x),
        l398_132(x),
        l398_133(x),
        l398_134(x),
        l398_135(x),
        l398_136(x),
        l398_137(x),
        l398_138(x),
        l398_139(x),
        l398_140(x),
        l398_141(x),
        l398_142(x),
        l398_143(x),
        l398_144(x),
        l398_145(x),
        l398_146(x),
        l398_147(x),
        l398_148(x),
        l398_149(x),
        l398_150(x),
        l398_151(x),
        l398_152(x),
        l398_153(x),
        l398_154(x),
        l398_155(x),
        l398_156(x),
        l398_157(x),
        l398_158(x),
        l398_159(x),
        l398_160(x),
        l398_161(x),
        l398_162(x),
        l398_163(x),
        l398_164(x),
        l398_165(x),
        l398_166(x),
        l398_167(x),
        l398_168(x),
        l398_169(x),
        l398_170(x),
        l398_171(x),
        l398_172(x),
        l398_173(x),
        l398_174(x),
        l398_175(x),
        l398_176(x),
        l398_177(x),
        l398_178(x),
        l398_179(x),
        l398_180(x),
        l398_181(x),
        l398_182(x),
        l398_183(x),
        l398_184(x),
        l398_185(x),
        l398_186(x),
        l398_187(x),
        l398_188(x),
        l398_189(x),
        l398_190(x),
        l398_191(x),
        l398_192(x),
        l398_193(x),
        l398_194(x),
        l398_195(x),
        l398_196(x),
        l398_197(x),
        l398_198(x),
        l398_199(x),
        l398_200(x),
        l398_201(x),
        l398_202(x),
        l398_203(x),
        l398_204(x),
        l398_205(x),
        l398_206(x),
        l398_207(x),
        l398_208(x),
        l398_209(x),
        l398_210(x),
        l398_211(x),
        l398_212(x),
        l398_213(x),
        l398_214(x),
        l398_215(x),
        l398_216(x),
        l398_217(x),
        l398_218(x),
        l398_219(x),
        l398_220(x),
        l398_221(x),
        l398_222(x),
        l398_223(x),
        l398_224(x),
        l398_225(x),
        l398_226(x),
        l398_227(x),
        l398_228(x),
        l398_229(x),
        l398_230(x),
        l398_231(x),
        l398_232(x),
        l398_233(x),
        l398_234(x),
        l398_235(x),
        l398_236(x),
        l398_237(x),
        l398_238(x),
        l398_239(x),
        l398_240(x),
        l398_241(x),
        l398_242(x),
        l398_243(x),
        l398_244(x),
        l398_245(x),
        l398_246(x),
        l398_247(x),
        l398_248(x),
        l398_249(x),
        l398_250(x),
        l398_251(x),
        l398_252(x),
        l398_253(x),
        l398_254(x),
        l398_255(x),
        l398_256(x),
        l398_257(x),
        l398_258(x),
        l398_259(x),
        l398_260(x),
        l398_261(x),
        l398_262(x),
        l398_263(x),
        l398_264(x),
        l398_265(x),
        l398_266(x),
        l398_267(x),
        l398_268(x),
        l398_269(x),
        l398_270(x),
        l398_271(x),
        l398_272(x),
        l398_273(x),
        l398_274(x),
        l398_275(x),
        l398_276(x),
        l398_277(x),
        l398_278(x),
        l398_279(x),
        l398_280(x),
        l398_281(x),
        l398_282(x),
        l398_283(x),
        l398_284(x),
        l398_285(x),
        l398_286(x),
        l398_287(x),
        l398_288(x),
        l398_289(x),
        l398_290(x),
        l398_291(x),
        l398_292(x),
        l398_293(x),
        l398_294(x),
        l398_295(x),
        l398_296(x),
        l398_297(x),
        l398_298(x),
        l398_299(x),
        l398_300(x),
        l398_301(x),
        l398_302(x),
        l398_303(x),
        l398_304(x),
        l398_305(x),
        l398_306(x),
        l398_307(x),
        l398_308(x),
        l398_309(x),
        l398_310(x),
        l398_311(x),
        l398_312(x),
        l398_313(x),
        l398_314(x),
        l398_315(x),
        l398_316(x),
        l398_317(x),
        l398_318(x),
        l398_319(x),
        l398_320(x),
        l398_321(x),
        l398_322(x),
        l398_323(x),
        l398_324(x),
        l398_325(x),
        l398_326(x),
        l398_327(x),
        l398_328(x),
        l398_329(x),
        l398_330(x),
        l398_331(x),
        l398_332(x),
        l398_333(x),
        l398_334(x),
        l398_335(x),
        l398_336(x),
        l398_337(x),
        l398_338(x),
        l398_339(x),
        l398_340(x),
        l398_341(x),
        l398_342(x),
        l398_343(x),
        l398_344(x),
        l398_345(x),
        l398_346(x),
        l398_347(x),
        l398_348(x),
        l398_349(x),
        l398_350(x),
        l398_351(x),
    ]