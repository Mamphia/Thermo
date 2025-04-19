import numpy as np

def run_simulation(length, width, flow_rate, alpha, nx=50, ny=50, nt=100, dt=0.01):
    dx = length / nx
    dy = width / ny
    T = np.ones((ny, nx)) * 20
    T[:, 0] = 100

    alpha_x = alpha * dt / dx**2
    alpha_y = alpha * dt / dy**2

    T_record = [T.copy()]  # 👈 store time steps

    for _ in range(nt):
        T_new = T.copy()
        T_new[1:-1, 1:-1] = (
            T[1:-1, 1:-1]
            + alpha_x * (T[1:-1, 2:] - 2*T[1:-1, 1:-1] + T[1:-1, :-2])
            + alpha_y * (T[2:, 1:-1] - 2*T[1:-1, 1:-1] + T[:-2, 1:-1])
        )
        T = T_new
        T_record.append(T.copy())

    return T, T_record
