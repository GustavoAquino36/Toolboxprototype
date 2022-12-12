from MenuFunctions import *
from time import sleep

def highNumber():
  clear()
  try:
    numeros = list(map(int, input('Inserir lista de numeros separados por virgula: (ex: 1, 2)\n').strip().split(',')))
    print(f'O maior numero da lista acima é: {max(numeros)}')
    backToMenu()
  except ValueError:
    print('Favor inserir apenas numeros e virgulas! (ex: 1, 2)')
    sleep(1.5)
    highNumber()
  
