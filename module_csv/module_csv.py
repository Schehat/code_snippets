import csv
import os

os.chdir(os.path.dirname(__file__))

with open("names.csv", "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)  # skips first element of the iterable

    for line in csv_reader:
        if any(datapoint.strip() for datapoint in line):  # skip blank rows
            print(line)

# copy in another file
with open("names.csv", "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("new_names.csv", "w", encoding="UTF-8", newline="\n") as new_file:
        # create writer with new delimiter
        csv_writer = csv.writer(new_file, delimiter="\t")

        # write rows from original csf_file
        for line in csv_reader:
            print(line)
            csv_writer.writerow(line)

# # read with different delimiter
# with open("new_names.csv", "r", encoding="UTF-8") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter="\t")

# using Dict
with open("names.csv", "r", encoding="UTF-8") as csv_file:
    # pro: headers are keys, no indexing required for specifying a field
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line["email"])  # instead of line[2] in the csv.reader method

# copy in another file with Dict
with open("names.csv", "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open("new_names.csv", "w", encoding="UTF-8", newline="\n") as new_file:
        fieldnames = ["first_name", "last_name", "email"]

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter="\t")

        csv_writer.writeheader()  # to include header

        for line in csv_reader:
            csv_writer.writerow(line)

# copy in another file with Dict and exclude a field
with open("names.csv", "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open(
        "new_names_ex_email.csv", "w", encoding="UTF-8", newline="\n"
    ) as new_file:
        fieldnames = ["first_name", "last_name"]  # excluded email

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter="\t")

        csv_writer.writeheader()

        for line in csv_reader:
            del line["email"]  # delete field
            csv_writer.writerow(line)
