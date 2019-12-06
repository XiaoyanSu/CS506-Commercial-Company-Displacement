import numpy as np
import pandas as pd

df = pd.read_csv('clean_data.csv')
print(df[:10])
CS = df['MAIL CS'].tolist()
print(CS[:10])
current = []
for i in range(len(CS)):
    if CS[i] == 'ROXBURY MA' or CS[i] == 'EAST BOSTON MA' or CS[i] == 'MATTAPAN MA' or  CS[i] == 'DORCHESTER MA':
        current.append([(df['PID'][i]), (df['LU'][i]), (df['MAIL_ADDRESS'][i]), (df['MAIL CS'][i])])

current2 = pd.DataFrame(current)
print(current2[:10])
current2.columns = {'PID', 'LU', 'MAIL_ADDRESS', 'MAIL CS'}
export_csv = current2.to_csv(r'/Users/xiaoyansu/Documents/2019Fall/CS506/Project/clean_data2.csv')

