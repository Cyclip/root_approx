import numpy as np
import utils

def prod_diff(x, i):
    """Product of the differences in all elements of list against i, excluding i"""
    return np.prod(
        x[i] - x[x != x[i]]
    )

def durand_kerner(f, deg):
    """
    Approximate the roots of a polynomial function using the Durand-Kerner method.
    
    Given p(x) = (x - a)(x - b)(x - c) for example,
        aₙ₊₁ = aₙ - p(aₙ)/(aₙ - bₙ)(aₙ - cₙ)
        bₙ₊₁ = bₙ - p(bₙ)/(bₙ - aₙ)(bₙ - cₙ)
        cₙ₊₁ = cₙ - p(cₙ)/(cₙ - aₙ)(cₙ - bₙ)
    """

    # Evenly distributed initial guesses along a circle
    # For now we pick random complex points
    x = np.array([1j * i for i in range(1, deg + 1)])
    history = np.array(x)

    for i in range(utils.MAX_RUNS):
        for i in range(len(x)):
            x[i] -= f(x[i]) / prod_diff(x, i)
        
        print(x)
        history = np.append(history, x)
    
    return x, history
