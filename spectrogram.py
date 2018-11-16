# with matplotlib

from scipy.io import wavfile
import numpy as np

import matplotlib.pyplot as plt

sample_rate, samples = wavfile.read('wavefiles/test.wav')

# draw a spectrogram
for i in [8,9,10,11]:
    NFFT = 2**i
    plt.specgram(samples, NFFT=NFFT, Fs=sample_rate)
    plt.savefig('figs/specgram_NFFT' + str(NFFT) + '.png', dpi=600)