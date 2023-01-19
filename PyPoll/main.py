#import modules
import os
import csv

#path for file
file_to_load=os.path.join("..", "Resources", "election_data.csv")

#output files
file_to_output = os.path.join("Election_Results.txt")

#set output of text file
text_path="output.txt"

#lists to store data
cand_total = []
cand_names = []

#open cvs file
with open (file_to_load) as election_data:
    reader= csv.reader(election_data)

    #read header row
    header=next(reader)
    #loop through total votes
    for row in reader:
        #count total number of votes
        cand_total.append(row[2])
        vote_total=len(cand_total)

#list of candidates
cand_set = set(cand_total)
cand_names = sorted(list(cand_set))

# total votes/percentage for candidates
cand0_total = cand_total.count(cand_names[0])
cand0_percent = round(cand0_total / vote_total * 100, 3)

cand1_total = cand_total.count(cand_names[1])
cand1_percent = round(cand1_total / vote_total * 100, 3)

cand2_total = cand_total.count(cand_names[2])
cand2_percent = round(cand2_total / vote_total * 100, 3)

#find winner
import statistics
winner = statistics.mode(cand_total)

#print out election results
print("Election Results")
print("----------------------------------------------------")
print(f"Total Ballots Cast: {vote_total}")
print("----------------------------------------------------")
print(f"{cand_names[0]}: {cand0_percent}% ({cand0_total})")
print(f"{cand_names[1]}: {cand1_percent}% ({cand1_total})")
print(f"{cand_names[2]}: {cand2_percent}% ({cand2_total})")
print("----------------------------------------------------")
print(f"Winner: {winner}")
print("----------------------------------------------------")

#write methods to print out to Election_Results
with open(file_to_output, 'w') as file:
    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------------------------------")
    file.write("\n")
    file.write(f"Total Ballots Cast: {vote_total}")
    file.write("\n")
    file.write("----------------------------------------------------")
    file.write("\n")
    file.write(f"{cand_names[0]}: {cand0_percent}% ({cand0_total})")
    file.write("\n")
    file.write(f"{cand_names[1]}: {cand1_percent}% ({cand1_total})")
    file.write("\n")
    file.write(f"{cand_names[2]}: {cand2_percent}% ({cand2_total})")
    file.write("\n")
    file.write("----------------------------------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
