

import numpy as np

mental_health_data = np.random.randint(low=0, high=10, size=(3,3))
np.save('mental_health_data', mental_health_data)