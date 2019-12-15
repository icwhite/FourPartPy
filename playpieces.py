from sound import *
from piece_classes import *

Note.generate_equal()
pitch_dict = Note.pitch_dict
A_4 = str(Note('A', 4))
half_step = 2 ** -12
C_2 = 65.70
C_5 = 525.63
guitarstrings = {}
for note in Note.pitch_dict:
    guitarstrings[note] = GuitarString(Note.pitch_dict[note])
### for playing the guitar
def pluck_guitar(note, start, end):
    '''Takes in a note object and a duration and plucks the guitar
    with its frequency. Start is the time that you want the guitar to be
    plucked and end is when you want the sound to cut out.'''
    string = guitarstrings[str(note)]
    # get rid of all the white noise
    string.pluck()
    # for _ in range(5000):
    #     string.sampler()
    print('hi!!')
    def sampler(t):
        seconds = t/frame_rate
        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        else:
            return string.sampler()
    return sampler
    # sampler = lambda x: string.sampler()
    # return string.sampler

def play_chord(notes, start, end):
    '''Plays a chord.
    >>> s = play_chord(['C3', 'A4'], 0.5, 2)'''
    samplers = []
    for note in notes:
        samplers.append(pluck_guitar(note, start, end))
    def sampler(t):
        total = 0
        for s in samplers:
            total += s(t)
        return total
    return sampler

def chord_sampler(chord, start, end):
    '''Plays a chord from the piece classes files.
    >>> chord is a Chord instance with C3, G3, E4, and C5
    >>> play_chord2(chord, start, end)
    '''
    samplers = []
    for note in chord.voices.values():
        samplers.append(pluck_guitar(note, start, end))
    def sampler(t):
        total = 0
        for s in samplers:
            total += s(t)
        return total
    return sampler

def piece_sampler(piece):
    '''Takes in a piece instance and then plays the music. :)'''
    pass


C3_sampler = pluck_guitar('C3', 0.5, 3)
A4_sampler = pluck_guitar('A4', 0.5, 3)
# testing the class version
C3 = Note('C', 3)
C4 = Note('C', 4)
G4 = Note('G', 4)
E4 = Note('E', 4)
c_major_triad = Chord(C3, C4, G4, E4)
class_chord = chord_sampler(c_major_triad, 0.5, 2)

chord = play_chord(['C3', 'G3', "E4", 'C5'], 0.5, 2)

# print(A4_sampler)
play(class_chord, "debugging.wav")
print(guitarstrings['A4'].tic_counter)
