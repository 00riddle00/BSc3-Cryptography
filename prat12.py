
#Blumo-Goldwasserio šifro privatus raktas
K_pr=[172764355471, 535707589267]

#Šifras: 
C = [126, 33, 250, 155, 124, 5, 162, 85, 163, 212, 6, 246, 158, 15, 33, 25826257355237703374115]

p = K_pr[0]
q = K_pr[1]
x = C[-1]
n = p*q

t = len(C) - 1

e = power_mod( (p+1)/4, t+1, p-1)
d = power_mod( (q+1)/4, t+1, q-1)

u = power_mod(x, e, p)
v = power_mod(x, d, q)

s = (1/p) % q
t2 = (1/q) % p

x0 = (u*(t2*q) + v*(s*p)) % n

res = []

xi = x0
for i, ci in enumerate(C[:-1]):
    # if i = 0, then xi = x1, ci = c1, pi = p1 (just random explanation)
    xi = power_mod(xi, 2, n)
    ci = C[i]
    pi = xi % 256
    mi = ci^^pi
    res.append(chr(mi))

print res
