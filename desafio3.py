import math

def taylor_sin(x):
    # Término 1: x
    term1 = x
    
    # Término 2: -x^3 / 3!
    term2 = - (x**3) / math.factorial(3)
    
    # Aproximación
    approximation = term1 + term2
    
    return approximation

# Valor de x
x = 0.2

# Calcular la aproximación
approximation = taylor_sin(x)

print(f"Aproximación de sin({x}) usando la serie de Taylor de tercer orden: {approximation}")
