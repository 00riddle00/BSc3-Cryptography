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
  
#print vigen('raktas','tekstas') 


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
C0=[7333109914047830423403358580366739968864018572071237174, 12064032717206770507949740475689958147166901266014058908]
#Balų failo rakto šifras
Cr=[8546284775834385955786936313017527364304510802731847173, 6854974634499061100353407038611108234835399974938772026]

# pakeisti C = C0 arba C = Cr
C = Cr

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

z = 1

for j in range(0,t):
    z = z * power_mod(Z[j],B[j],p) % p
    
M = C[1] / z % p
M = to_text(M)
print "mano atsakymas=",M

Desifr_raktas = ''.join([A[A.index(letter) * -1 % N] for letter in list(M)])

sifr='''uoxtb9dvs5k0q5k4bdua1tnv.ituvi.cbbc9qmowa
pktuvi.caba9qaxwbspituvi.cab.9qjy3bwrmpmli3e5c9bm2csd6wv07=jspnwh4o1csds3vw4ajspnwh4o4csp0sv9uejspnwh5o0csfs3v
a
jspnwh4o3jwo5ly7oli3e5c.be5jtr5l27ili3e5c9bf5jbi5lu7ili3e5c9bf5j2u.l2
ibjspnwh6o1jblslb5ibjspnwh6o1jwa5mu
icjspnwh6o2csl030s2=jspnwh4o1csg
10wxbjspnwh4o6j
o4p2wicjspnwh6o2csts309u=ateye1cg.
l
13
1ux9gfnpjwp1hm5rm8a34zgfnpjwp0hh5rj=53y7ofnpjwp1hj5rjby4kuffnpjwp0jwo4tu4ili3e5c9bf5j
avtu9i.jspnwh5o5jxdatu9i
jspnwh5o8jtu9tu
pli3e5c.bg
w1g2rggvktswl4g5j
kag2r4orcjspnwh5o4
l
1x428x=teye1ce.bl
s072=kcp9oeue9==q1hbt4u1s9mafjprsig
0p72bl8teye1ce
k=t23vmrcjspnwh5o1
l
=x62bm8teye1ce
t7r3n2frcjspnwh4o0el
7jb3y58teye1ce
qxd3ruhvktswl4g7qty5l
wntuvi.cabfd1rs4u5.lpmli3e5c=bf7cshs06sw.jspnwh4qvs3mslipmli3e5c9bg2csdwr6s==
teye1cg.=sa5m6s=gjspnwh5o3csd6v6s
=ateye1cg.
l
2j=4u98teye1ce
2tu4n2orcjspnwh5o4
l
9jz42m8teye1ce
kar4rwnvktswl5g6ql43m0nijrcjspnwh6o1el
0p742u9kfnpjwp2hi5rub26stgfnpjwp0hh5rtu.6yzhbffjprsig.idmr34w5s46ke2a2r0p
twx5v6zb9ke2a2r2p=mr9y37i64ke2a2r0rjb99o1g9oeue9=
q2ki=6vzwa5ffjprsii.hbt=u4x6zdfjprsig.jbt4u1x63ebbfrlk==fgnmmjtsy4em.savtsq9rot2q4vnh.6o5ltls1sgrfckd
2pvzm=kbsuu.s
fgdrmvwrm.ua3j
qhjlwm5oj5ebk4a.hipmj00q5xr5fbk4a.hipnch4e4w3vnbk4a.hipkchvs8wjpebk4a.hhr3ym.i45afrlk==hgir9y3.m0
ke2a2r1p=t22z00zb8ke2a2r2p.t9u204mjbbfrlk==gglhmjoam5rr4savtsq9t22z1svhbbfrlk==ggihmjlsr6sv4savtsq9t4u32vvb9ke2a2r2p=mr=81amt4ke2a2r0r823cs1ffnpjwp0j4u28u7jhateye1ce.an5ryu
goqg4k9ke2a2r1pboktvi
3vpefrlk==ggjr5sseey59frlk==ggmr
'''
print vigen(Desifr_raktas, sifr)