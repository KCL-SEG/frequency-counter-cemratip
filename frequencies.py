def frequencies(items):
    frequencies = {}
    for item in items:
        frequencies[str(item)] = 0
    for item in items:
        frequencies[str(item)] += 1
    return frequencies