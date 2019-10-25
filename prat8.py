# The system of linear feedback registers

def stream(c,xp,n):  # the keystream generation, c-coefficients, xp - initial state, n - number of bits
    x=[0,0,0,0,0,0,0,0]
    for i in range(0,8):
        x[i]=xp[i]
    sr=''
    for i in range(0,n):
        bt=0
        sr+=str(x[0])
        for j in range(0,8):
            bt+=c[j]*x[j]
        for j in range(1,8):
            x[8-j]=x[7-j]
        x[0]=bt%2
    return sr

# stream cipher
# t = baitu masyvas, kuri reikia issifruoti/desifruoti
# c = konstantos, paduodamos tokia tvarka: [c8,c7,...,c1]
# xp = pradines reg sistemos padetys
def str_cipher(t,c,xp): # t - plaintext (ASCII decimal list), c-coefficients, xp - initial state
    cp=[]
    k=len(t)
    sr=stream(c,xp,8*k)
    for i in range (0,k):
        cp.append(t[i]^^int(sr[8*i:8*i+8],2))
    return cp
# How to use
# t=[10,123]
# c=[1,0,1,0,1,1,0,1]
# xp=[1,0,1,0,1,1,0,1]
# cp=str_cipher(t,c,xp)
# print cp
# print str_cipher(cp,c,xp)

# UZD1
x1 = 'K'
x2 = 'A'
Y = [113, 24, 4, 172, 151, 123, 46, 45, 220, 204, 217, 213, 240, 234, 153, 185, 52, 70, 227, 127, 187, 6, 67, 191, 77, 83, 64, 125, 75, 62, 100, 197, 50, 251, 205, 128, 252, 21, 166, 167, 84, 64, 102, 127, 38, 17, 244, 179, 133, 104, 6, 48, 183, 246, 80, 163, 93, 96, 71, 15, 98, 171, 16, 127, 187, 48, 126, 219, 10, 238, 173, 171, 105, 106, 15, 40, 147, 246, 51, 155, 209, 23, 239, 142, 183, 7, 81, 129, 82, 33]
#Y = [86, 1, 168, 188, 56, 70, 195, 235, 157, 91, 81, 148, 21, 113, 41, 71, 15, 173, 169, 38, 70, 215, 240, 129, 69, 77, 147, 21, 116, 50, 92, 9, 178, 160, 52, 83, 212, 229, 145, 93, 87, 137, 17, 106, 63, 88, 22, 160, 165, 62, 86, 212, 225, 145, 92, 91, 141, 31, 107, 58, 75, 15, 166, 165, 48, 80, 202, 244, 152, 75, 77, 128, 25, 125, 63, 82, 10, 174, 175, 60, 86, 203, 243, 145, 68, 81]

c1 = 1

K_1_8 = ord(x1)^^Y[0]
K_9_16 = ord(x2)^^Y[1]

K_1_8 = list(format(K_1_8, '#010b')[2:])
K_9_16 = list(format(K_9_16, '#010b')[2:])

K_1_16 = K_1_8 + K_9_16

# spausdina matrica
#for i in range(8):
#    for j in range(8):
#        print(K_1_16[j+i]),
#    print('| '),
#    print(K_1_16[j+i+1])

# gautos konstantos issprendus binary
# lygciu sistema su xor vietoj sudeties
C_1_8 = [1,1,1,1,0,1,1,0]
K_1_8 =  [0, 1, 1, 0, 1, 0, 0, 1]


#t = Y[1:]
t = Y

C_1_8 = [0, 1, 1, 0, 1, 0, 0, 1]
c=C_1_8
#c=C_1_8[::-1]

#xp=(K_1_16[1:9])[::-1]
xp = K_1_8

t = map(int, t)
c = map(int, c)
xp = map(int, xp)


cp=str_cipher(t,c,xp)
print cp
res = map(lambda x : chr(x), cp)
#res.insert(0, x1)
print ''.join(res)

m_bytes = cp
c_bytes = Y


# PAGALBA
# Skaičiaus vertimas bitų eilute
getBin = lambda x, n: x >= 0 and str(bin(x))[2:].zfill(n) or "-" + str(bin(x))[3:].zfill(n)
getBin(1,8)

m_bits_tmp = map(lambda x : getBin(x,8), m_bytes)
c_bits_tmp = map(lambda x : getBin(x,8), c_bytes)

m_bits = b''
for bit8 in m_bits_tmp:
    m_bits += bit8

c_bits = b''
for bit8 in c_bits_tmp:
    c_bits += bit8

print m_bits
print c_bits

m0 = sum(map(lambda x : 1 if '0' in x else 0, m_bits)) 
m1 = sum(map(lambda x : 1 if '1' in x else 0, m_bits)) 
print m0
print m1

c0 = sum(map(lambda x : 1 if '0' in x else 0, c_bits)) 
c1 = sum(map(lambda x : 1 if '1' in x else 0, c_bits))
print c0
print c1

tm1 = ((m1-m0)**2)/len(m_bits)
print "tm1 ", tm1

tc1 = ((c1-c0)**2)/len(c_bits)
print "tc1 ", tc1

# Chi-kvadrat su m laisvės laipsnių p- reikšmė
m=1
T = RealDistribution('chisquared', m)
#t=2.5
pm1=1-T.cum_distribution_function(tm1)
print "pm1 ", pm1

# Chi-kvadrat su m laisvės laipsnių p- reikšmė
m=1
T = RealDistribution('chisquared', m)
#t=2.5
pc1=1-T.cum_distribution_function(tc1)
print "pc1 ", pc1

m_pairs = {
    '00':0,
    '01':0,
    '10':0,
    '11':0,
}

c_pairs = {
    '00':0,
    '01':0,
    '10':0,
    '11':0,
}

#m_bits = b'010100'
#print m_bits[0:2]
#i = 0
#m_pairs[m_bits[0:2]] += 1
#m_pairs[m_bits[i:i+2]] += 1

for i in range(len(m_bits)-1):
    m_pairs[m_bits[i:i+2]] += 1
    
for i in range(len(c_bits)-1):
    c_pairs[c_bits[i:i+2]] += 1

print m_pairs
print c_pairs

# calc t2
n = len(m_bits)
tm2 = (4/(n-1)) * ( m_pairs['00']**2 + m_pairs['01']**2 + m_pairs['10']**2 + m_pairs['11']**2 ) - (2/n) * ( m0 ** 2 + m1 ** 2) + 1
print "tm2 ", tm2

n = len(c_bits)
tc2 = (4/(n-1)) * ( c_pairs['00']**2 + c_pairs['01']**2 + c_pairs['10']**2 + c_pairs['11']**2 ) - (2/n) * ( c0 ** 2 + c1 ** 2) + 1
print "tc2 ", tc2

# Chi-kvadrat su m laisvės laipsnių p- reikšmė
m=2
T = RealDistribution('chisquared', m)
#t=2.5
pm2=1-T.cum_distribution_function(tm2)
print "pm2 ", pm2

# Chi-kvadrat su m laisvės laipsnių p- reikšmė
m=2
T = RealDistribution('chisquared', m)
#t=2.5
pc2=1-T.cum_distribution_function(tc2)
print "pc2 ", pc2





d = 3
shift = d-1

# TEKSTAS
n = len(m_bits)
m_bits_1 = m_bits[:n-shift]
m_bits_2 = m_bits[shift:]

n_tmp = n - shift

X_d = 0

for i in range(n_tmp-1):
    if m_bits_1[i] != m_bits_2[i]:
        X_d += 1
        
        
tm3 = (2 * X_d - (n - d)) / (sqrt(n - d))
print "tm3 ", tm3


# Standartinio normaliojo dėsnio p reikšmė
N= RealDistribution('gaussian', 1)
#t=2.5
# t3 < 0 (del to be minuso!!)
#pm3=1-N.cum_distribution_function(tc3)
pm3=N.cum_distribution_function(tm3)
print "pm3 ", pm3


# SIFRAS
n = len(c_bits)
c_bits_1 = c_bits[:n-shift]
c_bits_2 = c_bits[shift:]

n_tmp = n - shift

X_d = 0

for i in range(n_tmp-1):
    if c_bits_1[i] != c_bits_2[i]:
        X_d += 1
        
        
tc3 = (2 * X_d - (n - d)) / (sqrt(n - d))
print "tc3 ", tc3


# Standartinio normaliojo dėsnio p reikšmė
N= RealDistribution('gaussian', 1)
#t=2.5
# t3 < 0 (del to be minuso!!)
#pc3=1-N.cum_distribution_function(tc3)
pc3=N.cum_distribution_function(tc3)
print "pc3 ", pc3

   
        
        
        
        
        
        
        
        


