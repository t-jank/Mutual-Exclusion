

def iflegal(SK):
    if sum(SK) == 1:
        konfiguracja_legalna = True
    else:
        konfiguracja_legalna = False
    return konfiguracja_legalna

def MutualExclusion(n,P):
    SK=[] # sekcja krytyczna
    for i in range(0,n):
        P.append(-1)
        SK.append(2)
    step=0

    if P[0] == P[n-1]:
        SK[0] = 1
    else:
        SK[0] = 0
    for i in range(1,n):
        if P[i] != P[i-1]:
            SK[i] = 1
        else:
            SK[i] = 0


        
    
    
    return step

n = 5
P=[] # tokeny

for i in range(0,n):
    for j in range(0,n):
        for k in range(0,n):
            i=n



#Maksymalna liczba krokow do konfiguracji legalnej
print('n =',n,'\nworst case:',MutualExclusion(n,P))


