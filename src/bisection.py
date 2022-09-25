def is_positive(val):
    return val >= 0


def bisection(f, a, b):
    """Approximate a root using the bisection method.
    We start with an interval [a, b] assuming a root is
    in between. It will continually bisect midpoint,
    modifying the [a, b] interval until it reaches an
    acceptable error.
    
    Args:
        f (function):   Function of whose root we should approximate
        a (float):      Start interval
        b (float):      End interval
    
    Returns:
        float:          Approximate root x value"""
    
    if a > b:
        return ValueError("b must be greater than a")
    
    c = (a + b) / 2

    history = []
    while abs(f(c)) > 1e-5:
        print("Bisection", c, f(c))
        if is_positive(f(a)) == is_positive(f(c)):
            a = c
        else:
            b = c
        
        c = (a + b) / 2
        history.append(c)
    
    return c, history