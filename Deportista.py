class Deportista:
    #atributos e inicializador
    def __init__(self, deporte, años_practicando):
        self.deporte = deporte
        self.años_practicando = años_practicando

    #set y get

    def set_deporte(self, deporte):
        self.deporte = deporte

    def get_deporte(self):
        return self.deporte
    
    def set_años_practicando(self, años_practicando):
        self.años_practicando = años_practicando

    def get_años_practicando(self):
        return self.años_practicando