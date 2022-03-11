# Task 1
# Self-study input() function.
# Write a script which accepts a sequence of comma-separated numbers from user and generate
# a list and a tuple with those numbers and prints these objects as-is (just print(list)
# without any formatting).

result_list = input("Enter a comma-separated list: ").replace(" ", "").split(",")
print(result_list)
print(tuple(result_list))