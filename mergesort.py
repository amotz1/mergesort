import math


# [amotz] this is the merge fragment function, it is now working
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
        #   print('index_l =', index_l)
        #   print(not listl)
        #   print(not listr)
        elif listr[index_r] <= listl[index_l]:
            united[index_united] = listr[index_r]
            index_united = index_united + 1
            del listr[index_r]
            count = count + 1
        #   print(not listl)
        #   print(not listr)
    if listl:
        for i in range(len(listl)):
            #   print('listl[i] =', listl[i])
            #   print('united[index_united]= ', united[index_united])
            united[index_united] = listl[i]
            index_united = index_united + 1
    elif listr:
        for i in range(len(listr)):
            #    print(listr[i])
            #   print(united[index_united])
            united[index_united] = listr[i]
            index_united = index_united + 1
    return united


# [amotz] this is the listsplitter function, again working.
def listsplitter(list):
    n = len(list)
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
    return listl, listr

#[amotz] this is the sort function that you wanted me to write in our last conversation,
# it seems to work on all the test cases below...
def sort(list):
    if len(list) < 2:
        return list
    listlr = listsplitter(list)
    listl = sort(listlr[0])
    listr = sort(listlr[1])
    list = mergefragments(listl, listr)
    return list

#[amotz] the only thing that is not completed i think is that it seems i get some weird assertion error.
# without the assertion the test function seems to run smoothly without errors
# and give correct answer for all the test cases, but somehow if i run the program with the assertion
# it stops the program when it hit the [] testcase and then it throws off an assertion error...
def test():
    testCases = [[3, 5, 11, 3, 13],
                 [7, 8, 7, 9, 5, 2],
                 [6, 8, 8, 5, 4, 3],
                 [6, 8, 9, 9, 4, 3],
                 [8, 6, 6, 6, 9, 3, 2, 1, 2],
                 [1, 2, 3],
                 [3, 2, 1],
                 [],
                 [1],
                 [1, 1, 1]]

    for testCase in testCases:
        print("in\t", testCase)
        sort(testCase)
        print("out\t", sort(testCase))
        if sort(testCase) == sorted(testCase):
            print("you got it right")
            assert (sort(testCase))


test()
