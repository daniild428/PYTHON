set1 = set(map(int, input("Введите числа первого множества через пробел: ").split()))
set2 = set(map(int, input("Введите числа второго множества через пробел: ").split()))


unique_numbers = set1.union(set2)
print("Различные числа в обоих множествах:", unique_numbers)


common_numbers = sorted(list(set1.intersection(set2)))
print("Числа, входящие в оба множества в порядке возрастания:", common_numbers)