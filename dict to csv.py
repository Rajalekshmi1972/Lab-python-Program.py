import csv
data ={
     "Name": ["avinash", "anu"],
     "Age" : [23, 21]
}
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(data.keys())   
    rows = zip(*data.values())
    writer.writerows(rows)         

print("CSV file is created!")
