MONEDA = "C$"
IVA = 0.15

def agregar_producto(subtotal_actual, precio, cantidad):
    subtotal_actual = subtotal_actual + (precio * cantidad)
    return subtotal_actual

def calcular_valor_total(subtotal):
    total = subtotal + (subtotal * IVA)
    return total

def mostrar_inventario(subtotal_acumulado):
    total_con_iva = calcular_valor_total(subtotal_acumulado)
    print("El subtotal acumulado es:", MONEDA, subtotal_acumulado)
    print("El valor total con IVA es:", MONEDA, total_con_iva)

subtotal_inventario = 0
subtotal_inventario = agregar_producto(subtotal_inventario, 20, 5)   # Arroz (20 x 5)
subtotal_inventario = agregar_producto(subtotal_inventario, 30, 2)   # Frijoles (30 x 2)
mostrar_inventario(subtotal_inventario)