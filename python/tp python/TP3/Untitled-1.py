import doctest

"""
T  =[1, 2, 3]
for i in range(len(T)-1, -1, -1):
    print(T[i])
"""
def nb_sup(T1, T2):
    """
    >>> nb_sup([1, 8, 2], [0, 10, 1])
    2
    >>> nb_sup([1, 8, 2, 3], [0, 10, 1])
    2
    """
    cpt = 0
    if len(T1) > len(T2):
        for i in range(len(T2)):
            if T1[i] > T2[i]: cpt += 1
    else:
        for i in range(len(T1)):
            if T1[i] > T2[i]: cpt += 1
    return cpt

def dicho2(T, x, g=0, d=None):
    """
    >>> dicho2([4, 2, 1, 0], 2, 0, 3)
    1
    >>> dicho2([4, 2, 1, 0], 3, 0, 3)
    None
    """
    if d is None:
        d = len(T)-1
    if g <= d:
        mil = (g+d) // 2
        if T[mil] == x:
            return mil
        elif x < T[mil]:
            return dicho2(T, x, mil+1, d)
        else:
            return dicho2(T, x, g, mil-1)
    return None

def combien(T, e):
    compte = 0
    for i in T:
        if i == e: compte +=1
    return compte

def tri2(T):
    if len(T) == 0: return T
    minT = min(T)
    maxT = max(T)
    Cpt = [0 for i in range(maxT - minT +1)]
    print(len(T))
    for k in range(len(Cpt)):
        for l in T:
            if l == (k+minT) :
                Cpt[k] += 1

    T = []
    for i in range(len(Cpt)):
        for j in range(Cpt[i]): 
            T.append(i+minT)  
    return T
print(tri2([3, 5, 1, 0, -24, 3, 8, 8, 0, 3, 5, 18]))
doctest.testmod

