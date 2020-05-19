import random
age = random.randint(1,50)
guess = 0
i = 1
while i<=3:
    print('第%s次机会输入：'%i)
    guess = int(input())
    if guess==age:
        print('答对了')
    i+=1
    if i>3:
        choice = input('是否继续：(输入y or n)')
        if choice is 'y':
            i = 1
        else:
            print('结束了')
print("答案是：%s"%age)            



