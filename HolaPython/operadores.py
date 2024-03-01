#division entera con modulos
seconds = 1042
display_minutes = 1042 // 60
display_seconds = 1042 % 60

print(display_minutes)
print(display_seconds)

#orden de las operaciones
#Paréntesis
#Exponentes
#Multiplicación y división
#Suma y resta
result_1 = 1032 + 26 * 2
print(result_1)
result_2 = 1032 + (26 * 2)
print(result_2)


#cadenas a numeros
demo_int = int('215')
print(demo_int) #Si usa un valor no válido para int o float, recibirá un error.

demo_float = float('215.3')
print(demo_float)   #Si usa un valor no válido para int o float, recibirá un error.

#numeros absolutos, osea sin signos
print(abs(39 - 16))
print(abs(16 - 39))

#redondeo
print(round(1.4))
print(round(1.5))
print(round(2.5))
print(round(2.6))


#redondeando usando bibliotecas
from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)



