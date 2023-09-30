numbers = input("Введите список чисел через запятую: ").split(",")
numbers = [int(num) for num in numbers]
numbers.sort(reverse=True, key=lambda x: str(x))
result = "".join(str(num) for num in numbers)
print("Максимально возможное число:", result)