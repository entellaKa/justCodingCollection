width = 'ABCDEFGH'
height = '12345678'

def moveable(p, c):
    if p[0] == 'A' and 'L' in c:
        return False
    elif p[0] == 'H' and 'R' in c:
        return False
    elif p[1] == '1' and 'B' in c:
        return False
    elif p[1] == '8' and 'T' in c:
        return False
    else:
        return True

def move(p, c):
    w = p[0]
    h = p[1]
    if 'L' in c:
        w = width[width.index(w) - 1]
    if 'R' in c:
        w = width[width.index(w) + 1]
    if 'B' in c:
        h = height[height.index(h) - 1]
    if 'T' in c:
        h = height[height.index(h) + 1]

    return w+h

king, pawn, n = input().split()

for i in range(int(n)):
    m = input()
    if moveable(king, m):
        if move(king, m) == pawn:
            if moveable(pawn, m):
                pawn = move(pawn, m)
                king = move(king, m)
        else:
            king = move(king, m)
print(king)
print(pawn)


