import math

#[amotz] this suppose to be the function that split recursively the array (list in python), i think this is working.
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
    print(listl)
    listsplitter(listr)
    print(listr)
listsplitter ([3,6,7,8,5,2,2)



#[amotz] this is supposed to be the function that will merge the fragments to a sorted list so in the end i will call it from my listsplitter function,
# it is still not working though,
#the algorithm is getting confused i think because i delete each iteration of the loop an index in the list so it says
# an error list index out of range in line 39
# but i am not sure yet and it is work in progress
def mergefragments(listl, listr):
    count = 0
    length_listl = len(listl)
    length_listr = len(listr)
    united = [None] * (length_listl + length_listr)
    index_l = 0
    index_r = 0
    index_united = 0
    while index_l < length_listl and index_r < length_listr:
        if listl[index_l] < listr[index_r]:
            united[index_united] = listl[index_l]
            del listl[index_l]
            index_l = index_l + 1
            index_united = index_united + 1
            count = count + 1
            print('index_l =', index_l)
        elif listr[index_r] < listl[index_l]:
            united[index_united] = listr[index_r]
            index_united = index_united + 1
            del listr[index_r]
            index_r = index_r + 1
            count = count + 1
    if index_l == length_listl:
        for i in range(len(listl)):
            print('listr[i] =', listr[i])
            united[i + count] = listr[i]
    elif index_r == length_listr:
        for i in range(len(listr)):
            listl[i] == united[i]
    return united


print(mergefragments([3, 4, 5], [2, 8, 9]))
