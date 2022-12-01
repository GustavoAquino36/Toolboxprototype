import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def mainMenu():
    clear()
    print('''
-=-=-=-=-=- ****'s ToolBox -=-=-=-=-=-

1 - Inversor de Texto
x - 
x - 
    ''')
    choose = input('Selecione a ferramenta que gostaria de utilizar -> ')
    escolha(choose)

def escolha(escolha):
    if escolha == '1':
        invertexto()

def invertexto():
    clear()
    invertexto = input('Texto a ser invertido: ')
    palavras = invertexto.split(' ')
    print(f'Seu texto: {invertexto}\nPalavras invertidas:', ' '.join(palavras[::-1]), f'\nTexto invertido: {invertexto[::-1]}')
    input('Pressione qualquer botao para voltar ao menu inicial')

if __name__ == '__main__':
    while True:
        mainMenu()