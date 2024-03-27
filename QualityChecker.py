import csv
import datetime
def myreader(filename:str)->list:
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        return your_list

def departmentReport():
    departments = myreader('Department_Information.csv')
    departmentNames = []
    departmentid = []
    index = 1
    for i in departments:
        dateString = i[2].split("/")
        
        if departmentNames.count(i[1]) > 0:
            print(index, i, "Dupe Department Name")
        if departmentid.count(i[0]) > 0:
            print(index, i, "Dupe Department ID")
        if  not (i[0] and i[1] and i[2]):
            print(index, i, "Missing Data")
        elif i[2] != "DOE":
            if int(dateString[2])<1900:
                print(index, i, "Date too early")
        departmentNames.append(i[1])
        departmentid.append(i[0])
        index+=1

def studentCouncelingReport():
    students = myreader('Student_Counceling_Information.csv')
    departments = myreader('Department_Information.csv')
    validDepID = []
    for i in departments:
        validDepID.append(i[0])
    index = 1
    for i in students:
        if validDepID.count(i[4]) == 0:
            print(index, i, "Invalid Admitted Department")
        if not (i[0] and i[1] and i[2] and i[3] and i[4]):
            print(index, i, "Missing Values")
        index+=1

def studentPerformanceReport():
    performance = myreader('Student_Performance_Data.csv')
    index=1
    seenReports = dict()
    for i in performance:
        if index != 1:
            if not (i[0] and i[1] and i[2] and i[3] and i[4] and i[5]):
                print(index, i, "Missing Values")
            else:
                if int(i[4]) < 0 or int(i[4])>100:
                    print(index, i, "Invalid Performance")
                if int(i[5]) < 0:
                    print(index, i, "Invalid Effort Hours")
                if seenReports.get(i[0] + i[2]) != None:
                    print(index, i, "Duplicate Paper for student")
        seenReports.update({i[0] + i[2]: "a" })
        index+=1

# studentPerformanceReport()
# studentCouncelingReport()
departmentReport()