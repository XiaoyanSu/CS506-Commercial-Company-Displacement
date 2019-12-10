import pandas as pd
import numpy as np

df = pd.read_csv('combined_all_business.csv')
df2 = pd.read_csv('Combined Closed Business.csv')
hold_closed = []

print(df.shape)
print(df2.shape)
print(df2['Company Name'][:10])


for i in range(len(df)):
    if df['Record Type'][i]!='Verified':
        hold_closed.append([(df['Company Name'][i]),(df['Executive First Name'][i]), (df['Executive Last Name'][i]), (df['Address'][i]), (df['City'][i]), (df['State'][i]), (df['ZIP Code'][i]), (df['Record Type'][i]), (df['Executive Ethnicity'][i]), (df['Executive Gender'][i]), (df['Phone Number'][i]), (df['Square Footage'][i]), (df['Latitude'][i]), (df['Longitude'][i]), (df['Rent Expenses'][i]), (df['Type of Business'][i]), (df['Location Type'][i])]) 

closed_business = pd.DataFrame(hold_closed)
print(closed_business.shape)




"""Gender Analysis"""


closed_gender = df2[['Company Name','Executive Gender','City','Address']].dropna(axis=0,subset=['Executive Gender'])
print(closed_gender.shape)
print(closed_gender['Executive Gender'][:10])


Male_exective = []
Female_executive = []

for i in range(len(closed_gender)):
    if closed_gender['Executive Gender'][i] == 'Male':
        print(closed_gender['Executive Gender'][i])
        Male_exective.append([(closed_gender['Company Name'][i]),(closed_gender['Executive Gender']),(closed_gender['City'][i]),(closed_gender['Address'][i])])
    if closed_gender['Executive Gender'][i] != 'Male':
        print(closed_gender['Executive Gender'][i])
        Female_exective.append([(closed_gender['Company Name'][i]),(closed_gender['Executive Gender']),(closed_gender['City'][i]),(closed_gender['Address'][i])])

Male_exective = pd.DataFrame(Male_exective)
Female_exective = pd.DataFrame(Male_exective)
