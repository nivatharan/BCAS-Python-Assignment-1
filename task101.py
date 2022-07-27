import os
import summary


def Task():
    os.system("cls")
    print("======Welcome To The DashBoard======")
    print("""
    +============================+
    | Press [1] for INCOME       |
    | Press [2] for EXPENSE      |
    | Press [3] for Summary      |
    | Press [0] for QUIT         |
    +============================+
    \n
    """)

    while True:
        UserInput = int(input("\nEnter your Choice [1 or 2]: "))
        if UserInput == 1:
            with open("C:/Users/Nivan/Desktop/Python ESOFT/income.txt", "a") as File:
                IncomeAmmount = int(input("Enter the Income ammount: "))
                Write = File.write(str(IncomeAmmount)+"\n")
        elif UserInput == 2:
            with open("C:/Users/Nivan/Desktop/Python ESOFT/expense.txt", "a") as File:
                InputExpense = int(input("Enter the Expense: "))
                Write = File.write(str(InputExpense)+"\n")
        elif UserInput == 3:
            summary.summaryDetails()
        elif UserInput == 0:
            print("\n---Thank you!---\n")
            exit()
        else:
            print("!!!Enter Valid input!!!")


if __name__ == "__main__":
    Task()
