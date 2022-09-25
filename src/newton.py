import utils

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

    # repeat until f(x) is essentially 0
    x = x0
    history = [x,]

    runs = 0
    while abs(f(x)) > utils.ACCEPT_ERROR and runs < utils.MAX_RUNS:
        x -= f(x)/d(x)
        history.append(x)
        print(f"Newton {x:.5f} {d(x):.5f}")
        runs += 1
    
    return x, history