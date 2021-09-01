import csv
import os

os.chdir(os.path.dirname(__file__))

html_output = ""
names = []

with open("patrons.csv", "r", encoding="UTF-8") as data_file:
    csv_reader = csv.DictReader(data_file)

    next(csv_reader)  # skip first entry

    for line in csv_reader:
        if line["FirstName"] == "No Reward":
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += f"<p>{len(names)} contributors</p>"

html_output += "\n<ul>"

for name in names:
    html_output += f"\n\t<li>{name}</li>"

html_output += "\n</ul>"

print(html_output)
