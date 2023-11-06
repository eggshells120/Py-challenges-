import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("election_data.csv")

# Calculate the total number of votes cast
total_votes = len(df)

# Create a DataFrame with candidate names and their respective vote counts
candidate_counts = df["Candidate"].value_counts().reset_index()
candidate_counts.columns = ["Candidate", "Vote Count"]

# Calculate the percentage of votes each candidate won
candidate_counts["Percentage"] = (candidate_counts["Vote Count"] / total_votes) * 100

# Find the winner based on the popular vote
winner = candidate_counts.iloc[candidate_counts["Vote Count"].idxmax()]

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for index, row in candidate_counts.iterrows():
    print(f"{row['Candidate']}: {row['Percentage']:.3f}% ({row['Vote Count']})")
print("-------------------------")
print(f"Winner: {winner['Candidate']}")
print("-------------------------")

# Export the results to a text file
with open("election_results.txt", "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-------------------------\n")
    for index, row in candidate_counts.iterrows():
        textfile.write(f"{row['Candidate']}: {row['Percentage']:.3f}% ({row['Vote Count']})\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Winner: {winner['Candidate']}\n")
    textfile.write("-------------------------")


