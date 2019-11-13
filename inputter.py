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
