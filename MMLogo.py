from __future__ import print_function


def print_symbols(size, symbol):
    result = ""
    for _ in range(size):
        result += symbol
    return result


def print_top_part(start_space_count, stars_count, middle_space_count):
    print(print_symbols(start_space_count, "-") + print_symbols(stars_count, "*") + print_symbols(middle_space_count, "-") + print_symbols(stars_count, "*") + \
          print_symbols(start_space_count, "-") + print_symbols(start_space_count, "-") + print_symbols(stars_count, "*") + print_symbols(middle_space_count, "-") + \
          print_symbols(stars_count, "*") + print_symbols(start_space_count, "-"))


def print_bottom_part(start_space_count, stars_count, stars_middle_count, middle_space_count):
    print(print_symbols(start_space_count, "-") + print_symbols(stars_count, "*") + print_symbols(middle_space_count, "-") + print_symbols(stars_middle_count, "*") + \
          print_symbols(middle_space_count, "-") + print_symbols(stars_count, "*") + print_symbols(start_space_count, "-") +
          print_symbols(start_space_count, "-") + print_symbols(stars_count, "*") + print_symbols(middle_space_count, "-") + print_symbols(stars_middle_count, "*") + \
          print_symbols(middle_space_count, "-") + print_symbols(stars_count, "*") + print_symbols(start_space_count, "-"))


def print_last_line(count):
    print(print_symbols(count, "*") + print_symbols(count, "-") + print_symbols(count, "*") + print_symbols(count, "-") + \
          print_symbols(count, "*") + print_symbols(count, "*") + print_symbols(count, "-") + print_symbols(count, "*") + \
          print_symbols(count, "-") + print_symbols(count, "*"))


print("Enter number:", end=" ")
n = int(input())
row_size = n + 1
col_size = n * 10
start_space_count = n
middle_top_space_count = n
middle_bottom_space_count = 1
middle_decrease_stars_count = 1
stars_count = n
if 2 < n < 10000:
    if (n % 2) == 1:
        for row in range(row_size):
            for col in range(col_size):
                if col == 0 and row != row_size - 1:
                    if row < row_size / 2:
                        print_top_part(start_space_count, stars_count, middle_top_space_count)
                        start_space_count -= 1
                        middle_top_space_count -= 2
                        stars_count += 2
                    else:
                        print_bottom_part(start_space_count, n, n*2 - middle_decrease_stars_count, middle_bottom_space_count)
                        start_space_count -= 1
                        middle_bottom_space_count += 2
                        middle_decrease_stars_count += 2

                if col == 0 and row == row_size - 1:
                    print_last_line(n)

    else:
        print("Enter odd number!")
else:
    print("Enter number between 2 and 10 000")