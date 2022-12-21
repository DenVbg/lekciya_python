# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

print("Программа, которая принимает на вход вещественное число и показывает сумму его цифр")
number = str(abs(float(input("Введите число: "))))
my_sum = 0
value = number.split('.')
for i in range(0,len(value[0])):
    my_sum += int(value[0][i])
if value[1]: 
    for i in range(0,len(value[1])):
        my_sum += int(value[1][i])
print(my_sum)

