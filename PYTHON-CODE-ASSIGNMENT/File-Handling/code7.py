import csv

def column_averages(filename):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)
        sums = [0] * len(headers)
        count = 0
        for row in reader:
            for i in range(len(row)):
                try:
                    sums[i] += float(row[i])
                except ValueError:
                    pass
            count += 1
        averages = [s / count for s in sums]
        return dict(zip(headers, averages))

print("Column Averages: ")
print("-------------------------------------------------")
print(column_averages("data.csv"))
