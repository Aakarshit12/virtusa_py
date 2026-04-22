import json
import os

fi="expenses.json"
# this functio will be used when we need the data in the file eg- when asked for the report
def getExpenses():
    if not os.path.exists(fi):
        return []
    with open(fi,"r") as f:
        return json.load(f)
#  this is a function we are using to save the data to expense json file
def putExpenses(ex):
    with open(fi,"w") as f:
        json.dump(ex,f) 