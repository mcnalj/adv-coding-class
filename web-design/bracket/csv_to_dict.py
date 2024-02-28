import csv, json
data = {}
with open('team-data.csv', encoding='utf-8', newline='')as csvfile:
    contents = csv.DictReader(csvfile)
    for row in contents:
        key = row["id"]
        data[key] = row
with open('team-data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=4))
