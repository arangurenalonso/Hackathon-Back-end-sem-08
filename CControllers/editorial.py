from BModels.editorial import editorial
from DHelpers.validacion import validacion
from DHelpers.menu import Menu

class controller_editorial:
    def __init__(self):
        self.editorial = editorial()
        self.salir = False
        self.validar = validacion()
    
    def menu(self): 
        try:
            while True:
                print('''
                ==================
                  Menu Editorial
                ==================
                ''')
                lista_menu = ["Crear Editorial", "Mostrar Editorial","Mantenimiento Editorial", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.insert_editorial()
                elif respuesta == 2:
                    self.show_editorial()
                    pass
                elif respuesta == 3:
                    self.maintenance_editorial()
                    pass
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def insert_editorial(self):
        print('''
            ====================
                CREAR EDITORIAL
            ====================
            ''')
        Nombre_editorial = self.validar.valiar_ingreso_texto("Ingrese el nombre de la Editorial")
        data = {
            'nombre_editorial': Nombre_editorial
        }
        if self.validar.validar_existencia_campo_valor('nombre_editorial',Nombre_editorial,self.editorial):
            print("Editorial ya registrada")
        else:
            self.editorial.insert_editorial(data)

            print('''
            =========================
                EDITORIAL Creada
            =========================
            ''')
            editorial_creada=self.validar.validar_existencia_campo_valor('nombre_editorial',Nombre_editorial,self.editorial)
            print(self.validar.print_table(editorial_creada, ['ID', 'Nombre Editorial']))
        
            
        input('Presiona una tecla para continuar...')

    def show_editorial(self):
        try:
            condicion = {}
            seleccion = {
                '_id' : 1,
                'nombre_editorial': 1

            }    
            cates = self.editorial.get_all_editorial(condicion, seleccion)
            
            
            print('''
            =========================
                    EDITORIAL
            =========================
            ''')
            print(self.validar.print_table(cates, ['ID', 'Nombre Editorial']))
            input('Presiona una tecla para continuar...')

        except Exception as e:
            print(f'{str(e)}')
    
    def maintenance_editorial(self):
        try:
            print('''
                =====================
                    BUSCAR EDITORIAL
                =====================
                ''')
            Nombre_editorial = self.validar.valiar_ingreso_texto("Ingrese el nombre de la Editorial")
            editorial_buscada=self.validar.validar_existencia_campo_valor('nombre_editorial',Nombre_editorial,self.editorial)

            if editorial_buscada:
                print('''
            =========================
               EDITORIAL Encontrada
            =========================
            ''')
                print(self.validar.print_table(editorial_buscada, ['ID', 'Nombre Editorial']))
                if self.validar.question('¿Deseas dar mantenimiento a la editorial?'):
                    opciones = ['Editar', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    print(respuesta)
                    if respuesta == 1:
                        self.update_editorial(editorial_buscada["_id"])
                    elif respuesta == 2:
                        self.delete_editorial(editorial_buscada["_id"])
            else:
                print("No existe ninguna editorial ingresada con ese nombre")
            
        except Exception as e:
            print(f'{str(e)}')
        input('Presiona una tecla para continuar...')

    def delete_editorial(self,id_editorial):
        
        data = {
            '_id': id_editorial
        }
        self.editorial.delete_editorial(data)
        print('''
                =========================
                    EDITORIAL Eliminada
                =========================
                ''')
    def update_editorial(self, id_editorial):   
    
        print('''
            =========================
                ACTUALIZAR EDITORIAL
            =========================
            ''')
        Nombre_editorial = self.validar.valiar_ingreso_texto("Ingrese el nombre de la Editorial")

        condicion = {
            '_id': id_editorial
        }
        cambio = {
            'nombre_editorial': Nombre_editorial
        }
        self.editorial.update_editorial(condicion,cambio)
        


        print('''
        =========================
          Categoria Actualizada
        =========================
        ''')
