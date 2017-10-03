'''The average change in revenue between months over the entire period
The greatest increase in revenue (date and amount) over the entire period
The greatest decrease in revenue (date and amount) over the entire period'''

#first step is to initialize and open csv data file
import os
import csv

mypath=os.path.join('Resources','budget_data_1.csv')

#need a variable counter to keep track of revenue overall
total_revenue = 0
#need a counter to keep track of the number of months
months=0

comp=0
compI =0
compD=0
#creating a list to store each monthly change in revenue
change=[]
#need initial values for the first row date and revenue
prev_row_rev=0
prev_row_date=""
#need a dictionary and variable to keep track of greatest increase date and revenue
greatest_inc={}
greatI=0

#need a dictionary and variable to keep track of greatest decrease date and revenue
greatest_dec={}
greatD=0
#setting a variable to insure that the first row of information is stored into initial variables
count1=1

with open(mypath,newline='') as csvfile:
	myreader=csv.reader(csvfile,delimiter=',')
#skipping the first row of headers in csv file
	next(myreader,None)
	#for comparison, setting first row of data as initialization
	for row in myreader:
		months+=1
		total_revenue+=int(row[1])
		if count1==1:
			prev_row_rev=int(row[1])
			greatest_inc[row[0]]=int(row[1])
			greatest_dec[row[0]]=int(row[1])
			count1+=1
			#print(count1)
		elif int(row[1])>prev_row_rev:
			if (int(row[1])> 0 and prev_row_rev>0) or (int(row[1])<0 and prev_row_rev<0):
				compI=abs(abs(int(row[1]))- abs(prev_row_rev))
				change.append(compI)
			else:
				compI=abs(abs(int(row[1]))+abs(prev_row_rev))
				change.append(compI)
			if compI>greatI:
				greatI=compI
				greatest_inc={}
				greatest_inc[row[0]]=(row[1])

		else:
			if (int(row[1])> 0 and prev_row_rev>0) or (int(row[1])<0 and prev_row_rev<0):
				compD=abs(abs(int(row[1]))- abs(prev_row_rev))
				change.append(compD)
			else:
				compD=abs(abs(int(row[1]))+abs(prev_row_rev))
				change.append(compD)
			if compD>greatD:
				greatD=compD
				greatest_dec={}
				greatest_dec[row[0]]=row[1]

print(change)

#Average change we should now be able to take the change list, sum all values and divide by length
#	to obtain the average change between the months
sum1=0		
for i in (change):
	sum1+=float(i)
avg_change = sum1/(len(change))


print(inc_month, inc_amount)

print("Financial Analysis")
print("----------------------------")
print("Total Months: "+ str(months))
print("Total Revenue: $"+ str(total_revenue))
print("Average Revenue Change: $" + str(avg_change))
print("Greatest Increase in Revenue: "+ str(greatest_inc))
print("Greatest Decrease in Revenue: "+ str(greatest_dec))
print("---------------------------")