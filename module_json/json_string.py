import json

people_string = """
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7154",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "John Doe",
            "phone": "560-555-7164",
            "emails": null,
            "has_license": true
        }
    ]
}
"""

data = json.loads(people_string)
print(f"json converted into: {type(data)}\n")

print(data)

print("\niteration over people:")
for people in data["people"]:
    print(people)

    del people["phone"]

# convert dict to json, indent intends 2 per level in json format
new_string = json.dumps(data, indent=2, sort_keys=True)
print(f"\nmodified json string:\n{new_string}")
