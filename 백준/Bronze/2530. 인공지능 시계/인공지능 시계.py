h, m, s = map(int, input().split())
t = int(input())

s += t % 60
t = t//60

if s>=60:
    s -= 60
    m += 1

m += t % 60
t = t//60
if m>=60:
    m -= 60
    t += 1

h += t % 24 
if h >= 24:
    h -= 24

print(h, m, s)