def iter(M,k,f):
    r=M[1]
    l=M[0]^^eval(f)
    return [r,l]

def de_feistel(M, K, f):

    res = []

    for m in M:
        for k in K[::-1]:
            m=iter(m,k,f)
        res.append(m[::-1])

    return ''.join([chr(item) for sublist in res for item in sublist])

def feistel(M, K, f):
    return de_feistel(M, K[::-1], f)

def str_to_ord(string):
    retrun [ord(string[0]), ord(sring[1])]

def xor(c1d_f, IV):
    m1_0 = IV[0] ^^ ord(c1d_f[0])
    m1_1 = IV[1] ^^ ord(c1d_f[1])
    return [m1_0, m1_1]

def xor2(c1, IV):
    m1_0 = IV[0] ^^ c1[0]
    m1_1 = IV[1] ^^ c1[1]
    return [m1_0, m1_1]

# UZD3
C2 = [[87, 65], [78, 19], [24, 94], [22, 26], [81, 68], [88, 29], [16, 76], [24, 20], [78, 76], [81, 24], [24, 87], [27, 11], [83, 73], [81, 24], [5, 79], [19, 18], [72, 80], [70, 18], [12, 88], [27, 16], [76, 92], [76, 12], [1, 95], [15, 5], [71, 88], [84, 8], [21, 84], [14, 16], [91, 82], [94, 31], [27, 64], [21, 25], [95, 83], [74, 26], [10, 79], [15, 30], [83, 87], [77, 20], [12, 75], [11, 0], [64, 64], [66, 12], [4, 82], [10, 17], [65, 91], [84, 31], [28, 80], [18, 0], [92, 83], [72, 10], [10, 93], [18, 30], [77, 76], [80, 7], [20, 66], [26, 7], [77, 84], [65, 23], [29, 83], [9, 1], [73, 69], [92, 28], [26, 71], [31, 14]]
IV2 = [7, 14]
K2 = [215, 224, 185]
f2 = '(r^k)&((k//16)|r)'



M = [[]]

for i in range(len(C2)):
    ci = C2[i]
    IV2s = str_to_ord(feistel([IV2], K2, f2))
    #cid = de_feistel([ci], K2, f2)
    mi = xor2(ci, IV2s)
    IV2 = ci
    M.append(mi)
    
print ''.join([chr(item) for sublist in M for item in sublist])

   



    