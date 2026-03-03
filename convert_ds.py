import pandas as pd
import json

# Read ds.xlsx from workspace root
df = pd.read_excel('ds.xlsx', header=None)
# Expect col0 = dob, col1 = filename
records = []
for idx, row in df.iterrows():
    dob = str(row[0]).strip()
    filename = str(row[1]).strip()
    if dob and filename and dob.lower() != 'nan' and filename.lower() != 'nan':
        records.append({"dob": dob, "file": filename})

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(records, f, ensure_ascii=False, indent=2)

print(f'Wrote {len(records)} records to data.json')
