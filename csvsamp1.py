import csv

with open('details.csv','r')as csv_readfile:
    csv_reader=csv.reader(csv_readfile)
##to remove the title use generators
    next(csv_reader)
    for lines in csv_reader:
       print(lines[2])#represents index values

#for writing the csv file
    with open('writedetails.csv','w')as csv_writefile:
        csv_writer=csv.writer(csv_writefile,delimiter='+')
    
        for lines in csv_reader:
            csv_writer.writerow(lines)


## for reading file from the write file
with open('writedeatils.csv','r')as csv_readfile:
    csv_reader=csv.reader(csv_readfile,delimiter='+')#to print it as , instead of +
    for lines in csv_reader:
        print(lines)

## Using dict reader
with open('details.csv','r')as csv_readfile:
    csv_reader=csv.DictReader(csv_readfile)
    
#     #writing with dict reader
    with open('dictwritedetails.csv','w')as csv_writefile:
        #it is neccessary to mention the fields
        fieldnames=[ ' Age', ' Height(inches)', ' Position', ' Team', ' Weight(lbs)', 'Name']
        csv_writer=csv.DictWriter(csv_writefile,fieldnames=fieldnames,delimiter='\t')
         #to write the first row in file
        csv_writer.writeheader()
        for lines in csv_reader:
            csv_writer.writerow(lines)