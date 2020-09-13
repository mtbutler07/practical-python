# pcost.py
#
# Exercise 1.27

import csv
import sys


def portfolio_cost(filename):

    with open(filename, mode="r") as f:

        rows = csv.reader(f)
        next(rows)
        sum = 0
        for row in rows:
            try:
                sum += int(row[1]) * float(row[2])
            except ValueError:
                print(f"Found missing fields - {row}")
                continue
    return sum


if len(sys.argv) == 2:
    filename = sys.argv[1]
    cost = portfolio_cost(filename)
    print(f"Total cost {cost}")
else:
    print("Provide filename")
    sys.exit(1)
