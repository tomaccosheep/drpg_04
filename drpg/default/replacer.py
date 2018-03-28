import json
import fileinput
file = open('replace.json', 'r')
conf_dict = json.load(file)
for i in conf_dict.keys():
    if i[0:3] == 'sty':
        for line in fileinput.input(['templates/user_app/index.html'], inplace=True):
            print(line.replace(i, conf_dict[i]), end='')
