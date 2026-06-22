"""
profiling_demo.py
=================
Script de demostración para aprender cProfile en Python.

Contiene funciones con cuellos de botella INTENCIONALES de distintos tipos:
  1. Algoritmo cuadrático (búsqueda ineficiente)
  2. Llamadas repetidas a una función costosa
  3. Operaciones de string ineficientes
  4. Cálculo recursivo sin memoización

Cómo usarlo:
  # Modo básico (imprime resumen en consola)
  python -m cProfile profiling_demo.py

  # Ordenar por tiempo acumulado
  python -m cProfile -s cumulative profiling_demo.py

  # Guardar resultados en archivo binario para análisis posterior
  python -m cProfile -o resultado.prof profiling_demo.py

  # Analizar el archivo .prof con pstats
  python -c "import pstats; p = pstats.Stats('resultado.prof'); p.sort_stats('cumulative'); p.print_stats(15)"

  # O correr el profiler directamente desde código (ver main)
  python profiling_demo.py
"""

import cProfile
import pstats
import io
import time


# ─────────────────────────────────────────────────────────────
# 1. CUELLO DE BOTELLA: Búsqueda cuadrática O(n²)
#    En lugar de usar un set/dict, buscamos con "in" sobre lista
# ─────────────────────────────────────────────────────────────

def busqueda_lenta(lista, objetivos):
    """Busca cada objetivo en la lista con complejidad O(n·m)."""
    encontrados = []
    for objetivo in objetivos:
        if objetivo in lista:          # "in" en lista = O(n) cada vez
            encontrados.append(objetivo)
    return encontrados


def busqueda_rapida(lista, objetivos):
    """Versión optimizada: convierte la lista a set primero → O(1) por búsqueda."""
    conjunto = set(lista)
    return [o for o in objetivos if o in conjunto]


# ─────────────────────────────────────────────────────────────
# 2. CUELLO DE BOTELLA: Llamadas repetidas a función costosa
#    Recalcula algo que podría calcularse una sola vez
# ─────────────────────────────────────────────────────────────

def es_primo(n):
    """Verifica si n es primo (función costosa si se llama miles de veces)."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def filtrar_primos_lento(numeros):
    """Filtra primos llamando es_primo() en cada iteración sin caché."""
    return [n for n in numeros if es_primo(n)]


# ─────────────────────────────────────────────────────────────
# 3. CUELLO DE BOTELLA: Concatenación de strings con +=
#    Crea una nueva cadena en cada iteración → O(n²) en memoria
# ─────────────────────────────────────────────────────────────

def concatenar_lento(palabras):
    """Construye un string concatenando con += (ineficiente)."""
    resultado = ""
    for palabra in palabras:
        resultado += palabra + " "    # Nueva cadena en cada paso
    return resultado.strip()


def concatenar_rapido(palabras):
    """Versión correcta usando join()."""
    return " ".join(palabras)


# ─────────────────────────────────────────────────────────────
# 4. CUELLO DE BOTELLA: Fibonacci recursivo sin memoización
#    Recalcula los mismos valores exponencialmente
# ─────────────────────────────────────────────────────────────

def fibonacci_lento(n):
    """Fibonacci recursivo O(2^n) — muchas llamadas redundantes."""
    if n <= 1:
        return n
    return fibonacci_lento(n - 1) + fibonacci_lento(n - 2)


def fibonacci_rapido(n, memo={}):
    """Fibonacci con memoización O(n)."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_rapido(n - 1, memo) + fibonacci_rapido(n - 2, memo)
    return memo[n]


# ─────────────────────────────────────────────────────────────
# Función orquestadora — aquí se llama todo
# ─────────────────────────────────────────────────────────────

def ejecutar_escenarios():
    N = 5_000

    # Escenario 1: búsqueda
    lista_grande = list(range(N))
    objetivos = list(range(0, N, 3))
    busqueda_lenta(lista_grande, objetivos)
    busqueda_rapida(lista_grande, objetivos)

    # Escenario 2: primos
    numeros = list(range(2, 1_500))
    filtrar_primos_lento(numeros)

    # Escenario 3: strings
    palabras = [f"palabra{i}" for i in range(2_000)]
    concatenar_lento(palabras)
    concatenar_rapido(palabras)

    # Escenario 4: fibonacci
    fibonacci_lento(30)           # ← aquí verás el pico de llamadas
    fibonacci_rapido(30)


# ─────────────────────────────────────────────────────────────
# Main: corre el profiler desde código y muestra los resultados
# ─────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  DEMO cProfile — Detección de cuellos de botella")
    print("=" * 60)

    # Crear profiler
    profiler = cProfile.Profile()

    # Ejecutar código bajo el profiler
    profiler.enable()
    ejecutar_escenarios()
    profiler.disable()

    # ── Reporte 1: Top 15 funciones por tiempo propio (tottime) ──
    print("\n📊 TOP 15 — Ordenado por tiempo PROPIO (tottime)")
    print("   (tiempo dentro de la función, sin contar sus llamadas internas)\n")
    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream)
    stats.sort_stats("tottime")
    stats.print_stats(15)
    print(stream.getvalue())

    # ── Reporte 2: Top 15 por tiempo acumulado (cumulative) ──
    print("\n📊 TOP 15 — Ordenado por tiempo ACUMULADO (cumtime)")
    print("   (tiempo total incluyendo todas las sub-llamadas)\n")
    stream2 = io.StringIO()
    stats2 = pstats.Stats(profiler, stream=stream2)
    stats2.sort_stats("cumulative")
    stats2.print_stats(15)
    print(stream2.getvalue())

    # ── Reporte 3: quién llama a fibonacci_lento ──
    print("\n📊 ¿Quién llama a fibonacci_lento? (callers)")
    stream3 = io.StringIO()
    stats3 = pstats.Stats(profiler, stream=stream3)
    stats3.sort_stats("cumulative")
    stats3.print_callers("fibonacci_lento")
    print(stream3.getvalue())

    print("\n💡 COLUMNAS que verás en el reporte:")
    print("   ncalls    → número de veces que se llamó la función")
    print("   tottime   → tiempo propio de la función (sin sub-llamadas)")
    print("   percall   → tottime / ncalls")
    print("   cumtime   → tiempo acumulado incluyendo todas las llamadas internas")
    print("   percall   → cumtime / ncalls")
    print()
    print("💡 COMANDOS útiles desde la terminal:")
    print("   python -m cProfile -s cumulative profiling_demo.py")
    print("   python -m cProfile -o resultado.prof profiling_demo.py")
    print("   python -m pstats resultado.prof   (modo interactivo)")
    print()
    print("💡 VISUALIZACIÓN con snakeviz (instalar aparte):")
    print("   pip install snakeviz")
    print("   snakeviz resultado.prof")


if __name__ == "__main__":
    main()