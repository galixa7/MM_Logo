from __future__ import print_function
import Validator
import Printer
import Counter

print("Enter number:", end=" ")
n = int(input())
counters = Counter.Counters(n)
if Validator.has_validate_input(n):
    for row in range(counters.row_size):
        for col in range(counters.col_size):
            if col == 0 and row != counters.row_size - 1:
                if row < counters.row_size / 2:
                    Printer.print_top_part(counters.start_space, counters.stars, counters.middle_top_space)
                    counters.increase()
                else:
                    Printer.print_bottom_part(counters.start_space, n, n * 2 - counters.middle_decrease_stars, counters.middle_bottom_space)
                    counters.decrease()

            if col == 0 and row == counters.row_size - 1:
                Printer.print_last_line(n)
