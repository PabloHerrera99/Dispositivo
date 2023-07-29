from dispositivo import Dispositivo
class Database:
    def __init__(self, data) -> None:
        self.database = []
        dispos = data.get("dispositivos")
        for i in range(len(dispos)):
            self.database.append(Dispositivo(diccionario=dispos[i]))
    
    def delete_by_id(self, id):
        for i in range(len(self.database)):
            if id == self.database[i].id:
                del self.database[i]
                break
    def add_dispositivo(self, dispo=None, diccionario=False):
        if diccionario:
            self.database.append(Dispositivo(diccionario=diccionario))
        else:
            self.database.append(dispo)

