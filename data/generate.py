import csv

filename = "citations.csv"
output = "../content/publications/index.md"

data = []
with open(filename, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header if necessary
    next(csv_reader)

    for row in csv_reader:
        data.append(row)


data_sorted = sorted(data, key=lambda x: x[6], reverse=True)

data_out = "+++\ntitle = 'Publications'\n date = 2023-11-11T03:08:47+01:00\n draft = false\n+++\n\n## Publication List ({})\n\n""".format(len(data_sorted))

## Liste des publications"
for data_temp in data_sorted:
    data_out += "* {} *{}*, {}, {}\n".format(data_temp[0], data_temp[1], data_temp[2], data_temp[6])

with open(output, 'w') as file:
    file.write(data_out)
