from copy import copy

gros_si_dim = input().split(' ')

grosime_raft_etalon = int(gros_si_dim[0])
dimensiuni = int(gros_si_dim[1])

cmg_carte_de_introdus = 0

grosime_raft_curent = copy(grosime_raft_etalon)
carti_asezate = []
registru = {}

# metoda 1
def verificare_carti_pt_asezare(registru):
    # sum(registru.values())
    summ = sum(registru.values())
    # print(summ)
    if summ == 0:
        return False
    else:
        return True
    
# metoda 2
# def verificare_carti_pt_asezare(registru):
#     # sum(registru.values())
#     summ = 0
#     for key,value in registru.items():
#         summ += value
#     if summ == 0:
#         return False
#     else:
#         return True


for dimensiune in range(dimensiuni):
    carti_si_grosime_carte = input().split(' ')
    registru[int(carti_si_grosime_carte[1])] = int(carti_si_grosime_carte[0])

#cea mai mica carte
cmm_carte = min(registru.keys())

print(f'Cmm carte: {cmm_carte}')
print('registru inainte de asezare: ', registru)
while(verificare_carti_pt_asezare(registru)):
    cmg_de_introdus = 0
    
    while(grosime_raft_curent >= cmm_carte):
        for key, value in registru.items():
            if value != 0 and key <= grosime_raft_curent:
                cmg_carte_de_introdus = key
                grosime_raft_curent = grosime_raft_curent - cmg_carte_de_introdus
                carti_asezate.append(cmg_carte_de_introdus)
                registru[key] = registru[key] - 1
        if verificare_carti_pt_asezare(registru) == False:
           break
    
    print(*carti_asezate)

    carti_asezate.clear()
    grosime_raft_curent = copy(grosime_raft_etalon)
    

print('registru dupa asezare: ', registru)
print('SFARSIT')
