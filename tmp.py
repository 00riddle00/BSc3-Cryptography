def super_incr(mn, m): # Generating superincreasing weights
    w=[]
    w.append(int(random()*mn+mn))
    p=w[0]
    for i in range (0,m-1):
        v=p+int(random()*mn+mn)
        w.append(v)
        p=p+v
    return [w,p]

exmpl=super_incr(5,10)
exmpl
p=exmpl[1]+1
p
s=3777 #for example
gcd(p,s) # greatest common divisor
V=[]
for w in exmpl[0]: # create the public key
    V.append(w*s%p)

#Viešas raktas:
V = [33415, 35218, 230274, 69475, 189589, 82664, 73209, 185458]

# Pirma privataus rakto komponentė
W = [1715, 0, 0, 0, 0, 0, 0, 0]


# Modulis:
p = 267835

#šifras:
C = [408176, 603089, 796412, 593634, 713748, 230274, 408176, 796412, 606823, 533614, 593634, 230274, 490840, 450950, 593634, 450950, 408176, 450950]


w1 = W[0]
v1 = V[0]



def getT(vi, wi):
    d = gcd(vi, p)
    ti = (wi/d) / (vi/d) % (p/d)
    res = []
    if d == 1:
        print "d=1"
        return [ti]
    else:
        res.append(ti)
        for i in range(1,d):
            ti = ti + i*(p/d)
            res.append(ti)
        print "d=", d
        return res

res = getT(v1, w1)

print "res=", res

for ti in res:
    W = [elem * ti % p for elem in V]
    print "ti=", ti, "W=", W
    
W = [1715, 2048, 4204, 8375, 16744, 33539, 66999, 134078]

t = 96706
#t = 364541

CR = [0,0,0,0,0,0,0,0]

for i in range(8):
    print i
    CR[i] = t * C[i] % p
    
print "CR=", CR

W1 = [0,0,0,0,0,0,0,0]

CR1 = CR[0]

#def get_WI():
#    for i in range(
#    tmp = CR1 - W[7]
#    if tmp >= 0:
#        CR1 = tmp
        
 
    
    
    
    
    
    
    
    
    
    