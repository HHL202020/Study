print('2.7.2身体质量指数')
weight = float(input('请输入你的体重(单位KG)：\n'))
tall = float(input('请输入你的身高(单位M)：\n'))
BMI = weight/tall**2
print(f'\n你的BMI指数是{BMI}')