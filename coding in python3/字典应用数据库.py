#字典示例
#简单数据库
#人名作为键的字典，每人用另一字典表示

people={
    
    'wyman':{
        'phone':'1111',
        'addr':'bb street'
    },
    'jacky':{
        'phone':'2222',
        'addr':'kk street'
    },
    'bitch':{
        'phone':'2333',
        'addr':'bb blocks'
    }
}
#描述标签
labels = {
    'phone':'phone number',
    'addr':'address'
}

name = input('name:')
request = input('phone number(p) or address(a)?')

if request == 'p':key='phone'
if request == 'a':key='addr'

person = people.get(name,{})
label  = labels.get(key,key)
result = person.get(key,'not available')
#if name in people:print("%s's %s is %s."% (name,labels[key],people[name][key]))
print("%s's %s is %s."% (name,label,result))
