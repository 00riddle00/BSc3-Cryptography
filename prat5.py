
def iter(M,k,f):
    r=M[1]
    l=M[0]^^eval(f)
    return [r,l]

f_ex='(r*k+r)%256'
f1 = '(r|k)^((k//16)&r)'
f2 = '(r&k)^((k%16)|r)'
f3 = f2


M1 = [[37, 17], [59, 20], [53, 11], [59, 17], [42, 23], [35, 9], [37, 12], [57, 22], [47, 9], [51, 26], [59, 2], [59, 20], [61, 17], [47, 17], [38, 21], [47, 15], [61, 17], [60, 22], [42, 23], [47, 19], [43, 31], [37, 12], [57, 22], [53, 13], [59, 20], [37, 17], [47, 19], [53, 25], [37, 17], [33, 16], [47, 19], [60, 3], [35, 21], [33, 13], [38, 21], [40, 11], [42, 17], [51, 9], [47, 27], [42, 13], [47, 9], [45, 25], [33, 29], [53, 24], [39, 23], [38, 15], [62, 15], [39, 19], [52, 12], [43, 19], [61, 17], [41, 30], [47, 19], [52, 9], [53, 28], [52, 13], [78, 91]]
K1 = [91,89,53]

res = []

for M in M1:
    x = M
    exit(1)
    for k in K1[::-1]:
        x=iter(x,k,f1)
    res.append(x[::-1])

for x in res:
    print chr(x[0]),
    print chr(x[1]),



