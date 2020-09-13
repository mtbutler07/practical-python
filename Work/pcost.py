# pcost.py
#
# Exercise 1.27

import csv


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


cost = portfolio_cost("Work/Data/missing.csv")

print(f"Total cost {cost}")
