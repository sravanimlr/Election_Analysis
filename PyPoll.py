
# Add our dependencies
import csv
import os
#Assign a variable to load a file from a path.
file_to_load=os.path.join("election_results.csv")
#Assign a variable to save the file to a path.
file_to_save=os.path.join("analysis","election_analysis.txt")
#1. Initialize a total vote counter. 
total_votes= 0
#Candidate options
candidate_options=[]
#Declare the empty dictionary
candidate_votes={}
#Winning candidate and Winning Count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Open the election results and read the file. 
with open(file_to_load) as election_data:
    #To do: read and analyze the data here.
    # Read the file wit the reader function. 
    file_reader = csv.reader(election_data)
    #Read header row.
    headers = next(file_reader)
    #Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count. 
        total_votes += 1
        #Print cadidate name for each row 
        candidate_name = row[2]
        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #Add a vote to the candidates count
        candidate_votes[candidate_name] += 1

with open(file_to_save,"w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)    
    #Determine the percentage of votes for each candidate by looping through counts
    # Iterate through the candidate list.
    for candidate in candidate_votes:
        #Retrieve vote count of a candidate 
        votes = candidate_votes[candidate]
        #Calculate the percentage of votes
        vote_percentage= float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)    
        #Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning percent = vote_percentage 
            winning_count = votes
            winning_percentage = vote_percentage
            # And set the winning_candidate equal to the candidate's name
            winning_candidate = candidate
            
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
