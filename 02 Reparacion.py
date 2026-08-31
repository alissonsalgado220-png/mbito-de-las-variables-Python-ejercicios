saldo = 200
def retirar(monto1):
    global saldo
    saldo = saldo - monto1
retirar(100)
print("El saldo final es de:", saldo)

def retirar2(saldo2, monto2):
    return saldo2 - monto2
saldo2 = retirar2(200, 100)
print("El saldo final es de:", saldo2)
#Creo que prefiero esta porque es mas 'facil' de usar y no confundirse debido a los parametros