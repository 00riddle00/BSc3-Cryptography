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

#stream cipher
def str_cipher(t,c,xp): # t - plaintext (ASCII decimal list), c-coefficients, xp - initial state
    cp=[]
    k=len(t)
    sr=stream(c,xp,8*k)
    for i in range (0,k):
        cp.append(t[i]^^int(sr[8*i:8*i+8],2))
    return cp
# How to use
c=[1,0,1,0,1,1,0,1]
t=[10,123]
xp=[1,0,1,0,1,1,0,1]
cp=str_cipher(t,c,xp)
print cp
print str_cipher(cp,c,xp)

# PAGALBA
# Skaičiaus vertimas bitų eilute
getBin = lambda x, n: x >= 0 and str(bin(x))[2:].zfill(n) or "-" + str(bin(x))[3:].zfill(n)
getBin(1,8)

# Chi-kvadrat su m laisvės laipsnių p- reikšmė
m=1
T = RealDistribution('chisquared', m)
t=2.5
p=1-T.cum_distribution_function(t)

# Standartinio normaliojo dėsnio p reikšmė
N= RealDistribution('gaussian', 1)
t=2.5
p=1-N.cum_distribution_function(t)
p