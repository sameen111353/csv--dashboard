import csv

# Create CSV file
with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks", "Age"])
    writer.writerow(["Ali", 85, 20])
    writer.writerow(["Sara", 90, 21])
    writer.writerow(["Ahmed", 78, 19])

print("CSV file created successfully")

# Read CSV file
with open("student.csv", "r") as file:
    reader = csv.reader(file)
    lines = list(reader)

# Store headers separately
headers = lines[0]

# Menu loop
while True:
    print("\n--- CSV CLI Dashboard ---")
    print("1. Show Columns")
    print("2. Count Rows")
    print("3. Search Name")
    print("4. Exit")

    choice = input("Enter choice: ")

    # 1. Show columns
    if choice == "1":
        print("\nColumns:")
        for col in headers:
            print(col)

    # 2. Count rows
    elif choice == "2":
        print("Total rows:", len(lines) - 1)

    # 3. Search name
    elif choice == "3":
        search = input("Enter name: ").strip().lower()
        found = False

        for row in lines[1:]:
            if row[0].strip().lower() == search:
                print("Name:", row[0])
                print("Marks:", row[1])
                print("Age:", row[2])
                found = True
                break

        if not found:
            print("Not found")

    # 4. Exit
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
