# -*- coding: utf-8 -*-

from copy import deepcopy

abc='AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ'
abcd='AaĄąBbCcČčDdEeĘęĖėFfGgHhIiĮįYyJjKkLlMmNnOoPpRrSsŠšTtUuŲųŪūVvZzŽž'
n = len(abc)
K = [[25,14],[6,29]]

sifr1=u'''
Pūbtb ūhaėū eyeąk cmėiū zoeim 
pčtūi pėšfū ąkloė bflvū fūoėb 
fėhtū ąėbhf ūąklr ūyūpd pmfk
'''

sifr2=u'''
Fžrlb lvėęį fėžėk cocėŠ fųoįė 
fdyfv ąfįžė fūbfv hįėvf ydįėŠ 
fųogv įhbga fėuįę įfeėf ėsįjf 
olfhy įzfhę lblve rųfzh lzevž 
hvfųv rfųoį ėjųhį ėfhjh įkžėz 
įfvbį ėįbėf sždšė aįsųz fojzį 
rllyf vbįėf hęaįž hžėęž rlsįb 
lsįėį fdvfį ffhhl zpėfz įhęaį 
žhųėo fė
'''

sifr3=u'''
LŽOAL ŪYČŠA KČČGL ŪNKČL ELŽČP 
RĄŽOP ŪAČUŽ ŪTUFU YĖTUF ŪĘĖLŲ 
ČLČFČ UYŪLY ČURSY ČURKY ČURKČ 
GYČPČ AKČCŲ KLKGS RGKFČ KČRMŲ 
UPŪAK ČCTKE PČKER ŪLUPČ LUPŪA 
KČCŲČ LČUYL RKELČ EŪLUL KEĘĖL 
LCČPN EĘČEŪ LUZEŲ ŪLYKR EAĘUL 
ŽĖŽČ
'''

sifr4=u'''
ĮEĘZL ZIŠŪP YFČKG ŪYSDB TŠUAŲ 
OLGAT MĘMKP SIŠDA TUYĄZ ŠFYSI 
OĘŲOF BŠŪĖŪ FVTUR ĮĖŪLF OPRPK 
UREŠP YŲOOR ŪTUJL YFAMČ ŪĖULG 
OĘ
'''

def clean_text(text):
    return text.replace('\n', ' ').replace('\r', '').replace(' ', '')

def Ceasar(alphabet,text,l1,l2):
    n = len(alphabet)
    text = clean_text(text)
    res=''
    for c in text:
        m=(l1*alphabet.index(c)+l2)%n
        res+=alphabet[m]
    return res

# bf := bruteforce
def bf_Ceasar_1():
    for l1 in range(1, 64, 2):
        l2 = (4 - 18*l1) % 64
        print("l1={}  | l2={}".format(l1,l2))
        print(Ceasar(abcd,sifr2, l1, l2))


def bf_Ceasar_2():
    for l1 in range(1, 32, 2):
        for l2 in range(32):
            print("l1={}  | l2={}".format(l1,l2))
            print(Ceasar(abc,sifr3, l1, l2))
            
            
def det(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]

def vector_x_matrix(V, M):
    return [ V[0]*M[0][0] + V[1]*M[1][0], V[0] * M[0][1] + V[1] * M[1][1] ]

def scalar_x_matrix(s, M):
    return [[item * s for item in row] for row in M]

def mod_of_vector(V, n):
    return [item % n for item in V ]

def mod_of_matrix(M, n):
    return [[item % n for item in row] for row in M]

def reorderM(M):
    M1 = deepcopy(M)
    M1[0][0] = M[1][1]
    M1[0][1] = -M[0][1]
    M1[1][0] = -M[1][0]
    M1[1][1] = M[0][0]
    return M1

def inverse(M):
    # Sage is needed here. 1/x => 0, 1.0/x => ok, but we need fractions
    return mod_of_matrix(scalar_x_matrix (1 / det(M), reorderM(K)), n)


def Hill(text,K):
    text = clean_text(text)

    # cc := ciphered text to numbers
    cc = []

    for c in text:
        cc.append(abc.index(c))

    res=''

    i = 0
    K_inv = inverse(K)

    while i < len(text):
        c_vector = [ cc[i], cc[i+1] ]

        m_vector = mod_of_vector(vector_x_matrix( c_vector, K_inv ), n)
        for el in m_vector:
            res += abc[el]
        i+=2

    return res

# T1
#print(Ceasar(abcd, sifr1, 25, 48))

# T2
# ans. starts with "Buvo"
#bf_Ceasar_1()

# T3
# ans. starts with "STŪKSO"
#bf_Ceasar_2()

# T4
#import time

#start = time.time()

#print(Hill(sifr4, K))

#end = time.time()
#print("{0:.3f}ms".format((end-start)*1000))
