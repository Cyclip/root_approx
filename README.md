# root_approx
Visualisation of different function root approximation methods

## Results
| ![Figure_1.jpg](https://github.com/Cyclip/root_approx/blob/main/repo/Figure_1.png?raw=true) | 
|:--:| 
| *Figure 1 - Different approximation methods visualised on different functions* |

| ![Figure_2.jpg](https://github.com/Cyclip/root_approx/blob/main/repo/Figure_2.png?raw=true) | 
|:--:| 
| *Figure 2 - Enlarged domain color map for Weierstrass method function* |

## Structure
```
src
 main.py             // Main python file for visualising all methods
 newton.py           // Newton-Raphson method module
 secant.py           // Secant line method module
 bisection.py        // Bisection method module
 durand_kerner.py    // Durand-Kerner method module
 map.py              // Complex domain colouring for the Durand-Kerner example function
 utils.py            // Constants
```

## Methods

### Newton-Raphson method
**Function**: $p(x) = \prod (x-r_i), x \in \mathbb{R}$  
The NR methods requires you to know the derivative of the function $f'(x)'$. We will instead use an approximation for the derivative by determining $h = 1e-6$ which will act similar to $f'(x)$ with a low margin of error. Given an initial value $x_0$, the iterative formula is defined by:
$$x_{n + 1} = x_n + \frac{f(x)}{f'(x)}$$
This will run until either it has reached `utils.MAX_RUNS` times, or until $|f(x_n)| < \alpha$. This is limited to finding 1 real root at a time, and has a chance of failure.

### Secant line method
**Function**: $p(x) = \prod (x-r_i), x \in \mathbb{R}$  
The Secant method uses a secant line (wherein it intersects $f(x)$ twice) given 2 points $x_1$ and $x_2$. It will identify the x-axis interception (when $y = 0$) giving $x3$. $x1$ is set to the value of $x2$, and $x2$ to $x3$. This will run until either it has reached `utils.MAX_RUNS` times, or until $|f(x_n)| < \alpha$. This is limited to finding 1 real root at a time. This has the chance of failure, and a possibility of dividing by 0 if the points do not intersect the x axis.

### Bisection method
**Function**: $p(x) = \prod (x-r_i), x \in \mathbb{R}$  
The bisection method takes in an inclusive interval $[a, b]$, selects the midpoint of the interval $c$ and determines whether the new interval should be the left ($[a, c]$) or right ($[c, b]$) interval. It does this by checking if the signs of $f(a)$ and $f(c)$ are the same (i.e. both are negative or positive). If so, the new interval is $[c, b]$; otherwise the new interval is $[a, c]$. This is limited to finding 1 real root at a time, but has a guaranteed success rate albeit its low performance.

### Durand-Kerner method (Weierstrass)
**Function**: $p(z) = \prod (z - r_n), z \in \mathbb{C}$  
Given a polynomial function $p(z) = (z - r^1)(z - r^2)(z - r^3)$ (not exponent), we can rearrange to solve for all roots:
$$r^1 = z - \frac{p(z)}{(z - r^2)(z - r^3)}$$
$$r^2 = z - \frac{p(z)}{(z - r^1)(z - r^3)}$$
$$r^3 = z - \frac{p(z)}{(z - r^1)(z - r^2)}$$
Which can be further rearranged into the 3 iterative formulae,
$$r^1_{n + 1} = r^1_n - \frac{p(x)}{(r^1_n - r^2_n)(r^1_n - r^3_n)}$$
$$r^2_{n + 1} = r^2_n - \frac{p(x)}{(r^2_n - r^1_n)(r^2_n - r^3_n)}$$
$$r^3_{n + 1} = r^3_n - \frac{p(x)}{(r^3_n - r^1_n)(r^3_n - r^2_n)}$$

First we create some $n$ initial guesses, where $n$ is the degree of $p(x)$. For $p(x)$ of degree $3$, this will look like
$$x = [1i, 2i, 3i] \textup{ where } x_n = r^n$$
We will then apply the formulae over multiple iterations.  

#### Visualisation
Due to the nature of the Weierstrass method, 2 subplots are used for the real and imaginary part.  
The first subplot consists of the real input $f(z), z \in \mathbb{R}$.  
The second subplot consists of the imaginary input where $f(z), z \in \mathbb{I}$.  
A domain colourmap is generated using the `magma` colourmap, since it will be a 4 dimensional graph (complex numbers are $a + bi$). On hte complex plane, the inputs will be mapped to the outputs as vectors. The angle of the vector will be represented as the colour, and the magnitude of the vector as the brightness (where lower magnitude is darker). This implies that the darkest points are the roots, whether complex or not.  
