import random


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or  quantity > (max-min):
        return "Wrong values"
    empty_set = set()
    while len(empty_set) != quantity:
        empty_set.add(random.randint(min, max+1))
    numbers = list(empty_set)
    return sorted(numbers)


print(get_numbers_ticket(1,36,6))
print(get_numbers_ticket(0,36,6))
print(get_numbers_ticket(1,36,37))