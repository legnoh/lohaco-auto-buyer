import json,yaml,os,shutil

genres = {}
lists = {}
urls = {}

# items ディレクトリ配下のファイルを一旦全て削除する
shutil.rmtree('./items/', ignore_errors=True)
os.makedirs('./items/', exist_ok=True)

# read yml file
with open('./config/items.yml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

genres = {}

# convert list to dict
for genre_name, genre in config['genres'].items():

    index_genre_value = ""
    lists[genre_name] = {}
    urls[genre_name] = {}
    for item in genre['items']:
        os.makedirs(f"./items/{genre_name}/{item['product_name']}", exist_ok=True)
        if index_genre_value != "":
            index_genre_value += ","
        index_genre_value += item['product_name']
        lists[genre_name][item['product_name']] = item['candidates'][0]['name']
        urls[genre_name][item['product_name']] = {}
        i = 1
        for candidate in item['candidates']:
            with open(f"./items/{genre_name}/{item['product_name']}/{i}", 'w') as s:
                s.write(candidate['url'])
            urls[genre_name][item['product_name']][candidate['name']] = candidate['url']
            i += 1
    genres[genre_name] = index_genre_value

# write index json file
with open('items/index.json', 'w') as s:
    json.dump(genres, s, indent=2)
for genre, value in lists.items():
    with open(f"items/{genre}/index.json", 'w') as s:
        json.dump(lists[genre], s, indent=2)

# write urls text file
for genre, products in urls.items():
    for product_name, candidates in products.items():
        with open(f"./items/{genre}/{product_name}/index.json", 'w') as s:
            json.dump(candidates, s, indent=2)
