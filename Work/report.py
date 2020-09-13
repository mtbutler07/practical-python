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
                holding = dict(symbol=row[0], shares=int(row[1]), price=float(row[2]))
                portfolio.append(holding)
            except ValueError:
                print(f"Found missing fields - {row}")
                continue
    return portfolio


if len(sys.argv) == 2:
    filename = sys.argv[1]
    portfolio = read_portfolio(filename)
    total = 0
    for holding in portfolio:
        total += holding.get("shares") * holding.get("price")
    print(f"Total cost {total}")
else:
    print("Provide filename")
    sys.exit(1)
