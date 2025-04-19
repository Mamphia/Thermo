import matplotlib.pyplot as plt
import os
import uuid
import numpy as np
import matplotlib.animation as animation

def ensure_plot_dir():
    os.makedirs("static/plots", exist_ok=True)

def save_temperature_plot(temp_matrix):
    ensure_plot_dir()
    fig, ax = plt.subplots()
    c = ax.imshow(temp_matrix, cmap="hot", origin="lower")
    fig.colorbar(c, ax=ax)
    filename = f"{uuid.uuid4().hex}.png"
    filepath = os.path.join("static/plots", filename)
    plt.savefig(filepath)
    plt.close()
    return f"plots/{filename}"

def save_animation(temp_record):
    ensure_plot_dir()
    fig, ax = plt.subplots()
    ims = []
    for T in temp_record:
        im = ax.imshow(T, cmap="hot", animated=True, origin="lower")
        ims.append([im])
    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True)
    filename = f"{uuid.uuid4().hex}.gif"
    filepath = os.path.join("static/plots", filename)
    ani.save(filepath, writer="pillow")
    plt.close()
    return f"plots/{filename}"

def save_line_profile(temp_matrix):
    ensure_plot_dir()
    mid_row = temp_matrix[temp_matrix.shape[0] // 2, :]
    fig, ax = plt.subplots()
    ax.plot(mid_row, color='orange')
    ax.set_title("1D Temperature Profile (Mid Row)")
    ax.set_xlabel("X position")
    ax.set_ylabel("Temperature (°C)")
    filename = f"{uuid.uuid4().hex}_line.png"
    filepath = os.path.join("static/plots", filename)
    plt.savefig(filepath)
    plt.close()
    return f"plots/{filename}"

def save_contour_plot(temp_matrix):
    ensure_plot_dir()
    fig, ax = plt.subplots()
    cp = ax.contourf(temp_matrix, cmap="hot")
    fig.colorbar(cp)
    ax.set_title("Contour Plot of Temperature")
    filename = f"{uuid.uuid4().hex}_contour.png"
    filepath = os.path.join("static/plots", filename)
    plt.savefig(filepath)
    plt.close()
    return f"plots/{filename}"
