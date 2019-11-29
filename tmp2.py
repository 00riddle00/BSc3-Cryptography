# DSS sudarymas
q = 
Kv = [p,q,alpha,beta]


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