import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import newton

def move_figure(f, x, y):
    """Move figure's upper left corner to pixel (x, y)"""
    backend = matplotlib.get_backend()
    if backend == 'TkAgg':
        f.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))
    elif backend == 'WXAgg':
        f.canvas.manager.window.SetPosition((x, y))
    else:
        # This works for QT and GTK
        # You can also use window.setGeometry
        f.canvas.manager.window.move(x, y)


def f(x):
    return x ** 2


x0 = 8
result_nr, history_nr = newton.newton(f, x0)

# Plot the function
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))
fig.suptitle("Approximating roots through multiple methods")

# Ax1
x = np.linspace(-10, 10, 100)
ax1.plot(x, f(x), label="f(x)")
ax1.plot(history_nr, f(np.array(history_nr)), marker='o', label="History")
ax1.plot(result_nr, f(result_nr), 'o', label="Result")
ax1.set_title("Newton-Raphson")
ax1.legend()

# Move window to top left corner
move_figure(fig, 0, 0)

plt.show()
