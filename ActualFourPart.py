from inputter import *


def convert_to_number(piece):
    assert isinstance(piece, Piece), "input has to be of type Piece"
    layout = str(piece)
    for measure in layout:
        for note in measure:
            note = note.number
    return layout


def check_difference(list, num):
    """check_difference([[1,1,3,5], [2,2,4,6]], 4)
    >>>[[[1,4], [2,4]], [[1,4], [2,4]]]"""

    """check_each_elem([1,1,3,5], 4)
    >>>[[1,4], [2,4]]"""
    
    lst_of_voices = []
    def check_each_elem(start, lst, num):
        #check the difference of one single list
        #return a nested list of index
        "do stuff"
        check_each_elem(start+1, lst[1:], num)

    for elem in list:
        lst_of_voices.append(check_each_elem(1, elem, num))











def check_paralle_fifth(piece):
    """do things"""
    """There is a piece, which is displayed as a nested list"""
    """first, unfoil them, and then for each item, make them into their number"""
    #the unfoil process
    assert isinstance(piece, Piece), 'the input has to be a list dude'
    number_piece = convert_to_number(piece)
    check_difference(number_piece, 4)

def check_paralle_octave(Piece):
    assert isinstance(piece, Piece), 'the input has to be a list dude'
    number_piece = convert_to_number(piece)
    check_difference(number_piece, 0)

def has_third(Piece):
    pass
