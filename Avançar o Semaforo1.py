#Avançar o Semaforo

semaforo = input("Qual estado do sinal atualmente? \n")
numero_de_pessoas = int(input("Quantas pessoas vão atravessar? \n"))
if semaforo.lower() == 'verde':
    print('Motorista pode passar o sinal! ')
    print('Pessoas não podem atravessar. ')
elif semaforo.lower() =='vermelho':
    if numero_de_pessoas > 5:
        print('Pessoas não podem atravessar. ')
    else:
        print('Pedestres podem atravessar')
    print('Carro não pode ultrapassar o sinal! ')
elif semaforo.lower() =='amarelo':
    print('Diminua a velocidade e pare o carro! ')
    print('Pessoas não podem atravessar. ')
else:
    print('Condição não encontrada. ')





'''
Pergunte quantas pessoas tem para atravessar a rua 
e não permita que + do que 5 pessoas atravessem
'''