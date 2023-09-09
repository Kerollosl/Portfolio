def main():

    income = get_input("What is your household income after taxes?\n")
    monthly = income/12
    leftover = calculate_leftover(income)
    expenses = monthly - leftover
    fun = income * 0.1
    investments = (monthly - expenses) * 12 - fun
    percentage = investments / income * 100
    expense_ratio = expenses / monthly * 100


    output = "Your total monthly income after taxes is ${:,.0f} and your total monthly expenses is ${:,.0f}\nmaking your monthly expenses {:,.2f}% of your monthly income."
    output2 = "It is good to spend about 10% of your income on fun which in your case would be ${:,.0f}.\nThis would make your total leftover for investments ${:,.0f} which is {:,.2f}% of your total income\n"


    print(output.format(monthly, expenses, expense_ratio))
    print(output2.format(fun, investments, percentage))

def get_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_leftover(income):
    car_insurance = get_input("\nWhat is your car insurance payment?\n")
    leftover = income - car_insurance

    rent_or_mortgage = get_input("\nHow much do you spend per month on rent or mortgage payments?\n")
    leftover = leftover / 12 - rent_or_mortgage

    gas = get_input("\nHow much do you spend per month on gas?\n")
    leftover = leftover - gas

    student_loans = get_input("\nHow much do you spend per month on student loans?\n")
    leftover = leftover - student_loans

    car_payment = get_input("\nWhat is your monthly car payment?\n")
    leftover = leftover - car_payment

    food = get_input("\nHow much do you spend per month on food?\n")
    leftover = leftover - food

    health_insurance = get_input("\nHow much do you spend per month on health insurance? (including dental)\n")
    leftover = leftover - health_insurance

    utilities = get_input("\nHow much do you spend per month on utilities?\n")
    leftover = leftover - utilities

    subscriptions = get_input("\nHow much do you spend per month on subscriptions? (Gym, Netflix, Apple Music, etc)\n")
    leftover = leftover - subscriptions

    other_expenses = get_input("\nHow much do you spend per month on anything else not listed above?\n")
    leftover = leftover - other_expenses

    return leftover


if __name__ == "__main__":
    main()
