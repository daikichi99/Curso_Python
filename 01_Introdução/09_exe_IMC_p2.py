"""
Agora vamos finalizar o IMC gerando uma saída
personalizada para o usuário de acordo com a
tabela:
______________________________________________
| Menor que 18.5      | Abaixo do peso       |
| Entre 18.5 - 24.9   | Peso Normal          |
| Entre 25.0 - 29.9   | Excesso de peso      |
| Entre 30.0 - 34.9   | Obesidade classe I   |
| Entre 35.0 - 39.9   | Obesidade classe II  |
| Maior ou igual 40.0 | Obesidade classe III |
----------------------------------------------

Mostre também a data deste resultado.
"""


nome = str(input('digite seu noma:  ' )).title
idade = int(input(f'{nome}, agora sua idade:  '))
peso = float INPUT('PESO:  '))
ALTURA = FLOAT(INPUT('ALTURA:  '))

IMC= FLOAT(PESO)

PRINT(TIME.LPCAÇTIME().TM_YEAR)
PRINT(TIME.LOCALTIME())



if (IMC >= 40.0): 
    print('Obesidade Classe III')
elif (IMC >= 35.0 and IMC < 40.0):
    print('Obesidade Classe II')
elif (IMC >=30 and IMC < 35.0):
    print('obesidade classe I')
elif (IMC >= 25.0 and IMV < 30.0):
    print('excesso de peso')
elif (IMC >= 18.5 and IMC < 25.0):
    print('peso normal')
elif (IMC < 18.5 and IMC > 0):
    print('abaixo do peso')
else: print('IMC invalido')



 



