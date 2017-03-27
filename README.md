# Python

[![N|Solid](https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png)](https://nodesource.com/products/nsolid)

## Qué es Python

Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en una sintaxis que favorezca un código legible.
Se trata de un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional. Es un lenguaje interpretado, usa tipado dinámico y es multiplataforma.

Es administrado por la Python Software Foundation. Posee una licencia de código abierto, denominada Python Software Foundation License, que es compatible con la Licencia pública general de GNU a partir de la versión 2.1.1, e incompatible en ciertas versiones anteriores.

## Para qué se puede usar Python

- Web Programming: [Django](https://www.djangoproject.com/), [Pylons Project](http://pylonsproject.org/), [Bottle](http://bottlepy.org/docs/dev/), [Tornado](http://www.tornadoweb.org/en/stable/), [Flask](http://flask.pocoo.org/), [web2py](http://www.web2py.com/)

- GUI Development: [wxPython](https://www.wxpython.org/), [tkInter](https://wiki.python.org/moin/TkInter), [PyGtk](http://www.pygtk.org/), [PyQt](https://riverbankcomputing.com/software/pyqt/intro)

- Scientific and Numeric: [SciPy](http://www.scipy.org/), [Pandas](http://pandas.pydata.org/), [IPython](http://ipython.org/)

- Software Development: [Buildbot](http://buildbot.net/), [Trac](https://trac.edgewall.org/), [Roundup](http://roundup.sourceforge.net/)

- System Administration: [Ansible](https://www.ansible.com/), [Salt](https://saltstack.com/), [OpenStack](https://www.openstack.org/)

# Dónde se usa Python

Google utiliza Python para muchas tareas, incluyendo los backends de aplicaciones web como Google Groups, Gmail y Google Maps, así como de algunas de sus partes internas de motores de búsqueda.
La NASA está usando Python para implementar un sistema CAD / CAE repositorio / PDM y gestión de modelos, la integración, y el sistema de transformación que será el núcleo de la infraestructura para su próxima generación de entorno de ingeniería colaborativa. También es el lenguaje de desarrollo para OpenMDAO, un marco desarrollado por la NASA para la resolución de problemas de optimización de diseño multidisciplinarios.
Reddit fue originalmente escrito en Common Lisp, pero fue reescrito en Python en 2005.
Yahoo! Grupos utiliza Python "para mantener sus grupos de discusión".
YouTube utiliza Python "para producir características mantenibles en un tiempo récord, con un mínimo de desarrolladores".

### Instalación

En linux:
La mayoría de las dsitribuciones de Linux ya viene con Python instalado en su última versión.
Abrir una consola y escribir:
```sh
$ sudo apt-get install python
```
En Windows descargar de la [página oficial](https://www.python.org/downloads/) e instalar.


## Micro Tutorial de Python
---
####  Números

```
>>> 2+2
4
>>> (50-5*6)/4
5
>>> 216532163*8127321
1759826395525323
>>> 3*3.75/1.5
7.5
>>> (2+3j)*(8-4j)
(28+16j)
```
#### Cadenas
```
>>> 'Secuenciadecaracteres'
'Secuenciadecaracteres'
>>> "Hola"+"mundo"
'Holamundo'
>>> "Eco"*4
'EcoEcoEcoEco'
>>> saludo='Holamundo'
>>> saludo[0],saludo[-2]
('H','d')
>>> saludo[2:5]
'la'
```

### Listas
```
>>> a=[100,'huevos','sal']
>>> a
[100,'huevos','sal']
>>> a[0]
100
>>> a[-2:]
['huevos','sal']
>>> a+['oro',9]
[100,'huevos','sal','oro',9]
>>> a[0]="manteca"
>>> a
['manteca','huevos','sal']
```

### Conjuntos
```
>>> f=set("abracadabra")
>>> f
set(['a','r','b','c','d'])
>>> f&set(['a','e','i','o','u'])
set(['a'])
```

### Diccionarios
```
>>> dias={"Ene":31,"Jul":30}
>>> dias
{'Ene':31,'Jul':30}
>>> dias["Ene"]
31
>>> dias["Ago"]
>>> dias["Ago"]=31
>>> dias["Jul"]=31
>>> dias
{'Ago':31,'Ene':31,'Jul':31}
>>> "Mar"indias
False
>>> dias.keys()
['Ago','Ene','Jul']
>>> dias.values()
[31,31,31]
```
## Estructuras de Control
### Condicionales
```
>>> if <expression>:
... <suite>
elif <expression>:
... <suite>
else:
... <suite>
```
Una <expression> es algo que evalúa siempre a Verdadero o Falso.
Operadores lógicos: or,and,not.
Comparadores: <> == != inis.
Una <suite> es un bloque de código, de una o más líneas, delimitado por la sangría.

### while
```
while <expression>:
<suite>
```

### for
```
>>> bichos=["pulgas","piojos"]
>>> for bich in bichos:
... print "Mata-" + bich
...
Mata-pulgas
Mata-piojos
```
### List comprehensions
```
>>> vec=[3,7,12,0,3,-13,8]
>>> [x**2forxinvec]
[9,49,144,0,9,169,64]
>>> [x**2forxinvecifx<=7]
[9,49,0,9,169]
```

### Excepciones
```
>>> try:
...     5/0
... except ZeroDivisionError:
...     print “oops!”
oops!

try:
    <suite>
except [Excepcion1,...]:
    <suite>
finally:
    <suite>
else:
    <suite>
```

Si hay una excepción en la suite del try, se ejecuta la suite del except.
Si no hubo ninguna excepción, se ejecuta la suite del else. Y siempre se ejecuta la suite del finally.
```
>>> raiseValueError(“Ejemplo!”)
Traceback(mostrecentcalllast):
    File“<stdin>”,line1,in...
ValueError:Ejemplo!
```

### Funciones
```
>>> def alcuadrado(n):
... res=n**2
... returnres
...
>>> alcuadrado(3)
9
>>> def func(a,b=0,c=7):
... returna,b,c
...
>>> func(1)
(1,0,7)
>>> func(1,3)
(1,3,7)
>>> func(1,c=9)
(1,0,9)
>>> func(b=2,a=-3)
(-3,2,7)
```
### Clases
```
>>> import math

>>> classPosicion:
... def __init__(self,x,y):
... self.x=x
... self.y=y
... def distancia(self):
... x=self.x**2 + self.y**2
... return math.sqrt(x)
...
>>> p1=Posicion(3,4)
>>> p1.x
3
>>> p1.dist()
>>> p1.distancia()
>>> p1.distancia()
5.0
>>> p2=Posicion(7,9)
>>>
>>> p2.y
9
>>> p1.y
4
```

### Módulos

- Funciones, clases, y / o código suelto, todo es un archivo.
- Es un .py normal, sólo lo importamos y directamente lo usamos (Ej:import
math, math.sqrt(x))
- Fácil, rápido, ¡y funciona!

Armamos unos .py que contiene la clase definida arriba:

```
>>> importpos
>>> p=pos.Posicion(2,3)
>>> p.x
2
```

# El zen de Python

por Tim Peters

- Bello es mejor que feo.
- Explícito es mejor que implícito.
- Simple es mejor que complejo.
- Complejo es mejor que complicado.
- Plano es mejor que anidado.
- Disperso es mejor que denso.
- La legibilidad cuenta.
- Los casos especiales no son tan especiales como para quebrantar las reglas.
- Aunque lo práctico gana a la pureza.
- Los errores nunca deberían dejarse pasar silenciosamente.
- A menos que hayan sido silenciados explícitamente.
- Frente a la ambigüedad, rechaza la tentación de adivinar.
- Debería haber una ­y preferiblemente sólo una­ manera obvia de hacerlo.
- Aunque esa manera puede no ser obvia al principio a menos que usted sea holandés.
- Ahora es mejor que nunca.
- Aunque nunca es a menudo mejor que ya mismo.
- Si la implementación es difícil de explicar, es una mala idea.
- Si la implementación es fácil de explicar, puede que sea una buena idea.
- Los espacios de nombres (namespaces) son una gran idea ¡Hagamos más de esas cosas!

**La Fuente - Coducción del CEFI**
