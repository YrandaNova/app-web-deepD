import csv
#file_path="/home/yranda/Documents/Deep_dive/prueba/resumen.csv"
def create_csv(file_path, date, email):
    data=[]
    data.append((date, email) )
       
 
    with open(file_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
"""
date="19 march, 2023"
email="mfcr112000@gmail.com"
create_csv(file_path,date,email)
create_csv(file_path,date,email)
create_csv(file_path,date,email)
"""