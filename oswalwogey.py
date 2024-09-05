# Lista de videojuegos con sus géneros
videojuegos = [
{"nombre": "The Legend of Zelda: Breath of the Wild", "genero": "Shooter"},
{"nombre": "Super Mario Odyssey", "genero": "Shooter"},
{"nombre": "The Witcher 3: Wild Hunt", "genero": "Shooter"},
{"nombre": "God of War", "genero": "Shooter"},
{"nombre": "Celeste", "genero": "Shooter"},
{"nombre": "Hollow Knight", "genero": "Shooter"},
{"nombre": "Stardew Valley", "genero": "Shooter"},
{"nombre": "Overwatch", "genero": "Shooter"},]

genero_busqueda = input("Introduce el nombre del género: ")

print(f"Videojuegos del género '{genero_busqueda}':")

for juego in videojuegos:
    if juego["genero"]== genero_busqueda:
        print(f"- {juego['nombre']}")