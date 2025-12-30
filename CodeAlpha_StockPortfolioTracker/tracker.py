import datetime
import csv
import yfinance as yf

portfolio = []
stock_names = []
profits = []

total_investment = 0
total_current_value = 0

print("\n📊 Welcome to Live Stock Portfolio Tracker")
print("-------------------------------------------")
print("Example symbols: AAPL, TSLA, TCS.NS, RELIANCE.NS, INFY.NS")
print("Note: For Indian stocks use .NS suffix\n")

n = int(input("How many different stocks do you own? "))

for i in range(n):
    print(f"\nStock {i+1}:")

    symbol = input("Enter stock symbol: ").upper()

    while True:
        qty_input = input("Enter quantity you bought: ")
        if qty_input.isdigit():
            qty = int(qty_input)
            break
        print("❌ Please enter a valid number for quantity.")

    while True:
        try:
            buy_price = float(input("Enter your buy price per stock: "))
            break
        except:
            print("❌ Enter valid price (numbers only).")

    ticker = yf.Ticker(symbol)
    live_data = ticker.history(period="1d")

    if live_data.empty:
        print("⚠ Invalid symbol or no data found. Skipping...")
        continue

    current_price = live_data["Close"].iloc[0]

    invested = qty * buy_price
    current_val = qty * current_price
    profit = current_val - invested

    portfolio.append([symbol, qty, buy_price, current_price, invested, current_val, profit])

    stock_names.append(symbol)
    profits.append(profit)

    total_investment += invested
    total_current_value += current_val

total_profit = total_current_value - total_investment

print("\n================ LIVE Portfolio Summary ================")
print("Stock | Qty | Buy Price | Current Price | Invested | Current Value | P/L")

for item in portfolio:
    print(f"{item[0]}   {item[1]}   {item[2]}   {item[3]}   {item[4]}   {item[5]}   {item[6]}")

print("\n--------------------------------------------------------")
print("Total Invested Amount =", total_investment)
print("Total Current Value   =", total_current_value)
print("Net Profit / Loss     =", total_profit)

with open("advanced_stock_portfolio.txt", "w", encoding="utf-8") as f:
    f.write("Advanced Stock Portfolio Report (LIVE)\n")
    f.write("Generated on: " + str(datetime.datetime.now()) + "\n\n")
    for item in portfolio:
        f.write(f"{item[0]} Qty:{item[1]} Invested:{item[4]} Current:{item[5]} P/L:{item[6]}\n")
    f.write("\nTotal Invested = " + str(total_investment))
    f.write("\nTotal Current Value = " + str(total_current_value))
    f.write("\nNet Profit/Loss = " + str(total_profit))

with open("portfolio.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Stock", "Qty", "Buy Price", "LIVE Price", "Invested", "Current Value", "Profit/Loss"])
    writer.writerows(portfolio)

print("\n📁 Files saved: advanced_stock_portfolio.txt & portfolio.csv")
print("✅ Program completed successfully.")

