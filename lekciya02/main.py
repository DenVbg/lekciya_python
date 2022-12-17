# 1 вариант перезапись
# with open('file.txt', 'w') as data:
#  data.write('line 1\n')
#  data.write('line 2\n')


# 2 вариант дозапись
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.close()
# exit()

# 3 вариант чтение
path = 'file.txt'
data = open(path, 'r')
for line in data:
 print(line)
data.close()