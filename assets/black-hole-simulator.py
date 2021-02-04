import numpy as np

def evap_ee( n_pairs ):
    total = [0 for j in range( 2*n_pairs )] # initializes BH
    ee_record = list(range( 2*n_pairs + 1)) # sets up array to record entanglement entropy
    for i in range( 2*n_pairs ): # time steps for BH evaporation
        bh = [j for j in range( 2*n_pairs ) if total[j] == 0] # generates list of qubits in BH
        evap = np.random.choice( bh ) # randomly chooses qubit in BH to evaporate
        total[evap] = 1 # emit qubit
        ee = sum([1 for k in range( n_pairs ) if total[ 2*k ] + total[ 2*k + 1] == 1]) # compute entanglement entropy
        ee_record[i+1] = ee # record entanglement entropy
    return ee_record

import matplotlib.pyplot as plt # plotting package

plt.style.use('seaborn-whitegrid') # stylish

ee_data = evap_ee(5000) # go with 5000 pairs for a smooth curve
plt.plot(range(1, 2*5000 + 2), ee_data)
plt.show()

# ------------
# To do:
# - Try messing around with this by, e.g. every now and
# again replacing an outgoing qubit with a random coin flip.
# This should give something in between Hawking and Page!
# - Find the equation for this simple Page curve.
# ------------
# David Wakeham, Feb 1, 2021
# <david.a.wakeham@gmail.com>
# ------------
