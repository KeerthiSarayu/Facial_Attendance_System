import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("FaceRecognition.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': ""
})

ref = db.reference('Students')

data = {
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 1,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "123456":
        {
            "name": "Sarayu",
            "major": IT",
            "starting_year": 2022,
            "total_attendance": 1,
            "standing": "A",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:52:13"
        },
    "654321":
        {
            "name": "Sowkya",
            "major": "Maths",
            "starting_year": 2021,
            "total_attendance": 1,
            "standing": "B",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
