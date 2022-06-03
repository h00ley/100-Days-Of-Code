import pandas as pd
import matplotlib.pyplot as plt


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

merged.age.plot(kind='hist', bins=[0, 15, 35, 55, 70, 80])
plt.show()
merged.diagnosis.value_counts().plot(kind='pie')
plt.show()
fig, axs = plt.subplots()
plt.violinplot(merged.height, showmeans=True, showmedians=True)
plt.show()

print(f'''The answer to the 1st question: 15-35
The answer to the 2nd question: {merged.diagnosis.value_counts().idxmax()}
The answer to the 3rd question: It's because...''')

