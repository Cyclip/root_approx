import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import newton
import secant

EXPECTED = 0

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

# Newton-Raphson method
x0 = 8
result_nr, history_nr = newton.newton(f, x0)
error_nr = result_nr - EXPECTED

# Secant line method
# Ensure they intersect x axis, otherwise zero division error
x1 = -10
x2 = -7
result_s, history_s = secant.secant(f, x1, x2)
error_s = result_s - EXPECTED

# Plot the function
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))
fig.suptitle("Approximating roots through multiple methods")

# Ax1
x = np.linspace(-10, 10, 100)
ax1.plot(x, f(x), label="f(x)")
ax1.plot(history_nr, f(np.array(history_nr)), marker='o', label="History")
ax1.plot(result_nr, f(result_nr), 'o', label="Result")
ax1.set_title(f"Newton-Raphson ({len(history_nr)} runs, error: {error_nr:.2f})")
ax1.legend()

# Ax2
x = np.linspace(-10, 10, 100)
ax2.plot(x, f(x), label="f(x)")

# Plot history
# History formatted as [(x1, x2), (x2, x3), ...]
# Plot the x1 and x2 values
x1 = [x[0] for x in history_s]
x2 = [x[1] for x in history_s]
ax2.plot(x1, f(np.array(x1)), marker='o', label="History")
ax2.plot(x2, f(np.array(x2)), marker='o')

ax2.plot(result_s, f(result_s), 'o', label="Result")
ax2.set_title(f"Secant ({len(history_s)} runs, error: {error_s:.2f})")
ax2.legend()


# Move window to top left corner
move_figure(fig, 0, 0)

plt.show()
