import matplotlib.pyplot as plt
from sqlalchemy import values
from storage import getExpenses

def summaryformonth(month,year):
    expense=getExpenses()
    report=[]
    for i in expense:
        _,i_month,i_year=i['date'].split('-')
        if int(i_month) == int(month) and int(i_year) == int(year):
            report.append(i)
        
    if not report:
        print(f"No expenses in  {month}/{year}.")
        return
    
    total=0
    for i in report:
        total+=i['amount']
    print(f"\nExpense Summary for {month}/{year}:\n")
    print(f"Total Expenses Rs.{total}")
    print("no of transactions:",len(report))

def hightestExpense():
    expense=getExpenses()
    if not expense:
        print("No expenses found.")
        return
    report={}
    max=0
    max_cat=""
    for i in expense:
        cat=i['category']
        report[cat]=report.get(cat,0)+i['amount']
        if report[cat] > max:
            max = report[cat]
            max_cat = cat
    print("\nHighest Expense Category:\n")
    print(f"{max_cat}: Rs.{max}")

def pie_chart():
    expense=getExpenses()
    if not expense:
        print("No expenses found.")
        return
    report={}
    for i in expense:
        cat=i['category']
        report[cat]=report.get(cat,0)+i['amount']
        labels=list(report.keys())
        value=list(report.values())
    plt.figure(figsize=(6, 6))
    plt.pie(value, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Spending by Category")
    plt.show()

    
