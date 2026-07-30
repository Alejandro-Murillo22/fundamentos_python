#Reto 2

def clasificar_unidad(cantidad: int) -> str:
    if cantidad == 0:
        return "Agotado - Reorden Inmediata"
    elif 1 <= cantidad <= 5:
        return "Crítico - Reposición Sugerida"
    return "Adecuado"


def procesar_inventario(stock: list[int]) -> dict:
    if not stock:
        return {
            "clasificaciones": [],
            "productos_agotados": [],
            "total_criticos": [],
            "porcentaje_disponibilidad": 0.0
        }

    clasificaciones = [clasificar_unidad(cant) for cant in stock]
    productos_agotados = [i for i, cant in enumerate(stock) if cant == 0]
    total_criticos = [cant for cant in stock if 1 <= cant <= 5]
    
    disponibles = len(stock) - len(productos_agotados)
    porcentaje_disponibilidad = (disponibles / len(stock)) * 100

    return {
        "clasificaciones": clasificaciones,
        "productos_agotados": productos_agotados,
        "total_criticos": total_criticos,
        "porcentaje_disponibilidad": porcentaje_disponibilidad
    }


def main():
    stock_inicial = [12, 0, 5, 23, 2, 0, 8]
    resultado = procesar_inventario(stock_inicial)

    for i, est in enumerate(resultado["clasificaciones"]):
        print(f"Índice {i}: {est}")

    print(f"productos_agotados: {resultado['productos_agotados']}")
    print(f"total_criticos: {resultado['total_criticos']}")
    print(f"Porcentaje de disponibilidad: {resultado['porcentaje_disponibilidad']:.2f}%")


if __name__ == "__main__":
    main()