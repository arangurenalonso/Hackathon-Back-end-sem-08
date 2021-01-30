from Aconnection.conn import Connection


class Lector:
    def __init__(self):
        self.model = Connection('biblioteca')

    def get_all_Lector(self,condition={}, select={}):
        return self.model.get_all('Lector',condition,select)

    def insert_Lector(self, data):
        return self.model.insert('Lector',data)

    def update_Lector(self, condition, change):
        return self.model.update('Lector',condition, change)

    def delete_Lector(self, condition):
        return self.model.delete('Lector', condition)
        
    def get_all_validacion(self,condition={}):
        return self.model.get_all_validacion('Lector',condition)

