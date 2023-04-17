import csv

to_add = []
with open('param.csv', mode='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        to_add.append(lines)

# data rows of csv file 
rows = [ ['Nikhil', 'COE'], 
         ['Sanchit', 'COE'], 
         ['Aditya', 'IT'], 
         ['Sagar', 'SE'], 
         ['Prateek', 'MCE'], 
         ['Sahil', 'EP']] 

for i in rows:
    to_add.append(i)
    
print(to_add)

# name of csv file 
filename = "param.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
            
    # writing the data rows 
    for j in to_add:
        if(j == []):
            continue
        else:
            csvwriter.writerow(j)