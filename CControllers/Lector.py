from BModels.Lector import Lector
from DHelpers.menu import Menu
from DHelpers.validacion import validacion
import uuid

class Lector_Controllers:
    def __init__(self):
        self.lector = Lector() 
        self.salir = False
        self.validar=validacion()
        

    def menu(self):
        try:
            
            
            while True:
                print('''
                ==================
                    Menu Lector
                ==================
                ''')
                lista_menu = ["Mostrar Lista", "Agregar", "Modificar", "Eliminar", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    print("Bienvenido")
                    self.get_all_Lectores()
                
                elif respuesta == 2:
                    self.register_Lector()

                elif respuesta == 3:
                    self.update_lector()

                elif respuesta == 4:
                    self.delete_Lector
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def register_Lector(self):
        print('''
                ==================
                    CREAR CUENTA
                ==================
                ''')
         
        while True:
            Nombre = self.validar.valiar_ingreso_texto("Ingrese el nombre")
            Apellido=self.validar.valiar_ingreso_texto("Ingrese el apellidos")
            if not self.lector.get_all_Lector({'Nombre':Nombre, 'Apellido':Apellido}, { '_id':0, 'Nombre':1, 'Apellido':1, 'telefono':1, 'correo':1, 'direccion':1, 'carnet':1,}):
                    nombreva = Nombre
                    apellidova = Apellido

                    break
            else:
                print('Ha ingresado una combinación de Nombre y Apellido que ya existe')
                
                

        telefono = self.validar.validar_telefono("Ingrese un teléfono")
        correo=self.validar.validar_correo('Ingrese un correo')
        direccion=input('Ingrese una dirección')
        carnet= uuid.uuid4()
        
        
        return self.lector.insert_Lector({
        'Nombre': nombreva,
        'Apellido': apellidova,
        'telefono':telefono,
        'correo': correo,
        'direccion':direccion,
        'carnet':carnet
            
            })

        

        

    def get_all_Lectores(self):
        try:
            print('''
            ==========================
                Listar Lectores
            ==========================
            ''')
            usuarios = self.lector.get_all_Lector({
                
            },{
                '_id':0,
                'Nombre':1,
                'Apellido':1,
                'telefono':1,
                'correo':1,
                'direccion':1,
                'carnet':1,
                
            })
            print(self.validar.print_table(usuarios, ['Nombre', 'Apellido','Telefono','Correo','Direccion', 'Carnet']))
            return(usuarios[0]["_id"])
        except Exception as e:
            print(f'{str(e)}')

    def update_lector(self):
        try:
            print('''
                =========================
                    ACTUALIZAR LECTOR
                =========================
                ''')
            while True:
                carnet = input('Ingrese un código de Carnet')
                if (not self.validar.validar_existencia_campo_valor_Lector('carnet', carnet)):
                    print('Has ingresado un código de carnet que no existe')
                else:
                    condicion = {
                    'carnet': carnet,
                    }
                    break
            
            cambio = {}
            if self.validar.question('¿Deseas cambiar el nombre?'):
                
                Nombre = self.validar.valiar_ingreso_texto("Ingrese el nombre")
                cambio['Nombre']=Nombre
                        
            if self.validar.question('¿Deseas cambiar el apellido?'):
                apellido = self.validar.valiar_ingreso_texto("Ingrese el apellido")
                cambio['Apellido']=apellido
            
            if self.validar.question('¿Deseas cambiar el telefono?'):
                telefono = self.validar.validar_telefono("Ingrese el telefono")
                cambio['telefono']=telefono
                    
            if self.validar.question('¿Deseas actualizar el correo?'):
                correo= self.validar.validar_correo("Ingrese el correo")
                cambio['correo']=correo

            if self.validar.question('¿Deseas actualizar la direccion?'):
                direccion = self.validar.valiar_ingreso_texto("Ingrese la direccion")
                cambio['direccion']=direccion
        
            
            self.lector.update_Lector(condicion,cambio)
        
            print('''
            =========================
                Lector Actualizado
            =========================
            ''')
        except Exception as e:
            print(f'{str(e)}')

    def delete_Lector(self,carnet):
        print('''
            ======================
              ELIMINAR LECTOR
            ======================
            ''')
        carnet = input('Ingrese un código de Carnet')
        while True:
            if (not self.validar.validar_existencia_campo_valor_Lector('carnet', carnet)):
                print('Has ingresado un código de carnet que no existe')
            else:
                data = {
                'carnet': carnet,
                }
                break
            return self.lector.delete_Lector(data)  

            
       
        input('Presiona una tecla para continuar...')