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
        # if seconds < start:
        #     return 0
        # elif seconds > end:
        #     return 0
        # else:
        return string.sampler()
    return sampler
    # sampler = lambda x: string.sampler()
    # return string.sampler

C3_sampler = pluck_guitar('C3', 0.5, 3)
A4_sampler = pluck_guitar('A4', 0.5, 3)
# print(A4_sampler)
play(C3_sampler, "struggles.wav")
print(guitarstrings['A4'].tic_counter)
