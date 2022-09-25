import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import newton
import secant
import bisection


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


def f_nr(x):
    return (x - 1) * (x - 4)

def f_sec(x):
    return -1 * (x + 1) * (x - 3)

def f_bis(x):
    return (x + 2) * (x - 3) * (x - 2)

def f_dk(x):
    return x ** 4 - 3 * x ** 2 + x - 1

# =================================== ESTIMATION ===================================

# Newton-Raphson method ===================================
x0 = 8
result_nr, history_nr = newton.newton(f_nr, x0)
error_nr = abs(f_nr(result_nr))

# Secant line method    ===================================
# Ensure they intersect x axis, otherwise zero division error
x1 = -10
x2 = -7
result_s, history_s = secant.secant(f_sec, x1, x2)
error_s = abs(f_sec(result_s))

# Bisection method      ===================================
a = -9
b = 12
result_b, history_b = bisection.bisection(f_bis, a, b)
error_b = abs(f_bis(result_b))


# =================================== PLOTTING ===================================

# Plot the function
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))
fig.suptitle("Approximating roots through multiple methods")
x = np.linspace(-10, 10, 100)

# Ax1 ===================================
ax1.plot(x, f_nr(x), label="f(x)")
ax1.plot(history_nr, f_nr(np.array(history_nr)), marker='o', label="History")
ax1.plot(result_nr, f_nr(result_nr), 'o', label="Result", color="red")
ax1.set_title(f"Newton-Raphson ({len(history_nr)} runs, error: {error_nr:.2f})")
ax1.legend()


# Ax2 ===================================
ax2.plot(x, f_sec(x), label="f(x)")
# Plot history
# History formatted as [(x1, x2), (x2, x3), ...]
# Plot the x1 and x2 values
x1 = [x[0] for x in history_s]
x2 = [x[1] for x in history_s]
ax2.plot(x1, f_sec(np.array(x1)), marker='o', label="History")
ax2.plot(x2, f_sec(np.array(x2)), marker='o')
ax2.plot(result_s, f_sec(result_s), 'o', label="Result", color="red")
ax2.set_title(f"Secant ({len(history_s)} runs, error: {error_s:.2f})")
ax2.legend()


# Ax3 ===================================
ax3.plot(x, f_bis(x), label="f(x)")
ax3.plot(history_b, f_bis(np.array(history_b)), marker='o', label="History")
ax3.plot(result_b, f_bis(result_b), 'o', label="Result", color="red")
ax3.set_title(f"Bisection ({len(history_b)} runs, error: {error_b:.2f})")
ax3.legend()


# y = 0
ax1.plot(x, np.zeros(len(x)), color='#B1B1B1', alpha=0.75, linewidth=0.5)
ax2.plot(x, np.zeros(len(x)), color='#B1B1B1', alpha=0.75, linewidth=0.5)
ax3.plot(x, np.zeros(len(x)), color='#B1B1B1', alpha=0.75, linewidth=0.5)

# Move window to top left corner
move_figure(fig, 0, 0)

plt.show()
