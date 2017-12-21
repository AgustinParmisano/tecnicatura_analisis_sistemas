num1 = input('Ingrese el numero 1 ')

num2 = input('Ingrese el numero 2 ')

num3 = input('Ingrese el numero 3 ')

def multiplicacion(num1,num2,num3):
    
    resultado = num1 * num2

    if(num3 > num1):
        print('El numero %s es mayor a %s' %(num3,num1))

    elif(num3 < num1):
        print('El numero %s es menor a %s' %(num3,num1))
    else:
        print('El numero %s es igual a %s' %(num3,num1))

    return resultado


valor = multiplicacion(num1,num2,num3)


def comparacion(valor,num3):
    if(num3 > valor):
        print('El numero %s es mayor al producto = %s' %(num3,valor))
    elif (num3 < valor):
        print('El numero %s es menor al producto = %s' %(num3,valor))
    else:
        print('El numero %s es igual al producto = %s' %(num3,valor))

comparacion(valor,num3)
