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


d = gcd(v1, p)

print 'dbd', dbd
ti = (w1/d) / (v1/d) % (p/d)

res = []

if d == 1:
    print "d=1"
    print "ti=", ti
else:
    for i in range(1,d):
        ti = ti + i*(p/d)
        res.append(ti)
    print "d=", d
    print "ti_LIST=", res

