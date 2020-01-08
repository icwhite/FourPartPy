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
        self.selected_measure = None
        self.selected_voice = None
        print("Great! Now let's start composing!")
        self.composing()

    def composing(self):
        '''The method where users can decide to do one of the following things;
            * create a new measure 'n'
            * change the tempo of the piece 't'
            * print out a copy of their piece so far 'p'
            * delete a measure they created 'd' -> further prompts needed
            * edit a measure they created 'e'
            * listen to the piece so far 'l'
            * finish composing and display the piece 'done' '''
        action = input('What would you like to do? Press the appropriate key:', \
                        '\n n: create a new measure', \
                        '\n t: change the tempo of the piece', \
                        '\n p: print out a copy of your piece so far', \
                        '\n d: delete a measure you have created', \
                        '\n e: edit a measure you have created', \
                        '\n l: listen to your piece so far!', \
                        '\n done: finish composing and here your piece \n')
        if not isinstance(action, str):
            self.composing()
        self.piece_forker(action)

    def piece_forker(self, action):
        '''Reads in input and then makes edits to the piece accordingly'''
        if action == 'n': # create new measure
            self.create_measure()
        elif action == 't':
            new_tempo = int(input('What would you like to change the tempo to?'))
            self.piece.change_tempo(new_tempo)
            self.composing()
        elif action == 'p':
            print(self.piece)
            self.composing()
        elif action == 'd':
            print(self.piece)
            index = int(input('Which measure would you like to delete?')) - 1
            try:
                self.piece.remove_measure(index)
            except ValueError:
                print('Oops! You entered a measure number which does not exist!')
                self.forker('d')
        elif action == 'e':
            index = int(input('Which measure would you like to edit?')) - 1
            try:
                self.edit_measure(index)
            except ValueError:
                print('Oops! You entered a measure number which does not exist!')
                self.forker('e')
        elif action == 'done':
            self.end_of_piece()
        else:
            print('Oops! Looks like you did not enter a valid command.')
            self.composing()

    def create_measure(self):
        '''Creates a measure according to the user's specifications and prompts
        for inputs. Users can do one of the following things;
            * edit a voice of their choosing 's', 'a', 't', 'b'
            * delete a voice of their choosing 'd' -> further prompts
            * be done creating the measure 'done' '''
        print('...')
        self.selected_measure = Measure(self.beats_per, self.num_voices, self.tempo)
        print('You created a measure!')
        self.edit_measure(self)

    def edit_measure(self):
        '''Prompts for input.'''
        print(self.selected_measure)
        action = input('Would you like to...',\
                        '\n e: edit a voice', \
                        '\n d: delete a voice
                        '\n done: stop editing this measure')
        self.measure_forker(action)

    def measure_forker(self, action):
        '''Same as piece forker except with a measure.'''
        if action == 'e':
            voice = int(input('What voice would you like to edit?', \
                            '\n 0: soprano, 1: alto, 2: tenor, 3: bass'))
            self.edit_voice(voice)
        elif action == 'd':
            index = int(input('Which voice would you like to delete?')) - 1
            try:
                self.piece.remove_voice(index)
            except ValueError:
                print('Oops! You entered a voice number which does not exist!')
                self.measure_forker('d')
        elif action = 'done':
            self.selected_measure = None
            self.composing()
        else:
            self.edit_measure()


    def edit_voice(self, voice):
        '''Editing a voice of self.selected_measure. The voice attribute is the index in
        the measure.voices list. Start by printing the voice. Users can:
            * add a note to the end of the measure 'a'
            * delete a note from the end of the measure 'd'
            * finish editing this voice 'done' '''
        print('...')
        voices = ['soprano', 'alto', 'tenor', 'bass']
        print('You are editing the {0} voice!'.format(voices[voice]))
        self.selected_voice = self.selected_measure[voice]
        print(self.selected_voice)
        action = input('Type [Letter][accidental][octave number] ex: C4, F#4', \
                        '\n d: to delete last note entered', \
                        '\n done: to be done editing this voice \n')
        self.voice_forker(action)

    def voice_forker(self, action):
        '''Another forker... :/'''
        if action == 'd':
            self.selected_voice.remove_note()
            self.edit_voice()
        elif action == 'done':
            self.selected_voice = None
            self.edit_measure()
        else:
            beats = int(input('How many beats would you like this beat to have? '))
            try:
                self.add_note(self, action)
            except SyntaxError:
                print('Oops! Too many beats!')
                self.voice_forker(string)

    def add_note(self, string, num_beats):
        '''Parse the string and add it to self.selected_voice'''
        octave = int(string[-1])
        name = string[:-1]
        note = Note(name, octave, num_beats, self.tempo)
        self.selected_voice.add_note(note)


    def end_of_piece(self):
        '''Print out the piece and then ask if the user would like to title it
        and then create the wave file.'''
        print('Congrats! You have finished your piece!', \
                '\n Here is what it looks like:')
        print(self.piece)
        # somehow play the piece
        # then analyze it 



def initiating-input():
    print("Welcome to the Four Part Chorale style music writer!")
    measures = int(input('How many measures would you like?'))
    beats_per = int(input(\
    'How many beats per measure? (compound types not available)'))
    tempo = int(input('How many beats per minute? (i.e. 60, 120)'))

    print("Great! Now let's start composing!")
