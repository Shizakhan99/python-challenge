import csv
# \Resources\budget_data.csv
# Read the budget data from the CSV file


with open('PyBank/Resources/budget_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    months = []
    profit_losses = []
    changes = []

    for row in reader:
        months.append(row[0])
        profit_losses.append(int(row[1]))

# Calculate the total number of months
total_months = len(months)

# Calculate the net total amount of profit/losses
net_total = sum(profit_losses)

# Calculate the changes in profit/losses and store them in a list
for i in range(1, total_months):
    change = profit_losses[i] - profit_losses[i-1]
    changes.append(change)

# Calculate the average change
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_increase_date = months[changes.index(greatest_increase) + 1]
greatest_decrease = min(changes)
greatest_decrease_date = months[changes.index(greatest_decrease) + 1]


# Print the analysis results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

#Exporing to .txt file
# output = open("output.txt", "w")

# output.write("Financial analysis")

# output.write("-----------------------------")
# output.write(f"Total Months: {total_months}")
# output.write(f"Total: ${net_total}")
# output.write(f"Average Change: ${average_change:.2f}")
# output.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
# output.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
        
# file.close()
with open('financial_analysis.txt', 'w') as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("-----------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${net_total}\n")
    text_file.write(f"Average Change: ${average_change:.2f}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    text_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
    