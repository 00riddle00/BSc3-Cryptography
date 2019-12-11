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

print S

# Raskite paslaptį, padalytą pagal Asmutho-Blumo schemą su slenksčiu t=3,
# ir padalykite ją iš naujo 5 dalyviams pagal Shamiro schemą su slenksčiu 2
t = 3
[p,p1,p2,p3]=[18430037, 36860003, 73720013, 147440003]
[s1,s2,s3]=[30453158, 30453172, 30453149]

