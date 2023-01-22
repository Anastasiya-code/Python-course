from statistics import mean
listNames = {}
amount = int(input("Введите число N: "))

for i in range(amount):
    name = input("Имя: ")
    age = int(input("Возраст: "))
    listNames[name] = age

print(mean(listNames.values()))
print(max(listNames.keys(), key=len))

