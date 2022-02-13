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
        os.makedirs('./items/{genre}/{product}'.format(genre=genre_name,product=item['product_name']), exist_ok=True)
        index_genre_value += item['product_name'] + ","
        lists[genre_name][item['product_name']] = item['candidates'][0]['name']
        urls[genre_name][item['product_name']] = {}
        i = 1
        for candidate in item['candidates']:
            with open('./items/{genre}/{product}/{i}'.format(genre=genre_name, product=item['product_name'],i=i), 'w') as s:
                s.write(candidate['url'])
            urls[genre_name][item['product_name']][candidate['name']] = candidate['url']
            i += 1
    genres[genre_name] = index_genre_value

# write index json file
with open('items/index.json', 'w') as s:
    json.dump(genres, s, indent=2)

for genre, value in lists.items():
    with open('items/{genre}/index.json'.format(genre=genre), 'w') as s:
        json.dump(lists[genre], s, indent=2)

for genre, products in urls.items():
    for product_name, candidates in products.items():
        with open('./items/{genre}/{product}/index.json'.format(genre=genre, product=product_name), 'w') as s:
            json.dump(candidates, s, indent=2)
