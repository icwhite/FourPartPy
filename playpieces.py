from sound import *
from piece_classes import *

Note.generate_equal()
pitch_dict = Note.pitch_dict
A_4 = Note('A', 4)# the frequency of A above middle C
half_step = 2 ** -12
C_2 = 65.70
C_5 = 525.63
guitarstrings = {}
for note in Note.pitch_dict:
    guitarstrings[note] = GuitarString(Note.pitch_dict[note])
### for playing the guitar
def pluck_guitar(note):
    def sampler2():
        string = guitarstrings[note]
        string.pluck()
        for _ in range(5000):
            string.sampler()
        return string.sampler()
    return sampler2

A4_sampler = pluck_guitar(A_4)
play_buffer(A4_sampler)
