def getAnswer(cards, goal, i):
    if i < 0:
        return goal
    an = goal - cards[0]

    for c in range(len(cards)-i):
        t = getAnswer(cards[c+1:], goal-cards[c], i-1)
        if 0 <= t < an:
            an = t
    return an


n, goal = map(int, input().split(" "))
cards = list(map(int,input().split(" ")))

print(goal-getAnswer(cards, goal, 2))