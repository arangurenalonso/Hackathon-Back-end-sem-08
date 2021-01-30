from BModels.libro import libro
from DHelpers.validacion import validacion
from BModels.editorial import editorial
from DHelpers.menu import Menu
from BModels.prestamo import prestamo
from BModels.Lector import Lector

class controller_libro:
    def __init__(self):
        self.libro = libro()
        self.salir = False
        self.validar = validacion()
        self.editorial = editorial()
        self.lector = Lector() 
        self.prestamo=prestamo()
    
    def menu(self): 
        try:
            while True:
                print('''
                ==================
                  Menu LIBRO
                ==================
                ''')
                lista_menu = ["Crear Libro", "Mostrar Libro","Mantenimiento Libro","prestamo","devolucion", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.insert_libro()
                elif respuesta == 2:
                    self.show_libro()
                    pass
                elif respuesta == 3:
                    self.maintenance_libro()
                    pass
                elif respuesta == 4:
                    self.prestamo_libro()
                    pass
                elif respuesta == 5:
                    self.devolucion_libro()
                    pass
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def insert_libro(self):
        print('''
            ====================
                CREAR LIBRO
            ====================
            ''')
        Nombre_Libro = self.validar.valiar_ingreso_texto("Ingrese el nombre del libro")
        if self.validar.validar_existencia_campo_valor('nombre_libro',Nombre_Libro,self.libro):
            print("Libro ya registrada")
            return
        
        nombre_autor = self.validar.valiar_ingreso_texto("Ingrese el nombre del autor")

        while True:
            Nombre_editorial = self.validar.valiar_ingreso_texto("Ingrese de la editorial")
            if self.validar.validar_existencia_campo_valor('nombre_editorial',Nombre_editorial,self.editorial):
                break
            else:
                print(f'''
-------------------------------------------------------------------------------------
El nombre de la editorial '{Nombre_editorial}' no ha sido registrado en el sistema
    NOTA: Actualmente se encuentran registradas las siguientes editoriales''')
                try:    
                    cates = self.editorial.get_all_editorial({}, {
                        '_id' : 1,
                        'nombre_editorial': 1
                    })
                    print('''
                    ========================
                       EDITORIAL REGISTRADAS
                    =========================''')
                    print(self.validar.print_table(cates, ['ID', 'Nombre Editorial']))
                except Exception as e:
                    print(f'{str(e)}')
                
                if self.validar.question('¿Deseas ingresar alguna editorial registrada?'):
                     pass
                else:
                    return

        anolibro=self.validar.validar_ano('Ingrese el año del libro>')
        id_libro=self.validar.codigo_correlativo_libro('id_libro',self.libro)
        data = {
            'id_libro':id_libro,
            'nombre_libro': Nombre_Libro,
            'nombre_autor': nombre_autor,
            'nombre_editorial':Nombre_editorial,
            'año_libro':anolibro,
            'Estado':'disponible',
        }
    
        
        self.libro.insert_libro(data)
        print('''
        =========================
            Libro Creado
        =========================
        ''')
        libro_creado=self.validar.validar_existencia_campo_valor('id_libro',id_libro,self.libro)
        print(self.validar.print_table(libro_creado, ['ID', 'id_libro','nombre_libro','nombre_autor','nombre_editorial','año_libro','Estado']))
        input('Presiona una tecla para continuar...')

    def show_libro(self):
        try:
            
            condicion = {}
            seleccion = {
                '_id' : 0,
                'id_libro':1,
                'nombre_libro':1,
                'nombre_autor':1,
                'nombre_editorial': 1,
                'año_libro':1,
                'Estado':1
            }    
            cates = self.libro.get_all_libro(condicion, seleccion)
            
            
            print('''
            =========================
                    LIBROS
            =========================
            ''')
            print(self.validar.print_table(cates, ['ID', 'Nombre Editorial']))
            input('Presiona una tecla para continuar...')

        except Exception as e:
            print(f'{str(e)}')
    
    def maintenance_libro(self):
        try:
            print('''
                =====================
                    BUSCAR EDITORIAL
                =====================
                ''')
            Nombre_Libro = self.validar.valiar_ingreso_texto("Ingrese el nombre del libro")
            libro_buscado=self.validar.validar_existencia_campo_valor('nombre_libro',Nombre_Libro,self.libro)

            if libro_buscado:
                print('''
            =========================
               Libro Encontrado
            =========================
            ''')
            
                print(self.validar.print_table(libro_buscado, ['ID', 'id_libro','nombre_libro','nombre_autor','nombre_editorial','año_libro','Estado']))
            
                if self.validar.question('¿Deseas dar mantenimiento al libro?'):
                    opciones = ['Editar', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    print(respuesta)
                    if respuesta == 1:
                        self.update_libro(libro_buscado["id_libro"])
                    elif respuesta == 2:
                        self.delete_libro(libro_buscado["id_libro"])
            else:
                print("No se encuentra ningún libro con ese nombre")

        except Exception as e:
            print(f'{str(e)}')
        input('Presiona una tecla para continuar...')

    def delete_libro(self,id_libro):

        data = {
            'id_libro': id_libro
        }
        self.libro.delete_libro(data)
        print('''
                =========================
                    Libro Eliminada
                =========================
                ''')

    def update_libro(self, id_libro):   
     
        print('''
            =========================
                ACTUALIZAR EDITORIAL
            =========================
            ''')
        

        condicion = {
            'id_libro': id_libro
        }
        cambio = {}
        if self.validar.question('¿Deseas actualizar el nombre del Libro?'):
            Nombre_Libro = self.validar.valiar_ingreso_texto("Ingrese el nombre del libro")
            cambio['nombre_libro']=Nombre_Libro

        if self.validar.question('¿Deseas actualizar el nombre del Autor?'):
            nombre_autor = self.validar.valiar_ingreso_texto("Ingrese el nombre del autor")
            cambio['nombre_autor']=nombre_autor
        if self.validar.question('¿Deseas actualizar la Editorial?'):
            while True:
                Nombre_editorial = self.validar.valiar_ingreso_texto("Ingrese de la editorial")
                if self.validar.validar_existencia_campo_valor('nombre_editorial',Nombre_editorial,self.editorial):
                    cambio['nombre_editorial']=Nombre_editorial
                    break
                else:
                    print(f'''El nombre de la editorial '{Nombre_editorial}' no ha sido registrado en el sistema''')
        if self.validar.question('¿Deseas actualizar el año?'):
            anolibro=self.validar.validar_ano('Ingrese el año del libro>')
            cambio['año_libro']=anolibro
        
        self.libro.update_libro(condicion,cambio)



        print('''
        =========================
          Libro Actualizado
        =========================
        ''')

    def prestamo_libro(self):
        try:
            
            Nombre_Libro = self.validar.valiar_ingreso_texto("Ingrese el nombre del libro")
            libro_buscado=self.validar.validar_existencia_campo_valor('nombre_libro',Nombre_Libro,self.libro)

            if libro_buscado:
                if libro_buscado["Estado"]=="disponible":
                    print("El libro esta disponible")
                    if self.validar.question('Desea Prestar el libro?'):
                        fecha_devolucion=self.validar.validar_fecha_mayor_fecha_actual()
                        fecha_prestamo=self.validar.obtener_fecha()
                        id_libro=libro_buscado["id_libro"]
                        while True:
                            nombre_lector = self.validar.valiar_ingreso_texto("Ingrese el nombre del lector")
                            lector_buscado=self.validar.validar_existencia_campo_valor('Nombre',nombre_lector,self.lector)
                            if lector_buscado:
                                break
                            else:
                                print("El alumno no ha sido registrado")


                        data = {
                         'nombre_lector':nombre_lector,
                         'id_libro': id_libro,
                         'fecha_prestamo': fecha_prestamo,
                         'fecha_devolucion':fecha_devolucion,
                     }
    
        
                        self.prestamo.insert_prestamo(data)
                    
                    
                    #Cambiar estado del libro a prestado
                    condicion = {
                        'id_libro': libro_buscado["id_libro"]
                    }
                    cambio = {
                        'Estado':"prestado"
                    }
                    self.libro.update_libro(condicion,cambio)

                else:
                    print("El libro buscado esta prestado:")

            else:
                print("No se encuentra ningún libro con ese nombre")
        except Exception as e:
            print(f'{str(e)}')
        input('Presiona una tecla para continuar...')

    def devolucion_libro(self):
        try:
            
            Nombre_Libro = self.validar.valiar_ingreso_texto("Ingrese el nombre del libro")
            libro_buscado=self.validar.validar_existencia_campo_valor('nombre_libro',Nombre_Libro,self.libro)

            if libro_buscado:
                if libro_buscado["Estado"]=="prestado":
                    if self.validar.question('El libro esta siendo devuelto?'):
                        self.delete_prestamo(libro_buscado["id_libro"])
                        #Cambiar estado del libro a prestado
                        condicion = {
                            'id_libro': libro_buscado["id_libro"]
                        }
                        cambio = {
                            'Estado':"disponible"
                        }
                        self.libro.update_libro(condicion,cambio)

                else:
                    print("El libro se encuentra disponible para prestamo:")

            else:
                print("No se encuentra ningún libro con ese nombre")
        except Exception as e:
            print(f'{str(e)}')
        input('Presiona una tecla para continuar...')

    def delete_prestamo(self,id_libro):
        
        data = {
            'id_libro': id_libro
        }
        self.prestamo.delete_prestamo(data)
        print('El libro ha sido reingresado al sistema')
        input('Presiona una tecla para continuar...')
