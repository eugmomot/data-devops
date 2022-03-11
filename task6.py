# Task 6
# Create a function that will take a string as an argument and return
# a dictionary where keys are symbols from the string and values are the count of inclusion of that symbol.

def char_counts(str):
    dic = dict()
    for w in str:
        if w in dic.keys():
            dic[w] = dic[w] + 1
        else:
            dic[w] = 1
    return dic

print(char_counts("aaabbccccddddddd"))