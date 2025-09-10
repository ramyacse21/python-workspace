    a=[5,6,2,3]
    l=len(a)
    temp=[]
    for i in range(l):
        b=a[0]
        index=0
        for j in range(len(a)):
            if a[j] < b:
                b=a[j]
                index=j
        temp.append(b)
        a.pop(index)
    print(temp)    
