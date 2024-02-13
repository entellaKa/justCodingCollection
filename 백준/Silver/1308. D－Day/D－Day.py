import datetime

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

y = y2 - y1

if y > 1000:
    print('gg')
elif y == 1000 and (m1, d1) <= (m2, d2):
    print('gg')
else:
    today = datetime.date(y1, m1, d1)
    target_date = datetime.date(y2, m2, d2)

    d_day = target_date - today
    print(f"D-{d_day.days}")
