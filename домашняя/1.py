#Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке.
# Последовательность завершается числом 0, при считывании которого программа должна закончить свою работу
# и вывести количество членов последовательности (не считая завершающего числа 0). Числа, следующие за числом 0,
# считывать не нужно.
x=0
while int(input()) !=0:
    x=x+1
print(x)