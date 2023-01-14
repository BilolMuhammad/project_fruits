import csv


def get_cheapest_fruit_id(data: str) -> id:
    """
    This function returns the index of the cheapest fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the cheapest fruit
    """
    # your code here
    pass
    reader = open(data).read().split('\n')[1:]
    num_list = []
    for n in reader:
        num_list.append(float(n.split(',')[1]))

    min1 = num_list[0]
    for m in num_list:
        if m < min1:
            min1 = m

    return num_list.index(min1)


print(get_cheapest_fruit_id('fruits.csv'))
