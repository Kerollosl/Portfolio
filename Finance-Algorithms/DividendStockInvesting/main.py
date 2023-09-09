def calculate_portfolio_growth(initial_amount, annual_investment, dividend_yield, num_years):
    portfolio_value = initial_amount
    for year in range(1, num_years + 1):
        portfolio_value += annual_investment
        annual_dividend = portfolio_value * (dividend_yield / 100)
        portfolio_value += annual_dividend
        formatted_portfolio_value = "{:,}".format(round(portfolio_value))
        formatted_annual_dividend = "{:,}".format(round(annual_dividend))

        print(f"The portfolio value after {year} years will be: ${formatted_portfolio_value}")
        print(f"        ****The ANNUAL DIVIDEND PAYMENT will be: ${formatted_annual_dividend}****")
        print("\n")
    return portfolio_value




def main():
    # Example usage
    initial_amount = 5000
    annual_investment = 30000
    dividend_yield = 3
    num_years = 40

    portfolio_value = calculate_portfolio_growth(initial_amount, annual_investment, dividend_yield, num_years)



if __name__ == "__main__":
    main()
