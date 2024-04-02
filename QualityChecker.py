import csv
import datetime
def myreader(filename:str)->list:
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        return your_list
    

def csvPrinter(fileName:str, foundAlerts):
    with open("./reports/"+fileName, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Row" , "Value In Database ('|' is the seperator for the sub array)" , "Error Type"])

        for i in foundAlerts:
            writer.writerow(toReaderPrinter(i))
    pass

def toReaderPrinter(i:list):
    formattedString = "["
    for c in i[1]:
        formattedString = formattedString + str(c) + " | "
    formattedString = formattedString + "]"
    return [i[0], formattedString, i[2]]

def departmentReport():
    departments = myreader('Department_Information.csv')
    departmentNames = dict()
    departmentid = dict()
    index = 1
    foundAlerts = []
    for i in departments:
        dateString = i[2].split("/")
        if index != 1:
            if  not (i[0] and i[1] and i[2]):
                foundAlerts.append([index, i, "Missing Data"])
            else:
                result = departmentNames.get(i[1])
                if result != None:
                    foundAlerts.append([index,i,"Duplicate Department Name at index " + str(result)])
                result = departmentid.get(i[0])
                if  result != None:
                    foundAlerts.append([index, i, "Duplicate Department ID at index " + str(result)])
                if int(dateString[2])<=1900:
                    foundAlerts.append([index, i, "Date too early"])
                if (int(dateString[1]) < 0 or int(dateString[1]) > 31 or int(dateString[0]) < 0 or int(dateString[0]) >12):
                    foundAlerts.append([index, i, "Invalid Date"])
        departmentNames.update({i[1]:index})
        departmentid.update({i[0]:index})
        index+=1
    csvPrinter("department.csv", foundAlerts)

def studentCouncelingReport():
    students = myreader('Student_Counceling_Information.csv')
    departments = myreader('Department_Information.csv')
    validDepID = []
    foundAlerts = []
    index = 1
    seenStudentIDs = dict()
    for i in departments:
        validDepID.append(i[0])
    for i in students:
        if index != 1:
            if not (i[0] and i[1] and i[2] and i[3] and i[4]):
                foundAlerts.append([index, i, "Missing Values"])
            else:
                if validDepID.count(i[4]) == 0:
                    foundAlerts.append([index, i, "Invalid Admitted Department"])
                if validDepID.count(i[3]) == 0:
                    foundAlerts.append([index, i, "Invalid Requested Department"])
                dateString = i[1].split("/")
                if (int(dateString[1]) < 0 or int(dateString[1]) > 31 or int(dateString[0]) < 0 or int(dateString[0]) >12):
                    foundAlerts.append([index, i, "Invalid Date"])
                dateString = i[2].split("/")
                if (int(dateString[1]) < 0 or int(dateString[1]) > 31 or int(dateString[0]) < 0 or int(dateString[0]) >12):
                    foundAlerts.append([index, i, "Invalid Date"])
                result = seenStudentIDs.get(i[0] + i[3])
                if (result != None):
                    foundAlerts.append([index, i, "Duplicate Student Entry at index " + str(result)])
        seenStudentIDs.update({i[0] + i[3]:index})
        index+=1
        
    csvPrinter("studentCounceling.csv", foundAlerts)

def studentPerformanceReport():
    performance = myreader('Student_Performance_Data.csv')
    students = myreader('Student_Counceling_Information.csv')
    validStudentID = dict()
    seenReports = dict()
    foundAlerts = []
    for i in students:
        validStudentID.update({i[0]:"a"})
    index=1
    
    for i in performance:
        if index != 1:
            if not (i[0] and i[1] and i[2] and i[3] and i[4] and i[5]):
                foundAlerts.append([index, i, "Missing Values"])
            else:
                if int(i[4]) < 0 or int(i[4])>100:
                    foundAlerts.append([index, i, "Invalid Performance"])
                if int(i[5]) < 0:
                    foundAlerts.append([index, i, "Invalid Effort Hours"])
                result = seenReports.get(i[0] + i[2])
                if result != None:
                    foundAlerts.append([index, i, "Duplicate Paper for Student at index " + str(result)])
                if validStudentID.get(i[0]) != "a":
                    foundAlerts.append([index, i, "Student not in System"])
        seenReports.update({i[0] + i[2]: index })
        index+=1
    csvPrinter("studentPreformance.csv", foundAlerts)
    

def employeeReport():
    employees = myreader('Employee_Information.csv')
    departments = myreader('Department_Information.csv')
    validDepID = dict()
    seenEmployeeID = dict()
    foundAlerts = []
    index = 1
    for i in departments:
        validDepID.update({i[0]:"a"})
    for i in employees:
        if index !=1:
            if not (i[0] and i[1] and i[2] and i[3]):
                foundAlerts.append([index, i, "Missing Values"])
                return
            else:
                dateString = i[1].split("/")
                if (int(dateString[1]) < 0 or int(dateString[1]) > 31 or int(dateString[0]) < 0 or int(dateString[0]) >12):
                    foundAlerts.append([index, i, "Invalid Date"])
                dateString = i[2].split("/")
                if (int(dateString[1]) < 0 or int(dateString[1]) > 31 or int(dateString[0]) < 0 or int(dateString[0]) >12):
                    foundAlerts.append([index, i, "Invalid Date"])
                if validDepID.get(i[3]) != "a":
                    foundAlerts.append([index, i, "Invalid Department"])
                result = seenEmployeeID.get(i[0])
                if result != None:
                    foundAlerts.append([index, i, "Duplicate Employee ID at index " + str(result)])
        seenEmployeeID.update({i[0]:index})
        index+=1
    csvPrinter("employee.csv", foundAlerts)

    

studentPerformanceReport()
studentCouncelingReport()
departmentReport()
employeeReport()