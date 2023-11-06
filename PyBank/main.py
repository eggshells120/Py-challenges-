import pandas as pd


df = pd.read_csv("New Text Document.txt")

# Calculate the total number of months
total_months = len(df)

# Calculate the net total amount of profit/loss
net_total = df["Profit/Losses"].sum()

# Calculate the change in profit/loss from the previous month and store it in a new column
df["Profit/Loss Change"] = df["Profit/Losses"].diff()

# Calculate the average change
average_change = df["Profit/Loss Change"].mean()

# Find the row with the greatest increase and decrease in profits
greatest_increase = df[df["Profit/Loss Change"] == df["Profit/Loss Change"].max()]
greatest_decrease = df[df["Profit/Loss Change"] == df["Profit/Loss Change"].min()]

# Extract the date and amount of the greatest increase and decrease
greatest_increase_date = greatest_increase["Date"].values[0]
greatest_increase_amount = greatest_increase["Profit/Loss Change"].values[0]
greatest_decrease_date = greatest_decrease["Date"].values[0]
greatest_decrease_amount = greatest_decrease["Profit/Loss Change"].values[0]

# Print the financial analysis
print("Financial Analysis")
print("---------------------------- \n")
print(f"Total Months: {total_months} \n")
print(f"Total: ${net_total} \n")
print(f"Average Change: ${average_change:.2f} \n")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount:.0f}) \n")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount:.0f})")


