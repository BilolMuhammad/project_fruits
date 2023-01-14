def get_cheapest_fruit(data: str) -> str:
    """
    This function returns the name of the cheapest fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the cheapest fruit
    """
    # your code here
    pass
    reader = open(data).read().split('\n')[1:]
    num_list = []
    for r in reader:
        num_list.append(float(r.split(',')[1]))

    min = num_list[0]
    for n in num_list:
        if n < min:
            min = n
    ans = ''
    for r in reader:
        if float(r.split(',')[1]) == min:
            ans = r.split(',')[0]
    return ans


print(get_cheapest_fruit('fruits.csv'))
