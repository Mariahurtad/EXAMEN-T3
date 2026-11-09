

import argparse
import math
import random


def estimar_area(a, b, c, d, cantidad, semilla=None):
    """Muestrea el rectángulo y usa la proporción respecto de la elipse."""
    if any(not math.isfinite(v) or v <= 0 for v in (a, b, c, d)):
        raise ValueError("a, b, c y d deben ser números positivos y finitos.")
    if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
        raise ValueError("La cantidad debe ser un entero positivo.")

    generador = random.Random(semilla)
    dentro_elipse = 0
    interseccion = 0
    for _ in range(cantidad):
        x = generador.uniform(-a, a)
        y = generador.uniform(-b, b)
        if (x / a) ** 2 + (y / b) ** 2 <= 1:
            dentro_elipse += 1
            if (x / c) ** 2 - (y / d) ** 2 >= 1:
                interseccion += 1

    area_elipse = math.pi * a * b
    area = area_elipse * interseccion / dentro_elipse if dentro_elipse else None
    return dentro_elipse, interseccion, area_elipse, area


def mostrar_resultado(a, b, c, d, cantidad, semilla=None):
    dentro, interseccion, area_elipse, area = estimar_area(
        a, b, c, d, cantidad, semilla
    )
    print(f"a={a:g}, b={b:g}, c={c:g}, d={d:g}; cantidad={cantidad}")
    print(f"Puntos dentro de la elipse: {dentro}")
    print(f"Puntos en la intersección: {interseccion}")
    print(f"Área de la elipse: {area_elipse:.6f}")
    if area is None:
        print("No hubo puntos en la elipse. Repita con más puntos.")
    else:
        print(f"Área aproximada de la intersección: {area:.6f} unidades cuadradas")
        print(f"Proporción de la elipse: {interseccion / dentro:.4%}")


def leer_positivo(nombre, entero=False):
    while True:
        try:
            texto = input(f"Ingrese {nombre}: ").strip().replace(",", ".")
            valor = int(texto) if entero else float(texto)
            if valor > 0 and (entero or math.isfinite(valor)):
                return valor
        except ValueError:
            pass
        print("Ingrese un entero positivo." if entero else "Ingrese un número positivo y finito.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pruebas", action="store_true", help="Ejecutar los tres casos del enunciado")
    parser.add_argument("--semilla", type=int, default=None, help="Semilla opcional para reproducir resultados")
    argumentos = parser.parse_args()
    if argumentos.pruebas:
        for a, b, c, d, cantidad in (
            (10, 5, 4, 4, 1000),
            (12, 7, 5, 4, 10000),
            (10, 5, 4, 4, 100000),
        ):
            mostrar_resultado(a, b, c, d, cantidad, argumentos.semilla)
            print()
    else:
        print("INTERSECCIÓN DE ELIPSE E HIPÉRBOLA POR MONTECARLO")
        valores = [leer_positivo(nombre) for nombre in ("a", "b", "c", "d")]
        cantidad = leer_positivo("cantidad de puntos", entero=True)
        mostrar_resultado(*valores, cantidad, argumentos.semilla)


if __name__ == "__main__":
    main()
