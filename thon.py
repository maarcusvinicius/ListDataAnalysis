temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 17)
print(f'Os dados foram {princ}')
print(f'Ao todo foram criados {len(princ)} registros')
print(f'O maior peso foi de {mai:.2f}Kg. ', end='')
for p in princ:
    if p[1] == mai:
        print(f'Peso de {p[0]}')
print(f'O menor peso foi de {men:.2f}Kg. ', end='')
for p in princ:
    if p[1] == men:
        print(f'Peso de {p[0]} ')