# LuisOR
from src.data import HEADERS

def clear():
    print("\033c", end="")
    
def pause():
    input("Presione cualquier tecla para continuar...")

def end():
    exit()
    
def print_dec(num = 10, text = ""):
    print(str('=' * num) + str(text).strip() + str('=' * num))

def print_Tdec(num = 10, text = ''):
    print('=' * num)
    print(f'''{text}''')
    print('=' * num)

def print_Udec(num = 10, text = ''):
    print('=' * num)
    print(f'''{text}''')
    
def print_Ddec(num = 10, text = ''):
    print(f'''{text}''')
    print('=' * num)

def data_control(mesage):
    response = ''
    cont = 0
    while response.rstrip() == '':
        if cont > 0:
            clear()
            print('¡Debe ingresar la información solicitada!')
        response = str(input(mesage))
        cont += 1
    return response 


def print_item(key, item):
    print(f'''RUC: {key}''')
    print(f'''Razón Social: {item[HEADERS[1]]}''')
    print(f'''Dirección: {item[HEADERS[2]]}''')