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


p=next_prime(12^18)
g=primitive_root(p)

a=199111
bt=power_mod(g,a,p)
K_pr=a
K_v=[p,g,bt]

# K_pr, K_v

M=10000000000001
k=12345
C_1=power_mod(g,k,p)
C_2=M*power_mod(bt,k,p)%p
C=[C_1,C_2]
#C
M=C_2/power_mod(C_1,a,p)%p
M