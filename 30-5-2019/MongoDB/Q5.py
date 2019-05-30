from pymongo import MongoClient
from pprint import pprint

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["dhi_bits_interns"]

dhi_student_attendance = mydb["dhi_student_attendance"]
dhi_degree = mydb["dhi_degree"]
dhi_term_detail = mydb['dhi_term_detail']
dhi_copo_mapping = mydb["dhi_copo_mapping"]
dhi_calendarevents = mydb["dhi_calendarevents"]
dhi_lesson_plan = mydb["dhi_lesson_plan"]
dhi_timetable = mydb["dhi_timetable"]
pms_user_leaves = mydb["pms_user_leaves"]
pms_holiday = mydb["pms_holiday"]
dhi_user = mydb["dhi_user"]
dhi_internal = mydb["dhi_internal"]

# acadYear = input("acadYear: ")
# degree = input("degree: ")
# dept = input("dept: ")
acadYear = "2018-19"
degreeid = "BE"
dept = "EE"

pprint([x for x in mydb.dhi_user.aggregate([
    {
        "$match":
        {
            "academicYear":"2018-19",
            "degreeId":"BE",
            "deptId":"IS"
        }
    },
    {
        "$match":
        {
            "$or":
            [
                {
                    "userType":"TEACHING"
                },
                {
                    "userType":"ADMINISTRATIVE"
                }
            ]        
        }
    },
    {
        "$lookup":
        {
            "from":"dhi_lesson_plan",
            "localField":"academicYear",
            "foreignField":"academicYear",
            "as":"lessonplan"
        }
    },
    {
        "$unwind": "$lessonplan"
    },
    {
        "$unwind":"$lessonplan.faculties"
    },
    {
        "$unwind":"$lessonplan.departments"
    },
    {
        "$unwind":"$lessonplan.plan"
    },
    {
        "$redact":
        {
            "$cond":
            [
                {
                    "$eq":
                        ["$degreeId","$lessonplan.degreeId"]
                        #["$employeeGivenId","$lessonplan.faculties.facultyGivenId"]              

                },
                "$$KEEP",
                "$$PRUNE"
            ]
        }
    },
    {
        "$redact":
        {
            "$cond":
            [
                {
                    "$eq":
                        ["$employeeGivenId","$lessonplan.faculties.facultyGivenId"]              

                },
                "$$KEEP",
                "$$PRUNE"
            ]
        }
    },
    {
        "$redact":
        {
            "$cond":
            [
                {
                    "$eq":
                        ["IS","$lessonplan.departments.deptId"]              

                },
                "$$KEEP",
                "$$PRUNE"
            ]
        }
    },
    {
        "$group":
        {
            '_id':
            {
                "facname":"$lessonplan.faculties.facultyName",
                "date":"$lessonplan.plan.plannedDate"
            },
            "count":{"$sum":1}
        }
    },
    {
        "$group":
        {
            "_id":"$_id.facname",
            "count":{"$sum":1}
        }
    },
])
])
