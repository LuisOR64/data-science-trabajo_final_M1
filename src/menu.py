# LuisOR
from src.data import HEADERS
from src.utils import print_Tdec, print_dec
from src.decorators import clear_con

@clear_con()
def main_menu():
    print('''
          ==========SQL_PY==========
          (1)         Nuevo registro
          (2)      Imprimir registro
          (3)    Actualizar Registro
          (4)      Eliminar Registro
          (5)          Imprimir Todo   
          (C)         Cerrar Sistema
          ==========================''')
    
@clear_con()
def up_menu(key, item):
    print_Tdec(text="""¿Cómo desea realizar la actualización?""", num=40)
    print(f"""(1)       Actualizar RUC [{ key }]""")
    print(f"""(2)       Actualizar Razón Social [{ item[HEADERS[1]] }]""")
    print(f"""(3)       Actualizar Dirección [{ item[HEADERS[2]] }]""")
    print(f"""(4)       Actualizar Todo""")
    print(f"""(C)       Cerrar Transacción""")
    print_dec(text="", num=20)