# Q.3 Python object ko json string mai convert karne ka program likho?
import json
d={"name":"anjali","age":20,"is student?":True,"is married?":False,"salary":None}
j=json.dumps(d)
print(j)
print(type(d))
print(type(j))
