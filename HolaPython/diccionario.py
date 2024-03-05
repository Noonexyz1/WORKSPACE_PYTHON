#Creacion de un diccionario
planet = {
    'name': 'Earth',
    'moons': 1
}


#Acceso al diccionario de datos
print(planet.get('name'))
# planet['name'] is identical to using planet.get('name')
print(planet['name'])
#cuando el atributo no existe
#wibble = planet.get('wibble') # Returns None
#wibble = planet['wibble'] # Throws KeyError


#Modificiacion de valores
planet.update({'name': 'Makemake'})
print(planet.get('name'))

planet['name'] = 'Makemake'
# No output: name is now set to Makemake.


#Cambio de valor a varios atributos
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

planet['name'] = 'Jupiter'
planet['moons'] = 79


#Adicion y eliminacion de claves
planet['orbital period'] = 4333
print(planet)
planet.pop('orbital period')    #para quitar clave
print(planet)

#Diccionarios dentro de otros diccionarios
# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}
print(planet)



#Recuperacion de todas las claves y valores
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
#Enfasis en el metodo .keys()
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')


#Determinar la existencia de una clave en un diccionario
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1
# Because december exists, the value will be 3.1
print(rainfall)


#Recuperacion de todos los valores
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter.')



