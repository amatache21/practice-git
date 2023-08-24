#AICI AM FACUT RAPID PROBLEMA CUM AM STIUT SI DE LA EA AM TRANSCRIS-O PRIN OOP
nr_zaruri = int(input())

numere_zar = ['1','2','3','4','5','6']

lista_zaruri_nevazute = []
for i in range(nr_zaruri):
    inpt = input().split(' ')
    for nr in numere_zar: 
        if nr not in inpt:
            lista_zaruri_nevazute.append(int(nr))
        else:
            continue

print(sum(lista_zaruri_nevazute))