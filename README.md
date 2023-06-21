# binary_search_algorithm
Algoritmo de busca binária, basicamente busca um elemento em uma lista usando método binário, feito em Python.

Basicamente é gerado uma lista com base nos intervalo que você der, e um número a se procurar nessa lista.

O algoritmo utiliza busca binária para achar.

A busca binária consiste em ordenar os itens em ordem crescente e ver se o número é maior ou menor que o elemento do meio da lista. Se for menor, vai procurar para baixo, se for maior, vai procurar para cima, e vai seguindo assim, restringindo a faixa. Quando o elemento do meio corresponder ao alvo, o programa retornará essa posição na lista ordenada. Se não encontrou em nenhuma faixa, é retornado 'NULL'.

Basicamente isso o programa.

Fatos interessantes:

É um método muito mais eficiente que o método brusco, visto que usando um condicional 'if' comparar o alvo com cada item do array é muito mais processamento do que apenas um 'if' para cada metade do array, e condicional é algo que pesa bastante.

Por exemplo, procurar um número em uma faixa de 100 números, dezenas de condicionais seriam realizados, podendo ser até 100, enquanto com a busca binária, seria cerca de 7 'ifs'. Procurar um número em uma faixa de 1000 números, centenas de 'ifs' podendo ser até 1000, enquanto a busca binária usa cerca de 10. Com uma faixa de 100000 números, poderia ser até 100000 condicionais testados, enquanto a busca binária usaria cerca de 17.

Foi adicionado um medidor de tempo, totalmente inútil porque são poucas contas, já que não importa ter um array de 500000 números se somente 19 serão testados com condicionais. Então o tempo sempre é menos de 1 segundo, por volta de 5 casas após a vírgula.
