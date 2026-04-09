# Crie um programa que faça o computador jogar jokempô com você: 

import random

jokempo = str(input('Vamos jogar jokempô ?\n' \
                    'pedra\n' \
                    'papel\n' \
                    'tesoura\n'))
 
jogo = ['pedra', 'papel', 'tesoura',]

embaralhar = random.choice(jogo)

if embaralhar == jokempo:
    print('Empate, vamos de novo!')
elif jokempo == 'pedra' and embaralhar == 'tesoura':
    print('Ganhou!')
elif  jokempo == 'tesoura' and embaralhar == 'papel':
    print('Ganhou!')
elif jokempo == 'papel' and embaralhar == 'pedra':
    print('Ganhou!')

else:
    print('Perdeu, vamos jogar novamente ?')

 



