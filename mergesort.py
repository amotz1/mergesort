import math
def amotzmergesort(list):
    n = len(list)
    if n < 2:
        return list
    mid = n/2
    listl = [None] * int(math.floor(mid))
    listr= [None] * int(math.ceil((n-mid)))
    for i in range(0, int(math.floor(mid))):
        listl[i] = list[i]
    if (mid).is_integer() == False:
        for i in range(0, int(math.ceil((n-mid)))):
            listr[i] = list[int(math.ceil((n/2)+i-1))]
    else:
        if (mid).is_integer() == True:
            for i in range(0, int(math.ceil((n - mid)))):
                listr[i] = list[int(math.ceil((n / 2) + i))]
    amotzmergesort(listl)
    print(listl)
    amotzmergesort(listr)
    print(listr)

amotzmergesort(list)
print(list)






