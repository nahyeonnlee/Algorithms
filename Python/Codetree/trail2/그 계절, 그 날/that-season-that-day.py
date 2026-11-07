Y, M, D = map(int, input().split())

if (Y%4==0 and Y%100!=0) or (Y%400==0):
    is_yn = True
else:
    is_yn = False

if M in (3,4,5):
    if M==4 and D==31:
        print(-1)
    else:
        print("Spring")

elif M in (6,7,8):
    if M==6 and D==31: 
        print(-1)
    else:
        print("Summer")

elif M in (9,10,11):
    if M in (9,11) and D==31:
        print(-1)
    else:
        print("Fall")

else:
    if M==2 and (D > 29 or (is_yn == False and D==29)):
        print(-1)
    else:
        print("Winter")