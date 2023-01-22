listFruit = {}
amount = int(input("Введите количество: "))
for i in range(amount):
    name = input("Наименование фрукта: ")
    amountFruit = int(input("Количество: "))
    listFruit[name] = amountFruit
print(listFruit)