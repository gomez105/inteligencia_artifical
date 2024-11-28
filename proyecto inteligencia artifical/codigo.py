import os
import pygame

def buscar_genero(entrada, generos):
    """
    Busca el género en una lista de géneros disponibles.
    :param entrada: Género ingresado por el usuario.
    :param generos: Diccionario de géneros disponibles en minúsculas.
    :return: El género original si se encuentra, None si no.
    """
    for genero_min, genero_original in generos.items():
        if genero_min == entrada:
            return genero_original
    return None

def main():
    # Diccionario con géneros y canciones en formato mp3
    canciones = {
        "salsa": ["canciones/desnudate_mujer.mp3", "canciones/mi_desengaño.mp3"],
        "Regueton": ["canciones/que_la_pases_bien.mp3", "canciones/vuelve.mp3"],
        "merengue": ["canciones/nuestra_cancion.mp3", "canciones/Suavemente.mp3"],
        "vallenato": ["canciones/la_lira.mp3", "canciones/matilde_lina.mp3"]
    }

    # Convertir claves a minúsculas para facilitar la comparación
    generos_disponibles = {genero.lower(): genero for genero in canciones.keys()}

    print("¡Bienvenido al reproductor de música de Gómez!")
    print("Estos son los géneros disponibles:")
    for genero in canciones.keys():
        print(f"- {genero}")

    while True:
        try:
            # Solicitar el nombre del género al usuario
            genero_deseado = input("\nPor favor, escribe el nombre del género que quieres escuchar: ").strip().lower()
            
            # Buscar género utilizando búsqueda secuencial
            genero_original = buscar_genero(genero_deseado, generos_disponibles)
            
            if genero_original:
                print(f"\nHas seleccionado: {genero_original}")
                print("Reproduciendo las canciones de este género...")
                
                # Reproducir todas las canciones del género seleccionado
                for cancion in canciones[genero_original]:
                    print(f"\nReproduciendo: {cancion}")
                    reproducir_cancion(cancion)
                
                print("\nTodas las canciones del género han sido reproducidas. ¡Disfruta!")
                break  # Salir del bucle tras terminar el género seleccionado
            else:
                print(f"El género '{genero_deseado}' no está disponible. Intenta de nuevo.")
        except Exception as e:
            print(f"Error: {e}. Intenta de nuevo.")

def reproducir_cancion(cancion):
    try:
        # Inicializar pygame para reproducir audio
        pygame.mixer.init()

        # Verifica si el archivo existe antes de intentar cargarlo
        if os.path.exists(cancion):
            pygame.mixer.music.load(cancion)
            pygame.mixer.music.play()

            print("Presiona Enter para saltar a la siguiente canción.")
            while pygame.mixer.music.get_busy():  # Reproducir mientras la canción esté sonando
                if input() == "":  # Detectar Enter
                    pygame.mixer.music.stop()  # Detener la canción actual
                    break
        else:
            print(f"El archivo {cancion} no se encuentra en la ruta especificada.")
    except Exception as e:
        print(f"Error al intentar reproducir la canción: {e}")

# Ejecutar el programa
if __name__ == "__main__":
    main()