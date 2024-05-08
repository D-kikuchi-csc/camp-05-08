n = int(input())
s = []
for i in range(n):
    s += [int(input( ))]
a=0
b=0
f_point=[a,b]

for x in range(n):
    if x%4==0:
        f_point[1]+=s[x]
    elif x%4==1:
        f_point[0]+=s[x]
    elif x%4==2:
        f_point[1]-=s[x]
    else:
        f_point[0]-=s[x]
print (f_point[0],f_point[1])