n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    dat, da, we = map(str,input().split())
    date.append(dat)
    day.append(da)
    weather.append(we)

class DDW:
    def __init__(self,date,day,weather):
        self.date=date
        self.day=day
        self.weather=weather

listddw = []

for i in range(n):
    ddw = DDW(date[i], day[i], weather[i])
    if weather[i] == "Rain":
        listddw.append(ddw)
    
listddw.sort(key=lambda x: x.date)
target = listddw[0]
print(f"{target.date} {target.day} {target.weather}")

