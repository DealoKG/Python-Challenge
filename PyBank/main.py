# Dependencies
import os
import csv

#Path to the csv file
budget = os.path.join("/Users/lordfranko/Desktop/Class_Repo/python-challenge/PyBank/Resources/budget_data.csv")

#Iniialize the variables
tmonths = 0
tprofl = 0
inchanprof = 0
chanprofl = []
ginc =  ["", 0]
gdec = ["", 0]

#Open the csv file
with open(budget, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read the header row 
    csv_header = next(csvreader)

    #Iterate through the rows in the csv file
    for budget in csvreader:
        tmonths = tmonths + 1
        tprofl = tprofl + int(budget[1])

        change = int(budget[1]) - inchanprof

        inchanprof = int(budget[1])
        chanprofl.append(change)

    #Calculate the greatest increase in profits
        if change > ginc[1]:
            ginc[0] = budget[0]
            ginc[1] = change

    #Calculate the greatest decrease in profits
        if change < gdec[1]:
            gdec[0] = budget[0]
            gdec[1] = change

#Calculate the average change in profits
average = sum(chanprofl[1:]) / (tmonths - 1)

#Print the analysis to terminal
print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {tmonths}")
print(f"Total: ${tprofl}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {ginc[0]} (${ginc[1]})")
print(f"Greatest Decrease in Profits: {gdec[0]} (${gdec[1]})")

#Print to the file 
with open("/Users/lordfranko/Desktop/Class_Repo/python-challenge/PyBank/analysis/budget_analysis.csv", "w", newline="") as output:

    outputwriter = csv.writer(output, delimiter=",")

    outputwriter.writerow(["Financial Analysis"])   
    outputwriter.writerow(["-----------------------"])  
    outputwriter.writerow([f"Total Months: {tmonths}"])
    outputwriter.writerow([f"Total: ${tprofl}"])
    outputwriter.writerow([f"Average Change: ${average}"])
    outputwriter.writerow([f"Greatest Increase in Profits: {ginc[0]} (${ginc[1]})"])
    outputwriter.writerow([f"Greatest Decrease in Profits: {gdec[0]} (${gdec[1]})"])





