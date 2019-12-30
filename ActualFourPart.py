from piece_classes import *


def convert_to_number(measure):
    """measure_with_one_chord = Measure(1)
    c_major_triad = Chord(C3, C4, G4, E4)
    measure_with_one_chord.add_chord(c_major_triad)
    convert_to_number(measure_with_one_chord)
    >>>[1, 1, 3.5, 2]"""
    assert isinstance(measure, Measure), "input has to be type Measure"
    note_numbers = []
    for chord in measure.chords:
        temp = []
        for voice in list(chord.voices.values()): #each voice is an instance of the class Note
            temp.append(voice.number%12)
        note_numbers.append(temp)
    print(note_numbers)
    return note_numbers

def expand_piece(piece):
    output_lst = []
    for measure in piece.measures:
        output_lst.extend(convert_to_number(measure))
    return output_lst

def remove_common_tone(piece):
    """cadential_six_four = [[5, 5, 1, 3], [5, 5, 7, 2]]
    >>>[[*, *, 1, 3], [5, 5, 7, 2]]"""
    assert isinstance(piece, Piece), "the input has to be an instance of Piece"
    result = expand_piece(piece) #here the piece is expanded
    if len(result)==1:
        return result
    for i in range(len(result)-1):
        voice = 0
        while voice<3:
            if result[i][voice]==result[i+1][voice]:
                result[i][voice]="*"
            voice+=1
    return result


def check_each_elem(start, lst, num):
    #check the difference of one single list
    #return a nested list of index
    """check_each_elem(1, [1,1,3,5], 4)
    >>>[[1,4], [2,4]]"""

    a_list = []
    def helper(start, lst):
        nonlocal a_list
        first = lst[0]
        rest = lst[1:]
        if len(rest)==0:
            return a_list
        else:
            for elem in range(len(rest)):
                if rest[elem]-first == num: #and (first!='*' or rest!='*'):
                    a_list.append([start, start+elem+1])
            a_list.extend(helper(start+1, lst[1:]))
            return a_list
    return helper(start, lst)



def check_intervals(piece, num):
    """return a list of voices that has the designated interval"""
    """check_intrvals([[1,1,3,5], [2,2,4,6]], 4)
    >>>[[[1,4], [2,4]], [[1,4], [2,4]]]"""
    assert isinstance(piece, Piece), 'the input has to be a piece dude'
    reviesed_piece = remove_common_tone(piece)
    voices_with_interval = []
    for chord in reviesed_piece:
        voices_with_interval.append(check_each_elem(1, chord, num))
    return voices_with_interval


def check_and_print(voices_list, statement):
    #this part is very bad, I'm gonna fix this alter
    """check the processed voice list, and print out a statement if there is a parallel something"""
    voice_num={1: 'soprano', 2: 'alto', 3: 'tenor', 4: 'bass'}
    if len(voices_list)==1:
        print ('Done')
        return None
    for chord in range(len(voices_list)-1):
        first, second = voices_list[chord], voices_list[chord+1]
        min_len = min(len(first), len(second))
        for j in range(min_len):
            if first[j]==second[j]:
                #first_voice, scond_voice = voice_num[first[j]], voice_num[second[j]]
                print ("there is a parallel {0} between chord No.{1} and chord No.{2}". format(statement, chord+1, chord+2))
                return None


def check_paralle_fifth(piece):
    result = check_intervals(piece, 7)
    check_and_print(result, "fifth")

def check_paralle_octave(Piece):
    result = check_intervals(Piece, 0)
    check_and_print(result, "octave")

# def check_paralle_unison(Piece):
#     result = check_intervals(Piece, 0)
#     check_and_print(result, "unison")


def has_third(piece):
    """expanded_piece = [[1,1,5,1], [2,2,4,6]]
    >>>'Chord No.1 has no third!' """

    #assert isinstance(piece Piece), "nah the input has to be a piece my friend"
    result = expand_piece(piece)
    lst = []
    for chord in result:
        chord_lst = []
        for note in chord:
            chord_lst.append(note%12)
        lst.append(chord_lst)
    index = 1
    for chords in lst:
        root = min(chords)
        third1 = root+4
        third2 = root+3
        if third1 not in chords and third2 not in chords:
            print("Chord No. {0} has no third! {1}".format(index, chords))
        index+=1

def leading_tone_doubled(piece):
    """check each chord if the leading tone is doubeled"""
    assert isinstance(piece, Piece), "the input has to be a piece!"
    expanded = expand_piece(piece)
    root = min(expanded[0])
    if root ==0:
        leading = 11
    else:
        leading = root-1
    for chord in expanded:
        curr_chord = 0
        leading_count = chord.count(leading)
        if leading_count>1:
            print ("you doubled the leading tone in chord No. {0}! {1}".format(curr_chord+1, chord))

def is_seventh(chord_in_num_form):
    seventh = find_seventh(chord_in_num_form)
    if seventh in chord_in_num_form or seventh-1 in chord_in_num_form:
        return True
    return False

def find_seventh(chord_in_num_form):
    root = min(chord_in_num_form)
    if root == 1:
        return 11
    else:
        return root-1

def seventh_resolved_down(piece):
    """check each seventh chord in a piece whether or not the seventh is resolved down by step"""
    expanded = expand_piece(piece)
    if len(expanded)==1:
        return None
    curr, second = iter(expanded), iter(expanded)
    next(second)
    while curr:
        chord_count = 1
        curr_chord = next(curr)
        if is_seventh(curr_chord):
            seventh = find_seventh(curr_chord)
            i = curr_chord.index(seventh)
            diff = curr_chord[i] - next(second)[i]
            if diff!=2 or diff!=1:
                print ("your seventh in chord No. {0} is not resolved down by step!{1}".format(chord_count+1, curr_chord))
        chord_count+=1
        next(curr)
        next(second)
    # except StopIterationError as e:
    #     print("check seventh res, done")

def run_it():
    start=True
    while start:
        print('Hello welcome my dude! You are composing music now.')
        new_piece = Piece(int(input('how many measures would you like?')), \
                        int(input('And how many beats?')))
        if new_piece.num_measures == 0 or new_piece.num_beats ==0:
            start = False
            print("OK BYE")
            return None
        new_piece.get_input()
        #here goes soemthing that allows the guitar to play
        has_third(new_piece)
        leading_tone_doubled(new_piece)
        #seventh_resolved_down(new_piece)
        check_paralle_fifth(new_piece)
        check_paralle_octave(new_piece)
        # check_paralle_unison(new_piece)

run_it()

# new_measure = Measure(4)
# C3 = Note('C', 3)
# C4 = Note('C', 4)
# G4 = Note('G', 4)
# E4 = Note('E', 4)
# c_major_triad = Chord(C3, C4, G4, E4)
