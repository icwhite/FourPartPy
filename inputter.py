# inputter
class Measure:
    """each individual mearuse consists of number of chords"""
    curr_beat = 0
    def __init__(self, beat):
        """things in it"""
        self.beat = beat
        self.chords = []

    def set_chord(chord, place):
        """Add a chord object """
        assert curr_beat<=beat, "Beat is out of range"
        self.chords[place-1] = chord
        curr_beat += chord.duration


    def get_chord(index):
        return self.chord[index]

class Chord:
    """the class creates a single chord with four notes, which are the
       soprano, the alto, the tenor and the bass. Each note is an instanse of the Note class.
       Duration is a dictionary containing quater notes, whole note, half note, etc.
       Each type corresbond with a duration, which is an integer"""

    durations = {'Eighth': 0.5, 'Quater': 1, "Half": 2, 'Dotted Half': 3, "Whole": 4}

    def __init__(self, soprano=None, alto=None, tenor=None, bass=None, duration = durations['Quater']):
        assert "all has to be instance of Note class or None"
        self.soprano = soprano
        self.alto = alto
        self.tenor = tenor
        self.bass = bass
        self.duration = duration

    def __str__(self):
        return "{0} \n{1} \n{2} \n{3}".(self.soprano, self.alto, self.tenor, self.bass) #I forgot the exact symtax lol

class Note:
    """A note should be in the form of new_note = Note (C, 4, #)
       Notes have name, octave, quality. """

    qualities = {'#': 'Sharp', 'b': 'Flat', 'nat': 'Natural'}
    available_names = ['C', 'D', 'E', 'F', 'G', 'A', 'B']


    def __init__(self, note_name=None, octave=None, quality=qualities['nat']):
        self.note_name = note_name
        self.ocvate = octave
        self.quality = quality

    def change_note_name(self, new_name):
        assert new_name in available_names, "You have to put an actual note"
        self.note_name = new_name

    def change_octave(self, new_octave):
        assert new_octave is in range(1, 8), "You sure that's the right octave lol?"
        self.octave = new_octave

    def change_quality = (self, new_quality):
        assert new_quality in qualities, "You are too big brain for this software"
        self.quality = qualities[new_quality] #???

    def __str__(self):
        return "{0} {1}". (self.note_name, self.quality)


new_measure = Measure(4)
C3 = Note('C', 3)
C4 = Note('C', 4)
G4 = Note('G', 4)
E4 = Note('E', 4)
c_major_triad = Chord(C3, C4, G4, E4)
measure.set_chord(c_major_triad, 1) #add the c_major_triad to the first chord in the Measure
measure.get_chord(1) #this will return the first chord, which is an instanse of the chord object
measure.get_chord(1).tenor = Note('B', 4, '#')
C3.change_note_name('C')
new_measure.chords
# inputter
