# UZD 1

#Needham-Shroeder sesijos rakto nustatymo protokolas
#http://www.mif.vu.lt/katedros/matinf/asm/vs/pask/crypto/crpr_07/cr_protocols/needh.php

#K_AC=27
#1. A->C: tomas zigmas riiirri
#2. A<-C:  H999HH9aP97C1IaRWaGLP942q8  
#des: (63-27)*H999HH9aP97C1IaRWaGLP942q8 ->  riiirri zigmas 16 qvzidbPh
#3. A->B: qvzidbPh
#4. A<-B:  HM
#des: (63-16)*HM -> 27
#sifr: 16*(27-1) -> HL
#5. A->B: HL

#tomas zigmas riiirri*H999HH9aP97C1IaRWaGLP942q8*qvzidbPh*HM*HL

#Jums skirtas laiškas:
#ayu0P0qy3 4zqPtAy7q9y8Q -> (desifravus su raktu k=16) -> Kiek kainuoja dviratisA
#Įveskite į atsakymų puslapį:
#Needham-Shroeder
#tomas zigmas riiirri*H999HH9aP97C1IaRWaGLP942q8*qvzidbPh*HM*HL
#gbZNfxmVTZNfxeVVVeeV

# UZD 2
# Raskite paslaptį, padalytą pagal Shamiro schemą su slenksčiu t=3

t = 3

p=3138428376749
xi = [x1,x2,x3]=[2144295889985, 2637427724858, 2226520426368]
S_i = [s1,s2,s3]=[94897600353, 2024951377202, 2913545732906]

# Paslapties atkurimas
f0=S_i[0]*xi[1]*xi[2]/((xi[0]-xi[1])*(xi[0]-xi[2]))%p
f1=S_i[1]*xi[0]*xi[2]/((xi[1]-xi[0])*(xi[1]-xi[2]))%p
f2=S_i[2]*xi[0]*xi[1]/((xi[2]-xi[0])*(xi[2]-xi[1]))%p

S = (f0+f1+f2)%p

print "Shamiro paslaptis=", S
print "............."

# UZD 3

# Raskite paslaptį, padalytą pagal Asmutho-Blumo schemą su slenksčiu t=3,
# ir padalykite ją iš naujo 5 dalyviams pagal Shamiro schemą su slenksčiu 2
t = 3
[p,p1,p2,p3]=[18430037, 36860003, 73720013, 147440003]
[s1,s2,s3]=[30453158, 30453172, 30453149]

u = 1 / (p2*p3) % p1
v = 1 / (p1*p3) % p2
w = 1 / (p1*p2) % p3

S_masked = (s1*u*p2*p3 + s2*v*p1*p3 + s3*w*p1*p2) % (p1*p2*p3)

S = S_masked % p

# print S
print "Paslaptis=",S
print "p=",p

a1=2345

a=S+a1*x
n=5

xi=[23451325421412,123421342314132,1234213423423,1234234213,21342134]
print "xi=",xi

S_i=[int(a(x=u))%p for u in xi]
print "S_i=",S_i

