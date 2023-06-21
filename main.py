import binary_search as bs
import random as r
import sys        

print('Olá. Vamos definir uma lista.\n')

QTD = int(input('Digite a quantidade números.\n'))
INI = int(input('Digite o primeiro número da faixa.\n'))
END = int(input('Digite o último número da faixa.\n'))

if(INI > END):
    aux = INI
    INI = END
    END = aux

try: 
    array = r.sample(range(INI,END+1),QTD)
except:
    QTD_S = END - INI + 1
    print(f'\nErro.\nSerão gerados números sem repetição, não há como gerar {QTD} números com {QTD_S} disponíveis.\n')
    sys.exit(1)

num = int(input('\nDigite um número a ser procurado.\n'))

res = bs.binary_search(array,num)

if res == 'NULL':
    print(f'Elemento {num} não está presente na lista.\n')
else:
    print(f'Elemento {num} foi identificado na posição {res} (ordem crescente).\n')
