import tracemalloc

def profile_memory_total(func, *args, **kwargs):
    """
    Mide la memoria total utilizada por una función y muestra los valores en gigabytes (GB).
    """
    tracemalloc.start()  # Inicia el seguimiento de memoria

    # Ejecuta la función con los argumentos proporcionados (sin retornar el resultado)
    func(*args, **kwargs)

    # Obtén estadísticas totales de memoria
    current, peak = tracemalloc.get_traced_memory()
    print(f"Memoria actual utilizada: {current / (1024 ** 3):.6f} GB")  # Convertir a GB
    print(f"Pico de memoria utilizada: {peak / (1024 ** 3):.6f} GB")    # Convertir a GB

    tracemalloc.stop()  # Detiene el seguimiento de memoria