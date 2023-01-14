def get_expensive_fruit(data: str) -> str:
    """
    This function returns the name of the most expensive fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the most expensive fruit
    """
    # your code here
    data = open(data).read().split('\n')[1:]
    num_list = []
    for n in data:
        num_list.append(float(n.split(',')[1]))

    max = num_list[0]
    for n in num_list:
        if n > max:
            max = n
    ans = ''
    for d in data:
        if float(d.split(',')[1]) == max:
            ans = d.split(',')[0]
    return ans


print(get_expensive_fruit('fruits.csv'))
