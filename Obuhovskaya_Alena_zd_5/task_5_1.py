
def generator_odd(to_odd):
    for odd in range(1, to_odd+1, 2):
        yield odd

g_odd = generator_odd(17)
print(next(g_odd))
print(next(g_odd))
print(next(g_odd))
print(next(g_odd))
print(next(g_odd))
print(next(g_odd))
print(next(g_odd))
print(next(g_odd))
print(next(g_odd))
print(next(g_odd))


