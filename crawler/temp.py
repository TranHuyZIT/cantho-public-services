import os
import json

data = []


for file in os.listdir(f"./data/thutuchanhchinh"):
    with open(os.path.join(f"./data/thutuchanhchinh", file), 'r') as json_file:
        try:
            print(file)
            data.append(json.load(json_file))
            json_file.close()
        except Exception as e:
            continue


with open(f"./data//thutuchanhchinh/thutuchanhchinh.json", 'w') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
    json_file.close()