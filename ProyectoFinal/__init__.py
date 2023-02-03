"""
The flask application package.
"""

from flask import Flask
import json


app = Flask(__name__)

wsgi_app = app.wsgi_app

peliculas = [
    {
        "titulo": "Ant Man and The Wasp Quantunmania",
        "año": 2023,
        "director": "Peyton Reed",
        "genero": "Accion, Ciencia Ficcion",
        "sinopsis": "Los superhéroes Scott Lang y Hope Van Dyne regresan para continuar sus aventuras como Ant-Man y Wasp. Con los padres de Hope, Hank Pym y Janet Van Dyne, y con la hija de Scott, Cassie Lang, la familia explora el Reino Quántico, interactúa con extrañas criaturas y se embarca en una aventura que los hará ir más allá de lo que creían posible. *ANT-MAN AND THE WASP: QUANTUMANIA contiene varias escenas con luces intermitentes que pueden afectar a personas susceptibles a la epilepsia fotosensible o a padecer otras fotosensibilidades.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2651_img2.jpg"
    },
    {
        "titulo": "Babylon",
        "año": 2023,
        "director": "Damien Chazelle",
        "genero": "Drama",
        "sinopsis": "De Damien Chazelle, BABYLON es una historia épica original ambientada en Los Ángeles de la década de 1920, protagonizada por Brad Pitt, Margot Robbie y Diego Calva, con un elenco que incluye a Jovan Adepo, Li Jun Li y Jean Smart. Una historia de ambición descomunal y exceso escandaloso, sigue el ascenso y la caída de múltiples personajes durante una era de decadencia y depravación desenfrenada en los inicios de Hollywood.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2558_img2.jpg"
    },
    {
        "titulo": "Argentina, 1985",
        "año": 2022,
        "director": "Santiago Mitre",
        "genero": "Drama",
        "sinopsis": "Argentina, 1985 está inspirada en la historia real de Julio Strassera, Luis Moreno Ocampo y su joven equipo jurídico que se atrevieron a acusar, contra viento y marea, a contrarreloj y bajo constante amenaza, a la más sangrienta dictadura militar argentina. Una batalla de David contra Goliat, con los héroes menos esperados.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2544_img2.jpg"
    },
    {
        "titulo": "Avatar: El Camino del Agua",
        "año": 2022,
        "director": "James Cameron",
        "genero": "Fantasia",
        "sinopsis": "Ambientada más de una década después de los sucesos que tuvieron lugar en la primera película, AVATAR: EL CAMINO DEL AGUA narra la historia de la familia Sully (Jake, Neytiri y sus hijos), el peligro que los persigue, los esfuerzos que hacen para mantenerse a salvo, las batallas que libran para seguir con vida, y las tragedias que sobrellevan.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2482_img2.jpg"
    },
    {
        "titulo": "Gato con Botas 2: El Ultimo Deseo",
        "año": 2022,
        "director": "Joel Crawford",
        "genero": "Aventuras",
        "sinopsis": "Por primera vez en más de una década, DreamWorks Animation presenta una nueva aventura en el universo de Shrek en la que el temerario y aventurero Gato con Botas descubre que su pasión por el peligro y su indiferencia por la seguridad le han pasado factura. Nuestro heroico felino ha gastado ocho de sus nueve vidas, aunque ha perdido la cuenta por el camino. Recuperar esas vidas hará que el Gato con Botas emprenda su más grande aventura hasta ahora. El nominado al Oscar® Antonio Banderas vuelve a ser la voz del famoso Gato con Botas, que se embarca en un viaje épico al Bosque Negro para encontrar la mítica Estrella de los Deseos y recuperar sus vidas perdidas. Pero cuando sólo le queda una vida, el Gato tendrá que aprender a ser humilde y pedir ayuda a su antigua compañera y némesis: la cautivadora Kitty Soft Paws (nominada al Oscar® Salma Hayek). En su búsqueda, el Gato con Botas y Kitty contarán a regañadientes con la ayuda de un perro callejero, parlanchín e implacablemente alegre, Perro (Harvey Guillén, Lo que hacemos en las sombras). Juntos, nuestro trío de héroes tendrá que ir un paso adelante de Ricitos de Oro (nominada al Oscar® Florence Pugh, Viuda Negra) y de la Familia del Crimen de los Tres Osos, el Gran Jack Horner (ganador del Emmy John Mulaney, Big Mouth) y el terrorífico cazarrecompensas, El Lobo Feroz (Wagner Moura, Narcos).",
        "link": "https://www.cinemacenter.com.ar/img_movies/2523_img2.jpg"
    },
    {
        "titulo": "M3gan",
        "año": 2023,
        "director": "Gerard Johnstone",
        "genero": "Terror",
        "sinopsis": "M3GAN es una maravilla de la inteligencia artificial, una muñeca parecida a un humano programada para ser la mejor compañía de un niño y el mejor aliado de un padre. Diseñada por la brillante especialista en robótica de una empresa de juguetes (Allison Williams, Get Out), M3GAN puede escuchar, mirar y aprender mientras se convierte en amiga y maestra, compañera y protectora, para el niño al que está vinculada.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2559_img2.jpg"
    },
    {
        "titulo": "Creed III",
        "año": 2023,
        "director": "Michael B. Jordan",
        "genero": "Drama, Deportes",
        "sinopsis": "Después de dominar el mundo del boxeo, Adonis Creed ha prosperado tanto en su carrera como en su vida familiar. Cuando un amigo de la infancia y ex prodigio del boxeo, Damian (Jonathan Majors), resurge después de cumplir una larga condena en prisión, está ansioso por demostrar que merece su oportunidad en el ring. El enfrentamiento entre antiguos amigos es más que una simple pelea. Para ajustar cuentas, Adonis debe arriesgar su futuro para luchar contra Damian, un luchador que no tiene nada que perder.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2575_img2.jpg"
    },
    {
        "titulo": "¡SHAZAM! La Furia de los Dioses",
        "año": 2023,
        "director": "David F. Sandberg",
        "genero": "Accion, Ciencia Ficcion",
        "sinopsis": "De New Line Cinema llega ¡Shazam! La furia de los dioses, que continúa la historia del adolescente Billy Batson que, al recitar la palabra mágica ¡SHAZAM!, se transforma en su alter ego de superhéroe adulto, Shazam.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2562_img2.jpg"
    },
    {
        "titulo": "John Wick 4",
        "año": 2023,
        "director": "Chad Stahelski",
        "genero": "Acccion, Thriller",
        "sinopsis": "John Wick (Keanu Reeves) descubre un camino para derrotar a La Mesa. Pero antes de poder ganar su libertad, Wick deberá enfrentarse a un nuevo enemigo con poderosas alianzas en todo el mundo; y contra las fuerzas que convierten a viejos amigos en enemigos.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2612_img2.jpg"
    },
    {
        "titulo": "Super Mario Bros. La Pelicula",
        "año": 2023,
        "director": "Aaron Horvath, Michael Jelenic",
        "genero": "Comedia, Aventura, Fantasia",
        "sinopsis": "Dirigida por by Aaron Horvath y Michael Jelenic (colaboradores en Los Jóvenes Titanes en acción, Jóvenes Titanes en acción: la película) de un guion de Matthew Fogel (La gran aventura LEGO 2, Minions: Nace un villano), la película es protagonizada por Chris Pratt como Mario, Anya Taylor-Joy como la Princesa Peach, Charlie Day como Luigi, Jack Black como Bowser, Keegan-Michael Key como Toad, Seth Rogen como Donkey Kong, Fred Armisen como Cranky Kong, Kevin Michael Richardson como Kamek y Sebastian Maniscalco como Spike.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2561_img2.jpg"
    }
]

if __name__ == "__main__":
    app.run("localhost", 8000)
