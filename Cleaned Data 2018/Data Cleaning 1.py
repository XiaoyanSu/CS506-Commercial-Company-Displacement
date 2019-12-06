import numpy as np
import pandas as pd

df = pd.read_csv('project506.csv')
LU1 = df['LU'].tolist()
current = []
for i in range(len(LU1)):
    if LU1[i] == 'RC' or LU1[i] == 'C':
        current.append([(df['PID'][i]), (df['LU'][i]), (df['MAIL_ADDRESS'][i]), (df['MAIL CS'][i])])


current2 = pd.DataFrame(current)

current2.columns = {'PID', 'LU', 'MAIL_ADDRESS', 'MAIL CS'}
print(current2[:10])
export_csv = current2.to_csv(r'/Users/xiaoyansu/Documents/2019Fall/CS506/Project/clean_data.csv')
