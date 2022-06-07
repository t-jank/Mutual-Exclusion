import random

v = 8 # liczba krawedzi
V = []
for i in range(0,v):
    V.append(i)
wybor = [0]*v

AdjacencyList = []
for i in range(0,v):
    liczba_sasiadow = random.randint(1, v-3)
    AdjacencyList.append([])
    for j in range(0,liczba_sasiadow):
        sasiad = random.randint(0,v-1)
        while(sasiad in AdjacencyList[i]):
            sasiad = random.randint(0,v-1)
        AdjacencyList[i].append(sasiad)

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
