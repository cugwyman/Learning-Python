database=[
    ['wyman','1111'],
    ['aa'   ,'2222'],
    ['fefe' ,'efef'],
]

username = input('user name:')
pin = input('pin code:')

if[username,pin] in database:print('access granted')
