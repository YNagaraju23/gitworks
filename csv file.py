import csv
fh=open("test.csv",'w')
fw=csv.writer(fh)
fw.writerow([1,2,3,4])