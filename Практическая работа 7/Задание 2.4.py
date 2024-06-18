def draw_flag(N, M):
    for i in range(N):
        if i % 2 == 0:
            print("- " * M)
        else:
            print("+" * M)

N = 5  # количество строк флага
M = 6  # длина строки флага
draw_flag(N, M)
