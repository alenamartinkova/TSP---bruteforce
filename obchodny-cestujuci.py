from typing import List
from itertools import permutations
from threading import Thread
from Coordinate import Coordinate


def calculate_combinations(list_of_coords: list, recursive_list: list, final_combinations: list) -> list:
    for coord in list_of_coords:
        if coord in recursive_list:
            continue

        _list = [*recursive_list, coord]
        if len(_list) != len(list_of_coords):
            calculate_combinations(list_of_coords, _list, final_combinations)
        else:
            final_combinations.append(_list)

    return final_combinations


def calculate_distance(comb: List[Coordinate], result: List) -> float:
    for one_comb in comb:
        distance_sum = 0

        for i in range(len(one_comb) - 1):
            distance_sum += one_comb[i].distance(one_comb[i + 1])

        result.append(distance_sum)


coords_list = []
with open("/Users/alenamartinkova/Desktop/School/Ing./2. rok/PA/data.txt") as f:
    lines_after_7 = list(f.readlines())[7:]

    for line in lines_after_7:
        _, number, x, y = line.split(" ")
        coords_list.append(Coordinate(float(x), float(y)))

coords_list = coords_list[:10]
all_combinations = permutations(coords_list)
iterable_all_combinations = list(all_combinations)

thread_list = []
result = []
number_of_threads = 4

for thread in range(number_of_threads):
    data_for_thread = []

    for index, x in enumerate(iterable_all_combinations):
        if index % number_of_threads == thread:
            data_for_thread.append((*x, x[0]))

    thread_var = Thread(args=(data_for_thread, result), target=calculate_distance)
    thread_var.start()
    thread_list.append(thread_var)

for thread in thread_list:
    thread.join()

min_result = min(result)
print(min_result)
