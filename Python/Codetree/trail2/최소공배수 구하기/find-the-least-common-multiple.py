n, m = map(int, input().split())

a = max(n,m)
b = min(n,m)

while(b!=0):
    a,b = b,a%b

print(n*m//a)