"""
Cadastre 3 produtos no estoque, cada produto precisa ter:
- nome
- preço
- data e hora que foi cadastrado
- Nome do Funcionário

Em seguida, permita que os produtos sejam visualizados.
"""
from datetime import date
estoque = []

while True:
    menu = int(input('1| cadastrar\in2| visualizar\n3| sair\nopco:  ')
               
               match  menu:
                case1:
                    produto = dict(
                    nome_produto = str(input('nome:  ')).title
                    preco = float(input('preco:  R$  '))
                    nome_funciomario = str(input('Funcionario: '))
                    dt_cadastro = datetime.now().strtime("%d .%m.%Y | %H:%M'break ') # colocando no fotrmato portugues
                    )
                    estoque.append(produto) 

                case 2: # Vizualizar estoque
                    for i, p in estoque:  #for chave  VALOR
                        print(produto)
                ...
                 case3:

                    break]
                case _:
               

#    print('')

#for cont in range(3):
#    produto = dict(
#        nome = str(input('nome do produto:  ')),
#
#        preco = float(input(f'Preco do produto:  '))
#    estoque.append(produto)
#for produto in estoque:
#   for chave, valor in produto.items():
#    print(f'{chave} l {VALOR}') # ATENCAO ONDE TEM L DEVE SER AQUELA BARRA VERTICAL.
#PRINT()








