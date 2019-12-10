`from piece_classes import *


def convert_to_number(measure):
    assert isinstance(measure, Measure), "input has to be of type Measure"
    note_numbers = []
    for chord in measure.chords:
        temp = []
        for voice in chord.voices:
            temp.append(voice.number)
        note_numbers.append(temp)
    return note_numbers

def expand_piece(piece):
    output_lst = []
    for measure in piece.measures:
        output_lst.extend(convert_to_number(measure))
    return output_lst


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
                if rest[elem]-first == num and first!="*" or rest!="*":
                    a_list.append([start, start+elem+1, first, rest[elem]])
            a_list.extend(check_each_elem(start+1, lst[1:], num))
            return a_list
    return helper(start, lst, num)


def check_difference(list, num):
    """check_difference([[1,1,3,5], [2,2,4,6]], 4)
    >>>[[[1,4,1,5], [2,4,1,5]], [[1,4,2,6], [2,4,2,6]]]"""

    """check_each_elem([1,1,3,5], 4)
    >>>[[1,4], [2,4]]"""

    lst_of_voices = []
    for elem in list:
        lst_of_voices.append(check_each_elem(1, elem, num))

    return lst_of_voices

def remove_common_tone(piece):
    """cadential_six_four = [[5, 5, 1, 3], [5, 5, 7, 2]]
    >>>[[*, *, 1, 3], [5, 5, 7, 2]]"""
    result = expand_piece(piece)
    for i in range(result):
        voice = 0
        while voice<4:
            if result[i][voice]==result[i+1][voice]:
                result[i][voice]="*"
            voice+=1
    return result


def check_and_print(voices_list, statement):
    #this part if very bad, I'm gonna fix this alter
    voice_num={1: soprano, 2: alto, 3: tenor, 4: bass}
    for chord in range(voices_list):
        first, second = voices_list[chord], voices_list[chord+1]
        min_len = min(len(first), len(second))
        for j in range(min_len):
            if first[j]==second[j]:
                first_voice, scond_voice = voice_num[first[j]], voice_num[second[j]]
                print ("there is a {0} fifth between {1}, and {2} between chord No.{3} and chord No.{4}". format(statement, first_voice, set_voice, chord, chord+1))


def check_intervals(Piece, num):
    assert isinstance(piece, Piece), 'the input has to be a list dude'
    number_piece_expanded = expand_piece(piece)
    voices_with_interval = []
    for chord in remove_common_tone(number_piece_expanded):
        voices_with_octave.append(check_difference(number_piece_expanded, num))
    return voices_with_interval


def check_paralle_fifth(Piece):
    result = check_intervals(Piece, 4)
    check_and_print(result, "fifth")

def check_paralle_octave(Piece):
    result = check_intervals(Piece, 0)
    check_and_print(result, "octave")



def has_third(Piece):
    result = check_intervals(Piece, 2)
    for chords in range(result):
        if len(chord)==0:
            print ("No thirds in chord No.{0}!". format(chord))
