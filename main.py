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
                if len(row) < 2:
                    continue
                try:
                    total += float(row[1])
                except:
                    continue

        print("Total expense:", total)

    except FileNotFoundError:
        print("No data found.")

while True:
    print("\n1. Add Expense")
    print("2. View Total")
    print("3. Show Category Chart")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_total()
    elif choice == "3":
        show_category_chart()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
         import matplotlib.pyplot as plt

def show_category_chart():
    data = {}
    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[2]
                amount = float(row[1])
                if category in data:
                    data[category] += amount
                else:
                    data[category] = amount

        categories = list(data.keys())
        amounts = list(data.values())

        plt.bar(categories, amounts)
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.title("Expenses by Category")
        plt.show()

    except:
        print("No data to display.")
