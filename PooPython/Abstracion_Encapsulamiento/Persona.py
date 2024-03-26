class Persona:
    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.edad = 0
        self.direccion = ""

    def caminar():
        print("Estoy caminando...")

    def comer():
        print("Estoy comiendo...")

    def despertar():
        print("Buenos dias...")

    def presentarse(self):
        print("Me presento, mi nombre es {} y tengo {} anios".format(self.nombre, self.edad))
    
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre