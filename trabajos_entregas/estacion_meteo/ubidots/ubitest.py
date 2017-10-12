from ubidots import ApiClient
import random
import time

mi_token = 'A1E-23UQYfbsc0yT8Bg3jzYntlvaBYiIDF' # id del token que del cliente ubidots

api = ApiClient(token=mi_token)

id_variable = '59df9065c03f971fb1aea2ea' # id de la variable del device de ubidots: temperatura mauro: 59df9065c03f971fb1aea2ea

obj_variable = api.get_variable(id_variable)

while True:
	valor = random.randint(0,101) # el valor que deseamos enviarle a la variable de ubidots
	nuevo_valor = obj_variable.save_value({'value':valor})
	time.sleep(5)
	print "Enviando dato: " + str(valor)
