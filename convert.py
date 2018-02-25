
import json
import os


def proces_file(file_name):
    f = open('maps/{}'.format(file_name))
    g = open('txt-maps/{}'.format(file_name.replace(".json", ".txt")), 'wt')

    data = json.load(f)

    max_city = 0
    for city in data['sites']:
        max_city = max(max_city, city['id'])

    # g.write('{}\n'.format(len(data['sites'])))
    g.write('{}\n'.format(max_city + 1))

    mines = data['mines']
    g.write('{}\n'.format(len(mines)))
    g.write('{}\n'.format(' '.join(map(str, mines))))
    g.write('{}\n'.format(len(data['rivers'])))
    for river in data['rivers']:
        s = river['source']
        t = river['target']
        g.write('{} {}\n'.format(s, t))
    g.close()


files = os.listdir('maps/')
for f in files:
    proces_file(f)
    # break
