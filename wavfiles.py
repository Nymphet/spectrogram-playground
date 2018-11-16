# reads a wave file with scipy

from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

# open wave file
sample_rate, samples = wavfile.read('wavefiles/みとせのりこ - 荒城の月.wav')

print(sample_rate)


# deal with stereo sound
samples_0 = samples[:, 0]
samples_1 = samples[:, 1]

# save a copy of first channel (left?)
wavfile.write('wavefiles/みとせのりこ - 荒城の月_1.wav', sample_rate, samples_1)

# truncate to first n seconds
n_seconds = 10
truncated_samples = samples_0[0:sample_rate * n_seconds]
wavfile.write('wavefiles/sample_10s.wav', sample_rate, truncated_samples)


