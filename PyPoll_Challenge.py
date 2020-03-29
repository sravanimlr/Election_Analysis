
# Add our dependencies
import csv
import os
#Assign a variable to load a file from a path.
file_to_load=os.path.join("election_results.csv")
#Assign a variable to save the file to a path.
file_to_save=os.path.join("analysis","election_analysis.txt")

#1. Initialize a total vote counter. 
total_votes= 0

# Create list for counties  
counties= []

#Create a dictionary where county is key and votes in value
county_votes={}

#Create and empty string for county name with the largest turnout 
county_name= ""

#Candidate options
candidate_options=[]

#Declare the empty dictionary
candidate_votes={}

#Declare largest turnout county
largest_turnout_county = ""
largest_turnout_percentage = 0

#Winning candidate and Winning Count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader= csv.reader(election_data)
    headers = next(file_reader)

    for row in file_reader:
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

        county_name = row[1]
        #If statement to check if county name is recorded,if not add it to the list 
        if county_name not in counties:
            counties.append(county_name)

            county_votes[county_name]  = 0

        county_votes[county_name] += 1

with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #Determine percentage for county votes 
    for county_name in county_votes:
        votes= county_votes[county_name]
        vote_percentage= float(votes) / float(total_votes) * 100
        county_results_summary = (
            f"{county_name}: {vote_percentage:.1f}% ({votes})\n")
        print(county_results_summary)
        txt_file.write(county_results_summary)

        #Determine largest turnout for county
        if (vote_percentage > largest_turnout_percentage):
            largest_turnout_percentage = vote_percentage
            largest_turnout_county= county_name
    
    largest_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_turnout_county}\n"
        f"-------------------------\n")
    print(largest_county_summary)
    txt_file.write(largest_county_summary)

    
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

    
 





       