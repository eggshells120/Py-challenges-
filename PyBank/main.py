import csv

# Define the input file and output file names
input_file = "New Text Document.txt"
output_file = "financial_analysis.txt"

# Initialize variables to store the financial data
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_loss_changes = []
months = []

# Read the CSV file and calculate the financial values
with open(input_file, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row

    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        total_months += 1
        net_total += profit_loss

        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)
            months.append(date)

        previous_profit_loss = profit_loss

# Calculate the average change in profit/loss
average_change = sum(profit_loss_changes) / (total_months - 1)

# Find the greatest increase and decrease in profit
greatest_increase = max(profit_loss_changes)
greatest_decrease = min(profit_loss_changes)

# Find the corresponding months for the greatest increase and decrease
greatest_increase_month = months[profit_loss_changes.index(greatest_increase)]
greatest_decrease_month = months[profit_loss_changes.index(greatest_decrease)]

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Export the analysis to a text file
with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

# Print a confirmation message
print(f"Results exported to {output_file}")
