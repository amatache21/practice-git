class Zaruri:
    numere_zar = ['1','2','3','4','5','6']
    def __init__(self, numar_zaruri:int):

        assert 1<= numar_zaruri  <= 100, "Numarul de zaruri trebuie sa fie cuprins intre 1 si 100!"
        self.numar_zaruri = numar_zaruri

    def output(self):
        lista_zaruri_nevazute = []
        for i in range(self.numar_zaruri):
            inpt = input().split(' ')
            for nr in self.numere_zar: 
                if nr not in inpt:
                    lista_zaruri_nevazute.append(int(nr))
                else:
                    continue
        print(sum(lista_zaruri_nevazute))