import os
import csv

# Document Path
csvpath = os.path.join(r"C:\Users\Simon\Desktop\Data Bootcamp\MONU-VIRT-DATA-PT-08-2023-U-LOLC\02-Homework\03-Python\Starter_Code\Python-Challenge\PyBank\Resources\budget_data.csv")

# Initialise Variables
total_months = 0
total_profit = 0
net_change = 0
greatest_profit = float("-inf")
greatest_profit_date = ""
greatest_loss = float("inf")
greatest_loss_date = ""
last_profit = None

# Open and read file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip reading headers
    next(csvreader)

    # Loop through rows
    for row in csvreader:
        date, profit_loss = row
        profit_loss = int(profit_loss)

        # Count of Months
        total_months = total_months + 1

        # Total Profit/loss
        total_profit = total_profit + profit_loss

        if last_profit is not None:

            # Calculate monthly change in profit
            change = profit_loss - last_profit
            net_change = net_change + change

            # Find Greatest profit
            if change > greatest_profit:
                greatest_profit = change
                greatest_profit_date = date

            # Find Greatest loss
            if change < greatest_loss:
                greatest_loss = change
                greatest_loss_date = date

        # Update Vairable for next 
        last_profit = profit_loss

# Calculate the average change
average_change = net_change / (total_months - 1)

print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Net Total Profit: ${total_profit}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Profit: {greatest_profit_date} - ${greatest_profit}")
print(f"Greatest Loss: {greatest_loss_date} - ${greatest_loss}")
