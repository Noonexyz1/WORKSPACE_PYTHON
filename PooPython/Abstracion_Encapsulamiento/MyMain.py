from Persona import Persona

persona1 = Persona()
persona1.presentarse()

persona1.set_nombre("Diego")
nombre1 = persona1.get_nombre()
print(nombre1)

persona1.presentarse()


persona2 = persona1
persona2.set_nombre("Carlos")

persona1.presentarse()
persona2.presentarse()
