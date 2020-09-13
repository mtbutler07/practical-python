# report.py
#
# Exercise 2.4
import csv
import sys


def read_portfolio(filename: str) -> list:

    with open(filename, mode="r") as f:
        rows = csv.reader(f)
        next(rows)  # skip headers
        portfolio = []
        for row in rows:
            try:
                holding = (row[0], int(row[1]), float(row[2]))
                portfolio.append(holding)
            except ValueError:
                print(f"Found missing fields - {row}")
                continue
    return portfolio


if len(sys.argv) == 2:
    filename = sys.argv[1]
    portfolio = read_portfolio(filename)
    total = 0
    for symbol, shares, price in portfolio:
        total += shares * price
    print(f"Total cost {total}")
else:
    print("Provide filename")
    sys.exit(1)
