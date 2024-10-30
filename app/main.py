# app/main.py
from menus.user_menu import user_menu
from menus.pluvial_menu import pluvial_menu
from menus.song_menu import song_menu
from menus.artist_menu import artist_menu
from menus.album_menu import album_menu
from menus.playlist_menu import playlist_menu
from menus.usuario_genero_menu import usuario_genero_menu
from menus.historial_reproduccion_menu import historial_reproduccion_menu
from menus.favoritos_menu import favoritos_menu

def main_menu():
    while True:
        print("\nBienvenido al sistema de gestión!")
        print("1. Gestión de Usuarios")
        print("2. Gestión de Datos Pluviales")
        print("3. Gestión de Música")
        print("4. Gestión de Artistas")
        print("5. Gestión de Álbumes")
        print("6. Gestión de Playlists")
        print("7. Gestión de Géneros por Usuario")
        print("8. Historial de Reproducción")
        print("9. Gestión de Favoritos")
        print("10. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            user_menu()
        elif opcion == '2':
            pluvial_menu()
        elif opcion == '3':
            song_menu()
        elif opcion == '4':
            artist_menu()
        elif opcion == '5':
            album_menu()
        elif opcion == '6':
            playlist_menu()
        elif opcion == '7':
            usuario_genero_menu()
        elif opcion == '8':
            historial_reproduccion_menu()
        elif opcion == '9':
            favoritos_menu()
        elif opcion == '10':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main_menu()
