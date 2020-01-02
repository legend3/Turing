# 系统默认的模块搜索路径
import sys

print(type(sys.path))
print(sys.path)  # 属性可以获取路径列表

for p in sys.path:
    print(p)
