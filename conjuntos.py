arquivos = ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt']

for arquivo in arquivos:
    
    with open(arquivo, 'r') as arquivo:

        qtde_operacao = int(arquivo.readline())

        for i in range(qtde_operacao):
            
            operacao = arquivo.readline().strip()

            conjunto1 = set(arquivo.readline().strip().split(','))
            
            conjunto2 = set(arquivo.readline().strip().split(','))

            if operacao == 'U':
                resultado = conjunto1.union(conjunto2)
                print(f"União: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}")

            elif operacao == 'I':
                resultado = conjunto1.intersection(conjunto2)
                print(f"Interseção: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}")

            elif operacao == 'D':
                resultado = conjunto1.difference(conjunto2)
                print(f"Diferença: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}")

            elif operacao == 'C':
                resultado = {(x, y) for x in conjunto1 for y in conjunto2}
                print(f"Produto Cartesiano: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}")