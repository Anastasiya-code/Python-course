# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

file1txt = open('fileData1.txt', 'r')
file2txt = open('fileData2.txt', 'r')
result = open('result_4-5.txt', 'w')
file1 = file1txt.readline()
file2 = file2txt.readline()
for i in range(len(file1)):
    if file1[i-1] != '^':
        if file1[i].isnumeric():
            result.write(str(int(file1[i])+int(file2[i])))
        else:
            result.write(str(file1[i]))
    else:
        result.write(str(file1[i]))
file1txt.close
file2txt.close
result.close