import Persona
import Deportista

class Futbolista(Persona, Deportista):
    #Atributo clase
    Lista_Futbolistas = None

    #Iniciliazador y atributos
    def __init__(self, nombre, edad, altura, sexo, años_practicando, goles_marcados, tarjetas_rojas, pierna_habil):

        self.goles_marcados = goles_marcados
        self.tarjetas_rojas = tarjetas_rojas
        self.pierna_habil = pierna_habil

        Persona.init(self, nombre, edad, altura, sexo)
        Deportista.init(self, "Futbol", años_practicando)
        Futbolista.Lista_Futbolistas.append(self)

        #get y set

    def set_goles_marcados(self, goles_marcados):
        self.goles_marcados = goles_marcados

    def get_goles_marcados(self):
        return self.goles_marcados

    def set_tarjetas_rojas(self, tarjetas_rojas):
        self.tarjetas_rojas = tarjetas_rojas

    def get_tarjetas_rojas(self):
        return self.tarjetas_rojas

    def set_pierna_habil(self, pierna_habil):
        self.pierna_habil = pierna_habil

    def get_pierna_habil(self):
        return self.pierna_habil

    @classmethod
    def set_Lista_Futbolistas(cls, Lista_Futbolistas):
        cls.Lista_Futbolistas = Lista_Futbolistas

    @classmethod
    def get_Lista_Futbolistas(cls):
        return cls.Lista_Futbolistas

    #Metodo str()
    def str(self):
        return "Mi nombre es " + super().get_nombre() + " soy profesional en el deporte " + super().get_deporte() + "Tengo " + super().get_edad() + " años de edad y llevo " + super().get_años_practicando + "años en el deporte"
