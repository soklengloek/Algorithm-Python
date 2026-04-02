def solve(a, b):
    """
    Solves the equation of ax + b = 0
    Returns the value of x
    """
    if a == 0:
        if b == 0:
            return "Infinite solutions"
        else:
            return "No solution"
    x = -b / a
    return x
# Example
a = 2
b = 4
result = solve(a, b)
print(f"For equation {a}x + {b} = 0")
print(f"x = {result}")