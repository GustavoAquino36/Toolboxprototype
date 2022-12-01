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

def mainMenu():
  clear()
  print('''
-=-=-=-=-=- ****'s ToolBox -=-=-=-=-=-

1 - Inversor de Texto
2 - Organizador de numeros em sequencia
x - 
x - 
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

def invertexto():
  clear()
  invertexto = input('Texto a ser invertido: ')
  palavras = invertexto.split(' ')
  print(f'Seu texto: {invertexto}\nPalavras invertidas:', ' '.join(palavras[::-1]), f'\nTexto invertido: {invertexto[::-1]}')
  backToMenu()

def bubblesorter():
  clear()
  num = input('Numeros a serem organizados: ')
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

if __name__ == '__main__':
  while True:
    mainMenu()