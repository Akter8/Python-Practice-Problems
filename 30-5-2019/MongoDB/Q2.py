from pymongo import MongoClient
import datetime
from datetime import timedelta
from pprint import pprint

myclient = MongoClient('192.168.1.159',27017)
mydb = myclient["dhi_bits_interns"]
pms_university_exam = mydb["pms_university_exam"]

#input:
# degreeid = input("DegreeID: ")
# degreebatch = input("DegreeBatch: ")
# acadyear = input("AcademicYear: ")
# scheme = input("Scheme: ")
# courseCode = input("CourseCode: ")
degreeid = "BE"
degreebatch = "REGULAR"
acadyear = "2016-17"
scheme = "Scheme 2010"
courseCode = "10AL61"

l  = ([x for x in mydb.pms_university_exam.aggregate([
    {
        "$unwind":"$terms"
    },
    {
        "$unwind":"$terms.scores"
    },
    {
        "$unwind":"$terms.scores.courseScores"
    },
    {
        "$match":
        {
            "degreeId":degreeid
        }
    },
    {
        "$match":
        {
            "degreeBatch":degreebatch
        }
    },
    {
        "$match":
        {
            "academicYear":acadyear
        }
    },
    {
        "$match":
        {
            "terms.scores.courseScores.courseCode":courseCode
        }   
    },
    {
        "$group":
        {
            '_id':"$terms.scores.courseScores.resultType", "count":{ "$sum":1 }
        }
    }
])])

pprint(l)