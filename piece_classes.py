class Piece:
    '''A class representing a Piece'''
    def __init__(self, num_measures=0, num_beats=4, num_voices = 4, tempo = 120):
        # print('Measures: {0} Beats: {1} Voices: {2}, Tempo: {3}'.\
        #         format(num_measures, num_beats, num_voices, tempo))
        self.num_measures = num_measures
        self.num_beats = num_beats
        self.measures = []
        self.tempo = tempo
        self.num_voices = num_voices
        # for i in range(num_measures, self.tempo):
        #     self.measures.append(Measure(num_beats, tempo = tempo))

    def get_measure(self, measure_num):
        '''Returns the measure corresponding to measure number
        inputted by the user
        >>> new_piece = Piece()
        >>> get_measure(1)
        --- repr for measure 1 --- '''
        return self.measures[measure_num - 1]

    def add_measure(self, measure = None):
        '''Adds a new blank measure to Piece at the end of the piece if measure
        is none, otherwise, appends the new measure to self.measures.'''
        # assert type(measure) == Measure, 'must be measure instance'
        if measure is None:
            self.measures.append(Measure(self.num_beats, self.num_voices, \
                                         self.tempo))
        else:
            assert (measure.num_beats == self.num_beats), \
                    'Cannot add this measure incorrect number of beats'
            assert (measure.num_voices == self.num_voices), \
                    'Cannot add this measure incorrect number of voices'
            measure.change_tempo(self.tempo)
            self.measures.append(measure)

    def insert_measure(self, pos, measure = None):
        '''Insert a measure at the designated position'''
        assert pos <= len(self.measures), "Measure number is out of range"
        if measure is None:
            self.measures.insert(pos, Measure(self.num_beats, self.num_voices, \
                                                self.tempo))
        else:
            assert (measure.num_beats == self.num_beats), \
                    'Cannot add this measure incorrect number of beats'
            assert (measure.num_voices == self.num_voices), \
                    'Cannot add this measure incorrect number of voices'
            measure.change_tempo(self.tempo)
            self.measures.insert(pos, measure)

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
                lst = []
                for voice in range(4):
                    voice_input = input('Measuere {0} Beat {1} voice {2}'.\
                    format(count_measure, i, voice))
                    name, quality, octave = self.processor(voice_input)
                    lst.append(Note(name, octave, quality))
                new_chord = Chord(lst[0], lst[1], lst[2], lst[3])
                self.get_measure(i - 1).add_chord(new_chord)


                # bass_input = input('Measure {0} Beat {1} bass voice '\
                #                     .format(count_measure, i))
                # bass_name, bass_quality, bass_octave = self.processor(bass_input)
                # bass = Note(bass_name, bass_quality, bass_octave)
                #
                # tenor = Note(input('Measure {0} Beat {1} tenor voice '\
                #                     .format(count_measure, i)))
                # alto = Note(input('Measure {0} Beat {1} alto voice '\
                #                     .format(count_measure, i)))
                # soprano = Note(input('Measure {0} Beat {1} soprano voice '\
                #                         .format(count_measure, i)))
                #                  #also num_beats and stuff but I am a bit lazy lol
                # new_chord = Chord(soprano, alto, tenor, bass)
            count_measure += 1

    def processor(self, string):
        if len(string) == 3:
            name = [0]
            quality = string[1]
            octave = int(string[2])
        else:
            name = string[0]
            quality = ''
            octave = int(string[1])
        return name, quality, octave



class Measure:
    """Represents a measure"""
    def __init__(self, num_beats, num_voices = 4, tempo=120, voices = []):
        """things in it"""
        # print('Beats: {0} Voices: {1}, Tempo: {2}'.\
        #         format(num_beats, num_voices, tempo))
        self.voices = voices
        self.num_voices = num_voices
        self.tempo = tempo
        self.num_beats = num_beats
        self.num_seconds = 60/self.tempo * self.num_beats
        if voices == []:
            for i in range(self.num_voices):
                self.voices.append(Voice())

    # def add_voice(self, voice = Voice.empty):
    #     '''Append a voice object to self.voices'''
    #     voice.change_tempo(tempo)
    #     self.voices.append(voice)

    def change_tempo(self, tempo):
        '''Change the tempo of the measure and all the chords inside of it.'''
        # this method could be optimized more :)
        self.tempo = tempo
        for voice in self.voices:
            voice.change_tempo(tempo)
        self.num_seconds = 60/self.tempo * self.num_beats

    def __str__(self):
        '''Prints out each of the chords in measure
        >>> m = Measure(4)
        >>> print(m)
        >>> [add four chords, each with num_beat one in some manners]
        [ [] [] [] []
          [] [] [] []
          [] [] [] []
          [] [] [] [] ]'''
        output = ''
        for voice in self.voices:
            voice_str = str(voice)
            if voice.curr_beat < self.num_beats:
                for i in range(self.num_beats - voice.curr_beat):
                    voice_str += ' [1] '
            output += '\n' + voice_str
        return output

class Voice:
    '''Represents the notes in a given voice of a measure.'''

    beat_dict = {'Eighth': 0.5, 'Quarter': 1, "Half": 2, \
                    'Dotted Half': 3, "Whole": 4}

    def __init__(self, notes = [], num_beats = 4, tempo = 120):
        self.curr_beat = 0
        self.notes = notes
        self.tempo = tempo
        self.num_beats = num_beats
        # want this to be sum bc of how it is used in musicplayer class
        self.num_seconds = sum([note.num_seconds for note in self.notes])
        for note in self.notes:
            self.curr_beat += note.num_beats

    def add_note(self, note):
        assert self.curr_beat<=self.num_beats, "Beat is out of range"
        # this really isn't quite that simple, need to insert in the
        # correct place
        note.change_tempo(self.tempo)
        self.note.append(chord)
        self.curr_beat += note.num_beats
        self.notes.append(note)

    def get_note(self, index):
        return self.notes[index]

    def change_tempo(self, tempo):
        self.tempo = tempo
        for note in self.notes:
            note.change_tempo(tempo)
        self.num_seconds = sum([note.num_seconds for note in self.notes])

    def __str__(self):
        '''Prints out a string representing the voice in the following format.
        'A4-1 G4-1' '''
        voice_str = ''
        for note in self.notes:
            voice_str += ' ' + str(note) + '-' + str(note.num_beats)
        return voice_str




class Note:
    """A note should be in the form of new_note = Note (C, 4, #)
       Notes have name, octave, quality. """

    # qualities = {'#': 'Sharp', 'b': 'Flat', 'nat': 'Natural'}
    qualities = ['#', 'b', '']
    available_names = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    notes_and_num = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G':7, 'A':9, 'B':11, \
                    '': 0, '#': 1, 'b': -1}
    pitch_dict = {}

    def __init__(self, note_name=None, octave=None, num_beats=1, tempo = 120):
        if len(note_name) > 1:
            self.note_name = note_name[0]
            self.quality = note_name[1]
        else:
            self.note_name = note_name
            self.quality = ''
        self.tempo = tempo
        self.num_beats = num_beats
        self.num_seconds = 60/self.tempo * self.num_beats
        self.octave = octave
        self.number = self.notes_and_num[self.note_name] + \
                    self.notes_and_num[self.quality] + self.octave * 12
        # self.frequency = self.pitch_dict[self]

    def change_beats(self, beats):
        '''Change the attribute num_beats and then update num_seconds'''
        self.num_beats = beats
        self.num_seconds = 60/self.tempo * self.num_beats

    def change_tempo(self, tempo):
        '''Change the tempo attribute and then change num_seconds accordingly'''
        self.tempo = tempo
        self.num_seconds = 60/self.tempo * self.num_beats

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
        >>> n = Note('Bb', 4)
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
                sharp = str(Note(key + '#', octave_num))
                # sharp += key + '#' + str(octave_num)
            elif Note.notes_and_num[key] == (n + 1) % 12\
                and key != '#' and key != '':
                flat = str(Note(key + 'b', octave_num))
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
# testing to see whether pitch dict still works
# Note.generate_equal()
# for note in Note.pitch_dict:
#     print(note, Note.pitch_dict[note])

### measure-str testing
# C3 = Note('C', 3)
# C3.num_beats = 2
# C4 = Note('C', 4)
# G4 = Note('G', 4)
# E4 = Note('E', 4)
# D3 = Note('D', 3)
# D4 = Note('D', 4)
# A4 = Note('A', 4)
# Fs4 = Note('F#', 4)
# b = Voice([C3])
# t = Voice([C4, D4])
# a = Voice([E4, Fs4])
# s = Voice([G4, A4])
# print(s)
# new_measure = Measure(2, 4, 40, [s,a,t,b])
# piece = Piece(2, 2, 4, 40)
# piece.add_measure(new_measure)
# piece.add_measure()
# print(piece)
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
