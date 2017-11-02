# Estación Meteorológica

Cosas que falta hacer:

## Base de Datos:

- Separar el código del generador de datos (configurador y seteador de variables) del alertador.
- Hacer que lo configurado se guarde en un archivo llamado meteo_vars.conf.
- Hacer un generador de datos random que lea del archivo meteo_vars.conf los valores a generar.
- Hacer que el generador genere datos random para cada variable de meteo_vars.conf.
- Hacer que el generador guarde linea a linea los diccionarios generados con los datos random.

## Alertas:

- Hacer que el alertador corra aparte y cada 1 segundo lea el archivo donde se guardan los datos generados.
- Hacer que el alertador lea los topes del archivo meteo_vars.conf.
- Hacer que el alertador compare la fecha actual con la de los datos del archivo de datos y con las variables de alerta de meteo_vars.conf e imprima las alertas.

