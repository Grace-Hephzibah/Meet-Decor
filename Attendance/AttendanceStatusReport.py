import csv

import DB

filename = "Attendance.csv"

fields = []
rows = []
timeLapse = [0 for i in DB.classNames]
tdelta = 1
attendance = [0 for i in DB.classNames]
FMT = '%H:%M:%S'

def constructor():
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)

        for row in csvreader:
            rows.append(row)

    for row in rows:
        TimeLapse(row)

    numRows = csvreader.line_num

    timeStart = rows[0][1]
    timeEnd = rows[numRows - 2][1]
    i = 0

    for duration in timeLapse:

        attendance[i] = AttendanceCheck(duration)
        i = i+1

    csvOverwrite()

def TimeLapse(row):
    name = row[0]
    index = DB.classNames.index(name)
    timeLapse[index] += .25

def AttendanceCheck(duration):
    if (duration >= (0.70*tdelta)):
        return 1
    else:
        return 0

def csvOverwrite():
    Final_fields = ['Name', 'Time', 'Status']

    # data rows of csv file
    Final_rows = [[DB.classNames[i], timeLapse[i], attendance[i]] for i in range(0, len(timeLapse))]
    print(Final_rows)

    # name of csv file
    filename = "main.csv"

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(Final_fields)

        # writing the data rows
        csvwriter.writerows(Final_rows)

print(DB.classNames)

constructor()