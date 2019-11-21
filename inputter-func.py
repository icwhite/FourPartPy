# this is a file for the inputter function
"""I can't quite remember how to do the input function lol but here we are"""
"""Also this function is way too long need to find ways to shorten it up """
def user_input():
    print('Hello welcome my dude! You are composing music now.')
    new_piece = Piece(int(input('how many measures would you like?')), \
                    int(input('And how many beats?')))
    print("Great! Now let's start composing")
    count_measure = 1
    def note_composing():
        nonlocal count_measure, new_piece
        while count_measure <= new_piece.num_measures: #while we are not running out of measures
            print("Now let's create music for measure No.{0}".format(count_measure))
            count_beats = new_piece.get_measure(count_measure).num_beats #number of beats in the current measure
            for i in range(1, count_beats+1):
                bass = Note(input('Measure {0} Beat {1} \
                            bass voice'.format(count_measure, i)))
                tenor = Note(input('Measure {0} Beat {1} \
                            tenor voice'.format(count_measure, i)))
                alto = Note(input('Measure {0} Beat {1} \
                            alto voice'.format(count_measure, i)))
                soprano = Note(input('Measure {0} Beat {1} \
                                soprano voice'.format(count_measure, i)))
                                 #also durations and stuff but I am a bit lazy lol
                new_chord = Chord(soprano, alto, tenor, bass)
                new_piece.get_measure(i).add_chord(new_chord)
            count_beats+=1
    note_composing()
