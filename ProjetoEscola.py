nome =input('Qual o nome do aluno? \n' )
nota1 = float(input('Qual a nota do primeiro Bimestre? \n ' ))
nota2 = float(input('Qual a nota do segundo Bimestre? \n ' ))
nota3 = float(input('Qual a nota do terceiro Bimestre? \n ' ))
nota4 = float(input('Qual a nota do quarto Bimestre? \n ' ))
soma = (nota1 + nota2 + nota3 + nota4) / 4
print('Sua média é {soma}. \n ')

if soma >= 7:
    print(f'{nome}, sua média foi {soma}, você foi APROVADO.' )
else: 
    print(f'{nome}, sua média foi {soma}, você foi REPROVADO.' )


'''
Inserir notas na lista,
A Soma ser feita baseada nas notas da Lista, não da variavel soma .
Possibilidade de escolher, ver a média 
ou nota de bimestre especifico .
'''