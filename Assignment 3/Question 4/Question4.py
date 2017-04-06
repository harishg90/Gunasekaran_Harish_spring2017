import pandas as pd
import numpy as np
import re

data = pd.read_csv('C:/Users/ABC/DataAnalysis4Python_Spring17/Assignments/Assignment 3/Data/movies_awards.csv', sep=',')[['Title','Awards']]

data['Awards Won'] = data['Awards'].str.extract('(\d+) w', expand=True).fillna(0)
data['Awards Nominated']  = data['Awards'].str.extract('(\d+) n', expand=True).fillna(0)
data['BAFTAs Won']  = data['Awards'].str.extract('Won (\d+) BAFTA', expand=True).fillna(0)
data['Oscars Won']  = data['Awards'].str.extract('Won (\d+) Oscar[s]?', expand=True).fillna(0)
data['Prime Won'] = data['Awards'].str.extract('Won (\d+) Prime', expand=True).fillna(0)
data['Golden Globes Won'] = data['Awards'].str.extract('Won (\d+) Golden', expand=True).fillna(0)
data['Nominated for BAFTA']  = data['Awards'].str.extract('Nominated for (\d+) BAFTA', expand=True).fillna(0)
data['Nominated for OSCAR']  = data['Awards'].str.extract('Nominated for (\d+) Oscar', expand=True).fillna(0)
data['Nominated for Prime'] = data['Awards'].str.extract('Nominated for (\d+) Prime', expand=True).fillna(0)
data['Nominated for Golden Globe'] = data['Awards'].str.extract('Nominated for (\d+) Golden', expand=True).fillna(0)
data.to_csv('Question4Output.csv', sep=',', encoding='utf-8')