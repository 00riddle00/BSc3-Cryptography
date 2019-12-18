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


#Užduotyje rasite du ElGamalio šifrus grupei su slenksčiu t=5 ir savo rakto
#dalį. Iššifruokite juos. Iššifravę antrąjį gausite raktą paskaitų klausimų
#failui iššifruoti.

#Dešifravimo rakto šifras sudarytas ElGamalio kriptosistema grupei su slenksčiu t=5
    
#ElGamalio kriptosistema grupei
#Viešas raktas
[p,q,g,y]= [20231527231815140719270415142027130111052701271809070899, 58271408650148251087586012071, 4528647203244485661481740338407226739486206949292857701, 6176642083154182479341784815974008469233494177711848747]

#Jūsų rakto dalis
[x_1,y_1]=[4767448543, 1669401542459254327092595963]
#Slenkstis
t=5
#Šifras
C=[7333109914047830423403358580366739968864018572071237174, 12064032717206770507949740475689958147166901266014058908]
#Balų failo rakto šifras
Cr=[8546284775834385955786936313017527364304510802731847173, 6854974634499061100353407038611108234835399974938772026]

z_1 = power_mod(C[0],y_1,p)

[x_2,y_2]=[7844124052, 41714609188702023833787726715]
[x_3,y_3]=[2462963080, 15002719016344124139387721584]
[x_4,y_4]=[2709051497, 45902960490610215320735106048]
[x_5,y_5]=[8688256461, 30435986281558612299144403365]

X = [x_1,x_2,x_3,x_4,x_5]
Y = [y_1,y_2,y_3,y_4,y_5]

Z = []

for i in range(0,len(X)):
    Z.append(power_mod(C[0],Y[i],p))
    
[z_1,z_2,z_3,z_4,z_5] = Z

b1 = ( ( x_2*x_3*x_4*x_5 ) / ( (x_2-x_1)*(x_3-x_1)*(x_4-x_1)*(x_5-x_1) ) ) % q
b2 = ( ( x_1*x_3*x_4*x_5 ) / ( (x_1-x_2)*(x_3-x_2)*(x_4-x_2)*(x_5-x_2) ) ) % q
b3 = ( ( x_1*x_2*x_4*x_5 ) / ( (x_1-x_3)*(x_2-x_3)*(x_4-x_3)*(x_5-x_3) ) ) % q
b4 = ( ( x_1*x_2*x_3*x_5 ) / ( (x_1-x_4)*(x_2-x_4)*(x_3-x_4)*(x_5-x_4) ) ) % q
b5 = ( ( x_1*x_2*x_3*x_4 ) / ( (x_1-x_5)*(x_2-x_5)*(x_3-x_5)*(x_4-x_5) ) ) % q

      
B = [b1,b2,b3,b4,b5]
B





