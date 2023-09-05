# 1.列表
abc = ['1','2','3','4','5']     # 在Python中，用方括号（[]）表示列表

# 2.打印列表
print(abc)      # 显示：['1', '2', '3', '4', '5']  是有[]的

# 3.访问列表，这里假如访问3号元素
print(abc[2],'\n')   # 显示：4      索引从0而不是1开始

# 4.Python为访问最后一个列表元素提供了一种特殊语法
print(abc[-1])  # [-1]访问最后一个列表元素，即[]中的负数为倒叙
print(abc[-2])
print(abc[-3],'\n')

# 4.使用列表中的各个值
message = f'我们有{abc[-1]}根手指头和{abc[1]}只眼睛'
print(message,'\n')

# 练习3-1：姓名　将一些朋友的姓名存储在一个列表中，并将其命名为names。依次访问该列表中的每个元素，从而将每个朋友的姓名打印出来。
friend = ['徐','张','祁','叶','陈']
print(friend[0],'\n',
      friend[1],'\n',
      friend[2],'\n',
      friend[3],'\n',
      friend[4],'\n')

# 练习3-2：问候语　继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
nei = '你好啊!'
hua = f'{friend[0]}'
print(hua+nei)
hua = f'{friend[1]}'
print(hua+nei)
hua = f'{friend[2]}'
print(hua+nei)
hua = f'{friend[3]}'
print(hua+nei)
hua = f'{friend[4]}'
print(hua+nei,"\n")

# 练习3-3：自己的列表　想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，下面是一个例子。
way = ['共享单车','出租车','公交车','高铁','飞机']
print('从学校回家我会乘'+way[3],'\n')

print('5.修改、添加和删除元素')
motorcycles = ['Honda','Yamaha','Suzuki']
print(motorcycles)
motorcycles[0] = 'Ducati'
print(motorcycles,'\n')

print('6.在列表中添加元素')
motorcycles = ['Honda','Yamaha','Suzuki']
print(motorcycles)
motorcycles.append('Ducati')     # .append给列表附加元素时，它将添加到列表末尾
print(motorcycles,'\n')

print('7.在列表中插入元素')
motorcycles = ['Honda','Yamaha','Suzuki']
print(motorcycles)
motorcycles.insert(0,'Ducati')      # 使用方法insert()可在列表的任何位置添加新元素
print(motorcycles,'\n')

print('8.从列表中删除元素')
motorcycles = ['Honda','Yamaha','Suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles,'\n')

print('9.使用方法pop()删除元素')
motorcycles = ['Honda','Yamaha','Suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()     # 需要理解弹出列表并使用的概念
print(motorcycles)
print(popped_motorcycle)

popped_motorcycle = motorcycles.pop(0)    # .pop()括号内可选择弹出的值
print(popped_motorcycle,'\n')

print('10.根据值删除元素')
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')              # 如果只知道要删除的元素的值，可使用方法remove()
print(motorcycles,'\n')

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'我买不起{too_expensive},因为它太贵了！\n')

print('练习3-4：嘉宾名单　如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？请创建一个列表，其中包含至少三个你想邀请的人，然后使用这个列表打印消息，邀请这些人来与你共进晚餐')
customer = ['爷爷','爸爸','妈妈']
print(f'我想邀请{customer}一起共度晚餐。')
message = '，晚上一起吃饭吧！'
print(f'{customer[0]}{message}')
print(f'{customer[1]}{message}')
print(f'{customer[2]}{message}\n')

print('练习3-5：修改嘉宾名单　你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。\n'
      '▲ 以完成练习3-4时编写的程序为基础，在程序末尾添加一条print语句，指出哪位嘉宾无法赴约。\n'
      '▲ 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。\n'
      '▲ 再次打印一系列消息，向名单中的每位嘉宾发出邀请\n')
print('妈妈临时有事儿不能来了')
lost_customer = '妈妈'
customer.remove(lost_customer)
print(f'今晚只能和{customer}一起用餐了\n')

print('练习3-6：添加嘉宾　你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。'
      '▲ 以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print语句，指出你找到了一个更大的餐桌。\n'
      '▲ 使用insert()将一位新嘉宾添加到名单开头。\n'
      '▲ 使用insert()将另一位新嘉宾添加到名单中间。\n'
      '▲ 使用append()将最后一位新嘉宾添加到名单末尾。\n'
      '▲ 打印一系列消息，向名单中的每位嘉宾发出邀请。\n')
print('我找到了一个更大的餐桌！！我要再邀请三个人！！')
new_customer = ['奶奶','哥哥','姐姐']
print(f'这是之前的清单{customer}')
customer.insert(0,{new_customer[0]})
customer.insert(2,{new_customer[1]})
customer.append({new_customer[2]})
print(f'更新后的的清单是{customer}\n')

print('练习3-7：缩减名单　你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。'
      '▲ 以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。'
      '▲ 使用pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。'
      '▲ 对于余下两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。'
      '▲ 使用del将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。')
print('真见鬼，新找到的桌子长腿跑了，所以只能和两个人共度晚餐了...')
out_customer = ['哥哥','奶奶','姐姐']
customer.remove({out_customer[0]})
print(f'{out_customer[0]},对不起下次请你吃饭')
customer.remove({out_customer[1]})
print(f'{out_customer[1]},对不起下次请你吃饭')
customer.remove({out_customer[2]})
print(f'{out_customer[2]},对不起下次请你吃饭\n')
print(f'{customer[0]},我们还是照常吃饭哈')
print(f'{customer[1]},我们还是照常吃饭哈')

print('晚饭结束了...')
del customer[1]
print(customer)
del customer[2]
print(customer)


