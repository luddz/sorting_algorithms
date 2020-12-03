from selection_sort.selection_sort import selection_sort


def test_selection_sort():
    empty_list = []
    print(selection_sort(empty_list))

    tmp = [2,3,3,3,3,3,2,2,2,1,1,1,0,4,5,6,7]
    print(tmp)
    print(selection_sort(tmp))


if __name__ == '__main__':
    test_selection_sort()
