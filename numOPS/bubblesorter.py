from MenuFunctions import *
from time import sleep

def bubblesorter():
  clear()
  num = input('Numeros a serem organizados: ')
  if num.isnumeric():
    qtd = len(num)-1
    num2 = []
    for i in range(len(num)):
      num2.append(int(num[i]))
    for j in range(qtd):
      for i in range(qtd):
        if num2[i] > num2[i+1]:
          num2[i], num2[i+1] = num2[i+1], num2[i]
    print(f'numeros organizados crescente: {num2}\nnumeros organizados decrescente: {num2[::-1]}')
    backToMenu()
  else:
    print('Favor inserir numeros inteiros')
    sleep(1)
    bubblesorter()
