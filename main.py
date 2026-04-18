import csv

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    amount = input("Enter amount: ")
    category = input("Enter category: ")

    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])

    print("Expense added successfully!")

def view_total():
    total = 0
    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[1])
        print("Total expense:", total)
    except:
        print("No data found.")

while True:
    print("\n1. Add Expense")
    print("2. View Total")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_total()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
