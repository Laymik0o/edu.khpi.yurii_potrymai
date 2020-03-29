def quick_sort(input_list):
    """
    * Realize quick sort of a list

    * Params:
        * input_list ('list'): List to be sorted

    * Return:
        * ('list'): Sorted list
    """

    left_part = []
    right_part = []
    medium_part = []

    if len(input_list) <= 1:
        return input_list
    else:
        base_elem = input_list[(0 + len(input_list)) // 2]
        for elem in input_list:
            if elem < base_elem:
                left_part.append(elem)
            elif elem > base_elem:
                right_part.append(elem)
            else:
                medium_part.append(elem)
    sorted_right = quick_sort(right_part)
    sorted_left = quick_sort(left_part)
    return sorted_left + medium_part + sorted_right


def find_elem_by_value(input_list, value):
    """
    * Finds element of list by it's value

    * Params:
        * input_list ('list'): list for searching

    * Return:
        * ('int'): index of founded element
    """
    return input_list.index(value)


def find_sequence(input_list, sequence):
    """
    * Finds given sequence in the list

    * Params:
        * input_list ('list'): list for searching through
        * sequence ('list'): the sequence to be searched

    * Return:
        * ('int'): start index of founded sequence in the list
    """
    start_index = input_list.index(sequence[0])

    list_length = len(input_list)
    seq_length = len(sequence)

    if 1 < seq_length <= list_length - start_index + 1:
        is_equals = False
        while not is_equals:
            if input_list[start_index: seq_length + start_index] == sequence:
                is_equals = True
            else:
                start_index = input_list[start_index + 1: list_length - 1].index(sequence[0])
    return start_index


def find_first_min(input_list, amount):
    """
    * Finds first minimal elements in a given quantity

    * Params:
        * input_list ('list'): list for searching through
        * amount ('int'): amount of minimal elements to search

    * Return:
        * ('list'): list of minimal elements
    """
    minimals = []
    buffer_list = list(input_list)
    while len(minimals) < amount:
        minimum = min(buffer_list)
        minimals.append(minimum)
        buffer_list.remove(minimum)
    return minimals


def find_first_max(input_list, amount):
    """
    * Finds first maximum elements in a given quantity

    * Params:
        * input_list ('list'): list for searching through
        * amount ('int'): amount of maximum elements to search

    * Return:
        * ('list'): list of maximum elements
    """
    maximums = []
    buffer_list = input_list
    while len(maximums) < amount:
        maximum = max(buffer_list)
        maximums.append(maximum)
        buffer_list.remove(maximum)
    return maximums


def find_average(input_list):
    """
    * Finds average of elements from given array

    * Params:
        * input_list ('list'): list of elements

    * Return:
        * ('float'): average of elements
    """
    sum_of_elements = 0
    for elem in input_list:
        sum_of_elements += elem
    return sum_of_elements / len(input_list)


def remove_duplicates(input_list):
    """
    * Removes duplicates from given list

    * Params:
        * input_list ('list'): list of elements

    * Return:
        * ('list'): list with removed duplicates
    """
    output_list = []
    for elem in input_list:
        if elem not in output_list:
            output_list.append(elem)
    return output_list
