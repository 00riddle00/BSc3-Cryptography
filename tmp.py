# Gouillou-Quisquater digital signature

A = 'abcdefghijklmnopqrstuvwxyz0123456789'
def hash(text, n):
    t=''
    for r in text:
        if r in A:
            ind=A.index(r)+1
            if ind<10: t = t+'0'+str(ind)
            else: t=t+str(ind)
    return int(t,10)%n  

x = hash("tomasgiedraitis", 10000000000)

a = next_prime(2^13) # pasirenkame
p = next_prime(2^64)
q = next_prime(2^72) # sikart pasirenkame savo nuoziura 

n = p*q
phil_n = (p - 1)*(q - 1)

#print n
#print phil_n

e = next_prime(2^17)
print gcd(phil_n, e)

I = x #7821411115
print gcd(n, I)

d = 1/e % phil_n
# a = 1/power_mod(I, d, n) % n
a = power_mod(I, -d, n)

#print a

K_pr = a
K_pb = [n, e, I]

k = next_prime(2^15)
r = power_mod(k, e, n)
l = hash(str(x+r), 10000000000)

s = k*power_mod(a, l, n) % n

u = power_mod(s,e,n) * power_mod(I,l,n) % n
# print 'u is ', u
# print 'r is ', r

ls = hash(str(x+u), 10000000000)
print 'ls == l is ', ls == l

Sig = [s, l]

print 'x = ', x                   # Pranesimas
print '[s, l] = ', Sig            # Parasas
print '[n, e, I] = ', K_pb        # Viesas raktas (parasui tikrinti)
