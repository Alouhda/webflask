import random

def ls_while():
    numbers = list()
    length = random.randint(1,10)
    while len(numbers) != length:
        numbers.append(random.randint(10,100))
    return(numbers)  # вместо такой конструкции следует использовать `return numbers` 

	
def ls_for():
    numbers = list()
    length = random.randint(1,11)
    for i in range(length):
        numbers.append(random.randint(10,100))
    return(numbers)


# в питоне есть очень полезная конструкция:
# some_list = [element for element in range(100)] ## можно почитать тут: https://habr.com/ru/post/320288/
# ниже - пример ее использования
def get_rand_list():
    low_val = 10
    up_val = 100
    rand_length = random.randint(1, 11)
    numbers = [random.randint(low_val, up_val) for _ in range(rand_length)]
    return numbers
