from MenuFunctions import *
from numOPS.bubblesorter import *
from strOPS.invertexto import *
from strOPS.nondupes import *
from numOPS.highNumber import *

def mainMenu():
  clear()
  print('''
-=-=-=-=-=- ****'s ToolBox -=-=-=-=-=-

1 - Inversor de Texto
2 - Organizador de numeros inteiros em sequencia
3 - Letras unicas em uma frase
4 - Maior numero em uma lista
0 - Fechar toolbox
    ''')
  choose = input('Selecione a ferramenta que gostaria de utilizar -> ')
  escolha(choose)

def escolha(escolha):
  if escolha == '0':
    quitou()
  elif escolha == '1':
    invertexto()
  elif escolha == '2':
    bubblesorter()
  elif escolha == '3':
    removeDupes()
  elif escolha == '4':
    highNumber()

if __name__ == '__main__':
  while True:
    mainMenu()