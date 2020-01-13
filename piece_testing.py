# Piece classes testing file
from piece_classes import *
m = Measure()
vs = m.voices
v = m.get_voice(0)
print(v) # should print nothing
n = Note('C', 4, 4)
print(n) # should print C4
v.add_note(n)
print(v) # should return C4-4
for voice in vs:
    print(voice)
# only first element filled
print(m)
# should return
# C4-4
# [1] [1] [1] [1]
# [1] [1] [1] [1]
# [1] [1] [1] [1]
