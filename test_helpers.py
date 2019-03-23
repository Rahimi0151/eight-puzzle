import pytest
import Helpers

def test_it_copies_a_list_correctly():
    list1 = [1,2,3,4,5]
    list2 = Helpers.copy_list(list1)

    assert list1 == list2
    
def test_it_shuffles_correctly():
    list1 = [1,2,3,4,5,6,7,8,9]
    list2 = Helpers.shuffle( list1 )

    # they are not equal...
    assert not list1 == list2

    # but they have the same elements
    for x in list2:
        assert x in list1





