# 这是一个示例 Python 脚本。
# 乘方运算使用、最大值最小值判断 range函数
squares = []
for value in range(1,10):
    square = value**2
    squares.append(square)
    print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))