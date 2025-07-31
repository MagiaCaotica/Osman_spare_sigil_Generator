import matplotlib.pyplot as plt
import numpy as np
import random

def create_sigil(desire):
    # Paso 1: Enshrine your desire in a short sentence
    # Vamos a asumir que el texto 'desire' ya es una oración corta
    # Paso 2: Write out the sentence and then put down all the individual letters of which it is composed, omitting any repetition of a letter
    # Convertimos el texto a minúsculas y eliminamos repeticiones de letras
    consonants = [c for c in desire.lower() if c.isalpha() and c not in 'aeiou']
    letters = list(set(consonants))
    
    # Paso 3: Unite them graphically in one composite glyph which does not suggest the nature of the desire
    # Crear un glifo compuesto
    random.shuffle(letters)  # Mezclamos las letras aleatoriamente
    sigil = ''.join(letters)
    
    # Paso 4: Then—and this is of great importance—forget the desire and sink the sigil in the subconsciousness
    return sigil

def fibonacci_sphere(samples=1):
    rnd = 1.
    points = []
    offset = 2./samples
    increment = np.pi * (3. - np.sqrt(5.))
    for i in range(samples):
        y = ((i * offset) - 1) + (offset / 2)
        r = np.sqrt(1 - y*y)
        phi = ((i + rnd) % samples) * increment
        x = np.cos(phi) * r
        z = np.sin(phi) * r
        points.append([x, y, z])
    return points

def visualize_sigil(sigil):
    fig, ax = plt.subplots(figsize=(6,6))  # Tamaño del lienzo
    ax.set_aspect('equal')
    ax.axis('off')

    # Aquí creamos un círculo goético para el sigilo
    circle = plt.Circle((0.5, 0.5), 0.4, color='black', fill=False, lw=2)
    ax.add_artist(circle)

    # Obtenemos las posiciones de las letras en el círculo siguiendo la espiral de Fibonacci
    num_letters = len(sigil)
    fibonacci_points = fibonacci_sphere(num_letters)
    x_letters = [0.5 + 0.35 * p[0] for p in fibonacci_points]
    y_letters = [0.5 + 0.35 * p[1] for p in fibonacci_points]

    # Dibujamos las letras
    for i, letter in enumerate(sigil):
        ax.text(x_letters[i], y_letters[i], letter, fontsize=1, ha='center', va='center', color='black')

    # Unimos las letras con líneas místicas
    for i in range(num_letters):
        j = (i + 1) % num_letters  # Unimos con el siguiente punto en la espiral
        x_start, y_start = x_letters[i], y_letters[i]
        x_end, y_end = x_letters[j], y_letters[j]
        ax.plot([x_start, x_end], [y_start, y_end], color='black')

    # Colocamos un pequeño círculo al principio de la primera línea
    ax.scatter(x_letters[0], y_letters[0], color='black', s=20)

    # Colocamos un pequeño círculo al final de la última línea
    ax.scatter(x_letters[-1], y_letters[-1], color='black', s=20)

    plt.xlim(0, 1)  # Limitamos los ejes para que el círculo no se salga del lienzo
    plt.ylim(0, 1)
    plt.show()

# Ejemplo de uso
desire = "mutantes skateboarding"
sigil = create_sigil(desire)
print("Sigil:", sigil)
visualize_sigil(sigil)
