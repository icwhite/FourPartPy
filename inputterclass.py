# making a terminal inputter so that pieces can be easily accessed
from piece_classes import *
from musicplayer import *

class Inputter:
    '''A collection of methods needed for inputting piece data'''
    def __init__(self, piece):
        print("Welcome to the Four Part Chorale style music writer!")
        self.measures = int(input('How many measures would you like?'))
        self.beats_per = int(input(\
        'How many beats per measure? (compound types not available)'))
        self.tempo = int(input('How many beats per minute? (i.e. 60, 120)'))
        self.piece = Piece(self.measures, self.beats_per, tempo = self.tempo)
        print("Great! Now let's start composing!")
        self.composing(0)

    def create_measure(self):
        self.piece.add_measure()

    def composing(self, measure):
        '''Handles composing each measure, starting with the measure in
        the attribute measure. If measure equals the total number of measures that
        are in the piece, prompt to add another measure or end the piece.'''
        pass

    def end_of_piece(self):
        '''Print out the piece and then ask if the user would like to title it
        and then create the wave file.'''
        pass



def initiating-input():
    print("Welcome to the Four Part Chorale style music writer!")
    measures = int(input('How many measures would you like?'))
    beats_per = int(input(\
    'How many beats per measure? (compound types not available)'))
    tempo = int(input('How many beats per minute? (i.e. 60, 120)'))

    print("Great! Now let's start composing!")
