# Task 2: Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "MSFT": 300
}

stock_name = input("Enter stock name (AAPL, TSLA, GOOGL, MSFT): ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stock_prices:
    price = stock_prices[stock_name]
    total_value = price * quantity

    print("Stock Name:", stock_name)
    print("Price per Stock:", price)
    print("Quantity:", quantity)
    print("Total Investment Value:", total_value)
else:
    print("Stock not found!")