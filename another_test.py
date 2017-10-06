

import os
import csv
mypath=os.path.join('Resources','budget_data_1.csv')

path2=os.path.join('Resources','budget_data_2.csv')

budgetnew=[]

with open(mypath,newline='') as csvfile:
	myreader=csv.reader(csvfile,delimiter=',')
#skipping the first row of headers in csv file
	next(myreader,None)
	for row in myreader:
		budgetnew.append(row)

#print(budgetnew)

with open(path2,newline='')as csvfile:
	mynewreader=csv.reader(csvfile,delimiter=',')
	next(mynewreader,None)
	for addrow in mynewreader:
		budgetnew.append(addrow)

#print(budgetnew)

output_path=os.path.join('output','new.csv')

with open(output_path,'w',newline='')as csvfile:
	csvwriter=csv.writer(csvfile,delimiter=",")
	csvwriter.writerow(['Date','Revenue'])
	for z in budgetnew:
		csvwriter.writerow(z)
