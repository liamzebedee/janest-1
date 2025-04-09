import numpy as np




# Generated from reverse engineering
def l482_g(x: np.ndarray) -> np.ndarray:
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




def l482_0(x):
    # x is a list (or vector) of length 400
    return max(0, x[0])
def l482_1(x):
    # x is a list (or vector) of length 400
    return max(0, x[1])
def l482_2(x):
    # x is a list (or vector) of length 400
    return max(0, x[2])
def l482_3(x):
    # x is a list (or vector) of length 400
    return max(0, x[3])
def l482_4(x):
    # x is a list (or vector) of length 400
    return max(0, x[4])
def l482_5(x):
    # x is a list (or vector) of length 400
    return max(0, x[5])
def l482_6(x):
    # x is a list (or vector) of length 400
    return max(0, x[6])
def l482_7(x):
    # x is a list (or vector) of length 400
    return max(0, x[7])
def l482_8(x):
    # x is a list (or vector) of length 400
    return max(0, x[8])
def l482_9(x):
    # x is a list (or vector) of length 400
    return max(0, x[9])
def l482_10(x):
    # x is a list (or vector) of length 400
    return max(0, x[10])
def l482_11(x):
    # x is a list (or vector) of length 400
    return max(0, x[11])
def l482_12(x):
    # x is a list (or vector) of length 400
    return max(0, x[12])
def l482_13(x):
    # x is a list (or vector) of length 400
    return max(0, x[13])
def l482_14(x):
    # x is a list (or vector) of length 400
    return max(0, x[14])
def l482_15(x):
    # x is a list (or vector) of length 400
    return max(0, x[15])
def l482_16(x):
    # x is a list (or vector) of length 400
    return max(0, x[16])
def l482_17(x):
    # x is a list (or vector) of length 400
    return max(0, x[17])
def l482_18(x):
    # x is a list (or vector) of length 400
    return max(0, x[18])
def l482_19(x):
    # x is a list (or vector) of length 400
    return max(0, x[19])
def l482_20(x):
    # x is a list (or vector) of length 400
    return max(0, x[20])
def l482_21(x):
    # x is a list (or vector) of length 400
    return max(0, x[21])
def l482_22(x):
    # x is a list (or vector) of length 400
    return max(0, x[22])
def l482_23(x):
    # x is a list (or vector) of length 400
    return max(0, x[23])
def l482_24(x):
    # x is a list (or vector) of length 400
    return max(0, x[24])
def l482_25(x):
    # x is a list (or vector) of length 400
    return max(0, x[25])
def l482_26(x):
    # x is a list (or vector) of length 400
    return max(0, x[26])
def l482_27(x):
    # x is a list (or vector) of length 400
    return max(0, x[27])
def l482_28(x):
    # x is a list (or vector) of length 400
    return max(0, x[28])
def l482_29(x):
    # x is a list (or vector) of length 400
    return max(0, x[29])
def l482_30(x):
    # x is a list (or vector) of length 400
    return max(0, x[30])
def l482_31(x):
    # x is a list (or vector) of length 400
    return max(0, x[31])
def l482_32(x):
    # x is a list (or vector) of length 400
    return max(0, x[32])
def l482_33(x):
    # x is a list (or vector) of length 400
    return max(0, x[33])
def l482_34(x):
    # x is a list (or vector) of length 400
    return max(0, x[34])
def l482_35(x):
    # x is a list (or vector) of length 400
    return max(0, x[35])
def l482_36(x):
    # x is a list (or vector) of length 400
    return max(0, x[36])
def l482_37(x):
    # x is a list (or vector) of length 400
    return max(0, x[37])
def l482_38(x):
    # x is a list (or vector) of length 400
    return max(0, x[38])
def l482_39(x):
    # x is a list (or vector) of length 400
    return max(0, x[39])
def l482_40(x):
    # x is a list (or vector) of length 400
    return max(0, x[40])
def l482_41(x):
    # x is a list (or vector) of length 400
    return max(0, x[41])
def l482_42(x):
    # x is a list (or vector) of length 400
    return max(0, x[42])
def l482_43(x):
    # x is a list (or vector) of length 400
    return max(0, x[43])
def l482_44(x):
    # x is a list (or vector) of length 400
    return max(0, x[44])
def l482_45(x):
    # x is a list (or vector) of length 400
    return max(0, x[45])
def l482_46(x):
    # x is a list (or vector) of length 400
    return max(0, x[46])
def l482_47(x):
    # x is a list (or vector) of length 400
    return max(0, x[47])
def l482_48(x):
    # x is a list (or vector) of length 400
    return max(0, x[48])
def l482_49(x):
    # x is a list (or vector) of length 400
    return max(0, x[49])
def l482_50(x):
    # x is a list (or vector) of length 400
    return max(0, x[50])
def l482_51(x):
    # x is a list (or vector) of length 400
    return max(0, x[51])
def l482_52(x):
    # x is a list (or vector) of length 400
    return max(0, x[52])
def l482_53(x):
    # x is a list (or vector) of length 400
    return max(0, x[53])
def l482_54(x):
    # x is a list (or vector) of length 400
    return max(0, x[54])
def l482_55(x):
    # x is a list (or vector) of length 400
    return max(0, x[55])
def l482_56(x):
    # x is a list (or vector) of length 400
    return max(0, x[56])
def l482_57(x):
    # x is a list (or vector) of length 400
    return max(0, x[57])
def l482_58(x):
    # x is a list (or vector) of length 400
    return max(0, x[58])
def l482_59(x):
    # x is a list (or vector) of length 400
    return max(0, x[59])
def l482_60(x):
    # x is a list (or vector) of length 400
    return max(0, x[60])
def l482_61(x):
    # x is a list (or vector) of length 400
    return max(0, x[61])
def l482_62(x):
    # x is a list (or vector) of length 400
    return max(0, x[62])
def l482_63(x):
    # x is a list (or vector) of length 400
    return max(0, x[63])
def l482_64(x):
    # x is a list (or vector) of length 400
    return max(0, x[64])
def l482_65(x):
    # x is a list (or vector) of length 400
    return max(0, x[65])
def l482_66(x):
    # x is a list (or vector) of length 400
    return max(0, x[66])
def l482_67(x):
    # x is a list (or vector) of length 400
    return max(0, x[67])
def l482_68(x):
    # x is a list (or vector) of length 400
    return max(0, x[68])
def l482_69(x):
    # x is a list (or vector) of length 400
    return max(0, x[69])
def l482_70(x):
    # x is a list (or vector) of length 400
    return max(0, x[70])
def l482_71(x):
    # x is a list (or vector) of length 400
    return max(0, x[71])
def l482_72(x):
    # x is a list (or vector) of length 400
    return max(0, x[72])
def l482_73(x):
    # x is a list (or vector) of length 400
    return max(0, x[73])
def l482_74(x):
    # x is a list (or vector) of length 400
    return max(0, x[74])
def l482_75(x):
    # x is a list (or vector) of length 400
    return max(0, x[75])
def l482_76(x):
    # x is a list (or vector) of length 400
    return max(0, x[76])
def l482_77(x):
    # x is a list (or vector) of length 400
    return max(0, x[77])
def l482_78(x):
    # x is a list (or vector) of length 400
    return max(0, x[78])
def l482_79(x):
    # x is a list (or vector) of length 400
    return max(0, x[79])
def l482_80(x):
    # x is a list (or vector) of length 400
    return max(0, x[80])
def l482_81(x):
    # x is a list (or vector) of length 400
    return max(0, x[81])
def l482_82(x):
    # x is a list (or vector) of length 400
    return max(0, x[82])
def l482_83(x):
    # x is a list (or vector) of length 400
    return max(0, x[83])
def l482_84(x):
    # x is a list (or vector) of length 400
    return max(0, x[84])
def l482_85(x):
    # x is a list (or vector) of length 400
    return max(0, x[85])
def l482_86(x):
    # x is a list (or vector) of length 400
    return max(0, x[86])
def l482_87(x):
    # x is a list (or vector) of length 400
    return max(0, x[87])
def l482_88(x):
    # x is a list (or vector) of length 400
    return max(0, x[88])
def l482_89(x):
    # x is a list (or vector) of length 400
    return max(0, x[89])
def l482_90(x):
    # x is a list (or vector) of length 400
    return max(0, x[90])
def l482_91(x):
    # x is a list (or vector) of length 400
    return max(0, x[91])
def l482_92(x):
    # x is a list (or vector) of length 400
    return max(0, x[92])
def l482_93(x):
    # x is a list (or vector) of length 400
    return max(0, x[93])
def l482_94(x):
    # x is a list (or vector) of length 400
    return max(0, x[94])
def l482_95(x):
    # x is a list (or vector) of length 400
    return max(0, x[95])
def l482_96(x):
    # x is a list (or vector) of length 400
    return max(0, x[96])
def l482_97(x):
    # x is a list (or vector) of length 400
    return max(0, x[97])
def l482_98(x):
    # x is a list (or vector) of length 400
    return max(0, x[98])
def l482_99(x):
    # x is a list (or vector) of length 400
    return max(0, x[99])
def l482_100(x):
    # x is a list (or vector) of length 400
    return max(0, x[100])
def l482_101(x):
    # x is a list (or vector) of length 400
    return max(0, x[101])
def l482_102(x):
    # x is a list (or vector) of length 400
    return max(0, x[102])
def l482_103(x):
    # x is a list (or vector) of length 400
    return max(0, x[103])
def l482_104(x):
    # x is a list (or vector) of length 400
    return max(0, x[104])
def l482_105(x):
    # x is a list (or vector) of length 400
    return max(0, x[105])
def l482_106(x):
    # x is a list (or vector) of length 400
    return max(0, x[106])
def l482_107(x):
    # x is a list (or vector) of length 400
    return max(0, x[107])
def l482_108(x):
    # x is a list (or vector) of length 400
    return max(0, x[108])
def l482_109(x):
    # x is a list (or vector) of length 400
    return max(0, x[109])
def l482_110(x):
    # x is a list (or vector) of length 400
    return max(0, x[110])
def l482_111(x):
    # x is a list (or vector) of length 400
    return max(0, x[111])
def l482_112(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[112] + -1.0*x[128] + 1.0)
def l482_113(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[113] + -1.0*x[129] + 1.0)
def l482_114(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[114] + -1.0*x[130] + 1.0)
def l482_115(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[115] + -1.0*x[131] + 1.0)
def l482_116(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[116] + -1.0*x[132] + 1.0)
def l482_117(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[117] + -1.0*x[133] + 1.0)
def l482_118(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[118] + -1.0*x[134] + 1.0)
def l482_119(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[119] + -1.0*x[135] + 1.0)
def l482_120(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[120] + -1.0*x[136] + 1.0)
def l482_121(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[121] + -1.0*x[137] + 1.0)
def l482_122(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[122] + -1.0*x[138] + 1.0)
def l482_123(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[123] + -1.0*x[139] + 1.0)
def l482_124(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[124] + -1.0*x[140] + 1.0)
def l482_125(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[125] + -1.0*x[141] + 1.0)
def l482_126(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[126] + -1.0*x[142] + 1.0)
def l482_127(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[127] + -1.0*x[143] + 1.0)
def l482_128(x):
    # x is a list (or vector) of length 400
    return max(0, x[160])
def l482_129(x):
    # x is a list (or vector) of length 400
    return max(0, x[161])
def l482_130(x):
    # x is a list (or vector) of length 400
    return max(0, x[162])
def l482_131(x):
    # x is a list (or vector) of length 400
    return max(0, x[163])
def l482_132(x):
    # x is a list (or vector) of length 400
    return max(0, x[164])
def l482_133(x):
    # x is a list (or vector) of length 400
    return max(0, x[165])
def l482_134(x):
    # x is a list (or vector) of length 400
    return max(0, x[166])
def l482_135(x):
    # x is a list (or vector) of length 400
    return max(0, x[167])
def l482_136(x):
    # x is a list (or vector) of length 400
    return max(0, x[168])
def l482_137(x):
    # x is a list (or vector) of length 400
    return max(0, x[169])
def l482_138(x):
    # x is a list (or vector) of length 400
    return max(0, x[170])
def l482_139(x):
    # x is a list (or vector) of length 400
    return max(0, x[171])
def l482_140(x):
    # x is a list (or vector) of length 400
    return max(0, x[172])
def l482_141(x):
    # x is a list (or vector) of length 400
    return max(0, x[173])
def l482_142(x):
    # x is a list (or vector) of length 400
    return max(0, x[174])
def l482_143(x):
    # x is a list (or vector) of length 400
    return max(0, x[175])
def l482_144(x):
    # x is a list (or vector) of length 400
    return max(0, x[144])
def l482_145(x):
    # x is a list (or vector) of length 400
    return max(0, x[145])
def l482_146(x):
    # x is a list (or vector) of length 400
    return max(0, x[146])
def l482_147(x):
    # x is a list (or vector) of length 400
    return max(0, x[147])
def l482_148(x):
    # x is a list (or vector) of length 400
    return max(0, x[148])
def l482_149(x):
    # x is a list (or vector) of length 400
    return max(0, x[149])
def l482_150(x):
    # x is a list (or vector) of length 400
    return max(0, x[150])
def l482_151(x):
    # x is a list (or vector) of length 400
    return max(0, x[151])
def l482_152(x):
    # x is a list (or vector) of length 400
    return max(0, x[152])
def l482_153(x):
    # x is a list (or vector) of length 400
    return max(0, x[153])
def l482_154(x):
    # x is a list (or vector) of length 400
    return max(0, x[154])
def l482_155(x):
    # x is a list (or vector) of length 400
    return max(0, x[155])
def l482_156(x):
    # x is a list (or vector) of length 400
    return max(0, x[156])
def l482_157(x):
    # x is a list (or vector) of length 400
    return max(0, x[157])
def l482_158(x):
    # x is a list (or vector) of length 400
    return max(0, x[158])
def l482_159(x):
    # x is a list (or vector) of length 400
    return max(0, x[159])
def l482_160(x):
    # x is a list (or vector) of length 400
    return max(0, x[176])
def l482_161(x):
    # x is a list (or vector) of length 400
    return max(0, x[177])
def l482_162(x):
    # x is a list (or vector) of length 400
    return max(0, x[178])
def l482_163(x):
    # x is a list (or vector) of length 400
    return max(0, x[179])
def l482_164(x):
    # x is a list (or vector) of length 400
    return max(0, x[180])
def l482_165(x):
    # x is a list (or vector) of length 400
    return max(0, x[181])
def l482_166(x):
    # x is a list (or vector) of length 400
    return max(0, x[182])
def l482_167(x):
    # x is a list (or vector) of length 400
    return max(0, x[183])
def l482_168(x):
    # x is a list (or vector) of length 400
    return max(0, x[184])
def l482_169(x):
    # x is a list (or vector) of length 400
    return max(0, x[185])
def l482_170(x):
    # x is a list (or vector) of length 400
    return max(0, x[186])
def l482_171(x):
    # x is a list (or vector) of length 400
    return max(0, x[187])
def l482_172(x):
    # x is a list (or vector) of length 400
    return max(0, x[188])
def l482_173(x):
    # x is a list (or vector) of length 400
    return max(0, x[189])
def l482_174(x):
    # x is a list (or vector) of length 400
    return max(0, x[190])
def l482_175(x):
    # x is a list (or vector) of length 400
    return max(0, x[191])
def l482_176(x):
    # x is a list (or vector) of length 400
    return max(0, x[192])
def l482_177(x):
    # x is a list (or vector) of length 400
    return max(0, x[193])
def l482_178(x):
    # x is a list (or vector) of length 400
    return max(0, x[194])
def l482_179(x):
    # x is a list (or vector) of length 400
    return max(0, x[195])
def l482_180(x):
    # x is a list (or vector) of length 400
    return max(0, x[196])
def l482_181(x):
    # x is a list (or vector) of length 400
    return max(0, x[197])
def l482_182(x):
    # x is a list (or vector) of length 400
    return max(0, x[198])
def l482_183(x):
    # x is a list (or vector) of length 400
    return max(0, x[199])
def l482_184(x):
    # x is a list (or vector) of length 400
    return max(0, x[200])
def l482_185(x):
    # x is a list (or vector) of length 400
    return max(0, x[201])
def l482_186(x):
    # x is a list (or vector) of length 400
    return max(0, x[202])
def l482_187(x):
    # x is a list (or vector) of length 400
    return max(0, x[203])
def l482_188(x):
    # x is a list (or vector) of length 400
    return max(0, x[204])
def l482_189(x):
    # x is a list (or vector) of length 400
    return max(0, x[205])
def l482_190(x):
    # x is a list (or vector) of length 400
    return max(0, x[206])
def l482_191(x):
    # x is a list (or vector) of length 400
    return max(0, x[207])
def l482_192(x):
    # x is a list (or vector) of length 400
    return max(0, x[272])
def l482_193(x):
    # x is a list (or vector) of length 400
    return max(0, x[208] + x[273])
def l482_194(x):
    # x is a list (or vector) of length 400
    return max(0, x[209] + x[274])
def l482_195(x):
    # x is a list (or vector) of length 400
    return max(0, x[210] + x[275])
def l482_196(x):
    # x is a list (or vector) of length 400
    return max(0, x[211] + x[276])
def l482_197(x):
    # x is a list (or vector) of length 400
    return max(0, x[212] + x[277])
def l482_198(x):
    # x is a list (or vector) of length 400
    return max(0, x[213] + x[278])
def l482_199(x):
    # x is a list (or vector) of length 400
    return max(0, x[214] + x[279])
def l482_200(x):
    # x is a list (or vector) of length 400
    return max(0, x[215] + x[280])
def l482_201(x):
    # x is a list (or vector) of length 400
    return max(0, x[216] + x[281])
def l482_202(x):
    # x is a list (or vector) of length 400
    return max(0, x[217] + x[282])
def l482_203(x):
    # x is a list (or vector) of length 400
    return max(0, x[218] + x[283])
def l482_204(x):
    # x is a list (or vector) of length 400
    return max(0, x[219] + x[284])
def l482_205(x):
    # x is a list (or vector) of length 400
    return max(0, x[220] + x[285])
def l482_206(x):
    # x is a list (or vector) of length 400
    return max(0, x[221] + x[286])
def l482_207(x):
    # x is a list (or vector) of length 400
    return max(0, x[222] + x[287])
def l482_208(x):
    # x is a list (or vector) of length 400
    return max(0, x[223] + x[288])
def l482_209(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[224] + x[289] + 1.0)
def l482_210(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[225] + x[290] + 1.0)
def l482_211(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[226] + x[291] + 1.0)
def l482_212(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[227] + x[292] + 1.0)
def l482_213(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[228] + x[293] + 1.0)
def l482_214(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[229] + x[294] + 1.0)
def l482_215(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[230] + x[295] + 1.0)
def l482_216(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[231] + x[296] + 1.0)
def l482_217(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[232] + x[297] + 1.0)
def l482_218(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[233] + x[298] + 1.0)
def l482_219(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[234] + x[299] + 1.0)
def l482_220(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[235] + x[300] + 1.0)
def l482_221(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[236] + x[301] + 1.0)
def l482_222(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[237] + x[302] + 1.0)
def l482_223(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[238] + x[303] + 1.0)
def l482_224(x):
    # x is a list (or vector) of length 400
    return max(0, x[272] + -1.0)
def l482_225(x):
    # x is a list (or vector) of length 400
    return max(0, x[208] + x[273] + -1.0)
def l482_226(x):
    # x is a list (or vector) of length 400
    return max(0, x[209] + x[274] + -1.0)
def l482_227(x):
    # x is a list (or vector) of length 400
    return max(0, x[210] + x[275] + -1.0)
def l482_228(x):
    # x is a list (or vector) of length 400
    return max(0, x[211] + x[276] + -1.0)
def l482_229(x):
    # x is a list (or vector) of length 400
    return max(0, x[212] + x[277] + -1.0)
def l482_230(x):
    # x is a list (or vector) of length 400
    return max(0, x[213] + x[278] + -1.0)
def l482_231(x):
    # x is a list (or vector) of length 400
    return max(0, x[214] + x[279] + -1.0)
def l482_232(x):
    # x is a list (or vector) of length 400
    return max(0, x[215] + x[280] + -1.0)
def l482_233(x):
    # x is a list (or vector) of length 400
    return max(0, x[216] + x[281] + -1.0)
def l482_234(x):
    # x is a list (or vector) of length 400
    return max(0, x[217] + x[282] + -1.0)
def l482_235(x):
    # x is a list (or vector) of length 400
    return max(0, x[218] + x[283] + -1.0)
def l482_236(x):
    # x is a list (or vector) of length 400
    return max(0, x[219] + x[284] + -1.0)
def l482_237(x):
    # x is a list (or vector) of length 400
    return max(0, x[220] + x[285] + -1.0)
def l482_238(x):
    # x is a list (or vector) of length 400
    return max(0, x[221] + x[286] + -1.0)
def l482_239(x):
    # x is a list (or vector) of length 400
    return max(0, x[222] + x[287] + -1.0)
def l482_240(x):
    # x is a list (or vector) of length 400
    return max(0, x[223] + x[288] + -1.0)
def l482_241(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[224] + x[289])
def l482_242(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[225] + x[290])
def l482_243(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[226] + x[291])
def l482_244(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[227] + x[292])
def l482_245(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[228] + x[293])
def l482_246(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[229] + x[294])
def l482_247(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[230] + x[295])
def l482_248(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[231] + x[296])
def l482_249(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[232] + x[297])
def l482_250(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[233] + x[298])
def l482_251(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[234] + x[299])
def l482_252(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[235] + x[300])
def l482_253(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[236] + x[301])
def l482_254(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[237] + x[302])
def l482_255(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[238] + x[303])
def l482_256(x):
    # x is a list (or vector) of length 400
    return max(0, x[332])
def l482_257(x):
    # x is a list (or vector) of length 400
    return max(0, x[328])
def l482_258(x):
    # x is a list (or vector) of length 400
    return max(0, x[324])
def l482_259(x):
    # x is a list (or vector) of length 400
    return max(0, x[320])
def l482_260(x):
    # x is a list (or vector) of length 400
    return max(0, x[316])
def l482_261(x):
    # x is a list (or vector) of length 400
    return max(0, x[312])
def l482_262(x):
    # x is a list (or vector) of length 400
    return max(0, x[308])
def l482_263(x):
    # x is a list (or vector) of length 400
    return max(0, x[304])
def l482_264(x):
    # x is a list (or vector) of length 400
    return max(0, x[333])
def l482_265(x):
    # x is a list (or vector) of length 400
    return max(0, x[329])
def l482_266(x):
    # x is a list (or vector) of length 400
    return max(0, x[325])
def l482_267(x):
    # x is a list (or vector) of length 400
    return max(0, x[321])
def l482_268(x):
    # x is a list (or vector) of length 400
    return max(0, x[317])
def l482_269(x):
    # x is a list (or vector) of length 400
    return max(0, x[313])
def l482_270(x):
    # x is a list (or vector) of length 400
    return max(0, x[309])
def l482_271(x):
    # x is a list (or vector) of length 400
    return max(0, x[305])
def l482_272(x):
    # x is a list (or vector) of length 400
    return max(0, x[334])
def l482_273(x):
    # x is a list (or vector) of length 400
    return max(0, x[330])
def l482_274(x):
    # x is a list (or vector) of length 400
    return max(0, x[326])
def l482_275(x):
    # x is a list (or vector) of length 400
    return max(0, x[322])
def l482_276(x):
    # x is a list (or vector) of length 400
    return max(0, x[318])
def l482_277(x):
    # x is a list (or vector) of length 400
    return max(0, x[314])
def l482_278(x):
    # x is a list (or vector) of length 400
    return max(0, x[310])
def l482_279(x):
    # x is a list (or vector) of length 400
    return max(0, x[306])
def l482_280(x):
    # x is a list (or vector) of length 400
    return max(0, x[335])
def l482_281(x):
    # x is a list (or vector) of length 400
    return max(0, x[331])
def l482_282(x):
    # x is a list (or vector) of length 400
    return max(0, x[327])
def l482_283(x):
    # x is a list (or vector) of length 400
    return max(0, x[323])
def l482_284(x):
    # x is a list (or vector) of length 400
    return max(0, x[319])
def l482_285(x):
    # x is a list (or vector) of length 400
    return max(0, x[315])
def l482_286(x):
    # x is a list (or vector) of length 400
    return max(0, x[311])
def l482_287(x):
    # x is a list (or vector) of length 400
    return max(0, x[307])
def l482_288(x):
    # x is a list (or vector) of length 400
    return max(0, x[336])
def l482_289(x):
    # x is a list (or vector) of length 400
    return max(0, x[337])
def l482_290(x):
    # x is a list (or vector) of length 400
    return max(0, x[338])
def l482_291(x):
    # x is a list (or vector) of length 400
    return max(0, x[339])
def l482_292(x):
    # x is a list (or vector) of length 400
    return max(0, x[340])
def l482_293(x):
    # x is a list (or vector) of length 400
    return max(0, x[341])
def l482_294(x):
    # x is a list (or vector) of length 400
    return max(0, x[342])
def l482_295(x):
    # x is a list (or vector) of length 400
    return max(0, x[343])
def l482_296(x):
    # x is a list (or vector) of length 400
    return max(0, x[344])
def l482_297(x):
    # x is a list (or vector) of length 400
    return max(0, x[345])
def l482_298(x):
    # x is a list (or vector) of length 400
    return max(0, x[346])
def l482_299(x):
    # x is a list (or vector) of length 400
    return max(0, x[347])
def l482_300(x):
    # x is a list (or vector) of length 400
    return max(0, x[348])
def l482_301(x):
    # x is a list (or vector) of length 400
    return max(0, x[349])
def l482_302(x):
    # x is a list (or vector) of length 400
    return max(0, x[350])
def l482_303(x):
    # x is a list (or vector) of length 400
    return max(0, x[351])
def l482_304(x):
    # x is a list (or vector) of length 400
    return max(0, x[352])
def l482_305(x):
    # x is a list (or vector) of length 400
    return max(0, x[353])
def l482_306(x):
    # x is a list (or vector) of length 400
    return max(0, x[354])
def l482_307(x):
    # x is a list (or vector) of length 400
    return max(0, x[355])
def l482_308(x):
    # x is a list (or vector) of length 400
    return max(0, x[356])
def l482_309(x):
    # x is a list (or vector) of length 400
    return max(0, x[357])
def l482_310(x):
    # x is a list (or vector) of length 400
    return max(0, x[358])
def l482_311(x):
    # x is a list (or vector) of length 400
    return max(0, x[359])
def l482_312(x):
    # x is a list (or vector) of length 400
    return max(0, x[360])
def l482_313(x):
    # x is a list (or vector) of length 400
    return max(0, x[361])
def l482_314(x):
    # x is a list (or vector) of length 400
    return max(0, x[362])
def l482_315(x):
    # x is a list (or vector) of length 400
    return max(0, x[363])
def l482_316(x):
    # x is a list (or vector) of length 400
    return max(0, x[364])
def l482_317(x):
    # x is a list (or vector) of length 400
    return max(0, x[365])
def l482_318(x):
    # x is a list (or vector) of length 400
    return max(0, x[366])
def l482_319(x):
    # x is a list (or vector) of length 400
    return max(0, x[367])
def l482_320(x):
    # x is a list (or vector) of length 400
    return max(0, x[368])
def l482_321(x):
    # x is a list (or vector) of length 400
    return max(0, x[369])
def l482_322(x):
    # x is a list (or vector) of length 400
    return max(0, x[370])
def l482_323(x):
    # x is a list (or vector) of length 400
    return max(0, x[371])
def l482_324(x):
    # x is a list (or vector) of length 400
    return max(0, x[372])
def l482_325(x):
    # x is a list (or vector) of length 400
    return max(0, x[373])
def l482_326(x):
    # x is a list (or vector) of length 400
    return max(0, x[374])
def l482_327(x):
    # x is a list (or vector) of length 400
    return max(0, x[375])
def l482_328(x):
    # x is a list (or vector) of length 400
    return max(0, x[376])
def l482_329(x):
    # x is a list (or vector) of length 400
    return max(0, x[377])
def l482_330(x):
    # x is a list (or vector) of length 400
    return max(0, x[378])
def l482_331(x):
    # x is a list (or vector) of length 400
    return max(0, x[379])
def l482_332(x):
    # x is a list (or vector) of length 400
    return max(0, x[380])
def l482_333(x):
    # x is a list (or vector) of length 400
    return max(0, x[381])
def l482_334(x):
    # x is a list (or vector) of length 400
    return max(0, x[382])
def l482_335(x):
    # x is a list (or vector) of length 400
    return max(0, x[383])
def l482_336(x):
    # x is a list (or vector) of length 400
    return max(0, x[384])
def l482_337(x):
    # x is a list (or vector) of length 400
    return max(0, x[385])
def l482_338(x):
    # x is a list (or vector) of length 400
    return max(0, x[386])
def l482_339(x):
    # x is a list (or vector) of length 400
    return max(0, x[387])
def l482_340(x):
    # x is a list (or vector) of length 400
    return max(0, x[388])
def l482_341(x):
    # x is a list (or vector) of length 400
    return max(0, x[389])
def l482_342(x):
    # x is a list (or vector) of length 400
    return max(0, x[390])
def l482_343(x):
    # x is a list (or vector) of length 400
    return max(0, x[391])
def l482_344(x):
    # x is a list (or vector) of length 400
    return max(0, x[392])
def l482_345(x):
    # x is a list (or vector) of length 400
    return max(0, x[393])
def l482_346(x):
    # x is a list (or vector) of length 400
    return max(0, x[394])
def l482_347(x):
    # x is a list (or vector) of length 400
    return max(0, x[395])
def l482_348(x):
    # x is a list (or vector) of length 400
    return max(0, x[396])
def l482_349(x):
    # x is a list (or vector) of length 400
    return max(0, x[397])
def l482_350(x):
    # x is a list (or vector) of length 400
    return max(0, x[398])
def l482_351(x):
    # x is a list (or vector) of length 400
    return max(0, x[399])
def l482_(x):
    # x is a list (or vector) of length 400
    return [
        l482_0(x),
        l482_1(x),
        l482_2(x),
        l482_3(x),
        l482_4(x),
        l482_5(x),
        l482_6(x),
        l482_7(x),
        l482_8(x),
        l482_9(x),
        l482_10(x),
        l482_11(x),
        l482_12(x),
        l482_13(x),
        l482_14(x),
        l482_15(x),
        l482_16(x),
        l482_17(x),
        l482_18(x),
        l482_19(x),
        l482_20(x),
        l482_21(x),
        l482_22(x),
        l482_23(x),
        l482_24(x),
        l482_25(x),
        l482_26(x),
        l482_27(x),
        l482_28(x),
        l482_29(x),
        l482_30(x),
        l482_31(x),
        l482_32(x),
        l482_33(x),
        l482_34(x),
        l482_35(x),
        l482_36(x),
        l482_37(x),
        l482_38(x),
        l482_39(x),
        l482_40(x),
        l482_41(x),
        l482_42(x),
        l482_43(x),
        l482_44(x),
        l482_45(x),
        l482_46(x),
        l482_47(x),
        l482_48(x),
        l482_49(x),
        l482_50(x),
        l482_51(x),
        l482_52(x),
        l482_53(x),
        l482_54(x),
        l482_55(x),
        l482_56(x),
        l482_57(x),
        l482_58(x),
        l482_59(x),
        l482_60(x),
        l482_61(x),
        l482_62(x),
        l482_63(x),
        l482_64(x),
        l482_65(x),
        l482_66(x),
        l482_67(x),
        l482_68(x),
        l482_69(x),
        l482_70(x),
        l482_71(x),
        l482_72(x),
        l482_73(x),
        l482_74(x),
        l482_75(x),
        l482_76(x),
        l482_77(x),
        l482_78(x),
        l482_79(x),
        l482_80(x),
        l482_81(x),
        l482_82(x),
        l482_83(x),
        l482_84(x),
        l482_85(x),
        l482_86(x),
        l482_87(x),
        l482_88(x),
        l482_89(x),
        l482_90(x),
        l482_91(x),
        l482_92(x),
        l482_93(x),
        l482_94(x),
        l482_95(x),
        l482_96(x),
        l482_97(x),
        l482_98(x),
        l482_99(x),
        l482_100(x),
        l482_101(x),
        l482_102(x),
        l482_103(x),
        l482_104(x),
        l482_105(x),
        l482_106(x),
        l482_107(x),
        l482_108(x),
        l482_109(x),
        l482_110(x),
        l482_111(x),
        l482_112(x),
        l482_113(x),
        l482_114(x),
        l482_115(x),
        l482_116(x),
        l482_117(x),
        l482_118(x),
        l482_119(x),
        l482_120(x),
        l482_121(x),
        l482_122(x),
        l482_123(x),
        l482_124(x),
        l482_125(x),
        l482_126(x),
        l482_127(x),
        l482_128(x),
        l482_129(x),
        l482_130(x),
        l482_131(x),
        l482_132(x),
        l482_133(x),
        l482_134(x),
        l482_135(x),
        l482_136(x),
        l482_137(x),
        l482_138(x),
        l482_139(x),
        l482_140(x),
        l482_141(x),
        l482_142(x),
        l482_143(x),
        l482_144(x),
        l482_145(x),
        l482_146(x),
        l482_147(x),
        l482_148(x),
        l482_149(x),
        l482_150(x),
        l482_151(x),
        l482_152(x),
        l482_153(x),
        l482_154(x),
        l482_155(x),
        l482_156(x),
        l482_157(x),
        l482_158(x),
        l482_159(x),
        l482_160(x),
        l482_161(x),
        l482_162(x),
        l482_163(x),
        l482_164(x),
        l482_165(x),
        l482_166(x),
        l482_167(x),
        l482_168(x),
        l482_169(x),
        l482_170(x),
        l482_171(x),
        l482_172(x),
        l482_173(x),
        l482_174(x),
        l482_175(x),
        l482_176(x),
        l482_177(x),
        l482_178(x),
        l482_179(x),
        l482_180(x),
        l482_181(x),
        l482_182(x),
        l482_183(x),
        l482_184(x),
        l482_185(x),
        l482_186(x),
        l482_187(x),
        l482_188(x),
        l482_189(x),
        l482_190(x),
        l482_191(x),
        l482_192(x),
        l482_193(x),
        l482_194(x),
        l482_195(x),
        l482_196(x),
        l482_197(x),
        l482_198(x),
        l482_199(x),
        l482_200(x),
        l482_201(x),
        l482_202(x),
        l482_203(x),
        l482_204(x),
        l482_205(x),
        l482_206(x),
        l482_207(x),
        l482_208(x),
        l482_209(x),
        l482_210(x),
        l482_211(x),
        l482_212(x),
        l482_213(x),
        l482_214(x),
        l482_215(x),
        l482_216(x),
        l482_217(x),
        l482_218(x),
        l482_219(x),
        l482_220(x),
        l482_221(x),
        l482_222(x),
        l482_223(x),
        l482_224(x),
        l482_225(x),
        l482_226(x),
        l482_227(x),
        l482_228(x),
        l482_229(x),
        l482_230(x),
        l482_231(x),
        l482_232(x),
        l482_233(x),
        l482_234(x),
        l482_235(x),
        l482_236(x),
        l482_237(x),
        l482_238(x),
        l482_239(x),
        l482_240(x),
        l482_241(x),
        l482_242(x),
        l482_243(x),
        l482_244(x),
        l482_245(x),
        l482_246(x),
        l482_247(x),
        l482_248(x),
        l482_249(x),
        l482_250(x),
        l482_251(x),
        l482_252(x),
        l482_253(x),
        l482_254(x),
        l482_255(x),
        l482_256(x),
        l482_257(x),
        l482_258(x),
        l482_259(x),
        l482_260(x),
        l482_261(x),
        l482_262(x),
        l482_263(x),
        l482_264(x),
        l482_265(x),
        l482_266(x),
        l482_267(x),
        l482_268(x),
        l482_269(x),
        l482_270(x),
        l482_271(x),
        l482_272(x),
        l482_273(x),
        l482_274(x),
        l482_275(x),
        l482_276(x),
        l482_277(x),
        l482_278(x),
        l482_279(x),
        l482_280(x),
        l482_281(x),
        l482_282(x),
        l482_283(x),
        l482_284(x),
        l482_285(x),
        l482_286(x),
        l482_287(x),
        l482_288(x),
        l482_289(x),
        l482_290(x),
        l482_291(x),
        l482_292(x),
        l482_293(x),
        l482_294(x),
        l482_295(x),
        l482_296(x),
        l482_297(x),
        l482_298(x),
        l482_299(x),
        l482_300(x),
        l482_301(x),
        l482_302(x),
        l482_303(x),
        l482_304(x),
        l482_305(x),
        l482_306(x),
        l482_307(x),
        l482_308(x),
        l482_309(x),
        l482_310(x),
        l482_311(x),
        l482_312(x),
        l482_313(x),
        l482_314(x),
        l482_315(x),
        l482_316(x),
        l482_317(x),
        l482_318(x),
        l482_319(x),
        l482_320(x),
        l482_321(x),
        l482_322(x),
        l482_323(x),
        l482_324(x),
        l482_325(x),
        l482_326(x),
        l482_327(x),
        l482_328(x),
        l482_329(x),
        l482_330(x),
        l482_331(x),
        l482_332(x),
        l482_333(x),
        l482_334(x),
        l482_335(x),
        l482_336(x),
        l482_337(x),
        l482_338(x),
        l482_339(x),
        l482_340(x),
        l482_341(x),
        l482_342(x),
        l482_343(x),
        l482_344(x),
        l482_345(x),
        l482_346(x),
        l482_347(x),
        l482_348(x),
        l482_349(x),
        l482_350(x),
        l482_351(x),
    ]