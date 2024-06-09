import matplotlib.pyplot as plt
import numpy as np

def draw_pythagoras_tree(ax, x, y, angle, depth, size):
    if depth == 0:
        return
    
    x2 = x + size * np.cos(angle)
    y2 = y + size * np.sin(angle)
    
    ax.plot([x, x2], [y, y2], color="brown", lw=2)

    new_size = size * np.sqrt(2) / 2

    draw_pythagoras_tree(ax, x2, y2, angle - np.pi/4, depth - 1, new_size)
    draw_pythagoras_tree(ax, x2, y2, angle + np.pi/4, depth - 1, new_size)

def plot_pythagoras_tree(depth):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    draw_pythagoras_tree(ax, 0.5, 0, np.pi/2, depth, 0.1)
    plt.show()

plot_pythagoras_tree(5)
