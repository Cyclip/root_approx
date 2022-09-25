import utils

def gradient(f, x1, x2):
    """Calculate the gradient for a given function and 2 points"""
    y1, y2 = f(x1), f(x2)

    return (y2 - y1)/(x2 - x1)

def x_intercept(m, x, y):
    """
    Proof:
    y - y1 = m(x - x1)
    y = mx - mx1 + y1

    y = mx + c
    Given that y = 0,
        0 = mx + c
        => x = -c/m

    let c = -mx1 + y1

    x = -(-mx1 + y1)   / m
    = (mx1 - y1)  / m
    
    Args:
        m (float):  Gradient
        x (float):  x point
        y (float):  y point
    
    Returns:
        float:  x intercept
    """

    return (m * x - y) / m

def secant(f, x1, x2):
    """Approximates the root of a given function through
    the Secant line method.
    
    Args:
        f (function):   Function to estimate the root of
        x1 (float):     Initial x value
        x2 (float):     Initial x value
    
    Returns:
        float: Approximated root value"""
    
    # Repeat until the absolute difference between
    # x1 and x2 are negligible
    history = [(x1, x2),]
    runs = 0
    while abs(x1 - x2) > utils.ACCEPT_ERROR and runs < utils.MAX_RUNS:
        # Identify x-axis intersection
        m = gradient(f, x1, x2)
        x3 = x_intercept(m, x1, f(x1))

        # Update x1, x2 with given intersection value
        # Shift it all left, i.e. x1 replaced by x2 and x2 by x3
        x1 = x2
        x2 = x3

        history.append((x1, x2))
        print(f"Secant {x1}-{x2}")
        runs += 1
    
    return x2, history