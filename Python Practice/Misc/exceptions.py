
def sqrt(x):
    if not isinstance(x,(int,float)):
        raise TypeError('x must be numeric')
    elif x < 0:
        raise ValueError('x cannot be negative')

    return (x*x)

print(sqrt('a'))