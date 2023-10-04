#Avançar o Semaforo
semaforo = input("Qual estado do sinal atualmente? ")
if semaforo == 'verde':
    print('Pode passar o sinal! ')
elif semaforo =='vermelho':
    print('Não ultrapassar o sinal! ')
elif semaforo =='amarelo':
    print('Diminua a velocidade e pare o carro! ')
else:
    print('Condição não encontrada. ')
