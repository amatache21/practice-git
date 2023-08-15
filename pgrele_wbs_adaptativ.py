#INPUT NR BITI SI NR BLOC BITI
# nr_biti = int(input())
# nr_biti_bloc = (int(input()))
nr_biti = 10
nr_biti_bloc = 3

codare_in_zero = ['0']
codare_in_unu = ['1']

#definire marime codare pt formarea ulterioara a raportului
marime_codare_in_zero = 1
marime_codare_in_unu = 1

#INPUT BITI
biti = '1110001110'
# for i in range(nr_biti):
#     bit = input()
#     biti += bit

print(f'biti: {biti}')

def impartire_egala_str(your_str, n):
    return [your_str[i:i+n] for i in range(0, len(your_str), n)]

blocuri_biti = impartire_egala_str(biti, nr_biti_bloc)

print(f'blocuri biti: {blocuri_biti}')

# ignorarea blocurilor nule
for bloc in blocuri_biti:
    bloc_codare_0 = ''
    marime_bloc_codare_0 = 0
    if '1' in bloc and '0' in bloc or '1' in bloc and '0' not in bloc:
        # print('blocul contine 1 si 0 sau doar 1')
        bloc_codare_0 = '1' + bloc
    else:
        # print('blocul contine numai 0')
        bloc_codare_0 = '0'
        
    marime_bloc_codare_0 = len(bloc_codare_0)
    marime_codare_in_zero += marime_bloc_codare_0
    codare_in_zero.append(bloc_codare_0)

print(f'codare_in_zero: {codare_in_zero}')
print(f'raport codare in zero: {nr_biti / marime_codare_in_zero}')

# ignorarea blocurilor nenule
for bloc in blocuri_biti:
    bloc_codare_1 = ''
    marime_bloc_codare_1 = 0
    if '1' in bloc and '0' in bloc or '0' in bloc and '1' not in bloc:
        # print('blocul contine 1 si 0 sau doar 0')
        bloc_codare_1 = '0' + bloc
    else: 
        # print('blocul contine numai 1')
        bloc_codare_1 = '1'

    marime_bloc_codare_1 = len(bloc_codare_1)
    marime_codare_in_unu += marime_bloc_codare_1   
    codare_in_unu.append(bloc_codare_1)

print(f'codare_in_unu: {codare_in_unu}')
print(f'raport codare in unu: {nr_biti / marime_codare_in_unu}')
raport_codare_zero = nr_biti/marime_codare_in_zero
raport_codare_unu = nr_biti/marime_codare_in_unu

if raport_codare_unu > raport_codare_zero:
    print(raport_codare_unu) 
    for bloc in codare_in_unu:
        for bit in bloc:
            print(bit)

else:
    print(raport_codare_zero) 
    for bloc in codare_in_zero:
        for bit in bloc:
            print(bit)