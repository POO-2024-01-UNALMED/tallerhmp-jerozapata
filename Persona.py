
class Persona:

    #Atributos e inicializador
    def __init__(self, nombre, edad, altura, sexo):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.sexo = sexo

    #get y set
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre
    
    def set_edad(self, edad):
        self.edad = edad

    def get_edad(self):
        return self.edad
    
    def set_altura(self, altura):
        self.altura = altura

    def get_altura(self):
        return self.altura
    
    def set_sexo(self, sexo):
        self.sexo = sexo
        
    def get_sexo(self):
        return self.sexo
