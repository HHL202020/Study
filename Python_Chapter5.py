print('第 5 章　if语句')
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title(),)
print('\n')

print('5.2.1　检查是否相等')
car = 'bmw'
print(car == 'audi','\n')

print('5.2.2　检查是否相等时忽略大小写')
car = 'Audi'
print(car == 'audi','\n')

print('函数lower()不会修改最初赋给变量car的值')
car = 'Audi'
print(car.lower() == 'audi')

print('5.2.3　检查是否不相等')
requested_topping = 'mushrooms'
if requested_topping != 'mushrooms':
    print('Hold the anchovies!')

print('5.2.4　数值比较')
age = 18
print(age == 18,'\n')

answer = 17
if answer != 41:
    print('That is not the correct answer.Please try again!\n')

age = 19
print(age < 21,'\n')

print(age <= 21,'\n')

print(age > 21,'\n')

print(age >= 21,'\n')

print('5.2.5　检查多个条件')
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21,'\n')

print('使用or检查多个条件')
age_0 = 22
age_1 = 18
print((age_0 >= 21) or (age_1 >= 21),'\n')

age_0 = 18
print((age_0 >= 21) or (age_1 >= 21),'\n')

print('5.2.6　检查特定值是否包含在列表中')
requested_topping = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_topping,'\n')

print('pepperoni' in requested_topping,'\n')

print('5.2.7　检查特定值是否不包含在列表中')
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(f'{user.title()},you can post a response if you wish.\n')

print('5.2.8　布尔表达式\n')
game_active = True
can_edit = False

print('练习5-1：条件测试　编写一系列条件测试，将每个测试以及对其结果的预测和实际结果打印出来。\n'
      '你编写的代码应类似于下面这样：')
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print('练习5-2：更多条件测试　你并非只能创建10个测试。\n'
      '如果想尝试做更多比较，可再编写一些测试，并将它们加入conditional_tests.py中。\n'
      '对于下面列出的各种情况，至少编写两个结果分别为True和False的测试。\n'
      '▲ 检查两个字符串相等和不等。▲ 使用方法lower()的测试。\n'
      '▲ 涉及相等、不等、大于、小于、大于等于和小于等于的数值测试。\n'
      '▲ 使用关键字and和or的测试。\n'
      '▲ 测试特定的值是否包含在列表中。\n'
      '▲ 测试特定的值是否未包含在列表中。\n')

print('1')
hairs = ['red','yollow','black']
for hair in hairs:
    if hair == 'black':
        print('Is my baby!\n')

print('2')
car = 'Benz'
if car.lower() == 'benz':
    print('Is Benz')

print('3')
motherlands = ['zhongguo','meiguo','eluosi']
for motherland in motherlands:
    if motherland == 'zhongguo':
        print(f'{motherland.upper()} is my motherland!')
    else:
        print(f'{motherland.title()} Is not my motherland.')
print('')

print('4')
friends = ['wang','qi','ye','tong','lun']
for friend in friends:
    if friend != 'lun':
        print(f'{friend} is my friend!')
print('')

print('5')
age_3 = 18
age_4 = 19
if (age_3 >= 18) and (age_4 >= 18):
    print('Pass!\n')

print('6')
thing = [123,321,456,654,777]
if 777 in thing:
    print('Pass!\n')

print('7')
badlist = ['ni','ta','Ta']
if badlist != 'wo':
    print('Yes!!!')

print('5.3.1简单的if语句')
age = 19
if age >=18:
    print('You are old enough to vote!\n')

print('5.3.2 if-else语句')
age = 17
if age >=18:
    print('You are old enough to vote!')
else:
    print('Sorry,you are too young to vote.\n')

print('5.3.3 if-elif-else结构')
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
print('')

print('更简洁的版本：')
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f'Your admission cost is ${price}.')

print('5.3.4　使用多个elif代码块')
age = 13
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 20
print(f'Your admission cost is ${price}.\n')

print('5.3.5　省略else代码块\n'
      '在有些情况下，else代码块很有用；而在其他一些情况下，使用一条elif语句来处理特定的情形更清晰：\n'
      'else是一条包罗万象的语句，只要不满足任何if或elif中的条件测试，其中的代码就会执行。')
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")

print('5.3.6测试多个条件')
requested_toppings = ['mushroom','extra cheese']
if 'mushroom' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')
print('\nFinished making your pizaa!')

print("练习5-3：外星人颜色　假设在游戏中刚射杀了一个外星人，\n"
      "请创建一个名为alien_color的变量，并将其赋值为'green'、'yellow'或'red'。\n"
      "▲ 编写一条if语句，检查外星人是否是绿色的。如果是，就打印一条消息，指出玩家获得了5分\n"
      "▲ 编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）。")
alien_color = ['green','yellow','red']
for color in alien_color:
    if color == 'green':
        print('You got 1 point!')

print('练习5-4：外星人颜色2　像练习5-3那样设置外星人的颜色，并编写一个if-else结构。\n'
      '▲ 如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5分。\n'
      '▲ 如果外星人不是绿色的，就打印一条消息，指出玩家获得了10分。\n'
      '▲ 编写这个程序的两个版本，在一个版本中执行if代码块，在另一个版本中执行else代码块。')
alien_color = ['green','yellow','red']
for color in alien_color:
    if color == 'green':
        point = 5
    if color != 'green':
        point = 10
print(f'You got {print}.')

print('另一个版本')
alien_color = ['green','yellow','red']
if 'green' in alien_color:
    price = 5
else:
    price = 10
print(f'You got {price}')

print('练习5-5：外星人颜色3　将练习5-4中的if-else结构改为if-elif-else结构。\n'
      '▲ 如果外星人是绿色的，就打印一条消息，指出玩家获得了5分。\n'
      '▲ 如果外星人是黄色的，就打印一条消息，指出玩家获得了10分。\n'
      '▲ 如果外星人是红色的，就打印一条消息，指出玩家获得了15分。\n'
      '▲ 编写这个程序的三个版本，分别在外星人为绿色、黄色和红色时打印一条消息。')
alien_color = ['green','yellow','red']
if 'green' in alien_color:
    price = 5
elif 'yellow' in alien_color:
    price = 10
else:
    price = 10
print(f'You got {price}.\n')

alien_color = ['green','yellow','red']
if 'green' in alien_color:
    print('The player got 5 points.')
if 'yellow' in alien_color:
    print('The player got 10 points.')
if 'red' in alien_color:
    print('The player got 15 points.')

print('练习5-6：人生的不同阶段　设置变量age的值，再编写一个if-elif-else结构，\n'
      '根据age的值判断一个人处于人生的哪个阶段。\n'
      '▲ 如果年龄小于2岁，就打印一条消息，指出这个人是婴儿。\n'
      '▲ 如果年龄为2（含）～4岁，就打印一条消息，指出这个人是幼儿。\n'
      '▲ 如果年龄为4（含）～13岁，就打印一条消息，指出这个人是儿童。\n'
      '▲ 如果年龄为13（含）～20岁，就打印一条消息，指出这个人是青少年。\n'
      '▲ 如果年龄为20（含）～65岁，就打印一条消息，指出这个人是成年人。\n'
      '▲ 如果年龄超过65岁（含），就打印一条消息，指出这个人是老年人。')
age = int(input('请输入您的年龄：\n'))
if age < 2 :
    print('这个人是一个婴儿。')
elif age <= 4 :
    print('这个人是一个幼儿。')
elif age <= 13:
    print('这个人是一个儿童。')
elif age <= 20:
    print('这个人是一个青少年。')
elif age <= 65:
    print('这个人是一个成年人。')
elif age >65:
    print('这个人是一个老年人。')
print('')

print('练习5-7：喜欢的水果　创建一个列表，其中包含你喜欢的水果，再编写一系列独立的if语句，\n'
      '检查列表中是否包含特定的水果。\n'
      '▲ 将该列表命名为favorite_fruits，并在其中包含三种水果。\n'
      '编写5条if语句，每条都检查某种水果是否包含在列表中。如果是，就打印一条消息，下面是一个例子。')
favorite_fruits = ['apple','banana','watermelon']
if 'apple' in favorite_fruits:
    print('apple is my favorite fruit.')
if 'banana' in favorite_fruits:
    print('banana is my favorite fruit.')
if 'watermelon' in favorite_fruits:
    print('watermelon is my favorite fruit.')

print('5.4　使用if语句处理列表')
print('5.4.1　检查特殊元素')

