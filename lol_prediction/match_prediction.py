import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy as np
import json
import re
import time
from pandas.io.json import json_normalize

match_df = pd.read_pickle('match_data_version1.pickle')
winner_df =  pd.read_pickle('match_winner_data_version1.pickle')
loser_df = pd.read_pickle('match_loser_data_version1.pickle')

print(match_df['participants'].iloc[0][0])