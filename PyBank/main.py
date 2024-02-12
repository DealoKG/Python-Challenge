import os
import csv

# Define the path of the csv file
budget_csv = os.path.join("/Users/lordfranko/Desktop/PythonChallenge3/Python-Challenge/PyBank/Resources/budget_data.csv")

#Initialize the variables

tot_months = 0
tot_prof_loss = 0
ini_change_prof = 0
change_prof_loss = []
greatest_inc = ["", 0]
greatest_dec = ["", 0]

#Open the csv file
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    
    #read the header riw first
    csv_header = next(csvreader)

     # Iterate over the csv reader object
    for budget in csvreader:
        tot_months += 1
        tot_prof_loss += int(budget[1])
        
        change = int(budget[1]) - ini_change_prof
        
        ini_change_prof = int(budget[1])
        change_prof_loss.append(change)
        
     # Calculate the greatest increase in profits
        if change > greatest_inc[1]:
            greatest_inc[0] = budget[0]
            greatest_inc[1] = change

        # Calculate the greatest decrease in profits
        if change < greatest_dec[1]:
            greatest_dec[0] = budget[0]
            greatest_dec[1] = change

  
# Calculate the average change in profit/losses
average_change = sum(change_prof_loss[1:]) / (tot_months - 1)


# Print the financial analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {tot_months}")
print(f"Total: ${tot_prof_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})")
print(f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})")



# Write results to CSV file
with open("/Users/lordfranko/Desktop/PythonChallenge3/Python-Challenge/PyBank/analysis/budget_analysis.csv", "w", newline="") as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=",")
    
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow([f"Total Months: {tot_months}"])
    csvwriter.writerow([f"Total: ${tot_prof_loss}"])
    csvwriter.writerow([f"Average Change: ${average_change:.2f}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})"])


# Print the local path for user to find file
print(f"Results exported to the local file located in '/Users/lordfranko/Desktop/PythonChallenge3/Python-Challenge/PyBank/analysis/budget_analysis.csv'.")


