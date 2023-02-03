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
        "a�o": 2023,
        "director": "Peyton Reed",
        "genero": "Accion, Ciencia Ficcion",
        "sinopsis": "Los superh�roes Scott Lang y Hope Van Dyne regresan para continuar sus aventuras como Ant-Man y Wasp. Con los padres de Hope, Hank Pym y Janet Van Dyne, y con la hija de Scott, Cassie Lang, la familia explora el Reino Qu�ntico, interact�a con extra�as criaturas y se embarca en una aventura que los har� ir m�s all� de lo que cre�an posible. *ANT-MAN AND THE WASP: QUANTUMANIA contiene varias escenas con luces intermitentes que pueden afectar a personas susceptibles a la epilepsia fotosensible o a padecer otras fotosensibilidades.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2651_img2.jpg"
    },
    {
        "titulo": "Babylon",
        "a�o": 2023,
        "director": "Damien Chazelle",
        "genero": "Drama",
        "sinopsis": "De Damien Chazelle, BABYLON es una historia �pica original ambientada en Los �ngeles de la d�cada de 1920, protagonizada por Brad Pitt, Margot Robbie y Diego Calva, con un elenco que incluye a Jovan Adepo, Li Jun Li y Jean Smart. Una historia de ambici�n descomunal y exceso escandaloso, sigue el ascenso y la ca�da de m�ltiples personajes durante una era de decadencia y depravaci�n desenfrenada en los inicios de Hollywood.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2558_img2.jpg"
    },
    {
        "titulo": "Argentina, 1985",
        "a�o": 2022,
        "director": "Santiago Mitre",
        "genero": "Drama",
        "sinopsis": "Argentina, 1985 est� inspirada en la historia real de Julio Strassera, Luis Moreno Ocampo y su joven equipo jur�dico que se atrevieron a acusar, contra viento y marea, a contrarreloj y bajo constante amenaza, a la m�s sangrienta dictadura militar argentina. Una batalla de David contra Goliat, con los h�roes menos esperados.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2544_img2.jpg"
    },
    {
        "titulo": "Avatar: El Camino del Agua",
        "a�o": 2022,
        "director": "James Cameron",
        "genero": "Fantasia",
        "sinopsis": "Ambientada m�s de una d�cada despu�s de los sucesos que tuvieron lugar en la primera pel�cula, AVATAR: EL CAMINO DEL AGUA narra la historia de la familia Sully (Jake, Neytiri y sus hijos), el peligro que los persigue, los esfuerzos que hacen para mantenerse a salvo, las batallas que libran para seguir con vida, y las tragedias que sobrellevan.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2482_img2.jpg"
    },
    {
        "titulo": "Gato con Botas 2: El Ultimo Deseo",
        "a�o": 2022,
        "director": "Joel Crawford",
        "genero": "Aventuras",
        "sinopsis": "Por primera vez en m�s de una d�cada, DreamWorks Animation presenta una nueva aventura en el universo de Shrek en la que el temerario y aventurero Gato con Botas descubre que su pasi�n por el peligro y su indiferencia por la seguridad le han pasado factura. Nuestro heroico felino ha gastado ocho de sus nueve vidas, aunque ha perdido la cuenta por el camino. Recuperar esas vidas har� que el Gato con Botas emprenda su m�s grande aventura hasta ahora. El nominado al Oscar� Antonio Banderas vuelve a ser la voz del famoso Gato con Botas, que se embarca en un viaje �pico al Bosque Negro para encontrar la m�tica Estrella de los Deseos y recuperar sus vidas perdidas. Pero cuando s�lo le queda una vida, el Gato tendr� que aprender a ser humilde y pedir ayuda a su antigua compa�era y n�mesis: la cautivadora Kitty Soft Paws (nominada al Oscar� Salma Hayek). En su b�squeda, el Gato con Botas y Kitty contar�n a rega�adientes con la ayuda de un perro callejero, parlanch�n e implacablemente alegre, Perro (Harvey Guill�n, Lo que hacemos en las sombras). Juntos, nuestro tr�o de h�roes tendr� que ir un paso adelante de Ricitos de Oro (nominada al Oscar� Florence Pugh, Viuda Negra) y de la Familia del Crimen de los Tres Osos, el Gran Jack Horner (ganador del Emmy John Mulaney, Big Mouth) y el terror�fico cazarrecompensas, El Lobo Feroz (Wagner Moura, Narcos).",
        "link": "https://www.cinemacenter.com.ar/img_movies/2523_img2.jpg"
    },
    {
        "titulo": "M3gan",
        "a�o": 2023,
        "director": "Gerard Johnstone",
        "genero": "Terror",
        "sinopsis": "M3GAN es una maravilla de la inteligencia artificial, una mu�eca parecida a un humano programada para ser la mejor compa��a de un ni�o y el mejor aliado de un padre. Dise�ada por la brillante especialista en rob�tica de una empresa de juguetes (Allison Williams, Get Out), M3GAN puede escuchar, mirar y aprender mientras se convierte en amiga y maestra, compa�era y protectora, para el ni�o al que est� vinculada.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2559_img2.jpg"
    },
    {
        "titulo": "Creed III",
        "a�o": 2023,
        "director": "Michael B. Jordan",
        "genero": "Drama, Deportes",
        "sinopsis": "Despu�s de dominar el mundo del boxeo, Adonis Creed ha prosperado tanto en su carrera como en su vida familiar. Cuando un amigo de la infancia y ex prodigio del boxeo, Damian (Jonathan Majors), resurge despu�s de cumplir una larga condena en prisi�n, est� ansioso por demostrar que merece su oportunidad en el ring. El enfrentamiento entre antiguos amigos es m�s que una simple pelea. Para ajustar cuentas, Adonis debe arriesgar su futuro para luchar contra Damian, un luchador que no tiene nada que perder.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2575_img2.jpg"
    },
    {
        "titulo": "�SHAZAM! La Furia de los Dioses",
        "a�o": 2023,
        "director": "David F. Sandberg",
        "genero": "Accion, Ciencia Ficcion",
        "sinopsis": "De New Line Cinema llega �Shazam! La furia de los dioses, que contin�a la historia del adolescente Billy Batson que, al recitar la palabra m�gica �SHAZAM!, se transforma en su alter ego de superh�roe adulto, Shazam.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2562_img2.jpg"
    },
    {
        "titulo": "John Wick 4",
        "a�o": 2023,
        "director": "Chad Stahelski",
        "genero": "Acccion, Thriller",
        "sinopsis": "John Wick (Keanu Reeves) descubre un camino para derrotar a La Mesa. Pero antes de poder ganar su libertad, Wick deber� enfrentarse a un nuevo enemigo con poderosas alianzas en todo el mundo; y contra las fuerzas que convierten a viejos amigos en enemigos.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2612_img2.jpg"
    },
    {
        "titulo": "Super Mario Bros. La Pelicula",
        "a�o": 2023,
        "director": "Aaron Horvath, Michael Jelenic",
        "genero": "Comedia, Aventura, Fantasia",
        "sinopsis": "Dirigida por by Aaron Horvath y Michael Jelenic (colaboradores en Los J�venes Titanes en acci�n, J�venes Titanes en acci�n: la pel�cula) de un guion de Matthew Fogel (La gran aventura LEGO 2, Minions: Nace un villano), la pel�cula es protagonizada por Chris Pratt como Mario, Anya Taylor-Joy como la Princesa Peach, Charlie Day como Luigi, Jack Black como Bowser, Keegan-Michael Key como Toad, Seth Rogen como Donkey Kong, Fred Armisen como Cranky Kong, Kevin Michael Richardson como Kamek y Sebastian Maniscalco como Spike.",
        "link": "https://www.cinemacenter.com.ar/img_movies/2561_img2.jpg"
    }
]

if __name__ == "__main__":
    app.run("localhost", 8000)
