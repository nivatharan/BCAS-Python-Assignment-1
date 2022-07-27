def summaryDetails():

    print("=== Summary ===")
    print("""
\n
+======================+
| Income Details       |
+======================+
""")
    TotalIncome = 0
    with open("C:/Users/Nivan/Desktop/Python ESOFT/income.txt", "r") as IncomeFile:
        ReadLine = IncomeFile.readlines()
        TotalElement = len(ReadLine)
        print("Number of Records in Income File: ", TotalElement)

        for i in ReadLine:
            TotalIncome = TotalIncome + int(i)
        print("Total Income: ", TotalIncome)

        AverageIncome = TotalIncome / TotalElement
        print("Average Income: ", AverageIncome)

    print("""
\n
+====================+
| Expense Details    |
+====================+
""")
    TotalExpense = 0
    with open("C:/Users/Nivan/Desktop/Python ESOFT/expense.txt", "r") as ExpenseFile:
        ReadLine = ExpenseFile.readlines()
        TotalElement = len(ReadLine)
        print("Number of Records in Expense File: ", TotalElement)

        for i in ReadLine:
            TotalExpense = TotalExpense + int(i)
        print("Total Expense: ", TotalExpense)

        AverageExpense = TotalExpense / TotalElement
        print("Average Expense: ", AverageExpense)

    print("\n")

    DifferIncomeExpense = TotalIncome - TotalExpense
    print("Any difference by deducting expense from income: ", DifferIncomeExpense)
    print("\n")


if __name__ == "__main__":
    summaryDetails()
