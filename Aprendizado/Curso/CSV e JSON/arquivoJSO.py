'''
JSON

JSON - JavaScript Object Notation

'''
import json

ret = json.dumps(['produtos' , {'Playstation 4': ('2TB', 'Novo', '220V', 2340)}])

print(type(ret))
print(ret)