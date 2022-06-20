# j=json.dumps(emp,indent=4)
# print(type(j))
# print(j)

# with import json
# open("emp_file.txt","w") as f:
#     json.dump(emp,f,indent=4)



# import json
# d='{"a":10,"b":5,"c":6}'
# j=json.loads(d)
# print(type(j))
# print(j)


import json
d={"a":10,"b":5,"c":6}
j=json.dumps(d)
print(type(j))
print(j)
