from Aconnection.conn import Connection


class prestamo:
    def __init__(self):
        self.model = Connection('biblioteca')

    def get_all_prestamo(self,condition={}, select={}):
        return self.model.get_all('prestamo',condition,select)

    def insert_prestamo(self, data):
        return self.model.insert('prestamo',data)

    def update_prestamo(self, condition, change):
        return self.model.update('prestamo',condition, change)

    def delete_prestamo(self,condition):
        return self .model.delete('prestamo',condition)

    def get_all_validacion(self,condition={}):
        return self.model.get_all_validacion('prestamo',condition)
