from pymongo import MongoClient
from pprint import pprint

myclient = MongoClient('192.168.1.159',27017)
mydb = myclient["dhi_bits_interns"]

dhi_term_detail = mydb["dhi_term_detail"]
dhi_student_attendance_configuration_refactored = mydb["dhi_student_attendance_configuration_refactored"]


pprint(len([x for x in mydb.dhi_term_detail.aggregate([
    {
        "$match":
        {
            "current":True
        }
    },
    {
        "$lookup":
        {
            "from":"dhi_student_attendance_configuration_refactored",
            "localField":"academicYear",
            "foreignField":"academicYear",
            "as":"attendance"
        }
    },
    {
        "$unwind":"$attendance"
    },
    {
        "$unwind":"$attendance.schemeAttendanceConfigurations"
    }
])
]))