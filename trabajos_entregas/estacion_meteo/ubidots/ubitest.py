from ubidots import ApiClient

mi_token = '' # id del token que del cliente ubidots

api = ApiClient(token=mi_token)

mi_variable = '' # id de la variable del device de ubidots

variable = api.get_variable(mi_variable)


valor = '10' # el valor que deseamos enviarle a la variable de ubidots
nuevo_valor = mi_variable.save_value({'value':valor})
