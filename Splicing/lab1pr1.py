#string splicing

social = input("Please enter SSN: ")

if len(social) == 9:  
    new_ssn = social[0:3] + "-" + social[3:5] + "-" + social[5:9]
    print(new_ssn)
else:
    print("Incorrect SSN length.")
