# Task 5
# Develop a function that takes a list of integers (by idea not in fact)
# as an argument and returns list of top-three max integers.
# If passed list contains not just integers collect them
# and print the following error message: You've passed some extra elements that I can't parse: [<"elem1", "elem2" .... >]. If return value will have less than 3 elements for some reason it's ok and shouldn't cause any problem, but some list should be returned in any case.

def print_max_3_integers(integers):
    error_list = [x for x in integers if not str(x).isdigit()]

    if not len(error_list) == 0:
        raise ValueError("You've passed some extra elements that I can't parse: {}. If return value will have less than 3 elements for some reason it's ok and shouldn't cause any problem, but some list should be returned in any case".format(error_list))


    first = max(integers)
    second = max([x for x in integers if x != first])
    third = max([x for x in integers if x != first and x != second])
    return [first, second, third]

print(print_max_3_integers([1, 2, 3, 4, 51]))
