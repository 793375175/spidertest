import json
from jsonpath import jsonpath

json_str = '''
{ "store": {
    "book": [ 
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}
'''
json_dic = json.loads(json_str)

# print(jsonpath( json_dic, '$.store.book'))

# 获取书的所有的作者
# print(jsonpath(json_dic,'$.store.book[*].author'))
# jsonpath(json_dic,'$..author')
# print(jsonpath(json_dic, '$.store.*'))
# print(jsonpath(json_dic, '$..book[2]'))
# print(jsonpath(json_dic, '$..book[(@.length-1)]'))
# print(jsonpath(json_dic, '$..book[0,1]'))
# print(jsonpath(json_dic, '$..book[?(@.isbn)]'))
# print(jsonpath(json_dic, '$..book[?(@.price>10)]'))
print(jsonpath(json_dic, '$..*'))