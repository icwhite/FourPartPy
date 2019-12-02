from inputter import *


def convert_to_number(piece):
    layout = str(piece)
    for measure in layout:
        for note in measure:
            note = note.number
    return layout


def check_difference(num):
    """given a nested list of numbers, see if there a num difference between the index of the list next to each other"""
    """first keep track of all the differences"""
    pass




def check_paralle_fifth(piece):
    """do things"""
    """There is a piece, which is displayed as a nested list"""
    """first, unfoil them, and then for each item, make them into their number"""
    #the unfoil process
    assert isinstance(piece, Piece), 'the input has to be a list dude'
    number_piece = convert_to_number(piece)
    check_difference(4)

def check_paralle_octave(Piece):
    assert isinstance(piece, Piece), 'the input has to be a list dude'
    number_piece = convert_to_number(piece)
    check_difference(0)

def has_third(Piece):
    pass
