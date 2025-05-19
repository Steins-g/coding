# Lista de ventas: cada venta es un diccionario
ventas = [
    {"fecha": "2024-01-01", "producto": "Laptop", "cantidad": 2, "precio": 1000.0},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 25.0},
    {"fecha": "2024-01-02", "producto": "Laptop", "cantidad": 1, "precio": 980.0},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 3, "precio": 45.5},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 4, "precio": 30.0},
    {"fecha": "2024-01-03", "producto": "Teclado", "cantidad": 1, "precio": 50.0}
]

# 1. Ingresos totales
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

# 2. Producto más vendido
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    ventas_por_producto[producto] = ventas_por_producto.get(producto, 0) + venta["cantidad"]

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]

# 3. Promedio de precio por producto
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    total_precio = venta["precio"] * venta["cantidad"]
    cantidad = venta["cantidad"]
    if producto not in precios_por_producto:
        precios_por_producto[producto] = [0, 0]  # [suma de precios totales, cantidad]
    precios_por_producto[producto][0] += total_precio
    precios_por_producto[producto][1] += cantidad

precio_promedio_por_producto = {
    producto: round(precio_total / cantidad, 2)
    for producto, (precio_total, cantidad) in precios_por_producto.items()
}

# 4. Ingresos por día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    ingresos_por_dia[fecha] = ingresos_por_dia.get(fecha, 0) + ingreso

# 5. Resumen de ventas por producto
resumen_ventas = {}
for producto in ventas_por_producto:
    cantidad_total = ventas_por_producto[producto]
    ingresos_totales_producto = precios_por_producto[producto][0]
    precio_promedio = precio_promedio_por_producto[producto]
    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": ingresos_totales_producto,
        "precio_promedio": precio_promedio
    }

# === RESULTADOS ===
print("📦 LISTA DE VENTAS:")
for v in ventas:
    print(v)

print("INGRESOS TOTALES:", ingresos_totales)

print(f"PRODUCTO MÁS VENDIDO: {producto_mas_vendido} ({cantidad_mas_vendida} unidades)")

print("PRECIO PROMEDIO POR PRODUCTO:")
for producto, promedio in precio_promedio_por_producto.items():
    print(f"{producto}: ${promedio}")

print("INGRESOS POR DÍA:")
for fecha, ingreso in ingresos_por_dia.items():
    print(f"{fecha}: ${ingreso}")

print("RESUMEN DE VENTAS:")
for producto, datos in resumen_ventas.items():
    print(f"{producto}:")
    for k, v in datos.items():
        print(f"  {k}: {v}")
