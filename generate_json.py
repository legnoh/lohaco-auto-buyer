import json,yaml,os

genres = {}
lists = {}
urls = {}

# read yml file
with open('config/items.yml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

genres = {}

# convert list to dict
for genre_name, genre in config['genres'].items():

    # value部分にカンマ区切りのプロダクト名一覧を入れる
    index_genre_value = ""
    lists[genre_name] = {}
    urls[genre_name] = {}
    for item in genre['items']:
        index_genre_value += item['product_name'] + ","
        lists[genre_name][item['product_name']] = item['candidates'][0]['name']
        urls[genre_name][item['product_name']] = {}
        for candidate in item['candidates']:
            urls[genre_name][item['product_name']][candidate['name']] = candidate['url']
    genres[genre_name] = index_genre_value

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
