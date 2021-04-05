import random

def ls_while():
    numbers = list()
    length = random.randint(1,10)
    while len(numbers) != length:
        numbers.append(random.randint(10,100))
    return(numbers)
print(ls_while())

	
def ls_for():
    numbers = list()
    length = random.randrint(1,11)
    for i in range(length):
        numbers.append(random.randint(10,100))
    return(numbers)
print(ls_while())
	
