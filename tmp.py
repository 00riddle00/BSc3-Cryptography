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


#Vieši Algio ElGamalio  schemos raktai
[p,alpha,beta]=[12016012609141909200527091927191118250205121973, 1340, 567229645341541746447797908693212382352016288]

#Algio parašai
# tekstas_1
t1="naujienos"
x1=140121100905141519
# Parašas
[gama1,delta1] = [5570393885818468990720736511935245441421473683, 11318193604278953165137689101864251625102398263]

#tekstas_2
t2 = "lektuvas veluos"
x2=120511202122011927220512211519
# Parašas
[gama2,delta2] = [5570393885818468990720736511935245441421473683, 6600840420895214539082508270820765392182440243]

# Šifruotas laiškas Algiui 
[C_1,C_2]= [5353434162946175342506864580712183347054386024, 3415125406315829810122511480055610251790431991]

#gama1=gama2
gama = gama1

#tikriname parasus
#parasas1
print(power_mod(beta,gama,p)*power_mod(gama,delta1,p)%p == power_mod(alpha,x1,p))
#parasas2
print(power_mod(beta,gama,p)*power_mod(gama,delta2,p)%p == power_mod(alpha,x2,p) %p)

d=gcd(delta1-delta2,p-1)

def get_ki(d):
    
    k0 = (x1-x2)/(delta1-delta2) % ((p-1)/d)
    ki = k0

    if d == 1:
          return k0
    
    while power_mod(alpha,ki,p)%p != gama:
        ki = k0 + (p-1)//d
    
    return ki

def get_ai(d):
    
    a0 = (x1-delta1*k)/gama % ((p-1)/d)
    ai = a0

    if d == 1:
          return a0
    
    while power_mod(alpha,ai,p)%p != beta:
        ai = a0 + (p-1)//d
    
    return ai

k = get_ki(d)
print 'k=', k
print 'ar k geras?', power_mod(alpha,k,p)%p == gama

d = gcd(gama,p-1)

a = get_ai(d)
print 'a=', a
print 'ar a geras?', power_mod(alpha,a,p)%p == beta


# Desifravimas
M=C_2/power_mod(C_1,a,p)%p
print "M=", i_teksta(M)

# DSS sudarymas
print("DSS sudarymas")
g=primitive_root(p) 
# atkomentuoti
#print factor(p-1) # pasirenkame kuo didesni 'q', bet darom tradeoff tarp paraso trumpumo ir saugumo
q = 669824108147 # toki pasirinkau
K_p=a # is Algio
alpha=power_mod(alpha,(p-1//q),p)
beta=power_mod(alpha,a,p)
K_p=a
K_v=[p,g,alpha,beta]
print "Viesas raktas=", K_v

k=1234567
print 'gerai parinktas k? ', gcd(k,p-1) == 1

gama=