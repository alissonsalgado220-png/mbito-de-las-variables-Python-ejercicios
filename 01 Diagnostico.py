TASA_CAMBIO = 36.6
def a_dolares(cordobas):
    dolares= cordobas/TASA_CAMBIO
    return dolares
a_dolares(732)
print("La conversion de cordobas a dolares es de: ", dolares)
# El error que da es "NameError: name 'dolares' is not defined"

