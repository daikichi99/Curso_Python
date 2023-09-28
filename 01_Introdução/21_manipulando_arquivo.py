"""
Primeiro passo para leitura, é abrir o arquivo, para isto usamos
a função OPEN(nomeArquivo).
O parâmetro é o nome ou caminho do arquivo.

O arquivo deve existir, caso contrário retornará erro FileNotFound.

Open apenas abre o arquivo, para ler seu conteúdo é necessário usarmos
a função nomeArquivo.read()
Por padrão o Open abre com o parâmetro r(read)
"""

# criando um arquivo txt
# a -> adc w -> sub r -> leitura (pode ser suprimido)
# tratamento de erro

# Exercício de aula: criar um todo (lista de tarefas)
 # open() #  abre qualquer arquivo mas precisa fechar
# close()

# with opn NAO PRECISA FECHAR

with open('.\base\teste.txt', 'a', encoding='utf8') as arquivo: #onde tem 'a' pode ser w ou r
arquivo.write('ESTOU SO TESTANDO....)')
with open('./base/teste.txt', 'r', encoding='utf8') as arquivo:
    print(arquivo)
print(arquivo.read())



try:
        with open('comando Git.txt', 'r' , encoding='utf8') as arquivo:
                texto = arquivp.read()
        except FilenotFoundError:
            print


# Criar  umm to do (lista de tarefas
# 
with open('.\base\teste.txt', 'a', encoding='utf8') as arquivo:   #onde tem 'a' pode ser w ou r
arquivo.write('')


