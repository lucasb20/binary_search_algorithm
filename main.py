print('Olá. Vamos definir uma lista.\n')

N = int(input('Digite uma quantidade de números.\n'))
SHI = int(input('Digite um deslocamento para os números.\n'))

array = [x+SHI for x in range(N)]

array.sort()

print(array)

n = int(input('Digite um número a ser procurado.\n'))