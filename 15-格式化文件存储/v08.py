import json


data = {"name":"hahah", "age":12}


with open("func.json", 'w') as f:
    json.dump(data, f)#python内容写入json


with open("func.json", 'r') as f:
    d = json.load( f)
    print(d)

