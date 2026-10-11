# CodeAlpha Internship - Task 2
# Project: Stock Portfolio Tracker

def stock_portfolio_tracker():
    # Predefined stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 170,
        "MSFT": 420,
        "AMZN": 190
    }

    portfolio = []
    total_investment = 0

    print("=" * 45)
    print("       STOCK PORTFOLIO TRACKER")
    print("=" * 45)

    print("\nAvailable Stocks and Prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price:.2f} per share")

    print("\nEnter the stock details below.")
    print("Type 'done' when you finish adding stocks.")

    while True:
        stock_name = input("\nEnter stock symbol: ").strip().upper()

        if stock_name == "DONE":
            break

        if stock_name not in stock_prices:
            print("Invalid stock symbol. Please choose from the available stocks.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock_name}: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

        except ValueError:
            print("Invalid quantity. Please enter a whole number.")
            continue

        price = stock_prices[stock_name]
        investment = price * quantity

        portfolio.append({
            "stock": stock_name,
            "quantity": quantity,
            "price": price,
            "investment": investment
        })

        total_investment += investment

        print(f"{stock_name} added successfully!")
        print(f"Investment in {stock_name}: ${investment:,.2f}")

    print("\n" + "=" * 55)
    print("                 PORTFOLIO SUMMARY")
    print("=" * 55)

    if not portfolio:
        print("No stocks were added to your portfolio.")
    else:
        print(f"{'Stock':<10}{'Quantity':<12}{'Price ($)':<14}{'Total ($)':<14}")
        print("-" * 50)

        for item in portfolio:
            print(
                f"{item['stock']:<10}"
                f"{item['quantity']:<12}"
                f"{item['price']:<14.2f}"
                f"{item['investment']:<14.2f}"
            )

        print("-" * 50)
        print(f"Total Investment: ${total_investment:,.2f}")

        save_choice = input("\nSave portfolio to a text file? (yes/no): ").strip().lower()

        if save_choice == "yes":
            try:
                with open("stock_portfolio.txt", "w", encoding="utf-8") as file:
                    file.write("STOCK PORTFOLIO TRACKER\n")
                    file.write("=" * 45 + "\n")
                    file.write(
                        f"{'Stock':<10}{'Quantity':<12}"
                        f"{'Price ($)':<14}{'Total ($)':<14}\n"
                    )
                    file.write("-" * 50 + "\n")

                    for item in portfolio:
                        file.write(
                            f"{item['stock']:<10}"
                            f"{item['quantity']:<12}"
                            f"{item['price']:<14.2f}"
                            f"{item['investment']:<14.2f}\n"
                        )

                    file.write("-" * 50 + "\n")
                    file.write(
                        f"Total Investment: ${total_investment:,.2f}\n"
                    )

                print("Portfolio saved successfully to stock_portfolio.txt!")

            except OSError as error:
                print(f"Error saving portfolio: {error}")

    print("\nThank you for using Stock Portfolio Tracker!")


if __name__ == "__main__":
    stock_portfolio_tracker()