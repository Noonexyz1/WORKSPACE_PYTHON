#mi primera lista
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

planets[3] = "Planeta Rojo"
print("Marte tambien es conocido por: ", planets[3])
print(planets)

#para saber la longitud de un arreglo
numero_de_planetas = len(planets)
print("Hay " + str(numero_de_planetas) + " planetas en el sistema solar")

#agregar nuevos valores en la lista
planets.append("Pluton")
print(planets)

#eliminar el ultimo valor de la lista
planets.pop()   # Goodbye, Pluto
print(planets)

#Interesante:  Los índices negativos comienzan al final de la lista y van hacia atrás.
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

#busquedas de valores en una lista, encontrar el indice y mostrarlo al user con +1
jupiter_index = planets.index("Jupiter")
print("El planeta Jupiter es el", jupiter_index + 1, "planeta")

#uso de min y max
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 12650 # in Newtons, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "N")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "N")

#segmentacion de listas
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2] #esta es la segmentacion
print(planets_before_earth)

planets_after_earth = planets[3:8]
print(planets_after_earth)

planets_after_earth = planets[3:]   #asume que va hasta el final
print(planets_after_earth)

#unir dos listas con +
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons   #La unión de listas crean una lista nueva. No modifica la lista actual.
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

#ordenamiento de listas: El uso de sort modifica la lista actual.
regular_satellite_moons.sort(reverse = False)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
