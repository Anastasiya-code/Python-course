filetxt = open('les_5-1.txt', 'r', encoding="utf-8")
file1 = filetxt.readline()

print(f"Исходный текст: {file1}")
find_txt = "абв"
lst = [i for i in file1.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')

record = open('result_5-1.txt', 'w')
record.write(" ".join(lst))
record.close()