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
Y = [113, 24, 4, 172, 151, 123, 46, 45, 220, 204, 217, 213, 240, 234, 153, 185, 52, 70, 227, 127, 187, 6, 67, 191, 77, 83, 64, 125, 75, 62, 100, 197, 50, 251, 205, 128, 252, 21, 166, 167, 84, 64, 102, 127, 38, 17, 244, 179, 133, 104, 6, 48, 183, 246, 80, 163, 93, 96, 71, 15, 98, 171, 16, 127, 187, 48, 126, 219, 10, 238, 173, 171, 105, 106, 15, 40, 147, 246, 51, 155, 209, 23, 239, 142, 183, 7, 81, 129, 82, 33]

# gautos konstantos issprendus binary
# lygciu sistema su xor vietoj sudeties

#Koeficientų vektorius
C_1_8 = [0, 1, 1, 0, 1, 0, 0, 1]
# Pradinės padėties vektorius 
K_1_8 =  [0, 1, 1, 0, 1, 0, 0, 1]

t = Y
c=C_1_8
xp = K_1_8

cp=str_cipher(t,c,xp)

# print deciphered text
res = map(lambda x : chr(x), cp)
print ''.join(res)

# teksto baitai
m_bytes = cp
# sifro baitai
c_bytes = Y

# Skaičiaus vertimas bitų eilute
getBin = lambda x, n: x >= 0 and str(bin(x))[2:].zfill(n) or "-" + str(bin(x))[3:].zfill(n)
# pvz.
# getBin(X,8), X - teksto baitas

m_bits_tmp = map(lambda x : getBin(x,8), m_bytes)
c_bits_tmp = map(lambda x : getBin(x,8), c_bytes)

m_bits = b''
for bit8 in m_bits_tmp:
    m_bits += bit8

c_bits = b''
for bit8 in c_bits_tmp:
    c_bits += bit8

#print 'm_bits', m_bits
#print 'c_bits', c_bits

lg = len(m_bits)

title = '''
###############################
# Pavieniu bitu testas
###############################
'''

print title

m0 = sum(map(lambda x : 1 if '0' in x else 0, m_bits)) 
m1 = lg - m0
#print 'm0', m0
#print 'm1', m1

c0 = sum(map(lambda x : 1 if '0' in x else 0, c_bits)) 
c1 = lg - c0
#print 'c0', c0
#print 'c1', c1

tm1 = ((m1-m0)**2)/lg
print "tm1 ", float(tm1)

tc1 = ((c1-c0)**2)/lg
print "tc1 ", float(tc1)

# Chi-kvadrat su m laisvės laipsnių p- reikšmė
m=1
T = RealDistribution('chisquared', m)
pm1=1-T.cum_distribution_function(tm1)
print "pm1 ", float(pm1)

# Chi-kvadrat su m laisvės laipsnių p- reikšmė
m=1
T = RealDistribution('chisquared', m)
pc1=1-T.cum_distribution_function(tc1)
print "pc1 ", float(pc1)

title = '''
###############################
# Bitu poru testas
###############################
'''

print title

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

for i in range(lg-1):
    m_pairs[m_bits[i:i+2]] += 1
    
for i in range(lg-1):
    c_pairs[c_bits[i:i+2]] += 1

#print 'm_pairs', m_pairs
#print 'c_pairs', c_pairs

# calc 
n = lg
tm2 = (4/(n-1)) * ( m_pairs['00']**2 + m_pairs['01']**2 + m_pairs['10']**2 + m_pairs['11']**2 ) - (2/n) * ( m0 ** 2 + m1 ** 2) + 1
print "tm2 ", float(tm2)

n = lg
tc2 = (4/(n-1)) * ( c_pairs['00']**2 + c_pairs['01']**2 + c_pairs['10']**2 + c_pairs['11']**2 ) - (2/n) * ( c0 ** 2 + c1 ** 2) + 1
print "tc2 ", float(tc2)

# Chi-kvadrat su m laisvės laipsnių p- reikšmė
m=2
T = RealDistribution('chisquared', m)
pm2=1-T.cum_distribution_function(tm2)
print "pm2 ", float(pm2)

# Chi-kvadrat su m laisvės laipsnių p- reikšmė
m=2
T = RealDistribution('chisquared', m)
pc2=1-T.cum_distribution_function(tc2)
print "pc2 ", float(pc2)

title = '''
###############################
# Autokoreliacijos testas
###############################
'''

print title

d = 3

print 'd =', d, '\n'

shift = d-1

# TEKSTAS
n = lg
m_bits_1 = m_bits[:n-shift]
m_bits_2 = m_bits[shift:]

n_tmp = n - shift

X_d = 0

for i in range(n_tmp-1):
    if m_bits_1[i] != m_bits_2[i]:
        X_d += 1
        
tm3 = (2 * X_d - (n - d)) / (sqrt(n - d))
print "tm3 ", float(tm3)

# Standartinio normaliojo dėsnio p reikšmė
N= RealDistribution('gaussian', 1)
# tm3 < 0 (del to neatimame is 1-eto)
#pm3=1-N.cum_distribution_function(tc3)
pm3=N.cum_distribution_function(tm3)
print "pm3 ", float(pm3)

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
print "tc3 ", float(tc3)

# Standartinio normaliojo dėsnio p reikšmė
N= RealDistribution('gaussian', 1)
# tc3 < 0 (del to neatimame is 1-eto)
#pc3=1-N.cum_distribution_function(tc3)
pc3=N.cum_distribution_function(tc3)
print "pc3 ", float(pc3)
