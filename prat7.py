x1 = 'K'
x2 = 'A'

Y = [86, 1, 168, 188, 56, 70, 195, 235, 157, 91, 81, 148, 21, 113, 41, 71, 15, 173, 169, 38, 70, 215, 240, 129, 69, 77, 147, 21, 116, 50, 92, 9, 178, 160, 52, 83, 212, 229, 145, 93, 87, 137, 17, 106, 63, 88, 22, 160, 165, 62, 86, 212, 225, 145, 92, 91, 141, 31, 107, 58, 75, 15, 166, 165, 48, 80, 202, 244, 152, 75, 77, 128, 25, 125, 63, 82, 10, 174, 175, 60, 86, 203, 243, 145, 68, 81]

c1 = 1

K_1_8 = ord(x1)^^Y[0]
K_9_16 = ord(x2)^^Y[1]

#print type(K_1_8)
#print str(K_1_8).encode()
#print int(K_1_8).to_bytes(1)
#print bytes(int(K_1_8))

K_1_8 = list(format(K_1_8, '#010b')[2:])
K_9_16 = list(format(K_9_16, '#010b')[2:])

print K_1_8
print K_9_16

K_1_16 = K_1_8 + K_9_16

print K_1_16

#for i in range(8):
#    for j in range(8):
#        print(K_1_16[j+i]),
#    print('| '),
#    print(K_1_16[j+i+1])

C_1_8 = [1,1,1,1,0,1,1,0]


# The system of linear feedback registers

def stream(c,xp,n):  # the keystream generation, c-coefficients, xp - initial state, n - number of bits
    x=[0,0,0,0,0,0,0,0]
    for i in range(0,8):
        x[i]=xp[i]
    sr=''
    for i in range(0,n):
        bt=0
        sr+=str(x[0])
        for j in range(0,8):
            bt+=c[j]*x[j]
        for j in range(1,8):
            x[8-j]=x[7-j]
        x[0]=bt%2
    return sr

# stream cipher
# t = baitu masyvas, kuri reikia issifruoti/desifruoti
# c = c8,c7,...,c1
# xp = pradines reg sistemos padetys (ten mistika)

def str_cipher(t,c,xp): # t - plaintext (ASCII decimal list), c-coefficients, xp - initial state
    cp=[]
    k=len(t)
    sr=stream(c,xp,8*k)
    for i in range (0,k):
        cp.append(t[i]^^int(sr[8*i:8*i+8],2))
    return cp
# How to use
c=[1,0,1,0,1,1,0,1]
t=[10,123]
xp=[1,0,1,0,1,1,0,1]
cp=str_cipher(t,c,xp)
print cp
print str_cipher(cp,c,xp)




