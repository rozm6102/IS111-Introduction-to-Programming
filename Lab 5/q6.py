
# Put your code below
######################

# Part a) 
def get_all_combinations(str_list, num_list): 
        list_of_combinations = []
        for x in str_list: 
            for y in num_list: 
                list_of_combinations.append((x,y))
        return list_of_combinations

# Part b) 
def get_larger_numbers(num_list1, num_list2): 
    larger_numbers_list = []
    for x in num_list1:
        test_count = 0
        for y in num_list2: 
            if x > y: 
                test_count += 1 
        if test_count == len(num_list2): 
            larger_numbers_list.append(x)
    return larger_numbers_list

# Part c) 
def get_non_common_strings(str_list1, str_list2): 
    non_common_strings_list = []
    
    for x in str_list1: 
        is_identical = "False" 
        for y in str_list2: 
            if x == y:
                is_identical = "True" 
        if is_identical == "False": 
            non_common_strings_list.append(x) 

    for y in str_list2: 
        is_identical = "False" 
        for x in str_list1: 
            if y == x:
                is_identical = "True" 
        if is_identical == "False":
                non_common_strings_list.append(y)
    
    return non_common_strings_list


# Test Cases to test your code
##############################

r_list = get_all_combinations(["a", "b"], [1, 2, 3])
print("Expected: [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3)]")
print("Actual  : " + str(r_list))
print()

r_list = get_larger_numbers([4, 6, 10], [1, 3, 5])
print("Expected: [6, 10]")
print("Actual  : " + str(r_list))
print()

r_list = get_non_common_strings(["a", "b", "c", "d"], ["b", "d", "e", "f"])
print("Expected: ['a', 'c', 'e', 'f']")
print("Actual  : " + str(r_list))
print()