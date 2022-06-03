import pandas as pd
pd.set_option('display.max_columns', 8)

general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')

prenatal.rename(columns={'HOSPITAL':'hospital','Sex':'gender'}, inplace=True)
sports.rename(columns={'Hospital':'hospital','Male/female':'gender'}, inplace=True)
merged = pd.concat([general, prenatal, sports], ignore_index=True)
merged.drop(columns=['Unnamed: 0'], inplace=True)
print(merged.sample(n=20, random_state=30))

