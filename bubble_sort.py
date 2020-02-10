import time
def bubble(L):
    print("L before sorting",L)
    for i in range(len(L)-1):
        print("This is the",i,"pass")
        time.sleep(2)
        for j in range(len(L)-1-i):
            print("j is",L[i],"j+1 is",L[i+1])
            time.sleep(2)
            
            if L[j]>L[j+1]:
                print("Since ",L[j],"is greater than",L[j+1])
                print("swap")
                L[j],L[j+1]=L[j+1],L[j]
            print("After the inner loop")
        print("After ",i,"pass now the list",L)

    print(L)
            




L=[12,23,14,11,10,55,2]
bubble(L)
