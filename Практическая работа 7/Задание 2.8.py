def draw_numbers(rows):
    for i in range(rows, 0, -1):
        line = " ".join(["5"] * i)
        print(line)

draw_numbers(5)
