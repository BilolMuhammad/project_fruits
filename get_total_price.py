import csv


def get_total_price(data: str) -> float:
    """
    This function returns the total price of the fruits in the list

    args:
        data: CSV file with the fruits data
    returns:
        list of fruits total price
    """
    file = open(data)
    reader = csv.reader(file)
    next(reader)
    sum = 0
    for n in reader:
        sum += float(n[1])
    return sum


print(get_total_price('fruits.csv'))
