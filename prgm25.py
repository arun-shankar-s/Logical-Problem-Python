import csv
with open("defg.txt","w",newline="") as out:
    field=['Name','Department','Email']
    content=csv.DictWriter(out,fieldnames=field)
    content.writeheader()
    content.writerow({'Name': 'Arun', 'Department': 'MCA','Email': 'arun@gmail.com'})
    content.writerow({'Name': 'Anand', 'Department': 'Btech','Email': 'anand@gmail.com'})

with open("defg.txt","r") as inf:
    content1=csv.DictReader(inf)
    print("\t".join(content1.fieldnames))
    for row in content1:
        print("\t".join([row['Name'],row['Department'],row['Email']]))