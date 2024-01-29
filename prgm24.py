import csv
with open("defg.csv","w",newline="") as out:
    field=['Name','Department','Email']
    content=csv.DictWriter(out,fieldnames=field)
    content.writeheader()
    content.writerow({'Name': 'Arun', 'Department': 'MCA','Email': 'arun@gmail.com'})
    content.writerow({'Name': 'Anand', 'Department': 'Btech','Email': 'anand@gmail.com'})

with open("defg.csv",newline='')as csvfile:
 data=csv.reader(csvfile,delimiter=' ',quotechar='|')
 for row in data:
    print(','.join(row))