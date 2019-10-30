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

# custom fja dvi raides paversti i binary
def getBin2(pair):
    return getBin(ord(pair[0]), 8) + getBin(ord(pair[1]), 8)

# UZD1
# zodis: 'uogapiktas'
M1 = 'uo'
M2 = 'ga'
M3 = 'pi'
M4 = 'kt'
M5 = 'as'

h0 = 'uo' # init vektorius
r='pi' # kriptosistemos raktas
s=M1 # s yra pranesimas, kuri norime xorinti. Blokas is 2ju skaiciu arba 2 raidziu, ex. blokas 'ss' (2 baitai)
h=hfCBC(h0,r,M1)
#print h, decod(h) # h yra hashas, atitinka 2 bytes
#print decod(h) # decod(h) gauname h bitukais (16bits)
# decod - destytojo israiska decode, 16 raidziu abecele, 1 raide - 4 bitais

h_M1 = decod(h)
M2_bin = getBin2(M2)

print "h_M1=", h_M1
print "M2_bin=", M2_bin

y = int(h_M1,2) ^^ int(M2_bin,2) # y = h_M1 ^^ M2
print "y=", y

N1 = 'to'
N2 = 'mg'
N3 = 'ie'

h=hfCBC(h0,r,N1+N2) # veiktu ir su N1+N2+N3
#print h, decod(h)

h_N1N2 = decod(h)
h_N1N2_int = int(h_N1N2,2)

print "h_N1N2_int=", h_N1N2_int

X = y ^^ h_N1N2_int

X = bin(X)
print "X=", X

X = X[2:]
print "X=", X

x1 = chr(int(X[0:8],2))
x2 = chr(int(X[8:16],2))

print "x1=", x1
print "x2=", x2
print "ord(x1)=", ord(x1) # surandame google kas per ASCII simbolis tai yra
print "ord(x2)=", ord(x2) # surandame google kas per ASCII simbolis tai yra

h_M = hfCBC(h0, r, M1+M2+M3+M4+M5)
h_M1 = hfCBC(h0, r, N1+N2 + x1 + x2 + M3+M4+M5) # veiktu ir su N1+N2+N3

print "h_M=", h_M
print "h_M1=", h_M1

assert(h_M == h_M1)