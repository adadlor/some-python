from tqdm import tqdm, tqdm_gui
from time import sleep
import matplotlib.pyplot as plt

def recherche(T, r):
    """
    param :
        T : tableau
        r : var

    rôle : rechercher par le biais d'une recherche linéaire si la position de r dans T

    précondition : 
        T tableau
        r valeurs a chercher comparable au valeurs de T

    postcondition :
        indice de r dans T si r est dans T
        None si r n'est pas dans le tableau

    """
    pos = 0
    for i in T:
        if i == r:return pos
        pos += 1
    return None

def recherche2(T, r, i=0):
    if T[i] == r :return i
    elif i > len(T-1):return None
    return recherche2(T, r, i+1)

#exo3
def rechercheproche(T, r):
    test = recherche(T, r)
    if test != None:return test
    else: 
        return rechercheproche(T, r-1), rechercheproche(T, r+1)

def diss(T, r):
    r2 = rechercheproche(T, r)
    if r2 != None:
        return abs(r - r2)
#-------------------------------------------------------------------
def diss2(a, b):
    return abs(a - b)

def rechercheproche2(T, r, diss2):
    return T.index(min([diss2(r, i)for i in T]))

#tp1

#1
def ex1():
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    plt.plot(L)
    for i in tqdm_gui(range(len(L))):
        sleep(1)


ex1()