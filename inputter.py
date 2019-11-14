# inputter
class Piece:
    def __init__(self, num_measures = 4, num_beats = 4, num_voices = 4):
        self.num_measures = num_measures
        self.num_beats = num_beats
        self.measures = []
        for i in range(num_measures):
            self.measures.append(Measure(num_beats))
    def get(self, measure_num, beat_num, voice):
        '''Return the note at measure [measure_num] and beat [beat_num]
        and voice corresponding to the letter entered.
        Piece.get(1, 1, S) -> E4 the first beat, first measures
        soprano voice.'''
        return self.measures[measure_num -1].get_chord(beat_num).get_voice(voice)

    def set(self, measure_num, beat_num, voice, note):
        '''Set the voice at measure_num, beat_num and voice corresponding
        to the letter.
        >>> new_piece = Piece(4, 4)
        >>> new_piece.set(1, 1, S, E4)
        >>> new_piece.get(1, 1, S)
        E4'''
        self.measure[measure_num -1].get_chord(beat_num).set_voice(voice, note)

    def __str__(self):
        '''Relies on the implementation of Measure.__str__()
        new_piece = Piece()
        >>> print(new_piece)
        Measure 1
        --- stuff ---
        Measure 2
        --- stuff ---
        Measure 3
        --- stuff ---
        Measure 4
        --- stuff ---
        '''
        output = ''
        for i in range(len(self.measures)):
            output += 'Measure {0} \n {1} \n'.format(i+1, str(self.measures[i]))


class Measure:
    """each individual measure consists of number of chords"""
    curr_beat = 0
    def __init__(self, beat, num_voices = 4):
        """things in it"""
        self.chords = []
        for i in range(num_beats):
            self.chords.append(Chord())
        self.beat = beat

    def set_chord(chord, place):
        """Add a chord object """
        assert curr_beat<=beat, "Beat is out of range"
        self.chords[place-1] = chord
        curr_beat += chord.duration

    def get_chord(index):
        return self.chord[index]

    def __str__(self):
        '''Prints out each of the chords in measure
        >>> m = Measure(4)
        >>> print(m)
        [ [] [] [] []
          [] [] [] []
          [] [] [] []
          [] [] [] [] ]'''
        output = '['
        for voice in Chord.voices:
            for chord in self.chords:
                note = chord.get_voice(voice)
                if note is None:
                    output += ' []'
                else:
                    output += ' ' + str(note)
            if voice != 'B':
                output += ' ]'
            else:
                output += '\n 1'



class Chord:
    """the class creates a single chord with four notes, which are the
       soprano, the alto, the tenor and the bass. Each note is an instanse of the Note class.
       Duration is a dictionary containing quater notes, whole note, half note, etc.
       Each type corresbond with a duration, which is an integer"""

    durations = {'Eighth': 0.5, 'Quater': 1, "Half": 2, 'Dotted Half': 3, "Whole": 4}

    def __init__(self, soprano=None, alto=None, tenor=None, bass=None, duration = durations['Quater']):
        assert "all has to be instance of Note class or None"
        self.voices = {'S': soprano, 'A': alto, 'T': tenor, 'B': bass}
        # self.soprano = soprano
        # self.alto = alto
        # self.tenor = tenor
        # self.bass = bass
        self.duration = duration

    def get_voice(self, voice_letter):
        '''new_chord = Chord(E4)
        new_chord.get_voice('S') -> E4'''
        return self.voices[voice_letter]

    def set_voice(self, voice_letter, note):
        '''new_chord = Chord()
        >>> new_chord.set_voice('S', E4)
        >>> new_chord.get_voice('S')
        E4'''
        self.voices[voice_letter] = note

    def voice_part(self, voice_letter):
        '''
        >>> new_chord.voice_part('B')
        Bass'''
        pass
        # should I implement this? Seems a little useless

    def __str__(self):
        '''
        >>> new_chord = Chord(C3, C4, G4, E4)
        >>> print(new_chord)
        C3
        C4
        G4
        E4'''
        #I forgot the exact symtax lol
        return "{0} \n{1} \n{2} \n{3}".(self.voices['S'], self.voices['A'],
            self.voices['T'], self.voices['B'])

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
