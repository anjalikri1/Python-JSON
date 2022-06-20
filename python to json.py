import json
d={
    "name": "David", 
    "class": "I", 
    "age": 6
}
j=json.dumps(d)
print(type(d))
print(type(j))