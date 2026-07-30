#Reto 2

def calcular_metricas(horas_proyectos: list[float]) -> dict:
    total_horas = sum(horas_proyectos)
    num_proyectos = len(horas_proyectos)
    
    if num_proyectos == 0 or total_horas == 0:
        return {"total": 0.0, "promedio": 0.0, "porcentajes": []}

    promedio = total_horas / num_proyectos
    porcentajes = [(h / total_horas) * 100 for h in horas_proyectos]

    return {
        "total": total_horas,
        "promedio": promedio,
        "porcentajes": porcentajes
    }


def solicitar_horas(num_proyectos: int) -> list[float]:
    horas = []
    for i in range(1, num_proyectos + 1):
        while True:
            try:
                val = float(input(f"Horas para Proyecto {i}: "))
                if val < 0:
                    print("Las horas no pueden ser negativas.")
                    continue
                horas.append(val)
                break
            except ValueError:
                print("Entrada inválida. Ingrese un número.")
    return horas


def main():
    nombre = input("Nombre del desarrollador: ")
    try:
        num_proyectos = int(input("Cantidad de proyectos: "))
        if num_proyectos <= 0:
            return
    except ValueError:
        print("Cantidad no válida.")
        return

    horas = solicitar_horas(num_proyectos)
    metricas = calcular_metricas(horas)

    print(f"\nReporte: {nombre}")
    print(f"{'Proyecto':<12} {'Horas':<8} {'Porcentaje':<10}")
    for i, (h, p) in enumerate(zip(horas, metricas["porcentajes"]), 1):
        print(f"Proyecto {i:<3} {h:<8.1f} {p:.2f}%")

    print(f"Total: {metricas['total']:.1f}")
    print(f"Promedio: {metricas['promedio']:.2f}")


if __name__ == "__main__":
    main()


