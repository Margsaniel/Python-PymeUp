import csv, os

file_to_load = os.path.join("Resources/election_data.csv")

votes_count = 0
winning_count = 0

candidates = []
candidate_winner = ""
winning_count = 0
votes_for_candidates = {}

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as poll_data:
    reader = csv.reader(poll_data)
    remove_header = next(reader)

    for row in reader:
        print(". ", end=""),
        votes_count = votes_count + 1
        candidate_name = row[2]

        if candidate_name not in candidates:

            candidates.append(candidate_name)
            votes_for_candidates[candidate_name] = 0
            
        votes_for_candidates[candidate_name] = votes_for_candidates[candidate_name] + 1

        
    results = (       
    f"\n\nElection Results\n"
    f"--------\n"
    f"Total Votes: {votes_count}\n"
    f"--------\n")

    print(results)


    for candidate in votes_for_candidates:
        votes = votes_for_candidates.get(candidate)
        vote_percentage = float(votes) / float(votes_count) * 100

        if (votes > winning_count):
            winning_count = votes
            candidate_winner = candidate

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")
        
        
winning_candidate_summary = (
    f"--------\n"
    f"Winner: {candidate_winner}\n"
    f"--------\n")

print(winning_candidate_summary)
