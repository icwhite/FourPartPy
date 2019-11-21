# trying to do the one Princeton thing

class RingBuffer:
    '''A Ring Buffer.
    The ring buffer models the medium (a string tied down at both ends)
     in which the energy travels back and forth.
     The length of the ring buffer determines the fundamental frequency
     of the resulting sound. Sonically, the feedback mechanism reinforces
     only the fundamental frequency and its harmonics
     (frequencies at integer multiples of the fundamental).
     The energy decay factor (.994 in this case) models the
     slight dissipation in energy as the wave
     makes a roundtrip through the string.'''
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
        self.first = 0 # stores least recently inserted
        self.last = 0 # stores index one beyond most recently inserted

    def size(self):
        '''Return the number of items currently in the Buffer'''
        return len(self.items)

    def isEmpty(self):
        '''Returns whether or not the buffer is empty'''
        return self.items == []

    def isFull(self):
        '''Returns whether the buffer is at capacity'''
        return self.size() == self.capacity

    def enqueue(self, x):
        '''Add item x to the end and increment last by 1'''
        self.items.insert(self.last, x)
        self.last += 1

    def dequeue(self):
        '''Delete and return an item from the front. Increment first.'''
        og_val = self.items[0]
        self.items[0] = 0
        self.first += 1
        return og_val

    def peek(self):
        '''Return but do not delete item from front.'''
        return self.items[0]

    def __str__(self):
        return str(self.items)

# testing for Ring Buffer
# ring = RingBuffer(1)
# print(ring, ring.size(), ring.isEmpty(), ring.isFull())
# ring.enqueue(5)
# print(ring, ring.peek(), ring.isEmpty(), ring.isFull())
# print(ring.dequeue())
