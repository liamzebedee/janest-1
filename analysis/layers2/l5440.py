import numpy as np


def l5440_0(x):
    # x is a list (or vector) of length 48
    # masks     # add: 111111111111111100000000000000001111111111111111    # sub: 000000000000000000000000000000000000000000000000    # zero: 000000000000000000000000000000000000000000000000
    # bitshifts    x[16] >> 1    x[17] >> 1    x[18] >> 1    x[19] >> 1    x[20] >> 1    x[21] >> 1    x[22] >> 1    x[23] >> 1    x[24] >> 1    x[25] >> 1    x[26] >> 1    x[27] >> 1    x[28] >> 1    x[29] >> 1    x[30] >> 1    x[31] >> 1
    return max(0, x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7] + x[8] + x[9] + x[10] + x[11] + x[12] + x[13] + x[14] + x[15] + -2.0*x[16] + -2.0*x[17] + -2.0*x[18] + -2.0*x[19] + -2.0*x[20] + -2.0*x[21] + -2.0*x[22] + -2.0*x[23] + -2.0*x[24] + -2.0*x[25] + -2.0*x[26] + -2.0*x[27] + -2.0*x[28] + -2.0*x[29] + -2.0*x[30] + -2.0*x[31] + x[32] + x[33] + x[34] + x[35] + x[36] + x[37] + x[38] + x[39] + x[40] + x[41] + x[42] + x[43] + x[44] + x[45] + x[46] + x[47] + -15.0)
def l5440_(x):
    # x is a list (or vector) of length 48
    return [
        l5440_0(x),
    ]


# Generated from reverse engineering
def l5440_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 1
    out = np.empty(1, dtype=np.float32)
    
    biases = [-15.0]
    # for i in range(0, 1):
    for i in range(0, 1):
        s = x[0 + i] + x[1 + i] + x[2 + i] + x[3 + i] + x[4 + i] + x[5 + i] + x[6 + i] + x[7 + i] + x[8 + i] + x[9 + i] + x[10 + i] + x[11 + i] + x[12 + i] + x[13 + i] + x[14 + i] + x[15 + i] + x[32 + i] + x[33 + i] + x[34 + i] + x[35 + i] + x[36 + i] + x[37 + i] + x[38 + i] + x[39 + i] + x[40 + i] + x[41 + i] + x[42 + i] + x[43 + i] + x[44 + i] + x[45 + i] + x[46 + i] + x[47 + i] + -1 * -2.0 * x[i + 16] + -1 * -2.0 * x[i + 17] + -1 * -2.0 * x[i + 18] + -1 * -2.0 * x[i + 19] + -1 * -2.0 * x[i + 20] + -1 * -2.0 * x[i + 21] + -1 * -2.0 * x[i + 22] + -1 * -2.0 * x[i + 23] + -1 * -2.0 * x[i + 24] + -1 * -2.0 * x[i + 25] + -1 * -2.0 * x[i + 26] + -1 * -2.0 * x[i + 27] + -1 * -2.0 * x[i + 28] + -1 * -2.0 * x[i + 29] + -1 * -2.0 * x[i + 30] + -1 * -2.0 * x[i + 31]
        s += biases[i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    return out



