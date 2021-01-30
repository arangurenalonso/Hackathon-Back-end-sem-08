from Aconnection.conn import Connection


class editorial:
    def __init__(self):
        self.model = Connection('biblioteca')

    def get_all_editorial(self,condition={}, select={}):
        return self.model.get_all('editorial',condition,select)

    def insert_editorial(self, data):
        return self.model.insert('editorial',data)

    def update_editorial(self, condition, change):
        return self.model.update('editorial',condition, change)
    def delete_editorial(self,condition):
        return self .model.delete('editorial',condition)

    def get_all_validacion(self,condition={}):
        return self.model.get_all_validacion('editorial',condition)
