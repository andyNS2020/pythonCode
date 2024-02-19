# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。
    print("That's in.")

def print_hi2():
    first_name = "ada"
    last_name = "lovelace"
    full_name = first_name + " " + last_name
    message = "Hello, " + full_name.title() + "!"
    print(message)

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('test')
print("That's out true.")
print_hi2()
message = "Hello Python world!"
print(message)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
