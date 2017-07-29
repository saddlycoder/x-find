import sys
import random
global a
global x
global y
global z

memory = []

x = 100  # 1
y = 0  # 2

z = '+'  #

a = 228  #


def objectInMemory(x):
    if(int(x) in memory):
        return True
    else:
        return False

def getTrueInt():
	return random.randrange(0, 300)
			
def getTrueAnswer():
    while y == 0:
        r = 0
        r = getTrueInt()
        print(r)
        if(z == '+'):
            if(objectInMemory(r) == True):
                r = int(getTrueInt())
            a_1 = x + r
            if(a_1 != a):
                memory.append(r)
            elif(a_1 == a):
                print('Answer: ', r)
                break
        if(z == '-'):
            if(objectInMemory(r) == True):
                r = int(getTrueInt())
            a_1 = x - r
            print(a_1)
            if(a_1 != a):
                memory.append(r)
            elif(a_1 == a):
                print('Answer: ', r)
                break
        if(z == '*'):
            if(objectInMemory(r) == True):
                r = int(getTrueInt())
            a_1 = x * r
            if(a_1 != a):
                memory.append(r)
            elif(a_1 == a):
                print('Answer: ', r)
                break

        if(z == '/'):
            if(objectInMemory(r) == True):
                r = int(getTrueInt())
            try:
                a_1 = x / r
            except (TypeError, ZeroDivisionError) as err:
                pass
            if(a_1 != a):
                memory.append(r)
            elif(a_1 == a):
                print('Answer: ', r)
                break
getTrueAnswer()