import numpy as np




# Generated from reverse engineering
def l146_g(x: np.ndarray) -> np.ndarray:
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




def l146_0(x):
    # x is a list (or vector) of length 400
    return max(0, x[0])
def l146_1(x):
    # x is a list (or vector) of length 400
    return max(0, x[1])
def l146_2(x):
    # x is a list (or vector) of length 400
    return max(0, x[2])
def l146_3(x):
    # x is a list (or vector) of length 400
    return max(0, x[3])
def l146_4(x):
    # x is a list (or vector) of length 400
    return max(0, x[4])
def l146_5(x):
    # x is a list (or vector) of length 400
    return max(0, x[5])
def l146_6(x):
    # x is a list (or vector) of length 400
    return max(0, x[6])
def l146_7(x):
    # x is a list (or vector) of length 400
    return max(0, x[7])
def l146_8(x):
    # x is a list (or vector) of length 400
    return max(0, x[8])
def l146_9(x):
    # x is a list (or vector) of length 400
    return max(0, x[9])
def l146_10(x):
    # x is a list (or vector) of length 400
    return max(0, x[10])
def l146_11(x):
    # x is a list (or vector) of length 400
    return max(0, x[11])
def l146_12(x):
    # x is a list (or vector) of length 400
    return max(0, x[12])
def l146_13(x):
    # x is a list (or vector) of length 400
    return max(0, x[13])
def l146_14(x):
    # x is a list (or vector) of length 400
    return max(0, x[14])
def l146_15(x):
    # x is a list (or vector) of length 400
    return max(0, x[15])
def l146_16(x):
    # x is a list (or vector) of length 400
    return max(0, x[16])
def l146_17(x):
    # x is a list (or vector) of length 400
    return max(0, x[17])
def l146_18(x):
    # x is a list (or vector) of length 400
    return max(0, x[18])
def l146_19(x):
    # x is a list (or vector) of length 400
    return max(0, x[19])
def l146_20(x):
    # x is a list (or vector) of length 400
    return max(0, x[20])
def l146_21(x):
    # x is a list (or vector) of length 400
    return max(0, x[21])
def l146_22(x):
    # x is a list (or vector) of length 400
    return max(0, x[22])
def l146_23(x):
    # x is a list (or vector) of length 400
    return max(0, x[23])
def l146_24(x):
    # x is a list (or vector) of length 400
    return max(0, x[24])
def l146_25(x):
    # x is a list (or vector) of length 400
    return max(0, x[25])
def l146_26(x):
    # x is a list (or vector) of length 400
    return max(0, x[26])
def l146_27(x):
    # x is a list (or vector) of length 400
    return max(0, x[27])
def l146_28(x):
    # x is a list (or vector) of length 400
    return max(0, x[28])
def l146_29(x):
    # x is a list (or vector) of length 400
    return max(0, x[29])
def l146_30(x):
    # x is a list (or vector) of length 400
    return max(0, x[30])
def l146_31(x):
    # x is a list (or vector) of length 400
    return max(0, x[31])
def l146_32(x):
    # x is a list (or vector) of length 400
    return max(0, x[32])
def l146_33(x):
    # x is a list (or vector) of length 400
    return max(0, x[33])
def l146_34(x):
    # x is a list (or vector) of length 400
    return max(0, x[34])
def l146_35(x):
    # x is a list (or vector) of length 400
    return max(0, x[35])
def l146_36(x):
    # x is a list (or vector) of length 400
    return max(0, x[36])
def l146_37(x):
    # x is a list (or vector) of length 400
    return max(0, x[37])
def l146_38(x):
    # x is a list (or vector) of length 400
    return max(0, x[38])
def l146_39(x):
    # x is a list (or vector) of length 400
    return max(0, x[39])
def l146_40(x):
    # x is a list (or vector) of length 400
    return max(0, x[40])
def l146_41(x):
    # x is a list (or vector) of length 400
    return max(0, x[41])
def l146_42(x):
    # x is a list (or vector) of length 400
    return max(0, x[42])
def l146_43(x):
    # x is a list (or vector) of length 400
    return max(0, x[43])
def l146_44(x):
    # x is a list (or vector) of length 400
    return max(0, x[44])
def l146_45(x):
    # x is a list (or vector) of length 400
    return max(0, x[45])
def l146_46(x):
    # x is a list (or vector) of length 400
    return max(0, x[46])
def l146_47(x):
    # x is a list (or vector) of length 400
    return max(0, x[47])
def l146_48(x):
    # x is a list (or vector) of length 400
    return max(0, x[48])
def l146_49(x):
    # x is a list (or vector) of length 400
    return max(0, x[49])
def l146_50(x):
    # x is a list (or vector) of length 400
    return max(0, x[50])
def l146_51(x):
    # x is a list (or vector) of length 400
    return max(0, x[51])
def l146_52(x):
    # x is a list (or vector) of length 400
    return max(0, x[52])
def l146_53(x):
    # x is a list (or vector) of length 400
    return max(0, x[53])
def l146_54(x):
    # x is a list (or vector) of length 400
    return max(0, x[54])
def l146_55(x):
    # x is a list (or vector) of length 400
    return max(0, x[55])
def l146_56(x):
    # x is a list (or vector) of length 400
    return max(0, x[56])
def l146_57(x):
    # x is a list (or vector) of length 400
    return max(0, x[57])
def l146_58(x):
    # x is a list (or vector) of length 400
    return max(0, x[58])
def l146_59(x):
    # x is a list (or vector) of length 400
    return max(0, x[59])
def l146_60(x):
    # x is a list (or vector) of length 400
    return max(0, x[60])
def l146_61(x):
    # x is a list (or vector) of length 400
    return max(0, x[61])
def l146_62(x):
    # x is a list (or vector) of length 400
    return max(0, x[62])
def l146_63(x):
    # x is a list (or vector) of length 400
    return max(0, x[63])
def l146_64(x):
    # x is a list (or vector) of length 400
    return max(0, x[64])
def l146_65(x):
    # x is a list (or vector) of length 400
    return max(0, x[65])
def l146_66(x):
    # x is a list (or vector) of length 400
    return max(0, x[66])
def l146_67(x):
    # x is a list (or vector) of length 400
    return max(0, x[67])
def l146_68(x):
    # x is a list (or vector) of length 400
    return max(0, x[68])
def l146_69(x):
    # x is a list (or vector) of length 400
    return max(0, x[69])
def l146_70(x):
    # x is a list (or vector) of length 400
    return max(0, x[70])
def l146_71(x):
    # x is a list (or vector) of length 400
    return max(0, x[71])
def l146_72(x):
    # x is a list (or vector) of length 400
    return max(0, x[72])
def l146_73(x):
    # x is a list (or vector) of length 400
    return max(0, x[73])
def l146_74(x):
    # x is a list (or vector) of length 400
    return max(0, x[74])
def l146_75(x):
    # x is a list (or vector) of length 400
    return max(0, x[75])
def l146_76(x):
    # x is a list (or vector) of length 400
    return max(0, x[76])
def l146_77(x):
    # x is a list (or vector) of length 400
    return max(0, x[77])
def l146_78(x):
    # x is a list (or vector) of length 400
    return max(0, x[78])
def l146_79(x):
    # x is a list (or vector) of length 400
    return max(0, x[79])
def l146_80(x):
    # x is a list (or vector) of length 400
    return max(0, x[80])
def l146_81(x):
    # x is a list (or vector) of length 400
    return max(0, x[81])
def l146_82(x):
    # x is a list (or vector) of length 400
    return max(0, x[82])
def l146_83(x):
    # x is a list (or vector) of length 400
    return max(0, x[83])
def l146_84(x):
    # x is a list (or vector) of length 400
    return max(0, x[84])
def l146_85(x):
    # x is a list (or vector) of length 400
    return max(0, x[85])
def l146_86(x):
    # x is a list (or vector) of length 400
    return max(0, x[86])
def l146_87(x):
    # x is a list (or vector) of length 400
    return max(0, x[87])
def l146_88(x):
    # x is a list (or vector) of length 400
    return max(0, x[88])
def l146_89(x):
    # x is a list (or vector) of length 400
    return max(0, x[89])
def l146_90(x):
    # x is a list (or vector) of length 400
    return max(0, x[90])
def l146_91(x):
    # x is a list (or vector) of length 400
    return max(0, x[91])
def l146_92(x):
    # x is a list (or vector) of length 400
    return max(0, x[92])
def l146_93(x):
    # x is a list (or vector) of length 400
    return max(0, x[93])
def l146_94(x):
    # x is a list (or vector) of length 400
    return max(0, x[94])
def l146_95(x):
    # x is a list (or vector) of length 400
    return max(0, x[95])
def l146_96(x):
    # x is a list (or vector) of length 400
    return max(0, x[96])
def l146_97(x):
    # x is a list (or vector) of length 400
    return max(0, x[97])
def l146_98(x):
    # x is a list (or vector) of length 400
    return max(0, x[98])
def l146_99(x):
    # x is a list (or vector) of length 400
    return max(0, x[99])
def l146_100(x):
    # x is a list (or vector) of length 400
    return max(0, x[100])
def l146_101(x):
    # x is a list (or vector) of length 400
    return max(0, x[101])
def l146_102(x):
    # x is a list (or vector) of length 400
    return max(0, x[102])
def l146_103(x):
    # x is a list (or vector) of length 400
    return max(0, x[103])
def l146_104(x):
    # x is a list (or vector) of length 400
    return max(0, x[104])
def l146_105(x):
    # x is a list (or vector) of length 400
    return max(0, x[105])
def l146_106(x):
    # x is a list (or vector) of length 400
    return max(0, x[106])
def l146_107(x):
    # x is a list (or vector) of length 400
    return max(0, x[107])
def l146_108(x):
    # x is a list (or vector) of length 400
    return max(0, x[108])
def l146_109(x):
    # x is a list (or vector) of length 400
    return max(0, x[109])
def l146_110(x):
    # x is a list (or vector) of length 400
    return max(0, x[110])
def l146_111(x):
    # x is a list (or vector) of length 400
    return max(0, x[111])
def l146_112(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[112] + -1.0*x[128] + 1.0)
def l146_113(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[113] + -1.0*x[129] + 1.0)
def l146_114(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[114] + -1.0*x[130] + 1.0)
def l146_115(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[115] + -1.0*x[131] + 1.0)
def l146_116(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[116] + -1.0*x[132] + 1.0)
def l146_117(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[117] + -1.0*x[133] + 1.0)
def l146_118(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[118] + -1.0*x[134] + 1.0)
def l146_119(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[119] + -1.0*x[135] + 1.0)
def l146_120(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[120] + -1.0*x[136] + 1.0)
def l146_121(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[121] + -1.0*x[137] + 1.0)
def l146_122(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[122] + -1.0*x[138] + 1.0)
def l146_123(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[123] + -1.0*x[139] + 1.0)
def l146_124(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[124] + -1.0*x[140] + 1.0)
def l146_125(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[125] + -1.0*x[141] + 1.0)
def l146_126(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[126] + -1.0*x[142] + 1.0)
def l146_127(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[127] + -1.0*x[143] + 1.0)
def l146_128(x):
    # x is a list (or vector) of length 400
    return max(0, x[160])
def l146_129(x):
    # x is a list (or vector) of length 400
    return max(0, x[161])
def l146_130(x):
    # x is a list (or vector) of length 400
    return max(0, x[162])
def l146_131(x):
    # x is a list (or vector) of length 400
    return max(0, x[163])
def l146_132(x):
    # x is a list (or vector) of length 400
    return max(0, x[164])
def l146_133(x):
    # x is a list (or vector) of length 400
    return max(0, x[165])
def l146_134(x):
    # x is a list (or vector) of length 400
    return max(0, x[166])
def l146_135(x):
    # x is a list (or vector) of length 400
    return max(0, x[167])
def l146_136(x):
    # x is a list (or vector) of length 400
    return max(0, x[168])
def l146_137(x):
    # x is a list (or vector) of length 400
    return max(0, x[169])
def l146_138(x):
    # x is a list (or vector) of length 400
    return max(0, x[170])
def l146_139(x):
    # x is a list (or vector) of length 400
    return max(0, x[171])
def l146_140(x):
    # x is a list (or vector) of length 400
    return max(0, x[172])
def l146_141(x):
    # x is a list (or vector) of length 400
    return max(0, x[173])
def l146_142(x):
    # x is a list (or vector) of length 400
    return max(0, x[174])
def l146_143(x):
    # x is a list (or vector) of length 400
    return max(0, x[175])
def l146_144(x):
    # x is a list (or vector) of length 400
    return max(0, x[144])
def l146_145(x):
    # x is a list (or vector) of length 400
    return max(0, x[145])
def l146_146(x):
    # x is a list (or vector) of length 400
    return max(0, x[146])
def l146_147(x):
    # x is a list (or vector) of length 400
    return max(0, x[147])
def l146_148(x):
    # x is a list (or vector) of length 400
    return max(0, x[148])
def l146_149(x):
    # x is a list (or vector) of length 400
    return max(0, x[149])
def l146_150(x):
    # x is a list (or vector) of length 400
    return max(0, x[150])
def l146_151(x):
    # x is a list (or vector) of length 400
    return max(0, x[151])
def l146_152(x):
    # x is a list (or vector) of length 400
    return max(0, x[152])
def l146_153(x):
    # x is a list (or vector) of length 400
    return max(0, x[153])
def l146_154(x):
    # x is a list (or vector) of length 400
    return max(0, x[154])
def l146_155(x):
    # x is a list (or vector) of length 400
    return max(0, x[155])
def l146_156(x):
    # x is a list (or vector) of length 400
    return max(0, x[156])
def l146_157(x):
    # x is a list (or vector) of length 400
    return max(0, x[157])
def l146_158(x):
    # x is a list (or vector) of length 400
    return max(0, x[158])
def l146_159(x):
    # x is a list (or vector) of length 400
    return max(0, x[159])
def l146_160(x):
    # x is a list (or vector) of length 400
    return max(0, x[176])
def l146_161(x):
    # x is a list (or vector) of length 400
    return max(0, x[177])
def l146_162(x):
    # x is a list (or vector) of length 400
    return max(0, x[178])
def l146_163(x):
    # x is a list (or vector) of length 400
    return max(0, x[179])
def l146_164(x):
    # x is a list (or vector) of length 400
    return max(0, x[180])
def l146_165(x):
    # x is a list (or vector) of length 400
    return max(0, x[181])
def l146_166(x):
    # x is a list (or vector) of length 400
    return max(0, x[182])
def l146_167(x):
    # x is a list (or vector) of length 400
    return max(0, x[183])
def l146_168(x):
    # x is a list (or vector) of length 400
    return max(0, x[184])
def l146_169(x):
    # x is a list (or vector) of length 400
    return max(0, x[185])
def l146_170(x):
    # x is a list (or vector) of length 400
    return max(0, x[186])
def l146_171(x):
    # x is a list (or vector) of length 400
    return max(0, x[187])
def l146_172(x):
    # x is a list (or vector) of length 400
    return max(0, x[188])
def l146_173(x):
    # x is a list (or vector) of length 400
    return max(0, x[189])
def l146_174(x):
    # x is a list (or vector) of length 400
    return max(0, x[190])
def l146_175(x):
    # x is a list (or vector) of length 400
    return max(0, x[191])
def l146_176(x):
    # x is a list (or vector) of length 400
    return max(0, x[192])
def l146_177(x):
    # x is a list (or vector) of length 400
    return max(0, x[193])
def l146_178(x):
    # x is a list (or vector) of length 400
    return max(0, x[194])
def l146_179(x):
    # x is a list (or vector) of length 400
    return max(0, x[195])
def l146_180(x):
    # x is a list (or vector) of length 400
    return max(0, x[196])
def l146_181(x):
    # x is a list (or vector) of length 400
    return max(0, x[197])
def l146_182(x):
    # x is a list (or vector) of length 400
    return max(0, x[198])
def l146_183(x):
    # x is a list (or vector) of length 400
    return max(0, x[199])
def l146_184(x):
    # x is a list (or vector) of length 400
    return max(0, x[200])
def l146_185(x):
    # x is a list (or vector) of length 400
    return max(0, x[201])
def l146_186(x):
    # x is a list (or vector) of length 400
    return max(0, x[202])
def l146_187(x):
    # x is a list (or vector) of length 400
    return max(0, x[203])
def l146_188(x):
    # x is a list (or vector) of length 400
    return max(0, x[204])
def l146_189(x):
    # x is a list (or vector) of length 400
    return max(0, x[205])
def l146_190(x):
    # x is a list (or vector) of length 400
    return max(0, x[206])
def l146_191(x):
    # x is a list (or vector) of length 400
    return max(0, x[207])
def l146_192(x):
    # x is a list (or vector) of length 400
    return max(0, x[272])
def l146_193(x):
    # x is a list (or vector) of length 400
    return max(0, x[208] + x[273])
def l146_194(x):
    # x is a list (or vector) of length 400
    return max(0, x[209] + x[274])
def l146_195(x):
    # x is a list (or vector) of length 400
    return max(0, x[210] + x[275])
def l146_196(x):
    # x is a list (or vector) of length 400
    return max(0, x[211] + x[276])
def l146_197(x):
    # x is a list (or vector) of length 400
    return max(0, x[212] + x[277])
def l146_198(x):
    # x is a list (or vector) of length 400
    return max(0, x[213] + x[278])
def l146_199(x):
    # x is a list (or vector) of length 400
    return max(0, x[214] + x[279])
def l146_200(x):
    # x is a list (or vector) of length 400
    return max(0, x[215] + x[280])
def l146_201(x):
    # x is a list (or vector) of length 400
    return max(0, x[216] + x[281])
def l146_202(x):
    # x is a list (or vector) of length 400
    return max(0, x[217] + x[282])
def l146_203(x):
    # x is a list (or vector) of length 400
    return max(0, x[218] + x[283])
def l146_204(x):
    # x is a list (or vector) of length 400
    return max(0, x[219] + x[284])
def l146_205(x):
    # x is a list (or vector) of length 400
    return max(0, x[220] + x[285])
def l146_206(x):
    # x is a list (or vector) of length 400
    return max(0, x[221] + x[286])
def l146_207(x):
    # x is a list (or vector) of length 400
    return max(0, x[222] + x[287])
def l146_208(x):
    # x is a list (or vector) of length 400
    return max(0, x[223] + x[288])
def l146_209(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[224] + x[289] + 1.0)
def l146_210(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[225] + x[290] + 1.0)
def l146_211(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[226] + x[291] + 1.0)
def l146_212(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[227] + x[292] + 1.0)
def l146_213(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[228] + x[293] + 1.0)
def l146_214(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[229] + x[294] + 1.0)
def l146_215(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[230] + x[295] + 1.0)
def l146_216(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[231] + x[296] + 1.0)
def l146_217(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[232] + x[297] + 1.0)
def l146_218(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[233] + x[298] + 1.0)
def l146_219(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[234] + x[299] + 1.0)
def l146_220(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[235] + x[300] + 1.0)
def l146_221(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[236] + x[301] + 1.0)
def l146_222(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[237] + x[302] + 1.0)
def l146_223(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[238] + x[303] + 1.0)
def l146_224(x):
    # x is a list (or vector) of length 400
    return max(0, x[272] + -1.0)
def l146_225(x):
    # x is a list (or vector) of length 400
    return max(0, x[208] + x[273] + -1.0)
def l146_226(x):
    # x is a list (or vector) of length 400
    return max(0, x[209] + x[274] + -1.0)
def l146_227(x):
    # x is a list (or vector) of length 400
    return max(0, x[210] + x[275] + -1.0)
def l146_228(x):
    # x is a list (or vector) of length 400
    return max(0, x[211] + x[276] + -1.0)
def l146_229(x):
    # x is a list (or vector) of length 400
    return max(0, x[212] + x[277] + -1.0)
def l146_230(x):
    # x is a list (or vector) of length 400
    return max(0, x[213] + x[278] + -1.0)
def l146_231(x):
    # x is a list (or vector) of length 400
    return max(0, x[214] + x[279] + -1.0)
def l146_232(x):
    # x is a list (or vector) of length 400
    return max(0, x[215] + x[280] + -1.0)
def l146_233(x):
    # x is a list (or vector) of length 400
    return max(0, x[216] + x[281] + -1.0)
def l146_234(x):
    # x is a list (or vector) of length 400
    return max(0, x[217] + x[282] + -1.0)
def l146_235(x):
    # x is a list (or vector) of length 400
    return max(0, x[218] + x[283] + -1.0)
def l146_236(x):
    # x is a list (or vector) of length 400
    return max(0, x[219] + x[284] + -1.0)
def l146_237(x):
    # x is a list (or vector) of length 400
    return max(0, x[220] + x[285] + -1.0)
def l146_238(x):
    # x is a list (or vector) of length 400
    return max(0, x[221] + x[286] + -1.0)
def l146_239(x):
    # x is a list (or vector) of length 400
    return max(0, x[222] + x[287] + -1.0)
def l146_240(x):
    # x is a list (or vector) of length 400
    return max(0, x[223] + x[288] + -1.0)
def l146_241(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[224] + x[289])
def l146_242(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[225] + x[290])
def l146_243(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[226] + x[291])
def l146_244(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[227] + x[292])
def l146_245(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[228] + x[293])
def l146_246(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[229] + x[294])
def l146_247(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[230] + x[295])
def l146_248(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[231] + x[296])
def l146_249(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[232] + x[297])
def l146_250(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[233] + x[298])
def l146_251(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[234] + x[299])
def l146_252(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[235] + x[300])
def l146_253(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[236] + x[301])
def l146_254(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[237] + x[302])
def l146_255(x):
    # x is a list (or vector) of length 400
    return max(0, -1.0*x[238] + x[303])
def l146_256(x):
    # x is a list (or vector) of length 400
    return max(0, x[332])
def l146_257(x):
    # x is a list (or vector) of length 400
    return max(0, x[328])
def l146_258(x):
    # x is a list (or vector) of length 400
    return max(0, x[324])
def l146_259(x):
    # x is a list (or vector) of length 400
    return max(0, x[320])
def l146_260(x):
    # x is a list (or vector) of length 400
    return max(0, x[316])
def l146_261(x):
    # x is a list (or vector) of length 400
    return max(0, x[312])
def l146_262(x):
    # x is a list (or vector) of length 400
    return max(0, x[308])
def l146_263(x):
    # x is a list (or vector) of length 400
    return max(0, x[304])
def l146_264(x):
    # x is a list (or vector) of length 400
    return max(0, x[333])
def l146_265(x):
    # x is a list (or vector) of length 400
    return max(0, x[329])
def l146_266(x):
    # x is a list (or vector) of length 400
    return max(0, x[325])
def l146_267(x):
    # x is a list (or vector) of length 400
    return max(0, x[321])
def l146_268(x):
    # x is a list (or vector) of length 400
    return max(0, x[317])
def l146_269(x):
    # x is a list (or vector) of length 400
    return max(0, x[313])
def l146_270(x):
    # x is a list (or vector) of length 400
    return max(0, x[309])
def l146_271(x):
    # x is a list (or vector) of length 400
    return max(0, x[305])
def l146_272(x):
    # x is a list (or vector) of length 400
    return max(0, x[334])
def l146_273(x):
    # x is a list (or vector) of length 400
    return max(0, x[330])
def l146_274(x):
    # x is a list (or vector) of length 400
    return max(0, x[326])
def l146_275(x):
    # x is a list (or vector) of length 400
    return max(0, x[322])
def l146_276(x):
    # x is a list (or vector) of length 400
    return max(0, x[318])
def l146_277(x):
    # x is a list (or vector) of length 400
    return max(0, x[314])
def l146_278(x):
    # x is a list (or vector) of length 400
    return max(0, x[310])
def l146_279(x):
    # x is a list (or vector) of length 400
    return max(0, x[306])
def l146_280(x):
    # x is a list (or vector) of length 400
    return max(0, x[335])
def l146_281(x):
    # x is a list (or vector) of length 400
    return max(0, x[331])
def l146_282(x):
    # x is a list (or vector) of length 400
    return max(0, x[327])
def l146_283(x):
    # x is a list (or vector) of length 400
    return max(0, x[323])
def l146_284(x):
    # x is a list (or vector) of length 400
    return max(0, x[319])
def l146_285(x):
    # x is a list (or vector) of length 400
    return max(0, x[315])
def l146_286(x):
    # x is a list (or vector) of length 400
    return max(0, x[311])
def l146_287(x):
    # x is a list (or vector) of length 400
    return max(0, x[307])
def l146_288(x):
    # x is a list (or vector) of length 400
    return max(0, x[336])
def l146_289(x):
    # x is a list (or vector) of length 400
    return max(0, x[337])
def l146_290(x):
    # x is a list (or vector) of length 400
    return max(0, x[338])
def l146_291(x):
    # x is a list (or vector) of length 400
    return max(0, x[339])
def l146_292(x):
    # x is a list (or vector) of length 400
    return max(0, x[340])
def l146_293(x):
    # x is a list (or vector) of length 400
    return max(0, x[341])
def l146_294(x):
    # x is a list (or vector) of length 400
    return max(0, x[342])
def l146_295(x):
    # x is a list (or vector) of length 400
    return max(0, x[343])
def l146_296(x):
    # x is a list (or vector) of length 400
    return max(0, x[344])
def l146_297(x):
    # x is a list (or vector) of length 400
    return max(0, x[345])
def l146_298(x):
    # x is a list (or vector) of length 400
    return max(0, x[346])
def l146_299(x):
    # x is a list (or vector) of length 400
    return max(0, x[347])
def l146_300(x):
    # x is a list (or vector) of length 400
    return max(0, x[348])
def l146_301(x):
    # x is a list (or vector) of length 400
    return max(0, x[349])
def l146_302(x):
    # x is a list (or vector) of length 400
    return max(0, x[350])
def l146_303(x):
    # x is a list (or vector) of length 400
    return max(0, x[351])
def l146_304(x):
    # x is a list (or vector) of length 400
    return max(0, x[352])
def l146_305(x):
    # x is a list (or vector) of length 400
    return max(0, x[353])
def l146_306(x):
    # x is a list (or vector) of length 400
    return max(0, x[354])
def l146_307(x):
    # x is a list (or vector) of length 400
    return max(0, x[355])
def l146_308(x):
    # x is a list (or vector) of length 400
    return max(0, x[356])
def l146_309(x):
    # x is a list (or vector) of length 400
    return max(0, x[357])
def l146_310(x):
    # x is a list (or vector) of length 400
    return max(0, x[358])
def l146_311(x):
    # x is a list (or vector) of length 400
    return max(0, x[359])
def l146_312(x):
    # x is a list (or vector) of length 400
    return max(0, x[360])
def l146_313(x):
    # x is a list (or vector) of length 400
    return max(0, x[361])
def l146_314(x):
    # x is a list (or vector) of length 400
    return max(0, x[362])
def l146_315(x):
    # x is a list (or vector) of length 400
    return max(0, x[363])
def l146_316(x):
    # x is a list (or vector) of length 400
    return max(0, x[364])
def l146_317(x):
    # x is a list (or vector) of length 400
    return max(0, x[365])
def l146_318(x):
    # x is a list (or vector) of length 400
    return max(0, x[366])
def l146_319(x):
    # x is a list (or vector) of length 400
    return max(0, x[367])
def l146_320(x):
    # x is a list (or vector) of length 400
    return max(0, x[368])
def l146_321(x):
    # x is a list (or vector) of length 400
    return max(0, x[369])
def l146_322(x):
    # x is a list (or vector) of length 400
    return max(0, x[370])
def l146_323(x):
    # x is a list (or vector) of length 400
    return max(0, x[371])
def l146_324(x):
    # x is a list (or vector) of length 400
    return max(0, x[372])
def l146_325(x):
    # x is a list (or vector) of length 400
    return max(0, x[373])
def l146_326(x):
    # x is a list (or vector) of length 400
    return max(0, x[374])
def l146_327(x):
    # x is a list (or vector) of length 400
    return max(0, x[375])
def l146_328(x):
    # x is a list (or vector) of length 400
    return max(0, x[376])
def l146_329(x):
    # x is a list (or vector) of length 400
    return max(0, x[377])
def l146_330(x):
    # x is a list (or vector) of length 400
    return max(0, x[378])
def l146_331(x):
    # x is a list (or vector) of length 400
    return max(0, x[379])
def l146_332(x):
    # x is a list (or vector) of length 400
    return max(0, x[380])
def l146_333(x):
    # x is a list (or vector) of length 400
    return max(0, x[381])
def l146_334(x):
    # x is a list (or vector) of length 400
    return max(0, x[382])
def l146_335(x):
    # x is a list (or vector) of length 400
    return max(0, x[383])
def l146_336(x):
    # x is a list (or vector) of length 400
    return max(0, x[384])
def l146_337(x):
    # x is a list (or vector) of length 400
    return max(0, x[385])
def l146_338(x):
    # x is a list (or vector) of length 400
    return max(0, x[386])
def l146_339(x):
    # x is a list (or vector) of length 400
    return max(0, x[387])
def l146_340(x):
    # x is a list (or vector) of length 400
    return max(0, x[388])
def l146_341(x):
    # x is a list (or vector) of length 400
    return max(0, x[389])
def l146_342(x):
    # x is a list (or vector) of length 400
    return max(0, x[390])
def l146_343(x):
    # x is a list (or vector) of length 400
    return max(0, x[391])
def l146_344(x):
    # x is a list (or vector) of length 400
    return max(0, x[392])
def l146_345(x):
    # x is a list (or vector) of length 400
    return max(0, x[393])
def l146_346(x):
    # x is a list (or vector) of length 400
    return max(0, x[394])
def l146_347(x):
    # x is a list (or vector) of length 400
    return max(0, x[395])
def l146_348(x):
    # x is a list (or vector) of length 400
    return max(0, x[396])
def l146_349(x):
    # x is a list (or vector) of length 400
    return max(0, x[397])
def l146_350(x):
    # x is a list (or vector) of length 400
    return max(0, x[398])
def l146_351(x):
    # x is a list (or vector) of length 400
    return max(0, x[399])
def l146_(x):
    # x is a list (or vector) of length 400
    return [
        l146_0(x),
        l146_1(x),
        l146_2(x),
        l146_3(x),
        l146_4(x),
        l146_5(x),
        l146_6(x),
        l146_7(x),
        l146_8(x),
        l146_9(x),
        l146_10(x),
        l146_11(x),
        l146_12(x),
        l146_13(x),
        l146_14(x),
        l146_15(x),
        l146_16(x),
        l146_17(x),
        l146_18(x),
        l146_19(x),
        l146_20(x),
        l146_21(x),
        l146_22(x),
        l146_23(x),
        l146_24(x),
        l146_25(x),
        l146_26(x),
        l146_27(x),
        l146_28(x),
        l146_29(x),
        l146_30(x),
        l146_31(x),
        l146_32(x),
        l146_33(x),
        l146_34(x),
        l146_35(x),
        l146_36(x),
        l146_37(x),
        l146_38(x),
        l146_39(x),
        l146_40(x),
        l146_41(x),
        l146_42(x),
        l146_43(x),
        l146_44(x),
        l146_45(x),
        l146_46(x),
        l146_47(x),
        l146_48(x),
        l146_49(x),
        l146_50(x),
        l146_51(x),
        l146_52(x),
        l146_53(x),
        l146_54(x),
        l146_55(x),
        l146_56(x),
        l146_57(x),
        l146_58(x),
        l146_59(x),
        l146_60(x),
        l146_61(x),
        l146_62(x),
        l146_63(x),
        l146_64(x),
        l146_65(x),
        l146_66(x),
        l146_67(x),
        l146_68(x),
        l146_69(x),
        l146_70(x),
        l146_71(x),
        l146_72(x),
        l146_73(x),
        l146_74(x),
        l146_75(x),
        l146_76(x),
        l146_77(x),
        l146_78(x),
        l146_79(x),
        l146_80(x),
        l146_81(x),
        l146_82(x),
        l146_83(x),
        l146_84(x),
        l146_85(x),
        l146_86(x),
        l146_87(x),
        l146_88(x),
        l146_89(x),
        l146_90(x),
        l146_91(x),
        l146_92(x),
        l146_93(x),
        l146_94(x),
        l146_95(x),
        l146_96(x),
        l146_97(x),
        l146_98(x),
        l146_99(x),
        l146_100(x),
        l146_101(x),
        l146_102(x),
        l146_103(x),
        l146_104(x),
        l146_105(x),
        l146_106(x),
        l146_107(x),
        l146_108(x),
        l146_109(x),
        l146_110(x),
        l146_111(x),
        l146_112(x),
        l146_113(x),
        l146_114(x),
        l146_115(x),
        l146_116(x),
        l146_117(x),
        l146_118(x),
        l146_119(x),
        l146_120(x),
        l146_121(x),
        l146_122(x),
        l146_123(x),
        l146_124(x),
        l146_125(x),
        l146_126(x),
        l146_127(x),
        l146_128(x),
        l146_129(x),
        l146_130(x),
        l146_131(x),
        l146_132(x),
        l146_133(x),
        l146_134(x),
        l146_135(x),
        l146_136(x),
        l146_137(x),
        l146_138(x),
        l146_139(x),
        l146_140(x),
        l146_141(x),
        l146_142(x),
        l146_143(x),
        l146_144(x),
        l146_145(x),
        l146_146(x),
        l146_147(x),
        l146_148(x),
        l146_149(x),
        l146_150(x),
        l146_151(x),
        l146_152(x),
        l146_153(x),
        l146_154(x),
        l146_155(x),
        l146_156(x),
        l146_157(x),
        l146_158(x),
        l146_159(x),
        l146_160(x),
        l146_161(x),
        l146_162(x),
        l146_163(x),
        l146_164(x),
        l146_165(x),
        l146_166(x),
        l146_167(x),
        l146_168(x),
        l146_169(x),
        l146_170(x),
        l146_171(x),
        l146_172(x),
        l146_173(x),
        l146_174(x),
        l146_175(x),
        l146_176(x),
        l146_177(x),
        l146_178(x),
        l146_179(x),
        l146_180(x),
        l146_181(x),
        l146_182(x),
        l146_183(x),
        l146_184(x),
        l146_185(x),
        l146_186(x),
        l146_187(x),
        l146_188(x),
        l146_189(x),
        l146_190(x),
        l146_191(x),
        l146_192(x),
        l146_193(x),
        l146_194(x),
        l146_195(x),
        l146_196(x),
        l146_197(x),
        l146_198(x),
        l146_199(x),
        l146_200(x),
        l146_201(x),
        l146_202(x),
        l146_203(x),
        l146_204(x),
        l146_205(x),
        l146_206(x),
        l146_207(x),
        l146_208(x),
        l146_209(x),
        l146_210(x),
        l146_211(x),
        l146_212(x),
        l146_213(x),
        l146_214(x),
        l146_215(x),
        l146_216(x),
        l146_217(x),
        l146_218(x),
        l146_219(x),
        l146_220(x),
        l146_221(x),
        l146_222(x),
        l146_223(x),
        l146_224(x),
        l146_225(x),
        l146_226(x),
        l146_227(x),
        l146_228(x),
        l146_229(x),
        l146_230(x),
        l146_231(x),
        l146_232(x),
        l146_233(x),
        l146_234(x),
        l146_235(x),
        l146_236(x),
        l146_237(x),
        l146_238(x),
        l146_239(x),
        l146_240(x),
        l146_241(x),
        l146_242(x),
        l146_243(x),
        l146_244(x),
        l146_245(x),
        l146_246(x),
        l146_247(x),
        l146_248(x),
        l146_249(x),
        l146_250(x),
        l146_251(x),
        l146_252(x),
        l146_253(x),
        l146_254(x),
        l146_255(x),
        l146_256(x),
        l146_257(x),
        l146_258(x),
        l146_259(x),
        l146_260(x),
        l146_261(x),
        l146_262(x),
        l146_263(x),
        l146_264(x),
        l146_265(x),
        l146_266(x),
        l146_267(x),
        l146_268(x),
        l146_269(x),
        l146_270(x),
        l146_271(x),
        l146_272(x),
        l146_273(x),
        l146_274(x),
        l146_275(x),
        l146_276(x),
        l146_277(x),
        l146_278(x),
        l146_279(x),
        l146_280(x),
        l146_281(x),
        l146_282(x),
        l146_283(x),
        l146_284(x),
        l146_285(x),
        l146_286(x),
        l146_287(x),
        l146_288(x),
        l146_289(x),
        l146_290(x),
        l146_291(x),
        l146_292(x),
        l146_293(x),
        l146_294(x),
        l146_295(x),
        l146_296(x),
        l146_297(x),
        l146_298(x),
        l146_299(x),
        l146_300(x),
        l146_301(x),
        l146_302(x),
        l146_303(x),
        l146_304(x),
        l146_305(x),
        l146_306(x),
        l146_307(x),
        l146_308(x),
        l146_309(x),
        l146_310(x),
        l146_311(x),
        l146_312(x),
        l146_313(x),
        l146_314(x),
        l146_315(x),
        l146_316(x),
        l146_317(x),
        l146_318(x),
        l146_319(x),
        l146_320(x),
        l146_321(x),
        l146_322(x),
        l146_323(x),
        l146_324(x),
        l146_325(x),
        l146_326(x),
        l146_327(x),
        l146_328(x),
        l146_329(x),
        l146_330(x),
        l146_331(x),
        l146_332(x),
        l146_333(x),
        l146_334(x),
        l146_335(x),
        l146_336(x),
        l146_337(x),
        l146_338(x),
        l146_339(x),
        l146_340(x),
        l146_341(x),
        l146_342(x),
        l146_343(x),
        l146_344(x),
        l146_345(x),
        l146_346(x),
        l146_347(x),
        l146_348(x),
        l146_349(x),
        l146_350(x),
        l146_351(x),
    ]