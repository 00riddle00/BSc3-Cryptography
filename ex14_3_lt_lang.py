# ESIGN digital signature

from sage.functions.log import logb

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

k = 123456789

p = next_prime(2^64) # pasirenkame
q = next_prime(2^65) # pasirenkame

v = x
nEsign = p*p*q

r = next_prime(2^62)               # pasirenkame (mazesnis uz p)

print "Is r valid:", r < p

w = ceil((((v - power_mod(r,k,nEsign)) % nEsign) / (p*q)))
y = w / (k * power_mod(r,k-1,p)) % p
s = (r + y*p*q) % nEsign

K_pb = [nEsign, k]

# Verification
# if s := s+1, should not work!
u = power_mod(s,k,nEsign)
z = v

print "verifying:", z <= u and u <= 2^ceil((2/3)*log(nEsign,2))

print 'x =', x                  # Pranesimas
print "[n, k]=", K_pb           # Viesas raktas
print "s=", s                   # Parasas