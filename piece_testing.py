# Piece classes testing file
from piece_classes import *
from musicplayer import *
### this test was passed!!
# m = Measure()
# vs = m.voices
# v = m.get_voice(0)
# print(v) # should print nothing
# n = Note('C', 4, 4)
# print(n) # should print C4
# v.add_note(n)
# print(v) # should return C4-4
# for voice in vs:
#     print(voice)
# # only first element filled
# print(m)
# should return
# C4-4
# [1] [1] [1] [1]
# [1] [1] [1] [1]
# [1] [1] [1] [1]

### another test ###
music = Music()
p = Piece()
m = Measure()
v = m.get_voice(0)
n = Note('C', 4, 4)
v.add_note(n)
print(p)
p.add_measure(m)
music.play_piece(p, 'mypiece.wav')
music.play_wave('mypiece.wav')
