def Merge_sorted_arrays(array1, array2):
    if type(array1) != list or type(array2) != list:
        print('Invalid input')
    elif not array1:
        return array2
    elif not array2:
        return array1
    else:
        merged_array = []
        array1_item = array1[0]
        array2_item = array2[0]
        i =1 ; j = 1;
        while i < len(array1) and j < len(array2):
            print(array1_item, array2_item)
            if array1_item < array2_item:
                merged_array.append(array1_item)
                array1_item = array1[i]
                i +=1
            else:
                merged_array.append(array2_item)
                array2_item = array2[j]
                j += 1 
        print(i,j, 'here')
        if   i == len(array1):
            merged_array += array2[j-1:]
        elif j == len(array2): 
            merged_array += array1[i-1:]


        return merged_array
    
if __name__ == '__main__':
    print(Merge_sorted_arrays([0,4,6,31], [4,6,6,30]))
    aa = [3,4,5]