import os
import json

os.chdir(os.path.dirname(__file__))

with open("states.json", "r", encoding="UTF-8") as json_file:
    data = json.load(json_file)

for state in data["states"]:
    del state["area_codes"]

with open("new_states.json", "w", encoding="UTF-8") as json_file:
    json.dump(data, json_file, indent=2)
