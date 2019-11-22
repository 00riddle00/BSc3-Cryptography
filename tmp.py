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
C = 4193112016074571244795116993161685086752808927498748311171023074570004

# Algio RSA raktai 
[n_a,e_a]=[4612815926384476787239739621668907704717767309229707570311633835476393, 420380077031]

# Algiui skirtas RSA laiškas:
Ca_rsa = 2709568874488237512534696272580903807136898252036488204682740253059538

# Algiui skirtas Rabino kriptosistema šifruotas laiškas:
Ca_rab = 3378161399036048829048731846628034672714134203763663961355279590660397

# TIKSLAS: Perskaitykite visus šifruotus laiškus

# mano tekstas
print i_teksta(power_mod(C,d,n))

t = e*d-1
while (t % 2 == 0):
    t = t/2

print gcd(2,t)


    