from math import ceil, floor
from typing import List


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
            # [Aviv] I would refactor this. That is, I'd move this duplicated line to be in the while each time rather
            # than in each case.
            count = count + 1
        #   print('index_l =', index_l)
        #   print(not listl)
        #   print(not listr)
        elif listr[index_r] <= listl[index_l]:  # [Aviv] I think that this should just be "else"
            united[index_united] = listr[index_r]
            index_united = index_united + 1
            del listr[index_r]
            count = count + 1
        #   print(not listl)
        #   print(not listr)
    assert listl or listr, \
        'One of the lists should have elements remaining. ' \
        '(The while loop above stops running when one lists runs out of elemnts.)'
    if listl:
        for i in range(len(listl)):
            #   print('listl[i] =', listl[i])
            #   print('united[index_united]= ', united[index_united])
            united[index_united] = listl[i]
            index_united = index_united + 1
    elif listr:  # [Aviv] I think that this should just be "else"
        for i in range(len(listr)):
            #    print(listr[i])
            #   print(united[index_united])
            united[index_united] = listr[i]
            index_united = index_united + 1
    return united


# [amotz] this is the listsplitter function, again working.
# [Aviv] I'd rename this to be a verb, so for example, splitLists
# [Aviv] I'm not sure how these return value "hints" work, but I added this, and it didn't seem to break anything.
def listsplitter(list) -> List[List[int]]:
    n = len(list)
    mid = n / 2  # [Aviv] I would move the floor function to here and not use it below.
    listl = [None] * int(floor(mid))
    listr = [None] * int(ceil((n - mid)))
    for i in range(0, int(floor(mid))):
        listl[i] = list[i]
    if (mid).is_integer() == False:
        for i in range(0, int(ceil((n - mid)))):
            listr[i] = list[int(ceil((n / 2) + i - 1))]
    else:
        if (mid).is_integer() == True:
            for i in range(0, int(ceil((n - mid)))):
                listr[i] = list[int(ceil((n / 2) + i))]
    return listl, listr


def mergeSort(list: int) -> List[int]:
    if len(list) < 2:
        return list
    # [Aviv]. Sorry, I got carried away. Since the function above returns 2 things (which is a rare language feature)
    # I chnaged the usage of it here to assign 2 things. (above says "return a, b", and so here I say "a, b = call()"
    unsortedLeft, unsortedRight = listsplitter(list)
    sortedLeft = mergeSort(unsortedLeft)
    sortedRight = mergeSort(unsortedRight)
    mergeSorted = mergefragments(sortedLeft, sortedRight)
    return mergeSorted


# [amotz] the only thing that is not completed i think is that it seems i get some weird assertion error.
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

    testCase: List[int]
    for testCase in testCases:
        # print("in\t", testCase)
        mergeSorted = mergeSort(testCase)
        # print("out\t", mergeSorted)
        referenceSorted: List[int] = sorted(testCase)
        # [Aviv] This use of "==" is really confusing to me. I'm used to == being used to check if the 2 are the *same*
        # objects, not if they're "equal". But I don't know Python.
        if mergeSorted != referenceSorted:
            print("Wrong: %s != %s" % (mergeSorted, referenceSorted), end=' ')
            assert False
        else:
            print("Right! %s sorted = %s" % (testCase, mergeSorted))


test()
