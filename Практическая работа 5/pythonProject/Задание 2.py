initial_norm = 10
increase_factor = 1.10


total_distance = 0


for _ in range(7):
    total_distance += initial_norm
    initial_norm *= increase_factor

print("Суммарный пройденный путь за неделю: {:.2f} км".format(total_distance))