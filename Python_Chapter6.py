print('6.0字典')
print('一个简单的字典')
alien_0 = {'color':'green','points':5}
print('\n6.2使用字典')
print('在Python中，字典是一系列键值对。\n'
      '在Python中，字典用放在花括号（{}）中的一系列键值对表示\n'
      '键和值之间用冒号分隔，而键值对之间用逗号分隔。\n')
print('6.2.1　访问字典中的值')
alien_0 = {'color':'green'}
print(alien_0['color'],
      '\n')

alien_0 = {'color':'green','points':5}
new_points = alien_0['points']
print(f'You just earned {new_points} points!\n')

print('6.2.1　访问字典中的值')
alien_0 = {'color':'green','points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0,'\n')

print('6.2.3　先创建一个空字典')
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0,'\n')

print('6.2.4　修改字典中的值')
alien_0 = {'color':'green'}
print(f"The alien is {alien_0['color']}")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original x_position:{alien_0['x_position']}")
# 向右移动外星人
# 根据当前速度确定将外星人向右移动多远
if alien_0['speed'] == 'slow':
      x_increment = 1
elif alien_0['speed'] == 'medium':
      x_increment = 2
else:
      # 这个外星人移动速度一定很快
      x_increment =3
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position:{alien_0['x_position']}\n")

print('6.2.5　删除键值对')
alien_0 = {'color':'green','points':5}
print(alien_0)
# 永久删除哦！
del alien_0['points']
print(alien_0)

print('6.2.6　由类似对象组成的字典')
favorite_languages = {
      'jen':'python',
      'sarah':'c',
      'edward':'rudy',
      'phil':'python'
      }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}\n")

print('6.2.7　使用get()来访问值')
print('如果指定的键不存在就会出错')
alien_0 = {'color':'green','speed':'slow'}
print('使用方法get()在指定的键不存在时返回一个默认值，从而避免这样的错误。\n'
      '方法get()的第一个参数用于指定键，是必不可少的；第二个参数为指定的键不存在时要返回的值，是可选')
point_value = alien_0.get('points','No point value assigned.')
print(point_value,'\n')

print('动手试一试\n'
      '练习6-1：人　\n'
      '使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。\n'
      '该字典应包含键first_name、last_name、age和city。\n'
      '将存储在该字典中的每项信息都打印出来。')
massages = {
      'first_name':'xv',
      'last_name':'xiao',
      'age':'20',
      'city':'WuHan'
}
print(massages['first_name'],
      massages['last_name'],
      massages['age'],
      massages['city'],'\n')

print('练习6-2：喜欢的数　\n'
      '使用一个字典来存储一些人喜欢的数。\n'
      '请想出5个人的名字，并将这些名字用作字典中的键；\n'
      '找出每个人喜欢的一个数，并将这些数作为值存储在字典中。\n'
      '打印每个人的名字和喜欢的数。为了让这个程序更有趣，通过询问朋友确保数据是真实的。')
massages = {'aaaa':1,'bbbb':2,'cccc':3,'dddd':4,'xv':7}

for key in massages:
      print(key.title(),"'s favorite number is",massages[key])

print('\n练习6-3：词汇表　Python字典可用于模拟现实生活中的字典。\n'
      '为避免混淆，我们将后者称为词汇表。\n'
      '▲ 想出你在前面学过的5个编程术语，将其用作词汇表中的键，\n'
      '并将它们的含义作为值存储在词汇表中。\n'
      '▲ 以整洁的方式打印每个术语及其含义。为此，可先打印术语，\n'
      '在它后面加上一个冒号，再打印其含义；也可在一行打印术语，\n'
      '再使用换行符（\\n）插入一个空行，然后在下一行以缩进的方式打印其含义。')
hanghuas = {
      'for':'一种循环',
      'if':'另一种循环',
      'print':'能打印世间万物',
      'get()':'可以避免键不存在是出错',
      'del':'永久删除'
}
for key in hanghuas:
      print(key,':',hanghuas[key])
