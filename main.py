from tracker  import addExpense, checkreport, deleteExpense, categoryReport
from report import summaryformonth, hightestExpense, pie_chart

def main():
    print("Welcome to Expense Tracker made by Aakarshit Sharma\n")
    while True:
        print("\nPlease select an option:")
        print("1. Add your Expense")
        print("2. Check you Report")
        print("3. Delete any Expense")
        print("4. According to Category Report")
        print("5. Summary for a particular Month")
        print("6. Highest Expense")
        print("7. Pie Chart of Expenses")
        print("8. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            date=input("Enter Date pls (dd-mm-yyyy)").strip() 
            print("Categories:Food, Travel,Bills,Subscription,Entertainment,Other")
            category=input("Enter Category: ").strip()
            try:
                amount=int(input("Enter Amount: ").strip())
            except ValueError:
                print("Enter amount is wrong please fill the correct amount ")
                continue
            description=input("Enter Description: ").strip()
            addExpense(date,category,amount,description)
        elif choice == '2':
            checkreport()
        elif choice == '3':
            checkreport()
            try:
                idx=int(input("Enter the index of the expense to delete: ").strip())
                deleteExpense(idx)
            except ValueError:
                print(" index  not right ")
                continue
        elif choice == '4':
            categoryReport()
        elif choice == '5':
            try:
                month=input("Please enter the month(MM)").strip()
                year=input("Please enter the year(YYYY)").strip()
                summaryformonth(month,year)
            except ValueError:
                print("Wrong month and year entered")
                continue
        elif choice == '6':
            hightestExpense()
        elif choice == '7':
            pie_chart()
        elif choice == '8':
            print(" Bye Bye")
            break
        else:
            print("Wrong input please enter the right one")

if __name__ == "__main__":    
    main()
