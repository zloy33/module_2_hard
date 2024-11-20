print("code: ")
import random # библиотека( генератор случайных чисел)
def Jungle():
    list_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] # список для генерации чисел
    number_ = random.choice(list_) # выбор числа
    return number_ # возращение значения переменной

number_ = Jungle()
print (number_ )

print("result: ")
x = number_

for i in range(1,21):
    for j in range(i+1, x):
        if x % (i+j) == 0 or (i+j) % x == 0:
            print(i, j, sep="", end="")