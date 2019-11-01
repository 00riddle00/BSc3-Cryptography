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

title = '''
# UZD3.1
'''

print title

# zodis: 'uogapiktas'
M1 = 'uo'
M2 = 'ga'
M3 = 'pi'
M4 = 'kt'
M5 = 'as'

N1 = 'to'
N2 = 'mg'
N3 = 'ie'

h0 = 'uo' # init vektorius
r='pi' # kriptosistemos raktas

h_M1M2 = decod(hfOFB(h0, r, M1+M2))

Y = int(h_M1M2,2)

N = 'ab' # any
print "N=", N
h_N1N2N = decod(hfOFB(h0, r, N1+N2+N))
h_star = h_N1N2N

N_bin = getBin2(N)

Z = int(h_star,2) ^^ int(N_bin,2)

X = Z ^^ Y

X = getBin(X, 16)

x1 = chr(int(X[0:8],2))
x2 = chr(int(X[8:16],2))

print "x1=", x1
print "x2=", x2
print "ord(x1)=", ord(x1)
print "ord(x2)=", ord(x2)

h_M = hfOFB(h0, r, M1+M2+M3+M4+M5)
h_M_1 = hfOFB(h0, r, N1+N2 + x1 + x2 + M3+M4+M5)

print "h_M=", h_M
print "h_M_1=", h_M_1

title = '''
# UZD3.2
'''

print title

# zodis: 'uoga'
M1 = 'uo'
M2 = 'ga'

h_M1M2 = decod(hfOFB(h0, r, M1+M2))
Y = int(h_M1M2,2)

M = 'ab' # any
h_M1M2M = decod(hfOFB(h0, r, M1+M2+M))

M_bin = getBin2(M)

Z = int(h_M1M2M,2) ^^ int(M_bin,2)

U = Z ^^ Y

U = getBin(U, 16)

u1 = chr(int(U[0:8],2))
u2 = chr(int(U[8:16],2))

U = u1 + u2

print "u1=", u1
print "u2=", u2
print "ord(u1)=", ord(u1)
print "ord(u2)=", ord(u2)

h_M1M2 = hfOFB(h0, r, M1+M2)
h_M1M2U = hfOFB(h0, r, M1+M2+U)
h_M1M2UU = hfOFB(h0, r, M1+M2+U+U)
h_M1M2UUU = hfOFB(h0, r, M1+M2+U+U+U)

print "h_M1M2=", h_M1M2
print "h_M1M2U=", h_M1M2U
print "h_M1M2UU=", h_M1M2UU
print "h_M1M2UUU=", h_M1M2UUU