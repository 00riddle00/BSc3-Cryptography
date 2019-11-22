# Tekstams versti skaičiais (ir atvirkščiai)
A='abcdefghijklmnopqrstuvwxyz'
def i_skaiciu(text):
    t=''
    for r in text:
        if r in A:
            ind=A.index(r)+1
            if ind<10: t=t+'0'+str(ind)
            else: t=t+str(ind)
    return int(t,10)  

def i_teksta(M):
    n=M
    text=''
    while n>0:
        ind=n%100
        ind=ind-1
        if (ind>=0) & (ind<len(A)):
            text+=A[ind]
            n=(n-ind+1)//100
        else:
            text+='?'
            n=(n-ind+1)//100            
    return text[::-1]     
    
#M=i_skaiciu('vienas')
#T=i_teksta(M)
#M,T

# Jūsų RSA raktai
[n,e,d]= [4612815926384476787239739621668907704717767309229707570311633835476393, 916304813609, 429357073462636237660670034578942775191310478273876821838370595349505]

# Jums skirtas RSA laiškas
C_rsa = 4193112016074571244795116993161685086752808927498748311171023074570004

# Algio RSA raktai 
[n_a,e_a]=[4612815926384476787239739621668907704717767309229707570311633835476393, 420380077031]

# n_a sutampa su n

# Algiui skirtas RSA laiškas:
Ca_rsa = 2709568874488237512534696272580903807136898252036488204682740253059538

# Algiui skirtas Rabino kriptosistema šifruotas laiškas:
Ca_rab = 3378161399036048829048731846628034672714134203763663961355279590660397

# TIKSLAS: Perskaitykite visus šifruotus laiškus

# mano tekstas su RSA
T_1 = i_teksta(power_mod(C_rsa,d,n))
print T_1

t = e*d-1
while (t % 2 == 0):
    t = t//2 # du //, nes reikia ne tipo "Rational", o tipo "Integer"

print gcd(2,t)

for a in range(1,11):
    print "a=", a
    if (gcd(a,n) == 1):
        a0 = power_mod(a,t,n)
        ai, ai_prev = a0,a0
        while (ai != 1):
            ai_prev = ai
            ai = power_mod(ai, 2, n)
        p = gcd(ai_prev-1, n)
        print ("p=",p)
        if (p < n) and (p != 1):
            break
            
q = n//p

phi_n = (p-1)*(q-1)

d_a = (1/e_a) % phi_n
print d_a

# Algio tekstas su RSA
T_2 = i_teksta(power_mod(Ca_rsa,d_a,n))
print T_2

# Mano kriptosistema
p_mine = random_prime(2^128-1,False,2^127)
q_mine = random_prime(2^128-1,False,2^127)

print "p_mine=", p_mine
print "q_mine=", q_mine

n_mine = p_mine * q_mine
print "n_mine=", n_mine

d_mine = random_prime(2^128-1,False,2^127)
print "d_mine=", d_mine

phi_n_mine = (p_mine-1)*(q_mine-1)

e_mine = (1/d_mine) % phi_n_mine
print "e_mine", e_mine

# T_2 sifravimas su savo RSA (savo paraso sukurimas)
C_2_mine = power_mod(i_skaiciu(T_2),e_mine,n_mine)
print C_2_mine
# C_2 desifravimas su savo RSA (savo paraso tikrinimas)
T_2_mine = i_teksta(power_mod(C_2_mine,d_mine,n_mine))
print T_2_mine



     
    