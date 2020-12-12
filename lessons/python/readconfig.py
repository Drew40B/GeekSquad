import json
from types import SimpleNamespace

with open("config.json") as json_data_file:
    data = json.load(json_data_file,object_hook=lambda d: SimpleNamespace(**d))

print (f'username: {data.database.username}')
print (f'password: {data.database.password}')