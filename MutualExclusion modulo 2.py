import time
import sys

sys.setrecursionlimit(5)

def move(P,x):
    if x==0:
        P[x] = (P[x]+1) % (2)
    else:
        P[x] = P[x-1]
    return P

def MutualExclusion(n,P,step):
    print(P)
    worst_case = step
    SK = [1]*n
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
        return worst_case
    for s in range(0,n):
        if SK[s]==1:
            powrot_guarantee = P[s]
            worst_case = max(worst_case, MutualExclusion(n,move(P,s), step+1))
            P[s] = powrot_guarantee
    print('hej')
    return worst_case


def all_configurations(n):
    worst = 0
    if n==3:
        for a in range(0,n+1):
            for b in range(0,n+1):
                for c in range(0,n+1):
                    P=[a,b,c]
                    z = MutualExclusion(n,P,0)
                    if worst < z:
                        worst = z
    if n==4:
        for a in range(0,2):
            for b in range(0,2):
                for c in range(0,2):
                    for d in range(0,2):
                        P=[a,b,c,d]
                        print(P)
                        z = MutualExclusion(n,P,0)
                        if worst < z:
                            worst = z

    return worst


n = 4
#Maksymalna liczba krokow do konfiguracji legalnej
start = time.time()
print('n =',n,'\nworst case:',MutualExclusion(n,[0,0,1,0],0))
end = time.time()
print('czas:',end - start,'s')
