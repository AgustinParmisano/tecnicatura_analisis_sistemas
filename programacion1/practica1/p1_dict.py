persona=["jorge","peralta",34256643,1987,0]
clave_personal=persona[2] * persona[-2]
usuario ={"nombre":"jorge","apellido":"peralta","dni":persona[2],"nac":persona[3],"pgp":clave_personal}

casera=(persona[-1],"hola123")
usuario["pgp_casera"]=casera
print (usuario)
print (usuario["pgp_casera"][1])
