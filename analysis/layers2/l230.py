import numpy as np




# Generated from reverse engineering
def l230_g(x: np.ndarray) -> np.ndarray:
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




def l230_0(x):
    # x is a list (or vector) of length 400
    return max(0, x[0])
def l230_1(x):
    # x is a list (or vector) of length 400
    return max(0, x[1])
def l230_2(x):
    # x is a list (or vector) of length 400
    return max(0, x[2])
def l230_3(x):
    # x is a list (or vector) of length 400
    return max(0, x[3])
def l230_4(x):
    # x is a list (or vector) of length 400
    return max(0, x[4])
def l230_5(x):
    # x is a list (or vector) of length 400
    return max(0, x[5])
def l230_6(x):
    # x is a list (or vector) of length 400
    return max(0, x[6])
def l230_7(x):
    # x is a list (or vector) of length 400
    return max(0, x[7])
def l230_8(x):
    # x is a list (or vector) of length 400
    return max(0, x[8])
def l230_9(x):
    # x is a list (or vector) of length 400
    return max(0, x[9])
def l230_10(x):
    # x is a list (or vector) of length 400
    return max(0, x[10])
def l230_11(x):
    # x is a list (or vector) of length 400
    return max(0, x[11])
def l230_12(x):
    # x is a list (or vector) of length 400
    return max(0, x[12])
def l230_13(x):
    # x is a list (or vector) of length 400
    return max(0, x[13])
def l230_14(x):
    # x is a list (or vector) of length 400
    return max(0, x[14])
def l230_15(x):
    # x is a list (or vector) of length 400
    return max(0, x[15])
def l230_16(x):
    # x is a list (or vector) of length 400
    return max(0, x[16])
def l230_17(x):
    # x is a list (or vector) of length 400
    return max(0, x[17])
def l230_18(x):
    # x is a list (or vector) of length 400
    return max(0, x[18])
def l230_19(x):
    # x is a list (or vector) of length 400
    return max(0, x[19])
def l230_20(x):
    # x is a list (or vector) of length 400
    return max(0, x[20])
def l230_21(x):
    # x is a list (or vector) of length 400
    return max(0, x[21])
def l230_22(x):
    # x is a list (or vector) of length 400
    return max(0, x[22])
def l230_23(x):
    # x is a list (or vector) of length 400
    return max(0, x[23])
def l230_24(x):
    # x is a list (or vector) of length 400
    return max(0, x[24])
def l230_25(x):
    # x is a list (or vector) of length 400
    return max(0, x[25])
def l230_26(x):
    # x is a list (or vector) of length 400
    return max(0, x[26])
def l230_27(x):
    # x is a list (or vector) of length 400
    return max(0, x[27])
def l230_28(x):
    # x is a list (or vector) of length 400
    return max(0, x[28])
def l230_29(x):
    # x is a list (or vector) of length 400
    return max(0, x[29])
def l230_30(x):
    # x is a list (or vector) of length 400
    return max(0, x[30])
def l230_31(x):
    # x is a list (or vector) of length 400
    return max(0, x[31])
def l230_32(x):
    # x is a list (or vector) of length 400
    return max(0, x[32])
def l230_33(x):
    # x is a list (or vector) of length 400
    return max(0, x[33])
def l230_34(x):
    # x is a list (or vector) of length 400
    return max(0, x[34])
def l230_35(x):
    # x is a list (or vector) of length 400
    return max(0, x[35])
def l230_36(x):
    # x is a list (or vector) of length 400
    return max(0, x[36])
def l230_37(x):
    # x is a list (or vector) of length 400
    return max(0, x[37])
def l230_38(x):
    # x is a list (or vector) of length 400
    return max(0, x[38])
def l230_39(x):
    # x is a list (or vector) of length 400
    return max(0, x[39])
def l230_40(x):
    # x is a list (or vector) of length 400
    return max(0, x[40])
def l230_41(x):
    # x is a list (or vector) of length 400
    return max(0, x[41])
def l230_42(x):
    # x is a list (or vector) of length 400
    return max(0, x[42])
def l230_43(x):
    # x is a list (or vector) of length 400
    return max(0, x[43])
def l230_44(x):
    # x is a list (or vector) of length 400
    return max(0, x[44])
def l230_45(x):
    # x is a list (or vector) of length 400
    return max(0, x[45])
def l230_46(x):
    # x is a list (or vector) of length 400
    return max(0, x[46])
def l230_47(x):
    # x is a list (or vector) of length 400
    return max(0, x[47])
def l230_48(x):
    # x is a list (or vector) of length 400
    return max(0, x[48])
def l230_49(x):
    # x is a list (or vector) of length 400
    return max(0, x[49])
def l230_50(x):
    # x is a list (or vector) of length 400
    return max(0, x[50])
def l230_51(x):
    # x is a list (or vector) of length 400
    return max(0, x[51])
def l230_52(x):
    # x is a list (or vector) of length 400
    return max(0, x[52])
def l230_53(x):
    # x is a list (or vector) of length 400
    return max(0, x[53])
def l230_54(x):
    # x is a list (or vector) of length 400
    return max(0, x[54])
def l230_55(x):
    # x is a list (or vector) of length 400
    return max(0, x[55])
def l230_56(x):
    # x is a list (or vector) of length 400
    return max(0, x[56])
def l230_57(x):
    # x is a list (or vector) of length 400
    return max(0, x[57])
def l230_58(x):
    # x is a list (or vector) of length 400
    return max(0, x[58])
def l230_59(x):
    # x is a list (or vector) of length 400
    return max(0, x[59])
def l230_60(x):
    # x is a list (or vector) of length 400
    return max(0, x[60])
def l230_61(x):
    # x is a list (or vector) of length 400
    return max(0, x[61])
def l230_62(x):
    # x is a list (or vector) of length 400
    return max(0, x[62])
def l230_63(x):
    # x is a list (or vector) of length 400
    return max(0, x[63])
def l230_64(x):
    # x is a list (or vector) of length 400
    return max(0, x[64])
def l230_65(x):
    # x is a list (or vector) of length 400
    return max(0, x[65])
def l230_66(x):
    # x is a list (or vector) of length 400
    return max(0, x[66])
def l230_67(x):
    # x is a list (or vector) of length 400
    return max(0, x[67])
def l230_68(x):
    # x is a list (or vector) of length 400
    return max(0, x[68])
def l230_69(x):
    # x is a list (or vector) of length 400
    return max(0, x[69])
def l230_70(x):
    # x is a list (or vector) of length 400
    return max(0, x[70])
def l230_71(x):
    # x is a list (or vector) of length 400
    return max(0, x[71])
def l230_72(x):
    # x is a list (or vector) of length 400
    return max(0, x[72])
def l230_73(x):
    # x is a list (or vector) of length 400
    return max(0, x[73])
def l230_74(x):
    # x is a list (or vector) of length 400
    return max(0, x[74])
def l230_75(x):
    # x is a list (or vector) of length 400
    return max(0, x[75])
def l230_76(x):
    # x is a list (or vector) of length 400
    return max(0, x[76])
def l230_77(x):
    # x is a list (or vector) of length 400
    return max(0, x[77])
def l230_78(x):
    # x is a list (or vector) of length 400
    return max(0, x[78])
def l230_79(x):
    # x is a list (or vector) of length 400
    return max(0, x[79])
def l230_80(x):
    # x is a list (or vector) of length 400
    return max(0, x[80])
def l230_81(x):
    # x is a list (or vector) of length 400
    return max(0, x[81])
def l230_82(x):
    # x is a list (or vector) of length 400
    return max(0, x[82])
def l230_83(x):
    # x is a list (or vector) of length 400
    return max(0, x[83])
def l230_84(x):
    # x is a list (or vector) of length 400
    return max(0, x[84])
def l230_85(x):
    # x is a list (or vector) of length 400
    return max(0, x[85])
def l230_86(x):
    # x is a list (or vector) of length 400
    return max(0, x[86])
def l230_87(x):
    # x is a list (or vector) of length 400
    return max(0, x[87])
def l230_88(x):
    # x is a list (or vector) of length 400
    return max(0, x[88])
def l230_89(x):
    # x is a list (or vector) of length 400
    return max(0, x[89])
def l230_90(x):
    # x is a list (or vector) of length 400
    return max(0, x[90])
def l230_91(x):
    # x is a list (or vector) of length 400
    return max(0, x[91])
def l230_92(x):
    # x is a list (or vector) of length 400
    return max(0, x[92])
def l230_93(x):
    # x is a list (or vector) of length 400
    return max(0, x[93])
def l230_94(x):
    # x is a list (or vector) of length 400
    return max(0, x[94])
def l230_95(x):
    # x is a list (or vector) of length 400
    return max(0, x[95])
def l230_96(x):
    # x is a list (or vector) of length 400
    return max(0, x[96])
def l230_97(x):
    # x is a list (or vector) of length 400
    return max(0, x[97])
def l230_98(x):
    # x is a list (or vector) of length 400
    return max(0, x[98])
def l230_99(x):
    # x is a list (or vector) of length 400
    return max(0, x[99])
def l230_100(x):
    # x is a list (or vector) of length 400
    return max(0, x[100])
def l230_101(x):
    # x is a list (or vector) of length 400
    return max(0, x[101])
def l230_102(x):
    # x is a list (or vector) of length 400
    return max(0, x[102])
def l230_103(x):
    # x is a list (or vector) of length 400
    return max(0, x[103])
def l230_104(x):
    # x is a list (or vector) of length 400
    return max(0, x[104])
def l230_105(x):
    # x is a list (or vector) of length 400
    return max(0, x[105])
def l230_106(x):
    # x is a list (or vector) of length 400
    return max(0, x[106])
def l230_107(x):
    # x is a list (or vector) of length 400
    return max(0, x[107])
def l230_108(x):
    # x is a list (or vector) of length 400
    return max(0, x[108])
def l230_109(x):
    # x is a list (or vector) of length 400
    return max(0, x[109])
def l230_110(x):
    # x is a list (or vector) of length 400
    return max(0, x[110])
def l230_111(x):
    # x is a list (or vector) of length 400
    return max(0, x[111])
def l230_112(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[112] + -1.0*x[128] + 1.0)
def l230_113(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[113] + -1.0*x[129] + 1.0)
def l230_114(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[114] + -1.0*x[130] + 1.0)
def l230_115(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[115] + -1.0*x[131] + 1.0)
def l230_116(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[116] + -1.0*x[132] + 1.0)
def l230_117(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[117] + -1.0*x[133] + 1.0)
def l230_118(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[118] + -1.0*x[134] + 1.0)
def l230_119(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[119] + -1.0*x[135] + 1.0)
def l230_120(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[120] + -1.0*x[136] + 1.0)
def l230_121(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[121] + -1.0*x[137] + 1.0)
def l230_122(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[122] + -1.0*x[138] + 1.0)
def l230_123(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[123] + -1.0*x[139] + 1.0)
def l230_124(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[124] + -1.0*x[140] + 1.0)
def l230_125(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[125] + -1.0*x[141] + 1.0)
def l230_126(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[126] + -1.0*x[142] + 1.0)
def l230_127(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[127] + -1.0*x[143] + 1.0)
def l230_128(x):
    # x is a list (or vector) of length 400
    return max(0, x[160])
def l230_129(x):
    # x is a list (or vector) of length 400
    return max(0, x[161])
def l230_130(x):
    # x is a list (or vector) of length 400
    return max(0, x[162])
def l230_131(x):
    # x is a list (or vector) of length 400
    return max(0, x[163])
def l230_132(x):
    # x is a list (or vector) of length 400
    return max(0, x[164])
def l230_133(x):
    # x is a list (or vector) of length 400
    return max(0, x[165])
def l230_134(x):
    # x is a list (or vector) of length 400
    return max(0, x[166])
def l230_135(x):
    # x is a list (or vector) of length 400
    return max(0, x[167])
def l230_136(x):
    # x is a list (or vector) of length 400
    return max(0, x[168])
def l230_137(x):
    # x is a list (or vector) of length 400
    return max(0, x[169])
def l230_138(x):
    # x is a list (or vector) of length 400
    return max(0, x[170])
def l230_139(x):
    # x is a list (or vector) of length 400
    return max(0, x[171])
def l230_140(x):
    # x is a list (or vector) of length 400
    return max(0, x[172])
def l230_141(x):
    # x is a list (or vector) of length 400
    return max(0, x[173])
def l230_142(x):
    # x is a list (or vector) of length 400
    return max(0, x[174])
def l230_143(x):
    # x is a list (or vector) of length 400
    return max(0, x[175])
def l230_144(x):
    # x is a list (or vector) of length 400
    return max(0, x[144])
def l230_145(x):
    # x is a list (or vector) of length 400
    return max(0, x[145])
def l230_146(x):
    # x is a list (or vector) of length 400
    return max(0, x[146])
def l230_147(x):
    # x is a list (or vector) of length 400
    return max(0, x[147])
def l230_148(x):
    # x is a list (or vector) of length 400
    return max(0, x[148])
def l230_149(x):
    # x is a list (or vector) of length 400
    return max(0, x[149])
def l230_150(x):
    # x is a list (or vector) of length 400
    return max(0, x[150])
def l230_151(x):
    # x is a list (or vector) of length 400
    return max(0, x[151])
def l230_152(x):
    # x is a list (or vector) of length 400
    return max(0, x[152])
def l230_153(x):
    # x is a list (or vector) of length 400
    return max(0, x[153])
def l230_154(x):
    # x is a list (or vector) of length 400
    return max(0, x[154])
def l230_155(x):
    # x is a list (or vector) of length 400
    return max(0, x[155])
def l230_156(x):
    # x is a list (or vector) of length 400
    return max(0, x[156])
def l230_157(x):
    # x is a list (or vector) of length 400
    return max(0, x[157])
def l230_158(x):
    # x is a list (or vector) of length 400
    return max(0, x[158])
def l230_159(x):
    # x is a list (or vector) of length 400
    return max(0, x[159])
def l230_160(x):
    # x is a list (or vector) of length 400
    return max(0, x[176])
def l230_161(x):
    # x is a list (or vector) of length 400
    return max(0, x[177])
def l230_162(x):
    # x is a list (or vector) of length 400
    return max(0, x[178])
def l230_163(x):
    # x is a list (or vector) of length 400
    return max(0, x[179])
def l230_164(x):
    # x is a list (or vector) of length 400
    return max(0, x[180])
def l230_165(x):
    # x is a list (or vector) of length 400
    return max(0, x[181])
def l230_166(x):
    # x is a list (or vector) of length 400
    return max(0, x[182])
def l230_167(x):
    # x is a list (or vector) of length 400
    return max(0, x[183])
def l230_168(x):
    # x is a list (or vector) of length 400
    return max(0, x[184])
def l230_169(x):
    # x is a list (or vector) of length 400
    return max(0, x[185])
def l230_170(x):
    # x is a list (or vector) of length 400
    return max(0, x[186])
def l230_171(x):
    # x is a list (or vector) of length 400
    return max(0, x[187])
def l230_172(x):
    # x is a list (or vector) of length 400
    return max(0, x[188])
def l230_173(x):
    # x is a list (or vector) of length 400
    return max(0, x[189])
def l230_174(x):
    # x is a list (or vector) of length 400
    return max(0, x[190])
def l230_175(x):
    # x is a list (or vector) of length 400
    return max(0, x[191])
def l230_176(x):
    # x is a list (or vector) of length 400
    return max(0, x[192])
def l230_177(x):
    # x is a list (or vector) of length 400
    return max(0, x[193])
def l230_178(x):
    # x is a list (or vector) of length 400
    return max(0, x[194])
def l230_179(x):
    # x is a list (or vector) of length 400
    return max(0, x[195])
def l230_180(x):
    # x is a list (or vector) of length 400
    return max(0, x[196])
def l230_181(x):
    # x is a list (or vector) of length 400
    return max(0, x[197])
def l230_182(x):
    # x is a list (or vector) of length 400
    return max(0, x[198])
def l230_183(x):
    # x is a list (or vector) of length 400
    return max(0, x[199])
def l230_184(x):
    # x is a list (or vector) of length 400
    return max(0, x[200])
def l230_185(x):
    # x is a list (or vector) of length 400
    return max(0, x[201])
def l230_186(x):
    # x is a list (or vector) of length 400
    return max(0, x[202])
def l230_187(x):
    # x is a list (or vector) of length 400
    return max(0, x[203])
def l230_188(x):
    # x is a list (or vector) of length 400
    return max(0, x[204])
def l230_189(x):
    # x is a list (or vector) of length 400
    return max(0, x[205])
def l230_190(x):
    # x is a list (or vector) of length 400
    return max(0, x[206])
def l230_191(x):
    # x is a list (or vector) of length 400
    return max(0, x[207])
def l230_192(x):
    # x is a list (or vector) of length 400
    return max(0, x[272])
def l230_193(x):
    # x is a list (or vector) of length 400
    return max(0, x[208] + x[273])
def l230_194(x):
    # x is a list (or vector) of length 400
    return max(0, x[209] + x[274])
def l230_195(x):
    # x is a list (or vector) of length 400
    return max(0, x[210] + x[275])
def l230_196(x):
    # x is a list (or vector) of length 400
    return max(0, x[211] + x[276])
def l230_197(x):
    # x is a list (or vector) of length 400
    return max(0, x[212] + x[277])
def l230_198(x):
    # x is a list (or vector) of length 400
    return max(0, x[213] + x[278])
def l230_199(x):
    # x is a list (or vector) of length 400
    return max(0, x[214] + x[279])
def l230_200(x):
    # x is a list (or vector) of length 400
    return max(0, x[215] + x[280])
def l230_201(x):
    # x is a list (or vector) of length 400
    return max(0, x[216] + x[281])
def l230_202(x):
    # x is a list (or vector) of length 400
    return max(0, x[217] + x[282])
def l230_203(x):
    # x is a list (or vector) of length 400
    return max(0, x[218] + x[283])
def l230_204(x):
    # x is a list (or vector) of length 400
    return max(0, x[219] + x[284])
def l230_205(x):
    # x is a list (or vector) of length 400
    return max(0, x[220] + x[285])
def l230_206(x):
    # x is a list (or vector) of length 400
    return max(0, x[221] + x[286])
def l230_207(x):
    # x is a list (or vector) of length 400
    return max(0, x[222] + x[287])
def l230_208(x):
    # x is a list (or vector) of length 400
    return max(0, x[223] + x[288])
def l230_209(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[224] + x[289] + 1.0)
def l230_210(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[225] + x[290] + 1.0)
def l230_211(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[226] + x[291] + 1.0)
def l230_212(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[227] + x[292] + 1.0)
def l230_213(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[228] + x[293] + 1.0)
def l230_214(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[229] + x[294] + 1.0)
def l230_215(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[230] + x[295] + 1.0)
def l230_216(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[231] + x[296] + 1.0)
def l230_217(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[232] + x[297] + 1.0)
def l230_218(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[233] + x[298] + 1.0)
def l230_219(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[234] + x[299] + 1.0)
def l230_220(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[235] + x[300] + 1.0)
def l230_221(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[236] + x[301] + 1.0)
def l230_222(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[237] + x[302] + 1.0)
def l230_223(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[238] + x[303] + 1.0)
def l230_224(x):
    # x is a list (or vector) of length 400
    return max(0, x[272] + -1.0)
def l230_225(x):
    # x is a list (or vector) of length 400
    return max(0, x[208] + x[273] + -1.0)
def l230_226(x):
    # x is a list (or vector) of length 400
    return max(0, x[209] + x[274] + -1.0)
def l230_227(x):
    # x is a list (or vector) of length 400
    return max(0, x[210] + x[275] + -1.0)
def l230_228(x):
    # x is a list (or vector) of length 400
    return max(0, x[211] + x[276] + -1.0)
def l230_229(x):
    # x is a list (or vector) of length 400
    return max(0, x[212] + x[277] + -1.0)
def l230_230(x):
    # x is a list (or vector) of length 400
    return max(0, x[213] + x[278] + -1.0)
def l230_231(x):
    # x is a list (or vector) of length 400
    return max(0, x[214] + x[279] + -1.0)
def l230_232(x):
    # x is a list (or vector) of length 400
    return max(0, x[215] + x[280] + -1.0)
def l230_233(x):
    # x is a list (or vector) of length 400
    return max(0, x[216] + x[281] + -1.0)
def l230_234(x):
    # x is a list (or vector) of length 400
    return max(0, x[217] + x[282] + -1.0)
def l230_235(x):
    # x is a list (or vector) of length 400
    return max(0, x[218] + x[283] + -1.0)
def l230_236(x):
    # x is a list (or vector) of length 400
    return max(0, x[219] + x[284] + -1.0)
def l230_237(x):
    # x is a list (or vector) of length 400
    return max(0, x[220] + x[285] + -1.0)
def l230_238(x):
    # x is a list (or vector) of length 400
    return max(0, x[221] + x[286] + -1.0)
def l230_239(x):
    # x is a list (or vector) of length 400
    return max(0, x[222] + x[287] + -1.0)
def l230_240(x):
    # x is a list (or vector) of length 400
    return max(0, x[223] + x[288] + -1.0)
def l230_241(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[224] + x[289])
def l230_242(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[225] + x[290])
def l230_243(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[226] + x[291])
def l230_244(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[227] + x[292])
def l230_245(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[228] + x[293])
def l230_246(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[229] + x[294])
def l230_247(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[230] + x[295])
def l230_248(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[231] + x[296])
def l230_249(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[232] + x[297])
def l230_250(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[233] + x[298])
def l230_251(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[234] + x[299])
def l230_252(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[235] + x[300])
def l230_253(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[236] + x[301])
def l230_254(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[237] + x[302])
def l230_255(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[238] + x[303])
def l230_256(x):
    # x is a list (or vector) of length 400
    return max(0, x[332])
def l230_257(x):
    # x is a list (or vector) of length 400
    return max(0, x[328])
def l230_258(x):
    # x is a list (or vector) of length 400
    return max(0, x[324])
def l230_259(x):
    # x is a list (or vector) of length 400
    return max(0, x[320])
def l230_260(x):
    # x is a list (or vector) of length 400
    return max(0, x[316])
def l230_261(x):
    # x is a list (or vector) of length 400
    return max(0, x[312])
def l230_262(x):
    # x is a list (or vector) of length 400
    return max(0, x[308])
def l230_263(x):
    # x is a list (or vector) of length 400
    return max(0, x[304])
def l230_264(x):
    # x is a list (or vector) of length 400
    return max(0, x[333])
def l230_265(x):
    # x is a list (or vector) of length 400
    return max(0, x[329])
def l230_266(x):
    # x is a list (or vector) of length 400
    return max(0, x[325])
def l230_267(x):
    # x is a list (or vector) of length 400
    return max(0, x[321])
def l230_268(x):
    # x is a list (or vector) of length 400
    return max(0, x[317])
def l230_269(x):
    # x is a list (or vector) of length 400
    return max(0, x[313])
def l230_270(x):
    # x is a list (or vector) of length 400
    return max(0, x[309])
def l230_271(x):
    # x is a list (or vector) of length 400
    return max(0, x[305])
def l230_272(x):
    # x is a list (or vector) of length 400
    return max(0, x[334])
def l230_273(x):
    # x is a list (or vector) of length 400
    return max(0, x[330])
def l230_274(x):
    # x is a list (or vector) of length 400
    return max(0, x[326])
def l230_275(x):
    # x is a list (or vector) of length 400
    return max(0, x[322])
def l230_276(x):
    # x is a list (or vector) of length 400
    return max(0, x[318])
def l230_277(x):
    # x is a list (or vector) of length 400
    return max(0, x[314])
def l230_278(x):
    # x is a list (or vector) of length 400
    return max(0, x[310])
def l230_279(x):
    # x is a list (or vector) of length 400
    return max(0, x[306])
def l230_280(x):
    # x is a list (or vector) of length 400
    return max(0, x[335])
def l230_281(x):
    # x is a list (or vector) of length 400
    return max(0, x[331])
def l230_282(x):
    # x is a list (or vector) of length 400
    return max(0, x[327])
def l230_283(x):
    # x is a list (or vector) of length 400
    return max(0, x[323])
def l230_284(x):
    # x is a list (or vector) of length 400
    return max(0, x[319])
def l230_285(x):
    # x is a list (or vector) of length 400
    return max(0, x[315])
def l230_286(x):
    # x is a list (or vector) of length 400
    return max(0, x[311])
def l230_287(x):
    # x is a list (or vector) of length 400
    return max(0, x[307])
def l230_288(x):
    # x is a list (or vector) of length 400
    return max(0, x[336])
def l230_289(x):
    # x is a list (or vector) of length 400
    return max(0, x[337])
def l230_290(x):
    # x is a list (or vector) of length 400
    return max(0, x[338])
def l230_291(x):
    # x is a list (or vector) of length 400
    return max(0, x[339])
def l230_292(x):
    # x is a list (or vector) of length 400
    return max(0, x[340])
def l230_293(x):
    # x is a list (or vector) of length 400
    return max(0, x[341])
def l230_294(x):
    # x is a list (or vector) of length 400
    return max(0, x[342])
def l230_295(x):
    # x is a list (or vector) of length 400
    return max(0, x[343])
def l230_296(x):
    # x is a list (or vector) of length 400
    return max(0, x[344])
def l230_297(x):
    # x is a list (or vector) of length 400
    return max(0, x[345])
def l230_298(x):
    # x is a list (or vector) of length 400
    return max(0, x[346])
def l230_299(x):
    # x is a list (or vector) of length 400
    return max(0, x[347])
def l230_300(x):
    # x is a list (or vector) of length 400
    return max(0, x[348])
def l230_301(x):
    # x is a list (or vector) of length 400
    return max(0, x[349])
def l230_302(x):
    # x is a list (or vector) of length 400
    return max(0, x[350])
def l230_303(x):
    # x is a list (or vector) of length 400
    return max(0, x[351])
def l230_304(x):
    # x is a list (or vector) of length 400
    return max(0, x[352])
def l230_305(x):
    # x is a list (or vector) of length 400
    return max(0, x[353])
def l230_306(x):
    # x is a list (or vector) of length 400
    return max(0, x[354])
def l230_307(x):
    # x is a list (or vector) of length 400
    return max(0, x[355])
def l230_308(x):
    # x is a list (or vector) of length 400
    return max(0, x[356])
def l230_309(x):
    # x is a list (or vector) of length 400
    return max(0, x[357])
def l230_310(x):
    # x is a list (or vector) of length 400
    return max(0, x[358])
def l230_311(x):
    # x is a list (or vector) of length 400
    return max(0, x[359])
def l230_312(x):
    # x is a list (or vector) of length 400
    return max(0, x[360])
def l230_313(x):
    # x is a list (or vector) of length 400
    return max(0, x[361])
def l230_314(x):
    # x is a list (or vector) of length 400
    return max(0, x[362])
def l230_315(x):
    # x is a list (or vector) of length 400
    return max(0, x[363])
def l230_316(x):
    # x is a list (or vector) of length 400
    return max(0, x[364])
def l230_317(x):
    # x is a list (or vector) of length 400
    return max(0, x[365])
def l230_318(x):
    # x is a list (or vector) of length 400
    return max(0, x[366])
def l230_319(x):
    # x is a list (or vector) of length 400
    return max(0, x[367])
def l230_320(x):
    # x is a list (or vector) of length 400
    return max(0, x[368])
def l230_321(x):
    # x is a list (or vector) of length 400
    return max(0, x[369])
def l230_322(x):
    # x is a list (or vector) of length 400
    return max(0, x[370])
def l230_323(x):
    # x is a list (or vector) of length 400
    return max(0, x[371])
def l230_324(x):
    # x is a list (or vector) of length 400
    return max(0, x[372])
def l230_325(x):
    # x is a list (or vector) of length 400
    return max(0, x[373])
def l230_326(x):
    # x is a list (or vector) of length 400
    return max(0, x[374])
def l230_327(x):
    # x is a list (or vector) of length 400
    return max(0, x[375])
def l230_328(x):
    # x is a list (or vector) of length 400
    return max(0, x[376])
def l230_329(x):
    # x is a list (or vector) of length 400
    return max(0, x[377])
def l230_330(x):
    # x is a list (or vector) of length 400
    return max(0, x[378])
def l230_331(x):
    # x is a list (or vector) of length 400
    return max(0, x[379])
def l230_332(x):
    # x is a list (or vector) of length 400
    return max(0, x[380])
def l230_333(x):
    # x is a list (or vector) of length 400
    return max(0, x[381])
def l230_334(x):
    # x is a list (or vector) of length 400
    return max(0, x[382])
def l230_335(x):
    # x is a list (or vector) of length 400
    return max(0, x[383])
def l230_336(x):
    # x is a list (or vector) of length 400
    return max(0, x[384])
def l230_337(x):
    # x is a list (or vector) of length 400
    return max(0, x[385])
def l230_338(x):
    # x is a list (or vector) of length 400
    return max(0, x[386])
def l230_339(x):
    # x is a list (or vector) of length 400
    return max(0, x[387])
def l230_340(x):
    # x is a list (or vector) of length 400
    return max(0, x[388])
def l230_341(x):
    # x is a list (or vector) of length 400
    return max(0, x[389])
def l230_342(x):
    # x is a list (or vector) of length 400
    return max(0, x[390])
def l230_343(x):
    # x is a list (or vector) of length 400
    return max(0, x[391])
def l230_344(x):
    # x is a list (or vector) of length 400
    return max(0, x[392])
def l230_345(x):
    # x is a list (or vector) of length 400
    return max(0, x[393])
def l230_346(x):
    # x is a list (or vector) of length 400
    return max(0, x[394])
def l230_347(x):
    # x is a list (or vector) of length 400
    return max(0, x[395])
def l230_348(x):
    # x is a list (or vector) of length 400
    return max(0, x[396])
def l230_349(x):
    # x is a list (or vector) of length 400
    return max(0, x[397])
def l230_350(x):
    # x is a list (or vector) of length 400
    return max(0, x[398])
def l230_351(x):
    # x is a list (or vector) of length 400
    return max(0, x[399])
def l230_(x):
    # x is a list (or vector) of length 400
    return [
        l230_0(x),
        l230_1(x),
        l230_2(x),
        l230_3(x),
        l230_4(x),
        l230_5(x),
        l230_6(x),
        l230_7(x),
        l230_8(x),
        l230_9(x),
        l230_10(x),
        l230_11(x),
        l230_12(x),
        l230_13(x),
        l230_14(x),
        l230_15(x),
        l230_16(x),
        l230_17(x),
        l230_18(x),
        l230_19(x),
        l230_20(x),
        l230_21(x),
        l230_22(x),
        l230_23(x),
        l230_24(x),
        l230_25(x),
        l230_26(x),
        l230_27(x),
        l230_28(x),
        l230_29(x),
        l230_30(x),
        l230_31(x),
        l230_32(x),
        l230_33(x),
        l230_34(x),
        l230_35(x),
        l230_36(x),
        l230_37(x),
        l230_38(x),
        l230_39(x),
        l230_40(x),
        l230_41(x),
        l230_42(x),
        l230_43(x),
        l230_44(x),
        l230_45(x),
        l230_46(x),
        l230_47(x),
        l230_48(x),
        l230_49(x),
        l230_50(x),
        l230_51(x),
        l230_52(x),
        l230_53(x),
        l230_54(x),
        l230_55(x),
        l230_56(x),
        l230_57(x),
        l230_58(x),
        l230_59(x),
        l230_60(x),
        l230_61(x),
        l230_62(x),
        l230_63(x),
        l230_64(x),
        l230_65(x),
        l230_66(x),
        l230_67(x),
        l230_68(x),
        l230_69(x),
        l230_70(x),
        l230_71(x),
        l230_72(x),
        l230_73(x),
        l230_74(x),
        l230_75(x),
        l230_76(x),
        l230_77(x),
        l230_78(x),
        l230_79(x),
        l230_80(x),
        l230_81(x),
        l230_82(x),
        l230_83(x),
        l230_84(x),
        l230_85(x),
        l230_86(x),
        l230_87(x),
        l230_88(x),
        l230_89(x),
        l230_90(x),
        l230_91(x),
        l230_92(x),
        l230_93(x),
        l230_94(x),
        l230_95(x),
        l230_96(x),
        l230_97(x),
        l230_98(x),
        l230_99(x),
        l230_100(x),
        l230_101(x),
        l230_102(x),
        l230_103(x),
        l230_104(x),
        l230_105(x),
        l230_106(x),
        l230_107(x),
        l230_108(x),
        l230_109(x),
        l230_110(x),
        l230_111(x),
        l230_112(x),
        l230_113(x),
        l230_114(x),
        l230_115(x),
        l230_116(x),
        l230_117(x),
        l230_118(x),
        l230_119(x),
        l230_120(x),
        l230_121(x),
        l230_122(x),
        l230_123(x),
        l230_124(x),
        l230_125(x),
        l230_126(x),
        l230_127(x),
        l230_128(x),
        l230_129(x),
        l230_130(x),
        l230_131(x),
        l230_132(x),
        l230_133(x),
        l230_134(x),
        l230_135(x),
        l230_136(x),
        l230_137(x),
        l230_138(x),
        l230_139(x),
        l230_140(x),
        l230_141(x),
        l230_142(x),
        l230_143(x),
        l230_144(x),
        l230_145(x),
        l230_146(x),
        l230_147(x),
        l230_148(x),
        l230_149(x),
        l230_150(x),
        l230_151(x),
        l230_152(x),
        l230_153(x),
        l230_154(x),
        l230_155(x),
        l230_156(x),
        l230_157(x),
        l230_158(x),
        l230_159(x),
        l230_160(x),
        l230_161(x),
        l230_162(x),
        l230_163(x),
        l230_164(x),
        l230_165(x),
        l230_166(x),
        l230_167(x),
        l230_168(x),
        l230_169(x),
        l230_170(x),
        l230_171(x),
        l230_172(x),
        l230_173(x),
        l230_174(x),
        l230_175(x),
        l230_176(x),
        l230_177(x),
        l230_178(x),
        l230_179(x),
        l230_180(x),
        l230_181(x),
        l230_182(x),
        l230_183(x),
        l230_184(x),
        l230_185(x),
        l230_186(x),
        l230_187(x),
        l230_188(x),
        l230_189(x),
        l230_190(x),
        l230_191(x),
        l230_192(x),
        l230_193(x),
        l230_194(x),
        l230_195(x),
        l230_196(x),
        l230_197(x),
        l230_198(x),
        l230_199(x),
        l230_200(x),
        l230_201(x),
        l230_202(x),
        l230_203(x),
        l230_204(x),
        l230_205(x),
        l230_206(x),
        l230_207(x),
        l230_208(x),
        l230_209(x),
        l230_210(x),
        l230_211(x),
        l230_212(x),
        l230_213(x),
        l230_214(x),
        l230_215(x),
        l230_216(x),
        l230_217(x),
        l230_218(x),
        l230_219(x),
        l230_220(x),
        l230_221(x),
        l230_222(x),
        l230_223(x),
        l230_224(x),
        l230_225(x),
        l230_226(x),
        l230_227(x),
        l230_228(x),
        l230_229(x),
        l230_230(x),
        l230_231(x),
        l230_232(x),
        l230_233(x),
        l230_234(x),
        l230_235(x),
        l230_236(x),
        l230_237(x),
        l230_238(x),
        l230_239(x),
        l230_240(x),
        l230_241(x),
        l230_242(x),
        l230_243(x),
        l230_244(x),
        l230_245(x),
        l230_246(x),
        l230_247(x),
        l230_248(x),
        l230_249(x),
        l230_250(x),
        l230_251(x),
        l230_252(x),
        l230_253(x),
        l230_254(x),
        l230_255(x),
        l230_256(x),
        l230_257(x),
        l230_258(x),
        l230_259(x),
        l230_260(x),
        l230_261(x),
        l230_262(x),
        l230_263(x),
        l230_264(x),
        l230_265(x),
        l230_266(x),
        l230_267(x),
        l230_268(x),
        l230_269(x),
        l230_270(x),
        l230_271(x),
        l230_272(x),
        l230_273(x),
        l230_274(x),
        l230_275(x),
        l230_276(x),
        l230_277(x),
        l230_278(x),
        l230_279(x),
        l230_280(x),
        l230_281(x),
        l230_282(x),
        l230_283(x),
        l230_284(x),
        l230_285(x),
        l230_286(x),
        l230_287(x),
        l230_288(x),
        l230_289(x),
        l230_290(x),
        l230_291(x),
        l230_292(x),
        l230_293(x),
        l230_294(x),
        l230_295(x),
        l230_296(x),
        l230_297(x),
        l230_298(x),
        l230_299(x),
        l230_300(x),
        l230_301(x),
        l230_302(x),
        l230_303(x),
        l230_304(x),
        l230_305(x),
        l230_306(x),
        l230_307(x),
        l230_308(x),
        l230_309(x),
        l230_310(x),
        l230_311(x),
        l230_312(x),
        l230_313(x),
        l230_314(x),
        l230_315(x),
        l230_316(x),
        l230_317(x),
        l230_318(x),
        l230_319(x),
        l230_320(x),
        l230_321(x),
        l230_322(x),
        l230_323(x),
        l230_324(x),
        l230_325(x),
        l230_326(x),
        l230_327(x),
        l230_328(x),
        l230_329(x),
        l230_330(x),
        l230_331(x),
        l230_332(x),
        l230_333(x),
        l230_334(x),
        l230_335(x),
        l230_336(x),
        l230_337(x),
        l230_338(x),
        l230_339(x),
        l230_340(x),
        l230_341(x),
        l230_342(x),
        l230_343(x),
        l230_344(x),
        l230_345(x),
        l230_346(x),
        l230_347(x),
        l230_348(x),
        l230_349(x),
        l230_350(x),
        l230_351(x),
    ]