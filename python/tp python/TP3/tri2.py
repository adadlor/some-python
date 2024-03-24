

def tri2(T):
    if len(T) == 0: #on dégage la possibilité d'un tableau vide
        return T
    #calcul du maximum et du minimum de t :
    max_t = T[0]
    min_t = T[0]
    for nbr in T:
        if nbr > max_t:
            max_t = nbr
        if nbr < min_t:
            min_t = nbr
    #creation de Cpt
    Cpt = [0 for i in range(max_t - min_t +1)] #+1 car sinon max_t n'est pas compté
    
    #print("len de cpt : " + str(len(Cpt)))
    #remplissage de cpt
    for val in range(len(Cpt)):
        for nbr in T:
            if nbr == (val+min_t) :
                Cpt[val] += 1
    
    #reremplissage de T
    T = []
    for val in range(len(Cpt)):
        for ite in range(Cpt[val]):
            T.append(val+min_t)
            
    return T

print(tri2([3, 5, 1, 0, 5, 3, 8, 8, 0, 3, 5, 2]))
print(tri2([]))
print(tri2([-5, 2, -4, 0, 1, 2, 4]))