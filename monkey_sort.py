import random
def is_sorted(L):
    for i in range(len(L)-1):
        if L[i]>L[i+1]:
            return False
        return True
def monkey_sort(L):
    random.shuffle(L)

    if is_sorted(L):
        print(L)
    else:
        monkey_sort(L)

K=list(range(12))
print(monkey_sort(K))
