# pcost.py
#
# Exercise 1.27


def portfolio_cost(filename):

    sum = 0
    with open(filename, mode="r") as f:
        next(f)
        for line in f:
            line = line.strip()
            line = line.replace('"', "")
            line = line.split(",")
            try:
                sum += int(line[1]) * float(line[2])
            except ValueError:
                print(f"Found missing fields - {line}")
                continue
    return sum


cost = portfolio_cost("Work/Data/missing.csv")

print(f"Total cost {cost}")
