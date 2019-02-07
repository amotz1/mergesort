import math

#[amotz] it seems to me that i now finished mergefragments function and it now work for your test cases i think (will soon check that but i checked for some other cases with empty lists)
def mergefragments(listl, listr):
    count = 0
    length_listl = len(listl)
    length_listr = len(listr)
    united = [None] * (length_listl + length_listr)
    index_l = 0
    index_r = 0
    index_united = 0
    while listl and listr:
        if listl[index_l] <= listr[index_r]:
            united[index_united] = listl[index_l]
            del listl[index_l]
            index_united = index_united + 1
            count = count + 1
            print('index_l =', index_l)
            print(not listl)
            print(not listr)
        elif listr[index_r] <= listl[index_l]:
            united[index_united] = listr[index_r]
            index_united = index_united + 1
            del listr[index_r]
            count = count + 1
            print(not listl)
            print(not listr)
    if listl:
        for i in range(len(listl)):
            print('listl[i] =', listl[i])
            print('united[index_united]= ', united[index_united])
            united[index_united] = listl[i]
            index_united = index_united + 1
    elif listr:
        for i in range(len(listr)):
            print(listr[i])
            print(united[index_united])
            united[index_united] = listr[i]
            index_united = index_united + 1
    return united


# [amotz] i tried to make the whole thing work but it seems i have some bug in the listspliter function which i am still unable to understand.
# after working with the debugger it seems that in the example below which is [8,5,2]
# it somehow split the list correctly but at the end for some reason i dont fully understand
# right now its not giving me the last listl and listr but the listl and listr in an earlier stage so i want to get in the example below [8],[5],[2] but i get [8], [5,2]
#which later fails to merge correctly in the mergefragment function because it needs sorted arrays
def listsplitter(list):
    n = len(list)
    if n < 2:
        return list
    mid = n / 2
    listl = [None] * int(math.floor(mid))
    listr = [None] * int(math.ceil((n - mid)))
    for i in range(0, int(math.floor(mid))):
        listl[i] = list[i]
    if (mid).is_integer() == False:
        for i in range(0, int(math.ceil((n - mid)))):
            listr[i] = list[int(math.ceil((n / 2) + i - 1))]
    else:
        if (mid).is_integer() == True:
            for i in range(0, int(math.ceil((n - mid)))):
                listr[i] = list[int(math.ceil((n / 2) + i))]
    listsplitter(listl)
    listsplitter(listr)
#    mergefragments(listl, listr)

listsplitter([8, 5, 2, ])
# listsplitter([3, 6, 7, 8, 5, 2, 2])

