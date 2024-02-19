# 这是一个示例 Python 脚本。
# 元组：不能修改单个元素，但是可以重新定义

dimensions = (200, 50)
#dimensions[0] = 250
print(dimensions[0])
print(dimensions[1])
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)