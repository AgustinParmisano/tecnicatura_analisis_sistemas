1- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

2- Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

3- Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

5- Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

6- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:

****
*********
*******

11- Definir una función llamada palindromo() que tome una palabra y retorne 1 si la misma es palíndromo o 0 si no es lo es. Imprima "La palabra %s es palíndromo" y lo contrario dependiendo el caso.

12- Definir una función que reciba una lista de números de cualquier longitud. La función deberá retornar la lista de número en orden invertido.

13- Definir una función que reciba dos datos de teclado difentes numéricos y un dato de tipo string de cualquier tamaño. La función deberá almacenar los dos datos numéricos en una tupla y generar un diccionario donde la clave sea la letra y el valor la tupla generada anteriormente. Al finaliza retorne el diccionario.

14- Definir una función que reciba como parámetro una cadena de carácteres de cualquier tamaño y una letra y retorne las posiciones de la cadena donde encontró esa letra en una lista. Deberá retornar -1 en caso de no encontrar la letra en la cadena.

15- Definir una función que reciba una lista de carácteres y una lista de enteros y retorne otra cadena con las letras mismas de la cadena en las poiciones que indiquen la lista de enteros y el resto de las letras suplantarlas con "_ "  

BONUS1: Realizar el juego del ahorcado:
- Deberá definir una función juego donde:
	- Se defina una variable vidas = 10 y una variable ganó = False.
	- Se solicite una sola vez que se ingrese una palabra por teclado y se almacene en una variable.
	- Se haga un loop que sólo termine si la variable vidas = 0 o si la variable gano = True.
	- Dentro del loop se debe solicitar por teclado sólo 1 letra, de ingresar menos a mas letras deberá informar del error y restar 1 a la variable vidas.
	- Se deberá recorrer la palabra ingresado por teclado e inspeccionar que el caracter ingresado se encuentre en la palabra.
	- De estar presente en la palabra la letra se deberá devolver la palabra con esa o esas letras descubiertas y el resto cubiertas con "_ "
	- De no estar presente la letra en la palabra deberá restar 1 a la variable vida.
	- Si la palabra resulta totalmente descubierta se deberá poner la varibale gano en True

