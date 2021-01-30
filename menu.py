
from CControllers.editorial import controller_editorial
from CControllers.Lector import Lector_Controllers
from CControllers.libro import controller_libro
from DHelpers.validacion import validacion
from DHelpers.menu import Menu
class app():
    def __init__(self):
        self.validar=validacion() 
    def menu(self):

        try:

            print('''
            ==========================
                  MENU PRINCIPAL
            ==========================
            ''')
            menu_principal = ["Editorial", "Libro","Lector", "Salir"]
            menu=Menu(menu_principal)
            respuesta = menu.show()
            if respuesta == 1:
                editorial = controller_editorial()
                editorial.menu()
                if editorial.salir:
                    self.menu()
            elif respuesta == 2:
                libro = controller_libro()
                libro.menu()
                if libro.salir:
                    self.menu()
            elif respuesta == 3:
                lector = Lector_Controllers()
                lector.menu()
                if lector.salir:
                    self.menu()


            print("\n Gracias por utilizar el sistema \n")
        except KeyboardInterrupt:
            print('\n Se interrumpio la aplicación')
        except Exception as e:
            print(f'{str(e)}')


iniciar=app()
iniciar.menu()