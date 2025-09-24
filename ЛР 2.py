def f(x):
    return x**4 + 2*x**3 + 2*x**2 + 6*x - 3

def derivative2(x):
    return 12*x**2 + 12*x + 4

# Метод половинного ділення
def bisection(a, b, eps):
    if f(a) * f(b) > 0:
        return None
    while (b - a) > eps:
        mid = (a + b) / 2
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2

# Метод хорд 
def chord(a, b, eps):
    if f(a) * f(b) > 0:
        return None
    
    if f(a) * derivative2(a) > 0:
        x0 = a
        x = b
    else:
        x0 = b
        x = a
    
    while True:
        x_new = x - f(x) * (x - x0) / (f(x) - f(x0))
        if abs(x_new - x) < eps:
            return x_new
        x = x_new  

eps = 0.0001
root_bisect = bisection(0, 1, eps)
root_chord = chord(0, 1, eps)

print(f"Метод половинного ділення: x = {root_bisect:.5f}")
print(f"Метод хорд: x = {root_chord:.5f}")
print(f"f(корінь) = {f(root_bisect):.7f}")