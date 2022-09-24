import numpy as np

def deriv(f):
    """Calculate the derivative of a function.

    Args:
        f (function): Function to calculate the derivative of.

    Returns:
        function: Derivative of the function.
    """
    return lambda x: (f(x + 1e-6) - f(x)) / 1e-6

def newton(f, x0):
    """Approximate the root of a function using Newton-Raphson method.
    
    Args:
        f (function):   Function to estimate root of
        x0 (float):     Initial x value
    
    Returns:
        float: Approximated root x value"""

    d = deriv(f)

    # repeat until the gradient at x is essentially 0
    x = x0
    history = [x,]
    while abs(d(x) > 1e-5):
        x -= f(x)/d(x)
        history.append(x)
        print(f"Current x: {x}, dy/dx = {d(x)}")
    
    return x, history