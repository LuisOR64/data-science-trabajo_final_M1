# LuisOR
from src.utils import *
from src.data import businesses, save_data, HEADERS
from src.menu import *
from src.decorators import clear_con, pause_con

@clear_con()
def up_operator(option, key, item):
    print_Tdec(text=f"""Actualización de datos""", num=50)
    if option == 1:
        
        ruc = data_control('Ingrese en nuevo RUC: ')
        businesses[ruc] = businesses.pop(key)
        key = ruc
        
    elif option == 2:
        
        businesses[key][f'{HEADERS[1]}'] = data_control('Ingrese la nueva Razón Social: ')
        
    elif option == 3:
        
        businesses[key][f'{HEADERS[2]}'] = data_control('Ingrese la nueva dirección: ')
        
    elif option == 4:
        
        ruc = data_control('Ingrese en nuevo RUC: ')
        businesses.pop(key)
        businesses[ruc] = { f'{HEADERS[1]}' : data_control('Ingrese la nueva Razón Social: '), f'{HEADERS[2]}': data_control('Ingrese la nueva dirección: ')}
        key = ruc
        item = businesses[key]
    
    print_Tdec(text='Se realizaó la actualización satisfactoriamente', num=50)
    pause() 
    return key, item

def update_menu(key, item):
    control = True
    
    while control == True:
        
        up_menu(key, item)
    
        option = str(input('Ingrese una opción: ')).rstrip()
    
        if option.isdigit() == False:
            if option.upper() == 'C':
                control = False
            else:
                print('Opción no válida')
        elif 1 <= int(option) <= 4:
            key, item = up_operator(int(option), key, item)
        else:
            print('Opción no válida')

@clear_con()
def operate(option):
    temp3 = ''
    if option == 1:
    
        print_Tdec(text=f"""Ingrese la información según de valla solicitando""", num=50)
        ruc = data_control('Ingrese el RUC: ')
        businesses[ruc] = { f'{HEADERS[1]}' : data_control('Ingrese la Razón Social: '), f'{HEADERS[2]}': data_control('Ingrese la dirección: ')}
        print(f"""Registro completo""")
        
    elif option == 2:
        
        print_Tdec(text=f"""Impresión de datos""", num=40)
        ruc = data_control('Escriba el RUC a consultar: ')
        print_item(ruc, businesses[ruc]) if businesses.get(ruc) else print_Tdec(num=40, text='No se encontro la información solicitada')
        
    elif option == 3:
        
        print_Tdec(text=f"""Actualización de datos""", num=33)
        temp2 = data_control('Escriba el RUC a Actualizar: ')
        temp3 = businesses.get(temp2)
        if temp3:
            update_menu(temp2, temp3)
        else:
            print('No se encontro la información solicitada')
        
    elif option == 4:
        
        print_Tdec(text=f"""Eliminación de datos""", num=33)
        item = businesses.pop(data_control('Escriba el RUC a eliminar: '), None)
        print('Se ha eliminado el registro') if item else print('No se encontro el registro solicitado')
        
    elif option == 5:
        
        print_Tdec(text=f"""Impresión de datos""", num=33)
        
        for index, (key, item) in enumerate(businesses.items()):
            print_dec(num=10, text=f"Registro Nº {index+1}")
            print_item(key, item)
            
        print_Ddec(num=40)

def menu():
    
    main_menu()
    option = str(input('Ingrese una opción: ')).rstrip()
    
    if option.isdigit() == False:
        if option.upper() == 'C':
            clear()
            save_data(businesses)
            exit()
        else:
            print('Opción no válida')
    elif 1 <= int(option) <= 5:
        operate(int(option))
    else:
        print('Opción no válida')
    
@pause_con()
def run():
    while True:
        menu()
        pause()
