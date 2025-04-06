# def l2_56(x):
#     # x is a list (or vector) of length 224
#     # masks     # add: 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111111111111111111111111111111111111111111111111110000000000000000000000000000000000000000000000000000000    # sub: 00000000000000000000000000000000000000000000000000000000111111111111111111111111111111111111111111111111111111110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000    # zero: 11111111111111111111111111111111111111111111111111111111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111111111111111111111111111111111111111111111111
#     # bitshifts
#     return max(0, -1.0*x[56] + -1.0*x[57] + -1.0*x[58] + -1.0*x[59] + -1.0*x[60] + -1.0*x[61] + -1.0*x[62] + -1.0*x[63] + -1.0*x[64] + -1.0*x[65] + -1.0*x[66] + -1.0*x[67] + -1.0*x[68] + -1.0*x[69] + -1.0*x[70] + -1.0*x[71] + -1.0*x[72] + -1.0*x[73] + -1.0*x[74] + -1.0*x[75] + -1.0*x[76] + -1.0*x[77] + -1.0*x[78] + -1.0*x[79] + -1.0*x[80] + -1.0*x[81] + -1.0*x[82] + -1.0*x[83] + -1.0*x[84] + -1.0*x[85] + -1.0*x[86] + -1.0*x[87] + -1.0*x[88] + -1.0*x[89] + -1.0*x[90] + -1.0*x[91] + -1.0*x[92] + -1.0*x[93] + -1.0*x[94] + -1.0*x[95] + -1.0*x[96] + -1.0*x[97] + -1.0*x[98] + -1.0*x[99] + -1.0*x[100] + -1.0*x[101] + -1.0*x[102] + -1.0*x[103] + -1.0*x[104] + -1.0*x[105] + -1.0*x[106] + -1.0*x[107] + -1.0*x[108] + -1.0*x[109] + -1.0*x[110] + -1.0*x[111] + x[112] + x[113] + x[114] + x[115] + x[116] + x[117] + x[118] + x[119] + x[120] + x[121] + x[122] + x[123] + x[124] + x[125] + x[126] + x[127] + x[128] + x[129] + x[130] + x[131] + x[132] + x[133] + x[134] + x[135] + x[136] + x[137] + x[138] + x[139] + x[140] + x[141] + x[142] + x[143] + x[144] + x[145] + x[146] + x[147] + x[148] + x[149] + x[150] + x[151] + x[152] + x[153] + x[154] + x[155] + x[156] + x[157] + x[158] + x[159] + x[160] + x[161] + x[162] + x[163] + x[164] + x[165] + x[166] + x[167] + x[168] + -1.0)


# I imagine this models something like:

adds = "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111111111111111111111111111111111111111111111111110000000000000000000000000000000000000000000000000000000"
subs = "00000000000000000000000000000000000000000000000000000000111111111111111111111111111111111111111111111111111111110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"


def get_continuous_ranges(s: str):
    if not s:
        return []
    ranges, start = [], 0
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            ranges.append((start, i-1, int(s[start])))
            start = i
    ranges.append((start, len(s)-1, int(s[start])))
    return ranges

print(get_continuous_ranges(adds))
print(get_continuous_ranges(subs))

# (py39) ➜  js git:(main) ✗ python analysis/l2_56.py
# [(0, 111, '0'), (112, 168, '1'), (169, 223, '0')]
# [(0, 55, '0'), (56, 111, '1'), (112, 223, '0')]

def to_bitwise_op(ranges):
    # e.g.
    # input: [(0, 111, '0'), (112, 168, '1'), (169, 223, '0')]
    # output: ((1 << 112) - 1) - ((1 << 55) - 1)
    # algo:
    # - select from ranges, where '1', the start
    # - construct (1 << start) - 1
    # - then subtract all the other ones
    # - return the whole thing
    # - we can do this by iterating over the ranges, and XORing the results together
    exprs = []
    
    # search index highest 1
    highest_1 = 0
    for i, (start, end, value) in enumerate(ranges):
        if value == 1:
            highest_1 = i
    
    for (start, end, value) in ranges[highest_1:]:
        # print(start, end, value)
        if value == 1:
            exprs.append(f"((1 << {start}) - 1)")
        elif value == 0:
            b = end
            a = start
            d = b - a + 1
            exprs.append(f"((1 << {d}) - 1)")
    return " - ".join(exprs)

print(to_bitwise_op(get_continuous_ranges(adds)))
print(to_bitwise_op(get_continuous_ranges(subs)))
# print("((1 << 112) - 1) - ((1 << 55) - 1)")
exit()

# add 112-168
# sub 56-111

# write a bitshift expression for this
# mask_add = ((1 << 56) - 1) << 112
# mask_add = (1 << 224-1) >> 112
mask_add = (1 << 63) # string of 64 chars, first is 1
# mask_add = ((1 << 63) - 1)
# it's like pushing onto the stack in reverse
# push: 65*1
# 

# mask_add = ((1 << 224) - 1) - ((1 << 56) - 1) & ((1 << 168) - 1)
# print(int(mask_add))
# print(int(adds, 2))

print(bin(
    # 224 bits all 1
    # ((1 << 224) - 1) # 1x1,64x0
    
    # this is our string, but need to NOT
    # ((1 << 224) - 1) - ((1 << 56-1) - 1) ^ ((1 << 112) - 1)
    # ((1 << 224) - 1) - ((1 << 44) - 1) & ((1 << 112) - 1)
    # ((1 << 224) - 1) ^ ((1 << 112) - 1) 
    #| ((1 << 56) - 1)
    # (1 << 224) - 1 - (1 << 112) - (1 << 56)
    
    ((1 << 112) - 1) - ((1 << 55) - 1)
    # 0b1111111111111111111111111111111111111111111111111111111110000000000000000000000000000000000000000000000000000000
    # 0b1111111111111111111111111111111111111111111111111111111110000000000000000000000000000000000000000000000000000000
    
    
    
    # anotehr way to build this
    # 2**(236) * 1 - 2**(256-112) * 1 - 2**(256-112-64) * 0
))
print("0b1111111111111111111111111111111111111111111111111111111110000000000000000000000000000000000000000000000000000000")
# shift it left 112 bits
# mask_add = mask_add << 224-63

# okay how this works:
# binary digit 1
# shift it left 64 bits - this creates 1 [0*64]

# print(bin(mask_add))

# convert mask_add to a full mask string over 224 bits
# print(mask_add2)
print("0b"+adds)
exit()
print(mask_sub)
print(subs)


# input = 224 bit string (len(input))
# first operation: mask + add
# second operation: mask + sub
# third operation: bias thing

# input is random 224 bits
import random
inp = "0b" + "".join(random.choice("01") for _ in range(224))

# then we do the mask + add
inp_add = inp | mask_add
# Region for subtraction (bits 56-111)
# mask_sub = ((1 << 56) - 1) << 56
# # Region for addition (bits 112-167)
# mask_add = ((1 << 56) - 1) << 112
# # Extra bit at position 180 (within bits 168-223)
# mask_extra = 1 << 180
