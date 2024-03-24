from convertisseur import CversF

with open("celsius.txt", "r") as fh:
    L = fh.readlines()

print(L)

def fichier_convertion(L):
    with open("fahrenheit.txt", "w") as f:
        for c in L:
            f.write(str(CversF(float(c))))
            f.write("\n")
        f.close

fichier_convertion(L)