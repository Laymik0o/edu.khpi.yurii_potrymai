import random
import ListProcessing


def get_int_array_console():
    size = int(input("Enter size of an array: "))
    array = []
    for i in range(size):
        array.append(int(input("Enter %d number: " % i)))
    return array


def get_int_array_random():
    size = int(input("Enter size of an array: "))
    max_num = int(input("Enter high bound for random generator: "))
    array = [random.randint(0, max_num) for i in range(size)]
    return array


def sort():
    print("Sorting")
    given_list = get_int_array_random()
    print("Given list: ", given_list)
    sorted_list = ListProcessing.quick_sort(given_list)
    print("Sorted list: ", sorted_list)


def get_element_index():
    print("Get element index by value")
    given_list = get_int_array_console()
    val = int(input("Enter value to search: "))
    index = ListProcessing.find_elem_by_value(given_list, val)
    print("Index of given element: ", index)


def get_sequence_index():
    print("Find subsequence")
    given_list = get_int_array_console()
    print("Enter sequence to search:")
    sequence = get_int_array_console()
    sequence_index = ListProcessing.find_sequence(given_list, sequence)
    print("Sequence starts at ", sequence_index)


def get_first_mins():
    print("Get minimums")
    given_list = get_int_array_random()
    print("Given list: ", given_list)
    amount = 5
    mins = ListProcessing.find_first_min(given_list, amount)
    print("First minimums: ", mins)


def get_first_maximums():
    print("Get maximums")
    given_list = get_int_array_random()
    print("Given list: ", given_list)
    amount = 5
    maximums = ListProcessing.find_first_max(given_list, amount)
    print("First maximums: ", maximums)


def get_average():
    print("Calculate average")
    given_list = get_int_array_random()
    print("Given list: ", given_list)
    average = ListProcessing.find_average(given_list)
    print('Average: ', average)


def get_distinct_list():
    print("Removing duplicates")
    given_list = get_int_array_console()
    distinct_list = ListProcessing.remove_duplicates(given_list)
    print("List without duplicates: ", distinct_list)


def get_function(number):
    functions = {
        1: sort,
        2: get_element_index,
        3: get_sequence_index,
        4: get_first_mins,
        5: get_first_maximums,
        6: get_average,
        7: get_distinct_list
    }
    return functions[number]()


def start():
    function_number = int(input("Choose number of function to execute:\n" +
                                "1 - Quick sort of list\n" +
                                "2 - Get list element by it's value\n" +
                                "3 - Find subsequence in list\n" +
                                "4 - Get first 5 minimum elements\n" +
                                "5 - Get first 5 maximum elements\n" +
                                "6 - Get average of list elements\n" +
                                "7 - Remove duplicates from list\n"))
    try:
        get_function(function_number)
    except KeyError:
        print("You entered something wrong")


if __name__ == "__main__":
    start()
