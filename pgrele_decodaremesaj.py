import string

#input cod de decodat

# cod_decodare_sir = input()
cod_decodare_sir = '195318510'

cod_pt_decodare = cod_decodare_sir[:2]

#creare cod pt alfabet

alphabet = list(string.ascii_uppercase)
alphabet_cod = {}
cod = 0

cod_decodat = ''

for litera in alphabet:
    cod += 1
    alphabet_cod[litera] = cod

print(alphabet_cod)

max_cod = max(alphabet_cod.values())

# print(max_cod)

while len(cod_decodare_sir) > 0:

    #verificare daca nu e format doar din 0
    if '0' not in cod_pt_decodare or cod_pt_decodare[0] == '0':
        cod_pt_decodare = cod_decodare_sir[:2]
        print(cod_pt_decodare)
        if int(cod_pt_decodare) <= max_cod:
            # print(cod_pt_decodare)
            for key,value in alphabet_cod.items():
                # print(value)
                if int(cod_pt_decodare) == value:
                    # print(key)
                    cod_decodat += key
                    cod_decodare_sir = cod_decodare_sir[2:]
                    print(cod_decodare_sir)
        elif int(cod_pt_decodare) > max_cod:
            for key,value in alphabet_cod.items():
                if int(cod_pt_decodare[0]) == value:
                    # print(key)
                    cod_decodat += key
                    cod_decodare_sir = cod_decodare_sir[1:]

    #verificare daca e format doar din 0
    else:
        cod_pt_decodare = cod_decodare_sir[:2]
        if cod_pt_decodare == '00':
            cod_decodat += ' '
            cod_decodare_sir = cod_decodare_sir[2:]
    
print(cod_decodat)





