import json
emp='''{
    "name": "anjali",
    "age": 20,
    "salary": 100000,
    "isstudent": true,
    "marks": null,
}'''
d=json.loads(emp)
print(type(emp))
print(d)
print(d["marks"])

for k,v in d.items():
    print("{}:{}".format(k,v))
                    