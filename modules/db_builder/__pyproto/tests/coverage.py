import csv
import json
import sys
from collections import defaultdict

file = '../../tmp/tests/resolve_dump_{}.csv'


n_ambigous = defaultdict(int)
n_resolved = defaultdict(int)
n_missing = defaultdict(int)
T = 0


for file_id in range(1, 5):
    with open(file.format(file_id), encoding='utf-8') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.readline())
        dialect.escapechar = "\\"

        reader = csv.DictReader(csvfile, delimiter='|', quotechar='"', dialect=dialect)
        csvfile.seek(0)

        for row in reader:
            T += 1

            for attr, val in row.items():
                if val[0] == '{' and val[-1] == '}':
                    val = '[' + val[1:-1] + ']'

                    try:
                        val = json.loads(val)
                    except:
                        if attr == 'names':
                            continue

                if isinstance(val, list):
                    L = len([v for v in val if v != 'NA'])
                elif type(val) in [str, int, float, bool]:
                    # this case doesn't actually happen because every value in the CSV is stored as an array
                    L = 1
                else:
                    raise Exception(str(type(val)))

                if L == 0: n_missing[attr] += 1
                elif L == 1: n_resolved[attr] += 1
                else: n_ambigous[attr] += 1

                # if '_id' in attr:
                #    # attr is a reference ID
                #    pass

keys = list(sorted(n_resolved.keys()))
print('\t'.join(keys))

for attr in keys:
    print(n_resolved[attr]/T, end='\t')
print("")
for attr in keys:
    print(n_ambigous[attr]/T, end='\t')
print("")
for attr in keys:
    print(n_missing[attr]/T, end='\t')
print("")
