def chiffrage (m):
    T9 = {"a":"2", "b":"2", "c":"2", "d":"3", "e":"3", "f":"3", "g":"4", "h":"4", "i":"4", 
               "j":"5", "k":"5", "l":"5", "m":"6", "n":"6", "o":"6", "p":"7", "q":"7", "r":"7",
               "s":"7", "t":"8", "u":"8", "v":"8", "w":"9", "x":"9", "y":"9", "z":"9", " ":"0"}
    chaine=''    
    for i in m: chaine += T9[i]
    return chaine

#print(chiffrage("nom"))
def dechiffrage (m):
    dico = []
    chaine = []
    with open('dico.txt', 'r') as bank:
        for l in bank: dico.append(l.rstrip('\n'))
    for i in dico :
        if len(i)== len(m):
            cpt=0
            while chiffrage(i[cpt]) == m[cpt]:
                cpt+=1
                if cpt == len(i):
                    chaine.append(i) 
                    break           
    return chaine

#print(dechiffrage("666"))

