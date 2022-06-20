import json

d={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}

f= open("myfile.json", "w")
  
json.dump(d, f, indent = 6)
  
f.close()







# a=json.dumps(d)
# print(a)
# print(type(a))
# print(type(d))