import os
import csv

# Define the path of the csv file
election_csv = os.path.join("/Users/lordfranko/Desktop/PythonChallenge3/Python-Challenge/PyPoll/Resources/election_data.csv")

#Initialize the variables

vote_result = 0
can_votes = {}
winner = ""
winner_votes = 0

#Open the csv file
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    
    #read the header riw first
    csv_header = next(csvreader)
    


    # Iterate over the csv reader object
    for data in csvreader:
        vote_result += 1
        
        can_name = data[2]
        
        if can_name not in can_votes:
            can_votes[can_name] = 0
        can_votes[can_name] += 1

# Print the election results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote_result}")
print("-------------------------")
for candidate, votes in can_votes.items():
    percentage = (votes / vote_result) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# Write results to CSV file
with open("/Users/lordfranko/Desktop/PythonChallenge3/Python-Challenge/PyPoll/analysis/election_analysis.csv", "w", newline="") as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=",")
    
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow([f"Total Votes: {vote_result}"])
    for candidate, votes in can_votes.items():
        percentage = (votes / vote_result) * 100
        csvwriter.writerow([f"{candidate}: {percentage:.3f}% ({votes})"])
    csvwriter.writerow([f"Winner: {winner}"])

    
# Print the local path for user to find file
 
print(f"Results exported to the local file located in  '/Users/lordfranko/Desktop/PythonChallenge3/Python-Challenge/PyPoll/analysis/election_analysis.csv'.")


