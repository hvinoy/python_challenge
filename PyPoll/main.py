import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

votes = [] #stores all the name of people who voted
candidates = [] #stores all the votes people casted
k = int(0) #vote counts for khan
c = int(0) #vote counts for Correy
l = int(0) #vote counts for Li
o = int(0) #vote counts for O'tooley

with open(election_csv,'r') as csvfile:
    election_info = csv.reader(csvfile, delimiter=",")

    csv_header = next(election_info)

    for row in election_info:
        votes.append(row[0])
        candidates.append(row[2])

    for name in candidates:
        if "Khan" == name:
            k = k + 1
            
        elif "Correy" == name:
            c = c + 1
            
        elif "Li" == name:
            l = l + 1
            
        else:
            o = o + 1
           


#---------------------------------------------
Total_votes = len(votes)
k_per = (k/Total_votes)*100
c_per = (c/Total_votes)*100
l_per = (l/Total_votes)*100
o_per = (o/Total_votes)*100
#-------------------------------------------------
cand_votes = [] #percentage votes for each candidate
cand_votes.append(k_per)
cand_votes.append(c_per)
cand_votes.append(l_per)
cand_votes.append(o_per)
winners = ["Khan", "Correy","Li","O'Tooley"]
#print(f"{cand_votes}")

max = max(cand_votes) #finds corresponding index
number_1 = cand_votes.index(max)



print("Election Results")
print("-------------------------")
print(f"Total Votes: {Total_votes}")
print("-------------------------")
print(f"Khan: {'{:.3f}'.format(k_per)}% ({k})")
print(f"Correy: {'{:.3f}'.format(c_per)}% ({c})")
print(f"Li: {'{:.3f}'.format(l_per)}% ({l})")
print(f"O'Tooley: {'{:.3f}'.format(o_per)}% ({o})")
print("-------------------------")
print(f"Winner: {winners[number_1]}")
print("-------------------------")



# Specify the file to write to
output_path = os.path.join("Analysis","poll.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=' ')

     # Write the first row
    csvwriter.writerow(["Election Results"])

    csvwriter.writerow("-------------------------")
    csvwriter.writerow([f"Total Votes: {Total_votes}"])
    csvwriter.writerow("-------------------------")
    csvwriter.writerow([f"Khan: {'{:.3f}'.format(k_per)}% ({k})"])
    csvwriter.writerow([f"Correy: {'{:.3f}'.format(c_per)}% ({c})"])
    csvwriter.writerow([f"Li: {'{:.3f}'.format(l_per)}% ({l})"])
    csvwriter.writerow([f"O'Tooley: {'{:.3f}'.format(o_per)}% ({o})"])
    csvwriter.writerow("-------------------------")
    csvwriter.writerow([f"Winner: {winners[number_1]}"])
    csvwriter.writerow("-------------------------")
    
  