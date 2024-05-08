a=int(input())
b=list(map(int, input().split()))
c=list(map(int, input().split()))

T=""
for i in range(a):
    if b[i]==c[i]:
        T+=str(i+1)+" "

if len(T)!=0:print(T)
else:print("0")