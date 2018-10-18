import js2py

# 1.获取执行js的环境
context = js2py.EvalJs()

# 2.加载和执行js
js_code = '''
a = 10
function func(x){
    return x * x
}
'''
# 执行js
context.execute(js_code)

# 获取context数据
print(context.a)
print(context.func(10))

context.dic = {
    'a': 100
}

print(context.dic.to_dict())
print(type(context.dic))
print(type(context.dic.to_dict()))