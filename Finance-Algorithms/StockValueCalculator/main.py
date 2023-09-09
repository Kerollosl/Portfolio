def main():
    start = int(input("How much are you starting with?\n"))
    putting_in = int(input("\nHow much are you putting in per year?\n"))
    rate = float(input("\nAt what rate of return?\n"))
    if rate > 1:
        rate = rate / 100
    years = int(input("\nFor how many years?\n"))

    total = start
    current_year = 2023
    for i in range(1, years + 1):
        total = (1 + rate) * (total + putting_in)
        current_year +=1
        print("After {} years the total is ${:,.0f}".format(i, total))
       # print("Year: {} After {} years the total is ${:,.0f}".format(current_year, i, total))
if __name__ == "__main__":
    main()