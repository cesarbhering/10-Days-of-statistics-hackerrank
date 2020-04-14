Crianca1 = ['Menino', 'Menina']
Crianca2 = ['Menino', 'Menina']

probabilidades = 0
for i in Crianca1:
    for n in Crianca2:
        print(f'{i} e {n}')
        probabilidades += 1
#São 4 possibilidades, mas como sabemos que um já é menino, então exclui-se
#a opção de 'Menina , Menina', nos restando 3 opções, da qual 1 é 'Menino, Menino' 