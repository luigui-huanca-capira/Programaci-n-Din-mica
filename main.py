
"""
Actividad 9 - Programación Dinámica
Autor: Josue Miguel Flores Parra

Problemas implementados (según PDF):
1) Escaleras: número de formas de llegar al escalón N usando saltos de 1 o 2.
2) Cambio mínimo de monedas: mínimo número de monedas para formar una cantidad objetivo.

El programa muestra:
- Resultado principal
- Tabla DP generada
- Combinación válida (en cambio de monedas)
"""

from math import inf


# ======================================
# PROBLEMA 1: ESCALERAS (1 o 2 saltos)
# ======================================
def escaleras_dp(n):
    """
    Estado DP:
        dp[i] = número de formas de llegar al escalón i.

    Recurrencia:
        dp[i] = dp[i-1] + dp[i-2] para i >= 2

    Casos base:
        dp[0] = 1  (una forma: no moverse)
        dp[1] = 1  (una forma: 1 salto)
    """
    if n < 0:
        return 0, []

    if n == 0:
        return 1, [1]

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n], dp


# ============================================
# PROBLEMA 2: CAMBIO MÍNIMO DE MONEDAS (DP)
# ============================================
def cambio_min_monedas(monedas, cantidad):
    """
    Estado DP:
        dp[x] = mínimo número de monedas para formar la cantidad x.

    Recurrencia:
        dp[x] = min(dp[x], dp[x-c] + 1) para cada moneda c si x >= c

    Caso base:
        dp[0] = 0
        dp[x] = infinito para x > 0 inicialmente
    """
    dp = [inf] * (cantidad + 1)
    prev = [-1] * (cantidad + 1)
    dp[0] = 0

    for x in range(1, cantidad + 1):
        for c in monedas:
            if x - c >= 0 and dp[x - c] + 1 < dp[x]:
                dp[x] = dp[x - c] + 1
                prev[x] = c

    if dp[cantidad] == inf:
        return -1, [], dp

    combinacion = []
    x = cantidad
    while x > 0:
        combinacion.append(prev[x])
        x -= prev[x]

    return dp[cantidad], combinacion, dp


def leer_lista_enteros(msg):
    return list(map(int, input(msg).strip().split()))


def imprimir_combinacion(combinacion):
    if not combinacion:
        return "N/A"
    return " + ".join(map(str, combinacion))


def menu():
    while True:
        print("\n=== Actividad 9: Programación Dinámica ===")
        print("1) Resolver Escaleras")
        print("2) Resolver Cambio mínimo de monedas")
        print("3) Ejecutar ejemplos guía del PDF")
        print("0) Salir")

        try:
            opcion = input("Selecciona una opción: ").strip()
        except EOFError:
            print("\nEntrada finalizada (EOF). Saliendo...")
            break

        opcion = opcion.strip("\"'")

        if opcion == "1":
            print("\n--- Escaleras ---")
            n = int(input("Ingrese el número de escalones N: ").strip())
            total, tabla = escaleras_dp(n)
            print(f"Formas posibles: {total}")
            print("Tabla DP:")
            print(tabla)

        elif opcion == "2":
            print("\n--- Cambio mínimo de monedas ---")
            m = int(input("Cantidad de tipos de moneda: ").strip())
            monedas = leer_lista_enteros(f"Ingrese {m} monedas separadas por espacio: ")
            cantidad = int(input("Ingrese la cantidad objetivo: ").strip())

            if len(monedas) != m:
                print("Error: la cantidad de monedas ingresadas no coincide con m.")
                continue

            minimo, combinacion, tabla = cambio_min_monedas(monedas, cantidad)
            if minimo == -1:
                print("No es posible formar la cantidad con las monedas dadas.")
                print("Tabla DP:")
                print(["inf" if x == inf else x for x in tabla])
            else:
                print(f"Cantidad mínima de monedas: {minimo}")
                print(f"Combinación: {imprimir_combinacion(combinacion)}")
                print("Tabla DP:")
                print(tabla)

        elif opcion == "3":
            print("\n--- Ejemplos guía del PDF ---")

            print("\n[Escaleras - Ejemplo 1]")
            n = 5
            total, tabla = escaleras_dp(n)
            print(f"Entrada: N = {n}")
            print(f"Formas posibles: {total}")
            print("Tabla DP:")
            print(tabla)

            print("\n[Escaleras - Ejemplo 2]")
            n = 7
            total, tabla = escaleras_dp(n)
            print(f"Entrada: N = {n}")
            print(f"Formas posibles: {total}")
            print("Tabla DP:")
            print(tabla)

            print("\n[Cambio de monedas - Ejemplo 1]")
            monedas = [1, 3, 4]
            cantidad = 6
            minimo, combinacion, tabla = cambio_min_monedas(monedas, cantidad)
            print(f"Monedas: {monedas}")
            print(f"Cantidad: {cantidad}")
            print(f"Cantidad mínima de monedas: {minimo}")
            print(f"Combinación: {imprimir_combinacion(combinacion)}")
            print("Tabla DP:")
            print(tabla)

            print("\n[Cambio de monedas - Ejemplo 2]")
            monedas = [1, 2, 5]
            cantidad = 11
            minimo, combinacion, tabla = cambio_min_monedas(monedas, cantidad)
            print(f"Monedas: {monedas}")
            print(f"Cantidad: {cantidad}")
            print(f"Cantidad mínima de monedas: {minimo}")
            print(f"Combinación: {imprimir_combinacion(combinacion)}")
            print("Tabla DP:")
            print(tabla)

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
