import json,yaml

genres = {}
lists = {}

# read yml file
with open('config/items.yml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

# convert list to dict
for key, genre in config['stores'][0]['genres'].items():
    genres[key] = genre['name']
    lists[key] = {}
    for item in genre['items']:
        lists[key][item['product_name']] = item['candidates'][0]['name']

# write json file
for key, value in lists.items():
    with open('items/'+key+'.json', 'w') as outfile:
        json.dump(lists[key], outfile)

with open('items/index.json', 'w') as stream:
    json.dump(genres, stream, indent=2)
