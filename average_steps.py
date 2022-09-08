import csv 

infile = open('steps.csv' , 'r')

csvfile = csv.reader(infile)

next(csvfile)

outfile = open('avg_steps.csv' , 'w')
 
for record in csvfile:
    import csv

infile = open('steps.csv', 'r')
csvfile = csv.reader(infile)
next(csvfile)

outfile = open('avg_steps.csv', 'w')

month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
total_steps = 0
counter = 0
month = 1

for record in csvfile:
    if record[0] == str(month):
        total_steps += int(record[1])
        counter += 1
    else:
        avg_steps = format(total_steps/counter, '.2f')
        outfile.write(month_name[int(month)-1] + ', ' + str(avg_steps) + '\n')
        total_steps = int(record[1])
        counter = 1
        month = record[0]

avg_steps = format(total_steps/counter , '.2f')
outfile.write('December,' + avg_steps)       
       
outfile.close

