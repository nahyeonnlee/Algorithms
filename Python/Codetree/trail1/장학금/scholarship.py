score = list(map(int,input().split()))

if score[0] >= 90:
    if score[1] >= 95:
        print("100000")
    elif score[1] >= 90:
        print("50000")
    else:
        print("0")
else:
    print("0")
