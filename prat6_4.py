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
    return [ord(string[0]), ord(string[1])]

def xor(c1d_f, IV):
    m1_0 = IV[0] ^^ ord(c1d_f[0])
    m1_1 = IV[1] ^^ ord(c1d_f[1])
    return [m1_0, m1_1]

def xor2(c1, IV):
    m1_0 = IV[0] ^^ c1[0]
    m1_1 = IV[1] ^^ c1[1]
    return [m1_0, m1_1]

# UZD4
C2 = [[69, 83], [70, 68], [64, 73], [76, 84], [94, 77], [76, 75], [73, 86], [64, 64], [80, 65], [72, 72], [87, 94], [92, 66], [83, 88], [64, 88], [75, 95], [85, 84], [66, 84], [76, 82], [77, 73], [68, 82], [91, 77], [95, 92], [70, 77], [70, 79], [75, 65], [87, 89], [69, 91], [76, 77], [65, 94], [68, 74], [82, 77], [91, 68], [77, 117], [94, 104], [77, 115], [89, 96], [67, 101], [90, 108], [67, 109], [89, 100], [80, 108], [64, 107], [65, 123], [80, 9]]
#IV2 = [7, 14]
K2 = [215, 224, 185]
f2 = '(r^k)&((k//16)|r)'
f3 = '(m^k)&((k//16)|m)'

def sk_fja(m,k):
    T = eval(f3)
    return [T,T]

M_res = [[]]

for i in range(len(C2)):
    ci = C2[i]
    Ti = sk_fja(i,K2[0])
    Tis = str_to_ord(feistel([Ti], K2, f2))
    mi = xor2(ci, Tis)
    M_res.append(mi)
    
print ''.join([chr(item) for sublist in M_res for item in sublist])



    