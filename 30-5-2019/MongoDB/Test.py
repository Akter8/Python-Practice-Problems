from pymongo import MongoClient
import datetime
from datetime import timedelta
from pprint import pprint

myclient = MongoClient('192.168.1.159',27017)
mydb = myclient["dhi_pace_02-05-19_admin"]
#mycol = mydb["dhi_student_attendance"]

year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
date1 = datetime.datetime(year, month, day)-timedelta(hours=5,minutes=30)
print(date1)
dhi_student_attendance = mydb["dhi_student_attendance"]
# count = 0
# for x in attendance.find():
#     students = x["students"]
#     for y in students:
#         studentA = y["studentAttendance"]
#         for z in studentA:
#             if z["date"] == date1 and z["present"] == False:
#                 #print(y["studentName"],x["courseName"])
#                 count += 1
# print(count)

pprint(len(set([x["name"] for x in mydb.dhi_student_attendance.aggregate([
    {
        '$unwind':'$students'
    },
    {
        '$unwind':'$students.studentAttendance'
    },
    {
        "$match":
        {
            "students.studentAttendance.present":False
        }
    },
    {
        "$match":
        {
            "students.studentAttendance.date":date1
        }
    },
    {
        "$project":
        {
            "name":"$students.studentName", "_id":0
        }
    }
])
])))

