#根据年月日打印出日期
months=[
    'january',
    'february',
    'march',
    'april',
    'may',
    'june',
    'july',
    'august',
    'september',
    'october',
    'november',
    'december'
    ]
#以1-31的数字作结尾的列表
endings =['st','nd','rd']+17*['th']\
          +['st','nd','rd']+7*['th']\
          +['st']
year =input('year:')
month=input('month(1-12):')
day  =input('day(1-31)')

month_number = int(month)
day_number   = int(day)

#序列从0开始，所以月份、天数减1
month_name = months[month_number-1]
ordinal=day+endings[day_number-1]

print (month_name +' '+ordinal + '.'+year)

