

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


def all_configurations(n):
    if n==2:
        for a in range(0,n):
            for b in range(0,n):
                P=[a,b]
                print(P)
    if n==3:
        for a in range(0,n):
            for b in range(0,n):
                for c in range(0,n):
                    P=[a,b,c]
                    print(P)
    if n==4:
        for a in range(0,n):
            for b in range(0,n):
                for c in range(0,n):
                    for d in range(0,n):
                        P=[a,b,c,d]
                        print(P)
    if n==5:
        for a in range(0,n):
            for b in range(0,n):
                for c in range(0,n):
                    for d in range(0,n):
                        for e in range(0,n):
                            P=[a,b,c,d,e]
    if n==6:
        for a in range(0,n):
            for b in range(0,n):
                for c in range(0,n):
                    for d in range(0,n):
                        for e in range(0,n):
                            for f in range(0,n):
                                P=[a,b,c,d,e,f]

n = 3
P=[] # tokeny
for i in range(0,n):
    P.append(-1)

P[0]=0
P[1]=1
P[2]=1


#Maksymalna liczba krokow do konfiguracji legalnej
print('n =',n,'\nworst case:',MutualExclusion(n,P,0))


