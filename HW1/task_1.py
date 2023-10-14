#ИМПЕРАТИВНЫЙ 
def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

#ДЕКЛАРАТИВНЫЙ
def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)
