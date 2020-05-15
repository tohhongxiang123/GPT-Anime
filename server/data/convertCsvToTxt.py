import pandas as pd
import re

df = pd.read_csv('animes.csv')

synopses = []
failedRows = 0
totalRows = 0
for index, row in df.iterrows():
    totalRows += 1
    try:
        cleaned = re.sub(r'\(.+\)$', '', row['synopsis']).replace('\r\n', '\n').strip()
        formatted = '\n\n'.join([row['title'], cleaned])
        synopses.append(formatted)
    except Exception as e:
        failedRows += 1


with open('formattedAnimes.txt', 'w', encoding='utf-8') as f:
    for data in synopses:
        f.write(data)
        f.write('\n<|endoftext|>\n')

print('Completed {} rows with {} failed'.format(totalRows, failedRows))

