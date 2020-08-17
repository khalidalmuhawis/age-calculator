from datetime import datetime

def check_birthdate(year, month, day):
    date1 = datetime(year, month, day)
    date2 = datetime.now()
    return date2 > date1

def calculate_age(year, month, day):
    birthday = datetime(year, month, day)
    age = datetime.now() - birthday
    print("Age: %s"%(age.days/365))

def main():
    year = int(input("Year: "))
    month = int(input("Month: "))
    day = int(input("Day: "))

    if check_birthdate(year, month, day):
        calculate_age(year, month, day)
    else:
        print("Invalid Birthdate")



if __name__ == '__main__':
    main()
