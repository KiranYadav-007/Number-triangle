l=[];m=[]
n=int(input("Enter list size: "))
for i in range(1,n+1):
    l.append(i)
    m.append(i)
for i in range(len(l)):
    print(" "*i,end="")
    for j in l:
        print(j,end=" ")
    del(l[0])
    print('\r')
x=len(m)-2;length=0
if(len(m)%2==0):
    length=len(m)//2
else:
    length=int((len(m)//2)+1)
for i in range(len(m)-2,-1,-1):
    print(" "*i,end="")
    y=m[x:len(m)]
    for j in y:
        print(j,end=" ")
    x-=1 
    print('\r')
    if(x<0):
        break
