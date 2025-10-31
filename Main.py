import csv

# Data rows
rows = [
    ["teller_id", "name", "counter_type", "shift_start", "shift_end", "status"],
    ["T001", "A. Gunawardena", "Cash Counter", "08:00:00", "16:00:00", "Active"],
    ["T002", "B. Perera", "General Inquiry", "08:00:00", "16:00:00", "Active"],
    ["T003", "C. Fernando", "Cash Counter", "09:00:00", "17:00:00", "Active"],
    ["T004", "D. Silva", "Loan Desk", "09:00:00", "15:00:00", "On Break"]
]

# File name
filename = "teller.csv"

# Write CSV file
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print(f"{filename} created successfully!")
