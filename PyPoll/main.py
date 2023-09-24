import os
import csv

# Document Path
csvpath = os.path.join(r"C:\Users\Simon\Desktop\Data Bootcamp\MONU-VIRT-DATA-PT-08-2023-U-LOLC\02-Homework\03-Python\Starter_Code\Python-Challenge\PyPoll\Resources\election_data.csv")

# Initialising Variables
candidate_votes = {}
total_votes = 0

# Read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header row
    next(csvreader)

    #Loop through csv
    for row in csvreader:

        # Extracts candidate's name from third column
        candidate = row[2]
        
        # Checks for candidates name
        if candidate in candidate_votes:
            # Adds candidate vote if name exists
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            # Adds candidate name if does not exist
            candidate_votes[candidate] = 1
        
        # Total vote counter
        total_votes = total_votes + 1

# Calculate the percentage of votes each candidate won
percentage_votes = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Find the winner 
winner = max(candidate_votes, key=candidate_votes.get)

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes_received in candidate_votes.items():
    print(f"{candidate}: {percentage_votes[candidate]:.2f}% ({votes_received})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")