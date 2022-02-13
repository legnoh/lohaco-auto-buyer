import json,yaml,os

genres = {}
lists = {}
urls = {}

# read yml file
with open('config/items.yml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

# convert list to dict
for key, genre in config['genres'].items():
    genres[key] = genre['name']
    lists[key] = {}
    urls[key] = {}
    for item in genre['items']:
        lists[key][item['product_name']] = item['candidates'][0]['name']
        urls[key][item['product_name']] = {}
        for candidate in item['candidates']:
            urls[key][item['product_name']][candidate['name']] = candidate['url']

# write json file
with open('items/index.json', 'w') as s:
    json.dump(genres, s, indent=2)

for genre, value in lists.items():
    os.makedirs('./items/{genre}'.format(genre=genre), exist_ok=True)
    with open('items/{genre}/index.json'.format(genre=genre), 'w') as s:
        json.dump(lists[genre], s, indent=2)

for genre, products in urls.items():
    for product_name, candidates in products.items():
        with open('./items/{genre}/{product_name}.json'.format(genre=genre, product_name=product_name), 'w') as s:
            json.dump(candidates, s, indent=2)
