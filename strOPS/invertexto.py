from MenuFunctions import *

def invertexto():
  clear()
  invertexto = input('Texto a ser invertido: ')
  palavras = invertexto.split(' ')
  print(f'Seu texto: {invertexto}\nPalavras invertidas:', ' '.join(palavras[::-1]), f'\nTexto invertido: {invertexto[::-1]}')
  backToMenu()
  