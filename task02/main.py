#Напишите программу, которая на вход принимает 5 чисел и находит максимамальное
#1,4,8,7,5 - 8
#78, 55, 36, 90, 2 - 90

# num1 = int(input("num1 = "))
# num2 = int(input("num2 = "))
# num3 = int(input("num3 = "))
# num4 = int(input("num4 = "))
# num5 = int(input("num5 = "))
#
# if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
#     print(f"max = {num1}")
# elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
#     print(f"max = {num2}")
# elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
#     print(f"max = {num3}")
# elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
#     print(f"max = {num4}")
# else :
#     print(f"max = {num5}")



# numbers = [1,4,8,7,5]
# numbers = [78, 55, 36, 90, 2]
# my_max = 0
# for i in numbers:
#     if my_max < i:
#         my_max = i
# print(f"max = {my_max}")

numbers = []
for i in range(5):
        numbers.append(int(input("введите число: ")))
print(numbers)

my_max = 0
for i in numbers:
    if my_max < i:
        my_max = i
print(f"max = {my_max}")

my_max = numbers[0]
for i in range(1, len(numbers)):
    if my_max < numbers[i]:
        my_max = numbers[i]
print(f"max = {my_max}")