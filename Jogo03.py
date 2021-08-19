from random import randint

c = int(randint(1, 20))

x = 6

nome = str(input('Qual o seu nome? '))

print('{}, descubra o número que estou pensando entre 1 e 20. Você terá 6 chances de acertar.'.format(nome))


while x > 0:
    x = x-1
    p = int(input('Digite um número: '))
    if c != p and x > 0:
        print('Você errou! Você ainda tem {} tentativas para acertar.'.format(x))
    elif c == p:
        print('PARABÉNS, {}! Você acertou o número que eu estava pensando!'.format(nome))
        x = -1

if x == 0:
    print('Que pena. Você não acertou! O número que eu estava pensando era {}.'.format(c))
elif x == -1:
    input()
print('THE END')

print('==x==' * 20)

