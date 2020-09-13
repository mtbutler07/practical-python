# pcost.py
#
# Exercise 1.27

sum = 0
with open("Work/Data/portfolio.csv", mode="r") as f:

    headers = next(f).split(",")
    for line in f:
        line = line.strip()
        line = line.replace('"', "")
        line = line.split(",")
        sum += int(line[1]) * float(line[2])

print(f"Total cost {sum}")