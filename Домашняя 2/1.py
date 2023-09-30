x = input("Введите вводит числа, буквы или оставте поле пустым: ")
list = []
while x != "":
    list.append(x) 
    x = input("")
print("Итоговый список", list)