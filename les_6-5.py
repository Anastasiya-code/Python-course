resultList = {}
amount = int(input("Введите количество слов: "))

for i in range(amount):
    listData = input("Введите слово и значение: ")
    splitList = listData.split(' - ')
    valueList = splitList[1].split(',')
    resultList[splitList[0]] = valueList

print(resultList)