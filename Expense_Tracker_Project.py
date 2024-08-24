class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount


class Expense_Tracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):

        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("sucessfully remove expenses")
        else:
            print("Not Found INDEX VALUE FOR EXPENSES")

    def view_expense(self):
        if len(self.expenses) == 0:
            print("No found expense")

        else:
            print("List Exepenses")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. Date: {expense.date},Description:{expense.description},Amount:{expense.amount}")

    def total_expense(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses:Rs.{total:2f}")


def main():
    tracker = Expense_Tracker()

    while True:
        print("Expensice detail fills\n1.Add\n2.Remove\n3.View\n4.Total\n5.exit")
        choice = input("Enter Number 1-5 =")
        if choice == '1':
            Date = input("Enter Date (dd-mm-yyyy):")
            Description = input("Enter Description:")
            Amount = float(input("Enter Amount:"))
            expense = Expense(Date, Description, Amount)
            tracker.add_expense(expense)    
        elif choice == "2":

            index = int(input("Enter index value")) - 1
            tracker.remove_expense(index)

        elif choice == '3':
            tracker.view_expense()

        elif choice == '4':
            tracker.total_expense()

        elif choice == '5':
            break


if __name__ == '__main__':
    main()
