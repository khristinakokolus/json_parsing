import json


def read_json(file):
    '''
    (NoneType) -> dict

    Function that reads json file and decodes it
    '''
    with open(file, encoding='utf-8') as f:
        data = json.load(f)
    return data


def navigation(key_lst, data):
    '''
    (list) -> dict

    Function that returns the dictionary with keys of the screen_name
    of the user and value that is the information from the key that
    chose the user.
    '''
    info_dct = {}
    if key_lst[0] == "entities":
        if key_lst[1] == 'url':
            for j in range(len(data['users'])):
                try:
                    key = data['users'][j]['screen_name']
                    value = data['users'][j][key_lst[0]][key_lst[1]]['urls'][0][key_lst[2]]
                    info_dct[key] = value
                except Exception:
                        info_dct[key] = 'no information'
                        continue
            return info_dct
        elif key_lst[1] == 'description':
            for i in range(len(data['users'])):
                key = data['users'][i]['screen_name']
                value = data['users'][i][key_lst[0]][key_lst[1]]['urls']
                info_dct[key] = value
            return info_dct
    elif key_lst[0] == "status":
        if key_lst[1] == 'entities':
            for el in range(len(data['users'])):
                try:
                    key = data['users'][el]['screen_name']
                    value = data['users'][el][key_lst[0]][key_lst[1]][key_lst[2]][0][key_lst[3]]
                    info_dct[key] = value
                except Exception:
                    info_dct[key] = 'no information'
                    continue
            return info_dct
        elif key_lst[1] == 'retweeted_status':
            if key_lst[2] == 'entities':
                for el in range(len(data['users'])):
                    try:
                        key = data['users'][el]['screen_name']
                        value = data['users'][el][key_lst[0]][key_lst[1]][key_lst[2]][key_lst[3]][0][key_lst[4]]
                        info_dct[key] = value
                    except Exception:
                        info_dct[key] = 'no information'
                        continue
                return info_dct
            else:
                for el in range(len(data['users'])):
                    try:
                        key = data['users'][el]['screen_name']
                        value = data['users'][el][key_lst[0]][key_lst[1]][key_lst[2]]
                        info_dct[key] = value
                    except Exception:
                        info_dct[key] = 'no information'
                        continue
                return info_dct
        else:
            for i in range(len(data['users'])):
                try:
                    key = data['users'][i]['screen_name']
                    value = data['users'][i][key_lst[0]][key_lst[1]]
                    info_dct[key] = value
                except Exception:
                    info_dct[key] = 'no information'
                    continue
            return info_dct
    else:
        for i in range(len(data['users'])):
            key = data['users'][i]['screen_name']
            value = data['users'][i][key_lst[0]]
            info_dct[key] = value
        return info_dct


if __name__ == "__main__":
    data = read_json('friends_locations.json')
    keys = ', '.join(data['users'][0].keys())
    try:
        print('Here are keys to choose from: ', keys)
        keyy = input('Please enter a key(one of the proposed):')
        keys_lst = []
        keys_lst.append(keyy)
        if keyy == "entities":
            keys = ', '.join(data['users'][0]['entities'].keys())
            print('This key contain other keys: ', keys)
            keyy2 = input("Please choose one of these keys or the word all: ")
            keys_lst.append(keyy2)
            if keyy2 == 'url':
                keys = data['users'][0]['entities']['url']['urls'][0].keys()
                keys = ', '.join(keys)
                print('This key also has some other keys: ', keys)
                keyy3 = input("Please choose one of these keys: ")
                keys_lst.append(keyy3)
                print(navigation(keys_lst, data))
            elif keyy2 == 'description':
                print(navigation(keys_lst, data))
        elif keyy == "status":
            keys = ', '.join(data['users'][0]['status'].keys())
            keys = keys + ', ' + 'retweeted_status'
            print('This key contain other keys: ', keys)
            keyy2 = input('Please choose one of them: ')
            keys_lst.append(keyy2)
            if keyy2 == 'entities':
                keys = ', '.join(data['users'][0]['status']['entities'].keys())
                print('This key has some other keys:', keys)
                keyy3 = input("Please enter a key: ")
                keys_lst.append(keyy3)
                if keyy3 == 'user_mentions':
                    keys = "screen_name, name, id, id_str, indices"
                    print('This key has some other keys: ', keys)
                    keyy4 = input('Pleasee enter a key: ')
                    keys_lst.append(keyy4)
                    print(navigation(keys_lst, data))
                elif keyy3 == 'urls':
                    keys = "url, expanded_url, display_url, indices"
                    print('This key has some other keys: ', keys)
                    keyy4 = input('Please enter a key: ')
                    keys_lst.append(keyy4)
                    print(navigation(keys_lst, data))
                elif keyy3 == 'hashtags':
                        print('There are other keys: text,indices')
                        keyy4 = input('Please enter a key: ')
                        keys_lst.append(keyy4)
                        print(navigation(keys_lst, data))
                else:
                    print(navigation(keys_lst, data))
            elif keyy2 == 'retweeted_status':
                keyy3 = input('This key has other keys:')
                keys_lst.append(keyy3)
                if keyy3 == 'entities':
                    keys = data['users'][0]['status']['entities'].keys()
                    keys = ', '.join(keys)
                    print('This key has some other keys: ', keys)
                    keyy4 = input("Please enter a key: ")
                    keys_lst.append(keyy4)
                    if keyy4 == 'user_mentions':
                        keys = "screen_name, name, id, id_str, indices"
                        print('This key has some other keys: ', keys)
                        keyy5 = input('Please enter a key: ')
                        keys_lst.append(keyy5)
                        print(navigation(keys_lst, data))
                    elif keyy4 == 'urls':
                        keys = "url, expanded_url, display_url, indices"
                        print('This key has some other keys: ', keys)
                        keyy5 = input('Please enter a key: ')
                        keys_lst.append(keyy5)
                        print(navigation(keys_lst, data))
                    elif keyy4 == 'hashtags':
                        print('There are other keys: text,indices')
                        keyy5 = input('Please enter a key')
                        keys_lst.append(keyy5)
                        print(navigation(keys_lst, data))
                    else:
                        print(navigation(keys_lst, data))
                else:
                    print(navigation(keys_lst, data))
            else:
                print(navigation(keys_lst, data))

        else:
            print(navigation(keys_lst, data))
    except Exception:
        print('Inputted key is not available!')

