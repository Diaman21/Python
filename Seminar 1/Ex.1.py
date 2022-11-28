numbers =  input('введите через пробел 5 чисел: ')
numbers = numbers.split(' ') 
print (numbers)
maximum = int (numbers[0])  
for i in numbers:
    i= int (i)
    if maximum < i:
        maximum = i
print (maximum)
