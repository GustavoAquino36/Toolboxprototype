import os
import sys

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def backToMenu():
  input('Pressione qualquer botao para voltar ao menu inicial')

def quitou():
	clear()
	print('Obrigado por utilizar a Toolbox...')
	sys.exit()
