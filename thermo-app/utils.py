import matplotlib.pyplot as plt
import os
import uuid
import numpy as np
import shutil
import matplotlib.animation as animation

def ensure_plot_dir():
    os.makedirs("static/plots", exist_ok=True)

def save_temperature_plot(temp_matrix):
    ensure_plot_dir()
    fig, ax = plt.subplots()
    c = ax.imshow(temp_matrix, cmap="hot", origin="lower")
    fig.colorbar(c, ax=ax)

    tmp_path = f"/tmp/{uuid.uuid4().hex}.png"
    static_rel_path = f"plots/{uuid.uuid4().hex}.png"
    static_full_path = os.path.join("static", static_rel_path)

    plt.savefig(tmp_path)
    plt.close()
    shutil.copy(tmp_path, static_full_path)
    return static_rel_path

def save_animation(temp_record):
    ensure_plot_dir()
    fig, ax = plt.subplots()
    ims = [ [ax.imshow(T, cmap="hot", animated=True, origin="lower")] for T in temp_record ]
    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True)

    tmp_path = f"/tmp/{uuid.uuid4().hex}.gif"
    static_rel_path = f"plots/{uuid.uuid4().hex}.gif"
    static_full_path = os.path.join("static", static_rel_path)

    ani.save(tmp_path, writer="pillow")
    plt.close()
    shutil.copy(tmp_path, static_full_path)
    return static_rel_path

def save_line_profile(temp_matrix):
    ensure_plot_dir()
    mid_row = temp_matrix[temp_matrix.shape[0] // 2, :]
    fig, ax = plt.subplots()
    ax.plot(mid_row, color='orange')
    ax.set_title("1D Temperature Profile (Mid Row)")
    ax.set_xlabel("X position")
    ax.set_ylabel("Temperature (°C)")

    tmp_path = f"/tmp/{uuid.uuid4().hex}_line.png"
    static_rel_path = f"plots/{uuid.uuid4().hex}_line.png"
    static_full_path = os.path.join("static", static_rel_path)

    plt.savefig(tmp_path)
    plt.close()
    shutil.copy(tmp_path, static_full_path)
    return static_rel_path

def save_contour_plot(temp_matrix):
    ensure_plot_dir()
    fig, ax = plt.subplots()
    cp = ax.contourf(temp_matrix, cmap="hot")
    fig.colorbar(cp)
    ax.set_title("Contour Plot of Temperature")

    tmp_path = f"/tmp/{uuid.uuid4().hex}_contour.png"
    static_rel_path = f"plots/{uuid.uuid4().hex}_contour.png"
    static_full_path = os.path.join("static", static_rel_path)

    plt.savefig(tmp_path)
    plt.close()
    shutil.copy(tmp_path, static_full_path)
    return static_rel_path
