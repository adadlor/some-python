

def tri1(T):
    Cpt = [0 for i in range(10)]
    #remplissage de Cpt
    for val in range(len(Cpt)):
        for nbr in T:
            if nbr == val :
                Cpt[val] += 1
                
                
    #reremplissage de T
    T = []
    for val in range(len(Cpt)):
        for ite in range(Cpt[val]):
            T.append(val)
        
    return T

print(tri1([3, 5, 1, 0, 5, 3, 8, 8, 0, 3, 5, 2]))
print(tri1([]))

T = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for i in range(len(T))[::-1]:
    print(T[i])
            