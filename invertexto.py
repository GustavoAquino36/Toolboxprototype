import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()
invertexto = input('Texto a ser invertido: ')
clear()
print(f'Seu texto: {invertexto}\nTexto invertido: {invertexto[::-1]}')