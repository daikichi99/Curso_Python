""" # Sets
#set (conjuntos)
tupla1 = ()
tupla2 = tuple()

lista1 = []
lista2 = list()

dicionario1 = {}
dicionario2 = dict

conjunto1 = {'leo', 10, 10.4, True} # nao aceita valor repetido
conjunto2 = set()

numeros = {6,4,8,9,4,6,1,3,2,}
numeros.add(200) # para inserir novonumero


numeros.pop()#
numeros.discard(4)
numeros.discard(4)
numeros.remove(3)

"""
# Analise cidades (cada pessoa que entrou colocou a cidade de nascimento)
cidade = ['Rio de Janeiro', 'São Paulo', 'Juiz de Fora', 'Petrolina',
          'Salvador','Juiz de Fora', 'Rio de Janeiro', 'Petrolina',
          'Salvador', 'São Paulo', 'São Paulo', 'São Paulo',  'Juiz de Fora',
          'Rio de Janeiro', 'Petrolina', 'Rio de Janeiro', 'Salvador',
          'Juiz de Fora',  'Petrolina', 'Salvador', 'Rio de Janeiro',
          'Rio de Janeiro', 'Rio de Janeiro', 'Rio de Janeiro', 'São Paulo',
          'São Paulo', 'São Paulo', 'São Paulo', 'Rio de Janeiro',
          'Rio de Janeiro', 'Rio de Janeiro',  'São Paulo', 'Rio de Janeiro',
          'São Paulo', 'Rio de Janeiro', 'São Paulo']




print(f'total de pessoas: {len(cidade)}')

# quantas pessoas sao do rio de janeiro:

print(f'Total de pessoas do RJ:{cidade.count("Rio de Janeiro")}')
# de quantas cisdades recebi visita hoje
print(f'Quantidade de cidades: {len(set(cidade))}')
print(f'Cidades: {set(cidade)}')
#quantas pessoas sao do Rio de Janeiro
# precisamos saber quantas pessoas compareceram
# total
curso_python ={'Leo A', 'Maria', 'Juca', 'Paulo', 'Ana', 'Beto'}  }
curso_sql = {'Leo A', 'Pedro', 'Juca', 'Cris', Claudia', 'Robert'}

#total de alunos
print(f'QTD alunos PY : {len(curso_python)}')
print(f'QTDlen(curso_sql alunos SQL: {len(curso_sql)}')
# alunos matriculados nos dois cursos

print(f'total de alunos: {len(total_alunos1)}')
# alunos que estao em apenas um curso
so_python = curso_python.difference(curso_sql)
so_sql = curso_sql ^ curso_python


print((f'QTD alunos PY.......: {len(curso_python)}')
print((f'QTD alunos SQL....... {len(curso_sql)}')
print((f'QTD total de alunos . {len(total_alunos1)}')
print((f'QTD alunos nos 2 cursos... {len(ambos_cursos2)}')
print((f'QTD alunos  so PY.......: {len(so_python)}')
print((f'QTD alunos so SQL.......: {len(so_sql)}')

ambos_cursos1 = curso_python.intersetion(curso_sql)
ambos_cursos2 = curso_python & (curso_sql
                                
print(f'Alunos nos 2 cursos: {len(ambo)}')