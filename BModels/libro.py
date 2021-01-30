from Aconnection.conn import Connection


class libro:
    def __init__(self):
        self.model = Connection('biblioteca')

    def get_all_libro(self,condition={}, select={}):
        return self.model.get_all('libro',condition,select)

    def insert_libro(self, data):
        return self.model.insert('libro',data)

    def update_libro(self, condition, change):
        return self.model.update('libro',condition, change)

    def delete_libro(self,condition):
        return self .model.delete('libro',condition)

    def get_all_validacion(self,condition={}):
        return self.model.get_all_validacion('libro',condition)
