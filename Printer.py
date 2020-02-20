def print_symbols(count, symbol):
    result = ""
    for _ in range(count):
        result += symbol
    return result


def get_top_m(start_space_count, stars_count, middle_space_count):
    return (print_symbols(start_space_count, "-") + print_symbols(stars_count, "*") +
            print_symbols(middle_space_count, "-") + print_symbols(stars_count, "*") +
            print_symbols(start_space_count, "-"))


def get_bottom_m(start_space_count, stars_count, stars_middle_count, middle_space_count):
    return (print_symbols(start_space_count, "-") + print_symbols(stars_count, "*") +
            print_symbols(middle_space_count, "-") + print_symbols(stars_middle_count, "*") +
            print_symbols(middle_space_count, "-") + print_symbols(stars_count, "*") +
            print_symbols(start_space_count, "-"))


def print_top_part(start_space_count, stars_count, middle_space_count):
    print(get_top_m(start_space_count, stars_count, middle_space_count) +
          get_top_m(start_space_count, stars_count, middle_space_count))


def print_bottom_part(start_space_count, stars_count, stars_middle_count, middle_space_count):
    print(get_bottom_m(start_space_count, stars_count, stars_middle_count, middle_space_count) +
          get_bottom_m(start_space_count, stars_count, stars_middle_count, middle_space_count))


def print_last_line(count):
    print(print_symbols(count, "*") + print_symbols(count, "-") + print_symbols(count, "*") +
          print_symbols(count, "-") + print_symbols(count, "*") + print_symbols(count, "*") +
          print_symbols(count, "-") + print_symbols(count, "*") + print_symbols(count, "-") + print_symbols(count, "*"))
