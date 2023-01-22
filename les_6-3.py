listNames = {}
amount = int(input("Введите число N: "))
for i in range(amount):
    name = input("Имя: ")
    age = int(input("Возраст: "))
    listNames[name] = age

min_value = min(listNames.values())
for name, am in listNames.items():
    if am == min_value:
        print("Самый младший: " + name)