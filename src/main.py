import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable

import newton
import secant
import bisection
from durand_kerner import durand_kerner as dk

def error(f, x):
    rv = abs(f(x))
    if not isinstance(rv, float):
        rv = sum(rv)
    
    return rv

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

def f_dk(z):
    """Roots are -4i, -2, 3j"""
    return (z**3 + 2*z**2 + 12*z + 24) + (z**2 + 2*z) * 1j


# Degree of f_dk
f_dk_deg = 3

# =================================== ESTIMATION ===================================

# Newton-Raphson method ===================================
x0 = 8
result_nr, history_nr = newton.newton(f_nr, x0)
error_nr = error(f_nr, result_nr)

# Secant line method    ===================================
# Ensure they intersect x axis, otherwise zero division error
x1 = -10
x2 = -7
result_s, history_s = secant.secant(f_sec, x1, x2)
error_s = error(f_sec, result_s)

# Bisection method      ===================================
a = -9
b = 12
result_b, history_b = bisection.bisection(f_bis, a, b)
error_b = error(f_bis, result_b)

# Durand Kerner method  ===================================
result_dk, history_dk = dk(f_dk, f_dk_deg)
error_dk = error(f_dk, result_dk)


# =================================== PLOTTING ===================================
# Gridspec for subplots
gs = gridspec.GridSpec(2, 3)

# CMap for plotting
c_white = matplotlib.colors.colorConverter.to_rgba('white',alpha = 0)
c_black= matplotlib.colors.colorConverter.to_rgba('black',alpha = 1)
cmap_rb = matplotlib.colors.LinearSegmentedColormap.from_list('rb_cmap',[c_black, c_white],512)

# Plot the function
fig = plt.figure(figsize=(12, 8))
fig.suptitle("Approximating roots through multiple methods")
x = np.linspace(-10, 10, 100)

# Ax1 ===================================
# Newton-Raphson method
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(x, f_nr(x), label="f(x)")
ax1.plot(history_nr, f_nr(np.array(history_nr)), marker='o', label="History")
ax1.plot(result_nr, f_nr(result_nr), 'o', label="Result", color="red")
ax1.set_title(f"Newton-Raphson ({len(history_nr)} runs, error: {error_nr:.2f})")
ax1.legend()


# Ax2 ===================================
# Secant line method
ax2 = fig.add_subplot(gs[0, 1])
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
# Bisection method
ax3 = fig.add_subplot(gs[0, 2])
ax3.plot(x, f_bis(x), label="f(x)")
ax3.plot(history_b, f_bis(np.array(history_b)), marker='o', label="History")
ax3.plot(result_b, f_bis(result_b), 'o', label="Result", color="red")
ax3.set_title(f"Bisection ({len(history_b)} runs, error: {error_b:.2f})")
ax3.legend()


# Ax4 ===================================
# Durand Kerner method (real part)
ax4 = fig.add_subplot(gs[1, 0])
ax4.plot(x, f_dk(x).real, label="f(x)")
ax4.plot(history_dk.real, f_dk(history_dk).real, marker='o', label="History")
ax4.plot(result_dk.real, f_dk(result_dk).real, 'o', label="Result", color="red")
ax4.set_title(f"Durand-Kerner (real) ({len(history_dk)} runs, error: {error_dk:.2f})")
ax4.legend()

# Ax5 ===================================
# Durand Kerner method (imaginary part)
ax5 = fig.add_subplot(gs[1, 1])

# Plot colormesh
x = np.linspace(-15, 15, 1000)
y = np.linspace(-15, 15, 1000)
X, Y = np.meshgrid(x, y)
Z = X + Y * 1j
F = f_dk(Z)
ax5.pcolormesh(X, Y, np.angle(F), cmap='hsv')
# Darken (brightness) the image based on magnitude
ax5.pcolormesh(X, Y, np.log(np.abs(F)), cmap=cmap_rb)

# Plot history
ax5.plot(history_dk.real, history_dk.imag, marker='o', label="History")
ax5.plot(result_dk.real, result_dk.imag, 'o', label="Result", color="red")
ax5.set_title(f"Durand-Kerner (imaginary) ({len(history_dk)} runs, error: {error_dk:.2f})")
ax5.legend()
ax5.set_aspect('equal')
ax5.set_ylabel("Imaginary")
ax5.set_xlabel("Real")

# y = 0
ax1.plot(x, np.zeros(len(x)), color='#B1B1B1', alpha=0.75, linewidth=0.5)
ax2.plot(x, np.zeros(len(x)), color='#B1B1B1', alpha=0.75, linewidth=0.5)
ax3.plot(x, np.zeros(len(x)), color='#B1B1B1', alpha=0.75, linewidth=0.5)
ax4.plot(x, np.zeros(len(x)), color='#B1B1B1', alpha=0.75, linewidth=0.5)

# Move window to top left corner
move_figure(fig, 0, 0)

plt.show()
