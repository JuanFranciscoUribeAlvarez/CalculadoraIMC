#Calculadora de IMC
nombre = ""
while not nombre:
    nombre = input("Infrese su nombre(s) por favor: ")

apellidop = ""
while not apellidop:
    apellidop = input("Ingrese su apellido paterno por favor: ")
    
apellidom = ""
while not apellidom:
    apellidom = input("Ingrese su apellido materno por favor: ")

while True:
    try:
        edad = int(input("Ingrese su edad por favor: "))
    except ValueError:
        print("Debe ser un numero entero")
        continue
    break
while True:
    try:
        peso = float(input("Ingrese su peso (KG) por favor: "))
    except ValueError:
        print("Deebes de poner un valor con decimales")
        continue
    break
while True:
    try:
        estatura = float(input("Deme su estatura por favor: "))
    except ValueError:
        print("Lo siento debe ser un numero con decimales")
        continue
    break
IMC=peso/estatura**2
print("Nombre Completo: " + nombre + " " + apellidop + " " + apellidom + "\n" 
      + "Edad: " + str (edad) + "\n"
      + "Peso: " + str (peso) + "\n"
      + "Estatura: " + str (estatura) + "\n"
      + "Indice de Masa Corporal (IMC): " + str (IMC))



       


        
