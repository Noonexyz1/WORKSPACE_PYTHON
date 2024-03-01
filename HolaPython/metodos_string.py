#para letra capital
print("temperaturas y hechos sobre la luna".title())

heading = "temperaturas y hechos sobre la luna"
heading_upper = heading.title()
print(heading_upper)

#division de una cadena
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()    #comvierte la oracion en un vector de palabras
print(temperatures_list)

temperatures = "Daylight: 260 F\n Nighttime: -280 F"    #tomando en cuenta \n como separador de palabras
temperatures_list = temperatures.split('\n')
print(temperatures_list)

#busqueda de una cadena
print("Moon" in "This text will describe facts and challenges with space travel")   #devuelve FALSO
print("Moon" in "This text will describe facts about the Moon") #devuelve VERDADERO

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))    #devuelve -1 porque no hay Moon en la cadena

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))    #devuelve 64, 64 es la posición donde "Mars" aparece en la cadena.

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))   #devuelve el numero de repeticiones con Mars
print(temperatures.count("Moon"))   #devuelve el numero de repeticiones con Moon

print("The Moon And The Earth".lower()) #para distingir quitar letra capital
print("The Moon And The Earth".upper()) #para hacer todo mayusacula


#comprobacion de contenido
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])
print(parts[-2])

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():    #Como sucede con el método .isnumeric(), .isdecimal() puede buscar cadenas que parezcan decimales.
        print(item)


print("-60".startswith('-'))    #retorna true

if "30 C".endswith("C"):        #retorna true
    print("This temperature is in Celsius")

#reemplazando cadenas
print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text)   #es FALSO
text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower())   #Es VERDAD, normalizar la cadena para minusculas, para que no haya confuciones

#para unir cadenas
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))

#dar formato en cadenas %s, lo remplaza usando %
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)

print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))


mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))

mass_percentage = "1/6"
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))

mass_percentage = "1/6"
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))



subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)

