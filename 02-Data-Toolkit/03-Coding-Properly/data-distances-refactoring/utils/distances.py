import math

def manhattan(a,b):
    distance = abs(b[0] - a[0]) + abs(b[1] - a[1])
    return distance


def euclidean(a, b):
    distance = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    return distance
