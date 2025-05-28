import csv # importing the csv module.
 
# csv file path
filename = "addresses.csv.py"
#opening the csvfile in traditional way
csvfile=open(filename,'r')
 
# initializing the titles and rows list
fields = []
rows = []
 
# reading CSV file
# creating a CSV reader object
csvreader = csv.reader(csvfile)
#this object is our go-to for every change in the
# we will just interact with it.
# csvreader is an iterator it has the data in the form of rows
# a next is called on it, then it goes to the next row.
# so the first row will have fields, and correspondingly we can
# go for next.
 
# extracting field names through first row
fields = next(csvreader)
# next function returns the current row and
#advances the row to the next.
 
 
# extracting each data row one by one
# in for loop next is automatically called for
# an iterator.
for row in csvreader:
        rows.append(row)
 
# get total number of rows
print("Total no. of rows: %d"%(csvreader.line_num))
 
# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
 
# printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print(col,end=" ")
    print('\n')