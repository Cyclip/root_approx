import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def f_dk(z):
    return (z**3 + 2*z**2 + 12*z + 24) + (z**2 + 2*z) * 1j


c_white = matplotlib.colors.colorConverter.to_rgba('white',alpha = 0)
c_black= matplotlib.colors.colorConverter.to_rgba('black',alpha = 1)
cmap_rb = matplotlib.colors.LinearSegmentedColormap.from_list('rb_cmap',[c_black, c_white],512)


x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)
X, Y = np.meshgrid(x, y)
Z = X + Y * 1j
F = f_dk(Z)
plt.figure()
plt.title("Domain color plot")
plt.pcolormesh(X, Y, np.angle(F), cmap='hsv')
# Darken (brightness) the image based on magnitude
plt.pcolormesh(X, Y, np.log(np.abs(F)), cmap=cmap_rb)
plt.colorbar()
plt.show()
