#Crear un programa que calcule y obtenga el total a pagar por un producto determinado.
#Se debera de solicitar el nombre o descripcion del producto, codigo del producto,
#Cantidad del producto, precio unitario. El total a pagar incliye el iva y el descuento.
#Si se compran de uno a 5 productos se otorga el 10% de descuento. Si se compran de 6 a 10 se otorga el 15% de descuento
#Y si se compran más de 10 se otorga un 20% de descuento

nombre_producto = input("Ingrese el nombre del producto: ")
codigo_producto = input("Ingrese el código del producto: ")
cantidad = int(input("Ingrese la cantidad del producto: "))
precio_unitario = float(input("Ingrese el precio unitario del producto: "))
    
    # Definir el porcentaje de IVA
IVA = 0.16
    
    # Calcular el descuento basado en la cantidad
if 1 <= cantidad <= 5:
        descuento = 0.10
elif 6 <= cantidad <= 10:
        descuento = 0.15
elif cantidad > 10:
        descuento = 0.20
else:
        descuento = 0

subtotal = cantidad * precio_unitario
monto_descuento = subtotal * descuento
subtotal_Descuento = subtotal - monto_descuento
    
monto_iva = subtotal_Descuento * IVA
    
total_Pagar = subtotal_Descuento + monto_iva
    
    # Mostrar los resultados
print("\n")
print("Detalles del producto:")
print(f"Nombre del producto: {nombre_producto}")
print(f"Código: {codigo_producto}")
print(f"Cantidad: {cantidad}")
print(f"Precio unitario: ${precio_unitario:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento aplicado: {descuento*100}%")
print(f"Monto de descuento: ${monto_descuento:.2f}")
print(f"Subtotal con descuento: ${subtotal_Descuento:.2f}")
print(f"IVA (16%): ${monto_iva:.2f}")
print(f"Total a pagar: ${total_Pagar:.2f}")