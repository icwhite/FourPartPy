# wavetable synthesis
# https://flothesof.github.io/Karplus-Strong-algorithm-Python.html
import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(0, 1, num=100)
wavetable = np.sin(np.sin(2 * np.pi * t))
# plt.plot(t, wavetable, '-o')
def synthesize(sampling_speed, wavetable, n_samples):
    """Synthesizes a new waveform from an existing wavetable."""
    samples = []
    current_sample = 0
    while len(samples) < n_samples:
        current_sample += sampling_speed
        current_sample = current_sample % wavetable.size
        samples.append(wavetable[current_sample])
        current_sample += 1
    return np.array(samples)
sample1 = synthesize(1, wavetable, 300)
sample2 = synthesize(2, wavetable, 300)

plt.plot(sample1)
plt.plot(sample2)
plt.xlabel('sample number')
plt.show()
