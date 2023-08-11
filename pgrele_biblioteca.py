from copy import copy

gros_si_dim = input().split(' ')

grosime_raft_etalon = int(gros_si_dim[0])
dimensiuni = int(gros_si_dim[1])

cmg_carte_de_introdus = 0
cmm_carte = copy(grosime_raft_etalon)

grosime_raft_curent = copy(grosime_raft_etalon)
carti_asezate = []
registru = dict()
carti_de_asezat = True

# metoda 1
def verificare_carti_pt_asezare(registru):
    # sum(registru.values())
    summ = sum(registru.values())
    # print(summ)
    if summ == 0:
        carti_de_asezat = False
    else:
        carti_de_asezat = True
    return carti_de_asezat
    

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
    if int(carti_si_grosime_carte[1]) < cmm_carte:
        cmm_carte = int(carti_si_grosime_carte[1])

# cmm_carte = min(registru.keys())

# print(registru)

print(f'Cmm carte: {cmm_carte}')
print('registru inainte de asezare: ', registru)
while(carti_de_asezat):
    # print('while1')
    cmg_de_introdus = 0
    
    while(grosime_raft_curent >= cmm_carte):
        # print(f'grosime raft curent: {grosime_raft_curent}')
        # print(f'cmm carte: {cmm_carte}')
        for key, value in registru.items():
            # print('da2')
            if value != 0 and key <= grosime_raft_curent:
                cmg_carte_de_introdus = key
                grosime_raft_curent = grosime_raft_curent - cmg_carte_de_introdus
                carti_asezate.append(cmg_carte_de_introdus)
                registru[key] = registru[key] - 1
        if verificare_carti_pt_asezare(registru) == False:
           break
    
    # print(registru)
    print(*carti_asezate)

    carti_asezate.clear()
    # print(carti_asezate)
    # print(grosime_raft_curent)
    grosime_raft_curent = copy(grosime_raft_etalon)
    
    # print(grosime_raft_curent)
    carti_de_asezat = verificare_carti_pt_asezare(registru)
    # print(carti_de_asezat)

print('registru dupa asezare: ', registru)
print('SFARSIT')
