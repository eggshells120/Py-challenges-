import csv

# Define the input file and output file names
input_file = "election_data.csv"
output_file = "election_results.txt"

# Initialize variables to store the election data
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file and calculate the election values
with open(input_file, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row

    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidates:
            candidates[candidate_name] = 0
        candidates[candidate_name] += 1

# Calculate the election results
results = []
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, percentage, votes))

# Find the winner
for candidate, votes in candidates.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Print the election results to the terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
for candidate, percentage, votes in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

# Export the election results to a text file
with open(output_file, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("----------------------------\n")
    for candidate, percentage, votes in results:
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("----------------------------\n")

# Print a confirmation message
print(f"Results exported to {output_file}")
