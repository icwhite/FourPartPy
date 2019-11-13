# inputter
class Piece:
    def __init__(self, num_measures, num_beats):
        self.num_measures = num_measures
        self.num_beats = num_beats
        self.measures = []
        for i in range(num_measures):
            self.measures.append(Measure(num_beats))


class Measure:
    def __init__(self, num_beats):
        self.chords = []
        for i in range(num_beats):
            self.chords.append(Chord())
    def get_chord(self, ):
        '''hiiiii'''
        pass


class Chord:
    '''A class representing a Chord'''
    pass


Piece.get(1, 1, S) # first measure, first beat, soprano
Piece.set(1, 1, S, 'C6') # first measure, first beat, soprano, is C6
Piece.set_chord(1, 1, ['C3', 'C4', 'E4', 'G4'])
