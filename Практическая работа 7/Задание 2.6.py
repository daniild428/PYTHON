def draw_numbers(rows):
    for i in range(1, rows + 1):
        line = " ".join(["5"] * i)
        print(line)

draw_numbers(5)
