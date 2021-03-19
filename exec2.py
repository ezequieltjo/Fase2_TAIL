"""
    Exercício 2 - Fase 2
"""
import pandas as pd
dataset = pd.read_csv('https://raw.githubusercontent.com/franklinthony/dataset/master/titanic_disaster.csv', sep = ',')
print(dataset.describe())