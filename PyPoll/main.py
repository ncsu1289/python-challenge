'''You will be given two sets of poll data (election_data_1.csv and election_data_2.csv). 
Each dataset is composed of three columns: Voter ID, County, and Candidate. 
Your task is to create a Python script that analyzes the votes and calculates each of the 
following:
The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote.
As an example, your analysis should look similar to the one below:
Election Results
-------------------------
Total Votes: 620100
-------------------------
Rogers: 36.0% (223236)
Gomez: 54.0% (334854)
Brentwood: 4.0% (24804)
Higgins: 6.0% (37206)
-------------------------
Winner: Gomez
-------------------------'''
import os
import csv

# went through code with test csv first mypath=os.path.join('../Resources','test_poll.csv')
#two csv polling files were not provided.  Would use the join script used in PyBank to combine
#two polling files if provided.

mypath=os.path.join('../Resources','election_data_2.csv')


candidate=[]
poll={}
stat_poll={}
tot_vote=0
cnt1=0
cnt2=0
winner=""
out_strng={}

with open(mypath,newline='') as csvfile:
	myreader=csv.reader(csvfile,delimiter=',')
#skipping the first row of headers in csv file
	next(myreader,None)
	#for comparison, setting first row of data as initialization
	for row in myreader:
		tot_vote+=1
		candidate.append(row[2])

#print(candidate)

myset=list(set(candidate))

#print(myset)
#print(candidate)
for x in range(len(myset)):
	#print(myset[x])
	for i in range(len(candidate)):
		#print(candidate[i])
		if (myset[x])== candidate[i]:
			cnt1+=1
	poll[myset[x]]=cnt1
	stat_poll[myset[x]]=(cnt1/float(tot_vote))*100
	cnt1=0

#print(poll)
#print results to screen
print(" \n")
print("Election Results\n")
print("-------------------------\n")
print("Total Votes: "+ str(tot_vote)+"\n")
print("-------------------------\n")
for q in (poll):
	#print(q)
	for b in (stat_poll):
		#print(b)
		if q == b:
			#print(q +": "+ str(stat_poll[b])+"% ("+str(poll[q])+")\n")
			print(q +": "+ ("%.1f" %int(stat_poll[b]))+"% ("+str(poll[q])+")\n")
			if stat_poll[b]> cnt2:
				cnt2=stat_poll[b]
				winner=b
#print("%.1f" %int(stat_poll[b]))
#Rogers: 36.0% (223236)
#Gomez: 54.0% (334854)
#Brentwood: 4.0% (24804)
#Higgins: 6.0% (37206)
print("-------------------------\n")
print("Winner: "+ winner+"\n")
print("-------------------------\n")

with open("PyPoll_output.txt","w") as text_file:
	text_file.write("Election Results\n")
	text_file.write("-------------------------\n")
	text_file.write("Total Votes: "+ str(tot_vote)+"\n")
	text_file.write("-------------------------\n")
	for q in (poll):
		for b in (stat_poll):
			if q == b:
				text_file.write(q +": "+ ("%.1f" %int(stat_poll[b]))+"% ("+str(poll[q])+")\n")
	text_file.write("-------------------------\n")
	text_file.write("Winner: "+ winner+"\n")
	text_file.write("-------------------------\n")
