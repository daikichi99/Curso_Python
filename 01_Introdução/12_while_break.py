"""
While com Break
while True: >>> este laço será executado enquanto 
não encontrar o Break pelo caminho.
Break >>> Condição de parada de um loop. (FLAG)
"""
# sintaxe
# Validando tipo de dado com break


qtd_notas = 1
soma_notas = 0
while qtd_notas <= 4:
   nota = float(input(f'Digite a {qtd_notas} enezima nota: '))
   if nota >= 0 and nota <= 10:
     qtd_notas += 1
     soma_notas += nota
    else:
        print('nota invalida... digite novamente..')
      
media = round(soma_notas / qtd_notas +1, 1)
print(f'media: {round(soma_notas / qtd_notas, 1)}')




while True:
   menu = int(input('[1]SOMAR\n[2]SUNTRAIR\n[3]SAIR\nOpcao:  '))



