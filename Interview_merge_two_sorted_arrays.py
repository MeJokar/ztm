"""
You are given the heads of two sorted lists list_1 and list_2.
Merge the two lists in a one sorted list. (Do NOT concatenate two list and sort them)
Return the merged list.

 

Example

 

List_1 = [3, 6, 8, 10]

List_2 = [2, 8, 9, 17, 23]

 

Answer: [2, 3, 6, 8, 8, 9, 10, 17, 23]

"""
# list3 = list1 + list2 ; list3.sort()
# non empty lists, lists include only numbrs, there can repitions, 

# we read the first element of each list ; l1_item ; l2_item 
# we creat list3 = []
# we comare l1_itme and l2_item, whichever is smaller will be appended to the list, and we update the temp items, 
# we hit the last item of either of the list, we can stop iterations, append 

def merge_and_sort_lists(list1, list2):

    counter1 = 0 # keep track of index in list 1
    counter2 = 0 # keep track of index in list 2
    l1 = len(list1)
    l2 = len(list2)
    list3 = []
    while counter1 < l1 and counter2 < l2:
        l1_temp = list1[counter1]
        l2_temp = list2[counter2]
        if l1_temp < l2_temp:
            list3.append(l1_temp)
            counter1 +=1        
        elif l2_temp < l1_temp:
            list3.append(l2_temp)
            counter2 +=1
        elif l1_temp == l2_temp:
            list3.append(l1_temp)
            counter1 +=1
            pass

    if counter1 == l1:
        list3 += list2[counter2:]
    else: 
        list3 += list1[counter1:]

    return list3

if __name__ == "__main__":
    List_1 = [3, 6, 8, 10]
    List_2 = [2, 8, 9, 17, 23]
    print(merge_and_sort_lists(List_1, List_2))

        




# we start from the end, pop 