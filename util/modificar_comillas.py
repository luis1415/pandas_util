import pandas as pd
import numpy as np
import csv

df = pd.read_csv('Enrollment.csv')
df = df.drop(df.columns[[1, 7]], axis=1)
df = df.fillna('')
for i in list(df.columns):
    df[i] = '\"' + df[i].astype(str) + '\"'
df.to_csv('Enrollment_nuevo.csv', sep=',', index=False, encoding='utf-8', quotechar="\"", doublequote=True, quoting=csv.QUOTE_NONE)
