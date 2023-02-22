

import numpy as np

# Create an array of 64 elements with values from 0 to 63
data = np.arange(64)

# Reshape the array into a 8x8 matrix
data = data.reshape(8, 8)

# Save the array to a .npy file
np.save('mental_health_data.npy', data)
