import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import numpy as np
from matplotlib.ticker import MultipleLocator
from datetime import datetime


# I want to see which parameter works best for musical waves, bu apparantly I have
# no choice but try them all...

from spectrogram2 import draw_log_scale_log_spectrogram_12tone

for i in range(10,27):
    nperseg = 2**i
    for j in range(0, 9):
        nfft = nperseg * 2**j
        # default
        noverlap = nperseg // 8
        print('python3 test_for_param_single_run.py {nperseg} {nfft} {noverlap}'.format(nperseg=nperseg, nfft=nfft, noverlap=noverlap))
        # and more params we want to test
        for k in range(1, 27):
            noverlap = nperseg - (nperseg // (2**k))
            print('python3 test_for_param_single_run.py {nperseg} {nfft} {noverlap}'.format(nperseg=nperseg, nfft=nfft, noverlap=noverlap))
        

