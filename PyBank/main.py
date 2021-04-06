import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")
months = [] #stores all the months
total = int(0)
profit = [] #stores all the profits/losses
change = [] #change between each month
total_change = int(0)
with open(budget_csv,'r') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")

    csv_header = next(budget_data)
    #print(f"CSV Header: {csv_header}")

    for row in budget_data:
        months.append(row[0])
        profit.append(int(row[1]))
        total = total + int(row[1])
        

for x in range(len(profit)-1):
    difference = profit[x + 1] - profit[x]    
    change.append(difference)

for x in range(len(change)):  #average of change between months
    total_change = total_change + change[x]  #finds total of the change between months
    length = len(change)
    average = round(float(total_change/(length)),2)



total_months = len(months)

max = max(change)
min = min(change)

#finds the corresponding month for max and min change
max_month = change.index(max) + 1
min_month = change.index(min) + 1
#print(max_month)
#print(months)
#print(profit)
#print(change)

#print(len(profit))
#print(len(change))
#print(months[25])
#print(change.index(max))

#----------------------------------------------
#output
print("Financial Analysis")
print("-------------------------")

print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change:  ${average}")
print(f"Greatest Increase in Profits: {months[max_month]} (${max})")
print(f"Greatest Decrease in Profits: {months[min_month]} (${min})")



# Specify the file to write to
output_path = os.path.join("Analysis", "bank.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=' ')

    # Write the first row
    csvwriter.writerow(["Financial Analysis"])

    # Write the second row
    csvwriter.writerow("-------------------------")
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Total: ${total}"])
    csvwriter.writerow([f"Average Change:  ${average}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {months[max_month]} (${max})"])
    csvwriter.writerow([(f"Greatest Decrease in Profits: {months[min_month]} (${min})")])
