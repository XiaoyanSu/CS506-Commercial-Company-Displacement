import pandas as pd
import numpy as np

df = pd.read_csv('new_all_business.csv')

df= df.dropna(subset = ['Rent Expenses', 'Square Footage'])
df = df.reset_index()

rent = list(df['Rent Expenses'])

print(len(rent))
for i in range(len(rent)):
    if 'Less than' in rent[i]:
        rent[i] = '$0 to'+ rent[i][rent[i].index('n')+1:]
        #print(rent[i])
    if 'Over' in rent[i]:
        rent[i] = rent[i][rent[i].index('r')+2:]
        #print(rent[i])

mean_rent = []

for i in range(len(rent)):
    if 'to' in rent[i]:
        rent[i] = rent[i].split(' to ')
    else:
        rent[i] = [rent[i]]

    sum_ = 0
    for each in rent[i]:
        each = each.replace(',', '')
        each = each.replace('$', '')
        sum_+= int(each)

    mean = sum_/len(rent[i])
    mean_rent.append(mean)

df['Rent Expenses'] = mean_rent

print(mean_rent[:10])
print(df['Rent Expenses'][:20])


sq = list(df['Square Footage'])
print(len(sq))

mean_sq = []
for j in range(len(sq)):
    if '-' not in sq[j]:
        sq[j] = [sq[j]]

    sum_2 =0
    if '-' in sq[j]:
        sq[j] = sq[j].split(' - ')

    for each in sq[j]:
        each  = each.replace(',', '')
        sum_2+=int(each)

    mean = sum_2/len(sq[j])
    mean_sq.append(mean)

df['Square Footage'] = mean_sq
print(mean_sq[:10])
print(df['Square Footage'][:20])

rent_sq_ft = []

def round2(x):
    return round(float(x)+0.00000000001,2)

for k in range(len(mean_sq)):
    outcome = round2(mean_rent[k]/mean_sq[k])
    rent_sq_ft.append(outcome)

print(rent_sq_ft[:10])
df['Rent per Square Foot'] = rent_sq_ft

export_csv2 = df.to_csv(r'/Users/xiaoyansu/Documents/2019Fall/CS506/CS506-Commercial-Company-Displacement/Cleaned Data 2019/data5.csv')

