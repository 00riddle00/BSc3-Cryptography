
def iter(M,k,f):
    r=M[1]
    l=M[0]^^eval(f)
    return [r,l]


# UZD1
M1 = [[37, 17], [59, 20], [53, 11], [59, 17], [42, 23], [35, 9], [37, 12], [57, 22], [47, 9], [51, 26], [59, 2], [59, 20], [61, 17], [47, 17], [38, 21], [47, 15], [61, 17], [60, 22], [42, 23], [47, 19], [43, 31], [37, 12], [57, 22], [53, 13], [59, 20], [37, 17], [47, 19], [53, 25], [37, 17], [33, 16], [47, 19], [60, 3], [35, 21], [33, 13], [38, 21], [40, 11], [42, 17], [51, 9], [47, 27], [42, 13], [47, 9], [45, 25], [33, 29], [53, 24], [39, 23], [38, 15], [62, 15], [39, 19], [52, 12], [43, 19], [61, 17], [41, 30], [47, 19], [52, 9], [53, 28], [52, 13], [78, 91]]
K1 = [91,89,53]
f1 = '(r|k)^((k//16)&r)'

res1 = []

for M in M1:
    x = M
    for k in K1[::-1]:
        x=iter(x,k,f1)
    res1.append(x[::-1])

for x in res1:
    print chr(x[0]),
    print chr(x[1]),

print('\n')

# UZD2
M2 = [[90, 21], [79, 10], [85, 4], [83, 4], [83, 4], [75, 12], [76, 11], [65, 8], [89, 17], [69, 17], [73, 24], [75, 8], [77, 14], [84, 19], [73, 24], [86, 29], [82, 27], [83, 18], [73, 10], [73, 10], [82, 18], [65, 23], [73, 0], [84, 23], [73, 0], [65, 16], [66, 21], [86, 27], [78, 9], [71, 0], [82, 31], [78, 9], [83, 28], [65, 25], [73, 10], [85, 4], [73, 10], [83, 26], [82, 25], [83, 29], [69, 11], [73, 24], [84, 3], [82, 21], [74, 7], [86, 29], [83, 30], [86, 17], [73, 15], [82, 31], [68, 28], [73, 4], [89, 11], [65, 23], [89, 25], [69, 20]]
K2 = [0, 162] # 0 - nezinom
f2 = '(r&k)^((k%16)|r)'


for k2_1 in range(256):
    if k2_1 != 2:
        continue
    res2 = []
    print("raktas=",k2_1)
    K2[0] = k2_1
    for M in M2:
        x = M
        for k in K2[::-1]:
            x=iter(x,k,f2)
        res2.append(x[::-1])

    for x in res2:
        print chr(x[0]),
        print chr(x[1]),
    print('\n')



# UZD3


M3 = [[78, 31], [75, 26], [82, 3], [70, 7], [71, 2], [71, 4], [65, 7], [65, 8], [65, 3], [81, 26], [92, 1], [74, 23], [66, 5], [75, 18], [78, 25], [69, 2], [83, 18], [67, 7], [89, 23], [81, 26], [93, 7], [72, 17], [75, 18], [67, 4], [66, 5], [89, 17], [65, 12], [76, 21], [78, 19], [65, 13], [74, 29], [76, 13], [67, 10], [81, 25], [89, 17], [65, 12], [67, 4], [67, 2], [91, 7], [77, 7], [77, 30], [68, 13], [92, 2], [81, 27], [76, 29], [70, 10], [73, 12], [65, 2], [73, 5], [76, 29], [67, 15], [73, 3], [89, 19], [89, 21], [77, 15], [93, 22], [69, 8], [76, 21], [75, 30], [89, 21], [81, 13], [81, 19], [69, 2], [95, 18], [81, 27], [70, 11], [92, 2], [81, 26], [89, 17], [89, 18], [89, 20], [68, 5], [76, 27], [67, 2], [67, 4], [83, 24], [81, 26], [76, 29], [83, 25], [77, 31], [93, 12], [74, 19]]
K3 = [0,0] # abieju nezinome
f3 = '(r&k)^((k%16)|r)'

br = False

for k1 in range(256):
    if br == True:
        break
    for k2 in range(256):
        K3 = [k1,k2]
        x = M3[0]
        for k in K3[::-1]:
            x=iter(x,k,f3)
        if x[0] == ord('I') and x[1] == ord('V'):
            print('raktai=',K3)
            br = True
            break
            
            
K3 = [0,24]


res3 = []

for M in M3:
    x = M
    for k in K3[::-1]:
        x=iter(x,k,f3)
    res3.append(x[::-1])

for x in res3:
    print chr(x[0]),
    print chr(x[1]),
print('\n')