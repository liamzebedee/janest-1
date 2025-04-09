
# Generated from reverse engineering
def l5360_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 160
    out = np.empty(160, dtype=np.float32)
    
    # for i in range(0, 128):
    for i in range(0, 128):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 160):
    for i in range(0, 32):
        s = x[128 + i] + -2.0 * x[i + 160]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5362_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 223
    out = np.empty(223, dtype=np.float32)
    
    # for i in range(0, 97):
    for i in range(0, 97):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(97, 128):
    for i in range(0, 31):
        s = x[96 + i] + x[129 + i]
        s += biases[i]
        out[97 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 159):
    for i in range(0, 31):
        s = x[97 + i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(159, 190):
    for i in range(0, 31):
        s = x[128 + i] + x[129 + i]
        s += biases[i]
        out[159 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(190, 191):
    for i in range(0, 1):
        s = x[128 + i]
        out[190 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(191, 223):
    for i in range(0, 32):
        s = x[128 + i]
        out[191 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5364_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 192
    out = np.empty(192, dtype=np.float32)
    
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
        
    # for i in range(160, 192):
    for i in range(0, 32):
        s = x[191 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5366_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 222
    out = np.empty(222, dtype=np.float32)
    
    # for i in range(0, 97):
    for i in range(0, 97):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x1 (len=1)
    biases = [1.0]
    # for i in range(97, 98):
    for i in range(0, 1):
        s = -1 * x[97 + i]
        s += biases[i]
        out[97 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0]
    # for i in range(98, 99):
    for i in range(0, 1):
        s = x[96 + i] + x[130 + i]
        s += biases[i]
        out[98 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(99, 128):
    for i in range(0, 29):
        s = x[131 + i] + -1 * x[97 + i]
        out[99 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3fffffff (len=30)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(128, 158):
    for i in range(0, 30):
        s = -1 * x[98 + i]
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(158, 188):
    for i in range(0, 30):
        s = x[128 + i] + x[130 + i]
        s += biases[i]
        out[158 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(188, 190):
    for i in range(0, 2):
        s = x[128 + i]
        out[188 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(190, 222):
    for i in range(0, 32):
        s = x[160 + i]
        out[190 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5368_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 192
    out = np.empty(192, dtype=np.float32)
    
    # for i in range(0, 98):
    for i in range(0, 98):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3fffffff (len=30)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(98, 128):
    for i in range(0, 30):
        s = -1 * x[98 + i] + -1 * x[128 + i]
        s += biases[i]
        out[98 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 130):
    for i in range(0, 2):
        s = x[188 + i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(130, 160):
    for i in range(0, 30):
        s = x[158 + i]
        out[130 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 192):
    for i in range(0, 32):
        s = x[190 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5370_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 220
    out = np.empty(220, dtype=np.float32)
    
    # for i in range(0, 98):
    for i in range(0, 98):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3 (len=2)
    biases = [1.0, 1.0]
    # for i in range(98, 100):
    for i in range(0, 2):
        s = -1 * x[98 + i]
        s += biases[i]
        out[98 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0]
    # for i in range(100, 102):
    for i in range(0, 2):
        s = x[96 + i] + x[132 + i]
        s += biases[i]
        out[100 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(102, 128):
    for i in range(0, 26):
        s = x[134 + i] + -1 * x[98 + i]
        out[102 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xfffffff (len=28)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(128, 156):
    for i in range(0, 28):
        s = -1 * x[100 + i]
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(156, 184):
    for i in range(0, 28):
        s = x[128 + i] + x[132 + i]
        s += biases[i]
        out[156 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(184, 188):
    for i in range(0, 4):
        s = x[128 + i]
        out[184 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(188, 220):
    for i in range(0, 32):
        s = x[160 + i]
        out[188 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5372_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 192
    out = np.empty(192, dtype=np.float32)
    
    # for i in range(0, 100):
    for i in range(0, 100):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xfffffff (len=28)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(100, 128):
    for i in range(0, 28):
        s = -1 * x[100 + i] + -1 * x[128 + i]
        s += biases[i]
        out[100 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 132):
    for i in range(0, 4):
        s = x[184 + i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(132, 160):
    for i in range(0, 28):
        s = x[156 + i]
        out[132 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 192):
    for i in range(0, 32):
        s = x[188 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5374_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 216
    out = np.empty(216, dtype=np.float32)
    
    # for i in range(0, 100):
    for i in range(0, 100):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xf (len=4)
    biases = [1.0, 1.0, 1.0, 1.0]
    # for i in range(100, 104):
    for i in range(0, 4):
        s = -1 * x[100 + i]
        s += biases[i]
        out[100 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0]
    # for i in range(104, 108):
    for i in range(0, 4):
        s = x[96 + i] + x[136 + i]
        s += biases[i]
        out[104 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(108, 128):
    for i in range(0, 20):
        s = x[140 + i] + -1 * x[100 + i]
        out[108 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffffff (len=24)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(128, 152):
    for i in range(0, 24):
        s = -1 * x[104 + i]
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(152, 176):
    for i in range(0, 24):
        s = x[128 + i] + x[136 + i]
        s += biases[i]
        out[152 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(176, 184):
    for i in range(0, 8):
        s = x[128 + i]
        out[176 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(184, 216):
    for i in range(0, 32):
        s = x[160 + i]
        out[184 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5376_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 192
    out = np.empty(192, dtype=np.float32)
    
    # for i in range(0, 104):
    for i in range(0, 104):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffffff (len=24)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(104, 128):
    for i in range(0, 24):
        s = -1 * x[104 + i] + -1 * x[128 + i]
        s += biases[i]
        out[104 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 136):
    for i in range(0, 8):
        s = x[176 + i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(136, 160):
    for i in range(0, 24):
        s = x[152 + i]
        out[136 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 192):
    for i in range(0, 32):
        s = x[184 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5378_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 208
    out = np.empty(208, dtype=np.float32)
    
    # for i in range(0, 104):
    for i in range(0, 104):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xff (len=8)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(104, 112):
    for i in range(0, 8):
        s = -1 * x[104 + i]
        s += biases[i]
        out[104 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(112, 120):
    for i in range(0, 8):
        s = x[96 + i] + x[144 + i]
        s += biases[i]
        out[112 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(120, 128):
    for i in range(0, 8):
        s = x[152 + i] + -1 * x[104 + i]
        out[120 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffff (len=16)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(128, 144):
    for i in range(0, 16):
        s = -1 * x[112 + i]
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(144, 160):
    for i in range(0, 16):
        s = x[128 + i] + x[144 + i]
        s += biases[i]
        out[144 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 176):
    for i in range(0, 16):
        s = x[128 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(176, 208):
    for i in range(0, 32):
        s = x[160 + i]
        out[176 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5380_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 192
    out = np.empty(192, dtype=np.float32)
    
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
        
    return out


# Generated from reverse engineering
def l5382_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 160
    out = np.empty(160, dtype=np.float32)
    
    # for i in range(0, 96):
    for i in range(0, 96):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 97):
    for i in range(0, 1):
        s = x[160 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(97, 113):
    for i in range(0, 16):
        s = x[96 + i] + x[161 + i]
        out[97 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x7fff (len=15)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(113, 128):
    for i in range(0, 15):
        s = x[177 + i] + -1 * x[112 + i]
        s += biases[i]
        out[113 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0]
    # for i in range(128, 129):
    for i in range(0, 1):
        s = x[160 + i]
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(129, 145):
    for i in range(0, 16):
        s = x[96 + i] + x[161 + i]
        s += biases[i]
        out[129 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(145, 160):
    for i in range(0, 15):
        s = x[177 + i] + -1 * x[112 + i]
        out[145 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5384_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 192
    out = np.empty(192, dtype=np.float32)
    
    # for i in range(0, 32):
    for i in range(0, 32):
        s = x[64 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(32, 53):
    for i in range(0, 21):
        s = x[0 + i] + x[107 + i] + -2.0 * x[i + 139]
        s += biases[i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(53, 64):
    for i in range(0, 11):
        s = x[21 + i] + x[96 + i] + -2.0 * x[i + 128]
        s += biases[i]
        out[53 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 85):
    for i in range(0, 21):
        s = x[0 + i] + x[107 + i] + -2.0 * x[i + 139]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(85, 96):
    for i in range(0, 11):
        s = x[21 + i] + x[96 + i] + -2.0 * x[i + 128]
        out[85 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(96, 117):
    for i in range(0, 21):
        s = x[0 + i] + x[107 + i] + -2.0 * x[i + 139]
        s += biases[i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(117, 128):
    for i in range(0, 11):
        s = x[21 + i] + x[96 + i] + -2.0 * x[i + 128]
        s += biases[i]
        out[117 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 192):
    for i in range(0, 64):
        s = x[0 + i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5386_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 160
    out = np.empty(160, dtype=np.float32)
    
    # for i in range(0, 64):
    for i in range(0, 64):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 96):
    for i in range(0, 32):
        s = x[64 + i] + -2.0 * x[i + 96]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 160):
    for i in range(0, 64):
        s = x[128 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5388_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 223
    out = np.empty(223, dtype=np.float32)
    
    # for i in range(0, 33):
    for i in range(0, 33):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(33, 64):
    for i in range(0, 31):
        s = x[32 + i] + x[65 + i]
        s += biases[i]
        out[33 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 95):
    for i in range(0, 31):
        s = x[33 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(95, 126):
    for i in range(0, 31):
        s = x[64 + i] + x[65 + i]
        s += biases[i]
        out[95 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(126, 127):
    for i in range(0, 1):
        s = x[64 + i]
        out[126 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(127, 223):
    for i in range(0, 96):
        s = x[64 + i]
        out[127 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5390_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 192
    out = np.empty(192, dtype=np.float32)
    
    # for i in range(0, 33):
    for i in range(0, 33):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x7fffffff (len=31)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(33, 64):
    for i in range(0, 31):
        s = -1 * x[33 + i] + -1 * x[64 + i]
        s += biases[i]
        out[33 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 65):
    for i in range(0, 1):
        s = x[126 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(65, 96):
    for i in range(0, 31):
        s = x[95 + i]
        out[65 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 192):
    for i in range(0, 96):
        s = x[127 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5392_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 222
    out = np.empty(222, dtype=np.float32)
    
    # for i in range(0, 33):
    for i in range(0, 33):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x1 (len=1)
    biases = [1.0]
    # for i in range(33, 34):
    for i in range(0, 1):
        s = -1 * x[33 + i]
        s += biases[i]
        out[33 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0]
    # for i in range(34, 35):
    for i in range(0, 1):
        s = x[32 + i] + x[66 + i]
        s += biases[i]
        out[34 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(35, 64):
    for i in range(0, 29):
        s = x[67 + i] + -1 * x[33 + i]
        out[35 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3fffffff (len=30)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(64, 94):
    for i in range(0, 30):
        s = -1 * x[34 + i]
        s += biases[i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(94, 124):
    for i in range(0, 30):
        s = x[64 + i] + x[66 + i]
        s += biases[i]
        out[94 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(124, 126):
    for i in range(0, 2):
        s = x[64 + i]
        out[124 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(126, 222):
    for i in range(0, 96):
        s = x[96 + i]
        out[126 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5394_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 192
    out = np.empty(192, dtype=np.float32)
    
    # for i in range(0, 34):
    for i in range(0, 34):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3fffffff (len=30)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(34, 64):
    for i in range(0, 30):
        s = -1 * x[34 + i] + -1 * x[64 + i]
        s += biases[i]
        out[34 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 66):
    for i in range(0, 2):
        s = x[124 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(66, 96):
    for i in range(0, 30):
        s = x[94 + i]
        out[66 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 192):
    for i in range(0, 96):
        s = x[126 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5396_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 220
    out = np.empty(220, dtype=np.float32)
    
    # for i in range(0, 34):
    for i in range(0, 34):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3 (len=2)
    biases = [1.0, 1.0]
    # for i in range(34, 36):
    for i in range(0, 2):
        s = -1 * x[34 + i]
        s += biases[i]
        out[34 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0]
    # for i in range(36, 38):
    for i in range(0, 2):
        s = x[32 + i] + x[68 + i]
        s += biases[i]
        out[36 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(38, 64):
    for i in range(0, 26):
        s = x[70 + i] + -1 * x[34 + i]
        out[38 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xfffffff (len=28)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(64, 92):
    for i in range(0, 28):
        s = -1 * x[36 + i]
        s += biases[i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(92, 120):
    for i in range(0, 28):
        s = x[64 + i] + x[68 + i]
        s += biases[i]
        out[92 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(120, 124):
    for i in range(0, 4):
        s = x[64 + i]
        out[120 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(124, 220):
    for i in range(0, 96):
        s = x[96 + i]
        out[124 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5398_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 192
    out = np.empty(192, dtype=np.float32)
    
    # for i in range(0, 36):
    for i in range(0, 36):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xfffffff (len=28)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(36, 64):
    for i in range(0, 28):
        s = -1 * x[36 + i] + -1 * x[64 + i]
        s += biases[i]
        out[36 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 68):
    for i in range(0, 4):
        s = x[120 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(68, 96):
    for i in range(0, 28):
        s = x[92 + i]
        out[68 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 192):
    for i in range(0, 96):
        s = x[124 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5400_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 216
    out = np.empty(216, dtype=np.float32)
    
    # for i in range(0, 36):
    for i in range(0, 36):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xf (len=4)
    biases = [1.0, 1.0, 1.0, 1.0]
    # for i in range(36, 40):
    for i in range(0, 4):
        s = -1 * x[36 + i]
        s += biases[i]
        out[36 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0]
    # for i in range(40, 44):
    for i in range(0, 4):
        s = x[32 + i] + x[72 + i]
        s += biases[i]
        out[40 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(44, 64):
    for i in range(0, 20):
        s = x[76 + i] + -1 * x[36 + i]
        out[44 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffffff (len=24)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(64, 88):
    for i in range(0, 24):
        s = -1 * x[40 + i]
        s += biases[i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(88, 112):
    for i in range(0, 24):
        s = x[64 + i] + x[72 + i]
        s += biases[i]
        out[88 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(112, 120):
    for i in range(0, 8):
        s = x[64 + i]
        out[112 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(120, 216):
    for i in range(0, 96):
        s = x[96 + i]
        out[120 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5402_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 192
    out = np.empty(192, dtype=np.float32)
    
    # for i in range(0, 40):
    for i in range(0, 40):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffffff (len=24)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(40, 64):
    for i in range(0, 24):
        s = -1 * x[40 + i] + -1 * x[64 + i]
        s += biases[i]
        out[40 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 72):
    for i in range(0, 8):
        s = x[112 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(72, 96):
    for i in range(0, 24):
        s = x[88 + i]
        out[72 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 192):
    for i in range(0, 96):
        s = x[120 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5404_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 208
    out = np.empty(208, dtype=np.float32)
    
    # for i in range(0, 40):
    for i in range(0, 40):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xff (len=8)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(40, 48):
    for i in range(0, 8):
        s = -1 * x[40 + i]
        s += biases[i]
        out[40 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(48, 56):
    for i in range(0, 8):
        s = x[32 + i] + x[80 + i]
        s += biases[i]
        out[48 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(56, 64):
    for i in range(0, 8):
        s = x[88 + i] + -1 * x[40 + i]
        out[56 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffff (len=16)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(64, 80):
    for i in range(0, 16):
        s = -1 * x[48 + i]
        s += biases[i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(80, 96):
    for i in range(0, 16):
        s = x[64 + i] + x[80 + i]
        s += biases[i]
        out[80 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 112):
    for i in range(0, 16):
        s = x[64 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(112, 208):
    for i in range(0, 96):
        s = x[96 + i]
        out[112 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5406_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 192
    out = np.empty(192, dtype=np.float32)
    
    # for i in range(0, 48):
    for i in range(0, 48):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffff (len=16)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(48, 64):
    for i in range(0, 16):
        s = -1 * x[48 + i] + -1 * x[64 + i]
        s += biases[i]
        out[48 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 80):
    for i in range(0, 16):
        s = x[96 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(80, 96):
    for i in range(0, 16):
        s = x[80 + i]
        out[80 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 192):
    for i in range(0, 96):
        s = x[112 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5408_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 160
    out = np.empty(160, dtype=np.float32)
    
    # for i in range(0, 32):
    for i in range(0, 32):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(32, 33):
    for i in range(0, 1):
        s = x[96 + i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(33, 49):
    for i in range(0, 16):
        s = x[32 + i] + x[97 + i]
        out[33 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x7fff (len=15)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(49, 64):
    for i in range(0, 15):
        s = x[113 + i] + -1 * x[48 + i]
        s += biases[i]
        out[49 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0]
    # for i in range(64, 65):
    for i in range(0, 1):
        s = x[96 + i]
        s += biases[i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(65, 81):
    for i in range(0, 16):
        s = x[32 + i] + x[97 + i]
        s += biases[i]
        out[65 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(81, 96):
    for i in range(0, 15):
        s = x[113 + i] + -1 * x[48 + i]
        out[81 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 160):
    for i in range(0, 64):
        s = x[128 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5410_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 320
    out = np.empty(320, dtype=np.float32)
    
    biases = [0.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 0.0, 0.0, -1.0, -1.0, -1.0, 0.0, -1.0, -1.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0, -1.0, 0.0, 0.0, 0.0, -1.0, -1.0, 0.0, 0.0, -1.0]
    # for i in range(0, 32):
    for i in range(0, 32):
        s = x[0 + i]
        s += biases[i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x80c4a2e6 (len=32)
    biases = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0]
    # for i in range(32, 64):
    for i in range(0, 32):
        s = x[0 + i]
        s += biases[i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [0.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 0.0, 0.0, -1.0, -1.0, -1.0, 0.0, -1.0, -1.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0, -1.0, 0.0, 0.0, 0.0, -1.0, -1.0, 0.0, 0.0, -1.0]
    # for i in range(64, 96):
    for i in range(0, 32):
        s = x[0 + i]
        s += biases[i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 128):
    for i in range(0, 32):
        s = x[32 + i] + -2.0 * x[i + 64]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x91d5b3f7 (len=32)
    biases = [1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0]
    # for i in range(128, 160):
    for i in range(0, 32):
        s = 0
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, -1.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, -1.0, 0.0, -1.0, 0.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0, 0.0, -1.0, -1.0, 0.0]
    # for i in range(160, 192):
    for i in range(0, 32):
        s = x[96 + i]
        s += biases[i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x7f3b5d19 (len=32)
    biases = [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0]
    # for i in range(192, 224):
    for i in range(0, 32):
        s = x[96 + i]
        s += biases[i]
        out[192 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, -1.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, -1.0, 0.0, -1.0, 0.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0, 0.0, -1.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    # for i in range(224, 288):
    for i in range(0, 64):
        s = x[96 + i]
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x6e2a4c08 (len=32)
    biases = [0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
    # for i in range(288, 320):
    for i in range(0, 32):
        s = 0
        s += biases[i]
        out[288 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5412_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 320
    out = np.empty(320, dtype=np.float32)
    
    # for i in range(0, 32):
    for i in range(0, 32):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(32, 64):
    for i in range(0, 32):
        s = x[32 + i] + -2.0 * x[i + 64]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(64, 96):
    for i in range(0, 32):
        s = x[96 + i] + x[128 + i]
        s += biases[i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 128):
    for i in range(0, 32):
        s = x[96 + i] + x[128 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(128, 160):
    for i in range(0, 32):
        s = x[96 + i] + x[128 + i]
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 192):
    for i in range(0, 32):
        s = x[160 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(192, 224):
    for i in range(0, 32):
        s = x[192 + i] + -2.0 * x[i + 224]
        out[192 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(224, 256):
    for i in range(0, 32):
        s = x[256 + i] + x[288 + i]
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(256, 288):
    for i in range(0, 32):
        s = x[256 + i] + x[288 + i]
        out[256 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(288, 320):
    for i in range(0, 32):
        s = x[256 + i] + x[288 + i]
        s += biases[i]
        out[288 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5414_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 382
    out = np.empty(382, dtype=np.float32)
    
    # for i in range(0, 1):
    for i in range(0, 1):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(1, 32):
    for i in range(0, 31):
        s = x[0 + i] + x[33 + i]
        s += biases[i]
        out[1 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(32, 63):
    for i in range(0, 31):
        s = x[1 + i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(63, 94):
    for i in range(0, 31):
        s = x[32 + i] + x[33 + i]
        s += biases[i]
        out[63 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(94, 95):
    for i in range(0, 1):
        s = x[32 + i]
        out[94 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(95, 159):
    for i in range(0, 64):
        s = x[32 + i]
        out[95 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(159, 191):
    for i in range(0, 32):
        s = x[96 + i] + -2.0 * x[i + 128]
        out[159 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(191, 192):
    for i in range(0, 1):
        s = x[160 + i]
        out[191 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(192, 223):
    for i in range(0, 31):
        s = x[160 + i] + x[193 + i]
        s += biases[i]
        out[192 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(223, 254):
    for i in range(0, 31):
        s = x[161 + i]
        out[223 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(254, 285):
    for i in range(0, 31):
        s = x[192 + i] + x[193 + i]
        s += biases[i]
        out[254 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(285, 286):
    for i in range(0, 1):
        s = x[192 + i]
        out[285 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(286, 350):
    for i in range(0, 64):
        s = x[192 + i]
        out[286 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(350, 382):
    for i in range(0, 32):
        s = x[256 + i] + -2.0 * x[i + 288]
        out[350 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5416_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 446
    out = np.empty(446, dtype=np.float32)
    
    # for i in range(0, 1):
    for i in range(0, 1):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x7fffffff (len=31)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(1, 32):
    for i in range(0, 31):
        s = -1 * x[1 + i] + -1 * x[32 + i]
        s += biases[i]
        out[1 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(32, 33):
    for i in range(0, 1):
        s = x[94 + i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(33, 64):
    for i in range(0, 31):
        s = x[63 + i]
        out[33 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 97):
    for i in range(0, 33):
        s = x[95 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(97, 128):
    for i in range(0, 31):
        s = x[127 + i] + x[160 + i]
        s += biases[i]
        out[97 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 159):
    for i in range(0, 31):
        s = x[128 + i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(159, 190):
    for i in range(0, 31):
        s = x[159 + i] + x[160 + i]
        s += biases[i]
        out[159 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(190, 191):
    for i in range(0, 1):
        s = x[159 + i]
        out[190 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(191, 224):
    for i in range(0, 33):
        s = x[159 + i]
        out[191 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x7fffffff (len=31)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(224, 255):
    for i in range(0, 31):
        s = -1 * x[192 + i] + -1 * x[223 + i]
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(255, 256):
    for i in range(0, 1):
        s = x[285 + i]
        out[255 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(256, 287):
    for i in range(0, 31):
        s = x[254 + i]
        out[256 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(287, 320):
    for i in range(0, 33):
        s = x[286 + i]
        out[287 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(320, 351):
    for i in range(0, 31):
        s = x[318 + i] + x[351 + i]
        s += biases[i]
        out[320 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(351, 382):
    for i in range(0, 31):
        s = x[319 + i]
        out[351 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(382, 413):
    for i in range(0, 31):
        s = x[350 + i] + x[351 + i]
        s += biases[i]
        out[382 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(413, 414):
    for i in range(0, 1):
        s = x[350 + i]
        out[413 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(414, 446):
    for i in range(0, 32):
        s = x[350 + i]
        out[414 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5418_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 444
    out = np.empty(444, dtype=np.float32)
    
    # for i in range(0, 1):
    for i in range(0, 1):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x1 (len=1)
    biases = [1.0]
    # for i in range(1, 2):
    for i in range(0, 1):
        s = -1 * x[1 + i]
        s += biases[i]
        out[1 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0]
    # for i in range(2, 3):
    for i in range(0, 1):
        s = x[0 + i] + x[34 + i]
        s += biases[i]
        out[2 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(3, 32):
    for i in range(0, 29):
        s = x[35 + i] + -1 * x[1 + i]
        out[3 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3fffffff (len=30)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(32, 62):
    for i in range(0, 30):
        s = -1 * x[2 + i]
        s += biases[i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(62, 92):
    for i in range(0, 30):
        s = x[32 + i] + x[34 + i]
        s += biases[i]
        out[62 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(92, 94):
    for i in range(0, 2):
        s = x[32 + i]
        out[92 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(94, 127):
    for i in range(0, 33):
        s = x[64 + i]
        out[94 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x7fffffff (len=31)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(127, 158):
    for i in range(0, 31):
        s = -1 * x[97 + i] + -1 * x[128 + i]
        s += biases[i]
        out[127 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(158, 159):
    for i in range(0, 1):
        s = x[190 + i]
        out[158 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(159, 190):
    for i in range(0, 31):
        s = x[159 + i]
        out[159 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(190, 223):
    for i in range(0, 33):
        s = x[191 + i]
        out[190 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x1 (len=1)
    biases = [1.0]
    # for i in range(223, 224):
    for i in range(0, 1):
        s = -1 * x[224 + i]
        s += biases[i]
        out[223 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0]
    # for i in range(224, 225):
    for i in range(0, 1):
        s = x[223 + i] + x[257 + i]
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(225, 254):
    for i in range(0, 29):
        s = x[258 + i] + -1 * x[224 + i]
        out[225 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3fffffff (len=30)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(254, 284):
    for i in range(0, 30):
        s = -1 * x[225 + i]
        s += biases[i]
        out[254 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(284, 314):
    for i in range(0, 30):
        s = x[255 + i] + x[257 + i]
        s += biases[i]
        out[284 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(314, 316):
    for i in range(0, 2):
        s = x[255 + i]
        out[314 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(316, 349):
    for i in range(0, 33):
        s = x[287 + i]
        out[316 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x7fffffff (len=31)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(349, 380):
    for i in range(0, 31):
        s = -1 * x[320 + i] + -1 * x[351 + i]
        s += biases[i]
        out[349 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(380, 381):
    for i in range(0, 1):
        s = x[413 + i]
        out[380 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(381, 412):
    for i in range(0, 31):
        s = x[382 + i]
        out[381 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(412, 444):
    for i in range(0, 32):
        s = x[414 + i]
        out[412 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5420_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 444
    out = np.empty(444, dtype=np.float32)
    
    # for i in range(0, 2):
    for i in range(0, 2):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3fffffff (len=30)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(2, 32):
    for i in range(0, 30):
        s = -1 * x[2 + i] + -1 * x[32 + i]
        s += biases[i]
        out[2 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(32, 34):
    for i in range(0, 2):
        s = x[92 + i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(34, 64):
    for i in range(0, 30):
        s = x[62 + i]
        out[34 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 97):
    for i in range(0, 33):
        s = x[94 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x1 (len=1)
    biases = [1.0]
    # for i in range(97, 98):
    for i in range(0, 1):
        s = -1 * x[127 + i]
        s += biases[i]
        out[97 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0]
    # for i in range(98, 99):
    for i in range(0, 1):
        s = x[126 + i] + x[160 + i]
        s += biases[i]
        out[98 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(99, 128):
    for i in range(0, 29):
        s = x[161 + i] + -1 * x[127 + i]
        out[99 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3fffffff (len=30)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(128, 158):
    for i in range(0, 30):
        s = -1 * x[128 + i]
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(158, 188):
    for i in range(0, 30):
        s = x[158 + i] + x[160 + i]
        s += biases[i]
        out[158 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(188, 190):
    for i in range(0, 2):
        s = x[158 + i]
        out[188 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(190, 224):
    for i in range(0, 34):
        s = x[190 + i]
        out[190 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3fffffff (len=30)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(224, 254):
    for i in range(0, 30):
        s = -1 * x[224 + i] + -1 * x[254 + i]
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(254, 256):
    for i in range(0, 2):
        s = x[314 + i]
        out[254 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(256, 286):
    for i in range(0, 30):
        s = x[284 + i]
        out[256 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(286, 319):
    for i in range(0, 33):
        s = x[316 + i]
        out[286 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x1 (len=1)
    biases = [1.0]
    # for i in range(319, 320):
    for i in range(0, 1):
        s = -1 * x[349 + i]
        s += biases[i]
        out[319 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0]
    # for i in range(320, 321):
    for i in range(0, 1):
        s = x[348 + i] + x[382 + i]
        s += biases[i]
        out[320 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(321, 350):
    for i in range(0, 29):
        s = x[383 + i] + -1 * x[349 + i]
        out[321 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3fffffff (len=30)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(350, 380):
    for i in range(0, 30):
        s = -1 * x[350 + i]
        s += biases[i]
        out[350 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(380, 410):
    for i in range(0, 30):
        s = x[380 + i] + x[382 + i]
        s += biases[i]
        out[380 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(410, 412):
    for i in range(0, 2):
        s = x[380 + i]
        out[410 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(412, 444):
    for i in range(0, 32):
        s = x[412 + i]
        out[412 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5422_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 440
    out = np.empty(440, dtype=np.float32)
    
    # for i in range(0, 2):
    for i in range(0, 2):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3 (len=2)
    biases = [1.0, 1.0]
    # for i in range(2, 4):
    for i in range(0, 2):
        s = -1 * x[2 + i]
        s += biases[i]
        out[2 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0]
    # for i in range(4, 6):
    for i in range(0, 2):
        s = x[0 + i] + x[36 + i]
        s += biases[i]
        out[4 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(6, 32):
    for i in range(0, 26):
        s = x[38 + i] + -1 * x[2 + i]
        out[6 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xfffffff (len=28)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(32, 60):
    for i in range(0, 28):
        s = -1 * x[4 + i]
        s += biases[i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(60, 88):
    for i in range(0, 28):
        s = x[32 + i] + x[36 + i]
        s += biases[i]
        out[60 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(88, 92):
    for i in range(0, 4):
        s = x[32 + i]
        out[88 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(92, 126):
    for i in range(0, 34):
        s = x[64 + i]
        out[92 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3fffffff (len=30)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(126, 156):
    for i in range(0, 30):
        s = -1 * x[98 + i] + -1 * x[128 + i]
        s += biases[i]
        out[126 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(156, 158):
    for i in range(0, 2):
        s = x[188 + i]
        out[156 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(158, 188):
    for i in range(0, 30):
        s = x[158 + i]
        out[158 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(188, 222):
    for i in range(0, 34):
        s = x[190 + i]
        out[188 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3 (len=2)
    biases = [1.0, 1.0]
    # for i in range(222, 224):
    for i in range(0, 2):
        s = -1 * x[224 + i]
        s += biases[i]
        out[222 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0]
    # for i in range(224, 226):
    for i in range(0, 2):
        s = x[222 + i] + x[258 + i]
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(226, 252):
    for i in range(0, 26):
        s = x[260 + i] + -1 * x[224 + i]
        out[226 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xfffffff (len=28)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(252, 280):
    for i in range(0, 28):
        s = -1 * x[226 + i]
        s += biases[i]
        out[252 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(280, 308):
    for i in range(0, 28):
        s = x[254 + i] + x[258 + i]
        s += biases[i]
        out[280 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(308, 312):
    for i in range(0, 4):
        s = x[254 + i]
        out[308 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(312, 346):
    for i in range(0, 34):
        s = x[286 + i]
        out[312 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3fffffff (len=30)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(346, 376):
    for i in range(0, 30):
        s = -1 * x[320 + i] + -1 * x[350 + i]
        s += biases[i]
        out[346 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(376, 378):
    for i in range(0, 2):
        s = x[410 + i]
        out[376 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(378, 408):
    for i in range(0, 30):
        s = x[380 + i]
        out[378 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(408, 440):
    for i in range(0, 32):
        s = x[412 + i]
        out[408 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5424_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 440
    out = np.empty(440, dtype=np.float32)
    
    # for i in range(0, 4):
    for i in range(0, 4):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xfffffff (len=28)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(4, 32):
    for i in range(0, 28):
        s = -1 * x[4 + i] + -1 * x[32 + i]
        s += biases[i]
        out[4 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(32, 36):
    for i in range(0, 4):
        s = x[88 + i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(36, 64):
    for i in range(0, 28):
        s = x[60 + i]
        out[36 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 98):
    for i in range(0, 34):
        s = x[92 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3 (len=2)
    biases = [1.0, 1.0]
    # for i in range(98, 100):
    for i in range(0, 2):
        s = -1 * x[126 + i]
        s += biases[i]
        out[98 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0]
    # for i in range(100, 102):
    for i in range(0, 2):
        s = x[124 + i] + x[160 + i]
        s += biases[i]
        out[100 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(102, 128):
    for i in range(0, 26):
        s = x[162 + i] + -1 * x[126 + i]
        out[102 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xfffffff (len=28)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(128, 156):
    for i in range(0, 28):
        s = -1 * x[128 + i]
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(156, 184):
    for i in range(0, 28):
        s = x[156 + i] + x[160 + i]
        s += biases[i]
        out[156 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(184, 188):
    for i in range(0, 4):
        s = x[156 + i]
        out[184 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(188, 224):
    for i in range(0, 36):
        s = x[188 + i]
        out[188 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xfffffff (len=28)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(224, 252):
    for i in range(0, 28):
        s = -1 * x[224 + i] + -1 * x[252 + i]
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(252, 256):
    for i in range(0, 4):
        s = x[308 + i]
        out[252 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(256, 284):
    for i in range(0, 28):
        s = x[280 + i]
        out[256 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(284, 318):
    for i in range(0, 34):
        s = x[312 + i]
        out[284 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x3 (len=2)
    biases = [1.0, 1.0]
    # for i in range(318, 320):
    for i in range(0, 2):
        s = -1 * x[346 + i]
        s += biases[i]
        out[318 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0]
    # for i in range(320, 322):
    for i in range(0, 2):
        s = x[344 + i] + x[380 + i]
        s += biases[i]
        out[320 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(322, 348):
    for i in range(0, 26):
        s = x[382 + i] + -1 * x[346 + i]
        out[322 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xfffffff (len=28)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(348, 376):
    for i in range(0, 28):
        s = -1 * x[348 + i]
        s += biases[i]
        out[348 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(376, 404):
    for i in range(0, 28):
        s = x[376 + i] + x[380 + i]
        s += biases[i]
        out[376 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(404, 408):
    for i in range(0, 4):
        s = x[376 + i]
        out[404 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(408, 440):
    for i in range(0, 32):
        s = x[408 + i]
        out[408 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5426_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 432
    out = np.empty(432, dtype=np.float32)
    
    # for i in range(0, 4):
    for i in range(0, 4):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xf (len=4)
    biases = [1.0, 1.0, 1.0, 1.0]
    # for i in range(4, 8):
    for i in range(0, 4):
        s = -1 * x[4 + i]
        s += biases[i]
        out[4 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0]
    # for i in range(8, 12):
    for i in range(0, 4):
        s = x[0 + i] + x[40 + i]
        s += biases[i]
        out[8 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(12, 32):
    for i in range(0, 20):
        s = x[44 + i] + -1 * x[4 + i]
        out[12 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffffff (len=24)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(32, 56):
    for i in range(0, 24):
        s = -1 * x[8 + i]
        s += biases[i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(56, 80):
    for i in range(0, 24):
        s = x[32 + i] + x[40 + i]
        s += biases[i]
        out[56 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(80, 88):
    for i in range(0, 8):
        s = x[32 + i]
        out[80 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(88, 124):
    for i in range(0, 36):
        s = x[64 + i]
        out[88 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xfffffff (len=28)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(124, 152):
    for i in range(0, 28):
        s = -1 * x[100 + i] + -1 * x[128 + i]
        s += biases[i]
        out[124 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(152, 156):
    for i in range(0, 4):
        s = x[184 + i]
        out[152 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(156, 184):
    for i in range(0, 28):
        s = x[156 + i]
        out[156 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(184, 220):
    for i in range(0, 36):
        s = x[188 + i]
        out[184 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xf (len=4)
    biases = [1.0, 1.0, 1.0, 1.0]
    # for i in range(220, 224):
    for i in range(0, 4):
        s = -1 * x[224 + i]
        s += biases[i]
        out[220 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0]
    # for i in range(224, 228):
    for i in range(0, 4):
        s = x[220 + i] + x[260 + i]
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(228, 248):
    for i in range(0, 20):
        s = x[264 + i] + -1 * x[224 + i]
        out[228 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffffff (len=24)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(248, 272):
    for i in range(0, 24):
        s = -1 * x[228 + i]
        s += biases[i]
        out[248 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(272, 296):
    for i in range(0, 24):
        s = x[252 + i] + x[260 + i]
        s += biases[i]
        out[272 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(296, 304):
    for i in range(0, 8):
        s = x[252 + i]
        out[296 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(304, 340):
    for i in range(0, 36):
        s = x[284 + i]
        out[304 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xfffffff (len=28)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(340, 368):
    for i in range(0, 28):
        s = -1 * x[320 + i] + -1 * x[348 + i]
        s += biases[i]
        out[340 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(368, 372):
    for i in range(0, 4):
        s = x[404 + i]
        out[368 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(372, 400):
    for i in range(0, 28):
        s = x[376 + i]
        out[372 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(400, 432):
    for i in range(0, 32):
        s = x[408 + i]
        out[400 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5428_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 432
    out = np.empty(432, dtype=np.float32)
    
    # for i in range(0, 8):
    for i in range(0, 8):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffffff (len=24)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(8, 32):
    for i in range(0, 24):
        s = -1 * x[8 + i] + -1 * x[32 + i]
        s += biases[i]
        out[8 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(32, 40):
    for i in range(0, 8):
        s = x[80 + i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(40, 64):
    for i in range(0, 24):
        s = x[56 + i]
        out[40 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 100):
    for i in range(0, 36):
        s = x[88 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xf (len=4)
    biases = [1.0, 1.0, 1.0, 1.0]
    # for i in range(100, 104):
    for i in range(0, 4):
        s = -1 * x[124 + i]
        s += biases[i]
        out[100 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0]
    # for i in range(104, 108):
    for i in range(0, 4):
        s = x[120 + i] + x[160 + i]
        s += biases[i]
        out[104 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(108, 128):
    for i in range(0, 20):
        s = x[164 + i] + -1 * x[124 + i]
        out[108 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffffff (len=24)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(128, 152):
    for i in range(0, 24):
        s = -1 * x[128 + i]
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(152, 176):
    for i in range(0, 24):
        s = x[152 + i] + x[160 + i]
        s += biases[i]
        out[152 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(176, 184):
    for i in range(0, 8):
        s = x[152 + i]
        out[176 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(184, 224):
    for i in range(0, 40):
        s = x[184 + i]
        out[184 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffffff (len=24)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(224, 248):
    for i in range(0, 24):
        s = -1 * x[224 + i] + -1 * x[248 + i]
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(248, 256):
    for i in range(0, 8):
        s = x[296 + i]
        out[248 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(256, 280):
    for i in range(0, 24):
        s = x[272 + i]
        out[256 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(280, 316):
    for i in range(0, 36):
        s = x[304 + i]
        out[280 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xf (len=4)
    biases = [1.0, 1.0, 1.0, 1.0]
    # for i in range(316, 320):
    for i in range(0, 4):
        s = -1 * x[340 + i]
        s += biases[i]
        out[316 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0]
    # for i in range(320, 324):
    for i in range(0, 4):
        s = x[336 + i] + x[376 + i]
        s += biases[i]
        out[320 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(324, 344):
    for i in range(0, 20):
        s = x[380 + i] + -1 * x[340 + i]
        out[324 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffffff (len=24)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(344, 368):
    for i in range(0, 24):
        s = -1 * x[344 + i]
        s += biases[i]
        out[344 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(368, 392):
    for i in range(0, 24):
        s = x[368 + i] + x[376 + i]
        s += biases[i]
        out[368 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(392, 400):
    for i in range(0, 8):
        s = x[368 + i]
        out[392 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(400, 432):
    for i in range(0, 32):
        s = x[400 + i]
        out[400 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5430_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 416
    out = np.empty(416, dtype=np.float32)
    
    # for i in range(0, 8):
    for i in range(0, 8):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xff (len=8)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(8, 16):
    for i in range(0, 8):
        s = -1 * x[8 + i]
        s += biases[i]
        out[8 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(16, 24):
    for i in range(0, 8):
        s = x[0 + i] + x[48 + i]
        s += biases[i]
        out[16 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(24, 32):
    for i in range(0, 8):
        s = x[56 + i] + -1 * x[8 + i]
        out[24 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffff (len=16)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(32, 48):
    for i in range(0, 16):
        s = -1 * x[16 + i]
        s += biases[i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(48, 64):
    for i in range(0, 16):
        s = x[32 + i] + x[48 + i]
        s += biases[i]
        out[48 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 80):
    for i in range(0, 16):
        s = x[32 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(80, 120):
    for i in range(0, 40):
        s = x[64 + i]
        out[80 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffffff (len=24)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(120, 144):
    for i in range(0, 24):
        s = -1 * x[104 + i] + -1 * x[128 + i]
        s += biases[i]
        out[120 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(144, 152):
    for i in range(0, 8):
        s = x[176 + i]
        out[144 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(152, 176):
    for i in range(0, 24):
        s = x[152 + i]
        out[152 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(176, 216):
    for i in range(0, 40):
        s = x[184 + i]
        out[176 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xff (len=8)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(216, 224):
    for i in range(0, 8):
        s = -1 * x[224 + i]
        s += biases[i]
        out[216 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(224, 232):
    for i in range(0, 8):
        s = x[216 + i] + x[264 + i]
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(232, 240):
    for i in range(0, 8):
        s = x[272 + i] + -1 * x[224 + i]
        out[232 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffff (len=16)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(240, 256):
    for i in range(0, 16):
        s = -1 * x[232 + i]
        s += biases[i]
        out[240 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(256, 272):
    for i in range(0, 16):
        s = x[248 + i] + x[264 + i]
        s += biases[i]
        out[256 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(272, 288):
    for i in range(0, 16):
        s = x[248 + i]
        out[272 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(288, 328):
    for i in range(0, 40):
        s = x[280 + i]
        out[288 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffffff (len=24)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(328, 352):
    for i in range(0, 24):
        s = -1 * x[320 + i] + -1 * x[344 + i]
        s += biases[i]
        out[328 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(352, 360):
    for i in range(0, 8):
        s = x[392 + i]
        out[352 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(360, 384):
    for i in range(0, 24):
        s = x[368 + i]
        out[360 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(384, 416):
    for i in range(0, 32):
        s = x[400 + i]
        out[384 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5432_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 416
    out = np.empty(416, dtype=np.float32)
    
    # for i in range(0, 16):
    for i in range(0, 16):
        s = x[0 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffff (len=16)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(16, 32):
    for i in range(0, 16):
        s = -1 * x[16 + i] + -1 * x[32 + i]
        s += biases[i]
        out[16 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(32, 48):
    for i in range(0, 16):
        s = x[64 + i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(48, 64):
    for i in range(0, 16):
        s = x[48 + i]
        out[48 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 104):
    for i in range(0, 40):
        s = x[80 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xff (len=8)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(104, 112):
    for i in range(0, 8):
        s = -1 * x[120 + i]
        s += biases[i]
        out[104 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(112, 120):
    for i in range(0, 8):
        s = x[112 + i] + x[160 + i]
        s += biases[i]
        out[112 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(120, 128):
    for i in range(0, 8):
        s = x[168 + i] + -1 * x[120 + i]
        out[120 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffff (len=16)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(128, 144):
    for i in range(0, 16):
        s = -1 * x[128 + i]
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(144, 160):
    for i in range(0, 16):
        s = x[144 + i] + x[160 + i]
        s += biases[i]
        out[144 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 176):
    for i in range(0, 16):
        s = x[144 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(176, 224):
    for i in range(0, 48):
        s = x[176 + i]
        out[176 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffff (len=16)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(224, 240):
    for i in range(0, 16):
        s = -1 * x[224 + i] + -1 * x[240 + i]
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(240, 256):
    for i in range(0, 16):
        s = x[272 + i]
        out[240 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(256, 272):
    for i in range(0, 16):
        s = x[256 + i]
        out[256 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(272, 312):
    for i in range(0, 40):
        s = x[288 + i]
        out[272 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xff (len=8)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(312, 320):
    for i in range(0, 8):
        s = -1 * x[328 + i]
        s += biases[i]
        out[312 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(320, 328):
    for i in range(0, 8):
        s = x[320 + i] + x[368 + i]
        s += biases[i]
        out[320 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(328, 336):
    for i in range(0, 8):
        s = x[376 + i] + -1 * x[328 + i]
        out[328 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffff (len=16)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(336, 352):
    for i in range(0, 16):
        s = -1 * x[336 + i]
        s += biases[i]
        out[336 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(352, 368):
    for i in range(0, 16):
        s = x[352 + i] + x[368 + i]
        s += biases[i]
        out[352 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(368, 384):
    for i in range(0, 16):
        s = x[352 + i]
        out[368 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(384, 416):
    for i in range(0, 32):
        s = x[384 + i]
        out[384 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5434_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 320
    out = np.empty(320, dtype=np.float32)
    
    # for i in range(0, 1):
    for i in range(0, 1):
        s = x[64 + i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(1, 17):
    for i in range(0, 16):
        s = x[0 + i] + x[65 + i]
        out[1 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x7fff (len=15)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(17, 32):
    for i in range(0, 15):
        s = x[81 + i] + -1 * x[16 + i]
        s += biases[i]
        out[17 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0]
    # for i in range(32, 33):
    for i in range(0, 1):
        s = x[64 + i]
        s += biases[i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(33, 49):
    for i in range(0, 16):
        s = x[0 + i] + x[65 + i]
        s += biases[i]
        out[33 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(49, 64):
    for i in range(0, 15):
        s = x[81 + i] + -1 * x[16 + i]
        out[49 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(64, 80):
    for i in range(0, 16):
        s = x[96 + i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffff (len=16)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(80, 96):
    for i in range(0, 16):
        s = -1 * x[112 + i] + -1 * x[128 + i]
        s += biases[i]
        out[80 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 112):
    for i in range(0, 16):
        s = x[160 + i]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(112, 128):
    for i in range(0, 16):
        s = x[144 + i]
        out[112 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 160):
    for i in range(0, 32):
        s = x[176 + i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(160, 161):
    for i in range(0, 1):
        s = x[272 + i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(161, 177):
    for i in range(0, 16):
        s = x[208 + i] + x[273 + i]
        out[161 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x7fff (len=15)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(177, 192):
    for i in range(0, 15):
        s = x[289 + i] + -1 * x[224 + i]
        s += biases[i]
        out[177 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0]
    # for i in range(192, 193):
    for i in range(0, 1):
        s = x[272 + i]
        s += biases[i]
        out[192 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(193, 209):
    for i in range(0, 16):
        s = x[208 + i] + x[273 + i]
        s += biases[i]
        out[193 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(209, 224):
    for i in range(0, 15):
        s = x[289 + i] + -1 * x[224 + i]
        out[209 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(224, 240):
    for i in range(0, 16):
        s = x[304 + i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0xffff (len=16)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(240, 256):
    for i in range(0, 16):
        s = -1 * x[320 + i] + -1 * x[336 + i]
        s += biases[i]
        out[240 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(256, 272):
    for i in range(0, 16):
        s = x[368 + i]
        out[256 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(272, 288):
    for i in range(0, 16):
        s = x[352 + i]
        out[272 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(288, 320):
    for i in range(0, 32):
        s = x[384 + i]
        out[288 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5436_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 192
    out = np.empty(192, dtype=np.float32)
    
    # for i in range(0, 32):
    for i in range(0, 32):
        s = x[0 + i] + -2.0 * x[i + 32]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(32, 33):
    for i in range(0, 1):
        s = x[128 + i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(33, 49):
    for i in range(0, 16):
        s = x[64 + i] + x[129 + i]
        out[33 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x7fff (len=15)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(49, 64):
    for i in range(0, 15):
        s = x[145 + i] + -1 * x[80 + i]
        s += biases[i]
        out[49 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0]
    # for i in range(64, 65):
    for i in range(0, 1):
        s = x[128 + i]
        s += biases[i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(65, 81):
    for i in range(0, 16):
        s = x[64 + i] + x[129 + i]
        s += biases[i]
        out[65 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(81, 96):
    for i in range(0, 15):
        s = x[145 + i] + -1 * x[80 + i]
        out[81 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 128):
    for i in range(0, 32):
        s = x[160 + i] + -2.0 * x[i + 192]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(128, 129):
    for i in range(0, 1):
        s = x[288 + i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(129, 145):
    for i in range(0, 16):
        s = x[224 + i] + x[289 + i]
        out[129 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x7fff (len=15)
    biases = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    # for i in range(145, 160):
    for i in range(0, 15):
        s = x[305 + i] + -1 * x[240 + i]
        s += biases[i]
        out[145 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0]
    # for i in range(160, 161):
    for i in range(0, 1):
        s = x[288 + i]
        s += biases[i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
    # for i in range(161, 177):
    for i in range(0, 16):
        s = x[224 + i] + x[289 + i]
        s += biases[i]
        out[161 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(177, 192):
    for i in range(0, 15):
        s = x[305 + i] + -1 * x[240 + i]
        out[177 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5438_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 48
    out = np.empty(48, dtype=np.float32)
    
    biases = [-200.0]
    # for i in range(0, 1):
    for i in range(0, 1):
        s = x[0 + i] + 2.0 * x[i + 1] + 4.0 * x[i + 2] + 8.0 * x[i + 3] + 16.0 * x[i + 4] + 32.0 * x[i + 5] + 64.0 * x[i + 6] + 128.0 * x[i + 7]
        s += biases[i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-240.0]
    # for i in range(1, 2):
    for i in range(0, 1):
        s = x[8 + i] + 2.0 * x[i + 9] + 4.0 * x[i + 10] + 8.0 * x[i + 11] + 16.0 * x[i + 12] + 32.0 * x[i + 13] + 64.0 * x[i + 14] + 128.0 * x[i + 15]
        s += biases[i]
        out[1 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-102.0]
    # for i in range(2, 3):
    for i in range(0, 1):
        s = x[16 + i] + 2.0 * x[i + 17] + 4.0 * x[i + 18] + 8.0 * x[i + 19] + 16.0 * x[i + 20] + 32.0 * x[i + 21] + 64.0 * x[i + 22] + 128.0 * x[i + 23]
        s += biases[i]
        out[2 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-36.0]
    # for i in range(3, 4):
    for i in range(0, 1):
        s = x[24 + i] + 2.0 * x[i + 25] + 4.0 * x[i + 26] + 8.0 * x[i + 27] + 16.0 * x[i + 28] + 32.0 * x[i + 29] + 64.0 * x[i + 30] + 128.0 * x[i + 31]
        s += biases[i]
        out[3 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-61.0]
    # for i in range(4, 5):
    for i in range(0, 1):
        s = x[32 + i] + 2.0 * x[i + 33] + 4.0 * x[i + 34] + 8.0 * x[i + 35] + 16.0 * x[i + 36] + 32.0 * x[i + 37] + 64.0 * x[i + 38] + 128.0 * x[i + 39] + -2.0 * x[i + 64] + -4.0 * x[i + 65] + -8.0 * x[i + 66] + -16.0 * x[i + 67] + -32.0 * x[i + 68] + -64.0 * x[i + 69] + -128.0 * x[i + 70] + -256.0 * x[i + 71]
        s += biases[i]
        out[4 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-65.0]
    # for i in range(5, 6):
    for i in range(0, 1):
        s = x[40 + i] + 2.0 * x[i + 41] + 4.0 * x[i + 42] + 8.0 * x[i + 43] + 16.0 * x[i + 44] + 32.0 * x[i + 45] + 64.0 * x[i + 46] + 128.0 * x[i + 47] + -2.0 * x[i + 72] + -4.0 * x[i + 73] + -8.0 * x[i + 74] + -16.0 * x[i + 75] + -32.0 * x[i + 76] + -64.0 * x[i + 77] + -128.0 * x[i + 78] + -256.0 * x[i + 79]
        s += biases[i]
        out[5 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-171.0]
    # for i in range(6, 7):
    for i in range(0, 1):
        s = x[48 + i] + 2.0 * x[i + 49] + 4.0 * x[i + 50] + 8.0 * x[i + 51] + 16.0 * x[i + 52] + 32.0 * x[i + 53] + 64.0 * x[i + 54] + 128.0 * x[i + 55] + -2.0 * x[i + 80] + -4.0 * x[i + 81] + -8.0 * x[i + 82] + -16.0 * x[i + 83] + -32.0 * x[i + 84] + -64.0 * x[i + 85] + -128.0 * x[i + 86] + -256.0 * x[i + 87]
        s += biases[i]
        out[6 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-51.0]
    # for i in range(7, 8):
    for i in range(0, 1):
        s = x[56 + i] + 2.0 * x[i + 57] + 4.0 * x[i + 58] + 8.0 * x[i + 59] + 16.0 * x[i + 60] + 32.0 * x[i + 61] + 64.0 * x[i + 62] + 128.0 * x[i + 63] + -2.0 * x[i + 88] + -4.0 * x[i + 89] + -8.0 * x[i + 90] + -16.0 * x[i + 91] + -32.0 * x[i + 92] + -64.0 * x[i + 93] + -128.0 * x[i + 94] + -256.0 * x[i + 95]
        s += biases[i]
        out[7 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-195.0]
    # for i in range(8, 9):
    for i in range(0, 1):
        s = x[96 + i] + 2.0 * x[i + 97] + 4.0 * x[i + 98] + 8.0 * x[i + 99] + 16.0 * x[i + 100] + 32.0 * x[i + 101] + 64.0 * x[i + 102] + 128.0 * x[i + 103]
        s += biases[i]
        out[8 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-186.0]
    # for i in range(9, 10):
    for i in range(0, 1):
        s = x[104 + i] + 2.0 * x[i + 105] + 4.0 * x[i + 106] + 8.0 * x[i + 107] + 16.0 * x[i + 108] + 32.0 * x[i + 109] + 64.0 * x[i + 110] + 128.0 * x[i + 111]
        s += biases[i]
        out[9 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-173.0]
    # for i in range(10, 11):
    for i in range(0, 1):
        s = x[112 + i] + 2.0 * x[i + 113] + 4.0 * x[i + 114] + 8.0 * x[i + 115] + 16.0 * x[i + 116] + 32.0 * x[i + 117] + 64.0 * x[i + 118] + 128.0 * x[i + 119]
        s += biases[i]
        out[10 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-228.0]
    # for i in range(11, 12):
    for i in range(0, 1):
        s = x[120 + i] + 2.0 * x[i + 121] + 4.0 * x[i + 122] + 8.0 * x[i + 123] + 16.0 * x[i + 124] + 32.0 * x[i + 125] + 64.0 * x[i + 126] + 128.0 * x[i + 127]
        s += biases[i]
        out[11 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-118.0]
    # for i in range(12, 13):
    for i in range(0, 1):
        s = x[128 + i] + 2.0 * x[i + 129] + 4.0 * x[i + 130] + 8.0 * x[i + 131] + 16.0 * x[i + 132] + 32.0 * x[i + 133] + 64.0 * x[i + 134] + 128.0 * x[i + 135] + -2.0 * x[i + 160] + -4.0 * x[i + 161] + -8.0 * x[i + 162] + -16.0 * x[i + 163] + -32.0 * x[i + 164] + -64.0 * x[i + 165] + -128.0 * x[i + 166] + -256.0 * x[i + 167]
        s += biases[i]
        out[12 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-150.0]
    # for i in range(13, 14):
    for i in range(0, 1):
        s = x[136 + i] + 2.0 * x[i + 137] + 4.0 * x[i + 138] + 8.0 * x[i + 139] + 16.0 * x[i + 140] + 32.0 * x[i + 141] + 64.0 * x[i + 142] + 128.0 * x[i + 143] + -2.0 * x[i + 168] + -4.0 * x[i + 169] + -8.0 * x[i + 170] + -16.0 * x[i + 171] + -32.0 * x[i + 172] + -64.0 * x[i + 173] + -128.0 * x[i + 174] + -256.0 * x[i + 175]
        s += biases[i]
        out[13 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-251.0]
    # for i in range(14, 15):
    for i in range(0, 1):
        s = x[144 + i] + 2.0 * x[i + 145] + 4.0 * x[i + 146] + 8.0 * x[i + 147] + 16.0 * x[i + 148] + 32.0 * x[i + 149] + 64.0 * x[i + 150] + 128.0 * x[i + 151] + -2.0 * x[i + 176] + -4.0 * x[i + 177] + -8.0 * x[i + 178] + -16.0 * x[i + 179] + -32.0 * x[i + 180] + -64.0 * x[i + 181] + -128.0 * x[i + 182] + -256.0 * x[i + 183]
        s += biases[i]
        out[14 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-125.0]
    # for i in range(15, 16):
    for i in range(0, 1):
        s = x[152 + i] + 2.0 * x[i + 153] + 4.0 * x[i + 154] + 8.0 * x[i + 155] + 16.0 * x[i + 156] + 32.0 * x[i + 157] + 64.0 * x[i + 158] + 128.0 * x[i + 159] + -2.0 * x[i + 184] + -4.0 * x[i + 185] + -8.0 * x[i + 186] + -16.0 * x[i + 187] + -32.0 * x[i + 188] + -64.0 * x[i + 189] + -128.0 * x[i + 190] + -256.0 * x[i + 191]
        s += biases[i]
        out[15 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-199.0]
    # for i in range(16, 17):
    for i in range(0, 1):
        s = x[0 + i] + 2.0 * x[i + 1] + 4.0 * x[i + 2] + 8.0 * x[i + 3] + 16.0 * x[i + 4] + 32.0 * x[i + 5] + 64.0 * x[i + 6] + 128.0 * x[i + 7]
        s += biases[i]
        out[16 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-239.0]
    # for i in range(17, 18):
    for i in range(0, 1):
        s = x[8 + i] + 2.0 * x[i + 9] + 4.0 * x[i + 10] + 8.0 * x[i + 11] + 16.0 * x[i + 12] + 32.0 * x[i + 13] + 64.0 * x[i + 14] + 128.0 * x[i + 15]
        s += biases[i]
        out[17 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-101.0]
    # for i in range(18, 19):
    for i in range(0, 1):
        s = x[16 + i] + 2.0 * x[i + 17] + 4.0 * x[i + 18] + 8.0 * x[i + 19] + 16.0 * x[i + 20] + 32.0 * x[i + 21] + 64.0 * x[i + 22] + 128.0 * x[i + 23]
        s += biases[i]
        out[18 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-35.0]
    # for i in range(19, 20):
    for i in range(0, 1):
        s = x[24 + i] + 2.0 * x[i + 25] + 4.0 * x[i + 26] + 8.0 * x[i + 27] + 16.0 * x[i + 28] + 32.0 * x[i + 29] + 64.0 * x[i + 30] + 128.0 * x[i + 31]
        s += biases[i]
        out[19 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-60.0]
    # for i in range(20, 21):
    for i in range(0, 1):
        s = x[32 + i] + 2.0 * x[i + 33] + 4.0 * x[i + 34] + 8.0 * x[i + 35] + 16.0 * x[i + 36] + 32.0 * x[i + 37] + 64.0 * x[i + 38] + 128.0 * x[i + 39] + -2.0 * x[i + 64] + -4.0 * x[i + 65] + -8.0 * x[i + 66] + -16.0 * x[i + 67] + -32.0 * x[i + 68] + -64.0 * x[i + 69] + -128.0 * x[i + 70] + -256.0 * x[i + 71]
        s += biases[i]
        out[20 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-64.0]
    # for i in range(21, 22):
    for i in range(0, 1):
        s = x[40 + i] + 2.0 * x[i + 41] + 4.0 * x[i + 42] + 8.0 * x[i + 43] + 16.0 * x[i + 44] + 32.0 * x[i + 45] + 64.0 * x[i + 46] + 128.0 * x[i + 47] + -2.0 * x[i + 72] + -4.0 * x[i + 73] + -8.0 * x[i + 74] + -16.0 * x[i + 75] + -32.0 * x[i + 76] + -64.0 * x[i + 77] + -128.0 * x[i + 78] + -256.0 * x[i + 79]
        s += biases[i]
        out[21 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-170.0]
    # for i in range(22, 23):
    for i in range(0, 1):
        s = x[48 + i] + 2.0 * x[i + 49] + 4.0 * x[i + 50] + 8.0 * x[i + 51] + 16.0 * x[i + 52] + 32.0 * x[i + 53] + 64.0 * x[i + 54] + 128.0 * x[i + 55] + -2.0 * x[i + 80] + -4.0 * x[i + 81] + -8.0 * x[i + 82] + -16.0 * x[i + 83] + -32.0 * x[i + 84] + -64.0 * x[i + 85] + -128.0 * x[i + 86] + -256.0 * x[i + 87]
        s += biases[i]
        out[22 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-50.0]
    # for i in range(23, 24):
    for i in range(0, 1):
        s = x[56 + i] + 2.0 * x[i + 57] + 4.0 * x[i + 58] + 8.0 * x[i + 59] + 16.0 * x[i + 60] + 32.0 * x[i + 61] + 64.0 * x[i + 62] + 128.0 * x[i + 63] + -2.0 * x[i + 88] + -4.0 * x[i + 89] + -8.0 * x[i + 90] + -16.0 * x[i + 91] + -32.0 * x[i + 92] + -64.0 * x[i + 93] + -128.0 * x[i + 94] + -256.0 * x[i + 95]
        s += biases[i]
        out[23 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-194.0]
    # for i in range(24, 25):
    for i in range(0, 1):
        s = x[96 + i] + 2.0 * x[i + 97] + 4.0 * x[i + 98] + 8.0 * x[i + 99] + 16.0 * x[i + 100] + 32.0 * x[i + 101] + 64.0 * x[i + 102] + 128.0 * x[i + 103]
        s += biases[i]
        out[24 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-185.0]
    # for i in range(25, 26):
    for i in range(0, 1):
        s = x[104 + i] + 2.0 * x[i + 105] + 4.0 * x[i + 106] + 8.0 * x[i + 107] + 16.0 * x[i + 108] + 32.0 * x[i + 109] + 64.0 * x[i + 110] + 128.0 * x[i + 111]
        s += biases[i]
        out[25 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-172.0]
    # for i in range(26, 27):
    for i in range(0, 1):
        s = x[112 + i] + 2.0 * x[i + 113] + 4.0 * x[i + 114] + 8.0 * x[i + 115] + 16.0 * x[i + 116] + 32.0 * x[i + 117] + 64.0 * x[i + 118] + 128.0 * x[i + 119]
        s += biases[i]
        out[26 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-227.0]
    # for i in range(27, 28):
    for i in range(0, 1):
        s = x[120 + i] + 2.0 * x[i + 121] + 4.0 * x[i + 122] + 8.0 * x[i + 123] + 16.0 * x[i + 124] + 32.0 * x[i + 125] + 64.0 * x[i + 126] + 128.0 * x[i + 127]
        s += biases[i]
        out[27 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-117.0]
    # for i in range(28, 29):
    for i in range(0, 1):
        s = x[128 + i] + 2.0 * x[i + 129] + 4.0 * x[i + 130] + 8.0 * x[i + 131] + 16.0 * x[i + 132] + 32.0 * x[i + 133] + 64.0 * x[i + 134] + 128.0 * x[i + 135] + -2.0 * x[i + 160] + -4.0 * x[i + 161] + -8.0 * x[i + 162] + -16.0 * x[i + 163] + -32.0 * x[i + 164] + -64.0 * x[i + 165] + -128.0 * x[i + 166] + -256.0 * x[i + 167]
        s += biases[i]
        out[28 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-149.0]
    # for i in range(29, 30):
    for i in range(0, 1):
        s = x[136 + i] + 2.0 * x[i + 137] + 4.0 * x[i + 138] + 8.0 * x[i + 139] + 16.0 * x[i + 140] + 32.0 * x[i + 141] + 64.0 * x[i + 142] + 128.0 * x[i + 143] + -2.0 * x[i + 168] + -4.0 * x[i + 169] + -8.0 * x[i + 170] + -16.0 * x[i + 171] + -32.0 * x[i + 172] + -64.0 * x[i + 173] + -128.0 * x[i + 174] + -256.0 * x[i + 175]
        s += biases[i]
        out[29 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-250.0]
    # for i in range(30, 31):
    for i in range(0, 1):
        s = x[144 + i] + 2.0 * x[i + 145] + 4.0 * x[i + 146] + 8.0 * x[i + 147] + 16.0 * x[i + 148] + 32.0 * x[i + 149] + 64.0 * x[i + 150] + 128.0 * x[i + 151] + -2.0 * x[i + 176] + -4.0 * x[i + 177] + -8.0 * x[i + 178] + -16.0 * x[i + 179] + -32.0 * x[i + 180] + -64.0 * x[i + 181] + -128.0 * x[i + 182] + -256.0 * x[i + 183]
        s += biases[i]
        out[30 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-124.0]
    # for i in range(31, 32):
    for i in range(0, 1):
        s = x[152 + i] + 2.0 * x[i + 153] + 4.0 * x[i + 154] + 8.0 * x[i + 155] + 16.0 * x[i + 156] + 32.0 * x[i + 157] + 64.0 * x[i + 158] + 128.0 * x[i + 159] + -2.0 * x[i + 184] + -4.0 * x[i + 185] + -8.0 * x[i + 186] + -16.0 * x[i + 187] + -32.0 * x[i + 188] + -64.0 * x[i + 189] + -128.0 * x[i + 190] + -256.0 * x[i + 191]
        s += biases[i]
        out[31 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-198.0]
    # for i in range(32, 33):
    for i in range(0, 1):
        s = x[0 + i] + 2.0 * x[i + 1] + 4.0 * x[i + 2] + 8.0 * x[i + 3] + 16.0 * x[i + 4] + 32.0 * x[i + 5] + 64.0 * x[i + 6] + 128.0 * x[i + 7]
        s += biases[i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-238.0]
    # for i in range(33, 34):
    for i in range(0, 1):
        s = x[8 + i] + 2.0 * x[i + 9] + 4.0 * x[i + 10] + 8.0 * x[i + 11] + 16.0 * x[i + 12] + 32.0 * x[i + 13] + 64.0 * x[i + 14] + 128.0 * x[i + 15]
        s += biases[i]
        out[33 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-100.0]
    # for i in range(34, 35):
    for i in range(0, 1):
        s = x[16 + i] + 2.0 * x[i + 17] + 4.0 * x[i + 18] + 8.0 * x[i + 19] + 16.0 * x[i + 20] + 32.0 * x[i + 21] + 64.0 * x[i + 22] + 128.0 * x[i + 23]
        s += biases[i]
        out[34 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-34.0]
    # for i in range(35, 36):
    for i in range(0, 1):
        s = x[24 + i] + 2.0 * x[i + 25] + 4.0 * x[i + 26] + 8.0 * x[i + 27] + 16.0 * x[i + 28] + 32.0 * x[i + 29] + 64.0 * x[i + 30] + 128.0 * x[i + 31]
        s += biases[i]
        out[35 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-59.0]
    # for i in range(36, 37):
    for i in range(0, 1):
        s = x[32 + i] + 2.0 * x[i + 33] + 4.0 * x[i + 34] + 8.0 * x[i + 35] + 16.0 * x[i + 36] + 32.0 * x[i + 37] + 64.0 * x[i + 38] + 128.0 * x[i + 39] + -2.0 * x[i + 64] + -4.0 * x[i + 65] + -8.0 * x[i + 66] + -16.0 * x[i + 67] + -32.0 * x[i + 68] + -64.0 * x[i + 69] + -128.0 * x[i + 70] + -256.0 * x[i + 71]
        s += biases[i]
        out[36 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-63.0]
    # for i in range(37, 38):
    for i in range(0, 1):
        s = x[40 + i] + 2.0 * x[i + 41] + 4.0 * x[i + 42] + 8.0 * x[i + 43] + 16.0 * x[i + 44] + 32.0 * x[i + 45] + 64.0 * x[i + 46] + 128.0 * x[i + 47] + -2.0 * x[i + 72] + -4.0 * x[i + 73] + -8.0 * x[i + 74] + -16.0 * x[i + 75] + -32.0 * x[i + 76] + -64.0 * x[i + 77] + -128.0 * x[i + 78] + -256.0 * x[i + 79]
        s += biases[i]
        out[37 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-169.0]
    # for i in range(38, 39):
    for i in range(0, 1):
        s = x[48 + i] + 2.0 * x[i + 49] + 4.0 * x[i + 50] + 8.0 * x[i + 51] + 16.0 * x[i + 52] + 32.0 * x[i + 53] + 64.0 * x[i + 54] + 128.0 * x[i + 55] + -2.0 * x[i + 80] + -4.0 * x[i + 81] + -8.0 * x[i + 82] + -16.0 * x[i + 83] + -32.0 * x[i + 84] + -64.0 * x[i + 85] + -128.0 * x[i + 86] + -256.0 * x[i + 87]
        s += biases[i]
        out[38 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-49.0]
    # for i in range(39, 40):
    for i in range(0, 1):
        s = x[56 + i] + 2.0 * x[i + 57] + 4.0 * x[i + 58] + 8.0 * x[i + 59] + 16.0 * x[i + 60] + 32.0 * x[i + 61] + 64.0 * x[i + 62] + 128.0 * x[i + 63] + -2.0 * x[i + 88] + -4.0 * x[i + 89] + -8.0 * x[i + 90] + -16.0 * x[i + 91] + -32.0 * x[i + 92] + -64.0 * x[i + 93] + -128.0 * x[i + 94] + -256.0 * x[i + 95]
        s += biases[i]
        out[39 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-193.0]
    # for i in range(40, 41):
    for i in range(0, 1):
        s = x[96 + i] + 2.0 * x[i + 97] + 4.0 * x[i + 98] + 8.0 * x[i + 99] + 16.0 * x[i + 100] + 32.0 * x[i + 101] + 64.0 * x[i + 102] + 128.0 * x[i + 103]
        s += biases[i]
        out[40 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-184.0]
    # for i in range(41, 42):
    for i in range(0, 1):
        s = x[104 + i] + 2.0 * x[i + 105] + 4.0 * x[i + 106] + 8.0 * x[i + 107] + 16.0 * x[i + 108] + 32.0 * x[i + 109] + 64.0 * x[i + 110] + 128.0 * x[i + 111]
        s += biases[i]
        out[41 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-171.0]
    # for i in range(42, 43):
    for i in range(0, 1):
        s = x[112 + i] + 2.0 * x[i + 113] + 4.0 * x[i + 114] + 8.0 * x[i + 115] + 16.0 * x[i + 116] + 32.0 * x[i + 117] + 64.0 * x[i + 118] + 128.0 * x[i + 119]
        s += biases[i]
        out[42 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-226.0]
    # for i in range(43, 44):
    for i in range(0, 1):
        s = x[120 + i] + 2.0 * x[i + 121] + 4.0 * x[i + 122] + 8.0 * x[i + 123] + 16.0 * x[i + 124] + 32.0 * x[i + 125] + 64.0 * x[i + 126] + 128.0 * x[i + 127]
        s += biases[i]
        out[43 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-116.0]
    # for i in range(44, 45):
    for i in range(0, 1):
        s = x[128 + i] + 2.0 * x[i + 129] + 4.0 * x[i + 130] + 8.0 * x[i + 131] + 16.0 * x[i + 132] + 32.0 * x[i + 133] + 64.0 * x[i + 134] + 128.0 * x[i + 135] + -2.0 * x[i + 160] + -4.0 * x[i + 161] + -8.0 * x[i + 162] + -16.0 * x[i + 163] + -32.0 * x[i + 164] + -64.0 * x[i + 165] + -128.0 * x[i + 166] + -256.0 * x[i + 167]
        s += biases[i]
        out[44 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-148.0]
    # for i in range(45, 46):
    for i in range(0, 1):
        s = x[136 + i] + 2.0 * x[i + 137] + 4.0 * x[i + 138] + 8.0 * x[i + 139] + 16.0 * x[i + 140] + 32.0 * x[i + 141] + 64.0 * x[i + 142] + 128.0 * x[i + 143] + -2.0 * x[i + 168] + -4.0 * x[i + 169] + -8.0 * x[i + 170] + -16.0 * x[i + 171] + -32.0 * x[i + 172] + -64.0 * x[i + 173] + -128.0 * x[i + 174] + -256.0 * x[i + 175]
        s += biases[i]
        out[45 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-249.0]
    # for i in range(46, 47):
    for i in range(0, 1):
        s = x[144 + i] + 2.0 * x[i + 145] + 4.0 * x[i + 146] + 8.0 * x[i + 147] + 16.0 * x[i + 148] + 32.0 * x[i + 149] + 64.0 * x[i + 150] + 128.0 * x[i + 151] + -2.0 * x[i + 176] + -4.0 * x[i + 177] + -8.0 * x[i + 178] + -16.0 * x[i + 179] + -32.0 * x[i + 180] + -64.0 * x[i + 181] + -128.0 * x[i + 182] + -256.0 * x[i + 183]
        s += biases[i]
        out[46 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-123.0]
    # for i in range(47, 48):
    for i in range(0, 1):
        s = x[152 + i] + 2.0 * x[i + 153] + 4.0 * x[i + 154] + 8.0 * x[i + 155] + 16.0 * x[i + 156] + 32.0 * x[i + 157] + 64.0 * x[i + 158] + 128.0 * x[i + 159] + -2.0 * x[i + 184] + -4.0 * x[i + 185] + -8.0 * x[i + 186] + -16.0 * x[i + 187] + -32.0 * x[i + 188] + -64.0 * x[i + 189] + -128.0 * x[i + 190] + -256.0 * x[i + 191]
        s += biases[i]
        out[47 + i] = s if s > 0 else 0.0 # ReLu
        
    return out


# Generated from reverse engineering
def l5440_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 1
    out = np.empty(1, dtype=np.float32)
    
    biases = [-15.0]
    # for i in range(0, 1):
    for i in range(0, 1):
        s = x[0 + i] + x[1 + i] + x[2 + i] + x[3 + i] + x[4 + i] + x[5 + i] + x[6 + i] + x[7 + i] + x[8 + i] + x[9 + i] + x[10 + i] + x[11 + i] + x[12 + i] + x[13 + i] + x[14 + i] + x[15 + i] + x[32 + i] + x[33 + i] + x[34 + i] + x[35 + i] + x[36 + i] + x[37 + i] + x[38 + i] + x[39 + i] + x[40 + i] + x[41 + i] + x[42 + i] + x[43 + i] + x[44 + i] + x[45 + i] + x[46 + i] + x[47 + i] + -2.0 * x[i + 16] + -2.0 * x[i + 17] + -2.0 * x[i + 18] + -2.0 * x[i + 19] + -2.0 * x[i + 20] + -2.0 * x[i + 21] + -2.0 * x[i + 22] + -2.0 * x[i + 23] + -2.0 * x[i + 24] + -2.0 * x[i + 25] + -2.0 * x[i + 26] + -2.0 * x[i + 27] + -2.0 * x[i + 28] + -2.0 * x[i + 29] + -2.0 * x[i + 30] + -2.0 * x[i + 31]
        s += biases[i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    return out
