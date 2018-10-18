import json

json_str = '{"name":"laowang", "age":18, "hobby":["炼妖","练手"]}'

# json字符串-->dict
dict = json.loads(json_str)
# print(dict)
# print(type(dict))

json_str = json.dumps(dict, ensure_ascii=False)
# print(json_str)
# print(type(json_str))

with open('1_测试.json','w',encoding='utf8') as f:
    json.dump(dict,f,ensure_ascii=False,indent=2)

with open('1_测试.json','r', encoding='utf8')as f:
    dic = json.load(f)
    print(dic)