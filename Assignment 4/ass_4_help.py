import requests
import pandas as pd
import numpy as np

data = pd.read_csv("nba_all_elo.csv")
pd.set_option("display.max.columns", None)
type(data)

data.index.name = 'game_id'

unique_fran = data['opp_fran'].unique()

data['high_scores'] = np.where(data['opp_pts'] > 100, 'y', 'n')

top_10 = data.head(10)

TW = data[data['fran_id'] == 'Timberwolves']

TW = data[data['fran_id'] == 'Timberwolves']

print(data.shape)
data = data.set_index('game_id')
print(data.shape)
print(data.head(10))

data['high_scores'].count()

subset = data['fran_id', 'pts', 'opp_fran', 'opp_pts', 'high_score']
subset = data['fran_id']