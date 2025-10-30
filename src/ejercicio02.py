"""
Ejercicio 2: Clasificador de Temperaturas

Descripción:
    Programa que clasifica una temperatura en categorías y determina
    si es una temperatura extrema.
    
Autor: Eduardo Fdez
Fecha: 2025-10-25
"""


def clasificar_temperatura(temperatura: float) -> tuple[str, bool]:
    """
    Clasifica una temperatura y determina si es extrema.
    
    Esta función es la que se evaluará mediante tests automáticos.
    
    Args:
        temperatura: La temperatura en grados Celsius
        
    Returns:
        tuple[str, bool]: (clasificación, es_extrema)
            - clasificación: "Helada", "Frío", "Templado", "Cálido" o "Caluroso"
            - -50i a 0 helado, 0i a 10i frio,10 a 20i templado, 20 a 30i calido, 30 a 60i "caluroso"
            - es_extrema: True si temp < -10 o temp > 40, False en caso contrario
        
    Nota:
        - Si la temperatura está fuera del rango válido (-50 a 60), 
          devolver ("Inválida", False)
    """
    # TODO: Implementar la función
    if temperatura < -50 or temperatura > 60:
        return("Inválida", False)
    if temperatura >= -50 and temperatura < -10:
        return("Helada", True)
    elif temperatura >= -10 and temperatura < 0:
        return("Helada", False)
    elif temperatura >= 0 and temperatura <= 10:
        return("Frío", False)
    elif temperatura > 10 and temperatura <= 20:
        return("Templado", False)
    elif temperatura > 20 and temperatura <= 30:
        return("Cálido", False)
    elif temperatura > 30 and temperatura <= 40:
        return("Caluroso", False)
    elif temperatura > 40 and temperatura <= 60:
        return("Caluroso", True)



def solicitar_temperatura() -> float:
    """
    Solicita al usuario una temperatura y valida que esté en el rango correcto.
    
    Returns:
        float: La temperatura validada (entre -50 y 60)
    """
    temperatura: float = -100.0  # Valor inicial fuera de rango para entrar al bucle
    
    # Bucle que se ejecuta mientras la temperatura no sea válida
    while temperatura < -50 or temperatura > 60:
        entrada: str = input("Introduce la temperatura en °C: ")
        
        try:
            temperatura = float(entrada)
            
            # Validar el rango
            if temperatura < -50 or temperatura > 60:
                print("Error: La temperatura debe estar entre -50°C y 60°C")
        except ValueError:
            print("Error: Debe introducir un número válido.")
            temperatura = -100.0  # Mantener fuera de rango para continuar
    
    return temperatura


def mostrar_resultado(temperatura: float, clasificacion: str, es_extrema: bool) -> None:
    """
    Muestra el resultado de la clasificación de manera formateada.
    
    Args:
        temperatura: La temperatura analizada
        clasificacion: La clasificación obtenida
        es_extrema: Si la temperatura es extrema o no
    """
    print(f"\nTemperatura: {temperatura}°C")
    print(f"Clasificación: {clasificacion}")
    
    # Mostrar alerta según si es extrema o no
    if es_extrema:
        print("¡ALERTA! Temperatura EXTREMA")
    else:
        print("Temperatura NO extrema")


def main() -> None:
    """
    Función principal que coordina la ejecución del programa.
    
    Flujo:
        1. Solicita la temperatura al usuario (con validación)
        2. Clasifica la temperatura usando la función obligatoria
        3. Muestra el resultado formateado
    """
    # Paso 1: Obtener temperatura del usuario
    temperatura: float = solicitar_temperatura()
    
    # Paso 2: Clasificar usando la función obligatoria
    clasificacion: str
    es_extrema: bool
    clasificacion, es_extrema = clasificar_temperatura(temperatura)
    
    # Paso 3: Mostrar resultado
    mostrar_resultado(temperatura, clasificacion, es_extrema)


# Punto de entrada del programa
if __name__ == "__main__":
    main()
