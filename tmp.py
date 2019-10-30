getBin = lambda x, n: x >= 0 and str(bin(x))[2:].zfill(n) or "-" + str(bin(x))[3:].zfill(n)
abc_h='ABCDEFGHIJKLMNOP' # h-funcijos reikšmių abėcėlė
def e(m,k): #Kriptosistema
    f=lambda u,v,w:u^^((v*v+77*w)%256)
    c=[m[1],f(m[0],m[1],k[0])]
    return [c[1],f(c[0],c[1],k[1])]

def code(m): 
    e=getBin(m[0],8)+getBin(m[1],8)
    h=''
    for i in range(0,4):
        h+=abc_h[int(e[4*i:4*i+4],2)]
    return h

def decod(s): #h-funkcijos reikšmė į bitus
    bt=lambda r: bin(16^^r)[3:]
    b=''
    for c in s:
        if c in abc_h:
            b+=bt(abc_h.index(c))
    return b


# maisos fjos skaiciavimo script pgl cbc rezima
def hfCBC(h0,r,s): # h-funkcija CBC rezimas
    h=[ord(h0[0]),ord(h0[1])]
    k=[ord(r[0]),ord(r[1])]
    l=len(s)
    if l%2==1:
         s=s+s[0]
         l+=1
    for i in range(0,l//2):
        m=[ord(s[2*i])^^h[0],ord(s[2*i+1])^^h[1]]
        h=e(m,k)
    return code(h)

def hfOFB(h0,r,s): # h-funkcija OFB rezimas
    h=[ord(h0[0]),ord(h0[1])]
    k=[ord(r[0]),ord(r[1])]
    l=len(s)
    if l%2==1:
         s=s+s[0]
         l+=1
    h=e(h,k)    
    for i in range(0,l//2):
        m=[ord(s[2*i])^^h[0],ord(s[2*i+1])^^h[1]]
        h=e(m,k)
    return code(m)

# blokas is 2ju skaiciu arba 2 raidziu blokas 'ss' (2 baitai)
h0='uo' # iv
r='pi' # kriptosistemos raktas
s='uogapiktas' # s yra pranesimas, kuri norime xorinti
h=hfCBC(h0,r,s)
print h, decod(h)
# h yra hashas, atitinka 2 bytes
# decod(h) gauname h bitukais (16bits)


#h=hfOFB(h0,r,s)
#print h, decod(h)

#Sudarykite II tekstą M_1= tomgieABpiktas, kad būtų h(M)=h(M_1),

S = 'uogapiktas'
M1 = 'uo'
M2 = 'ga'
M3 = 'pi'
M4 = 'kt'
M5 = 'as'

#h0='uo' # iv'
h0 = 'uo'
r='pi' # kriptosistemos raktas
s=M1 # s yra pranesimas, kuri norime xorinti
h=hfCBC(h0,r,s)
print h, decod(h)
# decod - savo israiska decode, 16 raidziu abecele, 1 raide - 4 bitais

h_M1 = decod(h)

def getBin2(pair):
    return getBin(ord(pair[0]), 8) + getBin(ord(pair[1]), 8)

print type(h_M1)
print type(getBin2(M2))

y = bin(int(h_M1,2) ^^ int(getBin2(M2),2))

N1 = 'to'
N2 = 'mg'
N3 = 'ie'

h=hfCBC(h0,r,'tomg')
print h, decod(h)

h_N1N2 = decod(h)

print type(y)
print type(h_N1N2)

X = bin(int(y,2) ^^ int(h_N1N2,2))

X = X[2:]

x_1 = chr(int(X[0:8],2))
x_2 = chr(int(X[8:16],2))

print x_1, x_2

h1 = hfCBC(h0, r, 'uogapiktas')
h2 = hfCBC(h0, r, 'tomg'+x_1 + x_2 + 'iepiktas')

print h1
print h2