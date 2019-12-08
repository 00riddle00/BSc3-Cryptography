# DSA signature

A='abcdefghijklmnopqrstuvwxyz0123456789'
def hash(text,n):
    t=''
    for r in text:
        if r in A:
            ind=A.index(r)+1
            if ind<10: t=t+'0'+str(ind)
            else: t=t+str(ind)
    return int(t,10)%n  

x = hash("tomasgiedraitis", 10000000000)

a = next_prime(2^13) # pasirenkame
p = next_prime(2^64) # pasirenkame

#q = factor(p-1)
q = 658812288346769701 # pasirenkame is keliu variantu

g = primitive_root(p)
alpha = power_mod(g, (p-1)//q, p)
beta  = power_mod(alpha, a, p)

K_pr = a

K_pb = [p, q, alpha, beta]

k = next_prime(2^52)
#k = 165616515645645612
print 'gerai parinktas k? ', gcd(k,p-1) == 1

gama  = power_mod(alpha, k, p)%q
delta = (x + a*gama)/k % q
print 'gerai parinktas delta? ', gcd(delta, q) == 1

e1 = (x/delta)    % q
e2 = (gama/delta) % q

print "Tikrinimas:", power_mod(alpha, e1, p) * power_mod(beta, e2, p) % p % q == gama % q

Sig = [gama, delta]

print 'x=', x                                # Tekstas
print '[gama, delta]=', Sig                  # Parasas
print '[p, q, alpha, beta]=', K_pb           # Viesas raktas