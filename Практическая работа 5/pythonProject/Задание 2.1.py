pages_on_first_day = 40
increase_factor = 1.05


total_pages = 0

for _ in range(10):
    total_pages += pages_on_first_day
    pages_on_first_day *= increase_factor

print("Общее количество прочитанных страниц за 10 дней: {}".format(int(total_pages)))