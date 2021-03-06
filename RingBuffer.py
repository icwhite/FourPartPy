# trying to do the one Princeton thing
import random
from math import floor
from matplotlib import pyplot as plt
SAMPLING_RATE = 44100
ENERGY_DECAY = .994
# plotting initialization

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
        if not self.isFull():
            # print(x, self.last)
            self.items.insert(self.last, x)
            self.last = (self.last + 1) % self.capacity
            # print(self.last, len(self.items))
        else:
            raise SyntaxError("RingBuffer at capacity")

    def dequeue(self):
        '''Delete and return an item from the front. Increment first.'''
        # og_val = self.items[0]
        val = self.items.pop(self.first)
        self.first = (self.first + 1) % self.capacity
        return val
        # self.first = (self.first + 1) % self.capacity
        # x = self.items[0]
        # self.items = self.items[1:] # wait so first is being incremented twice????
        # return x
        # return og_val

    def peek(self):
        '''Return but do not delete item from front.'''
        return self.items[self.first]

    def __str__(self):
        return str(self.items)

# testing for Ring Buffer
# ring = RingBuffer(1)
# print(ring, ring.size(), ring.isEmpty(), ring.isFull())
# ring.enqueue(5)
# print(ring, ring.peek(), ring.isEmpty(), ring.isFull())
# print(ring.dequeue())

class GuitarString:
    '''A guitar string.'''
    def __init__(self, frequency):
        '''Using some equation we know that the desired capacity, n of
        the ring buffer is the sampling rate divided by the frequency.
        Therefore, we create a ring buffer of that desired capacity and
        enqueue it with n zeroes.'''
        self.tic_counter = 0 # keeps track of how often tic is called
        self.capacity = round(SAMPLING_RATE/frequency)
        self.buffer = RingBuffer(self.capacity)
        # for _ in range(self.capacity):
        #     self.buffer.enqueue(0)

    def pluck(self):
        '''Set the buffer to a trianlge wave with the necessary frequency.'''
        for i in range(self.capacity):
            try:
                # print(val)
                self.buffer.enqueue(random.uniform(-1,1))
            except SyntaxError:
                return len(self.buffer.items)
        # for setting the buffer to a triangle wave
        # for i in range(self.capacity):
        #     self.buffer.dequeue()
        #     self.buffer.enqueue(i / self.capacity - \
        #                         floor(i / self.capacity + 0.5))

    def tic(self):
        '''Applying the Karplus-Strong update. Delete the sample
        at the front of the ring buffer and then add to the end of the
        buffer the average of the first two samples multiplied by the energy
        decay factor. Tic should return None.'''
        self.tic_counter += 1
        # print('Tic:', self.buffer.last)
        new_val = 0.5 * \
                (self.buffer.items[self.buffer.last] + self.buffer.peek()) * \
                ENERGY_DECAY
        # print(self.buffer.peek())
        self.buffer.dequeue()
        self.buffer.enqueue(new_val)
        # return self.buffer.dequeue()
        # first = self.buffer.peek()
        # self.buffer.dequeue()
        # second = self.buffer.peek()
        # new_val = (first + second)/2 * ENERGY_DECAY
        # self.buffer.enqueue(new_val)

    def sample(self):
        '''Return the first value at the beginning of the buffer.'''
        return self.buffer.peek()

    def time(self):
        '''Number of times that tic was called.'''
        return self.tic_counter

    def sampler(self):
        '''Samples the buffer, and applies tic. This will happen every
        time the buffer is sampled.'''
        self.tic()
        return self.sample()


# testing for GuitarString
# b = RingBuffer(100)
# for i in range(100):
#     b.enqueue(i)
# print(b.peek())
# print(b.dequeue())
# print(b.dequeue())

# g = GuitarString(440)
# g.pluck()
# for _ in range(10):
#     print(g.sampler())
# print(g.buffer.size(),g.capacity, g.sample())
# g.pluck()
# print(g.buffer.size(), g.sample())
# g.tic()
# print(g.buffer.size(), g.sample(), g.time())
