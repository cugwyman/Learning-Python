#使用给定宽度打印格式化后的价格列表

width = input('please enter width:')

price_width = 10
item_width = width - price_width

header_format ='%-*s%*s'
format        ='%-*s%*.2f'

print('='*width)

print (header_format %(item_width,'apples',price_width)
