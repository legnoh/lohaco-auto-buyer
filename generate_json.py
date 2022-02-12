import json,yaml

lists = {}

# read yml file
with open('config/items.yml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

# convert list to dict
for item in config['stores'][0]['items']:
    lists[item["product_name"]] = item['candidates'][0]['name']

# write json file
with open('items/y-lohaco.json', 'w') as stream:
    json.dump(lists, stream, indent=2)
