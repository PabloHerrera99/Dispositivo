class Dispositivo:

    def __init__(self, id=None, nombre=None, marca=None, tipo=None, diccionario=False):
       self.id = id
       self.nombre = nombre
       self.marca = marca
       self.tipo = tipo
       if diccionario:
            self.id = diccionario.get("id",self.id)
            self.nombre = diccionario.get("nombre", self.nombre)
            self.marca = diccionario.get("marca", self.marca)
            self.tipo = diccionario.get("tipo", self.tipo)

    def __repr__(self) -> str:
        if self.tipo == None:
            return f'{self.id} - {self.nombre} - {self.marca}'
        elif self.marca == None:
            return f'{self.id} - {self.nombre} - {self.tipo}'
        else:
            return f'{self.id} - {self.nombre} - {self.marca} - {self.tipo}'
       