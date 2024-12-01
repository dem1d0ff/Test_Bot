import math

def BLH_XYZ(a, e_2, B, L, H):
    B = math.radians(B)
    L = math.radians(L)
    H = H
    N = a / math.sqrt(1 - e_2 * (math.sin(B)) ** 2)
    X = (N + H) * math.cos(B) * math.cos(L)
    Y = (N + H) * math.cos(B) * math.sin(L)
    Z = (N * (1 - e_2) + H) * math.sin(B)
    return (round((X), 3)), (round((Y), 3)), (round((Z), 3))