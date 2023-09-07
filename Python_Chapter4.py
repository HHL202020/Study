print('第四章 操作列表')
print('4.1.2　深入研究循环')
name =['zhang','li','wang']
for name in name:
    print(f'{name} 你的表演太精彩了！！')
    print(f'很期待你下一次的表演{name}\n')
print('非常感谢你们的表演！！\n')
print('练习4-1：比萨　想出至少三种你喜欢的比萨，将其名称存储在一个列表中，再使用for循环将每种比萨的名称打印出来。\n'
      '修改这个for循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。\n'
      '对于每种比萨，都显示一行输出。')
taste = ['番茄味','榴莲味','叉烧味']
for taste in taste:
    print(f'我喜欢吃{taste}的披萨')
    print(f'真的很喜欢吃{taste}的披萨')

print('练习4-2：动物　想出至少三种有共同特征的动物，将其名称存储在一个列表中，再使用for循环将每种动物的名称打印出来。\n'
      '修改这个程序，使其针对每种动物都打印一个句子。\n'
      '在程序末尾添加一行代码，指出这些动物的共同之处，如打印下面这样的句子')
animal =['熊','猫','狗']
for animal in animal:
    print(f'我喜欢{animal}')
print('他们都是长着毛毛和四条腿的动物！')

print('4.3.1　使用函数range()')
for value in range(1,5):
    print(value,'\n')

print('list()函数将range()的结果直接转换为列表')
numbers = list(range(1,6))
print(numbers,'\n')

print('range()函数的指定步长')
numbers = list(range(2,11,2))
print(numbers,'\n')

print('例如，如何创建一个列表，其中包含前10个整数（1～10）的平方呢？在Python中，用两个星号（**）表示乘方运算')
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)
print('==================上题第二种解决方案=====================================================')
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

print('4.3.3　digits()对数字列表执行简单的统计计算')
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

print('4.3.4　列表解析')
squares = [value**2 for value in range(1,11)]
print(squares)

print('练习4-3：数到20　使用一个for循环打印数1～20（含）。')
print('第一种方法')
squares =[]
for value in range(1,21):
    squares.append(value)
print(squares)

print('第二种方法')
squares = [value for value in range(1,21) ]
print(squares)

print('练习4-4：一百万　创建一个包含数1～1 000 000的列表，再使用一个for循环将这些数打印出来。\n'
      '（如果输出的时间太长，按Ctrl + C停止输出或关闭输出窗口。）')
'''
monry = [value for value in range(1,1000001)]
print(monry)
'''

print('练习4-5：一百万求和　创建一个包含数1～1 000000的列表，再使用min()和max()核实该列表确实是从1开始、到1 000 000结束的。\n'
      '另外，对这个列表调用函数sum()，看看Python将一百万个数相加需要多长时间。')
monry = [value for value in range(1,1000001)]
print(min(monry))
print(max(monry))
print(sum(monry))

print('练习4-6：奇数　通过给函数range()指定第三个参数来创建一个列表，其中包含1～20的奇数，再使用一个for循环将这些数打印出来。')
print('第一种方法')
squares =[value for value in range(1,21,2)]
print(squares,)
print('第二种方法')
squares = []
for value in range(1,21):
    squares.append(value)
print(squares,'\n')

print('练习4-8：立方　将同一个数乘三次称为立方。例如，在Python中，2的立方用2**3表示.\n'
      '请创建一个列表，其中包含前10个整数（1～10）的立方，再使用一个for循环将这些立方数打印出来')
print('第一种方法')
squares = [value**3 for value in range(1,11)]
print(squares)
print('第二种方法')
squares = []
for value in range(1,11):
    squares.append(value**3)
print(squares,'\n')

print('练习4-9：立方解析　使用列表解析生成一个列表，其中包含前10个整数的立方。')
squares = [value**3 for value in range(1,11)]
print(squares)

print('4.4.2　遍历切片')
players = ['charles','martina','michael','florence','eli']
print('我们的队伍中前三位球员是：')
for player in players[:3]:
    print(player.title())

print('4.4.3　复制列表')
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print(f'我最喜欢的食物是：\n{my_foods}')
print(f'我的朋友最喜欢的食物是：\n{friend_foods}')
my_foods.append('cannoil')
friend_foods.append('ice cream')
print(f'现在我最喜欢的食物是：\n{my_foods}')
print(f'现在我的朋友最喜欢的食物是：\n{friend_foods}')

print('练习4-10：切片　选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。\n'
      '▲ 打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。\n'
      '▲ 打印消息“Three items from the middle of the list are:”，再使用切片来打印列表的中间三个元素。\n'
      '▲ 打印消息“The last three items in the list are:”，再使用切片来打印列表的末尾三个元素。')
players = ['charles','martina','michael','florence','eli']
print('The first three items in the list are:')
for player in players[:3]:
    print(player,)

print('Three items from the middle of the list are:')
for player in players[1:4]:
    print(player)

print('The last three items in the list are:')
for player in players[-3:]:                     # 注意-3的位置！在:前面
    print(player)

print('练习4-11：你的比萨，我的比萨　在你为完成练习4-1而编写的程序中，创建比萨列表的副本，'
      '并将其赋给变量friend_pizzas，再完成如下任务。'
      '▲ 在原来的比萨列表中添加一种比萨。'
      '▲ 在列表friend_pizzas中添加另一种比萨。'
      '▲ 核实有两个不同的列表。为此，打印消息“My favorite pizzas are:”，'
      "再使用一个for循环来打印第一个列表；打印消息“My friend's favorite pizzas are:”，"
      '再使用一个for循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。')
my_pizza = ['one','two','three']
friend_pizza = my_pizza[:]
print(f'我的口味数量{my_pizza}')
print(f'朋友的口味数量{friend_pizza}\n')

my_pizza.append('four')
print(f'现在我的口味数量{my_pizza}')
print(f'现在朋友的口味数量{friend_pizza}\n')

friend_pizza.append('five')
print(f'现在2我的口味数量{my_pizza}')
print(f'现在2朋友的口味数量{friend_pizza}\n')

print("My friend's favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza,)

print('\n')
for pizza in my_pizza:
    print(pizza)

print('练习4-12：使用多个循环　在本节中，为节省篇幅，程序foods.py的每个版本都没有使用for循环来打印列表。\n'
      '请选择一个版本的foods.py，在其中编写两个for循环，将各个食品列表打印出来。')
my_foods = ['pizza','falafel','carrot cake']
for food in my_foods:
    print(food)

print('4.5.1　定义元组')
dimensions = (200,50)               # 注意！！是（）不是[]
print(dimensions[0])
print(dimensions[1])

print('注意　严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰。\n'
      '如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号：')            # !!一个元素

print('4.5.2　遍历元组中的所有值')
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

print('4.5.3　修改元组变量')
dimensions = (200,50)
print('原始元组：')
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print('现在元组：')
for dimension in dimensions:
    print(dimension)

print('练习4-13：自助餐　有一家自助式餐馆，只提供五种简单的食品。请想出五种简单的食品，并将其存储在一个元组中.\n'
      '▲ 使用一个for循环将该餐馆提供的五种食品都打印出来。▲ 尝试修改其中的一个元素，核实Python确实会拒绝你这样做。\n'
      '▲ 餐馆调整了菜单，替换了它提供的其中两种食品。请编写一个这样的代码块：给元组变量赋值，\n'
      '  并使用一个for循环将新元组的每个元素都打印出来。')
foods = ('番茄炒鸡蛋','青椒肉丝','红烧排骨','韭菜鸡蛋','鱼香肉丝')
print('这家餐馆有：')
for food in foods:
    print(food)

#  foods [0] ='丝瓜炒鸡蛋'
print('\n修改之后的菜单：')
foods = ('油闷大虾','酸菜鱼','红烧排骨','韭菜鸡蛋','鱼香肉丝')
for food in foods:
    print(food)

print('4.6.1　格式设置指南\n'
      '要提出Python语言修改建议，需要编写Python改进提案（Python Enhancement Proposal，PEP）。\n'
      'PEP 8是最古老的PEP之一，向Python程序员提供了代码格式设置指南。\n'
      ''
      '4.6.2　缩进\n'
      'PEP 8建议每级缩进都使用四个空格。这既可提高可读性，又留下了足够的多级缩进空间。\n'
      ''
      '4.6.3　行长\n'
      '很多Python程序员建议每行不超过80字符。\n'
      'PEP 8还建议注释的行长不应超过72字符，因为有些工具为大型项目自动生成文档时，会在每行注释开头添加格式化字符.\n'
      ''
      '4.6.4　空行\n'
      '要将程序的不同部分分开，可使用空行\n'
      '')
