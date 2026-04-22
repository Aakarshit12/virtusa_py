from expense import Expense
from storage import getExpenses, putExpenses

def addExpense(date,cat,amt,desc):
    expense=getExpenses()
    new_expense={
        "date":date,
        "category":cat,
        "amount":amt,
        "description":desc
    }
    expense.append(new_expense)
    putExpenses(expense)
    print("Expense added successfully")
def checkreport():
    expense=getExpenses()
    if not expense:
        print("expense not found")
        return 
    print('\n All Expenses done so far: \n')
    i=0
    for exp in expense:
        i+=1
        print(f"{i}. {exp['date']} - {exp['category']} - Rs.{exp['amount']} - {exp['description']}")

def deleteExpense(idx):
    expense=getExpenses()
    if idx<1 or idx>len(expense):
        print("invalid index")
        return
    removed=expense.pop(idx-1)
    putExpenses(expense)
    print(f"\nExpense '{removed['description']}' deleted successfully")

def categoryReport():
    expense=getExpenses()
    if not expense:
        print("No expenses found.")
        return
    report={}
    for i in expense:
        cat=i['category']
        amt=i['amount']
        if cat in report:
            report[cat]+=amt
        else:
            report[cat]=amt
    print("\nExpense Report by Category:\n")
    for cat,amt in report.items():
        print(f"{cat}: Rs.{amt}")
    return report

