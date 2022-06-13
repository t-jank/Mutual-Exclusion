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

def move(P,x):
    A=P
    if x==0:
        A[x] = (A[x]+1) % (len(A)+1)
    else:
        A[x] = A[x-1]
    return A

def MutualExclusion(n,P):
    worst_case = 0
    
    SK=[]
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
    if iflegal(P) == True:
        return worst_case

    for s in range(0,n):
        if SK[s]==1:
            A = P
            powrot_guarantee = P[s]
           # worst_case=max(worst_case,MutualExclusion(n,move(A,i)))
            MutualExclusion(n,move(A,s))
            P[s] = powrot_guarantee
    return worst_case


def all_configurations(n):
    worst = 0
    if n==2:
        for a in range(0,n+1):
            for b in range(0,n+1):
                P=[a,b]
                z = MutualExclusion(n,P)
                if worst < z:
                    worst = z
    if n==3:
        for a in range(0,n+1):
            for b in range(0,n+1):
                for c in range(0,n+1):
                    P=[a,b,c]
                    z = MutualExclusion(n,P)
                    if worst < z:
                        worst = z
    if n==4:
        for a in range(0,n+1):
            for b in range(0,n+1):
                for c in range(0,n+1):
                    for d in range(0,n+1):
                        P=[a,b,c,d]
                        z = MutualExclusion(n,P)
                        if worst < z:
                            worst = z
    if n==5:
        for a in range(0,n+1):
            for b in range(0,n+1):
                for c in range(0,n+1):
                    for d in range(0,n+1):
                        for e in range(0,n+1):
                            P=[a,b,c,d,e]
                            z = MutualExclusion(n,P)
                            if worst < z:
                                worst = z
    if n==6:
        for a in range(0,n+1):
            for b in range(0,n+1):
                for c in range(0,n+1):
                    for d in range(0,n+1):
                        for e in range(0,n+1):
                            for f in range(0,n+1):
                                P=[a,b,c,d,e,f]
                                z = MutualExclusion(n,P)
                                if worst < z:
                                    worst = z
    return worst


n = 4

#Maksymalna liczba krokow do konfiguracji legalnej
#print('n =',n,'\nworst case:',all_configurations(n))

MutualExclusion(n,[1,1,2,1])
