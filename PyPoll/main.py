'''You will be given two sets of poll data (election_data_1.csv and election_data_2.csv). Each dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
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

mypath=os.path.join('Resources','test_poll.csv')

candidate=[]
poll={}

cnt1=0


with open(mypath,newline='') as csvfile:
	myreader=csv.reader(csvfile,delimiter=',')
#skipping the first row of headers in csv file
	next(myreader,None)
	#for comparison, setting first row of data as initialization
	for row in myreader:
		candidate.append(row[2])

#print(candidate)

myset=list(set(candidate))

#print(myset)
#print(candidate)
for x in range(len(myset)):
	#print(myset[x])
	for i in range(len(candidate)):
		print(candidate[i])
		if (myset[x])== candidate[i]:
			cnt1+=1
	poll[myset[x]=cnt1
	cnt1=0

print(poll)