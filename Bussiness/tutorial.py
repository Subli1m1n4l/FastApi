#frameworks para el desarrollo de software:
# python,java,c++,ruby,goland,.net framework,.net core 3.1 superiores que son .net 6 
#algunos de frameworks son creados por microsoft creo .net 
# java oracle
# python ciencia de datos IA 

#variables c# decimal,float,double
# variables --> int, string(str),Boolean, number,.
# Clases.
# Objetos (listas,instancias de clases,tuplas,diccionarios).

# operadores logicos  > < >= <= !=
# operadores matematicos  + - / *

import infoTeams as teams


edad=16

nombre='Giovanny'




apellido:str='Pineda'
# #mostrar edad
# print(edad)
# #mostrar nombre
# print(nombre)
# #mostrar apellido
# print(apellido)

# print(type(teams.equipos_futbol))

# operaciones numericas

x=edad + 10
#print(f'edad sumada:{x}')

x=edad * 2

#print(f'edad multiplicada:{x}')

x=edad -5

#print(f'edad restada:{x}')

x=edad / 2

#print(f'edad dividida:{x}')

x=edad % 2

#print(f'edad es primo si es igual a 0 si no no es primo:{x}')

# operaciones con strings

nombre_total= nombre + apellido
#print(nombre_total)

#print("su nombre es :",nombre,apellido)

#print(f'el nombre de mi compañero es {nombre} y el apellido es {apellido} para tener un nombre total {nombre_total}')

x=len(nombre_total)
#print(x)

## ciclos

# for equipos in teams.equipos_futbol:
#     print(equipos)

# iterable=[78,99,88,54,55,44,11,22,9]
# print(iterable)
# x=0
# while x < len(iterable):
#     print(iterable[x],x)
#     x = x +1

# for item in iterable:
#     print(item)
  

# for equipo in teams.equipos_futbol:
#     print(equipo['nombre'])


persona={
    'nombre':'Johan',
    'edad':29,
    'Sexo':'M',
    'Altura':1.73,
    'Peso':79,
    'id':1254521,
    'telefono':45545
}

# print(persona['Peso']+ persona['Altura'])
# print(persona['id'])
# print(persona['nombre'])
# print(persona['Altura'])

# keys= persona.keys()

# for key in keys:
#     print(key)

# Condicionales 

# x =5
# y = 2

# if x == y:
#     print('x es igual a y')
# elif x < y:
#     print('x es menor que y')
# elif x > y:
#     print('x es mayor que  y')
# else:
#     print('x no cumple las condiciones')


# if x != y:
#     print('x es diferente de y')


# if x < y and x != y:
#     print('x es menor a y y es difernte de y')

# if x !=10:
#     print('x es diferente a 10')

value1=True
Value2=True
Value3=False

# if value1 and Value2:
#     print(True)

# if value1 and Value3:
#     print(False)

# if Value3 and value1:
#     print(False)

# if Value3 and Value3:
#     print(False)

if value1 or Value2:
    print(True)

if value1 or Value3:
    print(False)

if Value3 or value1:
    print(False)

if Value3 or Value3:
    print(False)