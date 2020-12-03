def test_selection_sort():
    empty_list = []
    print(selection_sort(empty_list))

    tmp = [2,3,3,3,3,3,2,2,2,1,1,1,0,4,5,6,7]
    print(tmp)
    print(selection_sort(tmp))

def selection_sort(to_sort):
    list_length = len(to_sort)
    for i in range(list_length):
        smallest_index = i
        for j in range(i, list_length):
            if to_sort[j] <  to_sort[smallest_index]:
                smallest_index = j

        if smallest_index != i:
            tmp = to_sort[smallest_index]
            to_sort[smallest_index] = to_sort[i]
            to_sort[i] = tmp

    return to_sort


test_selection_sort()
