import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import numpy as np
from matplotlib.ticker import MultipleLocator
from datetime import datetime




# read a wav file which is a real music file

wavfile_name = 'wavefiles/sample_10s.wav'

sample_rate, samples = wavfile.read(wavfile_name)


# I want to see which parameter works best for musical waves, bu apparantly I have
# no choice but try them all...

from spectrogram2 import draw_log_scale_log_spectrogram_12tone

for i in range(10,27):
    nperseg = 2**i
    for j in range(0, 9):
        nfft = nperseg * 2**j
        for k in range(1, 27):
            noverlap = nperseg - (nperseg // (2**k))

            print('Drawing for {filename} with params: nperseg={nperseg}, nfft={nfft}, noverlap={noverlap}'.format(filename=wavfile_name, nperseg=nperseg, nfft=nfft, noverlap=noverlap))

            start_time = datetime.now()

            try:
                draw_log_scale_log_spectrogram_12tone(samples, sample_rate, nperseg=nperseg, nfft=nfft,
                            noverlap=noverlap, vmax=None, dpi=600, cmap='nipy_spectral', filename='sample_10s')
            except TimeoutError as e:
                print("Timed out!")
            except KeyboardInterrupt as e:
                print(e)
                exit(0)
            except Exception as inst:
                print('Unexpected Exception happened: ', inst)
                continue
            
            time_elapsed = datetime.now() - start_time

            print('Done. Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))

