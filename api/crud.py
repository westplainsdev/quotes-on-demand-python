import json

with open('data.json') as json_file:
    data = json.load(json_file)


def get():
    return json.dumps(data)


def get_by_id(id):
    for item in data:
        if item['id'] == int(id):
            print('The object found is: ', item)
            return json.dumps(item)


def create(quote):
    max_item = max(data, key=lambda ev: ev['id'])
    new_id = int(max_item['id']) + 1
    print('The next ID is: ', new_id)
    quote['id'] = new_id
    print('The new quote is: ', quote)
    data.append(quote)
    return json.dumps(data)


def update(quote):
    for index, item in enumerate(data):
        if item['id'] == int(quote['id']):
            print('The object was: ', item)
            item = quote
            print('The object now is: ', item)
            data[index] = item
            return json.dumps(data)


def delete(id):
    for item in data:
        if item['id'] == int(id):
            data.remove(item)
            return json.dumps(data)
