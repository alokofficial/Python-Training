#flattering of list
a=[1,[2,3],[1,3,4,5],[1,2]]
x=[]
for i in a:
    if type(i)==list:
        x.extend(i)
    else:
        x.append(i)
print(x)
