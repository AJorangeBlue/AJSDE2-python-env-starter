def fatorial(n):
    result = n
    current = n
    while current > 0:
        current =- 1
        result = result * current
    return result

print(fatorial(3))

def fac_resursive(m):
    if m == 0:
        return 1
    else:
        return m * fac_resursive(m-1)
    
print(fac_resursive(3))