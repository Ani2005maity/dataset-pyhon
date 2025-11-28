import numpy as np
import pandas as pd
num_rows = 20
num_cols = 5
column_names = [f'Feature_{i+1}' for i in range(num_cols)]
random_data = np.random.rand(num_rows, num_cols)
df = pd.DataFrame(random_data, columns=column_names)
print("Random DataFrame Head:")
print(df.head())
df.to_csv('dataset.csv')
