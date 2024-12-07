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

def XYZ_BLH(a, e_2, X, Y, Z):
    Q = math.sqrt(float(X) ** 2 + float(Y) ** 2)
    B = math.atan(float(Z) / (Q * (1 - e_2)))  # первая итерация для B
    N = a / math.sqrt(1 - e_2 * (math.sin(B) ** 2))
    H = (Q / (math.cos(B)) - N)
    x = 1
    while x <= 7:
        B = math.atan(float(Z) / (Q * (1 - (N * e_2) / (N + H))))  # вторая итерация для B
        N = a / math.sqrt(1 - e_2 * (math.sin(B) ** 2))
        H = (Q / (math.cos(B)) - N)
        x = x + 1

    L = math.atan(float(Y) / float(X))
    if float(X) > 0 and float(Y) > 0 and float(Z) > 0:
        L = L
    elif float(X) < 0 and float(Y) > 0 and float(Z) > 0:
        L = L + math.radians(180)
    elif float(X) < 0 and float(Y) > 0 and float(Z) < 0:
        L = L + math.radians(180)
    elif float(X) < 0 and float(Y) < 0 and float(Z) > 0:
        L = L - math.radians(180)
    elif float(X) < 0 and float(Y) < 0 and float(Z) < 0:
        L = L - math.radians(180)
    else:
        L = L

    return (round(math.degrees(B), 9)), (round(math.degrees(L), 9)), (round((H), 3))