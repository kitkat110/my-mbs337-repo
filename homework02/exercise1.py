nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even_or_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} even")
        else:
            print(f"{num} odd")

even_or_odd(nums_list)