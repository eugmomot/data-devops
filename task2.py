# Task 2
# Develop a procedure to print all even numbers from a numbers list
# which is given as an argument. Keep the original order of numbers
# in list and stop printing if a number 254 was met. Don't forget to add
# a check of the passed argument type.

result_list = list(input("Enter a numbers list: ").split(" "))

for n in result_list:
    i = int(n)
    if i == 254:
        break
    if i % 2 == 0:
        print(i)
