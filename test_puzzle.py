import pytest
import Helpers
from Puzzle import Puzzle

def test_if_the_swapable_parts_are_correct():
    puzzle = Puzzle()
    
    # 1st row
    assert puzzle.is_swapable(1,2) == True
    assert puzzle.is_swapable(2,1) == True
    assert puzzle.is_swapable(2,3) == True
    assert puzzle.is_swapable(3,2) == True
    assert puzzle.is_swapable(1,3) == False
    assert puzzle.is_swapable(3,1) == False
    # 2nd row
    assert puzzle.is_swapable(4,5) == True
    assert puzzle.is_swapable(5,4) == True
    assert puzzle.is_swapable(5,6) == True
    assert puzzle.is_swapable(6,5) == True
    assert puzzle.is_swapable(4,6) == False
    assert puzzle.is_swapable(6,4) == False
    # 3rd row
    assert puzzle.is_swapable(7,8) == True
    assert puzzle.is_swapable(8,7) == True
    assert puzzle.is_swapable(8,9) == True
    assert puzzle.is_swapable(9,8) == True
    assert puzzle.is_swapable(7,9) == False
    assert puzzle.is_swapable(9,7) == False

def test_if_the_neigbours_are_correct():
    puzzle = Puzzle()

    assert puzzle.are_neigbours(4,1)
    assert puzzle.are_neigbours(6,9)
    assert puzzle.are_neigbours(4,1)
    assert puzzle.are_neigbours(2,3)
    assert puzzle.are_neigbours(7,8)
    assert puzzle.are_neigbours(4,5)
    assert puzzle.are_neigbours(4,7)
    assert puzzle.are_neigbours(2,1)
    assert puzzle.are_not_neigbours(8,4)
    assert puzzle.are_not_neigbours(5,1)
    assert puzzle.are_not_neigbours(5,1)
    assert puzzle.are_not_neigbours(3,9)
    assert puzzle.are_not_neigbours(9,2)
    assert puzzle.are_not_neigbours(3,5)
    assert puzzle.are_not_neigbours(4,6)

def test_it_can_switch_correctly():
    puzzle = Puzzle()
    first_element = 2
    second_element = 3
    board1 = puzzle.board
    board2 = Helpers.copy_list( board1 )

    puzzle.swap( first_element , second_element )

    for x in range( 0 , len(board1)-1 ):
        # Except for the two swaped elements...
        if (x == first_element or
            x == second_element):
            continue
        # Other elements should be the same
        assert board1[x] == board2[x]

def test_it_can_check_if_player_won():
    puzzle = Puzzle()

    assert puzzle.won() == False
    puzzle.board = [None,None,1,2,3,4,5,6,7,8]
    assert puzzle.won() == True

def test_it_can_move_correctly_and_raise_appropiate_exception():
    puzzle = Puzzle()
    puzzle.board = [None,None,1,2,3,4,5,6,7,8]

    puzzle.move(2)
    assert puzzle.board == [None,1,None,2,3,4,5,6,7,8]
    
    puzzle.move(5)
    assert puzzle.board == [None,1,4,2,3,None,5,6,7,8]

    with pytest.raises(Exception):
        puzzle.move(1)
    assert puzzle.board == [None,1,4,2,3,None,5,6,7,8]

def test_it_count_tries_correctly():
    puzzle = Puzzle()
    puzzle.board = [None,None,1,2,3,4,5,6,7,8]

    assert puzzle.tries == 0
    puzzle.move(2)
    assert puzzle.tries == 1
    puzzle.move(5)
    assert puzzle.tries == 2

    with pytest.raises(Exception):
        puzzle.move(1)
    assert puzzle.tries == 2
