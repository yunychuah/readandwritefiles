import csv 

infile = open('employeepay.csv' , 'r')

csvfile = csv.reader(infile)

next(csvfile)

for record in csvfile:
    total_pay = int(record[3]) * (1 + float(record[4]))
    print('ID:' + str(record[0]) + '\nName: ' +record[1] +' ' + record[2]+'\nTotal Pay: $' + format((total_pay) , '.2f'))
    input()