import random


def copy_list(list):
    new_list = []

    for x in range(len(list)):
        new_list.append(list[x])

    return new_list


def shuffle(original_list, times=1):
    list = copy_list(original_list)
    new_list = []

    for i in range(times):
        while list:
            new_list.append(list.pop(random.randint(0, len(list) - 1)))
        list = copy_list(new_list)
        new_list.clear()

    return list
