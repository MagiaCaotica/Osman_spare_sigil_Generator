import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

def create_sigil(desire):
    consonants = [c for c in desire.lower() if c.isalpha() and c not in 'aeiou']
    letters = list(set(consonants))
    random.shuffle(letters)
    sigil = ''.join(letters)
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
    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_aspect('equal')
    ax.axis('off')
    circle = plt.Circle((0.5, 0.5), 0.4, color='black', fill=False, lw=2)
    ax.add_artist(circle)
    num_letters = len(sigil)
    fibonacci_points = fibonacci_sphere(num_letters)
    x_letters = [0.5 + 0.35 * p[0] for p in fibonacci_points]
    y_letters = [0.5 + 0.35 * p[1] for p in fibonacci_points]
    for i, letter in enumerate(sigil):
        ax.text(x_letters[i], y_letters[i], letter, fontsize=1, ha='center', va='center', color='black')
    for i in range(num_letters):
        j = (i + 1) % num_letters
        x_start, y_start = x_letters[i], y_letters[i]
        x_end, y_end = x_letters[j], y_letters[j]
        ax.plot([x_start, x_end], [y_start, y_end], color='black')
    ax.scatter(x_letters[0], y_letters[0], color='black', s=20)
    ax.scatter(x_letters[-1], y_letters[-1], color='black', s=20)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    st.pyplot(fig)

st.title("Austin Osman Spare Sigil Generator")
st.text("Created by Frater Cha0smagick for the blog grimoriomagiadelcaos.blogspot.com")
st.text("generate chaos sigils under the sigilization theory created by Austin Osman Spare")
st.text("creator of the ZOS KIA CVLTVS")
desire = st.text_input("Enter your wish or intention:")
if desire:
    sigil = create_sigil(desire)
    st.write("Generated Sigil:", sigil)
    visualize_sigil(sigil)
