

def iflegal(P):
    SK=[] # sekcja krytyczna (mozliwosc ruchu dla kazdego wezla)
    n = len(P)
    for i in range(0,n):
        SK.append(2)
    if P[0] == P[n-1]:
        SK[0] = 1
    else:
        SK[0] = 0
    for i in range(1,n):
        if P[i] != P[i-1]:
            SK[i] = 1
        else:
            SK[i] = 0
    if sum(SK) == 1:
        konfiguracja_legalna = True
    else:
        konfiguracja_legalna = False
    return konfiguracja_legalna


def MutualExclusion(n,P,step):
    worst_case = 0
    if step > worst_case:
        worst_case = step

    if iflegal(P) == True:
        return worst_case
    
    for i in range(1,n):
        if P[i] != P[i-1]:
            A = P
            k = step
            k += 1
            MutualExclusion(n,A,k)
    
  
    return worst_case


n = 3
P=[] # tokeny
for i in range(0,n):
    P.append(-1)

P[0]=0
P[1]=1
P[2]=1



#Maksymalna liczba krokow do konfiguracji legalnej
print('n =',n,'\nworst case:',MutualExclusion(n,P,0))


