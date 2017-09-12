#while con diccionarios 

salir = False
lista_personas = []

while not salir:
    persona = {}
    persona["nombre"] = raw_input("Ingrese nombre: ")
    persona["apellido"] = raw_input("Ingrese apellido: ")
    persona["edad"] = input("Ingrese nombre: ")
    lista_personas.append(persona)
    print("Persona Agregada")
    salir = input("Terminar:1, Continuar:0 ")
print("Lista de Personas Agregadas:")
print(lista_personas)
print lista_personas[2]["nombre"]