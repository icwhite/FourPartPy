from inputter import *


def convert_to_number(measure):
    assert isinstance(measure, Measure), "input has to be of type Measure"
    layout = str(measure)
    for chord in layout:
        for note in chord:
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
        #Maybe we should move this function outside the check_difference function idk
        a_list = []
        def helper(start, lst, num):
            nonlocal a_list
            first = lst[0]
            rest = lst[1:]
            if len(rest)==0:
                return []
            else:
                for elem in range(rest):
                    if rest[elem]-first == num:
                        a_list.append([start, start+elem+1])
                a_list.extend(check_each_elem(start+1, lst[1:], num))
                return a_list
        return helper(start, lst, num)

    for elem in list:
        lst_of_voices.append(check_each_elem(1, elem, num))

    return lst_of_voices


def check_paralle_fifth(piece):

    #the unfoil process
    assert isinstance(piece, Piece), 'the input has to be a list dude'
    for measure in repr(piece):
        number_piece = convert_to_number(measure) #[[1,1,3,5], [2,2,4,6]]
        check_difference(number_piece, 4) #[[[1,4], [2,4]], [[1,4], [2,4]]]
        #if the first list contains the same element as the one next to it, then there's a parelle fifth


def check_paralle_octave(Piece):
    assert isinstance(piece, Piece), 'the input has to be a list dude'
    for measure in repr(piece):
        number_piece = convert_to_number(measure) #[[1,1,3,5], [2,2,4,6]]
        check_difference(number_piece, 0) #[[[1,2]], [[1,2]]]
        #if the first list contains the same element as the one next to it, then there's a parelle fifth

def has_third(Piece):
    pass
