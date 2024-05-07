# Declarar variables
nombre = ''
apellidoPaterno = ''
apellidoMaterno = ''
edad = 0.0
peso = 0.0
estatura = 0.0

# Pedir datos al usuario y validar que no esten vacios
while(len(nombre) <= 0) :
    nombre = input('Introduce tu nombre: ')
    if(len(nombre) <= 0) : print('No se puede dejar vacío el dato de nombre!')

while(len(apellidoPaterno) <= 0) :
    apellidoPaterno = input('Introduce tu apellido paterno: ')
    if(len(apellidoPaterno) <= 0) : print('No se puede dejar vacío el dato de apellido paterno!')

while(len(apellidoMaterno) <= 0) :
    apellidoMaterno = input('Introduce tu apellido materno: ')
    if(len(apellidoMaterno) <= 0) : print('No se puede dejar vacío el dato de apellido materno!')

while(edad <= 0) :
    try:
        edad = float(input('Introduce tu edad: '))
    except ValueError:
        print("Ingresa un dato numérico válido para la edad!")

while(peso <= 0) :
    try:
        peso = float(input('Introduce tu peso (kg): '))
    except ValueError:
        print("Ingresa un dato numérico válido para el peso!")

while(estatura <= 0) :
    try:
        estatura = float(input('Introduce tu estatura (m): '))
    except ValueError:
        print("Ingresa un dato numérico válido para la estatura!")

# Mostrar datos al usuario
imc = peso/(estatura**2)
print('Nombre: ' + nombre.capitalize())
print('Apellido paterno: ' + apellidoPaterno.capitalize())
print('Apellido materno: ' + apellidoMaterno.capitalize())
print('Edad: ' + str(edad) + ' años')
print('Peso: ' + str(peso) + 'kg')
print('Estatura: ' + str(estatura) + 'm')
print('Índice de masa corporal (IMC): ' + str(imc))

if imc < 18.9:
    print("Peso bajo")
elif (imc >=18.9 or imc <=24.9):
    print("Peso normal")
elif (imc >=25.0 or imc <=29.9):
    print("Sobrepeso")
elif (imc >=30.0 or imc <=34.9):
    print("Obesidad leve")
elif (imc >=35.0 or imc <=39.9):
    print("Obesidad media")
elif imc >40.0:
    print("Obesidad mórbida")