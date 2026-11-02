"""Beginner-friendly stock portfolio tracker using example prices."""

import csv
from datetime import datetime
from pathlib import Path

# Example prices for the assignment only; these are not live market prices.
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 420.00,
    "AMZN": 175.00,
}


def get_quantity(symbol):
    """Ask for a positive whole-number quantity, or zero to skip the stock."""
    while True:
        raw = input(f"How many shares of {symbol}? (0 to skip): ").strip()
        try:
            quantity = int(raw)
            if quantity < 0:
                print("Please enter zero or a positive whole number.")
                continue
            return quantity
        except ValueError:
            print("Please enter a whole number, such as 3.")


def save_report(holdings, total):
    """Save the calculated portfolio to a timestamped CSV file."""
    filename = Path(f"portfolio_{datetime.now():%Y%m%d_%H%M%S}.csv")
    with filename.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Stock", "Shares", "Example price per share", "Holding value"])
        for symbol, quantity in holdings.items():
            price = STOCK_PRICES[symbol]
            writer.writerow([symbol, quantity, f"{price:.2f}", f"{price * quantity:.2f}"])
        writer.writerow(["TOTAL", "", "", f"{total:.2f}"])
    return filename


def main():
    print("Stock Portfolio Tracker")
    print("Enter the shares you own for each stock. Prices are fixed example values.\n")

    holdings = {}
    total = 0.0

    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol}: ${price:,.2f} per share")
        quantity = get_quantity(symbol)
        if quantity > 0:
            holdings[symbol] = quantity
            value = quantity * price
            total += value
            print(f"  Holding value: ${value:,.2f}\n")
        else:
            print()

    print("Portfolio Summary")
    if not holdings:
        print("No shares entered.")
    else:
        for symbol, quantity in holdings.items():
            value = quantity * STOCK_PRICES[symbol]
            print(f"{symbol}: {quantity} shares x ${STOCK_PRICES[symbol]:,.2f} = ${value:,.2f}")
    print(f"Total investment value: ${total:,.2f}")

    if holdings:
        answer = input("Save this summary as a CSV file? (y/n): ").strip().lower()
        if answer == "y":
            filename = save_report(holdings, total)
            print(f"Report saved as: {filename}")


if __name__ == "__main__":
    main()
