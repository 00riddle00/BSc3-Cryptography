def to_text(M):
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

A='abcdefghijklmnopqrstuvwxyz0123456789.=\n'
N=len(A)
def vigen(key,text):
    keyn=''
    for r in key:
        if r in A: keyn+=r
    textn=''
    for r in text:
        if r in A: textn+=r
    rakt=[A.index(r) for r in keyn]  
    d=len(rakt)
    ciph=''
    for r in range(0,len(textn)):
        ciph+=A[(A.index(textn[r])+rakt[r%d])%N]
    return ciph    
  
vigen('raktas','tekstas') 

#ElGamalio kriptosistema grupei
#Viešas raktas
[p,q,g,y]= [20231527231815140719270415142027130111052701271809070899, 58271408650148251087586012071, 4528647203244485661481740338407226739486206949292857701, 6176642083154182479341784815974008469233494177711848747]

#Jūsų rakto dalis
[x_i,y_i]=[4767448543, 1669401542459254327092595963]
#Slenkstis
t=5
#Šifras
C=[7333109914047830423403358580366739968864018572071237174, 12064032717206770507949740475689958147166901266014058908]
#Balų failo rakto šifras
Cr=[8546284775834385955786936313017527364304510802731847173, 6854974634499061100353407038611108234835399974938772026]