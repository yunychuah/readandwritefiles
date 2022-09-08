
import csv
    
infile = open('customers.csv' , 'r')

csvfile = csv.reader(infile)

next(csvfile)

counter = 0

outfile = open('customer_country.csv','w')

for record in csvfile:

    outfile.write(record[1] + ' ' + record [2] +', ' + record[4]+'\n')
    
    counter += 1

outfile.write('Total number of customers:' + str(counter))   

outfile.close()


    




                               
  

