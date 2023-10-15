sym_weight = 4# TODO Найдите количество книг, которое можно разместить на дискете
sym_cnt = 25
lines_cnt = 50
pages_cnt = 100

disc_capacity_in_bytes = 1.44 * 1024 * 1024
books_cnt = disc_capacity_in_bytes / (sym_weight * sym_cnt * lines_cnt * pages_cnt)


print("Количество книг, помещающихся на дискету:", round(books_cnt))
