print('---------------------------------')
print ('Bem vindo ao jogo de advinhação!')
print('----------------------------------')

numero_secreto = 23
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute_str = input('Informe um número: ')
    print('Você digitou', chute_str)
    chute = int(chute_str)

#logica abaixo
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if (acertou):
        print ('Você acertou :) ')

    else: 
        if (maior):
         print( 'Você errou, o seu chute foi maior do que o número secreto')
        elif(menor):
         print('Você errou, o seu chute foi menor que o número secreto')
    rodada = rodada + 1

print ('fim do jogo :) ')    

#while = enquanto ainda há tentativas o código vai rodar