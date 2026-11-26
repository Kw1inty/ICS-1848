
import pandas as pd

df = pd.read_csv('massive.txt', sep=r'\s+', header=None)

s1 = pd.Series(df[0])
s2 = pd.Series(df[1])
s3 = pd.Series(df[2])

common = s1[s1.isin(s2) & s1.isin(s3)].drop_duplicates()

with open('one.txt', 'w') as f:
    for number in common:
        f.write(str(number) + '\n')

print('Спільні числа:', list(common))
