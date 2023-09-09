def main():
    while True:
        try:
            principle = float(input("What is the amount of the loan you are taking out?\n"))
            break
        except:
            print("Invalid input...try again")
    while True:
        try:
            rate = float(input("\nWhat is the interest rate of your loan?\n"))
            break
        except:
            print("Invalid input...try again")
    while True:
        try:
            years = float(input("\nHow many years is your loan over?\n"))
            break
        except:
            print("Invalid input...try again")
    while True:
        try:
            down_payment = float(input("\nWhat is your down payment? (20% would be ${:,.0f})\n".format(principle * 0.2)))
            break
        except:
            print("Invalid input...try again")

    principle -= down_payment

    n = years * 12
    if rate < 1:
        rate /= 12
    else:
        rate /= 1200

    monthly_payment = (principle * rate * pow(1 + rate, n)) / (pow(1 + rate, n) - 1)
    yearly_interest = 0
    yearly_principle = 0
    accumulated_equity = down_payment
    accumulated_interest = 0
    choice = input("\nYour monthly payment (principle and interest only) will be: ${:.2f}\n\nDo you want to have a fixed monthly payment that you pay until you finish the mortgage? (Y/N)\n".format(monthly_payment)).strip().lower()

    if choice == 'Y' or choice == 'y':
        monthly_payment = float(input("\nHow much do you want to pay per month until you finish your mortgage?\n"))

    months = 0

    for i in range(1, int(years * 12) + 1):
        monthly_interest = principle * rate
        monthly_principle = monthly_payment - monthly_interest
        principle -= monthly_principle
        accumulated_equity += monthly_principle
        accumulated_interest += monthly_interest

        yearly_principle += monthly_principle
        yearly_interest += monthly_interest

        if i % 12 == 0:
            print("Your total interest paid for year {} is: ${:,.0f}".format(i // 12, yearly_interest))
            print("Your total principle paid for year {} is: ${:,.0f}".format(i // 12, yearly_principle))
            print("Making your total accumulated equity over {} years: ${:,.0f}".format(i // 12, accumulated_equity))
            print("And your total accumulated interest: ${:,.0f}\n".format(accumulated_interest))
            yearly_interest = 0
            yearly_principle = 0

        if principle <= 0:
            years = int(i / 12)
            months = i % 12
            break

    choice_2 = input(f"In total, it will cost you ${accumulated_equity + accumulated_interest:,.0f} over {years} "
                     f"years and {months} months to finance this house, which is ${monthly_payment:,.0f} "
                     f"per month.\nWould you like to add Taxes, mortgage insurance, HOA fees, etc., to your total monthly payment?\n")


    if choice_2 == 'y' or choice_2 == 'Y':
        tax = float(input("\nProperty Tax? (per month)\n"))
        insurance = float(input("\nHome Insurance?\n"))
        hoa = float(input("\nHOA?\n"))

        total_fees = tax + insurance + hoa

        print(
            "\nIncluding extra payments listed above, it will cost you a total of $%.2lf to finance this house,\nwhich is $%.2lf per month over %.0lf years" % (
            accumulated_equity + accumulated_interest + total_fees * 12 * years, monthly_payment + total_fees, years))
    elif choice_2 == 'n' or choice_2 == 'N':
        pass
    while True:
        if choice not in ['y', 'Y', 'n', 'N']:
            print("\nInvalid answer try again\n")
            choice = input().strip()
        else:
            break
if __name__ == "__main__":
    main()