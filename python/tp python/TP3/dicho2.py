def DichoRec(T, x, g=0, d=None):
    if d is None:
        d = len(T)-1
    if g <= d:
        mil = (g+d) // 2
        if T[mil] == x:
            return mil
        elif x < T[mil]:
            return DichoRec(T, x, g, mil-1)
        else:
            return DichoRec(T, x, mil+1, d)
    return None



def dicho2(T, x, g, d = None):
    #on suit le meme template que pour dichorec, en inversant le processus pour traiter un tableau décroissant
    
    if d is None: #pas nécéssaire dans ce cas
        d = len(T)-1
    if g <= d:
        mil = (g+d) // 2 #rien ne change pour le calcul
        if T[mil] == x:
            return mil #pareil, aucun changement si valeur adéquate
        elif x < T[mil]: #si x est plus petit, c'est qu'il est sur la partie superieure
            return dicho2(T, x, mil + 1, d)
        else: #dqns l'autre cas, c'est qu'il est en dessous
            return dicho2(T, x, g, mil-1)
    return None

print(dicho2([4, 2, 1, 0], 2, 0, 3))
print(dicho2([4, 2, 1, 0], 3, 0, 3))

        