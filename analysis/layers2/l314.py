import numpy as np




# Generated from reverse engineering
def l314_g(x: np.ndarray) -> np.ndarray:
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




def l314_0(x):
    # x is a list (or vector) of length 400
    return max(0, x[0])
def l314_1(x):
    # x is a list (or vector) of length 400
    return max(0, x[1])
def l314_2(x):
    # x is a list (or vector) of length 400
    return max(0, x[2])
def l314_3(x):
    # x is a list (or vector) of length 400
    return max(0, x[3])
def l314_4(x):
    # x is a list (or vector) of length 400
    return max(0, x[4])
def l314_5(x):
    # x is a list (or vector) of length 400
    return max(0, x[5])
def l314_6(x):
    # x is a list (or vector) of length 400
    return max(0, x[6])
def l314_7(x):
    # x is a list (or vector) of length 400
    return max(0, x[7])
def l314_8(x):
    # x is a list (or vector) of length 400
    return max(0, x[8])
def l314_9(x):
    # x is a list (or vector) of length 400
    return max(0, x[9])
def l314_10(x):
    # x is a list (or vector) of length 400
    return max(0, x[10])
def l314_11(x):
    # x is a list (or vector) of length 400
    return max(0, x[11])
def l314_12(x):
    # x is a list (or vector) of length 400
    return max(0, x[12])
def l314_13(x):
    # x is a list (or vector) of length 400
    return max(0, x[13])
def l314_14(x):
    # x is a list (or vector) of length 400
    return max(0, x[14])
def l314_15(x):
    # x is a list (or vector) of length 400
    return max(0, x[15])
def l314_16(x):
    # x is a list (or vector) of length 400
    return max(0, x[16])
def l314_17(x):
    # x is a list (or vector) of length 400
    return max(0, x[17])
def l314_18(x):
    # x is a list (or vector) of length 400
    return max(0, x[18])
def l314_19(x):
    # x is a list (or vector) of length 400
    return max(0, x[19])
def l314_20(x):
    # x is a list (or vector) of length 400
    return max(0, x[20])
def l314_21(x):
    # x is a list (or vector) of length 400
    return max(0, x[21])
def l314_22(x):
    # x is a list (or vector) of length 400
    return max(0, x[22])
def l314_23(x):
    # x is a list (or vector) of length 400
    return max(0, x[23])
def l314_24(x):
    # x is a list (or vector) of length 400
    return max(0, x[24])
def l314_25(x):
    # x is a list (or vector) of length 400
    return max(0, x[25])
def l314_26(x):
    # x is a list (or vector) of length 400
    return max(0, x[26])
def l314_27(x):
    # x is a list (or vector) of length 400
    return max(0, x[27])
def l314_28(x):
    # x is a list (or vector) of length 400
    return max(0, x[28])
def l314_29(x):
    # x is a list (or vector) of length 400
    return max(0, x[29])
def l314_30(x):
    # x is a list (or vector) of length 400
    return max(0, x[30])
def l314_31(x):
    # x is a list (or vector) of length 400
    return max(0, x[31])
def l314_32(x):
    # x is a list (or vector) of length 400
    return max(0, x[32])
def l314_33(x):
    # x is a list (or vector) of length 400
    return max(0, x[33])
def l314_34(x):
    # x is a list (or vector) of length 400
    return max(0, x[34])
def l314_35(x):
    # x is a list (or vector) of length 400
    return max(0, x[35])
def l314_36(x):
    # x is a list (or vector) of length 400
    return max(0, x[36])
def l314_37(x):
    # x is a list (or vector) of length 400
    return max(0, x[37])
def l314_38(x):
    # x is a list (or vector) of length 400
    return max(0, x[38])
def l314_39(x):
    # x is a list (or vector) of length 400
    return max(0, x[39])
def l314_40(x):
    # x is a list (or vector) of length 400
    return max(0, x[40])
def l314_41(x):
    # x is a list (or vector) of length 400
    return max(0, x[41])
def l314_42(x):
    # x is a list (or vector) of length 400
    return max(0, x[42])
def l314_43(x):
    # x is a list (or vector) of length 400
    return max(0, x[43])
def l314_44(x):
    # x is a list (or vector) of length 400
    return max(0, x[44])
def l314_45(x):
    # x is a list (or vector) of length 400
    return max(0, x[45])
def l314_46(x):
    # x is a list (or vector) of length 400
    return max(0, x[46])
def l314_47(x):
    # x is a list (or vector) of length 400
    return max(0, x[47])
def l314_48(x):
    # x is a list (or vector) of length 400
    return max(0, x[48])
def l314_49(x):
    # x is a list (or vector) of length 400
    return max(0, x[49])
def l314_50(x):
    # x is a list (or vector) of length 400
    return max(0, x[50])
def l314_51(x):
    # x is a list (or vector) of length 400
    return max(0, x[51])
def l314_52(x):
    # x is a list (or vector) of length 400
    return max(0, x[52])
def l314_53(x):
    # x is a list (or vector) of length 400
    return max(0, x[53])
def l314_54(x):
    # x is a list (or vector) of length 400
    return max(0, x[54])
def l314_55(x):
    # x is a list (or vector) of length 400
    return max(0, x[55])
def l314_56(x):
    # x is a list (or vector) of length 400
    return max(0, x[56])
def l314_57(x):
    # x is a list (or vector) of length 400
    return max(0, x[57])
def l314_58(x):
    # x is a list (or vector) of length 400
    return max(0, x[58])
def l314_59(x):
    # x is a list (or vector) of length 400
    return max(0, x[59])
def l314_60(x):
    # x is a list (or vector) of length 400
    return max(0, x[60])
def l314_61(x):
    # x is a list (or vector) of length 400
    return max(0, x[61])
def l314_62(x):
    # x is a list (or vector) of length 400
    return max(0, x[62])
def l314_63(x):
    # x is a list (or vector) of length 400
    return max(0, x[63])
def l314_64(x):
    # x is a list (or vector) of length 400
    return max(0, x[64])
def l314_65(x):
    # x is a list (or vector) of length 400
    return max(0, x[65])
def l314_66(x):
    # x is a list (or vector) of length 400
    return max(0, x[66])
def l314_67(x):
    # x is a list (or vector) of length 400
    return max(0, x[67])
def l314_68(x):
    # x is a list (or vector) of length 400
    return max(0, x[68])
def l314_69(x):
    # x is a list (or vector) of length 400
    return max(0, x[69])
def l314_70(x):
    # x is a list (or vector) of length 400
    return max(0, x[70])
def l314_71(x):
    # x is a list (or vector) of length 400
    return max(0, x[71])
def l314_72(x):
    # x is a list (or vector) of length 400
    return max(0, x[72])
def l314_73(x):
    # x is a list (or vector) of length 400
    return max(0, x[73])
def l314_74(x):
    # x is a list (or vector) of length 400
    return max(0, x[74])
def l314_75(x):
    # x is a list (or vector) of length 400
    return max(0, x[75])
def l314_76(x):
    # x is a list (or vector) of length 400
    return max(0, x[76])
def l314_77(x):
    # x is a list (or vector) of length 400
    return max(0, x[77])
def l314_78(x):
    # x is a list (or vector) of length 400
    return max(0, x[78])
def l314_79(x):
    # x is a list (or vector) of length 400
    return max(0, x[79])
def l314_80(x):
    # x is a list (or vector) of length 400
    return max(0, x[80])
def l314_81(x):
    # x is a list (or vector) of length 400
    return max(0, x[81])
def l314_82(x):
    # x is a list (or vector) of length 400
    return max(0, x[82])
def l314_83(x):
    # x is a list (or vector) of length 400
    return max(0, x[83])
def l314_84(x):
    # x is a list (or vector) of length 400
    return max(0, x[84])
def l314_85(x):
    # x is a list (or vector) of length 400
    return max(0, x[85])
def l314_86(x):
    # x is a list (or vector) of length 400
    return max(0, x[86])
def l314_87(x):
    # x is a list (or vector) of length 400
    return max(0, x[87])
def l314_88(x):
    # x is a list (or vector) of length 400
    return max(0, x[88])
def l314_89(x):
    # x is a list (or vector) of length 400
    return max(0, x[89])
def l314_90(x):
    # x is a list (or vector) of length 400
    return max(0, x[90])
def l314_91(x):
    # x is a list (or vector) of length 400
    return max(0, x[91])
def l314_92(x):
    # x is a list (or vector) of length 400
    return max(0, x[92])
def l314_93(x):
    # x is a list (or vector) of length 400
    return max(0, x[93])
def l314_94(x):
    # x is a list (or vector) of length 400
    return max(0, x[94])
def l314_95(x):
    # x is a list (or vector) of length 400
    return max(0, x[95])
def l314_96(x):
    # x is a list (or vector) of length 400
    return max(0, x[96])
def l314_97(x):
    # x is a list (or vector) of length 400
    return max(0, x[97])
def l314_98(x):
    # x is a list (or vector) of length 400
    return max(0, x[98])
def l314_99(x):
    # x is a list (or vector) of length 400
    return max(0, x[99])
def l314_100(x):
    # x is a list (or vector) of length 400
    return max(0, x[100])
def l314_101(x):
    # x is a list (or vector) of length 400
    return max(0, x[101])
def l314_102(x):
    # x is a list (or vector) of length 400
    return max(0, x[102])
def l314_103(x):
    # x is a list (or vector) of length 400
    return max(0, x[103])
def l314_104(x):
    # x is a list (or vector) of length 400
    return max(0, x[104])
def l314_105(x):
    # x is a list (or vector) of length 400
    return max(0, x[105])
def l314_106(x):
    # x is a list (or vector) of length 400
    return max(0, x[106])
def l314_107(x):
    # x is a list (or vector) of length 400
    return max(0, x[107])
def l314_108(x):
    # x is a list (or vector) of length 400
    return max(0, x[108])
def l314_109(x):
    # x is a list (or vector) of length 400
    return max(0, x[109])
def l314_110(x):
    # x is a list (or vector) of length 400
    return max(0, x[110])
def l314_111(x):
    # x is a list (or vector) of length 400
    return max(0, x[111])
def l314_112(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[112] + -1.0*x[128] + 1.0)
def l314_113(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[113] + -1.0*x[129] + 1.0)
def l314_114(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[114] + -1.0*x[130] + 1.0)
def l314_115(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[115] + -1.0*x[131] + 1.0)
def l314_116(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[116] + -1.0*x[132] + 1.0)
def l314_117(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[117] + -1.0*x[133] + 1.0)
def l314_118(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[118] + -1.0*x[134] + 1.0)
def l314_119(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[119] + -1.0*x[135] + 1.0)
def l314_120(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[120] + -1.0*x[136] + 1.0)
def l314_121(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[121] + -1.0*x[137] + 1.0)
def l314_122(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[122] + -1.0*x[138] + 1.0)
def l314_123(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[123] + -1.0*x[139] + 1.0)
def l314_124(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[124] + -1.0*x[140] + 1.0)
def l314_125(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[125] + -1.0*x[141] + 1.0)
def l314_126(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[126] + -1.0*x[142] + 1.0)
def l314_127(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[127] + -1.0*x[143] + 1.0)
def l314_128(x):
    # x is a list (or vector) of length 400
    return max(0, x[160])
def l314_129(x):
    # x is a list (or vector) of length 400
    return max(0, x[161])
def l314_130(x):
    # x is a list (or vector) of length 400
    return max(0, x[162])
def l314_131(x):
    # x is a list (or vector) of length 400
    return max(0, x[163])
def l314_132(x):
    # x is a list (or vector) of length 400
    return max(0, x[164])
def l314_133(x):
    # x is a list (or vector) of length 400
    return max(0, x[165])
def l314_134(x):
    # x is a list (or vector) of length 400
    return max(0, x[166])
def l314_135(x):
    # x is a list (or vector) of length 400
    return max(0, x[167])
def l314_136(x):
    # x is a list (or vector) of length 400
    return max(0, x[168])
def l314_137(x):
    # x is a list (or vector) of length 400
    return max(0, x[169])
def l314_138(x):
    # x is a list (or vector) of length 400
    return max(0, x[170])
def l314_139(x):
    # x is a list (or vector) of length 400
    return max(0, x[171])
def l314_140(x):
    # x is a list (or vector) of length 400
    return max(0, x[172])
def l314_141(x):
    # x is a list (or vector) of length 400
    return max(0, x[173])
def l314_142(x):
    # x is a list (or vector) of length 400
    return max(0, x[174])
def l314_143(x):
    # x is a list (or vector) of length 400
    return max(0, x[175])
def l314_144(x):
    # x is a list (or vector) of length 400
    return max(0, x[144])
def l314_145(x):
    # x is a list (or vector) of length 400
    return max(0, x[145])
def l314_146(x):
    # x is a list (or vector) of length 400
    return max(0, x[146])
def l314_147(x):
    # x is a list (or vector) of length 400
    return max(0, x[147])
def l314_148(x):
    # x is a list (or vector) of length 400
    return max(0, x[148])
def l314_149(x):
    # x is a list (or vector) of length 400
    return max(0, x[149])
def l314_150(x):
    # x is a list (or vector) of length 400
    return max(0, x[150])
def l314_151(x):
    # x is a list (or vector) of length 400
    return max(0, x[151])
def l314_152(x):
    # x is a list (or vector) of length 400
    return max(0, x[152])
def l314_153(x):
    # x is a list (or vector) of length 400
    return max(0, x[153])
def l314_154(x):
    # x is a list (or vector) of length 400
    return max(0, x[154])
def l314_155(x):
    # x is a list (or vector) of length 400
    return max(0, x[155])
def l314_156(x):
    # x is a list (or vector) of length 400
    return max(0, x[156])
def l314_157(x):
    # x is a list (or vector) of length 400
    return max(0, x[157])
def l314_158(x):
    # x is a list (or vector) of length 400
    return max(0, x[158])
def l314_159(x):
    # x is a list (or vector) of length 400
    return max(0, x[159])
def l314_160(x):
    # x is a list (or vector) of length 400
    return max(0, x[176])
def l314_161(x):
    # x is a list (or vector) of length 400
    return max(0, x[177])
def l314_162(x):
    # x is a list (or vector) of length 400
    return max(0, x[178])
def l314_163(x):
    # x is a list (or vector) of length 400
    return max(0, x[179])
def l314_164(x):
    # x is a list (or vector) of length 400
    return max(0, x[180])
def l314_165(x):
    # x is a list (or vector) of length 400
    return max(0, x[181])
def l314_166(x):
    # x is a list (or vector) of length 400
    return max(0, x[182])
def l314_167(x):
    # x is a list (or vector) of length 400
    return max(0, x[183])
def l314_168(x):
    # x is a list (or vector) of length 400
    return max(0, x[184])
def l314_169(x):
    # x is a list (or vector) of length 400
    return max(0, x[185])
def l314_170(x):
    # x is a list (or vector) of length 400
    return max(0, x[186])
def l314_171(x):
    # x is a list (or vector) of length 400
    return max(0, x[187])
def l314_172(x):
    # x is a list (or vector) of length 400
    return max(0, x[188])
def l314_173(x):
    # x is a list (or vector) of length 400
    return max(0, x[189])
def l314_174(x):
    # x is a list (or vector) of length 400
    return max(0, x[190])
def l314_175(x):
    # x is a list (or vector) of length 400
    return max(0, x[191])
def l314_176(x):
    # x is a list (or vector) of length 400
    return max(0, x[192])
def l314_177(x):
    # x is a list (or vector) of length 400
    return max(0, x[193])
def l314_178(x):
    # x is a list (or vector) of length 400
    return max(0, x[194])
def l314_179(x):
    # x is a list (or vector) of length 400
    return max(0, x[195])
def l314_180(x):
    # x is a list (or vector) of length 400
    return max(0, x[196])
def l314_181(x):
    # x is a list (or vector) of length 400
    return max(0, x[197])
def l314_182(x):
    # x is a list (or vector) of length 400
    return max(0, x[198])
def l314_183(x):
    # x is a list (or vector) of length 400
    return max(0, x[199])
def l314_184(x):
    # x is a list (or vector) of length 400
    return max(0, x[200])
def l314_185(x):
    # x is a list (or vector) of length 400
    return max(0, x[201])
def l314_186(x):
    # x is a list (or vector) of length 400
    return max(0, x[202])
def l314_187(x):
    # x is a list (or vector) of length 400
    return max(0, x[203])
def l314_188(x):
    # x is a list (or vector) of length 400
    return max(0, x[204])
def l314_189(x):
    # x is a list (or vector) of length 400
    return max(0, x[205])
def l314_190(x):
    # x is a list (or vector) of length 400
    return max(0, x[206])
def l314_191(x):
    # x is a list (or vector) of length 400
    return max(0, x[207])
def l314_192(x):
    # x is a list (or vector) of length 400
    return max(0, x[272])
def l314_193(x):
    # x is a list (or vector) of length 400
    return max(0, x[208] + x[273])
def l314_194(x):
    # x is a list (or vector) of length 400
    return max(0, x[209] + x[274])
def l314_195(x):
    # x is a list (or vector) of length 400
    return max(0, x[210] + x[275])
def l314_196(x):
    # x is a list (or vector) of length 400
    return max(0, x[211] + x[276])
def l314_197(x):
    # x is a list (or vector) of length 400
    return max(0, x[212] + x[277])
def l314_198(x):
    # x is a list (or vector) of length 400
    return max(0, x[213] + x[278])
def l314_199(x):
    # x is a list (or vector) of length 400
    return max(0, x[214] + x[279])
def l314_200(x):
    # x is a list (or vector) of length 400
    return max(0, x[215] + x[280])
def l314_201(x):
    # x is a list (or vector) of length 400
    return max(0, x[216] + x[281])
def l314_202(x):
    # x is a list (or vector) of length 400
    return max(0, x[217] + x[282])
def l314_203(x):
    # x is a list (or vector) of length 400
    return max(0, x[218] + x[283])
def l314_204(x):
    # x is a list (or vector) of length 400
    return max(0, x[219] + x[284])
def l314_205(x):
    # x is a list (or vector) of length 400
    return max(0, x[220] + x[285])
def l314_206(x):
    # x is a list (or vector) of length 400
    return max(0, x[221] + x[286])
def l314_207(x):
    # x is a list (or vector) of length 400
    return max(0, x[222] + x[287])
def l314_208(x):
    # x is a list (or vector) of length 400
    return max(0, x[223] + x[288])
def l314_209(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[224] + x[289] + 1.0)
def l314_210(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[225] + x[290] + 1.0)
def l314_211(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[226] + x[291] + 1.0)
def l314_212(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[227] + x[292] + 1.0)
def l314_213(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[228] + x[293] + 1.0)
def l314_214(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[229] + x[294] + 1.0)
def l314_215(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[230] + x[295] + 1.0)
def l314_216(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[231] + x[296] + 1.0)
def l314_217(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[232] + x[297] + 1.0)
def l314_218(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[233] + x[298] + 1.0)
def l314_219(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[234] + x[299] + 1.0)
def l314_220(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[235] + x[300] + 1.0)
def l314_221(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[236] + x[301] + 1.0)
def l314_222(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[237] + x[302] + 1.0)
def l314_223(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[238] + x[303] + 1.0)
def l314_224(x):
    # x is a list (or vector) of length 400
    return max(0, x[272] + -1.0)
def l314_225(x):
    # x is a list (or vector) of length 400
    return max(0, x[208] + x[273] + -1.0)
def l314_226(x):
    # x is a list (or vector) of length 400
    return max(0, x[209] + x[274] + -1.0)
def l314_227(x):
    # x is a list (or vector) of length 400
    return max(0, x[210] + x[275] + -1.0)
def l314_228(x):
    # x is a list (or vector) of length 400
    return max(0, x[211] + x[276] + -1.0)
def l314_229(x):
    # x is a list (or vector) of length 400
    return max(0, x[212] + x[277] + -1.0)
def l314_230(x):
    # x is a list (or vector) of length 400
    return max(0, x[213] + x[278] + -1.0)
def l314_231(x):
    # x is a list (or vector) of length 400
    return max(0, x[214] + x[279] + -1.0)
def l314_232(x):
    # x is a list (or vector) of length 400
    return max(0, x[215] + x[280] + -1.0)
def l314_233(x):
    # x is a list (or vector) of length 400
    return max(0, x[216] + x[281] + -1.0)
def l314_234(x):
    # x is a list (or vector) of length 400
    return max(0, x[217] + x[282] + -1.0)
def l314_235(x):
    # x is a list (or vector) of length 400
    return max(0, x[218] + x[283] + -1.0)
def l314_236(x):
    # x is a list (or vector) of length 400
    return max(0, x[219] + x[284] + -1.0)
def l314_237(x):
    # x is a list (or vector) of length 400
    return max(0, x[220] + x[285] + -1.0)
def l314_238(x):
    # x is a list (or vector) of length 400
    return max(0, x[221] + x[286] + -1.0)
def l314_239(x):
    # x is a list (or vector) of length 400
    return max(0, x[222] + x[287] + -1.0)
def l314_240(x):
    # x is a list (or vector) of length 400
    return max(0, x[223] + x[288] + -1.0)
def l314_241(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[224] + x[289])
def l314_242(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[225] + x[290])
def l314_243(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[226] + x[291])
def l314_244(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[227] + x[292])
def l314_245(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[228] + x[293])
def l314_246(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[229] + x[294])
def l314_247(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[230] + x[295])
def l314_248(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[231] + x[296])
def l314_249(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[232] + x[297])
def l314_250(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[233] + x[298])
def l314_251(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[234] + x[299])
def l314_252(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[235] + x[300])
def l314_253(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[236] + x[301])
def l314_254(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[237] + x[302])
def l314_255(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[238] + x[303])
def l314_256(x):
    # x is a list (or vector) of length 400
    return max(0, x[332])
def l314_257(x):
    # x is a list (or vector) of length 400
    return max(0, x[328])
def l314_258(x):
    # x is a list (or vector) of length 400
    return max(0, x[324])
def l314_259(x):
    # x is a list (or vector) of length 400
    return max(0, x[320])
def l314_260(x):
    # x is a list (or vector) of length 400
    return max(0, x[316])
def l314_261(x):
    # x is a list (or vector) of length 400
    return max(0, x[312])
def l314_262(x):
    # x is a list (or vector) of length 400
    return max(0, x[308])
def l314_263(x):
    # x is a list (or vector) of length 400
    return max(0, x[304])
def l314_264(x):
    # x is a list (or vector) of length 400
    return max(0, x[333])
def l314_265(x):
    # x is a list (or vector) of length 400
    return max(0, x[329])
def l314_266(x):
    # x is a list (or vector) of length 400
    return max(0, x[325])
def l314_267(x):
    # x is a list (or vector) of length 400
    return max(0, x[321])
def l314_268(x):
    # x is a list (or vector) of length 400
    return max(0, x[317])
def l314_269(x):
    # x is a list (or vector) of length 400
    return max(0, x[313])
def l314_270(x):
    # x is a list (or vector) of length 400
    return max(0, x[309])
def l314_271(x):
    # x is a list (or vector) of length 400
    return max(0, x[305])
def l314_272(x):
    # x is a list (or vector) of length 400
    return max(0, x[334])
def l314_273(x):
    # x is a list (or vector) of length 400
    return max(0, x[330])
def l314_274(x):
    # x is a list (or vector) of length 400
    return max(0, x[326])
def l314_275(x):
    # x is a list (or vector) of length 400
    return max(0, x[322])
def l314_276(x):
    # x is a list (or vector) of length 400
    return max(0, x[318])
def l314_277(x):
    # x is a list (or vector) of length 400
    return max(0, x[314])
def l314_278(x):
    # x is a list (or vector) of length 400
    return max(0, x[310])
def l314_279(x):
    # x is a list (or vector) of length 400
    return max(0, x[306])
def l314_280(x):
    # x is a list (or vector) of length 400
    return max(0, x[335])
def l314_281(x):
    # x is a list (or vector) of length 400
    return max(0, x[331])
def l314_282(x):
    # x is a list (or vector) of length 400
    return max(0, x[327])
def l314_283(x):
    # x is a list (or vector) of length 400
    return max(0, x[323])
def l314_284(x):
    # x is a list (or vector) of length 400
    return max(0, x[319])
def l314_285(x):
    # x is a list (or vector) of length 400
    return max(0, x[315])
def l314_286(x):
    # x is a list (or vector) of length 400
    return max(0, x[311])
def l314_287(x):
    # x is a list (or vector) of length 400
    return max(0, x[307])
def l314_288(x):
    # x is a list (or vector) of length 400
    return max(0, x[336])
def l314_289(x):
    # x is a list (or vector) of length 400
    return max(0, x[337])
def l314_290(x):
    # x is a list (or vector) of length 400
    return max(0, x[338])
def l314_291(x):
    # x is a list (or vector) of length 400
    return max(0, x[339])
def l314_292(x):
    # x is a list (or vector) of length 400
    return max(0, x[340])
def l314_293(x):
    # x is a list (or vector) of length 400
    return max(0, x[341])
def l314_294(x):
    # x is a list (or vector) of length 400
    return max(0, x[342])
def l314_295(x):
    # x is a list (or vector) of length 400
    return max(0, x[343])
def l314_296(x):
    # x is a list (or vector) of length 400
    return max(0, x[344])
def l314_297(x):
    # x is a list (or vector) of length 400
    return max(0, x[345])
def l314_298(x):
    # x is a list (or vector) of length 400
    return max(0, x[346])
def l314_299(x):
    # x is a list (or vector) of length 400
    return max(0, x[347])
def l314_300(x):
    # x is a list (or vector) of length 400
    return max(0, x[348])
def l314_301(x):
    # x is a list (or vector) of length 400
    return max(0, x[349])
def l314_302(x):
    # x is a list (or vector) of length 400
    return max(0, x[350])
def l314_303(x):
    # x is a list (or vector) of length 400
    return max(0, x[351])
def l314_304(x):
    # x is a list (or vector) of length 400
    return max(0, x[352])
def l314_305(x):
    # x is a list (or vector) of length 400
    return max(0, x[353])
def l314_306(x):
    # x is a list (or vector) of length 400
    return max(0, x[354])
def l314_307(x):
    # x is a list (or vector) of length 400
    return max(0, x[355])
def l314_308(x):
    # x is a list (or vector) of length 400
    return max(0, x[356])
def l314_309(x):
    # x is a list (or vector) of length 400
    return max(0, x[357])
def l314_310(x):
    # x is a list (or vector) of length 400
    return max(0, x[358])
def l314_311(x):
    # x is a list (or vector) of length 400
    return max(0, x[359])
def l314_312(x):
    # x is a list (or vector) of length 400
    return max(0, x[360])
def l314_313(x):
    # x is a list (or vector) of length 400
    return max(0, x[361])
def l314_314(x):
    # x is a list (or vector) of length 400
    return max(0, x[362])
def l314_315(x):
    # x is a list (or vector) of length 400
    return max(0, x[363])
def l314_316(x):
    # x is a list (or vector) of length 400
    return max(0, x[364])
def l314_317(x):
    # x is a list (or vector) of length 400
    return max(0, x[365])
def l314_318(x):
    # x is a list (or vector) of length 400
    return max(0, x[366])
def l314_319(x):
    # x is a list (or vector) of length 400
    return max(0, x[367])
def l314_320(x):
    # x is a list (or vector) of length 400
    return max(0, x[368])
def l314_321(x):
    # x is a list (or vector) of length 400
    return max(0, x[369])
def l314_322(x):
    # x is a list (or vector) of length 400
    return max(0, x[370])
def l314_323(x):
    # x is a list (or vector) of length 400
    return max(0, x[371])
def l314_324(x):
    # x is a list (or vector) of length 400
    return max(0, x[372])
def l314_325(x):
    # x is a list (or vector) of length 400
    return max(0, x[373])
def l314_326(x):
    # x is a list (or vector) of length 400
    return max(0, x[374])
def l314_327(x):
    # x is a list (or vector) of length 400
    return max(0, x[375])
def l314_328(x):
    # x is a list (or vector) of length 400
    return max(0, x[376])
def l314_329(x):
    # x is a list (or vector) of length 400
    return max(0, x[377])
def l314_330(x):
    # x is a list (or vector) of length 400
    return max(0, x[378])
def l314_331(x):
    # x is a list (or vector) of length 400
    return max(0, x[379])
def l314_332(x):
    # x is a list (or vector) of length 400
    return max(0, x[380])
def l314_333(x):
    # x is a list (or vector) of length 400
    return max(0, x[381])
def l314_334(x):
    # x is a list (or vector) of length 400
    return max(0, x[382])
def l314_335(x):
    # x is a list (or vector) of length 400
    return max(0, x[383])
def l314_336(x):
    # x is a list (or vector) of length 400
    return max(0, x[384])
def l314_337(x):
    # x is a list (or vector) of length 400
    return max(0, x[385])
def l314_338(x):
    # x is a list (or vector) of length 400
    return max(0, x[386])
def l314_339(x):
    # x is a list (or vector) of length 400
    return max(0, x[387])
def l314_340(x):
    # x is a list (or vector) of length 400
    return max(0, x[388])
def l314_341(x):
    # x is a list (or vector) of length 400
    return max(0, x[389])
def l314_342(x):
    # x is a list (or vector) of length 400
    return max(0, x[390])
def l314_343(x):
    # x is a list (or vector) of length 400
    return max(0, x[391])
def l314_344(x):
    # x is a list (or vector) of length 400
    return max(0, x[392])
def l314_345(x):
    # x is a list (or vector) of length 400
    return max(0, x[393])
def l314_346(x):
    # x is a list (or vector) of length 400
    return max(0, x[394])
def l314_347(x):
    # x is a list (or vector) of length 400
    return max(0, x[395])
def l314_348(x):
    # x is a list (or vector) of length 400
    return max(0, x[396])
def l314_349(x):
    # x is a list (or vector) of length 400
    return max(0, x[397])
def l314_350(x):
    # x is a list (or vector) of length 400
    return max(0, x[398])
def l314_351(x):
    # x is a list (or vector) of length 400
    return max(0, x[399])
def l314_(x):
    # x is a list (or vector) of length 400
    return [
        l314_0(x),
        l314_1(x),
        l314_2(x),
        l314_3(x),
        l314_4(x),
        l314_5(x),
        l314_6(x),
        l314_7(x),
        l314_8(x),
        l314_9(x),
        l314_10(x),
        l314_11(x),
        l314_12(x),
        l314_13(x),
        l314_14(x),
        l314_15(x),
        l314_16(x),
        l314_17(x),
        l314_18(x),
        l314_19(x),
        l314_20(x),
        l314_21(x),
        l314_22(x),
        l314_23(x),
        l314_24(x),
        l314_25(x),
        l314_26(x),
        l314_27(x),
        l314_28(x),
        l314_29(x),
        l314_30(x),
        l314_31(x),
        l314_32(x),
        l314_33(x),
        l314_34(x),
        l314_35(x),
        l314_36(x),
        l314_37(x),
        l314_38(x),
        l314_39(x),
        l314_40(x),
        l314_41(x),
        l314_42(x),
        l314_43(x),
        l314_44(x),
        l314_45(x),
        l314_46(x),
        l314_47(x),
        l314_48(x),
        l314_49(x),
        l314_50(x),
        l314_51(x),
        l314_52(x),
        l314_53(x),
        l314_54(x),
        l314_55(x),
        l314_56(x),
        l314_57(x),
        l314_58(x),
        l314_59(x),
        l314_60(x),
        l314_61(x),
        l314_62(x),
        l314_63(x),
        l314_64(x),
        l314_65(x),
        l314_66(x),
        l314_67(x),
        l314_68(x),
        l314_69(x),
        l314_70(x),
        l314_71(x),
        l314_72(x),
        l314_73(x),
        l314_74(x),
        l314_75(x),
        l314_76(x),
        l314_77(x),
        l314_78(x),
        l314_79(x),
        l314_80(x),
        l314_81(x),
        l314_82(x),
        l314_83(x),
        l314_84(x),
        l314_85(x),
        l314_86(x),
        l314_87(x),
        l314_88(x),
        l314_89(x),
        l314_90(x),
        l314_91(x),
        l314_92(x),
        l314_93(x),
        l314_94(x),
        l314_95(x),
        l314_96(x),
        l314_97(x),
        l314_98(x),
        l314_99(x),
        l314_100(x),
        l314_101(x),
        l314_102(x),
        l314_103(x),
        l314_104(x),
        l314_105(x),
        l314_106(x),
        l314_107(x),
        l314_108(x),
        l314_109(x),
        l314_110(x),
        l314_111(x),
        l314_112(x),
        l314_113(x),
        l314_114(x),
        l314_115(x),
        l314_116(x),
        l314_117(x),
        l314_118(x),
        l314_119(x),
        l314_120(x),
        l314_121(x),
        l314_122(x),
        l314_123(x),
        l314_124(x),
        l314_125(x),
        l314_126(x),
        l314_127(x),
        l314_128(x),
        l314_129(x),
        l314_130(x),
        l314_131(x),
        l314_132(x),
        l314_133(x),
        l314_134(x),
        l314_135(x),
        l314_136(x),
        l314_137(x),
        l314_138(x),
        l314_139(x),
        l314_140(x),
        l314_141(x),
        l314_142(x),
        l314_143(x),
        l314_144(x),
        l314_145(x),
        l314_146(x),
        l314_147(x),
        l314_148(x),
        l314_149(x),
        l314_150(x),
        l314_151(x),
        l314_152(x),
        l314_153(x),
        l314_154(x),
        l314_155(x),
        l314_156(x),
        l314_157(x),
        l314_158(x),
        l314_159(x),
        l314_160(x),
        l314_161(x),
        l314_162(x),
        l314_163(x),
        l314_164(x),
        l314_165(x),
        l314_166(x),
        l314_167(x),
        l314_168(x),
        l314_169(x),
        l314_170(x),
        l314_171(x),
        l314_172(x),
        l314_173(x),
        l314_174(x),
        l314_175(x),
        l314_176(x),
        l314_177(x),
        l314_178(x),
        l314_179(x),
        l314_180(x),
        l314_181(x),
        l314_182(x),
        l314_183(x),
        l314_184(x),
        l314_185(x),
        l314_186(x),
        l314_187(x),
        l314_188(x),
        l314_189(x),
        l314_190(x),
        l314_191(x),
        l314_192(x),
        l314_193(x),
        l314_194(x),
        l314_195(x),
        l314_196(x),
        l314_197(x),
        l314_198(x),
        l314_199(x),
        l314_200(x),
        l314_201(x),
        l314_202(x),
        l314_203(x),
        l314_204(x),
        l314_205(x),
        l314_206(x),
        l314_207(x),
        l314_208(x),
        l314_209(x),
        l314_210(x),
        l314_211(x),
        l314_212(x),
        l314_213(x),
        l314_214(x),
        l314_215(x),
        l314_216(x),
        l314_217(x),
        l314_218(x),
        l314_219(x),
        l314_220(x),
        l314_221(x),
        l314_222(x),
        l314_223(x),
        l314_224(x),
        l314_225(x),
        l314_226(x),
        l314_227(x),
        l314_228(x),
        l314_229(x),
        l314_230(x),
        l314_231(x),
        l314_232(x),
        l314_233(x),
        l314_234(x),
        l314_235(x),
        l314_236(x),
        l314_237(x),
        l314_238(x),
        l314_239(x),
        l314_240(x),
        l314_241(x),
        l314_242(x),
        l314_243(x),
        l314_244(x),
        l314_245(x),
        l314_246(x),
        l314_247(x),
        l314_248(x),
        l314_249(x),
        l314_250(x),
        l314_251(x),
        l314_252(x),
        l314_253(x),
        l314_254(x),
        l314_255(x),
        l314_256(x),
        l314_257(x),
        l314_258(x),
        l314_259(x),
        l314_260(x),
        l314_261(x),
        l314_262(x),
        l314_263(x),
        l314_264(x),
        l314_265(x),
        l314_266(x),
        l314_267(x),
        l314_268(x),
        l314_269(x),
        l314_270(x),
        l314_271(x),
        l314_272(x),
        l314_273(x),
        l314_274(x),
        l314_275(x),
        l314_276(x),
        l314_277(x),
        l314_278(x),
        l314_279(x),
        l314_280(x),
        l314_281(x),
        l314_282(x),
        l314_283(x),
        l314_284(x),
        l314_285(x),
        l314_286(x),
        l314_287(x),
        l314_288(x),
        l314_289(x),
        l314_290(x),
        l314_291(x),
        l314_292(x),
        l314_293(x),
        l314_294(x),
        l314_295(x),
        l314_296(x),
        l314_297(x),
        l314_298(x),
        l314_299(x),
        l314_300(x),
        l314_301(x),
        l314_302(x),
        l314_303(x),
        l314_304(x),
        l314_305(x),
        l314_306(x),
        l314_307(x),
        l314_308(x),
        l314_309(x),
        l314_310(x),
        l314_311(x),
        l314_312(x),
        l314_313(x),
        l314_314(x),
        l314_315(x),
        l314_316(x),
        l314_317(x),
        l314_318(x),
        l314_319(x),
        l314_320(x),
        l314_321(x),
        l314_322(x),
        l314_323(x),
        l314_324(x),
        l314_325(x),
        l314_326(x),
        l314_327(x),
        l314_328(x),
        l314_329(x),
        l314_330(x),
        l314_331(x),
        l314_332(x),
        l314_333(x),
        l314_334(x),
        l314_335(x),
        l314_336(x),
        l314_337(x),
        l314_338(x),
        l314_339(x),
        l314_340(x),
        l314_341(x),
        l314_342(x),
        l314_343(x),
        l314_344(x),
        l314_345(x),
        l314_346(x),
        l314_347(x),
        l314_348(x),
        l314_349(x),
        l314_350(x),
        l314_351(x),
    ]