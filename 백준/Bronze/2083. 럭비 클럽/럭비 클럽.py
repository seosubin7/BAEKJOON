while True:
    n, a, w = input().split()
    if '#' in n:
        break
    if int(a) > 17 or int(w) >= 80:
        print(f"{n} Senior")
    else:
        print(f"{n} Junior")