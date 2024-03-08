import os
import random
import csv

def gen_PESEL():
    year = random.randint(0, 99)
    month = random.randint(1, 12)
    if month in [1, 3, 5, 7, 8, 10, 12]:    #months with 31 days
        day = random.randint(1,31)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30) #months with 30 days
    else:   #Luty
        day = random.randint(1, 28)

    random_digits = [random.randint(0, 9) for _ in range(4)]
    cont = random.randint(1,9)
    pesel = '{:02d}{:02d}{:02d}{}{}'.format(year, month, day, "".join(map(str, random_digits)), cont)
    return pesel

def last_num_check(pesel):
    weighs = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    c_sum = 0
    for i in range(10):
        c_sum += weighs[i] * int(pesel[i])
    c_digit = (10 - (c_sum % 10)) % 10
    return c_digit == int(pesel[10])



with open("PESEL.txt", "w") as file:    #save 50 random PESELs to file
    for i in range(100):
        file.write(gen_PESEL() + "\n")


with open("PESEL.txt", "r") as file:    #read pesels
    pesels = file.readlines()


#checking last number

with open("PESEL.csv", "w", newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["PESEL", "Data Urodzenia", "Gender"])


results = []
for p in pesels:
    if last_num_check(p):   #last number correct
        year = str(p[0:2])
        month = str(p[2:4])
        day = str(p[4:6])
        gender = int(p[9]) % 2
        if gender == 0:
            gender = "f"
        else:
            gender = "m"
        result = ';'.join([p.strip(), f"{day}-{month}-{year}", gender])
        print(result)
        results.append(result)
        
        with open("PESEL.csv", "a", newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(results)
    