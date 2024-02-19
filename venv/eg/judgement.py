# 判断语句
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

age = 19
if age == 18:
    print("You are old enough to vote!")

print("Have you registered to vote yet?")

if age==18:
    print("yr"+" ok")
elif age > 18:
    print("cool!")
else:
    print("not ok")


requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")