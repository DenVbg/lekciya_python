# 3. Напишите программу, которая определит позицию второго
# вхождения строки в списке либо сообщит, что её нет.
#
# *Пример:*
#
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

#text = ["qwe", "asd", "zxc", "qwe", "ertqwe"] # ищем: "qwe", ответ: 3
#search = "qwe"
text = ["йцу", "фыв", "ячс", "цук", "йцукен"] #, ищем: "йцу", ответ: -1
search = "йцу"
position = 2
def find_text(text, position):
    count = 0
    for i in range(len(text)):
        if search in text[i]:
            count += 1
            if count == position:
                return i
                break
    else:
        return -1

response = find_text(text, position)
print (f"Ответ: {response}")