#fibonacci series
n=20
a,b=0,1
for i in range (n):
    print(a,end=' ')
    a,b=b,a+b
    
#fibonacci series
limit=100
a=0
b=1
while a<limit:
    print(a,end=' ')
    a,b=b,a+b
    
#pallindrom
s="good"
if s==s[::-1]:
    print("palindrom")
else:
    print("not palindrom")

s="262"
if s==s[::-1]:
    print("palindrom")
else:
    print("not palindrom")

#right angle triangle
n=5
for i in range(1,n+1):
    print('*'*i)

#reverted right angle triangle
n=5
for i in range(5,0,-1):
    print('*'*i)
    
# triangle
n=5
for i in range(5,0,-1):
    print(i)
    
#pyramid
n=5
for i in range(1,n+1):
    print(' '*(n-i)+'*'*(2*i-1))

for i in range(n-1,0,-1):
    print(' '*(n-i)+'*'*(2*i-1))

n=5
for i in range (n):
    print('*',i*i)


for i in range(10):
    for j in range(10):
        print('*',end='')
    print()

for i in range(1,10+1):
    for j in range(1,10+1):
        if i==1 or i==10 or j==1 or j==10:
            print('*',end='')
        else:
            print(' ',end='')
    print()

for i in range(7):
    for j in range(7):
        print('*',end=' ')
    print()
