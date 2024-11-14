# 01
# numero = 10
# with open('variaveis.txt', 'w') as arquivo:
#     arquivo.write(str(numero))
#
# with open('variaveis.txt', 'r') as arquivo:
#     conteudo = arquivo.read()
#
# print(conteudo)

#02
#
# frutas = ['maçã','banana','creja']
#
# with open('frutas.txt','w') as arquivo:
#     for fruta in frutas:
#         arquivo.write(fruta + '\n')
#
# with open('frutas.txt','r') as arquivo:
#     conteudo = arquivo.read()
#
# print(conteudo)

#03
#
# with open('frutas.txt', 'r') as arquivo:
#     conteudo = arquivo.read().splitlines() #split divide o conteúdo em linhas
# print(conteudo[0])

#04

# with open('frutas.txt', 'r') as arquivo:
#     frutas = arquivo.read().splitlines()
#
# frutas[1] = 'laranja'
#
# with open('frutas.txt', 'w') as arquivo:
#     for fruta in frutas:
#         arquivo.write(fruta + '\n')
# with open('frutas.txt', 'r') as arquivo:
#     conteudo = arquivo.read()
#
# print(conteudo)

#5

# with open('frutas.txt', 'r') as arquivo:
#     frutas = arquivo.read().splitlines()
#
# frutas.append('uva')
#
# with open('frutas.txt', 'w') as arquivo:
#     for fruta in frutas:
#         arquivo.write(fruta + '\n')
#
# with open('frutas.txt', 'r') as arquivo:
#     conteudo = arquivo.read()
#
# print(conteudo)

#6

# with open('frutas.txt', 'r', encoding="utf-8") as arquivo:
#     frutas = arquivo.read().splitlines()
# frutas.remove('banana')
#
# with open('frutas.txt', 'w') as arquivo:
#     for fruta in frutas:
#         arquivo.write(fruta + '\n')
#
# with open('frutas.txt', 'r') as arquivo:
#     conteudo = arquivo.read()
# print(conteudo)

#7

# with open('frutas.txt', 'r') as arquivo:
#     frutas = arquivo.read().splitlines()
#
# numero_itens = len(frutas)
#
# with open('contagem.txt', 'w') as arquivo_contagem:
#     arquivo_contagem.write(f'Número de itens na lista:{numero_itens}\n')
#
# with open('contagem.txt', 'r') as arquivo_contagem:
#     conteudo = arquivo_contagem.read()
#
# print(conteudo)

#8

# with open('frutas.txt', 'r') as arquivo:
#     frutas = arquivo.read().split()
#
# fatia = frutas[1:3]
#
# with open('fatias.txt', 'w') as arquivo_fatia:
#     for item in fatia:
#         arquivo_fatia.write(item + '\n')
#
# with open('fatias.txt', 'r') as arquivo_fatia:
#     conteudo = arquivo_fatia.read()
#
# print(conteudo)

#9

# with open('frutas.txt', 'r', encoding='utf-8') as arquivo:
#     frutas = arquivo.read().splitlines()
#
# with open('frutas_lista.txt', 'w') as arquivo_lista:
#     for fruta in frutas:
#         arquivo_lista.write(fruta + '\n')
#
# with open('frutas_lista.txt', 'r') as arquivo_lista:
#     conteudo = arquivo_lista.read()
#
# print(conteudo)

#10
# with open('frutas.txt', 'r', encoding='utf-8') as arquivo: # aqui o enconding é necessário para verificar o '~' de maçã
#     frutas = arquivo.read().splitlines()
#
# if 'maçã' in frutas:
#     resultado = True
# else:
#     resultado = False
#
# with open('verificacao.txt', 'w') as arquivo_verificacao:
#     arquivo_verificacao.write(str(resultado) + '\n')
#
# with open('verificacao.txt', 'r') as arquivo_verificacao:
#     conteudo = arquivo_verificacao.read()
#
# print(conteudo)


# Intermediário

#1

# soma = 0
#
# with open('numeros.txt', 'r') as arquivo:
#     for linha in arquivo:
#         soma += int(linha.strip()) #strip remove espaços e quebras de linha
#
# print(f'Soma = {soma}')

#2

# contador_banana = 0
#
# with open('frutas.txt', 'r') as arquivo:
#     for linha in arquivo:
#         contador_banana += linha.lower().count('banana')
#
# with open('contagem_banana.txt', 'w') as arquivo_contagem:
#     arquivo_contagem.write(f'A palavra "banana" aparece {contador_banana}x no arquivo.\n')
#
# with open('contagem_banana.txt', 'r') as arquivo_contagem:
#     conteudo = arquivo_contagem.read()
#
# print(conteudo)

#3

# with open('arquivo1.txt', 'r') as arquivo1:
#     conteudo1 = arquivo1.read()  # Lê todo o conteúdo do arquivo1
#
# with open('arquivo2.txt', 'r') as arquivo2:
#     conteudo2 = arquivo2.read()  # Lê todo o conteúdo do arquivo2
#
# conteudo_combinado = conteudo1 + '\n' + conteudo2
#
# with open('arquivo_combinado.txt', 'w') as arquivo_combinado:
#     arquivo_combinado.write(conteudo_combinado)
#
# with open('arquivo_combinado.txt', 'r') as arquivo_combinado:
#     conteudo = arquivo_combinado.read()
#
# print(conteudo)
#
#

#4

# with open('frutas.txt', 'r', encoding='utf-8') as arquivo:
#     linhas = arquivo.readlines()
#
# linhas_filtradas = [linha for linha in linhas if 'cereja' not in linha.lower()]
#
# with open('frutas_filtradas.txt', 'w') as arquivo_filtrado:
#     arquivo_filtrado.writelines(linhas_filtradas)
#
# with open('frutas_filtradas.txt', 'r') as arquivo_filtrado:
#     conteudo = arquivo_filtrado.read()
#
# print(conteudo)

#5

# maior_numero = None
#
# with open('numeros_grandes.txt', 'r') as arquivo:
#     for linha in arquivo:
#         numero = int(linha.strip())
#         if maior_numero is None or numero > maior_numero:
#             maior_numero = numero
#
# with open('maior_numero.txt', 'w') as arquivo_maior:
#     arquivo_maior.write(f'Maior número encontrado: {maior_numero}\n')
#
# with open('maior_numero.txt', 'r') as arquivo_maior:
#     conteudo = arquivo_maior.read()
#
# print(conteudo)

#6

# with open('frutas.txt', 'r', encoding='utf-8') as arquivo:
#     frutas = arquivo.readlines()
#
# frutas = [fruta.strip() for fruta in frutas]
# frutas.sort()
#
# with open('frutas_ordenadas.txt', 'w') as arquivo_ordenado:
#     for fruta in frutas:
#         arquivo_ordenado.write(fruta + '\n')
#
# with open('frutas_ordenadas.txt', 'r') as arquivo_ordenado:
#     conteudo = arquivo_ordenado.read()
#
# print(conteudo)
#
#

#7

# with open('mensagem.txt', 'r') as arquivo:
#     conteudo = arquivo.read()
#
# palavras = conteudo.split()
# num_palavras = len(palavras)
#
# with open('contagem_palavras.txt', 'w') as arquivo_contagem:
#     arquivo_contagem.write(f'Número de palavras: {num_palavras}\n')
#
# with open('contagem_palavras.txt', 'r') as arquivo_contagem:
#     conteudo = arquivo_contagem.read()
#
# print(conteudo)

#8

# soma = 0
# contagem = 0
#
# with open('numeros.txt', 'r') as arquivo:
#     for linha in arquivo:
#         numero = float(linha.strip()) #pode dar número quebrado
#         soma += numero
#         contagem += 1
#
# media = soma / contagem if contagem > 0 else 0
#
# with open('media_numeros.txt', 'w') as arquivo_media:
#     arquivo_media.write(f'Média dos números: {media}\n')
#
# with open('media_numeros.txt', 'r') as arquivo_media:
#     conteudo = arquivo_media.read()
#
# print(conteudo)
#

#9

# with open('frutas.txt', 'r', encoding="utf-8") as arquivo:
#     frutas = arquivo.readlines()
#
# frutas = [fruta.strip() for fruta in frutas]
#
# frutas_unicas = list(dict.fromkeys(frutas))
#
# with open('frutas_unicas.txt', 'w') as arquivo_unicas:
#     for fruta in frutas_unicas:
#         arquivo_unicas.write(fruta + '\n')
#
# with open('frutas_unicas.txt', 'r') as arquivo_unicas:
#     conteudo = arquivo_unicas.read()
#
# print(conteudo)

#10

from datetime import datetime

data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

nova_entrada = input("Escreva entrada para o diário: ")

with open('diario.txt', 'a') as arquivo:
    arquivo.write(f"{data_hora_atual} - {nova_entrada}\n")

print("Nova entrada adicionada ao diário com sucesso! \n")

ver_conteudo = input("Deseja ver o conteúdo do diário? (sim/não): ").strip().lower()

if ver_conteudo == 'sim':

    with open('diario.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print("\nConteúdo do diário:")
        print(conteudo)
else:
    print("Programa encerrado.")


