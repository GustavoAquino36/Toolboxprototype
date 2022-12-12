from MenuFunctions import *

def removeDupes():
  clear()
  frase = str(input('Frase a ter letras repetidas removidas:\n'))
  letra = list(frase)
  unico = set(letra)
  ordem = sorted(unico)
  print(f'Essa frase contem as seguintes letras unicas:',' '.join(ordem),'\n(Ordem alfabetica aplicada)')
  backToMenu()
