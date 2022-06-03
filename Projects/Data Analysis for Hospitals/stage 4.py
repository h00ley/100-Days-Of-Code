import pandas as pd

general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')

prenatal.rename(columns={'HOSPITAL':'hospital','Sex':'gender'}, inplace=True)
sports.rename(columns={'Hospital':'hospital','Male/female':'gender'}, inplace=True)
merged = pd.concat([general, prenatal, sports], ignore_index=True)
merged.drop(columns=['Unnamed: 0'], inplace=True)
merged.dropna(how='all', inplace=True)
merged.gender.replace(['male', 'man', 'female', 'woman'], ['m', 'm', 'f', 'f'], inplace=True)
merged.loc[merged.hospital == 'prenatal', 'gender'] = merged.loc[merged.hospital == 'prenatal', 'gender'].fillna('f')
merged[merged.columns[5:]] = merged[merged.columns[5:]].fillna(0)

hospitals_max = merged.hospital.value_counts().idxmax()
general_stomach = (merged.loc[merged.hospital == 'general', 'diagnosis'].loc[merged.diagnosis == 'stomach'].count()) / 461
sports_dri = (merged.loc[merged.hospital == 'sports', 'diagnosis'].loc[merged.diagnosis == 'dislocation'].count()) / 214
difference = (merged.loc[merged.hospital == 'general', 'age'].median()) - (merged.loc[merged.hospital == 'sports', 'age'].median())
blood_tests = merged.pivot_table(index='hospital', columns='blood_test', aggfunc='count')

print(f'The answer to the 1st question is {hospitals_max}')
print(f'The answer to the 2nd question is {general_stomach.round(3)}')
print(f'The answer to the 3rd question is {sports_dri.round(3)}')
print(f'The answer to the 4th question is {difference}')
print(f'The answer to the 5th question is {merged.loc[merged.blood_test == "t", "hospital"].max()}, {merged.loc[merged.blood_test == "t", "hospital"].value_counts().max()} blood tests')



