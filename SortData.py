from typing import Optional


def SortData(file_paths):
    global values
    file = open(file_paths, "r")

    array1: list[int]
    array1, array2, array3 = [], [], {}

    lines: list[str] = file.readlines()
    new_file = open("FinalSortedFile.txt", "a")
    for x in lines:
        row = x.split(",")
        array1.append(int(row[0]))
        array2.append(row[1])
        name = row[1].replace("\n", "")
        array3[int(row[0])] = name
    array1.sort(reverse=False)

    for x in array1:
        values = array3.get(x)
        print("\n" + str(x) + "," + values)
        combined_data = "\n" + str(x) + "," + values

        print(combined_data)

        new_file.write(combined_data)

    new_file.close()
    file.close()


file_paths = "M1.txt"

SortData(file_paths)
