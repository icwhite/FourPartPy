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
        self.composing()

    def create_measure(self):
        self.piece.add_measure()

    def composing(self):
        '''The method where users can decide to do one of the following things;
            * create a new measure 'n'
            * change the tempo of the piece 't'
            * print out a copy of their piece so far 'p'
            * delete a measure they created 'd' -> further prompts needed
            * edit a measure they created 'e' '''
        action = input('What would you like to do? Press the appropriate key:', \
                        '\n n: create a new measure', \
                        '\n t: change the tempo of the piece', \
                        '\n p: print out a copy of your piece so far', \
                        '\n d: delete a measure you have created', \
                        '\n e: edit a measure you have created')
        if not isinstance(action, str):
            self.composing()

    def compose_measure(self):
        '''Creates a measure according to the user's specifications and prompts
        for inputs. Users can do one of the following things;
            * edit a voice of their choosing 's', 'a', 't', 'b'
            * delete a voice of their choosing 'd' -> further prompts'''
        pass

    def compose_voice(self, voice):
        '''Editing a voice of the measure. The voice attribute is the index in
        the measure.voices list. Start by printing the voice. Users can:
            * add a note to the end of the measure 'a'
            * delete a note from the end of the measure 'd' '''

    def edit_measure(self, measure):
        '''Editing a measure of the piece. The measure attribute is the index
        of the measure in piece.measures. Start by printing the measure.
        Users can:
            * edit a voice 's', 'a', 't', 'b'
            * delete a voice 'd' '''

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
