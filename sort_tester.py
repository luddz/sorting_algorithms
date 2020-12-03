from selection_sort.selection_sort import selection_sort
from insertion_sort.insertion_sort import insertion_sort

def test_selection_sort(test_list):
    print("Before sorting: \n {}".format(test_list))
    sorted = selection_sort(test_list)
    print("After sorting: \n {}".format(sorted))

def test_insertion_sort(test_list):
    print("Before sorting: \n {}".format(test_list))
    sorted = insertion_sort(test_list)
    print("After sorting: \n {}".format(sorted))


if __name__ == '__main__':
    tmp = [2,3,3,3,3,3,2,2,2,1,1,1,0,4,5,6,7]
    test_selection_sort(tmp)
    test_insertion_sort(tmp)
