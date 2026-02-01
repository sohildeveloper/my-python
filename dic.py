import json

# json file open karo 
with open("dic.json", "r") as file:
    dic = json.load(file)

# get method
    # c=dic.get("skills")
    # print(c)

# keys method
# for a in dic.keys():
#     print(a) 

# # values method
# for b in dic.values():
#     print(b)

# # items method
# for c in dic.items():
#     print(c)
    # print(dic)

# delete dictionary item
del dic['age']
print(dic)

# pop method
dic.pop('name')
print(dic)
# d={
#     'name': 'sohil khna',
#     'age': 21,
#     'city': 'ahmedabad'
# }

# f=d['age']
# print(f)

# print(d)
# print(d['name'])

# for n in d:
#     print(n)
#     print(d[n])

# print(dic)