import csv


def get_frutis_name(data: str) -> list:
    """
    This function returns the name of the fruits in the list

    args:
        data: CSV file with the fruits data
    returns:
        list of fruits names
    """
    file = open(data)
    reader = csv.reader(file)
    next(reader)
    name_list = []
    for n in reader:
        name_list.append(n[0])
    return name_list


print(get_frutis_name('fruits.csv'))
