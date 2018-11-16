# Calculates each pitch for a given temperament

import numpy as np

# general pitch names are

# C  D  E  F  G  A  B

# if in each octave we have 12 pitches, then

#   0       1       2       3       4       5       6       7       8       9       10      11      12
#   C       #C      D       #D      E       F       #F      G       #G      A       #A      B       C
#   do              re              mi      fa              sol             la              si      do
#   60      61      62      63      64      65      66      67      68      69      70      71      72


# # with MIDI standard, A4 is the 69th note, assuming we have a total of 120 notes, then
# # we can initialize an array of length 120
# n_notes = 120
# pitches = np.array([0] * n_notes)

# # Concert pitch
# pitch_A4 = 440.00
# # for the sake of consistency we will ignore the python style here and use 69 to denote the 69th item
# pitches[69] = pitch_A4

def twelve_tone_equal(A4=69, n_notes=120, pitch_A4=440.00):
    # 12-tone equal temporament
    # pitches[69] is the 69th note
    pitches = np.zeros(n_notes)
    pitches[A4] = pitch_A4

    for i in range(len(pitches)):
        pitches[i] = pitches[A4] * 2**((i - 69) / 12)

    return pitches





