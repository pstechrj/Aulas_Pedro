#Operadores Relacionais

#= afirma
#== pergunta
#== igualdade
#----

#>= maior que ou igual a....?
#<= menor que ou igual a ...?
#!= diferente ?

#-------------------------------------


nome = input('Qual seu nome?')
idade = input('Qual a sua idade?')
idade = int(idade)


idade_limite = 18

if idade >= (idade_limite):
    print(f'{nome} Pode pegar o empréstimo.')
else:
    print (f'{nome} Não pode pegar o emprestimo.')