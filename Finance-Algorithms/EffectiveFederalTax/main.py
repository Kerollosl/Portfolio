def gross_income():
    while True:
        try:
            gross_income = float(input("What is your gross income? "))
            return gross_income
        except ValueError:
            print("Invalid input. Please enter a number.")

def income_minus_deductions(gross_income, filing_type):
    while True:
        try:
            deductions = float(input("What are your deductions? (Not Including Standard Deduction) "))
            if deductions > gross_income:
                print("Invalid input. Deductions cannot be greater than gross income.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if filing_type[0].lower() == 's':
        standard_deduction = 12400
    elif filing_type[0].lower() == 'm':
        standard_deduction = 24800
    elif filing_type[0].lower() == 'h':
        standard_deduction = 18600
    else:
        print("Invalid filing type.")
    taxable_income = gross_income - deductions - standard_deduction
    return taxable_income

def calculate_tax(income):
    tax_brackets = [
        (9875, 0.1),
        (40125, 0.12),
        (85525, 0.22),
        (163300, 0.24),
        (207350, 0.32),
        (518400, 0.35),
        (float('inf'), 0.37)
    ]
    tax = 0
    for i, (bracket, rate) in enumerate(tax_brackets):
        if income <= bracket:
            tax += (income - sum(bracket for bracket, rate in tax_brackets[:i])) * rate
            break
        else:
            tax += (bracket - sum(bracket for bracket, rate in tax_brackets[:i])) * rate
    return tax

def main():
    while True:
        filing_type = input("How are you filing your taxes? (Single, Married, Head of Household) ")
        if filing_type[0].lower() in ['s', 'm', 'h']:
            break
        else:
            print("Invalid filing type.")

    gross = gross_income()
    income = income_minus_deductions(gross, filing_type)

    if income < 0:
        income = 0

    tax = calculate_tax(income)
    effective_tax_rate = tax / gross * 100
    fica_tax = gross * 0.0765
    state_tax = gross * 0.0505
    net_income = gross - tax - fica_tax - state_tax

    print(f"\nYour total effective tax will be ${tax:,.0f}")
    print(f"(${tax+fica_tax+state_tax:,.0f} if FICA tax and state income tax are included)")
    print(f"This means that your effective tax rate is {effective_tax_rate:,.3f}%")
    print(f"({effective_tax_rate+7.65+5.05:,.3f}% if FICA tax and state income tax are included)")
    print(f"It also means that your net yearly income after taxes")
    print(f"(including the 7.65% FICA Tax and the 5.05% Massachusetts State Income Tax) is ${net_income:,.0f}")

if __name__ == "__main__":
    main()
