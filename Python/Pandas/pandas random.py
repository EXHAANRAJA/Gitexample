import numpy as np
import pandas as pd

# Create Random Array of 3 * 3 and pass it to pandas dataframe

nparrays = np.random.rand(3,3)
# Create row Label
label = ['First','Second','Third']
myseries = pd.DataFrame(nparrays,label)

# Create Column Label
myseries.columns=['First','Second','Third']

# Data Series Printing
print(myseries)