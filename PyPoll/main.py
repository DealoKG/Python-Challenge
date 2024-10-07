import os
import csv

# Define the path to csv file
election_path = os.path.join("/Users/lordfranko/Desktop/Class_Repo/python-challenge/PyPoll/Resources/election_data.csv")

# Initialize variables
tvotes = 0
canvotes = {}
winner = ""
win_votes = 0

# Open csv file
with open(election_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row 
    csv_header = next(csvreader)

    # Iterate through the rows in the csv file
    for row in csvreader:
        tvotes += 1
        candidate = row[2]

        if candidate in canvotes:
            canvotes[candidate] += 1
        else:
            canvotes[candidate] = 1

# Print the Results to terminal
print("Election Results")
print("-----------------------")
print(f"Total Votes: {tvotes}")
print("-----------------------")

for candidate, votes in canvotes.items():
    print(f"{candidate}: {votes/tvotes:.3%} ({votes})")
    if votes > win_votes:
        winner = candidate
        win_votes = votes
print("-----------------------")
print(f"Winner: {winner}")
print("-----------------------")

# Print results to file
output_path = "/Users/lordfranko/Desktop/Class_Repo/python-challenge/PyPoll/analysis/election_analysis.csv"
with open(output_path, "w", newline="") as output:
    outputwriter = csv.writer(output, delimiter=",")
    outputwriter.writerow(["Candidate", "Percentage", "Votes"])
    for candidate, votes in canvotes.items():
        outputwriter.writerow([candidate, f"{votes/tvotes:.3%}", votes])
    outputwriter.writerow(["Winner", winner])