# inputter
class Piece:
    '''A class representing a Piece'''
    def __init__(self, num_measures=4, num_beats=4, num_voices = 4):
        self.num_measures = num_measures
        self.num_beats = num_beats
        self.measures = []
        for i in range(num_measures):
            self.measures.append(Measure(num_beats))

    def get_measure(self, measure_num):
        '''Returns the measure corresponding to measure number
        inputted by the user
        >>> new_piece = Piece()
        >>> get_measure(1)
        --- repr for measure 1 --- '''
        return self.measures[measure_num - 1]

    def add_measure(self, measure = None):
        '''Adds a new blank measure to Piece at the end of the piece.
        Appends measure to self.measures'''
        # should we scale this so you can do more
        # complicated manipulations??
        self.measures.append(Measure())


    def get_voice(self, measure_num, beat_num, voice):
        '''Return the note at measure [measure_num] and beat [beat_num]
        and voice corresponding to the letter entered.
        Piece.get_voice(1, 1, S) -> E4 the first beat, first measures
        soprano voice.'''
        return self.get_measure(measure_num).get_chord(beat_num).get_voice(voice)

    def set_voice(self, measure_num, beat_num, voice, note):
        '''Set the voice at measure_num, beat_num and voice corresponding
        to the letter.
        >>> new_piece = Piece(4, 4)
        >>> new_piece.set(1, 1, S, E4)
        >>> new_piece.get(1, 1, S)
        E4'''
        self.get_measure(measure_num).get_chord(beat_num).set_voice(voice, note)

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
        for i in range(self.num_measures):
            output += 'Measure {0} \n {1} \n'.format(i+1, str(self.measures[i]))
        return output

    def __repr__(self): #I don't really know if this is correct, but the basic idea is to put the entire piece into a nexted list
        """putting everything into a nested list"""
        output = []
        output.extend(self.mearures)
        return output

    def get_input(self):
        '''Get input from the user and then store that input in a Piece class'''
        count_measure = 1
        while count_measure <= self.num_measures: #while we are not running out of measures
            print("Now let's create music for measure No. {0} ".format(count_measure))
            # count_beats = self.num_beats #number of beats in the current measure
            for i in range(1, self.num_beats+1):
                bass = Note(input('Measure {0} Beat {1} bass voice '\
                                    .format(count_measure, i)))
                tenor = Note(input('Measure {0} Beat {1} tenor voice '\
                                    .format(count_measure, i)))
                alto = Note(input('Measure {0} Beat {1} alto voice '\
                                    .format(count_measure, i)))
                soprano = Note(input('Measure {0} Beat {1} soprano voice '\
                                        .format(count_measure, i)))
                                 #also durations and stuff but I am a bit lazy lol
                new_chord = Chord(soprano, alto, tenor, bass)
                self.get_measure(i - 1).add_chord(new_chord)
            count_measure += 1



class Measure:
    """each individual measure consists of number of chords"""
    curr_beat = 0
    def __init__(self, num_beats, num_voices = 4):
        """things in it"""
        self.chords = []
        self.num_beats = num_beats
        # for i in range(num_beats):
        #     self.chords.append(Chord())

    def add_chord(self, chord):
        """Add a chord object """
        assert self.curr_beat<=self.num_beats, "Beat is out of range"
        self.chords.insert(curr_beat, chord) #append it in certain places so that the beat can allign 
        self.curr_beat += chord.duration

    def rm_chord(self, identifier):
        pass

    def get_chord(self, index):
        assert index - 1 <= self.num_beats, "Beat is out of range"
        assert index - 1 <= len(self.chords), "the chord at that beat\
                                                hasn't been created yet!"
        return self.chords[index - 1]

    def __str__(self):
        '''Prints out each of the chords in measure
        >>> m = Measure(4)
        >>> print(m)
        >>> [add four chords, each with duration one in some manners]
        [ [] [] [] []
          [] [] [] []
          [] [] [] []
          [] [] [] [] ]'''
        output = '['
        for voice in Chord.voices: #This has to be a class attribute but now is an instance attribute
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
        lst = []
        for chord in self.chords:
            for voice in chord.voices:
                pass
                # now



class Chord:
    """the class creates a single chord with four notes, which are the
       soprano, the alto, the tenor and the bass. Each note is an instanse of the Note class.
       Duration is a dictionary containing quater notes, whole note, half note, etc.
       Each type corresbond with a duration, which is an integer"""

    durations = {'Eighth': 0.5, 'Quarter': 1, "Half": 2, 'Dotted Half': 3, "Whole": 4}
    # do we want user to input "Quarter", "Eighth", etc or 1, 0.5, etc

    def __init__(self, soprano=None, alto=None, tenor=None, bass=None, duration = durations['Quarter']):
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
        >>> new_chord = Chord(E4, G4, C4, C3)
        >>> new_chord.voice_part('B')
        C3'''
        pass
        # should I implement this? Seems a little useless
        # I actually don't understand the point of this method...
        # ...oops maybe I will just leave it here and hope I remember

    def voice_to_letter(self, voice_letter):
        '''Returns the corresponding voice letter for the voice entered
        >>> c = Chord(E4)
        >>> c.voice_to_letter(E4)
        S'''
        pass

    def __str__(self):
        '''
        >>> new_chord = Chord(C3, C4, G4, E4)
        >>> print(new_chord)
        C3
        C4
        G4
        E4'''
        #I forgot the exact symtax lol
        return "{0} \n{1} \n{2} \n{3}".format(self.voices['S'], self.voices['A'],
            self.voices['T'], self.voices['B'])

    def non_func(self, note):
        '''Add a passing tone for an already existing chord
        will be played OFF the beat.'''

class Note:
    """A note should be in the form of new_note = Note (C, 4, #)
       Notes have name, octave, quality. """

    # qualities = {'#': 'Sharp', 'b': 'Flat', 'nat': 'Natural'}
    qualities = ['#', 'b', '']
    available_names = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    notes_and_num = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G':7, 'A':9, 'B':11, \
                    '': 0, '#': 1, 'b': -1}
    pitch_dict = {}



    def __init__(self, note_name=None, octave=None, quality='',
        non_func = False):
        self.note_name = note_name
        self.octave = octave
        self.quality = quality
        self.non_func = non_func
        self.number = self.notes_and_num[note_name] + \
                    self.notes_and_num[quality] + \
                    self.octave * 12
        # self.frequency = self.pitch_dict[self]

    def change_note_name(self, new_name):
        assert new_name in self.available_names, "You have to put an actual note"
        self.note_name = new_name

    def change_octave(self, new_octave):
        assert new_octave in range(1, 8), "You sure that's the right octave lol?"
        self.octave = new_octave

    def change_quality(self, new_quality):
        assert new_quality in qualities, "You are too big brain for this software"
        self.quality = qualities[new_quality] #???

    def __str__(self):
        '''
        >>> n = Note('B', 4, 'b')
        >>> print(n)
        Bb4
        >>> print(Note('C', 4))
        C4 '''
        if self.quality == '':
            return "{0}{1}".format(self.note_name, self.octave)
        return "{0}{1}{2}".format(self.note_name, self.quality, self.octave)

    def generate_equal():
        '''Creates all the frequencies and then stores them
        in pitch_dict
        >>> generate_equal('A4', 'B4')
        >>> pitch_dict
        {'A4': 442, 'A#4': 468.28, 'B4': 496.13}'''
        A4_num = 45
        C2_num = 12
        C6_num = 60
        scalar = 2 ** (1/12)
        for num in range(C2_num, C6_num + 1):
            # store frequency and name in pitch_dict
            frequency = 442 * scalar ** (num - A4_num)
            notes = Note.number_to_note(num)
            for note in notes:
                Note.pitch_dict[note] = frequency

    def number_to_note(n):
        '''Convert a number to a note value where C1 is 0.
        Warning! Sometimes returns two values!!
        >>> n = Note('A4')
        >>> self.number_to_note(0)
        C1
        >>> self.number_to_note(1)
        C#1, Db1'''
        octave_num = n // 12 + 1
        for key in Note.notes_and_num:
            if Note.notes_and_num[key] == n % 12 and n % 12 != 1:
                return [str(Note(key, octave_num))]
        # sharp = ''
        # flat = ''
        for key in Note.notes_and_num:
            if Note.notes_and_num[key] == (n - 1) % 12 \
                and key != '#' and key != '':
                sharp = str(Note(key, octave_num, '#'))
                # sharp += key + '#' + str(octave_num)
            elif Note.notes_and_num[key] == (n + 1) % 12\
                and key != '#' and key != '':
                flat = str(Note(key, octave_num, 'b'))
                # flat += key + 'b' + str(octave_num)
        return [sharp, flat]

    def half_counter(n, m):
        '''Counts the number of half steps in between the
        two pitches described by Note objects n and m
        >>> half_counter('A4', 'A#4')
        1'''
        note1 = Note(n)
        note2 = Note(m)
        return note1.number - note2.number

    def frequency(self):
        return self.pitch_dict[self]


# new_measure = Measure(4)
# C3 = Note('C', 3)
# C4 = Note('C', 4)
# G4 = Note('G', 4)
# E4 = Note('E', 4)
# c_major_triad = Chord(C3, C4, G4, E4)
# print(c_major_triad)
# new_measure.add_chord(c_major_triad) # add the c_major_triad to the first chord in the Measure
# new_measure.get_chord(1).set_voice('T', Note('B', 4, '#'))
# new_measure.get_chord(1) #this will return the first chord, which is an instanse of the chord object
# C3.change_note_name('C')
# new_measure.chords

# for i in range(20):
#     print(Note.number_to_note(n, i))
# print(Note.pitch_dict)
# Note.generate_equal()
# for key in Note.pitch_dict:
#     print(key, Note.pitch_dict[key])
