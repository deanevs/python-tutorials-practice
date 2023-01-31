def example1(S):
    """Return the sum of the elements in Sequence S"""
    n = len(S)
    total = 0
    for j in range(n):
        total += S[j]
    return total

myset = (1,4,5,6,7,8)

print(example1(myset))