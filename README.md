# Stock Portfolio Tracker

A simple Python program for Task 2. It asks for the number of shares held in each listed stock, calculates each holding and the total using manually defined example prices, and can save a CSV report. It does not fetch live stock prices and requires no extra packages.

## Run it on Windows

1. Install Python 3 from [python.org](https://www.python.org/downloads/) if needed. Select **Add Python to PATH** during installation.
2. Extract the project ZIP to a folder you can find.
3. Open the extracted `stock_portfolio_tracker` folder in Visual Studio Code (**File → Open Folder**).
4. Select **Terminal → New Terminal**.
5. Run:

   ```powershell
   python stock_tracker.py
   ```

   If `python` is not recognized, try `py stock_tracker.py`.

6. Enter whole-number share quantities for each stock, or enter `0` to skip. The program displays holding values and the total. Enter `y` at the save prompt to create a CSV report in the same folder.

## Included example prices

The program uses fixed example prices: AAPL $180, TSLA $250, GOOGL $140, MSFT $420, and AMZN $175 per share. They are for demonstrating the calculation only, not live prices or financial advice. You can change them in `STOCK_PRICES` near the top of `stock_tracker.py`.

## Upload to GitHub

1. Sign in to [GitHub](https://github.com) and create a new repository named `CodeAlpha_StockPortfolioTracker` (or use the exact naming format required by your internship).
2. Open this extracted project folder in VS Code and choose **Terminal → New Terminal**.
3. Run these commands one by one. Replace `YOUR-USERNAME` with your GitHub username and use the repository URL shown by GitHub if you chose a different name.

   ```powershell
   git init
   git add stock_tracker.py README.md
   git commit -m "Add stock portfolio tracker"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/CodeAlpha_StockPortfolioTracker.git
   git push -u origin main
   ```

4. If Git requests authentication, complete the browser sign-in. Refresh the repository page and confirm `stock_tracker.py` and `README.md` appear. Copy that repository URL for the submission form.

If Git is not recognized, install Git for Windows, restart VS Code, and retry. If Git says a remote named `origin` already exists, use `git remote set-url origin https://github.com/YOUR-USERNAME/CodeAlpha_StockPortfolioTracker.git` and then run the push command.
