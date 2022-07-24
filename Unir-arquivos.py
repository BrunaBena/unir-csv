import os
import pandas as pd

master_df = pd.DataFrame()

for file in os.listdir(os.getcwd()):
    if file.startswith('ca'):
        master_df = master_df.append(pd.read_csv(file, sep=';'))

master_df.to_csv('Concatenado.csv', index=False)