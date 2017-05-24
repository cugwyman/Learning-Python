'''name=''
while not name :
    name=input('please enter your name:')

print('hello,%s!'%name)'''

'''for number in range(1,1001):
    print (number)'''

while True:   #T必须大写  其实就是while（1）死循环
    word = input('please enter a word:')
    if not word: break

    print('the word was ' + word)

