list_num = [3,4,436,4,1,54]
def suma(list_num):
    valor = 0
    for i in list_num:
        valor += i
    return valor
print(suma(list_num))


def multp(list_num):
    valor = 1
    for i in list_num:
        valor *= i
    return valor
print(multp(list_num))
