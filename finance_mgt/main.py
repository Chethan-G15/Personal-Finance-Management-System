from database.db import create_users_table
from auth.auth_service import register_user, login_user
from transactions.transaction import add_transaction,view_transaction,update_transaction,delete_transaction
from report import get_monthly_report,get_yearly_report
from budget import set_budget, check_budget
from backup import backup_database, restore_database

def main():
    create_users_table()

    while True:
        print("\n===== Personal Finance Manager =====")
        print("1. Register")
        print("2. Login")
        print("3. Backup Data")
        print("4. Restore Data")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            user_id=login_user()
            if user_id:
                while True:
                    print("\n---- Transaction Menu ----")
                    print("1. Add Transaction")
                    print("2. View Transactions")
                    print("3. Update Transaction")
                    print("4. Delete Transaction")
                    print("5. Monthly Report")
                    print("6. Yearly Report")
                    print("7. set Budget")
                    print("8. Check Budget")
                    print("7. Logout")

                    t_choice = input("Enter choice: ")
                    if t_choice == "1":
                        add_transaction(user_id)

                    elif t_choice == "2":
                        view_transaction(user_id)

                    elif t_choice == "3":
                        update_transaction(user_id)

                    elif t_choice == "4":
                        delete_transaction(user_id)

                    elif t_choice == "5":
                        month = input("enter month(MM): ")
                        year = input("enter year(yyyy): ")
                        income,expense,savings = get_monthly_report(user_id,month,year)
                        print("\n-------Monthly Report--------")
                        print("total income",income)
                        print("Total expense:",expense)
                        print("savings:",savings)
                    elif t_choice == "6":
                        year = input("Enter year(yyyy): ")
                        income,expense,savings = get_yearly_report(user_id,year)
                        print("\n-------Yearly Report---------")
                        print("Total income:",income)
                        print("total expense:",expense)
                        print("savings:",savings)
                    
                    elif choice == "7":
                        category = input("Enter category: ")
                        amount = float(input("Enter budget amount: "))
                        month = input("Enter month (MM): ")
                        year = input("Enter year (YYYY): ")

                        set_budget(user_id, category, amount, month, year)
                        print("✅ Budget set successfully!")

                    elif choice == "8":
                        category = input("Enter category: ")
                        month = input("Enter month (MM): ")
                        year = input("Enter year (YYYY): ")

                        budget, spent, remaining = check_budget(user_id, category, month, year)

                        if budget is None:
                            print("No budget set for this category.")
                        else:
                            print("\n--- Budget Report ---")
                            print("Budget Limit:", budget)
                            print("Total Spent:", spent)
                            print("Remaining:", remaining)

                            if remaining < 0:
                                print(" You exceeded your budget!")
                            elif remaining <= budget * 0.2:
                                print(" Budget almost finished!")
                            else:
                                print("You are within budget....")                    

                    elif t_choice == "9":
                        print("Logged out successfully!")
                        break
                    else:
                        print("Invalid choice!")

        elif choice == "3":
            print("Thank you for using Finance Manager!")
            break

        elif choice == "4":
            backup_database()

        elif choice == "5":
            restore_database()

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()