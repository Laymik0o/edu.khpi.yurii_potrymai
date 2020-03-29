import math


def main():
    task_1()
    task_2()
    task_3()


def task_1():
    print("Task 1")
    a = float(input("Enter a "))
    b = float(input("Enter b "))
    z = ((math.cos(a) - math.cos(b)) ** 2 - (math.sin(a) - math.sin(b)) ** 2)
    print(z)


def task_2():
    print("Task 2")
    n = int(input("Enter n "))
    sum_of_array = 0
    size = int(n / 2)
    for i in range(1, size + 1):
        if n % i == 0:
            sum_of_array += i
    print(sum_of_array)
    print(sum_of_array < n)


def task_3():
    print("Task 3")
    size = int(input("Enter size of array "))
    array = []
    for i in range(size):
        array.append(int(input("Enter %d number: " % (i))))
    print("Min negative number there: ", get_min_negative_number_in_array(array))
    print("There average of positive", get_average(get_positive(array)))
    print("Positive numbers there: ", get_positive(array))


def get_average(array):
    sum_of_elements = 0
    for element in array:
        sum_of_elements += element
    return sum_of_elements / len(array)


def get_min_negative_number_in_array(array):
    array_negatives = get_negative(array)
    if len(array_negatives) == 0:
        print("No negatives there")
    else:
        return min(array_negatives)


def get_negative(array):
    array_negative = []
    for element in array:
        if element < 0:
            array_negative.append(element)
    return array_negative


def get_positive(array):
    array_positive = []
    for element in array:
        if element > 0:
            array_positive.append(element)
    return array_positive


if __name__ == "__main__":
    main()
