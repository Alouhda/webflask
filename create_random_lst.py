import random

def random_list():
    numbers = list()
    length = random.randrange(1,10)
    i = random.randint(10,100)
    while length != len(numbers):
        numbers.append(i)
    return(numbers)
    result = random_list(numbers)
    print(result)
	
random_list()
