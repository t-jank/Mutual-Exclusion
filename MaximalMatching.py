import random

v = 8 # liczba wierzcholkow
V = []
for i in range(0,v):
    V.append(i)
wybor = [0]*v

AdjacencyList = []
liczba_krawedzi = 0.5 * v*(v-1)/2
for i in range(0,v):
    AdjacencyList.append([])
for j in range(0,int(liczba_krawedzi)):
    v1 = random.randint(0,v-1)
    v2 = random.randint(0,v-1)
    while v2 in AdjacencyList[v1] or v2 == v1:
        v2 = random.randint(0,v-1)
    AdjacencyList[v1].append(v2)
    AdjacencyList[v2].append(v1)
print(AdjacencyList)

koniec = 0
while True:
    koniec+=1
    for i in range(0,v):
        suma_sasiadow = 0
        for j in range(0,len(AdjacencyList[i])):
            suma_sasiadow += wybor[AdjacencyList[i][j]]
        if suma_sasiadow == 0:
            wybor[i] = 1
        else:
            wybor[i] = 0
    if koniec == 100: break
print(wybor)

