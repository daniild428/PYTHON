sequence = input("Введите последовательность:")



punctuation_set = set()


for char in sequence:
    if char in {'!', '?', ',', '.', ':', '<', '>', '=', '<=', '>=', '==', '!=', '<>'}:
        punctuation_set.add(char)


print("Множество знаков препинания и операций отношения в последовательности:")
print(punctuation_set)