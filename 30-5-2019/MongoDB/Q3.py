from pymongo import MongoClient
import datetime
from pprint import pprint

myclient = MongoClient('192.168.1.159',27017)
mydb = myclient["dhi_bits_interns"]

dhi_user = mydb["dhi_user"]
dhi_scholarship_and_excess_fee = mydb["dhi_scholarship_and_excess_fee"]

pprint(len([x for x in list(mydb.dhi_user.aggregate([
    {
        "$match":
        {
            "userType":"STUDENT"
        }
    },
    { 
        "$lookup":
        {
            "from":"dhi_scholarship_and_excess_fee",
            "localField":"usn",
            "foreignField":"usn",
            "as":"Scholars"
        }
    },
    {
        "$unwind": "$Scholars"
    },
    {
        "$unwind": "$Scholars.scholarships"
    },
    {
        "$project":
        {
            "Scholars.studentName":1,
            "Scholars.scholarships.grantedAmount":1,
            "_id":0
        }
    }
])
)]))
#print(l)