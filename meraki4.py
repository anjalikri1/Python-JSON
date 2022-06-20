import json
d1={'4': 5, '6': 7, '1': 3, '2': 4}
l=[]
d={}
for k in d:
    l.append(k)
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
for x in l:
    for y in l:
        if x==y:
            d.update({x:d1[y]})
print(d)


















# d1={"a":23,"b":34,"f":67,"c":20}
# l=[]
# d={}
# for i in d1:
#     l.append(i)
#     for a in range(len(l)):
#         for b in range(len(l)):
#             if l[a]<l[b]:
#                 l[a],l[b]=l[b],l[a]


# for x in l:
#     for y in l:
#         if y==x:
#             d.update({x:d1[y]})
# print(d)





